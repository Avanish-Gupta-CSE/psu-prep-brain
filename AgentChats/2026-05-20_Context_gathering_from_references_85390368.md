# Context gathering from references

| Metadata | Value |
| :--- | :--- |
| **Chat ID** | `85390368-b3a4-413a-b7d8-77a34035f087` |
| **Created At** | `2026-05-20 06:41:31` |
| **Last Updated At** | `2026-05-20 06:41:41` |
| **Files Touched / Summary** | Read Syllabus.md, AGENTS.md, HR-QUESTION-BANK.md, TECHNICAL-QUESTION-BANK.md, hooks.json |
| **Model** | `composer-2.5` |

---

## 👤 User Message #1

Can you get the context based on @.brain @.cursor @MSTC @CN @DBMS @DSA 
@.github/copilot-instructions.md 

and then come back to me after getting this with your findings

---

## 🤖 Assistant Response

Gathering context from the brain, cursor rules, MSTC track, subject folders, and Copilot instructions.

---

## 🤖 Assistant Response

## Context findings (synthesized)

I read `.brain/`, `.cursor/`, `MSTC/`, `CN/`, `DBMS/`, `DSA/`, and `.github/copilot-instructions.md`. Here is the operational picture.

---

### Critical path (what matters right now)

| Item | Status |
|------|--------|
| **Interview** | MSTC MT **(Systems)** — **21 May 2026, 9:00 AM**, World Trade Centre, Nauroji Nagar, New Delhi |
| **Today (per your env)** | **20 May 2026** → interview is **tomorrow** |
| **Active mode** | **MSTC only** (`.brain/NextSteps.md`, `.cursor/rules/psu-prep.mdc`) |
| **Interview shape** | Plan for **7–15 min**, often **technical-only lightning** (intro → Core-4 basics → done) |
| **Master schedule** | `MSTC/MASTER-PLAN-2026-05-15-to-21.md` — today = revision day; tomorrow = morning micro-plan |

---

### `.brain/` — memory layer

**Canonical handoff order:** `NextSteps.md` → `Progress.md` → `ExamTracker.md` → `StudyPlan.md` → `MSTC/README.md`

**Last logged session (18 May):**
- Ebook-derived notes live under `DBMS/`, `DSA/`, `CN/` (~**22/65** ebook pages done for Core-4).
- CN: README + `01` done; OSI was a friction point (fixed via 40s script + cheat sheet, not full protocol lists).
- **OS notes folder does not exist yet** — biggest Core-4 gap.
- Treat interview as **7–15 min**; prioritize **7-minute lightning** in `MSTC/TECHNICAL-QUESTION-BANK.md`.
- **20 May:** mixed mock + repairs + logistics; **one** YourPedia mock if available (don’t overload travel).

**Active weaknesses (`WeakAreas.md`):** Core-4 fast recall under pressure — DBMS, OS, CN, DSA — daily lightning + repair loops.

**Stale / inconsistent files (worth knowing):**
- `AGENTS.md` still says **HPCL first until 3 May** — contradicts current MSTC-only sprint in `.brain/`.
- `.brain/Syllabus.md` still shows **0%** on DSA/OS/CN topics even though `DBMS/`, `DSA/`, `CN/` READMEs mark many files **Done**.

---

### `.cursor/` — agent contract

- **`psu-prep.mdc`:** MSTC-only planning; load brain + MSTC at start; **web search + cite URLs** for facts; teaching = compressed theory → dry-run → MCQs → direct feedback; interview answers = **40s + 2 follow-ups**; session-end updates to `.brain/` + MSTC trackers + git push.
- **`hooks.json`:** `sessionEnd` runs `brain-sync.ps1` (auto sync hook).

---

### `.github/copilot-instructions.md` — note standards

