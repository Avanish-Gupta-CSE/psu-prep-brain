import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect Page 49 (0-indexed 48)
page = doc[48]
print("=== PAGE 49 SPANS ===")
for b in page.get_text("dict")["blocks"]:
    if "lines" in b:
        for l in b["lines"]:
            line_str = " ".join(s["text"] for s in l["spans"]).strip()
            if line_str:
                colors = [s["color"] for s in l["spans"]]
                print(f"  {line_str:70} | colors: {colors}")
