# Next Steps & Handoff (PSU Exam Preparation Reboot & Sprints)

Last updated: **October 21, 2026 (travel night)** — 🚕 **Left Bareilly by private cab → IGI Delhi → 22:00 flight to Kolkata (lands ~00:30 Thu 22 Oct).** 🎫 **NSPCL admit card PRINTED — exam Sun 25 Oct, Kolkata.** **ISRO 29 Oct = KOLKATA, SHIFT 1.** ✅ **GATE 2027 SUBMITTED.** 🎯 **Grand plan written: `CAREER-MASTER-PLAN-2026-2028.md`.** Previous: **RESET 18 Oct** — IOCL NOT selected (Sec A 37.75/50, Sec B 10/50).

**🌐 Public dashboard:** https://avanish-gupta-cse.github.io/psu-prep-brain/ — the full plan, cutoffs and probability models, published 21 Oct 2026.

This is the canonical resume-point file for any future login, agent, or chat system. 
Read this file first to understand the current priority queue and the immediate day-by-day action plan.

---

## 🚕 §0 — LIVE STATE: 21 Oct 2026 (travel night)

| Item | Status |
| :--- | :--- |
| **Where** | Private cab, Bareilly → **IGI Airport Delhi**. Flight **22:00 → Kolkata, lands ~00:30 Thu 22 Oct**. |
| **Home visit** | Closed. Next home trip only after NSPCL + ISRO are done. |
| **NSPCL Sr. Asst. Engineer (IT/ERP)** | ✅ **EXAM DONE 25 Oct.** 120 Q: Subject 80 + Aptitude 40 · −0.25 · separate cutoff in EACH section. **2 IT posts = UR 1 + OBC-NCL 1** · final = **85% test + 15% interview** · ₹5L / 4-yr bond. **Result expected ~1–4 Nov** (2024: 8 days to shortlist, 21 to interview). **Watch email only — nothing to submit.** |
| **ISRO ICRB SC (CS)** | **Thu 29 Oct — CONFIRMED. KOLKATA, SHIFT 1.** Admit card to download 22–23 Oct. **CL to be applied Thu 22 AM.** |
| **NICL AO (IT Specialist)** | 🟢 **DECIDED — APPLY.** 321 posts (IT: 11) · closes **28 Oct** · Phase-I **17 Nov**, Phase-II **22 Dec** · ~₹1.14 L/mo. Form Fri 23 Oct. |
| **Cabinet Secretariat DFO (Technical)** | 🟢 **DECIDED — APPLY.** Advt `02/2026` · 250 posts (**112 CS**) · Level-7 · **nil fee** · **by POST, must reach 15 Nov** → Post Bag No. 001, Lodhi Road HO, New Delhi-110003 |
| **Grand plan** | [`CAREER-MASTER-PLAN-2026-2028.md`](CAREER-MASTER-PLAN-2026-2028.md) — plan of record for the exit. **GATE 2028 = the real attempt, not 2027.** |
| **Java / UCO Realty** | Only curriculum that exists. No bank-granted study time. Plan = `uco-realty/.brain/Plan_v2_20Oct_to_25Oct.md` + §0b below. |

### §0a — ✅ GATE 2027: SUBMITTED (user-confirmed 21 Oct)
- **Registration done before the 12 Oct late window.** Gate **G1 ✅ closed.**
- **✅ Papers registered: CS + DA** (both). Two doors: **CS** for PGCIL/NTPC/IOCL ET; **DA** for Data-Science/AI posts + DFO-DA (10 posts).
- **⚠️ Still to capture:** Application No. · exam city · admit-card date.
- **Strategic consequence (see master plan §2):** GATE 2027 is a **rehearsal** (3.5 months out, current AIR 29,099). The **real attempt is GATE 2028 (Feb 2028)** — it lands exactly when the bond clears (Sept 2028) and inside the OBC age window (28 at exam, caps ~29–30).

### §0b — Java rule (settled 21 Oct)
The bank will not give study hours. Therefore **Java is learned inside the workday, not outside it**:
1. **30 min at end of workday** — re-read the one file you touched today, out loud, one sentence per annotation.
2. **Hand-copy 7 core snippets** (already listed in the learning tracker) in the commute/pre-sleep slot. ~3 h total.
3. **Sat 20-min defence drill** — say out loud: URL → Controller → Service → Repository → Oracle, and why `@Transactional` matters.
4. **Keep a "don't understand my own code" list.** Ask one specific question per morning. Specific questions read as competence; silence reads as risk.
5. **The bar is not Spring expertise.** It is: no self-approval, zone isolation, transactions, tests, no secrets in code. That is Plan v2 §4 — ship it and the "he doesn't know Spring" risk largely disappears.


