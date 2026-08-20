# PSU Prep Agents Contract

This repository is a personal PSU preparation workspace, not a software product.
All agents must optimize for exam readiness, memory continuity, and clear separation between shared prep and exam-specific prep.

## Shared State

- Treat `.brain/` as the canonical memory layer for cross-session and cross-agent state.
- Before planning or teaching, read `.brain/NextSteps.md`, `.brain/Progress.md`, and `.brain/ExamTracker.md` first.
- Use the current date to determine the active sprint and verify that the active phase in `.brain` is still correct before acting on it.
- Write session outcomes back into `.brain` when the work changes the student's prep status.

## Current Priority Rules

**Phase 6: Aug-Sept 2026 CBT Marathon + Form-Filling Sprint (ACTIVE as of 20 Aug 2026)**

- **IMMEDIATE (next 7 days):** Fill forms in `.brain/Jobs-Table.md` Tier 1 (closes 20–27 Aug). ISRO ICRB 267 closes TODAY (20 Aug 2026).
- **Active CBT sprint (23–24 Aug + 5–6 Sep):** BSNL JTO, HLL Lucknow, CIL Bangalore, HAL Bengaluru. Prep via `Notes/Shared/`/`/` + Knowledge Gate / GO Classes.
- **Berkadia exit active** (LWD 31 Aug 2026): handovers for ReservesAI, DMS, CMS.
- **UCO Bank SO onboarding:** September 2026 batch (Salt Lake, Kolkata).
- **Monitor:** NFL Top-5 OBC shortlist, IFFCO CBT 2 result, Balmer Lawrie result, NHAI shortlist, ISRO SC interview call, CERT-In interview call.
- **Out of scope for Phase 6:** MSTC (closed), STPI (closed), BARC OCES (closed), HPCL (closed), SEBI (closed), ECIL (closed).
- **Do not let new form-filling or exam prep displace Berkadia handovers or UCO onboarding admin** — those are time-locked.

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