import pymupdf
import re
import json

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

questions = []
current_section = "Unknown"

# Let's iterate page by page and parse questions
# In DigiALM, each question has:
# Q.<number>
# <Question text>
# Ans
# A. ... / B. ... / C. ... / D. ...
# Question ID : <qid>
# Option 1 ID : ...
# ...
# Status : Answered / Not Answered / Marked For Review
# Chosen Option : A/B/C/D / --

# Let's write a robust page-by-page span collector
all_pages_data = []

for pno in range(len(doc)):
    page = doc[pno]
    blocks = page.get_text("dict")["blocks"]
    page_spans = []
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    txt = s["text"].strip()
                    if txt:
                        page_spans.append({
                            "text": txt,
                            "color": s["color"],
                            "hex_color": hex(s["color"]),
                            "font": s["font"],
                            "size": s["size"],
                            "bbox": s["bbox"]
                        })
    all_pages_data.append(page_spans)

# Let's parse all questions across all pages
# Track current section
current_section = "Part 1 General Knowledge Awareness"

# Let's combine all spans sequentially but track section headers
full_stream = []
for pno, spans in enumerate(all_pages_data):
    for s in spans:
        s["page"] = pno + 1
        full_stream.append(s)

# Find question start indexes
q_indices = []
for i, s in enumerate(full_stream):
    txt = s["text"]
    if re.match(r'^Q\.\d+$', txt):
        q_indices.append(i)

print(f"Total Question markers found: {len(q_indices)}")

parsed_questions = []

for idx, q_start in enumerate(q_indices):
    q_end = q_indices[idx + 1] if idx + 1 < len(q_indices) else len(full_stream)
    q_spans = full_stream[q_start:q_end]
    
    q_num_str = q_spans[0]["text"]
    q_num = int(q_num_str.replace("Q.", ""))
    
    # Check if a section header appeared before this question or within its spans
    # Scan backward from q_start to see if a section header was set
    for s in full_stream[:q_start]:
        if "Section :" in s["text"]:
            # find next span
            s_idx = full_stream.index(s)
            sec_name = s["text"].replace("Section :", "").strip()
            if not sec_name and s_idx + 1 < len(full_stream):
                sec_name = full_stream[s_idx + 1]["text"].strip()
            if sec_name:
                current_section = sec_name
    
    # Also check if section header is right above or inside q_spans
    for s in q_spans:
        if "Section :" in s["text"]:
            s_idx = full_stream.index(s)
            sec_name = s["text"].replace("Section :", "").strip()
            if not sec_name and s_idx + 1 < len(full_stream):
                sec_name = full_stream[s_idx + 1]["text"].strip()
            if sec_name:
                current_section = sec_name

    # Extract Question text, options, Question ID, Status, Chosen Option, Correct Option
    q_id = None
    status = "Unknown"
    chosen_opt = None
    correct_opt = None
    
    # Find options
    options = {}
    
    # Scan spans
    for i_s, s in enumerate(q_spans):
        txt = s["text"]
        
        # Check for Question ID
        if txt == "Question ID :" or "Question ID :" in txt:
            if i_s + 1 < len(q_spans) and re.match(r'^\d+$', q_spans[i_s+1]["text"]):
                q_id = q_spans[i_s+1]["text"]
        
        # Check Status
        if txt == "Status :" or "Status :" in txt:
            if i_s + 1 < len(q_spans):
                status = q_spans[i_s+1]["text"]
        
        # Check Chosen Option
        if txt == "Chosen Option :" or "Chosen Option :" in txt:
            if i_s + 1 < len(q_spans):
                chosen_opt = q_spans[i_s+1]["text"]
        
        # Check Option spans A., B., C., D. or 1., 2., 3., 4.
        m = re.match(r'^([A-D])\.\s*(.*)', txt)
        if m:
            opt_letter = m.group(1)
            opt_text = m.group(2)
            is_green = (s["color"] == 4245067 or s["hex_color"] == "0x40c64b")
            options[opt_letter] = {
                "text": opt_text,
                "color": s["color"],
                "is_green": is_green
            }
            if is_green:
                correct_opt = opt_letter

    # Sometimes green color is on the option letter or text
    # Let's check if any option had green color
    if not correct_opt:
        for opt_letter, opt_data in options.items():
            if opt_data["is_green"]:
                correct_opt = opt_letter
                break

    parsed_questions.append({
        "q_num": q_num,
        "section": current_section,
        "q_id": q_id,
        "status": status,
        "chosen_opt": chosen_opt,
        "correct_opt": correct_opt,
        "options": {k: v["text"] for k, v in options.items()},
        "is_correct": (chosen_opt == correct_opt) if (chosen_opt and correct_opt and chosen_opt in ['A','B','C','D','1','2','3','4']) else False,
        "is_attempted": chosen_opt in ['A','B','C','D','1','2','3','4'] and chosen_opt != '--'
    })

print(f"Parsed {len(parsed_questions)} questions.")

# Let's verify questions missing correct_opt or chosen_opt
missing_correct = [q for q in parsed_questions if not q["correct_opt"]]
print(f"Questions missing correct option: {len(missing_correct)}")
if missing_correct:
    for q in missing_correct[:10]:
        print(f"  Q.{q['q_num']} on Section {q['section']}: q_id={q['q_id']}, status={q['status']}, chosen={q['chosen_opt']}")

# Summary by section
sections_summary = {}
for q in parsed_questions:
    sec = q["section"]
    if sec not in sections_summary:
        sections_summary[sec] = {
            "total": 0,
            "attempted": 0,
            "correct": 0,
            "incorrect": 0,
            "unattempted": 0,
            "questions": []
        }
    
    sections_summary[sec]["total"] += 1
    sections_summary[sec]["questions"].append(q)
    if q["is_attempted"]:
        sections_summary[sec]["attempted"] += 1
        if q["is_correct"]:
            sections_summary[sec]["correct"] += 1
        else:
            sections_summary[sec]["incorrect"] += 1
    else:
        sections_summary[sec]["unattempted"] += 1

print("\n" + "="*80)
print(f"{'SECTION':<40} | {'TOTAL':<5} | {'ATTEMPT':<7} | {'CORRECT':<7} | {'WRONG':<5} | {'MARKS':<5}")
print("="*80)

total_marks = 0
total_attempted = 0
total_correct = 0
total_wrong = 0
total_unattempted = 0
total_q = 0

for sec, data in sections_summary.items():
    marks = data["correct"]  # In CIL, +1 for correct, 0 for wrong/unattempted
    total_marks += marks
    total_attempted += data["attempted"]
    total_correct += data["correct"]
    total_wrong += data["incorrect"]
    total_unattempted += data["unattempted"]
    total_q += data["total"]
    print(f"{sec:<40} | {data['total']:<5} | {data['attempted']:<7} | {data['correct']:<7} | {data['incorrect']:<5} | {marks:<5}")

print("="*80)
print(f"{'TOTAL':<40} | {total_q:<5} | {total_attempted:<7} | {total_correct:<7} | {total_wrong:<5} | {total_marks:<5}")
print("="*80)