### §0f — 🧱 JOB STABILISATION: stack ramp-up (set 21 Oct) → [`UCO-STACK-RAMP-UP-PLAN.md`](UCO-STACK-RAMP-UP-PLAN.md) · [web](https://avanish-gupta-cse.github.io/psu-prep-brain/stack.html)
- **The real gap:** code was written with AI assistance and cannot yet be fully defended. Must now author code unaided, at a bank, with **no extra hours**.
- **Thesis: not more hours — reconstruction.** 15 deliberate min/day beats 2 h of tutorials because the artefact rebuilt is the system defended tomorrow.
- **Cost: ~4 h/week, all inside 10:00–18:30.** 30 min end-of-day explain-aloud + 10 min gap note + 5 min journal + 20 min Sat drill + 15 min Sun review. **No evenings, no weekends.**
- **Verified stack:** Java **17** · Spring Boot **3.2.5** (Jakarta, not javax) · Spring Data JPA · Spring Security 6 · **jjwt 0.12.5** · Oracle XE 21c / ojdbc11 · POI 5.2.5 · React **19.2** + TS + Vite 8 · 32 Java files · plain SQL migrations.
- **Three gotchas:** `jakarta.*` not `javax.*` · no `WebSecurityConfigurerAdapter` in Security 6 · jjwt 0.12 API changed. **Any tutorial older than 2023 teaches a dead framework.**
- **12 weeks from Mon 26 Oct:** W1 terrain map → W2 framework → W3 endpoint unaided → W4 service/tx → W5 JPA → W6 Oracle/EXPLAIN → W7 **security audit** → W8 **fix adminList fails-open + submit IDOR** → W9 tests → W10 React → W11 deploy → W12 **ship and defend a feature**. W13+ GATE taper.
- **Day-90 goal:** author a small feature end-to-end — design, code, test, document, and survive five "why" questions.
- **Rubric target:** 3/5 by day 90, 4/5 by day 180. Below 2 at day 90 → repeat weeks 3-6.
- **Exposure rule:** never bluff. *"Let me trace it and come back by end of day"* — then do it. The bank rewards reliability over brilliance.

### §0e — 🎯 2027 SWITCH DEADLINE (set 21 Oct) → [`GATE-DECISION-MODEL.md`](GATE-DECISION-MODEL.md) §13
- **User constraint: leave UCO within 2027.** PSU cannot deliver that (exam→interview→joining chain is 7-10 months; P(PSU by Dec 2027) = 0-10%). **2027 is a corporate deadline.**
- **P(any switch by Dec 2027):** WORST **7.5%** · AVERAGE **31.6%** · BEST **73.3%**.
- **The timing curve (conversion fixed at 50%):** search starting Dec-26 → 50% · Mar-27 → **38%** · May-27 → 23% · Jul-27 → 9% · Sep-27 → **0%**. **~7 points lost per month of delay after Feb 2027.**
- **Recommended: Option C (hybrid).** 60% corporate / 40% GATE until Feb 2027, then pivot fully to corporate on 1 Mar 2027. Shared curriculum (DSA/OS/DBMS/CN/Algo) is ~60%; only TOC/COA/DL/compilers are GATE-exclusive.
- **Hard milestones:** resume + 150 DSA by **31 Dec 2026** · first applications **7 Mar 2027** · 8+ interviews by **30 Jun 2027** · offer by **30 Sep 2027** · joined by **31 Dec 2027**.
- **Money:** UCO ₹10.4L → corporate ₹16-19L = **+₹5.6-8.6L/yr**; bond ₹2L recovered in **3-5 months**. A one-year delay costs ₹6-8L plus a year inside the age-capped window.

