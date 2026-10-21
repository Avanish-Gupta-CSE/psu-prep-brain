**🌐 Published:** https://avanish-gupta-cse.github.io/psu-prep-brain/ (source: `docs/index.html`)

# GATE Decision Model — "Can I actually crack this?"

**Written:** 21 Oct 2026 · **Method:** official GATE/POWERGRID statistics + 120,000-trial Monte Carlo across 4 scenarios × 2 cycles × 4 programmes
**Question:** Given ~30.03 marks / AIR 29,099 with no study, is GATE → Maharatna PSU a real plan or a fantasy?
**Answer up front:** **The goal is real. GATE is the wrong door.** Full reasoning below.

> Confidence tags: **[OFFICIAL]** = from a published statistical report or the organisation's own notice. **[INFERRED]** = modelled, assumptions stated. **[JUDGEMENT]** = my estimate, no clean source.

---

## 1. Ground truth — GATE CS 2026 [OFFICIAL, IIT Guwahati report]

| Metric | Value |
| :--- | :--- |
| Appeared | **2,11,020** |
| Qualified | 40,661 (**19.3%**) |
| General qualifying mark | **30.0** → score **350** |
| Top-0.1% average (Mt) | **77.03** |
| Mean / SD | 18.51 / 11.58 |
| His marks | **30.03** → score 350 → **AIR 29,099** |

**He is exactly on the qualifying floor.** 350 is not a base — it is the *minimum to appear in the result*. 40,661 people cleared it; his target is roughly the top 300.

### Marks → candidates at or above [OFFICIAL]

| Marks | Candidates ≥ | Percentile (of appeared) | What it buys |
| ---: | ---: | ---: | :--- |
| 30 | 29,611 | 86.0 | listed only |
| 40 | 10,340 | 95.1 | nothing |
| 50 | 3,655 | 98.3 | DFO-type large-seat posts |
| 60 | 1,170 | 99.45 | borderline PSU in a big-vacancy year |
| 70 | **295** | 99.86 | real PSU shortlists |
| 80 | **42** | 99.98 | PGCIL in a 2-seat year |

**The percentile he must reach: 99.8–99.98.** Not 95. Not 99. The last decimal place is the whole game.

---

## 2. Who actually takes GATE CS 2027 [OFFICIAL — each organisation's own notice, Sept 2026]

| Organisation | GATE 2027 CS? | CS posts | Notes |
| :--- | :--- | :--- | :--- |
| **POWERGRID (PGCIL)** | ✅ | **not yet published** (2025: **2**) | Advt CC/03/2026 · GATE 85% weight |
| **NTPC** | ✅ | not yet published | Advt 11/26 · GATE 2027 only |
| **Grid-India** | ✅ | **15** (UR 7, OBC 4, SC 2, ST 1, EWS 1) | Advt CC/26/2026 · GATE 85% + GD 3% + PI 12% |
| **DRDO (Scientist B)** | ✅ | ~34 last cycle | RAC notice 31.08.2026 · detailed advt pending |
| **IOCL** | ❌ **NO** | — | CS/IT via **its own CBT** (Advt 2026/01) |
| **HPCL** | ❌ **NO** | — | own officer process |
| **GAIL** | ❌ **NO** | — | Chem/Elec/Instr/Mech only — **no CS discipline at all** |
| **BHEL / ONGC / NLC / NHPC** | ❌ (not named) | — | own CBTs |
| **Cabinet Secretariat DFO** | ⚠️ different | **112** | accepts GATE 2024/25/26 — **verify 2027/28 acceptance** |

### ⚠️ This is the single biggest correction to the plan of record
The master plan treats "GATE 2028 → Maharatna township" as the spine. **In reality only two Maharatnas take GATE CS (PGCIL, NTPC), and both have tiny, unpublished, volatile CS seat counts.** The other names on the target list — IOCL, HPCL, BHEL, ONGC — must be reached through **their own CBTs**, not GATE.

**Total GATE-CS PSU seats per year ≈ 50–70, across 2.11 lakh candidates.** That is roughly **1 seat per 3,000–4,000 CS candidates.**

---

## 3. Cutoff reality — PGCIL's own published numbers [OFFICIAL]

