# IOCL FINAL 5-DAY BATTLE PLAN — 19 Sept (tonight) → 24 Sept CBT

> ⚠️ **SUPERSEDED 20 Sept 11:30 AM** — the 19-night window was lost; replaced by [`FINAL-4DAY-BATTLE-PLAN.md`](FINAL-4DAY-BATTLE-PLAN.md) (20 Sept 11:30 AM → 24 Sept 09:30 AM, ~55h). Kept for history; strategy section still valid.

> **Created:** 19 Sept 2026, 10:00 PM
> **Exam:** 24 Sept 2026, ~13:30 start, Bareilly · Roll 1171000327
> **Status:** DL 3.1 (42%) + DL 3.2 (39%) done. Everything else = ZERO.
> **Budget:** ~40h realistic (tonight ~2h + 4 days × 9.5h/day + exam morning 1.5h)
> **Career floor:** UCO Bank (joining 28 Sept). This is an UPGRADE attempt, not survival.

---

## 🧠 THE CORE INSIGHT — Score Maximization, Not Coverage

**You CANNOT cover everything. 288h of video in 40h is impossible.**
**You CAN maximize expected score by targeting the highest-ROI topics with PYQs + Notes ONLY.**

### The Math That Matters

| Component | Questions | Marks | Target | Strategy |
|-----------|----------|-------|--------|----------|
| **Section A (Tech)** | 75 | 75 | **50+** | PYQ-pattern + notes for 6 high-weight subjects |
| **Section B (Apt)** | 25 | 25 | **18+** | Formula sheet + 50 PQs per sub-topic |
| **Total** | 100 | 100 | **68+** | Realistic with ~40h if executed perfectly |

**Marking: +1 correct, -0.25 wrong.** To get 68 net: attempt ~80, get ~72 right, ~8 wrong → 72 - 2 = 70. Leave ~20 unattempted.

### Subject ROI Ranking (by PYQ weight × learnability in <1 day)

| Priority | Subject | PYQ Wt% | Est Qs | Time Needed | ROI Score |
|----------|---------|---------|--------|-------------|-----------|
| **P1** | **OS** | 11.3% | ~8 | 1 day | ★★★★★ (formula-heavy, predictable patterns) |
| **P1** | **DBMS** | 9.2% | ~7 | 1 day | ★★★★★ (SQL, normalization, transactions = drillable) |
| **P1** | **CN** | 9.3% | ~7 | 1 day | ★★★★☆ (subnetting needs drill but otherwise formula-based) |
| **P1** | **DS (data structures only)** | ~8% | ~6 | 0.5 day | ★★★★☆ (tree/graph/stack/queue = visual + drillable) |
| **P2** | **COA** | 9.6% | ~7 | 0.5 day | ★★★☆☆ (cache + pipeline numericals = formulaic) |
| **P2** | **DL (finish)** | 8.8% | ~7 | 0.5 day | ★★★☆☆ (partly done, close it) |
| **P2** | **Algo** | 7.3% | ~5 | 0.5 day | ★★★☆☆ (sorting + complexity = known patterns) |
| **P3** | **TOC** | 9.0% | ~7 | PYQ-only | ★★☆☆☆ (DFA/NFA/RE doable; PDA/TM = skip deep) |
| **P3** | **Eng Maths** | 15.8% | ~12 | PYQ-only | ★★☆☆☆ (HIGH weight but needs depth; cherry-pick probability + logic) |
| **P4** | **Compiler** | 5.5% | ~4 | PYQ-only | ★☆☆☆☆ (lowest weight, skip concept videos entirely) |
| **P1** | **Aptitude** | — | 25 | 1 day | ★★★★★ (25 free marks with formula practice) |

---

## 📅 THE PLAN — Hour by Hour

### TONIGHT — 19 Sept (Fri) 10:00 PM → 12:30 AM · ~2.5h

**Goal: Close DL + Set up exam-day systems**

