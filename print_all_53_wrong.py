import pymupdf
import re
import sys

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

wrong_list = []

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
    options = {}
    q_text_parts = []
    is_in_qtext = True
    
    for s_idx, s in enumerate(spans):
        txt = s["text"]
        if txt == "Ans" or txt.startswith("Ans"):
            is_in_qtext = False
        elif is_in_qtext and s_idx > 0 and not txt.startswith("Question ID") and not txt.startswith("Section :"):
            q_text_parts.append(txt)
            
        if "Question ID :" in txt:
            if s_idx + 1 < len(spans) and re.match(r'^\d+$', spans[s_idx+1]["text"]):
                q_id = spans[s_idx+1]["text"]
        if "Status :" in txt:
            if s_idx + 1 < len(spans):
                status = spans[s_idx+1]["text"]
        if "Chosen Option :" in txt:
            if s_idx + 1 < len(spans):
                chosen_opt = spans[s_idx+1]["text"]
                
        m = re.match(r'^([A-D1-4])\.(\s*(.*))?$', txt)
        if m:
            opt_letter = m.group(1)
            lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
            std_letter = lbl_map[opt_letter]
            is_green = (s["color"] == 4245067 or s["hex_color"] == "0x40c64b")
            if not is_green and s_idx + 1 < len(spans):
                next_s = spans[s_idx+1]
                if abs(next_s["bbox"][1] - s["bbox"][1]) < 5:
                    if next_s["color"] == 4245067 or next_s["hex_color"] == "0x40c64b":
                        is_green = True
            
            # collect option text spans
            opt_txt = m.group(3) if m.group(3) else ""
            options[std_letter] = {
                "text": opt_txt,
                "is_green": is_green,
                "color": s["color"]
            }

    std_chosen = None
    if chosen_opt:
        lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
        std_chosen = lbl_map.get(chosen_opt, chosen_opt)

    correct_opt = None
    for opt_lbl, opt_data in options.items():
        if opt_data["is_green"]:
            correct_opt = opt_lbl
            break

    if not (std_chosen in ['A','B','C','D'] and std_chosen == correct_opt):
        wrong_list.append({
            "index": i + 1,
            "q_num": q_num,
            "section": sec,
            "page": page,
            "q_id": q_id,
            "q_text": " ".join(q_text_parts),
            "chosen_opt": std_chosen,
            "correct_opt": correct_opt,
            "options": options
        })

print(f"Total wrong questions: {len(wrong_list)}")
print("\n" + "="*90)
for idx, w in enumerate(wrong_list):
    print(f"[{idx+1:2d}] {w['section']} - Q.{w['q_num']} (Page {w['page']}, QID: {w['q_id']})")
    print(f"     Text: {w['q_text'][:120]}")
    print(f"     Candidate Chosen: {w['chosen_opt']} | Official Key (Green): {w['correct_opt']}")
    print("-" * 90)
