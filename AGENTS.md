# PSU Prep Agents Contract

This repository is a personal PSU preparation workspace, not a software product.
All agents must optimize for exam readiness, memory continuity, and clear separation between shared prep and exam-specific prep.

## Shared State

- Treat `.brain/` as the canonical memory layer for cross-session and cross-agent state. **Copilot is now the primary workhorse** (migrated from Cursor 01 Sept 2026); `.cursor/rules/psu-prep.mdc` is historical reference only.
- Before planning or teaching, read `.brain/NextSteps.md`, `.brain/Progress.md`, `.brain/ExamTracker.md`, `.brain/TrackedJobs.md`, and `combined-HAL-then-IOCL-plan.md` first.
- Use the current date to determine the active sprint and verify that the active phase in `.brain` is still correct before acting on it. Today is 01 Sept 2026 — Phase 6 HAL sprint is live.
- **Mandatory pre-session check:** review `TrackedJobs.md` and run a rapid web/aggregator check (`indgovtjobs.in`, `iffco.in/careers`, `kribhco.net/careers`, plus each PSU portal) for admit cards / date changes / results. Flag updates immediately.
- Write session outcomes back into `.brain` when the work changes the student's prep status.

## Current Priority Rules — September 2026 Stacked Campaign

- **Career baseline: SECURED — UCO Bank SO (JMGS-I), Kolkata.** Every remaining exam is an upgrade attempt from security, not survival. See `.brain/UCO-BANK-DECISION-AUDIT.md`.
- **Immediate priority: HAL Design Trainee (CS) CBT — Sun 06 Sept 2026, Bengaluru (App No D321947) → IOCL Engineers/Officers CBT — 24 Sept 2026.** Run as ONE stacked campaign per `combined-HAL-then-IOCL-plan.md`, not two sprints. ~73% of IOCL is pre-covered by HAL; ~27 marks (Cloud/DevOps, OOP/Web, network security, NoSQL/Linux, Quant+DI) are isolated into 08–13 Sept Delta Week.
- **Admin gates (do not miss):** ISRO ICRB by 08 Sept (closes 16 Sept), CONCOR by 09 Sept (closes 30 Sept). HAL interview 21–25 Sept vs IOCL CBT 24 Sept clash is risk R1 — check call letter 12 Sept.
- **Result watch (no action, just monitor):** CIL MT (147/200 = 73.5% peak), NFL MT (99/150), IFFCO GET CBT2, STPI MTSS, ISP, HLL, Balmer Lawrie.
- **Standing rules from audit:** Do not withdraw any pending application. Opt for leased accommodation over cash HRA at UCO joining. Bond + probation clear ~Sept 2028 (age 28) — re-evaluate then.
- **Historical tracks:** HPCL is dead (not qualified 88.25/170 vs 117.5 cutoff). MSTC is closed (not selected July 2026). IFFCO CBT2 is awaiting result. Keep them as reference only — do not let them displace the HAL → IOCL sprint.

## Content Boundaries

- Put reusable CS fundamentals in `Notes/Shared-Core/`.
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