| Cycle | CS posts | UR cutoff | **OBC-NCL cutoff** | EWS |
| :--- | ---: | ---: | ---: | ---: |
| **GATE 2024** | ~37 selected | 67.88 | **57.40** | 57.12 |
| **GATE 2025** | **2** (CTUIL only) | 80.26 | **— no OBC post** | 31.83 |

**The two lessons:**
1. **OBC-NCL relief is worth ~10 marks** (67.88 → 57.40) — *but only when an OBC post exists.* In 2025 there was none, so OBC candidates had to clear 80.26 like everyone else.
2. **Cutoff is set by vacancy count, not by talent.** 37 posts → 57.40 for OBC (AIR ≈ 1,100). 2 posts → 80.26 (AIR ≈ 40). **A 19x swing in rank requirement between two consecutive years.**

**A 2024-type year is reachable. A 2025-type year is not.** And he cannot control which one arrives.

---

## 4. Hours → marks model [INFERRED — the key uncertainty]

Fitted curve: `M = 30 + (ceiling − 30) × (1 − e^(−H/1050))`, ceiling 72, ±5 marks noise.

| Effective hours | Expected marks | AIR (2026 field) | Verdict |
| ---: | ---: | ---: | :--- |
| 300 | 40.4 | 10,176 | nothing |
| 500 | 45.9 | 5,065 | nothing |
| **700** | **50.4** | **2,846** | DFO-type only |
| 900 | 54.2 | 1,767 | borderline big-year PSU |
| **1,100** | **57.3** | **1,191** | **PGCIL-2024-type OBC cutoff** |
| 1,400 | 60.9 | 747 | real shortlist |
| 1,800 | 64.4 | 478 | strong |
| 2,400 | 67.7 | 314 | near-guarantee |

**Cross-check against the real world:** 1,170 candidates scored 60+ in 2026. Almost all were full-time students with 1,500–3,000 hours. A working professional delivering 650–900 hours landing at 48–56 marks is the honest expectation.

---

## 5. Monte Carlo result — 120,000 trials per scenario [INFERRED]

Assumptions: hours delivered are lognormal around the scenario mean; marks from the curve above with ±5 noise; each cycle draws vacancy regimes for 3–4 programmes, correlated by a shared "hiring year" factor; no OBC post → OBC candidates must clear UR; P(offer | shortlist) = 0.33.

| Scenario | Hours actually delivered | E[marks] | **P(offer in 2028)** | **P(offer by 2029)** |
| :--- | ---: | ---: | ---: | ---: |
| **Pessimistic** — the pattern of the last 12 months | 450 | 42.7 | **0.6%** | **5.4%** |
| **Base** — realistic for a full-time bank officer | 650 | 48.6 | **3.4%** | **23.7%** |
| **Committed** — 1.5–2 h/day sustained for 16 months | 900 | 56.2 | **14.2%** | **50.9%** |
| **All-in** — 2.5–3 h/day, i.e. a different life | 1,500 | 68.4 | **44.8%** | **77.5%** |

### Sensitivity (single cycle, average vacancy year)

| Hours | P(shortlist) |
| ---: | ---: |
| 400 | 1.9% |
| 600 | 10.5% |
| 800 | 24.9% |
| 1,000 | 39.0% |
| 1,200 | 49.3% |
| 1,500 | 58.3% |

**Read:** the answer is not a fixed number — **it is a function of hours actually delivered, and that is the one variable he controls.** The band is 5% → 77%. Nothing else in the model moves it as much.

---

## 6. The counterfactual that matters — IOCL 2026 arithmetic [OFFICIAL scores]

| Section | His score | % | What it means |
| :--- | ---: | ---: | :--- |
| **A — Technical** | **37.75 / 50** | **75.5%** | **Already competitive.** The engineering is there. |
| **B — Aptitude** | **10.00 / 50** | **20.0%** | **Fatal.** 40 marks left on the table. |
| Total | 47.75 / 100 | 47.75% | Shortlist ≈ 65–70 |

**He was roughly 20 marks from an IOCL interview — and every one of those 20 marks was in the section he did not prepare.**

Cost to fix Section B from 20% → 60%: **≈ 150–200 hours.** Cost to move GATE from 30 → 57: **≈ 1,100 hours.**