| Time | Task | Source |
|------|------|--------|
| 10:00–10:45 | DL 3.2 close: Ex-OR/Ex-NOR (27 items) — notes + PYQs ONLY, skip videos | IOCL Paper-2 → DL |
| 10:45–11:15 | DL 3.2 close: Logic Families (11 items) — notes only | IOCL Paper-2 → DL |
| 11:15–11:45 | DL quick sweep: 3.3–3.4 (Boolean expr + minimization) — K-map rules from notes | IOCL Paper-2 → DL |
| 11:45–12:15 | DL quick sweep: 3.5–3.6 (Combinational + Sequential) — flip-flop table + counter rules from notes | IOCL Paper-2 → DL |
| 12:15–12:30 | DL 3.7–3.8 (Number system) — number conversion rules from notes | IOCL Paper-2 → DL |
| 12:30 | **SLEEP.** Not optional. 6h minimum. | — |

**DL Status after tonight: ~70% notes-covered. PYQ sweep pending (moved to Day 4 revision).**

---

### DAY 1 — 20 Sept (Sat) · **OS + DBMS** · ~9.5h

**These two subjects alone = ~15 questions (20% of the paper). Master them.**

| Block | Time | Task | Source | Target |
|-------|------|------|--------|--------|
| **A** | 06:30–07:30 | OS Notes: Process mgmt + CPU scheduling (FCFS/SJF/RR/SRTF/Priority) — **do 10 scheduling numericals** | IOCL Paper-2 → OS notes + PYQs | Know all 5 algorithms cold |
| **A** | 07:30–08:15 | OS Notes: Synchronization (semaphore, mutex, monitors) + Deadlock (4 conditions, Banker's algo — **do 5 Banker's numericals**) | IOCL Paper-2 → OS notes + PYQs | Banker's = guaranteed marks |
| **A** | 08:15–09:30 | OS Notes: Memory (paging, segmentation, page table) + Virtual Memory (FIFO/LRU/Optimal — **do 10 page-replacement numericals**) | IOCL Paper-2 → OS notes + PYQs | Page replacement = pure formula |
| **B** | 10:00–10:30 | OS Notes: Disk scheduling (FCFS/SSTF/SCAN/C-SCAN) + File systems (quick) | IOCL Paper-2 → OS notes | Fast topic, 1-2 Qs |
| **B** | 10:30–11:30 | **OS PYQ Sprint: attempt 60 PYQs** (of 341 available) — mark wrong ones | IOCL Paper-2 → OS PYQs | 60 PYQs = pattern lock |
| **B** | 11:30–13:00 | DBMS Notes: ER diagram + Relational model + FD + Keys + Normalization (1NF→BCNF) — **do 5 FD closure + 5 normalization drills** | IOCL Paper-2 → DBMS notes + PYQs | Normalization = guaranteed |
| **C** | 19:00–20:00 | DBMS Notes: SQL (JOINs, nested, aggregation, GROUP BY) + Indexing (B/B+ tree) | IOCL Paper-2 → DBMS notes | SQL = 2-3 easy Qs |
| **C** | 20:00–20:45 | DBMS Notes: Transactions (ACID, 2PL, timestamp) + Concurrency + Recovery | IOCL Paper-2 → DBMS notes | Transaction = 1-2 Qs |
| **C** | 20:45–21:30 | **DBMS PYQ Sprint: attempt 50 PYQs** (of 310 available) | IOCL Paper-2 → DBMS PYQs | |
| **C** | 21:30–22:30 | **Aptitude Block 1:** Quant formulas + 30 PQs (%, ratio, average, TSD, time-work) | IOCL Paper-1 → Quant | 8-10 Quant Qs in exam |

**Day 1 Output: OS ~80% + DBMS ~80% + Quant formulas loaded → ~15 Qs secured**

---

### DAY 2 — 21 Sept (Sun) · **CN + DS** · ~9.5h

**CN + DS = ~13 questions. After Day 2, you have ~28 Qs covered.**

