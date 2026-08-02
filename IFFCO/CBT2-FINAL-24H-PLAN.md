# IFFCO GET CBT 2 — Final 24-Hour Battle Plan

> **Exam:** Sunday, 02 Aug 2026 — Reporting **2:30 PM**, Gates close **3:15 PM**
> **Centre:** Nivansys Technologies, eMerit, No. 1, Maruthi Complex, 2nd Floor, Opp. Post Office, RT Nagar, Bengaluru - 560032
> **Hall Ticket No:** 1000-7311
> **Expected pattern (from CBT 1):** 100 technical questions / 60 minutes, backtracking allowed, flag/clear supported.

---

## Mentor Calls (read this first)

1. **Interview notes are POSTPONED.** CBT 2 is 100% technical MCQ. Interview prep only matters if you clear CBT 2 — do it from 3 Aug onward. Every minute tonight goes to MCQ recall.
2. **You WILL sleep 1:00 AM – 6:30 AM.** This is not soft advice — it is scoring strategy. An all-nighter costs you 10–15 marks in recall speed and silly mistakes during a 36-second-per-question exam. Sleep consolidates everything you memorize tonight.
3. **Coal India material is a lookup dictionary, not a course.** No new modules. Open `CoalIndiaLimited-PSU/Paper-2` ONLY when a weak topic needs a better explanation than Shared-Core notes have.
4. **The 100-question bank is your biggest edge.** CBT 2 will be scenario-style questions in the same voice as CBT 1. Even if questions differ, the *topics and traps* repeat. Master the bank → master the pattern.
5. **Drill tool:** `IFFCO/CBT2-RAPID-RECALL-SHEET.md` — all 100 questions as one-line cue → answer → trap, in 5 chunks of 20.

---

## SLOT 1 — Sat 6:00 PM → 12:00 AM (Bank Mastery)

| Time | Activity |
|------|----------|
| 6:00 – 7:00 | **Mock #1 (baseline):** Full 100Q/60min timed run on `IFFCO/simulator`. Exam conditions — no pausing, no looking things up. |
| 7:00 – 7:15 | Score it. Write every wrong/guessed Q number on paper. This is your personal hit-list. |
| 7:15 – 9:45 | **Chunk memorization** using the rapid-recall sheet — 5 chunks × ~30 min: Chunk A (Q1–20 DBMS+OS), B (Q21–40 OS+CN+DSA), C (Q41–60 Compilers+Arch+Mixed), D (Q61–80 Mixed), E (Q81–100 Mixed). Method: cover the answer column → say answer + why aloud → check → mark misses with ❌. Re-run only ❌ rows at the end of each chunk. |
| 9:45 – 10:45 | **Weak-topic surgery** — the 8 topics CBT 1 flagged: Compiler phases & optimizations, Raft vs 2PC vs Vector Clocks, Thrashing/Compaction/Fragmentation, Cache coherence + miss types (MESI, conflict vs capacity), Bellman-Ford vs Dijkstra vs BFS, AVL vs Red-Black vs B+ Tree (memory vs disk!), Bloom Filters, Aho-Corasick. Use `Notes/Shared-Core/*` first, CIL Paper-2 as fallback. |
| 10:45 – 11:45 | **Mock #2:** Full timed run. Target: 90+. |
| 11:45 – 12:00 | Review only the misses. Update hit-list. |

## SLOT 2 — 12:00 AM → 6:30 AM (Consolidate + SLEEP)

| Time | Activity |
|------|----------|
| 12:00 – 1:00 | Light pass: re-drill only ❌-marked rows from all 5 chunks. Then skim the comparison tables in `Notes/Shared-Core/DBMS.md`, `OPERATING-SYSTEMS.md`, `COMPUTER-NETWORKS.md` (tables and bold lines only, no deep reading). |
| **1:00 – 6:30** | **SLEEP. Non-negotiable.** Phone on Do-Not-Disturb, alarm at 6:30. |

## SLOT 3 — Sun 6:30 AM → 12:00 PM (Sharpen + Logistics)

| Time | Activity |
|------|----------|
| 6:30 – 7:00 | Wake, shower, proper breakfast. |
| 7:00 – 8:00 | **Mock #3 (final):** Full timed run, exam conditions. This locks your pacing muscle-memory. |
| 8:00 – 9:00 | Review misses. Re-drill any chunk with ≥2 errors. |
| 9:00 – 10:30 | **Beyond-the-bank sweep** (CBT 2 will have new questions): rapid pass over `Notes/Shared-Core/` — `DBMS.md`, `OPERATING-SYSTEMS.md`, `COMPUTER-NETWORKS.md`, `DATA-STRUCTURES-ALGORITHMS.md`, `PROGRAMMING-CONCEPTS.md`, `COMPUTER-ORGANIZATION.md`. Read tables, mnemonics, and bold text only. |
| 10:30 – 11:15 | **Full-sweep recall test:** run all 100 cues on the rapid-recall sheet at ~15 sec each (~25 min), then one last look at the 8 weak topics. |
| 11:15 – 12:00 | **Logistics:** print hall ticket (2 copies) + govt photo ID, pack water/pen, map route to RT Nagar centre. Plan to ARRIVE by 2:00 PM — leave by ~1:00 PM with Sunday-traffic buffer. |
| 12:00 – 1:00 | Lunch (light). STOP studying. Leave. |

---

## Exam Execution Strategy (100 Q / 60 min = 36 sec/question)

1. **Pass 1 (0–40 min):** Answer everything you can in under 30 seconds. Anything slow → pick best guess, FLAG, move on. Never let one question eat 2 minutes.
2. **Pass 2 (40–55 min):** Return to flagged questions via navigator grid.
3. **Final 5 min:** Check the on-screen instructions at start for negative marking. **If none → zero blanks; answer everything.** If negative marking exists, skip only pure coin-flips.
4. **Scenario decoding trick:** every CBT 1 question was scenario-first with ONE discriminating keyword ("after aggregation" → HAVING, "negative edges" → Bellman-Ford, "disk index" → B+ Tree, "read-heavy" → Read-Write Lock/AVL). Find the keyword, ignore the story.
5. **Trap discipline:** the wrong options are always *neighbouring concepts* (Dijkstra vs Bellman-Ford, 2PC vs Raft, conflict vs capacity miss). When torn between two options, re-read the scenario for the single word that separates them.

## After the Exam (3 Aug onward)

- Log recalled questions into a `CBT2-QUESTIONS` file same-day (memory fades in 24h).
- Start interview notes in `Notes/` — the postponed step 3.
- Update `PROGRESS-LOG.md` and `.brain/ExamTracker.md`.

**You have a verified 100% question bank from CBT 1, a simulator that mimics the real portal, and 20 usable hours. That is a strong position. Execute the plan — no improvising at 2 AM.**