> **This is the finding that reorders the entire plan.**
> 200 hours converts a failed IOCL attempt into a competitive one.
> 1,100 hours buys a ~25–35% shot at a PGCIL/NTPC interview.
> **The aptitude door is 5x cheaper for a comparable probability.**

---

## 7. Expected-value comparison [JUDGEMENT on probabilities]

| Route | Hours to viable | P(success) | Payoff | Time-to-decision |
| :--- | ---: | ---: | :--- | :--- |
| **Own-CBT PSU** (IOCL, HPCL, NTPC, BHEL, ONGC) | **200–300** | **30–40%** | ₹18–22L + township | **4–6 months** |
| **GATE → PGCIL / NTPC / Grid-India** | 900–1,200 | 25–35% | ₹22.5L + township | 16–28 months |
| **Direct IT** (NICL, ISRO, NSPCL, CONCOR) | 250–350 | 15–25% | ₹14–18L | 3–9 months |
| **DFO (112 CS seats)** | 500–700 | 45–55% | ₹9–10L (Level 7) | 12–24 months |
| **Corporate** (Java/Spring + DSA) | 400–600 | 55–65% | ₹16–20L | 6–12 months |

**The township PSU goal is reachable in 4–6 months through the CBT door, at one-fifth the study cost of the GATE door.**

---

## 8. Verdict

### Do not pursue GATE as the plan.
- Only 2 Maharatnas take GATE CS.
- Total CS seats ≈ 50–70/yr against 2.11 lakh candidates.
- Requires 99.8th percentile; he is at the 86th.
- Realistic delivery (650h) → ~24% over two cycles.
- It costs 16–28 months of the only irreplaceable resource: the age window.

### Do keep GATE as a free option.
- Already registered for 2027. Costs no leave (Sunday), no money.
- **Numeric gate:** GATE 2027 marks decide everything —
  - **< 45** → cancel GATE 2028. Redirect all hours to CBT + corporate.
  - **45–55** → keep 2028 as a cheap hedge, but CBT stays primary.
  - **> 55** → GATE becomes a live second engine; escalate hours.

### Do pursue the PSU goal — through the CBT door.
- **Aptitude is the binding constraint, not technical knowledge.** Proven by his own IOCL score.
- 150–200 hours of aptitude work is the highest-return study in this entire repository.
- The same 200 hours also serves NICL, ISRO, NSPCL, CONCOR, and every future CBT.

---

## 9. Kill criteria (pre-committed, so the decision is not made in a bad mood)

| Gate | Date | Condition | Action if failed |
| :--- | :--- | :--- | :--- |
| **K1** | 22 Oct 2026 | Aptitude block started (40Q timed, weekly) | Nothing else matters until this is habitual |
| **K2** | 31 Dec 2026 | ≥ 8 aptitude mocks done | GATE 2028 plan is fiction; cancel now |
| **K3** | 19 Mar 2027 | GATE 2027 result | < 45 → GATE 2028 cancelled |
| **K4** | 30 Jun 2027 | ≥ 2 CBT shortlists (IOCL/NTPC/HPCL/NICL class) | Re-weight toward corporate |
| **K5** | 31 Mar 2027 | Corporate trigger check | Still unbearable + no progress → open the corporate search |
| **K6** | Feb 2028 | GATE 2028 (only if K3 passed) | Final GATE attempt; 2029 only with PL unlocked |

**The point of K2 and K3 is to fail early and cheaply** — not in February 2028 with 16 months spent.

---

## 10. One-line answer

> **You are not 1,000 hours from a PSU. You are about 200 hours of aptitude from an IOCL interview, and 1,100 hours from a coin-flip at POWERGRID. Do the 200 first — and let the GATE score in March 2027 tell you, with real data, whether the 1,100 is worth starting.**

---

# 11. RECALIBRATION — 21 Oct evening (supersedes the framing of §7 and §10)

**User's correction:** *"I'm failing the PSU CBTs on technical questions from GATE subjects I haven't prepared."*

**He is right. §7 was too narrow, and the "GATE vs CBT" split was a false binary.**

## 11a. The verified record [OFFICIAL scores]

