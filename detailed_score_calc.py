import pymupdf
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's collect all elements per page: text spans, images, drawings
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

# Now let's extract all questions with exact bounding boxes
questions = []

for pno in range(len(doc)):
    page_num = pno + 1
    page = doc[pno]
    blocks = page.get_text("dict")["blocks"]
    
    # We want to group by question boxes. In DigiALM, question box starts with Q.<num>
    # Let's find all Q.<num> spans
    q_headers = []
    all_spans = []
    
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    txt = s["text"].strip()
                    if txt:
                        span_item = {
                            "text": txt,
                            "color": s["color"],
                            "hex_color": hex(s["color"]),
                            "font": s["font"],
                            "size": s["size"],
                            "bbox": s["bbox"],
                            "y": s["bbox"][1],
                            "page": page_num
                        }
                        all_spans.append(span_item)
                        if re.match(r'^Q\.\d+$', txt):
                            q_headers.append(span_item)
                            
    # Let's also attach page spans
    # We can process questions across page boundaries or within pages
    # Note: A question might span across 2 pages if it breaks across pages!

# Let's collect all spans globally with a unified global coordinate: (page_num * 10000 + y)
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
                            "page": page_num,
                            "global_y": page_num * 10000 + s["bbox"][1]
                        })

# Find all Question headers Q.<num>
q_starts = []
for idx, s in enumerate(global_spans):
    if re.match(r'^Q\.\d+$', s["text"]):
        q_starts.append((idx, s))

print(f"Total question headers found: {len(q_starts)}")

all_parsed_questions = []

for i, (start_idx, q_header) in enumerate(q_starts):
    end_idx = q_starts[i+1][0] if i+1 < len(q_starts) else len(global_spans)
    q_spans = global_spans[start_idx:end_idx]
    
    q_num = int(q_header["text"].replace("Q.", ""))
    q_page = q_header["page"]
    q_y = q_header["bbox"][1]
    
    sec = get_section_for(q_page, q_y)
    
    # Parse question details
    q_id = None
    status = None
    chosen_opt = None
    correct_opt = None
    options = {}
    q_text_parts = []
    is_in_question_text = True
    
    for s_idx, s in enumerate(q_spans):
        txt = s["text"]
        
        if txt == "Ans" or txt.startswith("Ans"):
            is_in_question_text = False
        elif is_in_question_text and s_idx > 0 and not txt.startswith("Question ID") and not txt.startswith("Section :"):
            q_text_parts.append(txt)
            
        if "Question ID :" in txt or txt == "Question ID :":
            if s_idx + 1 < len(q_spans) and re.match(r'^\d+$', q_spans[s_idx+1]["text"]):
                q_id = q_spans[s_idx+1]["text"]
                
        if "Status :" in txt or txt == "Status :":
            if s_idx + 1 < len(q_spans):
                status = q_spans[s_idx+1]["text"]
                
        if "Chosen Option :" in txt or txt == "Chosen Option :":
            if s_idx + 1 < len(q_spans):
                chosen_opt = q_spans[s_idx+1]["text"]
                
        m = re.match(r'^([A-D])\.\s*(.*)', txt)
        if m:
            opt_letter = m.group(1)
            opt_txt = m.group(2)
            is_green = (s["color"] == 4245067 or s["hex_color"] == "0x40c64b")
            options[opt_letter] = opt_txt
            if is_green:
                correct_opt = opt_letter

    # Also check if correct option is in option text spans
    if not correct_opt:
        for s in q_spans:
            if s["color"] == 4245067 or s["hex_color"] == "0x40c64b":
                m = re.match(r'^([A-D])\.', s["text"])
                if m:
                    correct_opt = m.group(1)

    is_attempted = (chosen_opt is not None and chosen_opt in ['A','B','C','D','1','2','3','4'] and chosen_opt != '--')
    is_correct = (is_attempted and chosen_opt == correct_opt)
    
    all_parsed_questions.append({
        "index": i + 1,
        "q_num": q_num,
        "section": sec,
        "page": q_page,
        "q_id": q_id,
        "question_text": " ".join(q_text_parts)[:100],
        "options": options,
        "status": status,
        "chosen_opt": chosen_opt,
        "correct_opt": correct_opt,
        "is_attempted": is_attempted,
        "is_correct": is_correct
    })

# Group by section
sections_dict = {}
for q in all_parsed_questions:
    s = q["section"]
    if s not in sections_dict:
        sections_dict[s] = []
    sections_dict[s].append(q)

print("\n" + "="*85)
print(f"{'SECTION NAME':<38} | {'TOTAL':<5} | {'ATTEMPT':<7} | {'CORRECT':<7} | {'WRONG':<5} | {'ACCURACY':<8} | {'MARKS':<5}")
print("="*85)

grand_total = 0
grand_attempt = 0
grand_correct = 0
grand_wrong = 0
grand_marks = 0

for sec_name, q_list in sections_dict.items():
    tot = len(q_list)
    att = sum(1 for q in q_list if q["is_attempted"])
    corr = sum(1 for q in q_list if q["is_correct"])
    wrg = att - corr
    acc = (corr / att * 100) if att > 0 else 0
    marks = corr # +1 per correct, 0 negative marking
    
    grand_total += tot
    grand_attempt += att
    grand_correct += corr
    grand_wrong += wrg
    grand_marks += marks
    
    print(f"{sec_name:<38} | {tot:<5} | {att:<7} | {corr:<7} | {wrg:<5} | {acc:>6.1f}%  | {marks:<5}")

print("="*85)
grand_acc = (grand_correct / grand_attempt * 100) if grand_attempt > 0 else 0
print(f"{'GRAND TOTAL':<38} | {grand_total:<5} | {grand_attempt:<7} | {grand_correct:<7} | {grand_wrong:<5} | {grand_acc:>6.1f}%  | {grand_marks:<5}")
print("="*85)