### §0d — 🧮 Strategy verdict, REVISED 21 Oct evening → [`GATE-DECISION-MODEL.md`](GATE-DECISION-MODEL.md) §11
- **Corrected position:** GATE is **not** a competing track — the GATE syllabus **is** the CBT technical syllabus. It is the curriculum, not the target.
- **His verified technical band:** STPI 64.0% · NFL Disc 69/100 · HLL 62.5% · CIL 73.5% · IOCL Sec A **37.75/50 (75.5%)**. Median ≈ **72%** — the ceiling, and not enough. He is right: this is breadth, not aptitude alone.
- **Aptitude still counts (cheap, not optional):** NFL 30/50 (60%) vs IOCL **10/50 (20%)**. IOCL with perfect technical + 20% aptitude = 60/100 → still below cutoff.
- **The free lever nobody used — seat arithmetic:** 1 OBC seat ⇒ need 84-88%. 6-15 seats ⇒ 72-76%. 15+ ⇒ 68-72%. **Same 73% is dead in a 1-seat exam and competitive in a 15-seat exam.** STPI and NFL both had **1 OBC-NCL seat**.
- **Hawk model (150k trials, 6 exams/yr, P(offer|shortlist)=25%):** 24-month P(PSU offer) = **29.8%** (300h) · **44.2%** (450h) · **53.1%** (600h) · **58.9%** (750h) · **62.9%** (900h). vs **23.7%** for GATE-only at 650h.
- **GATE is now a by-product:** same hours → 450h ≈ 44.6 marks (AIR ~5,957) · 600h ≈ 48.3 (~3,745) · 900h ≈ 54.2 (~1,767). Enough for DFO (112 seats), not for PGCIL in a normal year.
- **Rules:** (1) 100% of GATE topics at **80% depth**, skip TOC proofs / compiler-opt internals / advanced COA. (2) 150h aptitude, weekly timed block. (3) **Count OBC-NCL seats before applying** — 0-2 free only, 3-5 apply, 6+ prioritise. (4) 6-9 applications/yr across 15 portals.
- **K3 revised:** GATE 2027 < 45 **no longer cancels** the strategy — it only confirms GATE is the receipt, not the product.