| Exam | Overall | Technical | Aptitude | Seats |
| :--- | :--- | :--- | :--- | :--- |
| STPI Scientist 'B' | 96/150 = **64.0%** | NIELIT GATE-level CS | GA + Eng | **1 OBC-NCL** |
| NFL MT (IT) | 99/150 = **66.0%** | **69/100 = 69.0%** | 30/50 = **60.0%** | **1 OBC-NCL** |
| HLL Lifecare MT | 62.5/100 = **62.5%** | 50% domain half | 50% general half | 17 engg (IT subset) |
| **CIL MT (Systems)** | **147/200 = 73.5%** | peak of record | — | many |
| IOCL ET (CS) | 47.75/100 | **37.75/50 = 75.5%** | **10/50 = 20.0%** | moderate |

**Technical band: 69.0 – 75.5%, median ≈ 72%.** That is a stable ceiling, not variance. The GATE syllabus is exactly the union of what these papers test — so **the GATE curriculum is the correct fix for the technical sections.**

**What still stands from §7:** aptitude is *cheap*, and he skipped it. IOCL: even a perfect 50/50 technical with his actual 20/50 aptitude gives 60/100 — below a ~65–70 cutoff. **Aptitude is not optional; it is just inexpensive.**

**Conclusion: both. Not either.**

## 11b. The variable nobody was optimising — seat arithmetic

| OBC-NCL seats | You must be | Score needed | His ~73% |
| :--- | :--- | ---: | :--- |
| **1** (STPI, NFL) | the single best OBC candidate in India | 84–88% | **dead** |
| 3–5 | top 5 OBC | 78–82% | **dead** |
| 6–15 | top 15 OBC | 72–76% | borderline |
| 15+ | top 40 OBC | 68–72% | **competitive** |

**The same 73% is worthless in a 1-seat exam and competitive in a 15-seat exam.** STPI and NFL were unwinnable at 64–66% regardless of study effort — which is exactly what this repo already concluded: *"the failure mode is vacancy arithmetic, not scores."*

> **Moving from 1-seat exams to 10-seat exams is worth more than 300 study hours — and costs nothing.**

## 11c. The hawk model — 150,000-trial Monte Carlo [INFERRED]

Assumptions: 6 exams/year; only **75%** actually materialise; **P(offer | shortlist) = 25%**; seat tiers weighted to his real record (45% one-seat, 35% 3–5, 20% large); technical 65% / aptitude 35%; ±4 noise; shared year factor.

| Hours delivered | Technical | Aptitude | P(≥1 shortlist) | **P(≥1 offer, 24 mo)** |
| ---: | ---: | ---: | ---: | ---: |
| 300 | 76.9% | 58.1% | 72.6% | **29.8%** |
| 450 | 79.1% | 62.8% | 88.7% | **44.2%** |
| 600 | 80.8% | 66.0% | 94.6% | **53.1%** |
| 750 | 82.1% | 68.0% | 97.0% | **58.9%** |
| 900 | 83.0% | 69.4% | 98.1% | **62.9%** |

**Against §5: GATE-only = 23.7% over two cycles for 650 hours.**
**Hawk = 44–53% over 24 months for 450–600 hours.**

The strategy roughly **doubles the probability at two-thirds the hours**, because it converts one impossibly high bar into six-to-nine moderate bars.

### Single-exam value of the same hours

| Hours | P(clear one multi-seat CBT) |
| ---: | ---: |
| 0 (today) | **0.0%** |
| 300 | 3.3% |
| 600 | **25.9%** |
| 900 | **47.7%** |

## 11d. GATE becomes a free by-product

The same technical hours produce a GATE score with no separate effort:

| Hours | GATE marks | AIR |
| ---: | ---: | ---: |
| 450 | 44.6 | ~5,957 |
| 600 | 48.3 | ~3,745 |
| 750 | 51.4 | ~2,504 |
| 900 | 54.2 | ~1,767 |

Not enough for PGCIL/NTPC in a normal year. **Enough for DFO (112 seats), and enough to be a live ticket in a 2024-type vacancy year.**

**Sit GATE 2027 and 2028. Stop studying *for* it. Study the syllabus; the score is the receipt.**

