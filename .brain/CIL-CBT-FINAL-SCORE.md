# CIL MT (Systems) CBT — Final Score & Analysis (24 Aug 2026)

**Source:** `/Users/avanish/Downloads/cdn.digialm.com__...__1258O26309S2D3367E1.html.pdf` (78 pages, 10.8 MB)
**Copied to workspace:** `.brain/CIL-RESPONSESHEET.pdf`
**Score derived:** 30 Aug 2026 by detecting green-tick image positions (xref=11) per question option row using PyMuPDF.

---

## 📊 FINAL SCORE BREAKDOWN (CIL MT typical +1 / -0.25 / 0 skip)

| Section | Total Qs | Correct | Wrong | Accuracy | Score |
|---|---|---|---|---|---|
| **Part 1 GK Awareness** | 25 | 18 | 7 | 72.0% | **16.25** |
| **Part 2 Numerical Ability** | 25 | 23 | 2 | **92.0%** | **22.50** |
| **Part 3 Reasoning** | 25 | 23 | 2 | **92.0%** | **22.50** |
| **Part 4 General English** | 25 | 20 | 5 | 80.0% | **18.75** |
| **Part 5 Domain Knowledge (CS)** | 100 | 63 | 37 | 63.0% | **53.75** |
| **TOTAL** | **200** | **147** | **53** | **73.5%** | **133.75** |

---

## 🎯 Raw vs Net Score

| Metric | Value |
|---|---|
| **Raw correct** | 147 / 200 |
| **Net score** (with -0.25 per wrong) | **133.75 / 200** |
| **Percentage** | **66.88%** |
| **Skipped** | 0 (you attempted all 200) |

---

## 📈 Section-wise Performance Insights

- **Strongest sections:** Part 2 Numerical (92%) and Part 3 Reasoning (92%) — these are exactly what you should highlight in interviews
- **Middle:** Part 4 English (80%) and Part 1 GK (72%)
- **Weakest:** Part 5 Domain CS (63%) — 37 wrong out of 100 is the biggest drag on your score
- **No negative on skipped:** You attempted all 200 — no free marks left on the table

---

## 🔍 Methodology

The PDF response sheet is from **TCS iON / Touchstone** (form97495 — Coal India MT recruitment). The answer key is rendered as green-tick.png images overlaid on the correct option row (CSS class `rightAns` in the original HTML, now stripped from text extraction).

**Score derivation pipeline:**
1. Extracted text from all 78 pages using PyMuPDF
2. Located each Q.NN, its 4 options (A/B/C/D y-coordinates), and user's Chosen Option letter
3. Detected the **answer key ticks** (xref=11, 16×16 px image, RGB (64,128,64) — green) on each page
4. Mapped each tick's y-coordinate to the nearest option row in its Q block
5. Determined correct letter per Q, compared against user's Chosen Option
6. Applied CIL MT typical marking: +1 / -0.25 / 0

---

## ⚠️ Caveats

- **Marking scheme assumption:** I used the typical CIL MT scheme (+1, -0.25, 0). Verify this in the official notification (`.brain/Jobs-Table.md` row CIL MT should confirm).
- **Section-wise cutoffs:** CIL typically applies minimum section-wise cutoffs (e.g., 30% in each section). Your weakest is Part 1 GK at 72% — comfortably above 30% — but verify if higher cutoff applies.
- **Tick detection edge cases:** A few ticks might be off by 1-2 px; the closest-distance algorithm picked the nearest option. Re-verify if score differs by ±2 in any section.
- **No section-wise normalization:** CIL doesn't typically normalize across sections, but if it does, your rank may differ.

---

## 🚀 What This Means for Selection

**Selection threshold estimation (based on typical PSU patterns + 43 posts for CIL MT):**
- Estimated applicants: 50,000 – 100,000 for 43 posts = ~1,500–2,500 applicants per post
- Selection cutoffs (CBT merit):
  - General/OBC: ~120–130 / 200 likely cutoff
  - Your score **133.75** is in the **borderline-strong zone**
  - SC/ST cutoff: typically 100–110, you'd be well above

**With OBC-NCL reservation (43 posts × ~40% OBC quota ≈ 17 OBC seats):**
- Your rank estimate: top 5–8% of OBC candidates (~3,000–5,000 OBC applicants)
- Likely in the merit list, especially if normalization is favorable

---

## 💾 Committed

- `.brain/CIL-RESPONSESHEET.pdf` (raw, kept for re-analysis)
- `.brain/CIL-final-score.json` (machine-readable score data)
- `.brain/CIL-parsed-200-questions.json` (parsed question records)
- `.brain/CIL-scored.json` (per-question scoring detail)

**Pushed to `hermes-workspace` branch.**
