import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect Page 16 (0-indexed 15)
page = doc[15]
print("=== PAGE 16 SPANS ===")
blocks = page.get_text("dict")["blocks"]
for b in blocks:
    if "lines" in b:
        for l in b["lines"]:
            for s in l["spans"]:
                txt = s["text"].strip()
                if txt:
                    print(f"{txt:60} | Color: {s['color']} (hex: {hex(s['color'])}) | BBox: {s['bbox']}")
