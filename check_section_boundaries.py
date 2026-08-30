import pymupdf
import re

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect where section headers appear by looking at page text around page 8-10
for pno in range(7, 12):
    page = doc[pno]
    text = page.get_text()
    print(f"=== PAGE {pno+1} ===")
    lines = [l for l in text.split('\n') if l.strip()]
    for l in lines[:15]:
        print("  ", l)