| Block | Time | Task | Source | Target |
|-------|------|------|--------|--------|
| **A** | 06:30–07:30 | CN Notes: OSI/TCP-IP + Data Link (framing, CRC, sliding window, Go-Back-N, Selective Repeat) | IOCL Paper-2 → CN notes | Foundation layer |
| **A** | 07:30–08:30 | CN Notes: Network Layer — **IPv4 addressing + Subnetting** — **do 15 subnetting numericals** (WEAK AREA) | IOCL Paper-2 → CN notes + PYQs | Subnetting = 2-3 Qs guaranteed |
| **A** | 08:30–09:30 | CN Notes: Routing (DV, LS, RIP, OSPF, BGP) + Transport (TCP vs UDP, 3-way handshake, congestion) | IOCL Paper-2 → CN notes | |
| **B** | 10:00–10:30 | CN Notes: Application layer (DNS, HTTP, FTP, SMTP) + Security (RSA, digital signatures, SSL/TLS) | IOCL Paper-2 → CN notes | Quick topic |
| **B** | 10:30–11:15 | **CN PYQ Sprint: attempt 50 PYQs** (of 284 available) | IOCL Paper-2 → CN PYQs | |
| **B** | 11:15–12:00 | DS Notes: Arrays, Stacks, Queues, Linked Lists — operations + time complexity | IOCL Paper-2 → Prog+DS notes | Fundamental structures |
| **B** | 12:00–13:00 | DS Notes: Trees (BST, AVL, heap) + Graphs (BFS, DFS, representations) | IOCL Paper-2 → Prog+DS notes | Tree/Graph = 3-4 Qs |
| **C** | 19:00–19:45 | DS Notes: Hashing (collision resolution) + Programming basics (C pointers, storage classes — quick) | IOCL Paper-2 → Prog+DS notes | |
| **C** | 19:45–20:30 | **DS PYQ Sprint: attempt 50 PYQs** (of 471 available) | IOCL Paper-2 → Prog+DS PYQs | |
| **C** | 20:30–21:15 | **Aptitude Block 2:** Reasoning — series, coding-decoding, syllogism, blood relations, seating + 30 PQs | IOCL Paper-1 → Reasoning | 8-10 Reasoning Qs |
| **C** | 21:15–22:30 | **Aptitude Block 3:** English — grammar rules, error spotting, vocab, RC strategy + 30 PQs | IOCL Paper-1 → English | 5-7 English Qs |

**Day 2 Output: CN ~80% + DS ~70% + Reasoning + English loaded → ~28 Qs total secured**

---

### DAY 3 — 22 Sept (Mon) · **COA + Algo + Eng Maths (selective) + MOCK-1** · ~9.5h

**COA + Algo + Eng Maths cherry-pick = ~24 more Qs. After Day 3, you have ~52 Qs covered.**

| Block | Time | Task | Source | Target |
|-------|------|------|--------|--------|
| **A** | 06:30–07:15 | COA Notes: Number representation (fixed/floating point — IEEE 754) + Data path | IOCL Paper-2 → COA notes | |
| **A** | 07:15–08:15 | COA Notes: **Cache memory — do 10 cache numericals** (hit ratio, miss penalty, mapping) | IOCL Paper-2 → COA notes + PYQs | Cache = 2-3 Qs (formulaic) |
| **A** | 08:15–09:00 | COA Notes: Pipelining — **do 5 pipeline numericals** (speedup, stalls, hazards) + I/O | IOCL Paper-2 → COA notes + PYQs | Pipeline = 1-2 Qs |
| **A** | 09:00–09:30 | **COA PYQ Sprint: attempt 30 PYQs** (of 258 available) | IOCL Paper-2 → COA PYQs | |
| **B** | 10:00–10:45 | Algo Notes: Analysis of algorithms (Big-O, recurrences, Master theorem) | IOCL Paper-2 → Algo notes | Complexity = 2-3 Qs |
| **B** | 10:45–11:30 | Algo Notes: Sorting (all 9) + searching + Greedy + DP (knapsack, LCS, MCM pattern) | IOCL Paper-2 → Algo notes | |
| **B** | 11:30–12:00 | Algo Notes: Graph algos (MST — Prim/Kruskal, SP — Dijkstra/Bellman-Ford/Floyd) | IOCL Paper-2 → Algo notes | MST/SP = 1-2 Qs |
| **B** | 12:00–13:00 | Eng Maths CHERRY-PICK: **Probability** (Bayes, distributions) + **Combinatorics** (P&C) — notes + 20 PYQs | IOCL Paper-2 → Eng Maths notes + PYQs | 15.8% weight! Cherry-pick highest-frequency topics |
| **C** | 19:00–19:45 | Eng Maths CHERRY-PICK: **Linear Algebra** (matrix rank, eigenvalues, determinant) + **Propositional Logic** — notes + 20 PYQs | IOCL Paper-2 → Eng Maths notes + PYQs | 4 cherry-picked sub-topics → 6-8 of ~12 Qs |
| **C** | 19:45–21:45 | **🔥 MOCK-1: Full 100Q / 120 min exam simulation** — use IOCL Paper-2 Test Series full mock | IOCL Test Series | Exam simulation #1 |
| **C** | 21:45–22:30 | **Mock-1 analysis:** mark every wrong answer, identify pattern (concept gap vs silly mistake vs time pressure) | Error log | Feed Day 4 revision |