### §0c — Leave budget (settled 21 Oct)
- **12 CL/year = 6 (Jan) + 6 (Jul)** — the only discretionary instrument. **SL 12** (don't plan). **PL ~30 accruing — ⚠️ verify if availed during probation: one email, potentially +30 days.**
- **Non-working ≈ 88–91 days/yr** (52 Sundays + 24 off-Saturdays + ~12 weekday holidays). **~100 with CL.**
- **Exams are Sundays.** NSPCL Sun · NICL Sun · GATE Sun · PGCIL/NTPC/IOCL CBTs Sun · **DFO postal = 0 days**. Only ISRO 29 Oct (Thu) costs 1 CL.
- **Budget:** 5 interviews/DV · 2 weekday CBTs · 2 family · 3 study blocks · **0 for practice exams.**
- **3-day rule:** a CL must buy a 3–5 day block. Best 2027 block = **Sat 23–Tue 26 Jan (1 CL → 4 days)**. Biggest = **Durga Puja (2 CL → 7–8 days)**.
- **Capacity without extra leave ≈ 900 h/yr** — the 1,000 h/GATE target is reachable with **zero** additional leave. Full detail: master plan **§12**.

## ✅ Career Baseline: SECURED — and now EMPLOYED (Floor, in post)

**UCO Bank Software Developer (JMGS-I), Kolkata — JOINED 28 SEPTEMBER 2026.** Berkadia LWD completed 31 August 2026. Currently in **induction at the Staff Training Centre (STC), Salt Lake**; working posting thereafter = **DIT (Dept. of IT), Head Office-2, Salt Lake Sector-1** — not a branch.
**Positioning:** UCO is the **floor and the funding source**, not the destination. Every remaining exam is an **upgrade attempt from inside a paid officer post**.
Full accept-vs-decline reasoning: [`UCO-BANK-DECISION-AUDIT.md`](UCO-BANK-DECISION-AUDIT.md) — **Verdict still holds: correct decision (as floor).**
**New (01 Oct):** containment + structured-exit plan → [`../UCOBank/PHASE-8-TRAINING-AND-EXIT-STRATEGY.md`](../UCOBank/PHASE-8-TRAINING-AND-EXIT-STRATEGY.md)

Standing rules arising from that audit:
- **Do not withdraw any pending application.** ISRO, CONCOR, CIL, NFL, HLL and every new CS/IT PSU notification continue.
- **HARD RULE (unchanged):** Do **NOT** resign without an **appointment letter physically in hand.** UCO bond = 2 years, ₹2,00,000 penalty (≈2.3 months of gross — a **price list, not a prison**; also check the signed bond deed for a govt/PSU-transfer waiver).
- **NOC reality (key relief):** applying and **writing** PSU exams needs **no NOC**. NOC is only needed at **interview / document-verification / joining** stage. **The exam pipeline is open — keep writing exams.**
- **Opt for leased accommodation over cash HRA** (worth ₹2.16–2.64 LPA tax-free vs ₹6,133/mo taxable).
- **Bond + probation clear ~September 2028** (age 28).
- ~~Collect the Berkadia relieving letter (~11 Sept)~~ ✅ **RECEIVED 15 Sept 2026** (relieving letter + service certificate, both dated 03 Sept 2026, relieved w.e.f. close of business 31 Aug 2026). Filed in `Berkadia-Exit-Documents/Letters/`. **ACTION: reply to UCO Bank HR with both PDFs — draft ready at `UCOBank/RELIEVING-LETTER-REPLY-EMAIL.md`, send by 16–17 Sept.**

---

## 🏦 PHASE 8 — IN POST AT UCO BANK (from 28 Sept 2026)

| Item | Detail |
| :--- | :--- |
| **Joined** | **28 September 2026 (Mon)** — UCO Bank STC, Plot GE-8, Sector-III, Salt Lake, Kolkata 700106 |
| **Current phase** | **Induction / STC training** (Week 1 done as of 01 Oct) |
| **Hours & offs** | **10:00 AM – 6:00/6:30 PM**, 5 days · **2nd & 4th Sat + all Sundays off** · WB public holidays |
| **Working posting** | **DIT, HO-2, Salt Lake Sector-1** (after training) — enterprise Java/APIs, CBS/Finacle integration, security audits. **Zero public dealing.** |
| **App ID** | `7241178423` · Software Developer JMGS-I (Specialist Cadre) |
| **HR contact** | `hohrd_calcutta@ucobank.in` · 033-4455-7379 |
| **Pay** | Gross ₹86,589/mo (cash-HRA) \| ~₹13.4–14.4 LPA effective (lease + NPS 14%) |
| **Policy docs to obtain** | Leave policy (probationer) · exam leave · LWP rules · **copy of the signed bond deed** |
| **Strategy file** | [`UCOBank/PHASE-8-TRAINING-AND-EXIT-STRATEGY.md`](../UCOBank/PHASE-8-TRAINING-AND-EXIT-STRATEGY.md) |

### ⚠️ Reported friction (01 Oct) — and how to read it
- **Hindi-dominant working/social language at STC** → *this is the training-centre batch, not the job.* Bank policy = local language (Bengali) in WB + **English for technical/official documentation**; **DIT work runs in English.** Judge DIT by DIT.
- **Leave hard to get** → normal during induction; formal instruments (CL/SL/EL, exam leave, LWP) not yet used. **Get the policy in writing.**
- **Wants out** → valid signal to **build the exit plan**, not to execute an exit today.

### ❌ Missed: NMDC Steel ET CBT — 01 Oct 2026 (Ranchi)
Pre-agreed guardrail (15 Sept): *"attend only if induction leave is sanctioned; do not jeopardise probation"*. Leave unavailable in Week 1 → **skipped by design.** Logged and closed.

### 🎯 Containment + Exit — the plan in one block
| Lever | Detail |
| :--- | :--- |
| **Fund it** | Salary funds the exit; every month = ₹86k + NPS toward the plan. **Frame = "funded", not "trapped".** |
| **Keep the pipeline open** | **Writing PSU exams needs NO NOC** — only interview/DV/joining do. Keep applying and writing. |
| **Widen the door** | **GATE 2027** (score valid **3 years**) unlocks PowerGrid/NTPC/GAIL/BARC/NBCC/NHPC/SJVN/PFC/REC ET + IIT M.Tech. |
| **Daily rhythm** | 1h morning + 1h evening on weekdays; 4–5h each on 1st/3rd Sat + Sunday. **Floor 12–15 h/week.** |
| **Build the moat** | Finacle/CBS + enterprise Java at DIT = rare "banking-domain IT" profile. Leverage inside *and* outside. |
| **Never** | Resign without an offer in hand. |

### 🗓️ Decision Gates
| Gate | Date | Decision |
| :--- | :--- | :--- |
| **G1** | **5 Oct 2026** | ⚠️ **GATE 2027 form — URGENT** (12 Oct w/ late fee) |
| **G2** | by 15 Oct 2026 | Obtain leave policy + **bond deed copy** in writing |
| **G3** | 1 Dec 2026 | Soft review: is the discomfort STC-shaped or job-shaped? |
| **G4** | 6–21 Feb 2027 | GATE 2027 exam (no NOC needed) |
| **G5** | 19 Mar 2027 | GATE result → target list locked |
| **G6** | **31 Mar 2027** | **THE GATE — commit-or-stay with data** |
| **G7** | 1 Nov 2027 | 13th BPS revision (~15–17%) — re-run the maths |
| **G8** | ~Sept 2028 | Bond clears — free exit, age 28 |

> **Realistic exit window: ~Apr–Jul 2027** (PSU ET cycle via GATE 2027) — **~9–10 months from today.**

---

## 🧳 Travel — COMPLETED (09 Sept 2026)

| Leg | Date | Flight | Arrival | Status |
|---|---|---|---|---|
| **Bengaluru → Hyderabad** | **07 Sept** | **06:30 AM** | ~09:30 AM | ✅ Done |
| **Hyderabad → Bareilly** | **09 Sept** | **06:35 AM** | 11:30 AM | ✅ Done — **back at Bareilly home desk same day** |
| **Bareilly Home Sprint** | **09 Sept → 23 Sept** | — | — | 🔥 **LIVE NOW** — full-throttle IOCL sprint (~125+ focused hours) |

---

## 🚨 Immediate Priority: IOCL (24 Sept) SOLE FOCUS — HAL Closed 09 Sept

**HAL Design Trainee (CS) CBT 06 Sept (Bengaluru, App No D321947) — result 09 Sept: DID NOT MAKE THE CUT.** HAL track closed; interview 21–25 Sept clash (risk R1) is moot.
**Canonical September plan: [`combined-HAL-then-IOCL-plan.md`](../CoalIndiaLimited-PSU/combined-HAL-then-IOCL-plan.md)** — IOCL sections only now.

### 📅 IOCL Final Sprint — 18 → 24 Sept 2026 · EXAM IN BAREILLY 🎫

**🎫 Admit card received 18 Sept 2026:**
- **Roll `1171000327` · Password `41090186` · Reg `839223297` · Venue Code `12015`**
- **Date: 24 Sept 2026 (Thu) · Reporting 12:30 PM · Gate closes 13:00** → exam ~13:30–15:30
- **Venue: ION Digital Zone IDZ Dohna** — Shri Siddhi Vinayak Institute of Technology, 10 km milestone, Nainital Road, near Dohna Rly Stn, Bareilly UP 243202 (**home city — no travel**)
- **3h buffer rule:** study HALTS **09:30** on exam day; 09:30–12:30 = shower/food/docs/travel/settle.
- Carry: printed call letter + photo affixed & signed · original photo ID + photocopy · blue/black ball pen.

**Why replanned again (21 Sept 12:00 PM):** 20 Sept + 21 morning lost (only DL 3.2 ✓ + 3.3 partial: SOP/POS · function-counts · functional completeness). **V8 FINAL — 3-day sprint.** Window: **21 Sept 12:00 PM → 24 Sept 09:30 AM = ~70h real → ~44h study** (Mon ~12h · Tue ~15h · Wed ~15h · Thu skim 2.5h). All 5 KG courses re-scraped 21 Sept — counts stable (CIL 2,940/1,235/5,180 · P2 1,802/3,202 · P1 294/707 · TS 23+15). **Compiler cut (5.5%); Mock-2 → 2× 20Q speed sets.** Full plan: `IOCL/PROGRESS-TRACKER.md` (v3) + tracker site v8.

**Progress (23 Sept 7:30 PM):** DL 3.1 ✓ · 3.2 ✓ · 3.3 ✓ · **DL 3.4 K-map core done — K-Map Structure & PIs 9/35 (26%)** (parts 1–3, POS K-map, minimal expression, grouping rules, don't-cares, practice). Remaining: ~7 short videos + 12 PYQs. **All other subjects = ZERO.** Status unchanged since 22 Sept 10 AM (22–23 Sept lost: family episode → Motivation.md Confidence Reset; HLL merit list gave confidence but no study hours). **~14h left to the 09:30 stop.**

**🔁 V10 — QUESTION-FIRST MODE (standing method from 23 Sept):**
1. **ATTEMPT** a mock / PYQ set / PQ set (mark every Q: ✅ · 🟡 · ❌)
2. **HARVEST** every 🟡/❌ → grouped by topic
3. **ASK ME** (paste the question or name the topic)
4. **I RETURN** — exact subtopic + video titles + durations + the PYQ/PQ drill from **`IOCL/KG-VIDEO-INDEX.md`**
5. **FIX** — those videos at 2x → **re-attempt immediately**
6. **LOG** — one line (rule + trap) → one-pager

**Guardrails:** max 2 videos per gap · ≤25 min video per gap · always re-attempt · **never** open a lecture "to cover a subject".

**V10 Plan — Wed 23 (today) → Thu 24:**
* **Wed 23:** **MOCK-1 full 100Q/120m** (gap-discovery engine) → **harvest** list → **gap-fill round 1** (OS → DBMS → CN → DS → COA → DL) → dinner → **round 2 + DL 3.4 close** (12 PYQs → DL ✅) → Aptitude 20 Qs → one-pagers + pack bag → **sleep 01:00**.
* **Thu 24 — EXAM DAY:** one-pager skim 07:00–09:30 → **HARD STOP 09:30** → docs 10:15 → leave 10:45 → **REPORT 12:30 PM** IDZ Dohna. Target: **gates secured** (30/75 + 10/25 + 45/100).
* **Skip-if-short:** EngM → Algo → TOC → COA-deep. **Compiler = leave blank** (5.5% ≈ 4 Qs).
* **Workout:** Wed = walking breaks only (no gym); Thu = rest.

**🧰 NEW TOOLING (23 Sept) — reusable for ISRO/CONCOR too:**
* **`IOCL/KG-VIDEO-INDEX.md`** (348 KB) — **5,075 videos · 693h · 5,145 PYQs · 8,475 PQs** indexed at module → topic → subtopic → **video title + duration** level, across all 5 owned courses. Includes the **GAP-FILL PROTOCOL** at the top.
* **`tools/kg-index.json`** (881 KB) — machine-readable version for precise lookups.
* **`tools/kg_video_index.py`** — re-runnable scraper (KG public API) to refresh the index.
* **Verified lookups:** *"subnetting"* → `CN → IP Addressing > Subnetting & FLSM Design` (Basics 11m · Example 5m · VLSM 6m · CIDR 4m) · *"banker"* → `OS → Deadlock > Avoidance & Banker's Algo` (11m).

**Tracker (LIVE):** **https://avanish-gupta-cse.github.io/psu-prep-brain/tracker/** — `LS_KEY='iocl-final-tracker-v8'`, 4 days / 36 tasks. **Countdown targets `24 Sept 12:30 PM`.**
- **Local fallback:** `docs/tracker/index.html` via `file://` or `python3 -m http.server 8766 --directory docs/tracker`.
- ⚠️ **Progress is per-browser `localStorage`** — hosted and local copies track separately. Use **Export JSON** to move state; push to `main` to publish code changes.

---

### 📅 Upcoming Exam Timeline (September – October 2026)

| Date | Exam / PSU Target | Location | Status | Action / Focus |
| :--- | :--- | :--- | :--- | :--- |
| **06 Sept 2026 (Sunday)** | **HAL Design Trainee (CS)** | Bengaluru | **❌ CBT DONE — DID NOT MAKE CUT (result 09 Sept)** | Closed; carry lessons to IOCL |
| **24 Sept 2026 (Thu) · report 12:30 PM · BAREILLY** | **IOCL Engineers/Officers (CS/IT)** | **Bareilly (IDZ Dohna)** | **🎫 ADMIT CARD IN HAND — Roll `1171000327`** 🟢 | **SOLE FOCUS — MAHARATNA PSU TARGET (100 MCQs, ₹18.4 LPA)** 🔥 |
| **Late Sept / Oct 2026** | **RCFL MT (Information Tech)** | TBD | Applied (Advt: 16022026) | Navratna PSU (5 Posts) |
| **Late Sept / Oct 2026** | **SPMCIL Assistant Manager (IT)** | TBD | Applied (Advt: 02/2026) | Mini-Ratna (E-1 Level, 120 Qs) |
| **October / Nov 2026** | **ISRO ICRB Scientist/Engineer 'SC' (CS)** | 37 Cities | To Fill by 16 Sept 2026 | Group A Gazetted (Level 10, 80 Tech + 15 Apt) |
| **October / Nov 2026** | **CONCOR MT / AO (MIS/IT)** | TBD | To Apply (Opens 31 Aug) | Navratna CPSE (Ministry of Railways) |
| **September 2026** | **UCO Bank SO (Specialist Cadre)** | Kolkata | Selected & Joining Approved | Software Developer JMGS-I |

---

### 📋 Active Application Queue (August – September 2026)

| Target / Focus Area | Key Objectives | Status / Action |
| :--- | :--- | :--- |
| **IOCL Engineers/Officers (Grade A - CS/IT)** | Advt: IOCL/CO-HR/RECTT/2026/01. 22 Posts (4 OBC, 11 UR). Pay: ₹50k-160k (CTC ₹18.4 LPA). | **FILLED ON 30 AUG 2026** 🟢 (`IOCL/`) |
| **ISRO ICRB Scientist/Engineer 'SC' (CS)** | Advt: ISRO:ICRB:03(EMC):2026. 22 CS Posts (Level 10, ₹56.1k basic). Closes 16 Sept 2026. | **✅ SUBMITTED 16 SEPT 2026** — App No `ICRBS260037880`, ISRO+PRL, ₹750 paid, centres Kolkata/Ranchi/Delhi-NCR (`ISRO/ICRB-SC-CS-Application-ICRBS260037880.pdf`) |
| **CONCOR MT / Assistant Officer (MIS/IT)** | Advt: 05/2026. 77 Posts (MT MIS: 3, AO MIS: 2). Window: 31 Aug – 30 Sept 2026. | **OPENS 31 AUG (10 AM)** 🟢 (`CONCOR/`) |
| **SPMCIL Assistant Manager (IT)** | Advt: 02/2026. 24 Posts (AM IT: 2 Posts, E-1 Level). Written (75%) + Interview (25%). | **TRACKED FOR CBT** 🟢 (`SPMCIL/`) |
| **CERT-In Scientist 'B' (MeitY)** | Advt: CERT-In/SCB/2026/1. 83 Posts for CS/IT, Level 10 Pay. **App No: 261030011869**. | **SUBMITTED SUCCESSFULLY** 🟢 |
| **HAL Design Trainee (CS)** | Advt: HAL/CHRC-TM/RECT-02/2026. CBT 06 Sept 2026. | **❌ CLOSED — did not make cut (result 09 Sept)** |
| **Coal India Limited MT (Systems)** | Exam given on 24 Aug. Verified Raw Score: **147 / 200** (73.5%). | **AWAITING CBT MERIT LIST** 🔥 |
| **Berkadia Notice Period Exit** | System handovers; final exit formalities (LWD: 31 Aug 2026 WFH) | Active |
| **UCO Bank SO Onboarding** | Joining preparations for Kolkata (JMGS-I Software Developer) | September 2026 Batch |

---

## 📊 Administrative & Handoff Status

1. **System & Workspace Restoration**: Fully completed on 24 August 2026. `C:\Programs\` (1.69 GB, 9,376 items) and all personal project repositories restored and verified.
2. **CERT-In Scientist 'B' (MeitY)**: Successfully submitted on 17 August 2026 (Application No: `261030011869`). Confirmation page saved to `C:\Programs\Learning\Gov jobs\ICERT\ConfirmationPage-261030011869.pdf`.
3. **ISRO Scientist/Engineer 'SC' (CS)**: Application completed on 17 August 2026 using GATE 2026 CS Score (350) and GATE Scorecard (`GATE_2026_CS_Scorecard_Avanish.pdf`, 358 KB).
4. **HAL Design Trainee CS**: CBT 06 Sept 2026 (App No: `D321947`). Result 09 Sept 2026 — did not make the cut. Track closed.
5. **HLL Lifecare MT Exam**: Test date 23 August 2026 in Lucknow. Flights booked.
6. **ISP SPMCIL Supervisor IT Exam**: Test date 19 August 2026 in Bangalore.
7. **Coal India Limited (CIL) MT (Systems)**: CBT date 24 August 2026 in Bangalore.
