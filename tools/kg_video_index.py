#!/usr/bin/env python3
"""
KG Video Index Builder
----------------------
Pulls the COMPLETE granular curriculum (module -> topic -> subtopic -> lesson/video
with durations, PYQ counts, practice counts) from KnowledgeGate's public
course-content API for every owned course, and writes:

  1. IOCL/KG-VIDEO-INDEX.md   -- compact human-readable index (grep-friendly)
  2. tools/kg-index.json      -- machine-readable tree for precise question->video lookup

Usage:  python3 tools/kg_video_index.py
"""

import json
import os
import time
import urllib.request

API = "https://api.knowledgegate.ai/api/v1/course-content/public"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"Accept": "application/json", "User-Agent": "Mozilla/5.0"}

COURSES = [
    ("IOCL-ENGINEERS-OFFICERS-GRADE-A-PAPER-2", "IOCL Paper-2 (CS/IT)", "IOCL"),
    ("IOCL-ENGINEERS-OFFICER-GRADE-A-PAPER-1", "IOCL Paper-1 (Aptitude)", "IOCL"),
    ("COAL-INDIA-MANAGEMENT-TRAINEE", "CIL MT (CS) superset", "CIL"),
    ("IOCL-ENGINEERSOFFICERS-GRADE-A-CS-PAPER-2-TEST-SERIES", "IOCL P2 Test Series", "IOCL"),
    ("IOCL-ENGINEERSOFFICERS-GRADE-A-GENERAL-APTITUDE-PAPER-1-TEST-SERIES", "IOCL P1 Test Series", "IOCL"),
]


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode())
        except Exception as e:                     # noqa: BLE001
            if i == tries - 1:
                print(f"    !! FAILED {url}: {e}")
                return None
            time.sleep(1.5 * (i + 1))
    return None


def mins(sec):
    try:
        s = float(sec)
    except (TypeError, ValueError):
        return ""
    if s <= 0:
        return ""
    return f"{round(s / 60)}m" if s < 3600 else f"{s / 3600:.1f}h"


def walk(items, out, path):
    """Flatten the module tree into rows."""
    for it in items or []:
        typ = it.get("itemType") or it.get("type") or ""
        title = (it.get("title") or "").strip()
        kids = it.get("items") or it.get("lessons") or it.get("children") or []

        if typ == "topic":
            out.append({"k": "topic", "path": path + [title], "title": title})
            walk(kids, out, path + [title])
        elif typ == "subtopic":
            out.append({"k": "subtopic", "path": path + [title], "title": title})
            walk(kids, out, path + [title])
        elif typ == "lesson":
            row = {
                "k": "lesson",
                "path": path[:],
                "title": title,
                "lessonType": it.get("lessonType") or it.get("type") or "",
                "dur": mins(it.get("durationSeconds")),
                "secs": float(it.get("durationSeconds") or 0),
                "qs": it.get("questionCount") or it.get("practiceCount") or 0,
                "solutionSecs": float(it.get("videoSolutionDurationSeconds") or 0),
                "slug": it.get("slug") or "",
            }
            out.append(row)
        else:
            walk(kids, out, path)


