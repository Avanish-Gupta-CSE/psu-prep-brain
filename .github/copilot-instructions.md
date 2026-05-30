# PSU Prep Repository Instructions

This repository stores a personal exam-preparation system for PSU and government technical roles.
The workspace combines persistent prep memory in `.brain/`, source documents in exam folders such as `MSTC/`, and GitHub Copilot customizations under `.github/`.

## Start Here

- Read `.brain/NextSteps.md`, `.brain/Progress.md`, and `.brain/ExamTracker.md` at the start of every study or planning request.
- Compare the current date with exam dates before trusting the recorded active phase.
- Use `.brain/StudyPlan.md`, `.brain/Syllabus.md`, and `.brain/WeakAreas.md` to determine what should be studied next.

## Repository Layout

- `.brain/` stores the canonical prep state, logs, syllabus tracking, weak areas, motivation, and reference notes.
- `.cursor/rules/psu-prep.mdc` is the older Cursor-era operating contract and should be reflected in new Copilot customizations.
- `Notes/Shared-Core/` is the reusable CS and GATE-style prep layer shared across exams.
- `HPCL/`, `IFFCO/`, and `MSTC/` hold exam-specific materials.
- `Resume-Berkadia.tex` is the source file for career-history-based interview preparation.

## Working Rules

- Keep `.brain/` as the single shared memory system across all agents.
- Treat `.brain/NextSteps.md` as the canonical immediate handoff file for future logins and agent resumes.
- Store reusable subject notes once in `Notes/Shared-Core/` and reference them from exam folders instead of duplicating content.
- In exam-specific files, separate official information from inferred question patterns or strategy notes.
- When updating live prep state, keep `.brain/Progress.md`, `.brain/ExamTracker.md`, and `.brain/StudyPlan.md` internally consistent.
- Use the current urgent priority unless the user explicitly changes it: HPCL first, IFFCO second, MSTC interview readiness third.

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