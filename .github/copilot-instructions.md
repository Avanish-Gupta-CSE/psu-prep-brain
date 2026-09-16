# PSU Prep Repository Instructions — GitHub Copilot Workhorse

This repository is Avanish Kumar Gupta's personal PSU / government technical-role preparation system.
It combines persistent prep memory in `.brain/`, source documents in exam folders (`HAL/`, `IOCL/`, `ISRO/`, `CONCOR/`, `MSTC/`, etc.), reusable CS notes in `Notes/Shared-Core/`, and GitHub Copilot customizations under `.github/`.
**Copilot is now the primary workhorse** (migrated from Cursor on 01 Sept 2026 after Berkadia exit). `.cursor/rules/psu-prep.mdc` is retained as historical reference only — this file is the canonical operating contract.

## Start Here — Mandatory Context Loading (Every Conversation)

1. **Read these files first before responding to ANY message:**
   - `.brain/NextSteps.md` — canonical resume point and immediate day-by-day action plan
   - `.brain/Progress.md` — current phase, last session, streak, next goals
   - `.brain/ExamTracker.md` — all exams with dates, status, patterns
   - `.brain/TrackedJobs.md` — all tracked jobs, applications, results, emerging opportunities (MANDATORY check)
   - `.brain/StudyPlan.md` — phase-based schedule
   - `combined-HAL-then-IOCL-plan.md` — **single operational source of truth for Sept 2026** (HAL 06 Sept → IOCL 24 Sept stacked campaign)
2. **Compare the current date with exam dates** before trusting the recorded active phase. Today is 01 Sept 2026 — Phase 6 HAL sprint is live.
3. **Check for job updates (MANDATORY):** review `TrackedJobs.md` and run a rapid web search / aggregator check (`https://www.indgovtjobs.in/`, `iffco.in/careers`, `kribhco.net/careers`, plus each tracked PSU portal) for admit cards, date changes, results, or interview calls. Flag updates immediately in the response header.
4. **Use `.brain/Syllabus.md` and `.brain/WeakAreas.md`** to determine what should be studied next when the user asks about a topic.

## Repository Layout

- `.brain/` — canonical prep state, logs, syllabus tracking, weak areas, motivation, decision audits, and reference notes. **Single shared memory system across all agents.**
- `combined-HAL-then-IOCL-plan.md` — September 2026 stacked campaign plan (HAL 06 Sept → IOCL 24 Sept). Supersedes day allocation in `HAL/5-DAY-SPRINT-PLAN.md`.
- `Notes/Shared-Core/` — reusable CS and GATE-style prep layer shared across exams (DBMS, OS, CN, DSA, COA, Digital Logic, Aptitude, GA, etc.)
- `Notes/DBMS/`, `Notes/DSA/`, `Notes/OS/`, `Notes/CN/` — deep subject notes (DBMS is the strongest asset: 12 files)
- `HAL/` — HAL Design Trainee (CS) sprint: `5-DAY-SPRINT-PLAN.md`, `DRILL-01-OS-COA.md`, `ERROR-LOG.md`, `FORMULA-CARD.md`, `GA-DEFENCE-CAPSULE.md`
- `IOCL/` — IOCL Engineers/Officers (Grade A, CS/IT) — Advt `IOCL/CO-HR/RECTT/2026/01`, CBT 24 Sept 2026
- `ISRO/` — ISRO ICRB Scientist/Engineer 'SC' (CS) — 22 posts, closes 16 Sept 2026
- `CONCOR/` — CONCOR MT/AO (MIS/IT) — 77 posts, window 31 Aug–30 Sept 2026
- `CoalIndiaLimited-PSU/` — CIL MT (Systems) archive + KG course question-bank index (`Paper-2-Tracker.md`) and Paper-1/Paper-2 notes
- `IFFCO/`, `MSTC/`, `HPCL/`, `SPMCIL/`, `STPI/`, `UCOBank/`, `NFL/`, `NMDCSteel/`, `BalmerLawrie/` — exam-specific folders (some closed/archived, some awaiting results)
- `Form-Filling-Dossier/` — structured form-filling assets (academic, category, identity, photos/signatures, work experience, scorecards, resume)
- `Berkadia-Exit-Documents/` — resignation, payslips, Form 16, awards, PF/UAN, joining dossier
- `Resume-Berkadia.tex` — source of truth for career history and interview stories (STMicro + Berkadia + UCO Bank)
- `.github/` — Copilot customizations: `copilot-instructions.md` (this file), `instructions/*.instructions.md`, `agents/*.agent.md`, `prompts/*.prompt.md`
- `.cursor/` — legacy Cursor rules (`psu-prep.mdc`, `hooks/`, `settings.json`) — retained for reference, not canonical

## Current Priority — September 2026 Stacked Campaign (MANDATORY)

