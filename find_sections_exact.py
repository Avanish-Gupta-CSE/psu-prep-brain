import pymupdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect all 78 pages and identify exact section headers and every question box
# Let's print the exact page where each Section header is found
for pno in range(len(doc)):
    page = doc[pno]
    text = page.get_text()
    if "Section :" in text:
        lines = [l.strip() for l in text.split("\n") if "Section :" in l]
        print(f"Page {pno+1}: {lines}")
