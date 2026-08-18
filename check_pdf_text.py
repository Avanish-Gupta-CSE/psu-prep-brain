import os, pypdf

downloads = r'C:\Users\agupt1\Downloads'
pdf_files = [os.path.join(downloads, f) for f in os.listdir(downloads) if f.lower().endswith('.pdf')]

print(f"Total PDFs in Downloads: {len(pdf_files)}")

for pdf in pdf_files:
    fname = os.path.basename(pdf)
    if any(k in fname.lower() for k in ['gate', 'score', 'result', '2026', 'cs26', 'da26', 'marks', 'card']):
        print(f"\n--- Checking {fname} ---")
        try:
            reader = pypdf.PdfReader(pdf)
            text = ""
            for page in reader.pages[:2]:
                text += page.extract_text() or ""
            print("Extracted preview (first 300 chars):")
            print(repr(text[:300]))
            if "2026" in text or "Scorecard" in text or "GATE" in text:
                print("Matches keywords in PDF body!")
                for line in text.splitlines():
                    if any(k in line.lower() for k in ['gate', 'marks', 'score', 'candidate', 'roll', 'registration', 'name', 'qualifying']):
                        print("  ", line.strip())
        except Exception as e:
            print("  Error reading PDF:", e)