## 11e. Revised operating rules

1. **Curriculum rule — 100% of GATE topics at 80% depth.** Skip the last 20% that only GATE rewards: TOC proofs, compiler-optimisation internals, advanced COA numericals. That 20% buys ~8 GATE marks and ~0 CBT marks.
2. **Aptitude rule — 150 hours, non-negotiable, weekly timed block.** Never again enter a CBT with a 20% section.
3. **Portfolio rule — count OBC-NCL seats before applying.** 0–2 seats → apply only if free. 3–5 → apply. 6+ → prioritise.
4. **Hawk rule — 6–9 applications per year, 15 portals monitored weekly.** Probability compounds with shots taken, not with study hours.
5. **K3 revised:** GATE 2027 < 45 no longer cancels the strategy — it only confirms GATE is a by-product. The strategy is no longer GATE.

## 11f. Revised one-line answer

> **You were right: the gap is breadth, not aptitude alone — and the GATE syllabus is the map for it. But the map is not the destination. Learn the syllabus at 80% depth, take every multi-seat shot you can see, and let the GATE score arrive as a by-product. Probability of a PSU offer inside 24 months: ~44–53%, versus ~24% for GATE alone.**

---

# 12. FORWARD FORECAST — where he actually is at each date

**Method:** 180,000-trial 36-month simulation. Three streams run in parallel: PSU/CBT (6-9 exams/yr, 60-75% realised, P(offer|shortlist) 0.20-0.25), central-govt (NICL/DFO/STPI/CONCOR/ISRO), and corporate (trigger fires 31 Mar 2027 if no PSU movement, 7-16 month search). Two calibrations: **BASE** = realistic slippage (300-400 h/yr) and **CALIBRATED** = plan runs as designed (380-470 h/yr).

## 12a. Base case — most probable (realistic slippage, ~1,020 h by month 36)

| Checkpoint | Still at UCO | **PSU ET** | Central govt | Corporate |
| :--- | ---: | ---: | ---: | ---: |
| **Mid-2028** (21 mo) | **67%** | 10% | 10% | 12% |
| **End-2028** (27 mo) | **57%** | 21% | 11% | 12% |
| **Mid-2029** (33 mo) | **46%** | **30%** | 14% | 9% |

**Most probable single state at every checkpoint: still at UCO Bank.**

## 12b. Calibrated case — if the plan actually runs (~1,240 h by month 36)

| Checkpoint | Still at UCO | **PSU ET** | Central govt | Corporate |
| :--- | ---: | ---: | ---: | ---: |
| **Mid-2028** (21 mo) | **42%** | 30% | 12% | 15% |
| **End-2028** (27 mo) | 27% | **52%** | 10% | 11% |
| **Mid-2029** (33 mo) | 16% | **66%** | 12% | 6% |

**The entire gap between §12a and §12b is hours delivered. Nothing else.**

## 12c. The real inflection is September 2028, not 2027

- **Sept 2028 = bond end + probation end + PL unlocked (30 days).** Mobility, not motivation, is the binding constraint before that date.
- **31 Mar 2028 = HPCL age cap closes.** 31 Mar 2029 = IOCL / BPCL / GAIL close. 2030 = NTPC / BHEL. 2031 = PGCIL. 2033 = ONGC / NICL.
- Therefore: **the IOCL-class window is 2027 and 2028 cycles only.** By mid-2029 that door is shut regardless of preparation.

## 12d. Verdict

> **Pursue the preparation. Expect the payoff in late 2028 to mid-2029, not 2027.**
> Median trajectory: **UCO → UCO → UCO → move in the 2028-29 season.**
> The most likely single outcome is that nothing converts for ~24 months and then something does — which is exactly why the corporate trigger must be fired on schedule rather than treated as a last resort.

---

# 13. THE 2027 SWITCH CONSTRAINT — full permutation analysis

**New constraint (21 Oct, user):** *"I want to switch within 2027. If no result by then, I'll decide between corporate and staying at UCO."*

**This changes the primary vehicle.** A PSU offer cannot realistically land before 2028 — the exam→shortlist→interview→offer→joining chain alone takes 7-10 months. **A 2027 switch is a corporate deadline, not a PSU deadline.**

