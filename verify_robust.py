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

def get_section(pno, y):
    sec = "Part 1 General Knowledge Awareness"
    for p, py, name in section_starts:
        if pno > p or (pno == p and y >= py):
            sec = name
    return sec

all_spans = []
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
                        all_spans.append({
                            "page": page_num,
                            "text": txt,
                            "color": s["color"],
                            "hex_color": hex(s["color"]),
                            "bbox": s["bbox"],
                            "y": s["bbox"][1]
                        })

q_starts = []
for idx, s in enumerate(all_spans):
    if re.match(r'^Q\.\d+$', s["text"]):
        q_starts.append(idx)

print(f"Total Q markers: {len(q_starts)}")

verified_questions = []

for i, start_idx in enumerate(q_starts):
    end_idx = q_starts[i+1] if i+1 < len(q_starts) else len(all_spans)
    spans = all_spans[start_idx:end_idx]
    
    q_span = spans[0]
    q_num = int(q_span["text"].replace("Q.", ""))
    page = q_span["page"]
    y = q_span["y"]
    sec = get_section(page, y)
    
    q_id = None
    status = None
    chosen_opt = None
    
    # We will identify options strictly
    # Option spans start with A. / B. / C. / D. (or 1. / 2. / 3. / 4.)
    options = {}
    
    for s_idx, s in enumerate(spans):
        txt = s["text"]
        if "Question ID :" in txt or txt == "Question ID :":
            if s_idx + 1 < len(spans) and re.match(r'^\d+$', spans[s_idx+1]["text"]):
                q_id = spans[s_idx+1]["text"]
        if "Status :" in txt or txt == "Status :":
            if s_idx + 1 < len(spans):
                status = spans[s_idx+1]["text"]
        if "Chosen Option :" in txt or txt == "Chosen Option :":
            if s_idx + 1 < len(spans):
                chosen_opt = spans[s_idx+1]["text"]
                
        # Match option header: exactly "A.", "B.", "C.", "D." or "1.", "2.", "3.", "4."
        # or starting with "A. ", "B. ", etc.
        m = re.match(r'^([A-D1-4])\.(\s*(.*))?$', txt)
        if m:
            opt_letter = m.group(1)
            # Standardize letter
            lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
            std_letter = lbl_map[opt_letter]
            
            # The color of the option is either on this span or the immediately following text span
            # Check if this span is green (4245067)
            is_green = (s["color"] == 4245067 or s["hex_color"] == "0x40c64b")
            
            # If not green, check if next span is green
            if not is_green and s_idx + 1 < len(spans):
                next_s = spans[s_idx+1]
                # If next span is on same vertical line
                if abs(next_s["bbox"][1] - s["bbox"][1]) < 5:
                    if next_s["color"] == 4245067 or next_s["hex_color"] == "0x40c64b":
                        is_green = True
                        
            options[std_letter] = {
                "text": m.group(3) if m.group(3) else "",
                "color": s["color"],
                "is_green": is_green,
                "span_idx": s_idx
            }

    # Standardize chosen_opt
    std_chosen = None
    if chosen_opt:
        lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
        std_chosen = lbl_map.get(chosen_opt, chosen_opt)

    # Determine correct option
    correct_opt = None
    for opt_lbl, opt_data in options.items():
        if opt_data["is_green"]:
            correct_opt = opt_lbl
            break

    # If still not found, check all spans in question for green color
    if not correct_opt:
        for s in spans:
            if s["color"] == 4245067 or s["hex_color"] == "0x40c64b":
                # Check nearest preceding option letter
                for opt_lbl, opt_data in options.items():
                    if opt_data["span_idx"] <= spans.index(s):
                        correct_opt = opt_lbl

    is_attempted = (std_chosen in ['A','B','C','D'])
    is_correct = (is_attempted and std_chosen == correct_opt)
    
    verified_questions.append({
        "index": i + 1,
        "q_num": q_num,
        "section": sec,
        "page": page,
        "q_id": q_id,
        "status": status,
        "chosen_opt": std_chosen,
        "correct_opt": correct_opt,
        "options_found": options,
        "is_attempted": is_attempted,
        "is_correct": is_correct
    })

# Let's check all 200 questions
for q in verified_questions:
    if not q["correct_opt"]:
        print(f"ERROR: Missing correct opt on Q.{q['q_num']} (Page {q['page']}, Section: {q['section']})")

# Let's summarize
sec_dict = {}
for q in verified_questions:
    s = q["section"]
    if s not in sec_dict:
        sec_dict[s] = []
    sec_dict[s].append(q)

print("\n" + "="*85)
print(f"{'SECTION':<38} | {'TOTAL':<5} | {'ATT':<5} | {'CORRECT':<7} | {'WRONG':<5} | {'SCORE':<5}")
print("="*85)

total_score = 0
for s, qs in sec_dict.items():
    tot = len(qs)
    att = sum(1 for q in qs if q["is_attempted"])
    corr = sum(1 for q in qs if q["is_correct"])
    wrg = att - corr
    total_score += corr
    print(f"{s:<38} | {tot:<5} | {att:<5} | {corr:<7} | {wrg:<5} | {corr:<5}")

print("="*85)
print(f"{'GRAND TOTAL':<38} | {len(verified_questions):<5} | {sum(1 for q in verified_questions if q['is_attempted']):<5} | {total_score:<7} | {len(verified_questions)-total_score:<5} | {total_score:<5}")
print("="*85)
