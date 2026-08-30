import pymupdf
import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect all section headers across all pages with their exact bounding box and page number
sections = []
for pno in range(len(doc)):
    page = doc[pno]
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                line_text = "".join(s["text"] for s in l["spans"]).strip()
                if "Section :" in line_text:
                    sections.append((pno + 1, line_text, l["bbox"]))

print("All Section headers found:")
for p, txt, bbox in sections:
    print(f"Page {p:2d} | {txt} | BBox: {bbox}")