---

## 13a. Five checkpoints × three scenarios [220,000 trials]

Scenario definitions:

| | Hours/yr | Aptitude | Exams written/yr | Corporate search starts | Corporate conversion |
| :--- | ---: | ---: | ---: | :--- | ---: |
| **WORST** | 210–230 | never fixed | 1.6 | Jun 2027 | 20% |
| **AVERAGE** | 350–420 | reaches 60% | 3.2 | Mar 2027 | 42% |
| **BEST** | 550–620 | reaches 68% | 5.5 | Dec 2026 | 68% |

### WORST case

| Checkpoint | UCO | Corporate | Central govt | PSU |
| :--- | ---: | ---: | ---: | ---: |
| 2027-mid | **97.7%** | 0% | 2.3% | 0% |
| 2027-end | **92.5%** | 3.4% | 4.0% | 0.1% |
| 2028-mid | **74.3%** | 18.9% | 6.3% | 0.5% |
| 2028-end | **71.7%** | 18.9% | 7.8% | 1.5% |
| 2029-mid | **68.4%** | 18.6% | 9.8% | 3.2% |

### AVERAGE case

| Checkpoint | UCO | Corporate | Central govt | PSU |
| :--- | ---: | ---: | ---: | ---: |
| 2027-mid | **96.0%** | 0% | 4.0% | 0% |
| 2027-end | **68.4%** | 23.3% | 6.9% | 1.4% |
| 2028-mid | **48.2%** | 36.5% | 8.9% | 6.4% |
| 2028-end | **41.8%** | 32.9% | 9.6% | 15.6% |
| 2029-mid | **34.1%** | 28.4% | 10.0% | 27.5% |

### BEST case

| Checkpoint | UCO | Corporate | Central govt | PSU |
| :--- | ---: | ---: | ---: | ---: |
| 2027-mid | **82.9%** | 11.5% | 5.6% | 0% |
| 2027-end | 26.7% | **55.5%** | 7.9% | 10.0% |
| 2028-mid | 18.5% | **42.7%** | 7.3% | 31.4% |
| 2028-end | 11.4% | 28.1% | 5.4% | **55.1%** |
| 2029-mid | 6.3% | 16.7% | 3.7% | **73.4%** |

---

## 13b. The number that matters — P(switched out of UCO by end-2027)

| Scenario | **P(any switch by Dec 2027)** |
| :--- | ---: |
| WORST | **7.5%** |
| AVERAGE | **31.6%** |
| BEST | **73.3%** |

**At realistic effort, the 2027 switch is a 1-in-3 bet.** It only becomes likely if the corporate campaign starts *before* GATE 2027.

---

## 13c. The timing curve — the single most important finding

Controlled test: conversion held at 50%, only the month the search starts varies.

| Search starts | P(joined by Dec 2027) |
| :--- | ---: |
| Oct–Dec 2026 | **~50%** |
| Jan 2027 | 49% |
| Feb 2027 | 45% |
| **Mar 2027** | **38%** |
| Apr 2027 | 30% |
| May 2027 | 23% |
| Jun 2027 | 16% |
| Jul 2027 | 9% |
| Aug 2027 | 2% |
| Sep 2027 | **0%** |

> **Every month of delay after February 2027 costs ~7 percentage points. Starting in June instead of March halves the probability. Starting in August makes it impossible.**

**Implication: the corporate campaign cannot begin after GATE 2027. It must start alongside it.**

---

## 13d. Modal paths (Dec 2027 → Jun 2029)

| Path | WORST | AVERAGE | BEST |
| :--- | ---: | ---: | ---: |
| Never move (UCO throughout) | **68.5%** | **34.2%** | 6.2% |
| UCO → Corporate | 15.1% | 17.1% | 16.5% |
| UCO → PSU | 2.5% | **14.2%** | 17.3% |
| UCO → Corporate → PSU | 0.4% | 6.2% | **39.3%** |
| UCO → Central govt | 6.0% | 5.0% | 2.4% |
| Central govt only | 3.8% | 4.9% | 2.4% |
| PSU directly | 0% | 0% | 9.8% |