Aligned with Cursor rules. When creating study notes:
- Structure: target + read time → definition → types → rules → examples → **Hinglish mnemonic** → cheat sheet → **40s script** → follow-ups.
- Diagrams: Mermaid / ASCII / tables (not prose-only).
- Cross-ref instead of duplicate (`DBMS/`, `DSA/`, `CN/`, `OS/`).
- README: revision order + master cheat sheet per subject.

---

### Subject notes progress

| Folder | Done | Gap |
|--------|------|-----|
| **DBMS/** | **12/12** files ✅ (keys, normalization, joins, SQL traps, ACID, ER, RA, FD, aggregates…) | Indexing, concurrency/deadlock-in-DB still on TODO list |
| **DSA/** | **5/5** files ✅ (arrays, LL/stack/queue, trees/graphs, heap/hashing, sorting/complexity) | DP, advanced graph algos marked optional |
| **CN/** | **3** files ✅ (basics, OSI ★, topology) | TCP/IP detail, DNS, HTTP/HTTPS, CRC, routing — all on README TODO |
| **OS/** | **Missing entirely** | Process/thread, scheduling, deadlock, paging, sync — required for Core-4 + lightning bank |

**CN is interview-ready for ebook scope; OS is the hole in Core-4.**

---

### `MSTC/` — interview track

**Source of truth set:**
- `OFFICIAL-INTERVIEW-UPDATE.md` + PDFs
- `Resume-Berkadia.tex` (facts only)
- HR: `HR-QUESTION-BANK.md` (intro script mentor-approved), `CAREER-STORY-BANK.md`, `BEHAVIORAL-QUESTION-BANK.md`
- Technical: `TECHNICAL-QUESTION-BANK.md` (**7-minute lightning mode** + 15–20s scripts)
- Company: `MISSION-VISION.md`, `Company-MSTC-Research/`
- Execution: `MASTER-PLAN-2026-05-15-to-21.md`, `MOCK-INTERVIEW-TRACKER.md`, `PROJECT-DEEP-DIVE.md`

**HR status:** 30–40s intro locked; optional swap **Java → React/Node/TypeScript** if you want less Java grilling.

**Technical drill priority:** Lightning set rotates DBMS / OS / CN / DSA — definition → one tradeoff → one example → stop.

---

### Timeline vs plan (where you are)

```
15–18 May  → Core-4 deep + timed mocks (planned)
19 May     → Travel Delhi (light revision + company bullets)
20 May     → YOU ARE HERE — revision day (2 mixed mocks, HR cases, logistics, early sleep)
21 May     → Interview 9 AM (warm-up 6:00–7:15, arrive ≥30–45 min early)
```

**Open loops:** call letter final checklist; mock logging may be thin (many plan days show 0 questions logged).

---

### Cross-cutting risks (from history + current state)

1. **OS not written** while panel may ask process/thread, deadlock, paging in 15–20 seconds each.
2. **CN beyond OSI** (DNS, TLS, type-URL flow) still TODO in `CN/` but covered in `TECHNICAL-QUESTION-BANK.md` lightning scripts.
3. **Pressure blanking** (18 May session) — fix = scripts + retakes, not more theory.
4. **Doc drift** — `Syllabus.md` / `AGENTS.md` not updated to match MSTC sprint and new note folders.

---

### What agents should do on next message (if you want execution)

1. Treat **20 May master plan** as the schedule (mixed mock → repair → HR cases → logistics).
2. Use **`TECHNICAL-QUESTION-BANK.md` lightning mode** as the primary drill, not deep GATE theory.
3. Prefer **cheat sheets + 40s scripts** from `DBMS/`, `DSA/`, `CN/`; pull OS from Q-bank until `OS/` notes exist.
4. Do **not** switch to HPCL/IFFCO unless you explicitly ask — `.brain` overrides stale `AGENTS.md` priority text.

---

Tell me what you want next: **today’s revision run-through** (lightning mock), **OS crash notes** in one session, **HR warm-up**, or **logistics checklist** for tomorrow.

---
