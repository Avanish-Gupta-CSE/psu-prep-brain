# Weak Areas Tracker

## How This File Works
- Topics are added here when you score below 50% in practice/mocks or struggle during Cursor AI sessions
- Each entry has a remediation plan with specific resources
- Topics are removed (moved to "Resolved") when you score above 70% consistently

## Identified Weak Areas

### MSTC Final Interview Sprint (16 May - 21 May 2026) — Core-4 “basic mastery” (ACTIVE)

Target: be able to answer **basic** questions fast under short panel timing (intro → DBMS/CN/OS/DSA).

| Subject | Must-win basics (interview) | Daily drill (primary) | Lecture fallback (only if stuck) | Practice source (quick) |
|---|---|---|---|---|
| DBMS/SQL | keys, 1NF→3NF (what it prevents), JOINs + NULL traps, indexing basics, ACID + 1 anomaly | `MSTC/TECHNICAL-QUESTION-BANK.md` + “7-minute lightning mode” | [Gate Smashers DBMS Lec-1 (syllabus)](https://www.youtube.com/watch?v=kBdlM6hNDAE) | [GateOverflow — Transaction & Concurrency control](https://gateoverflow.in/505837/gate-cs-practice-transaction-concurrency-control-dbms) |
| OS | process vs thread, scheduling goals, deadlock (4 conditions + 1 prevention), paging/virtual memory, mutex vs semaphore | `MSTC/TECHNICAL-QUESTION-BANK.md` + “7-minute lightning mode” | [Neso Academy — Operating System](https://nesoacademy.org/cs/03-operating-system) | [GateOverflow — Deadlock tag](https://gateoverflow.in/442017/deadlock) |
| Computer Networks | TCP vs UDP, handshake, DNS, HTTP vs HTTPS/TLS, NAT, common ports | `MSTC/TECHNICAL-QUESTION-BANK.md` + “7-minute lightning mode” | [Neso Academy — Computer Networks playlist](https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx&feature=shared) | (use the MSTC Q-bank; add subnetting only if asked) |
| DSA | Big‑O talk, stack vs queue, hashing collisions, BFS vs DFS, BST basics | `MSTC/TECHNICAL-QUESTION-BANK.md` + “7-minute lightning mode” | [Abdul Bari — DSA playlist](https://www.youtube.com/playlist?list=PL03of0rPCur_NZ9Rr4w1a5RDMU2qegBQl&cbrd=1&ucbcb=1) | (use the MSTC Q-bank; keep it basic) |

### From GATE 2026 (CS: 21/100, DA: 28/100)

The GATE scores indicate broad weakness across the CS syllabus. Based on typical GATE question distribution and a score of 21, the following areas likely need the most work:

| Area | Likely Weakness | Priority | Remediation |
|------|----------------|----------|-------------|
| Algorithms & Complexity | DP, greedy, recurrence relations | 1 | GO Classes Algo playlist, practice 50+ MCQs |
| Data Structures | Tree operations (AVL rotations, B+ Tree), graph algorithms | 1 | GO Classes DS playlist, dry-run every operation |
| Operating Systems | Paging numericals, scheduling Gantt charts | 1 | GO Classes OS playlist, solve 30+ scheduling problems |
| Computer Networks | Subnetting, TCP congestion control | 2 | GO Classes CN playlist, practice subnetting until automatic |
| DBMS | Normalization edge cases, transaction serializability | 2 | GO Classes DBMS playlist, practice decomposition problems |
| TOC | NFA-DFA conversion, pumping lemma proofs | 2 | GO Classes TOC playlist |
| Discrete Math | Graph theory, combinatorics | 3 | GO Classes DM playlist |
| Engineering Math | Probability, linear algebra | 3 | Low priority for PSU exams |

### From BARC OCES CBT (14 Mar 2026 -- Attempted ~60/100)

BARC confirmed the same weaknesses identified from GATE, now with specific sub-topic clarity:

| Area | Confirmed Weakness | Priority | Remediation |
|------|-------------------|----------|-------------|
| DBMS -- SQL | Non-straightforward SQL queries, nested/complex queries | 1 | Practice 50+ SQL output prediction problems, focus on NULL traps, GROUP BY + HAVING edge cases |
| Computer Networks | Broad inability -- subnetting, CRC, fragmentation, routing | 1 | GO Classes CN full playlist, then solve 100+ CN MCQs |
| Theory of Computation | Could not solve TOC questions at all | 1 | GO Classes TOC playlist from scratch, focus on FA/NFA/DFA and pumping lemma |
| Operating Systems -- Deadlocks | Deadlock detection, Banker's algorithm numericals | 1 | GO Classes OS deadlock lectures + 30 Banker's algo problems |
| Computer Organization | Could not solve COA questions | 1 | GO Classes COA playlist, focus on cache and pipelining numericals |
| Algorithms | Could not solve algorithm questions | 1 | GO Classes Algo playlist, focus on DP, greedy, and graph algorithms |
| C Programming | Partially solved -- some gaps remain | 2 | Focus on pointer traps, fork() counting, macro expansion |

### From April 2026 Exam Mapping (HPCL + IFFCO)

These are immediate gaps identified by comparing the active exam paths with the current profile and prior performance. They are planning gaps, not yet mock-verified.

The earlier IFFCO Officer / Senior Officer (IT) notification was cancelled, so the old Oracle / C# / Entity Framework-specific assumptions are no longer the active planning baseline.

| Area | Gap | Priority | Remediation |
|------|-----|----------|-------------|
| HPCL -- Digital Logic | Boolean algebra, K-maps, combinational and sequential circuit recall speed | 1 | Create one compact formula sheet + solve 30 factual/numerical MCQs |
| HPCL -- Programming Concepts Breadth | Java/J2EE, Python, shell scripting, web stack breadth, API concepts | 1 | Use fast-recall revision notes instead of deep implementation study |
| HPCL -- Information Security | Crypto/auth/firewalls/IDS/IPS/risk/data privacy basics | 2 | Build one exam-focused summary and drill definition-based MCQs |
| HPCL -- Emerging Technologies | Cloud, virtualization, IoT, AI/ML, data mining, blockchain survey topics | 2 | Build high-level comparison notes and factual MCQ practice |
| IFFCO GET -- Broad CS Recall | Timed recall across DBMS, OS, CN, programming, and aptitude under uncertain test pattern | 1 | Reuse shared-core quick revision and short timed sets instead of speculative niche prep |
| IFFCO GET -- Remote Test Readiness | Open-environment prelim means device, internet, and calm execution are part of the risk | 1 | Prepare a device/internet checklist and practice at least one short timed session on your own setup |
| IFFCO GET -- Application Readiness | Form and upload requirements can cause avoidable deadline risk | 1 | Finish photo and combined document PDF early and submit before 30 Apr |
| IFFCO GET -- Motivation Framing | Explaining `why IFFCO / why GET / why PSU` credibly | 1 | Prepare concise answers from real career intent, not generic security language |
| MSTC -- Interview Fluency | Self-introduction, company-fit, and resume-story smoothness | 1 | Convert `CAREER-STORY-BANK.md` into spoken 60-90 second answers and run mocks after HPCL |

### From BEL MT CBT (Failed)

| Area | Notes | Remediation |
|------|-------|-------------|
| General CS breadth | BEL tests broad CS knowledge at moderate difficulty | Phase 2 CS Core Deep Dive covers this |
| Speed/Accuracy | May have had time management issues | Practice timed mocks, target 1.5 min/question |

### From BDL MT CBT (Failed, OBC cutoff was 112)

| Area | Notes | Remediation |
|------|-------|-------------|
| Core CS fundamentals | Similar pattern to BEL failure | Phase 2 CS Core Deep Dive |
| Aptitude section | If aptitude questions were weak | Add 15 min daily aptitude practice |

### From CBSE Assistant Secretary (Failed cutoff)

| Area | Notes | Remediation |
|------|-------|-------------|
| General awareness / GK | Different exam type, but indicates GK gap | Daily current affairs during Phase 1 and ongoing |

## Resolved Weak Areas

_Topics that were weak but have been addressed and now score above 70% consistently._

| Topic | Date Resolved | Final Score | Notes |
|-------|--------------|-------------|-------|
| -- | -- | -- | No resolved topics yet |

## Active Remediation Plan

### Immediate (22 Apr - 3 May: HPCL Sprint)
1. **Close the leftover HPCL breadth** -- Digital Logic, COA, Programming Concepts, Security, Emerging Tech
2. **Keep core weak areas alive** -- SQL, CN, OS deadlocks, COA numericals, Algorithms
3. **Start mixed mocks** -- shift from isolated topics to paper-style breadth before 3 May

### Parallel (Late Apr - May: IFFCO GET Track)
1. **Application completion** -- eliminate avoidable deadline and upload failures
2. **Broad shared-core readiness** -- stay fast across DBMS, OS, CN, programming, and aptitude
3. **GET / PSU fit answers** -- explain intent and trainability cleanly

### Scheduled Interview Track (MSTC)
1. HR and behavioral answer rehearsal
2. Career-story bank from `Resume-Berkadia.tex` turned into spoken answers
3. Call-letter, document, and travel readiness once released

## Session-Level Weak Spots

_Updated after each Cursor AI session when the student gets MCQs wrong._

| Date | Topic | Sub-Topic | Question Type | Notes |
|------|-------|-----------|---------------|-------|
| -- | -- | -- | -- | No sessions yet |

---

## MOCK 1 GAPS — Added 20 May 2026

**Source:** Mock Interview 1 (19 May 2026, 7 PM)
**Score:** HR 4/5, Technical 2/5

All 8 gaps now have 40-second repair scripts in `MSTC/TECHNICAL-GAPS-REPAIR.md`.

| # | Gap Topic | Correct Answer Summary | Repair File |
|---|---|---|---|
| 1 | IS NULL / IS clause | `= NULL` returns 0 rows always. Use `IS NULL` because NULL comparisons return UNKNOWN | TECHNICAL-GAPS-REPAIR.md |
| 2 | PK vs UK | PK: no null, one per table, clustered. UK: one null allowed, multiple per table, non-clustered | TECHNICAL-GAPS-REPAIR.md |
| 3 | OS technical definition | Interface between hardware and user. Manages CPU, memory, I/O. Takes instructions → directs CPU → hardware. | Notes/OS/01-OS-BASICS-AND-PROCESSES.md |
| 4 | Eigenvalues | Av = λv. Solve det(A - λI) = 0. Sum = trace, Product = determinant. | TECHNICAL-GAPS-REPAIR.md |
| 5 | Multiplexer | n select lines → 2ⁿ inputs → 1 output. Data selector/router. | TECHNICAL-GAPS-REPAIR.md |
| 6 | HAVING clause | WHERE = before GROUP BY (no aggregates). HAVING = after aggregation (aggregates ok). | TECHNICAL-GAPS-REPAIR.md |
| 7 | IPv4 vs IPv6 | IPv4 = 32-bit, 4.3B addresses, needs NAT. IPv6 = 128-bit, unlimited, built-in IPSec. | TECHNICAL-GAPS-REPAIR.md |
| 8 | Dijkstra (**WRONG ANSWER GIVEN**) | ✅ Works on BOTH directed AND undirected. ❌ Only fails on negative edge weights. | Notes/DSA/06-ADVANCED-ALGORITHMS.md |

---

## STPI SCIENTIST B GAPS — Added 30 May 2026

**Source:** STPI Scientist B CBT Exam (30 May 2026)
**Syllabus:** NIELIT Pattern (GATE-level CS + Quantitative Aptitude + General Awareness + English)

All of these gaps have been injected directly into your shared-core revision notes for fast, mobile-friendly recall on your phone.

| # | Gap Topic | Remediation Action & Concept Summary | Revision File |
|---|---|---|---|
| 1 | Time & Work / Pipes | LCM method, net inlets vs. outlets, alternate days, MDH formula | `Notes/Shared-Core/APTITUDE.md` |
| 2 | Trig standard values | Trigonometric matrix (sin, cos, tan, cot, sec, csc) with tan(60) = sqrt(3) | `Notes/Shared-Core/APTITUDE.md` |
| 3 | Mensuration Formulas | Area & Volume formulas for Cube, Cuboid, Cylinder, Cone, Sphere, Hemisphere | `Notes/Shared-Core/APTITUDE.md` |
| 4 | Calendar Shortcuts | Day calculation using Key-Value Codes and Zeller's Congruence formula | `Notes/Shared-Core/APTITUDE.md` |
| 5 | India's Nuclear Milestone | Kalpakkam PFBR (500 MWe, sodium-cooled, Stage-2, criticality on April 6, 2026) | `Notes/Shared-Core/GENERAL-AWARENESS.md` |
| 6 | May 2026 Appointments | Niti Aayog (PM Modi, Lahiri, Chhibber), RBI Governor Malhotra, SEBI Buch | `Notes/Shared-Core/GENERAL-AWARENESS.md` |
| 7 | English Spellings | Hard-to-spell word matrices (etiquette, palatial, accommodate, homogeneous) | `Notes/Shared-Core/GENERAL-AWARENESS.md` |
| 8 | Chomsky hierarchy | Type-3 (Regular), Type-2 (CFG/PDA), Type-1 (CSG/LBA), Type-0 Unrestricted (TM) | `Notes/Shared-Core/GENERAL-AWARENESS.md` |
| 9 | Full Adder gates | 2 HAs + 1 OR gate; 9 NAND gates; 9 NOR gates | `Notes/Shared-Core/DIGITAL-LOGIC.md` |
| 10 | Shannon's Theorem | Boolean decomposition SOP (F = x.Fx + x'.Fx') and multiplexer synthesis | `Notes/Shared-Core/DIGITAL-LOGIC.md` |
| 11 | Pipelining Cycles | K-stage, N instructions formula: Cycles = K + N - 1 + Stalls; Speedup = Tn/Tp | `Notes/Shared-Core/COMPUTER-ORGANIZATION.md` |
| 12 | Virtual memory paging | VA = page+offset; PA = frame+offset; Page Table Size = N_pages * PTE_size | `Notes/Shared-Core/OPERATING-SYSTEMS.md` |
| 13 | Counting Sort limits | Inefficient when key range k >> n (e.g., k = O(n^2)), degenerating to O(n^2) | `Notes/Shared-Core/DATA-STRUCTURES-ALGORITHMS.md` |
| 14 | Merge vs. Quick Sort | Merge (lists, stable, guaranteed O(n log n)); Quick (arrays, in-place, unstable) | `Notes/Shared-Core/DATA-STRUCTURES-ALGORITHMS.md` |
| 15 | Floyd-Warshall DP | All-pairs shortest path in O(V^3) time. Handles negative weights correctly. | `Notes/Shared-Core/DATA-STRUCTURES-ALGORITHMS.md` |