def main():
    index = {}
    lines = []

    lines.append("# KnowledgeGate — COMPLETE Granular Video Index")
    lines.append("")
    lines.append("> **Auto-generated** by `tools/kg_video_index.py` (API: `api.knowledgegate.ai/api/v1/course-content/public`).")
    lines.append("> **Purpose:** when a question can't be solved, look up the exact topic → subtopic → video below.")
    lines.append("> Companion: `tools/kg-index.json` (machine-readable, for precise lookups).")
    lines.append("> See also: `IOCL/KG-COURSE-INVENTORY-19SEPT.md` (course-level stats) · `IOCL/SYLLABUS.md` (official pattern).")
    lines.append("")
    lines.append("**How to read a row:** `SUBTOPIC — video (dur) [PQ n] · video (dur) [PYQ n]`")
    lines.append("Where `[PQ]` = practice questions in that lesson, `[PYQ]` = previous-year questions.")
    lines.append("")
    lines.append("---")
    lines.append("")

    grand = {"videos": 0, "hours": 0.0, "pyq": 0, "pq": 0}

    for slug, label, group in COURSES:
        print(f"== {label} ({slug})")
        summ = get(f"{API}/{slug}/summary")
        if not summ or not summ.get("success"):
            lines.append(f"## {label} — ⚠️ summary unavailable\n")
            continue
        d = summ["data"]
        db = d.get("durationBreakdown", {})
        cv = db.get("conceptVideos", {})
        ci = d.get("courseInfo", {})
        mods = sorted(d.get("moduleSummaries", []), key=lambda x: x.get("order", 0))

        vids = cv.get("count", 0)
        hrs = round(cv.get("durationSeconds", 0) / 3600, 1)
        pyq = d.get("totalPyqQuestions", 0)
        pq = db.get("practiceQuestions", {}).get("count", 0)
        grand["videos"] += vids
        grand["hours"] += hrs
        grand["pyq"] += pyq
        grand["pq"] += pq

        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"`{ci.get('canonicalUrl','')}` · **{vids} videos / {hrs}h** · {pyq} PYQs · {pq} PQs · "
                     f"{d.get('totalSubtopics',0)} subtopics · {db.get('tests',{}).get('count',0)} tests · "
                     f"{db.get('notes',{}).get('count',0)} notes")
        lines.append("")

        course_index = {"label": label, "slug": slug,
                        "stats": {"videos": vids, "hours": hrs, "pyq": pyq, "pq": pq},
                        "modules": []}

        for m in mods:
            mslug = m.get("slug")
            if m.get("conceptVideoCount", 0) == 0 and m.get("testCount", 0) == 0 and m.get("lessonCount", 0) == 0:
                continue
            detail = get(f"{API}/{slug}/modules/{mslug}")
            if not detail or not detail.get("success"):
                continue
            md = detail["data"]
            rows = []
            walk(md.get("module", {}).get("items", []), rows, [])

            mod_videos = [r for r in rows if r["k"] == "lesson" and r["dur"]]
            mod_index = {"module": md["module"]["title"], "slug": mslug,
                         "videos": m.get("conceptVideoCount", 0),
                         "pyq": m.get("pyqCount", 0), "topics": []}

            lines.append(f"### {m.get('order','')}. {md['module']['title']} "
                         f"— {m.get('conceptVideoCount',0)} vids · {mins(m.get('durationSeconds'))} · "
                         f"{m.get('pyqCount',0)} PYQs · {m.get('practiceCount',0)} PQs")
            lines.append("")

            cur_topic = None
            cur_sub = None
            for r in rows:
                if r["k"] == "topic":
                    cur_topic = r["title"]
                    cur_sub = None
                    mod_index["topics"].append({"topic": cur_topic, "subtopics": []})
                    lines.append(f"- **{cur_topic}**")
                elif r["k"] == "subtopic":
                    cur_sub = r["title"]
                    if mod_index["topics"]:
                        mod_index["topics"][-1]["subtopics"].append({"subtopic": cur_sub, "videos": [], "pyq": 0, "pq": 0})
                    lines.append(f"  - *{cur_sub}*")
                elif r["k"] == "lesson":
                    lt = (r["lessonType"] or "").lower()
                    if lt in ("pyq", "pyq-collection"):
                        if mod_index["topics"] and mod_index["topics"][-1]["subtopics"]:
                            mod_index["topics"][-1]["subtopics"][-1]["pyq"] = r["qs"]
                        lines.append(f"      · PYQ ×{r['qs']}")
                    elif lt in ("practice", "practice-collection"):
                        if mod_index["topics"] and mod_index["topics"][-1]["subtopics"]:
                            mod_index["topics"][-1]["subtopics"][-1]["pq"] = r["qs"]
                        lines.append(f"      · PQ ×{r['qs']}")
                    elif r["dur"]:
                        if mod_index["topics"] and mod_index["topics"][-1]["subtopics"]:
                            mod_index["topics"][-1]["subtopics"][-1]["videos"].append(
                                {"title": r["title"], "dur": r["dur"], "secs": r["secs"]})
                        lines.append(f"      · {r['title']} ({r['dur']})")
            lines.append("")
            course_index["modules"].append(mod_index)

        index[slug] = course_index
        lines.append("---")
        lines.append("")

    lines.insert(9, f"**Coverage:** {grand['videos']} concept videos · {grand['hours']:.0f}h · "
                    f"{grand['pyq']} PYQs · {grand['pq']} practice questions across 5 owned courses.")
    lines.insert(10, "")

    out_md = os.path.join(ROOT, "IOCL", "KG-VIDEO-INDEX.md")
    out_json = os.path.join(ROOT, "tools", "kg-index.json")
    os.makedirs(os.path.dirname(out_json), exist_ok=True)

    with open(out_md, "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(out_json, "w") as f:
        json.dump(index, f, indent=1)

    print(f"\nWROTE {out_md}  ({os.path.getsize(out_md)/1024:.0f} KB)")
    print(f"WROTE {out_json}  ({os.path.getsize(out_json)/1024:.0f} KB)")
    print(f"TOTAL: {grand['videos']} videos · {grand['hours']:.0f}h · {grand['pyq']} PYQs · {grand['pq']} PQs")


if __name__ == "__main__":
    main()
