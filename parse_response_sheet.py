import os
import sys
import pymupdf

pdf_path = r'C:\Users\agupt1\Downloads\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf'
doc = pymupdf.open(pdf_path)

page = doc[0]
print("--- Images on Page 1 ---")
images = page.get_images()
for img_info in images:
    xref = img_info[0]
    base_img = doc.extract_image(xref)
    print(f"Xref: {xref}, Dim: {base_img['width']}x{base_img['height']}, Ext: {base_img['ext']}")

print("--- Drawings on Page 1 ---")
drawings = page.get_drawings()
print(f"Total drawings: {len(drawings)}")
for d in drawings:
    # check fill color or stroke color
    fill = d.get("fill")
    color = d.get("color")
    rect = d.get("rect")
    if fill or color:
        print(f"Fill: {fill}, Color: {color}, Rect: {rect}")

print("--- Text Spans on Page 1 ---")
blocks = page.get_text("dict")["blocks"]
for b in blocks:
    if "lines" in b:
        for l in b["lines"]:
            for s in l["spans"]:
                txt = s["text"].strip()
                if txt:
                    print(f"Span: {txt:40} | Color: {s['color']} | Font: {s['font']} | Size: {s['size']:.1f} | BBox: {s['bbox']}")
