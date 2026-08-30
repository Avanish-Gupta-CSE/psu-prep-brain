import pymupdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's verify every single question in Domain Knowledge (Q.1 to Q.100)
# and get the question text snippet
# Let's inspect the wrong questions in Domain Knowledge to classify them by subject (DBMS, OS, CN, Algo, COA, etc.)
