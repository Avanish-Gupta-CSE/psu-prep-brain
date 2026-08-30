import pymupdf
import re

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

print(f"Total pages: {len(doc)}")

# Let's inspect page 2, 3, 4, 5
for pno in range(1, 5):
    page = doc[pno]
    blocks = page.get_text("dict")["blocks"]
    print(f"\n--- PAGE {pno+1} ---")
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    txt = s["text"].strip()
                    # Check if it starts with A. B. C. D. or 1. 2. 3. 4.
                    if re.match(r'^[A-D]\.\s', txt) or re.match(r'^[1-4]\.\s', txt) or "Chosen Option" in txt or "Status :" in txt or "Section :" in txt or re.match(r'^Q\.\d+', txt):
                        print(f"  {txt:50} | Color: {s['color']} (hex: {hex(s['color'])})")
