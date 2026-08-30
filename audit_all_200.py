import pymupdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's collect all spans page by page with full details
# In DigiALM:
# Section header appears at top or middle of a page
# Questions are sequentially numbered Q.1 to Q.25 in each section (and Q.1 to Q.100 in Domain Knowledge)

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

# Let's collect all spans
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

# Find Question starts
q_starts = []
for idx, s in enumerate(all_spans):
    if re.match(r'^Q\.\d+$', s["text"]):
        q_starts.append(idx)

print(f"Total Q markers: {len(q_starts)}")

parsed = []

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
    
    # Store options found
    # In DigiALM, options are listed under Ans:
    # A. <text> or 1. <text>
    # B. <text> or 2. <text>
    # C. <text> or 3. <text>
    # D. <text> or 4. <text>
    options = {}
    green_options = []
    
    for s_idx, s in enumerate(spans):
        txt = s["text"]
        if "Question ID :" in txt:
            if s_idx + 1 < len(spans) and re.match(r'^\d+$', spans[s_idx+1]["text"]):
                q_id = spans[s_idx+1]["text"]
        if "Status :" in txt:
            if s_idx + 1 < len(spans):
                status = spans[s_idx+1]["text"]
        if "Chosen Option :" in txt:
            if s_idx + 1 < len(spans):
                chosen_opt = spans[s_idx+1]["text"]
        
        # Check if this span is an option
        # Option span regex
        m = re.match(r'^([A-D1-4])\.\s*(.*)', txt)
        if m:
            opt_lbl = m.group(1)
            # Map 1->A, 2->B, 3->C, 4->D
            lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
            std_lbl = lbl_map[opt_lbl]
            options[std_lbl] = {
                "text": m.group(2),
                "color": s["color"],
                "hex": s["hex_color"],
                "page": s["page"]
            }
            if s["color"] == 4245067 or s["hex_color"] == "0x40c64b":
                green_options.append(std_lbl)
                
    # Also check if any span in this question has green color that corresponds to an option
    if not green_options:
        for s in spans:
            if s["color"] == 4245067 or s["hex_color"] == "0x40c64b":
                m = re.match(r'^([A-D1-4])\.', s["text"])
                if m:
                    lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
                    green_options.append(lbl_map[m.group(1)])

    # Standardize chosen_opt
    std_chosen = None
    if chosen_opt:
        lbl_map = {'1':'A', '2':'B', '3':'C', '4':'D', 'A':'A', 'B':'B', 'C':'C', 'D':'D'}
        std_chosen = lbl_map.get(chosen_opt, chosen_opt)
        
    correct_opt = green_options[0] if green_options else None
    
    is_attempted = (std_chosen in ['A','B','C','D'])
    is_correct = (is_attempted and std_chosen == correct_opt)
    
    parsed.append({
        "q_num": q_num,
        "section": sec,
        "page": page,
        "q_id": q_id,
        "status": status,
        "raw_chosen": chosen_opt,
        "std_chosen": std_chosen,
        "correct_opt": correct_opt,
        "all_green": green_options,
        "options_found": list(options.keys()),
        "is_attempted": is_attempted,
        "is_correct": is_correct
    })

print("\n--- Check any anomaly in questions ---")
anomalies = [p for p in parsed if not p["correct_opt"] or len(p["all_green"]) != 1 or not p["std_chosen"]]
print(f"Total anomalies: {len(anomalies)}")
for a in anomalies:
    print(a)

# Summary
print("\n" + "="*80)
print(f"{'SECTION':<35} | {'TOTAL':<5} | {'ATT':<5} | {'CORRECT':<7} | {'WRONG':<5} | {'SCORE':<5}")
print("="*80)

sec_groups = {}
for p in parsed:
    s = p["section"]
    if s not in sec_groups:
        sec_groups[s] = []
    sec_groups[s].append(p)

grand_score = 0
for s, qs in sec_groups.items():
    tot = len(qs)
    att = sum(1 for q in qs if q["is_attempted"])
    corr = sum(1 for q in qs if q["is_correct"])
    wrg = att - corr
    grand_score += corr
    print(f"{s:<35} | {tot:<5} | {att:<5} | {corr:<7} | {wrg:<5} | {corr:<5}")

print("="*80)
print(f"{'GRAND TOTAL':<35} | {len(parsed):<5} | {sum(1 for q in parsed if q['is_attempted']):<5} | {grand_score:<7} | {len(parsed)-grand_score:<5} | {grand_score:<5}")
print("="*80)