**The dominant BEST-case path is corporate-first, then PSU** — earn ₹16-19L from late 2027, then jump to a township PSU in the 2028-29 cycle when the package matches. That is the highest-probability route to *both* goals.

---

## 13e. The three real options

| Option | What it means | P(2027 switch) | P(PSU by 2029) |
| :--- | :--- | ---: | ---: |
| **A — GATE-first** | GATE hard to Feb 2027, corporate search from March | 32–38% | ~28% |
| **B — Corporate-first** | Corporate prep from now, apply Dec–Jan, GATE becomes a by-product | 50–73% | ~15% |
| **C — Hybrid (recommended)** | 60% corporate / 40% GATE until Feb, pivot fully to corporate in March | **45–55%** | ~25% |

**Why C:** DSA, OS, DBMS, CN, and algorithms are ~60% shared between the two tracks. The only GATE-exclusive content is TOC, compilers, COA, and Digital Logic — about 35% of the paper and ~0% of a corporate interview. Running both until February costs roughly the GATE-exclusive 35%, not the whole ticket.

---

## 13f. Money math

| | 2027 | 2028 | 2029 |
| :--- | ---: | ---: | ---: |
| UCO gross | ₹10.4L | ₹11.7L | ₹12.4L |
| Corporate entry | ₹16–19L | ₹17.5L | ₹19.5L |
| PSU ET | ₹17–22L | ₹19.5L | ₹22L |
| Central govt | ₹11–12.5L | ₹12L | ₹12.8L |

- **Gross delta UCO → corporate: ₹5.6–8.6L/year.**
- **Bond ₹2,00,000** (may be pro-rated — verify with HR).
- **Break-even: 3–5 months of the delta.** The bond is not a real obstacle.
- **Cost of a one-year delay: ₹6–8L gross**, plus one year of age inside the capped window.

---

## 13g. Calendar that actually hits the 2027 deadline

| Window | Action | Non-negotiable |
| :--- | :--- | :--- |
| **Now – Dec 2026** | DSA base (150 problems) · Spring Boot project depth · resume + LinkedIn rebuilt · 40Q aptitude block weekly · NSPCL/ISRO/NICL/DFO as scheduled | Resume must be interview-ready by **31 Dec 2026** |
| **Jan – Feb 2027** | GATE 2027 sprint · DSA to 250 problems · 2 mock interviews | GATE written 7 Feb 2027 |
| **1 Mar 2027** | **Corporate campaign opens.** 15–20 applications/week, every week | First application sent by **7 Mar 2027** |
| Mar – Jun 2027 | Interview loop, 8–15 interviews, iterate on feedback | 10 interviews completed by **30 Jun 2027** |
| Jul – Sep 2027 | Offers, negotiate, choose | Offer in hand by **30 Sep 2027** |
| Oct – Dec 2027 | Notice, bond, relieving letter, join | **Joined by 31 Dec 2027** |
| 2028 onward | PSU applications continue in background; GATE 2028 as free option | Do not stop the PSU pipeline |

---

## 13h. Decision rules (pre-committed)

| Date | Test | If failed |
| :--- | :--- | :--- |
| **31 Dec 2026** | Resume, LinkedIn, GitHub, 150 DSA problems done | The 2027 switch is already gone — accept 2028 and re-plan |
| **7 Mar 2027** | First 10 applications sent | Start the same week regardless of GATE result |
| **30 Jun 2027** | ≥ 8 real interviews completed | Diagnose: applications or conversions? Fix the failing side only |
| **30 Sep 2027** | ≥ 1 offer in hand | Extend to Q1 2028; reassess package expectations |
| **31 Dec 2027** | Joined, or a dated offer letter | If neither, the 2027 goal has failed — declare it and move to the 2028 PSU cycle with full hours |

---

## 13i. Verdict on the 2027 goal

> **A 2027 switch is achievable at roughly 1-in-3 with the current pace, and roughly 1-in-2 to 3-in-4 only if the corporate campaign starts by January 2027 and runs at 10+ interviews per quarter.**
>
> **The PSU cannot deliver 2027. The corporate route can. Run corporate as the exit vehicle and PSU as the upgrade that arrives in 2028-29.**
>
> The single most expensive mistake available is to spend all of 2027 preparing and none of it applying.
