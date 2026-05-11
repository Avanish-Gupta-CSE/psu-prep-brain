# Next Steps & Handoff

Last updated: 11 May 2026

This is the canonical resume-point file for any future login, agent, or chat system.
Read this file first when the goal is to understand what to do next without reconstructing context from multiple logs.

## Immediate Situation

- Current date context: `11 May 2026`
- Critical path: `MSTC MT (Systems)` interview scheduled on `21 May 2026` at `9.00 A.M.` (New Delhi)
- Focus rule: `MSTC only` unless explicitly requested otherwise
- Official source set: `MSTC/OFFICIAL-INTERVIEW-UPDATE.md` + PDFs in `MSTC/`
- Repo state: `.brain/` is the memory layer; MSTC work lives in `MSTC/`; important updates must be committed and pushed to `main`

## Resume Order

If a new system needs the full picture quickly, read files in this order:

1. `./NextSteps.md`
2. `./Progress.md`
3. `./ExamTracker.md`
4. `./StudyPlan.md`
5. the active MSTC track README (`../MSTC/README.md`)

## Immediate Next Actions

### 0. 10-day countdown plan (11 May -> 20 May)

Use the quick-revision notes as the “compressed theory” layer: `MSTC/Quick Revision Ebook/revision-ebook-glm.md`.

| Date | Primary Technical Focus | Mentor snap-interview trigger |
|------|--------------------------|------------------------------|
| 11 May | DBMS (SQL traps, joins, indexes, transactions) | If you can answer 10 DBMS rapid-fire Qs without pausing |
| 12 May | OS-1 (process/thread, scheduling, deadlocks) | If you can explain deadlock + one fix clearly |
| 13 May | OS-2 (memory/paging, sync basics, race conditions) | If you can answer 8 OS rapid-fire Qs |
| 14 May | Data Structures-1 (arrays/LL/stack/queue, hashing, Big-O talk) | If you can explain hashing collisions + tradeoffs |
| 15 May | Data Structures-2 (trees/graphs, BFS/DFS, heaps) | If you can answer 10 DS rapid-fire Qs |
| 16 May | OOP + design clarity (examples in TypeScript) | If you can do 40s + 2 follow-ups for each OOP pillar |
| 17 May | Networks + Web (DNS/HTTP/TLS + REST vs SOAP) | If you can explain “type URL → page load” end-to-end |
| 18 May | Security + DevOps/Cloud (OWASP basics, Docker/K8s, CI/CD, monitoring) | If you can explain incident triage steps credibly |
| 19 May | MSTC Systems scenarios (load, audit logs, DDoS, fake bids, dispute handling) | Full mixed mock with mentor (recommended) |
| 20 May | Final consolidation (2 mixed mocks + logistics checklist + calm revision) | Final mixed mock (HR + technical) |

### 1. Lock the “opening 90 seconds”
- Finalize: 30-sec + 60-sec self-introduction
- Finalize: `why MSTC`, `why PSU`, `why you`, `strengths/weakness` (resume-true, no extra claims)
- By-heart: MSTC **Vision / Mission / Objectives** using `GDR – THIPP – ICPWJRB` (`MSTC/MISSION-VISION.md`, `MSTC/Company-MSTC-Research/MSTC_VMO_Mnemonics.md`)
- Use: `MSTC/HR-QUESTION-BANK.md`, `MSTC/CAREER-STORY-BANK.md`

### 2. Technical interview readiness (MT Systems)
- Build fast-recall answers for: Networking, DBMS/SQL, OS basics, REST vs SOAP, auth basics, Docker/K8s, CI/CD, cloud fundamentals
- Turn each resume project into a deep-dive: architecture, decisions, failure modes, security/reliability, measurable outcomes
- Use: `.brain/MSTC-GD-Prep.md` (company context), `Resume-Berkadia.tex` (facts)
- Drill sources: `MSTC/TECHNICAL-QUESTION-BANK.md`, `MSTC/PROJECT-DEEP-DIVE.md`

### 3. Mock cadence (until interview day)
- Run alternating mocks: HR-only, Technical-only, Mixed
- Log each mock in `MSTC/MOCK-INTERVIEW-TRACKER.md` with “weakest answer → repair target”

### 4. Logistics (do once, then re-check when call letter arrives)
- Confirm venue and reporting guidance from `MSTC/OFFICIAL-INTERVIEW-UPDATE.md`
- Ensure: interview call letter print + valid original photo ID (ration card / learner DL not valid)
- Plan travel so arrival is at least `30 minutes` before reporting time

## Open Loops To Watch

- Call letter release link and document checklist (final confirmation from the call letter)
- Any interview-day changes (time/venue/mode)

## Update Rule

Update this file whenever one of these changes:

- the immediate next interview-prep block changes
- the active track priority changes
- a new interview update arrives
- a mock reveals a new weakness that changes the next drill target