- **Career baseline: SECURED — UCO Bank Software Developer (JMGS-I), Kolkata.** Appointment letter 08.07.2026, Berkadia LWD 31 Aug 2026 completed. Every remaining exam is an **upgrade attempt from security**, not survival. Full rationale: `.brain/UCO-BANK-DECISION-AUDIT.md` (verdict: correct decision).
- **Immediate priority: HAL Design Trainee (CS) CBT — Sun 06 Sept 2026, Bengaluru (App No D321947) → IOCL Engineers/Officers CBT — 24 Sept 2026.** Run as ONE stacked campaign, not two sprints. ~73% of IOCL paper is pre-covered by HAL sprint; ~27 marks (Cloud/DevOps, OOP/Web, network security, NoSQL/Linux, Quant+DI) are isolated into 08–13 Sept Delta Week.
- **Admin gates (do not miss):** ISRO ICRB by 08 Sept (closes 16 Sept), CONCOR by 09 Sept (closes 30 Sept). HAL interview 21–25 Sept vs IOCL CBT 24 Sept clash is risk R1 — check call letter 12 Sept.
- **Result watch (no action, just monitor):** CIL MT (147/200 = 73.5% peak), NFL MT (99/150), IFFCO GET CBT2, STPI MTSS, ISP, HLL, Balmer Lawrie.
- **Standing rules from audit:** Do not withdraw any pending application. Opt for leased accommodation over cash HRA at UCO joining. Bond + probation clear ~Sept 2028 (age 28) — re-evaluate then.

## Working Rules

- Keep `.brain/` as the single shared memory system across all agents and sessions.
- Treat `.brain/NextSteps.md` as the canonical immediate handoff file for future logins and agent resumes.
- Store reusable subject notes once in `Notes/Shared-Core/` and reference them from exam folders instead of duplicating content.
- In exam-specific files, separate `Confirmed` facts (advert, portal, admit card) from `Inferred` guidance (pattern, overlap, strategy) — never mix without labeling.
- When updating live prep state, keep `.brain/Progress.md`, `.brain/ExamTracker.md`, `.brain/StudyPlan.md`, and `.brain/NextSteps.md` internally consistent and date-consistent.
- Preserve history in `.brain` files instead of rewriting it away unless clearly obsolete.
- Use `Resume-Berkadia.tex` as source of truth for career claims — do not invent project numbers or role scope.

## Note Creation Guidelines (Active Study Session)

When creating study notes from ebook images, follow these standards consistently:

### File Structure
- Each file starts with: `> 🎯 Target: [what to achieve]` and `> ⏱️ Read time: X minutes`
- Sections in order: Definition → Classification/Types → Key Rules → Examples → Mnemonic → Quick Cheat Sheet → 40s Script → Follow-up Questions
- Mark high-priority topics with `★ HIGH PRIORITY` at the top

### Diagrams
- Use **Mermaid** (`\`\`\`mermaid`) for: hierarchies, classification trees, flowcharts, state machines. Renders on GitHub and VS Code with Mermaid extension.
- Use **ASCII art** for: memory layout diagrams, before/after tables, stack/queue states
- Use **Markdown tables** for: comparison tables, time complexity, feature differences
- Never describe a diagram in words when you can draw it

### Mnemonics — MANDATORY for memory-heavy topics
- Every list of 4+ items MUST have a mnemonic
- Prefer **Hinglish** (Hindi + English mix) — user's first language is Hindi, fluent in English
- Format: bold the first letter of each word in the mnemonic
- Examples of good Hinglish mnemonics:
  - OSI layers: "**P**ehle **D**ata **N**ikalte **H**ain, **T**ransport **S**e **P**rapt **A**ata" (Physical, Data Link, Network, Transport, Session, Presentation, Application)
  - Topologies: "**B**ahut **S**tar **R**ing **T**ree **M**esh **H**ybrid hai" (Bus, Star, Ring, Tree, Mesh, Hybrid)
  - Data flow: "Simplex = Sirf ek taraf, Half Duplex = Baari baari, Full Duplex = Ek saath dono"
- If Hinglish doesn't work naturally, use English mnemonics ("Please Do Not Throw Sausage Pizza Away")

### Interview Scripts
- Every major topic gets a **timed script**: 20s for simple topics, 40s for complex ones
- Scripts are in first person, conversational, complete sentences
- Scripts always end with a concrete example

### Cross-references
- If a topic is already covered in another file, add a `> See also: filename.md` note instead of duplicating
- SQL/DB topics go in `Notes/DBMS/`, data structure topics in `Notes/DSA/`, network topics in `Notes/CN/`, OS topics in `Notes/OS/`

### Time Estimates on README
- Each README.md includes a `⏱️ Read time` per file
- Includes a **Revision Order** section matching the ebook chapter order
- Includes a **Master Cheat Sheet** at the end for day-before revision

### What to ADD Beyond the Ebook
- If ebook content is too thin to answer in 40s, add the gap
- Always add: real-world analogy, the "why it matters" for PSU interview context, and at least 2 follow-up questions with answers
- Flag any topic where ebook has an error or oversimplification with `> ⚠️ Note:`

## Validation

- There is no conventional build or test pipeline for this repository.
- Validate changes by checking file consistency, date consistency, source attribution, and cross-file alignment.
- For customizations, ensure files are placed in the correct `.github/` locations so Copilot can discover them.