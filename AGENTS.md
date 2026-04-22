# PSU Prep Agents Contract

This repository is a personal PSU preparation workspace, not a software product.
All agents must optimize for exam readiness, memory continuity, and clear separation between shared prep and exam-specific prep.

## Shared State

- Treat `.brain/` as the canonical memory layer for cross-session and cross-agent state.
- Before planning or teaching, read `.brain/NextSteps.md`, `.brain/Progress.md`, and `.brain/ExamTracker.md` first.
- Use the current date to determine the active sprint and verify that the active phase in `.brain` is still correct before acting on it.
- Write session outcomes back into `.brain` when the work changes the student's prep status.

## Current Priority Rules

- Until the HPCL CBT on 3 May 2026, prioritize `HPCL/` and `Shared-Core/` over everything else.
- Treat `IFFCO/` as the next major target and keep a parallel but smaller track running for it.
- Treat `MSTC/` as an interview-readiness track while waiting for result updates.
- Do not let MSTC interview prep displace the HPCL sprint unless a new MSTC result or interview event is added.

## Content Boundaries

- Put reusable CS fundamentals in `Shared-Core/`.
- Put exam-specific framing, schedules, and source tracking in that exam's folder.
- Keep official facts and inferred patterns separate in every exam folder.
- Use `Resume-Berkadia.tex` as the source of truth for career history and interview stories.

## Sync Rules

- If an exam folder changes priorities, update `.brain/Progress.md`, `.brain/ExamTracker.md`, and `.brain/StudyPlan.md` as needed.
- If the immediate resume point changes, update `.brain/NextSteps.md` in the same session.
- If weaknesses are identified through mocks or drills, update `.brain/WeakAreas.md`.
- If preparation logs or mock scores are added, update `.brain/MockTestLog.md`.
- Avoid duplicating the same note in multiple places unless the framing materially changes by exam.

## Writing Style

- Keep notes crisp, scannable, and operational.
- Prefer checklists, compact tables, question banks, and day-by-day plans over long prose.
- Mark research sections as `Confirmed` or `Inferred` whenever the source confidence differs.