---
applyTo: ".brain/**/*.md"
---

`.brain/` is the canonical persistent memory — the single source of truth that survives context-window resets. Every Copilot session must treat it as the brain-complex.

**Core invariants (never break):**
- Preserve history instead of rewriting it away unless clearly obsolete. Append sessions; don't overwrite.
- When a session changes prep status, update trackers **together**: `.brain/NextSteps.md` + `.brain/Progress.md` + `.brain/ExamTracker.md` + `.brain/StudyPlan.md` must agree on phase, dates, and next action.
- Keep `.brain/NextSteps.md` current whenever the immediate next study block, deadline, or resume point changes — it is the handoff file for the next login.
- Keep dates explicit and consistent with the current date (today is 01 Sept 2026, Phase 6 HAL sprint live). Compare recorded phase against real exam dates before trusting it.
- `combined-HAL-then-IOCL-plan.md` is the single operational source of truth for Sept 2026 (HAL 06 Sept → IOCL 24 Sept). `.brain` files must stay consistent with it.
- `.brain/TrackedJobs.md` is mandatory pre-session check — review it and run a rapid web/aggregator check (`indgovtjobs.in`, `iffco.in/careers`, `kribhco.net/careers`, plus each PSU portal) for admit cards / date changes / results before answering.

**Content rules:**
- When adding weak areas, make them specific enough to be remediated with targeted practice (topic + sub-topic + error class + remediation file).
- When adding mock logs, include score, topic breakdown when known, and a next-action note. Live CBT scores (e.g., CIL 147/200 = 73.5%) are highest-signal — never discard them.
- When updating `Progress.md`, add a dated session entry (topics, questions attempted, accuracy, next goals), update streak, and update Last 7 Days summary.
- Standing rules from `.brain/UCO-BANK-DECISION-AUDIT.md` persist: do not withdraw pending applications; opt for leased accommodation over cash HRA; bond clears ~Sept 2028.
- Separate `Confirmed` (advert/portal/admit card) from `Inferred` (pattern/overlap/strategy) in every exam-adjacent note.