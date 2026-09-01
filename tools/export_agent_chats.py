import os
import sys
import sqlite3
import json
import re
import datetime

def sanitize_filename(name):
    # Remove characters invalid in Windows filenames
    s = re.sub(r'[\\/*?:"<>|]', '', name)
    s = re.sub(r'[\s_]+', '_', s).strip('_')
    return s[:60] if s else 'Untitled'

def main():
    output_dir = os.path.abspath('AgentChats')
    os.makedirs(output_dir, exist_ok=True)
    
    gdb = r'c:\Users\agupt1\AppData\Roaming\Cursor\User\globalStorage\state.vscdb'
    if not os.path.exists(gdb):
        print(f"Error: Database not found at {gdb}")
        return

    conn = sqlite3.connect(gdb)
    cur = conn.cursor()

    cur.execute('SELECT composerId, workspaceId, value FROM composerHeaders')
    all_headers = cur.fetchall()

    target_composers = []
    seen_ids = set()

    for cid, wid, val_str in all_headers:
        if cid in seen_ids:
            continue
        val = json.loads(val_str)
        is_target = False
        if wid in ['f19f57fb8ad35f5f072ce9503f738d6d', '2f1ea2587242941d3f27587ba58a6dad']:
            is_target = True
        elif 'psu-prep-brain' in val_str or 'Resume-Berkadia' in val_str or 'CoalIndiaLimited' in val_str:
            is_target = True

        if is_target:
            seen_ids.add(cid)
            target_composers.append((cid, wid, val))

    # Sort target composers chronologically by lastUpdatedAt (or createdAt)
    target_composers.sort(key=lambda x: x[2].get('lastUpdatedAt') or x[2].get('createdAt') or 0, reverse=True)

    catalog = []
    exported_count = 0

    for cid, wid, val in target_composers:
        raw_name = val.get('name') or val.get('title')
        subtitle = val.get('subtitle') or ''
        created_ts = val.get('createdAt', 0)
        updated_ts = val.get('lastUpdatedAt', 0)
        
        created_dt = datetime.datetime.fromtimestamp(created_ts/1000).strftime('%Y-%m-%d %H:%M:%S') if created_ts else 'N/A'
        updated_dt = datetime.datetime.fromtimestamp(updated_ts/1000).strftime('%Y-%m-%d %H:%M:%S') if updated_ts else 'N/A'
        date_prefix = datetime.datetime.fromtimestamp((updated_ts or created_ts or 0)/1000).strftime('%Y-%m-%d') if (updated_ts or created_ts) else '2026-00-00'

        # Fetch composerData from cursorDiskKV
        cur.execute('SELECT [value] FROM cursorDiskKV WHERE [key] = ?', (f'composerData:{cid}',))
        crow = cur.fetchone()
        
        cdata = {}
        if crow:
            try:
                cdata = json.loads(crow[0])
            except Exception:
                pass
        
        display_title = raw_name or cdata.get('name') or cdata.get('title') or (subtitle[:40] if subtitle else 'Draft Chat')
        if not display_title:
            display_title = 'Untitled Session'

        headers_list = cdata.get('fullConversationHeadersOnly', [])
        
        # If headers_list is empty, also check if conversation array exists or check bubbles directly
        bubbles = []
        if headers_list:
            for h in headers_list:
                bid = h.get('bubbleId')
                btype = h.get('type') # 1 = User, 2 = Assistant
                if not bid:
                    continue
                cur.execute('SELECT [value] FROM cursorDiskKV WHERE [key] = ?', (f'bubbleId:{cid}:{bid}',))
                brow = cur.fetchone()
                if brow:
                    try:
                        bdata = json.loads(brow[0])
                        bubbles.append((btype, bdata))
                    except Exception:
                        pass
        else:
            # Check conversation in cdata
            conv = cdata.get('conversation', [])
            for item in conv:
                btype = item.get('type')
                bid = item.get('bubbleId')
                if bid:
                    cur.execute('SELECT [value] FROM cursorDiskKV WHERE [key] = ?', (f'bubbleId:{cid}:{bid}',))
                    brow = cur.fetchone()
                    if brow:
                        try:
                            bdata = json.loads(brow[0])
                            bubbles.append((btype, bdata))
                            continue
                        except Exception:
                            pass
                if 'text' in item:
                    bubbles.append((btype, item))

        # Filter out completely empty sessions (e.g. 0 bubbles with no text)
        has_content = False
        for btype, bdata in bubbles:
            text = bdata.get('text', '').strip()
            if text:
                has_content = True
                break
        
        # If no bubbles from database, check if a jsonl transcript file exists
        if not has_content:
            transcript_path = os.path.join(
                os.path.expanduser('~'),
                r'.cursor\projects\c-Users-agupt1-Projects-Personal-psu-prep-brain\agent-transcripts',
                cid,
                f'{cid}.jsonl'
            )
            if os.path.exists(transcript_path):
                try:
                    with open(transcript_path, 'r', encoding='utf-8') as tf:
                        for line in tf:
                            line = line.strip()
                            if line:
                                ev = json.loads(line)
                                msg = ev.get('message', {})
                                role = msg.get('role')
                                content = msg.get('content', '')
                                if content:
                                    has_content = True
                                    btype = 1 if role == 'user' else 2
                                    bubbles.append((btype, {'text': content, 'role': role}))
                except Exception:
                    pass

        if not has_content and not subtitle:
            # Skip empty placeholder sessions
            continue

        safe_title = sanitize_filename(display_title)
        filename = f"{date_prefix}_{safe_title}_{cid[:8]}.md"
        filepath = os.path.join(output_dir, filename)

        # Build Markdown content
        md_lines = []
        md_lines.append(f"# {display_title}")
        md_lines.append("")
        md_lines.append("| Metadata | Value |")
        md_lines.append("| :--- | :--- |")
        md_lines.append(f"| **Chat ID** | `{cid}` |")
        md_lines.append(f"| **Created At** | `{created_dt}` |")
        md_lines.append(f"| **Last Updated At** | `{updated_dt}` |")
        if subtitle:
            md_lines.append(f"| **Files Touched / Summary** | {subtitle} |")
        model = cdata.get('modelConfig', {}).get('modelName') or val.get('model')
        if model:
            md_lines.append(f"| **Model** | `{model}` |")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

        turn_count = 0
        user_turn_count = 0

        for btype, bdata in bubbles:
            text = bdata.get('text', '').strip()
            if not text:
                continue
            
            turn_count += 1
            if btype == 1:
                user_turn_count += 1
                md_lines.append(f"## 👤 User Message #{user_turn_count}")
                md_lines.append("")
                # Clean prompt text if needed
                md_lines.append(text)
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
            else:
                md_lines.append(f"## 🤖 Assistant Response")
                md_lines.append("")
                
                # Check for thinking blocks
                thinking = bdata.get('allThinkingBlocks') or bdata.get('thinking')
                if thinking and isinstance(thinking, list) and len(thinking) > 0:
                    think_text = "\n".join([str(t) for t in thinking if str(t).strip()])
                    if think_text:
                        md_lines.append("<details>")
                        md_lines.append("<summary>💭 Thought Process</summary>")
                        md_lines.append("")
                        md_lines.append(think_text)
                        md_lines.append("")
                        md_lines.append("</details>")
                        md_lines.append("")

                md_lines.append(text)
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_lines))

        exported_count += 1
        catalog.append({
            'title': display_title,
            'filename': filename,
            'cid': cid,
            'updated_dt': updated_dt,
            'turns': turn_count,
            'user_turns': user_turn_count,
            'subtitle': subtitle
        })
        print(f"Exported [{cid[:8]}] {display_title} -> {filename} ({turn_count} turns)")

    # Build AgentChats/README.md catalog
    readme_lines = []
    readme_lines.append("# 💬 Agent Chats Archive")
    readme_lines.append("")
    readme_lines.append("Complete, searchable markdown archive of all Cursor agent and assistant chat conversations for the `psu-prep-brain` preparation complex.")
    readme_lines.append("")
    readme_lines.append(f"**Total Archived Sessions:** {len(catalog)}  ")
    readme_lines.append(f"**Archive Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")
    readme_lines.append("## 📑 Master Index of Chats")
    readme_lines.append("")
    readme_lines.append("| Date & Time | Chat Title | Turns | Summary / Artifacts | File Link |")
    readme_lines.append("| :--- | :--- | :--- | :--- | :--- |")

    for item in catalog:
        f_link = f"[{item['filename']}]({item['filename']})"
        sub_desc = item['subtitle'] if item['subtitle'] else "—"
        readme_lines.append(f"| `{item['updated_dt']}` | **{item['title']}** | {item['turns']} | {sub_desc} | {f_link} |")

    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")
    readme_lines.append("## 📌 Key Sessions by Category")
    readme_lines.append("")
    readme_lines.append("### 🌟 Pinned & Milestone Sessions")
    c18_file = next((item['filename'] for item in catalog if 'c18155ee' in item['filename']), '2026-09-01_Gemini_18_July_CURRENT_Context_gathering_for_project_referen_c18155ee.md')
    p12_file = next((item['filename'] for item in catalog if '789eb95e' in item['filename']), '2026-08-31_Paper_1_&_2_study_plan_789eb95e.md')
    readme_lines.append(f"- [Gemini 18 July / Current Context & Resume Sync]({c18_file}) — Multi-month master preparation brain, Form-Filling dossier, and Berkadia/STMicro resume synchronization.")
    readme_lines.append("- [Claude 18 July / Resignation & HR Proofs](2026-07-18_Claude18_July_CURRENT_Context_gathering_for_project_referenc_1dc9fa49.md) — Exit documentation, resignation email drafting, and statutory paperwork.")
    readme_lines.append("- [MSTC Final Interview Preparation](2026-05-18_MSTC_final_interview_preparation_8fa780d3.md) — Technical CS question bank, HR behavioral responses, and comprehensive interview battle-plan.")
    readme_lines.append("- [CBT 1 Notes Extension](2026-08-01_CBT_1_notes_extension_28f28463.md) — IFFCO CBT 1 paper review, DBMS, Security, and OS note consolidation.")
    readme_lines.append("")
    readme_lines.append("### 🧪 Exam Mark Audits & Analysis")
    readme_lines.append("- [PDF Assessment Marks Review (Part 1)](2026-08-30_PDF_assessment_marks_review_1faed7ac.md) — Response sheet parsing, raw score calculation scripts (`calc_raw_marks.mjs`), and 147/200 marks breakdown.")
    readme_lines.append("- [PDF Assessment Marks Review (Part 2)](2026-08-30_PDF_assessment_marks_review_aabf26db.md) — HTML/PDF answer key extraction and score verification.")
    readme_lines.append("")
    readme_lines.append("### 🛠 Infrastructure, Setup & System Specs")
    readme_lines.append("- [Docker and App Clutter Cleanup](2026-08-25_Docker_and_app_clutter_0c667055.md) — WSL2 compaction, Docker cleanup, and memory optimization.")
    readme_lines.append("- [Automatic Push Rules for Main Branch](2026-06-14_Automatic_push_rules_for_main_branch_21564636.md) — Git hooks, brain-sync automation, and `.cursor/rules` configurations.")
    readme_lines.append(f"- [Paper 1 & 2 Study Plan (Coal India)]({p12_file}) — DBMS, Relational Model, and Paper 1 non-tech planning.")

    readme_path = os.path.join(output_dir, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(readme_lines))

    print(f"\nGenerated AgentChats/README.md master catalog with {len(catalog)} entries.")

if __name__ == '__main__':
    main()