**Day 3 Output: COA ~70% + Algo ~60% + Eng Maths ~40% (cherry-picked) + Mock-1 baseline score → ~52 Qs covered**

---

### DAY 4 — 23 Sept (Tue) · **TOC + Compiler (PYQ-only) + DL PYQ sweep + REVISION + MOCK-2** · ~9.5h

**This is the CONSOLIDATION day. No new deep learning — only PYQ pattern-matching + revision.**

| Block | Time | Task | Source | Target |
|-------|------|------|--------|--------|
| **A** | 06:30–07:30 | TOC PYQ-FIRST: DFA/NFA construction, RE→DFA, Grammar classification — **attempt 40 PYQs, read solutions for wrong ones** | IOCL Paper-2 → TOC PYQs | PYQ pattern = 4-5 of 7 Qs |
| **A** | 07:30–08:00 | Compiler PYQ-FIRST: Parsing (LL/LR), first/follow, SDT, code generation — **attempt 25 PYQs** | IOCL Paper-2 → Compiler PYQs | PYQ pattern = 2-3 of 4 Qs |
| **A** | 08:00–09:00 | DL PYQ sweep: attempt 40 PYQs (of 284) — cover K-map, combinational, sequential, number system | IOCL Paper-2 → DL PYQs | Close the partly-done subject |
| **A** | 09:00–09:30 | Eng Maths PYQ sprint: attempt 30 more PYQs (Probability + Linear Algebra + Logic focused) | IOCL Paper-2 → Eng Maths PYQs | |
| **B** | 10:00–11:30 | **REVISION PASS 1:** OS (scheduling + page replacement + Banker's numericals) + DBMS (normalization + SQL + transactions) | Own notes + PYQ wrong answers | Strengthen P1 subjects |
| **B** | 11:30–13:00 | **REVISION PASS 2:** CN (subnetting + TCP/UDP + routing) + DS (tree traversal + graph BFS/DFS + hashing) | Own notes + PYQ wrong answers | Strengthen P1 subjects |
| **C** | 19:00–19:30 | **REVISION PASS 3:** COA (cache + pipeline formulas) + Algo (complexity + sorting + MST/SP) | Formula card | Quick formula refresh |
| **C** | 19:30–20:00 | **Aptitude revision:** Quant formulas + Reasoning tricks + English grammar rules | Formula card | Lock 18+ aptitude |
| **C** | 20:00–22:00 | **🔥 MOCK-2: Full 100Q / 120 min** — use a different IOCL full mock from test series | IOCL Test Series | Final exam simulation |
| **C** | 22:00–22:30 | Mock-2 analysis: compare with Mock-1, update error log, final weak area identification | Error log | |
| **C** | 22:30–23:00 | **Exam prep:** Pack bag (call letter + photo ID + pen), confirm centre route (IDZ Dohna), set alarms | — | **SLEEP BY 23:00** |

**Day 4 Output: TOC + Compiler PYQ-locked + DL PYQs done + full revision + Mock-2 → ~60+ Qs pattern-recognized**

---

### DAY 5 — 24 Sept (Wed) · **🔥 IOCL CBT — BAREILLY** · Report 12:30 PM

| Time | Task |
|------|------|
| 07:00 | Wake up, breakfast |
| 08:00–09:30 | **Formula card skim ONLY** — OS scheduling rules, page replacement, Banker's, normalization rules, subnetting, cache formulas, probability, sorting complexities, DFA rules, K-map. **NO new topics. NO questions.** |
| **09:30** | **🛑 HARD STOP — study is OVER** |
| 09:30–10:15 | Shower, get dressed, eat |
| 10:15 | Documents check: call letter (photo affixed + signed) + photo ID original + photocopy + pen |
| 11:00 | Leave for centre (Shri Siddhi Vinayak Institute, Nainital Road, near Dohna Rly Stn) |
| **12:30** | **REPORTING at ION Digital Zone IDZ Dohna · gate closes 13:00** |
| ~13:30–15:30 | **CBT 100Q / 120 min** — Strategy below |

### CBT Exam Strategy

| Phase | Time | Action |
|-------|------|--------|
| **Scan** | 0–5 min | Skim all 100 Qs, mentally tag: ✅ (sure), 🤔 (attempt), ❌ (skip) |
| **Round 1** | 5–60 min | Do all ✅ questions (~50-60) — these are your banked marks |
| **Round 2** | 60–100 min | Attempt 🤔 questions — eliminate 2 options first, then pick |
| **Round 3** | 100–115 min | Review marked answers, fix silly mistakes |
| **Final** | 115–120 min | ONLY attempt ❌ if you can eliminate 3 of 4 options. Otherwise LEAVE BLANK. |

**Gate requirements (OBC-NCL):** Tech ≥ 40% (30/75), Apt ≥ 40% (10/25), Overall ≥ 45% (45/100).

---

## 📊 Expected Score Model

| Subject | Est Qs | Target Correct | Net Marks |
|---------|--------|---------------|-----------|
| OS | ~8 | 6 | 5.5 |
| DBMS | ~7 | 5 | 4.5 |
| CN | ~7 | 5 | 4.5 |
| DS | ~6 | 4 | 3.5 |
| COA | ~7 | 4 | 3.5 |
| DL | ~7 | 4 | 3.5 |
| Algo | ~5 | 3 | 2.5 |
| TOC | ~7 | 3 | 2.5 |
| Eng Maths | ~12 | 5 | 4.0 |
| Compiler | ~4 | 2 | 1.5 |
| **Tech subtotal** | **~70** | **~41** | **~35.5** |
| Quant | ~10 | 7 | 6.5 |
| Reasoning | ~8 | 6 | 5.5 |
| English | ~7 | 5 | 4.5 |
| **Apt subtotal** | **~25** | **~18** | **~16.5** |
| **TOTAL** | **~95 attempted** | **~59** | **~52 net** |

**Realistic range: 50-65/100** depending on execution. Passes OBC-NCL gates (30/75 tech, 10/25 apt, 45/100 overall).

---

## ⚠️ HARD RULES (from FOCUS-PROTOCOL.md — still active)

1. **Phone never enters the study room.** Charge it in another room.
2. **Laptop = KnowledgeGate + notes ONLY.** SelfControl app blocks everything else.
3. **Breaks are offline.** Walk, water, stretch. Screens are not a break.
4. **No-zero-day.** Minimum 3 blocks even on a bad day.
5. **Sleep ≥ 6h.** Exhaustion destroys recall. Sleep by 23:00, wake by 06:00.

---

> **This is not about being perfect. It's about being strategic.**
> You have 62.5–73.5% on live CBTs. You know how to take exams.
> 40 focused hours of notes + PYQs will beat 100 hours of unfocused video watching.
> **Let's go.**
