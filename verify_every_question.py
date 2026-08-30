import pymupdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

# Let's inspect all blocks on all pages and construct the exact questions
# Each question in DigiALM is contained within a question table.
# Let's see how many total questions exist per section and check their exact option colors.

# Let's list all pages and their text blocks
all_text = ""
pages_text = [p.get_text() for p in doc]

# Let's check sections and question count per section
# In CIL exam:
# Paper 1:
# Section 1: General Knowledge Awareness - 25 Qs
# Section 2: Numerical Ability - 25 Qs
# Section 3: Reasoning - 25 Qs
# Section 4: General English - 25 Qs
# Paper 2:
# Section 5: Domain Knowledge (Systems) - 100 Qs

# Total = 200 Qs.

# Let's write a python script to parse each question block precisely.
