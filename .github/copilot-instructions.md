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
- `Shared-Core/` is the reusable CS and GATE-style prep layer shared across exams.
- `HPCL/`, `IFFCO/`, and `MSTC/` hold exam-specific materials.
- `Resume-Berkadia.tex` is the source file for career-history-based interview preparation.

## Working Rules

- Keep `.brain/` as the single shared memory system across all agents.
- Treat `.brain/NextSteps.md` as the canonical immediate handoff file for future logins and agent resumes.
- Store reusable subject notes once in `Shared-Core/` and reference them from exam folders instead of duplicating content.
- In exam-specific files, separate official information from inferred question patterns or strategy notes.
- When updating live prep state, keep `.brain/Progress.md`, `.brain/ExamTracker.md`, and `.brain/StudyPlan.md` internally consistent.
- Use the current urgent priority unless the user explicitly changes it: HPCL first, IFFCO second, MSTC interview readiness third.

## Validation

- There is no conventional build or test pipeline for this repository.
- Validate changes by checking file consistency, date consistency, source attribution, and cross-file alignment.
- For customizations, ensure files are placed in the correct `.github/` locations so Copilot can discover them.