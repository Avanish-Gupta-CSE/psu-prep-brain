import pymupdf
import re
import json

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

print(f"Total pages: {len(doc)}")

# Let's extract all text blocks with spans across all pages
all_spans = []
for pno in range(len(doc)):
    page = doc[pno]
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    txt = s["text"].strip()
                    if txt:
                        all_spans.append({
                            "page": pno + 1,
                            "text": txt,
                            "color": s["color"],
                            "hex_color": hex(s["color"]),
                            "font": s["font"],
                            "size": s["size"],
                            "bbox": s["bbox"]
                        })

print(f"Extracted {len(all_spans)} spans across {len(doc)} pages.")

# Let's see all unique sections in the document
sections = []
for s in all_spans:
    if "Section :" in s["text"]:
        # check surrounding spans
        idx = all_spans.index(s)
        sec_text = s["text"]
        if idx + 1 < len(all_spans):
            sec_text += " " + all_spans[idx+1]["text"]
        sections.append((s["page"], sec_text))

print("Sections found:", sections)
