import pymupdf
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

section_starts = [
    (1, 329.0, "Part 1 General Knowledge Awareness"),
    (9, 624.0, "Part 2 Numerical Ability"),
    (19, 458.0, "Part 3 Reasoning"),
    (32, 328.0, "Part 4 General English"),
    (43, 440.0, "Part 5 Domain Knowledge"),
]

def get_section_for(page_num, y_coord):
    sec_name = "Part 1 General Knowledge Awareness"
    for p, y, name in section_starts:
        if page_num > p or (page_num == p and y_coord >= y):
            sec_name = name
    return sec_name

global_spans = []
for pno in range(len(doc)):
    page_num = pno + 1
    page = doc[pno]
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    txt = s["text"].strip()
                    if txt:
                        global_spans.append({
                            "text": txt,
                            "color": s["color"],
                            "hex_color": hex(s["color"]),
                            "font": s["font"],
                            "size": s["size"],
                            "bbox": s["bbox"],
                            "page": page_num
                        })

q_starts = []
for idx, s in enumerate(global_spans):
    if re.match(r'^Q\.\d+$', s["text"]):
        q_starts.append((idx, s))

all_parsed_questions = []

for i, (start_idx, q_header) in enumerate(q_starts):
    end_idx = q_starts[i+1][0] if i+1 < len(q_starts) else len(global_spans)
    q_spans = global_spans[start_idx:end_idx]
    
    q_num = int(q_header["text"].replace("Q.", ""))
    q_page = q_header["page"]
    q_y = q_header["bbox"][1]
    sec = get_section_for(q_page, q_y)
    
    q_id = None
    status = None
    chosen_opt = None
    correct_opt = None
    options = {}
    
    for s_idx, s in enumerate(q_spans):
        txt = s["text"]
        if "Question ID :" in txt:
            if s_idx + 1 < len(q_spans) and re.match(r'^\d+$', q_spans[s_idx+1]["text"]):
                q_id = q_spans[s_idx+1]["text"]
        if "Status :" in txt:
            if s_idx + 1 < len(q_spans):
                status = q_spans[s_idx+1]["text"]
        if "Chosen Option :" in txt:
            if s_idx + 1 < len(q_spans):
                chosen_opt = q_spans[s_idx+1]["text"]
        m = re.match(r'^([A-D1-4])\.\s*(.*)', txt)
        if m:
            opt_letter = m.group(1)
            # Map 1->A, 2->B, 3->C, 4->D if numeric
            num_to_letter = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}
            std_opt = num_to_letter.get(opt_letter, opt_letter)
            opt_txt = m.group(2)
            is_green = (s["color"] == 4245067 or s["hex_color"] == "0x40c64b")
            options[std_opt] = opt_txt
            if is_green:
                correct_opt = std_opt

    if not correct_opt:
        for s in q_spans:
            if s["color"] == 4245067 or s["hex_color"] == "0x40c64b":
                m = re.match(r'^([A-D1-4])\.', s["text"])
                if m:
                    opt_letter = m.group(1)
                    num_to_letter = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}
                    correct_opt = num_to_letter.get(opt_letter, opt_letter)

    # Standardize chosen_opt
    num_to_letter = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}
    std_chosen = num_to_letter.get(chosen_opt, chosen_opt)

    is_attempted = (std_chosen is not None and std_chosen in ['A','B','C','D'] and std_chosen != '--')
    is_correct = (is_attempted and std_chosen == correct_opt)
    
    all_parsed_questions.append({
        "index": i + 1,
        "q_num": q_num,
        "section": sec,
        "page": q_page,
        "q_id": q_id,
        "status": status,
        "chosen_opt": std_chosen,
        "correct_opt": correct_opt,
        "is_attempted": is_attempted,
        "is_correct": is_correct
    })

# Let's inspect wrong questions per section
for sec_name in ["Part 1 General Knowledge Awareness", "Part 2 Numerical Ability", "Part 3 Reasoning", "Part 4 General English", "Part 5 Domain Knowledge"]:
    sec_qs = [q for q in all_parsed_questions if q["section"] == sec_name]
    correct_qs = [q for q in sec_qs if q["is_correct"]]
    wrong_qs = [q for q in sec_qs if not q["is_correct"]]
    print(f"\n=======================================================")
    print(f"{sec_name.upper()} ({len(correct_qs)}/{len(sec_qs)} Marks)")
    print(f"=======================================================")
    print("Correct Questions:", [q["q_num"] for q in correct_qs])
    print("Wrong Questions (Q_Num [Chosen -> Correct]):")
    for q in wrong_qs:
        print(f"  Q.{q['q_num']:2d} (Page {q['page']:2d}, QID: {q['q_id']}): Chosen = {q['chosen_opt']}, Correct = {q['correct_opt']}")
