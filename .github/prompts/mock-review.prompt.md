---
name: mock-review
description: Review a mock test or question set and convert mistakes into next actions (HAL → IOCL stacked campaign).
agent: hal-prep
---

Review the submitted mock or question set using the relevant exam folder (`HAL/` or `IOCL/`) plus the shared-core notes (`Notes/Shared-Core/`, `Notes/DBMS/`, `Notes/DSA/`, `Notes/OS/`, `Notes/CN/`) and `combined-HAL-then-IOCL-plan.md`.

Return:

- score summary (with sectional breakdown if available; HAL 160Q/150min, IOCL 100Q/120min)
- mistake categories with error classes: `concept` / `computation` / `trap` / `time` / `misread` (for `HAL/ERROR-LOG.md`)
- weak areas by topic with stacking flag: double-value (HAL+IOCL) vs HAL-terminal vs IOCL-only
- next 3 repair actions with exact files to drill and timed targets
- exact brain files that should be updated if the result changes the prep state, including `.brain/NextSteps.md` when the immediate repair order changes, plus `HAL/ERROR-LOG.md` and `HAL/FORMULA-CARD.md` for the Stacking Ledger