# Daily Plan — 13 May 2026 (9:00 AM → 5:00 AM)

Goal: finish **11 May (DBMS)** + **12 May (OS-1)** + **13 May (OS-2)** catch-up within an office day, with HR snaps at **1:15 PM**, **1:30 PM**, **5:35 PM** and sleep **11:00 PM → 2:00 AM**.

## Timed schedule (exhaustive)

| Time | Block | What you do (exact) | Done-when (checkpoint) | Drill source |
|---|---|---|---|---|
| 09:00–09:10 | Setup | Open `MSTC/TECHNICAL-QUESTION-BANK.md` + `revision-ebook-glm.md`; write today’s 3 targets: **DBMS finish, OS-1 finish, OS-2 start** | Targets written + timer ready | — |
| 09:10–09:45 | DBMS — SQL traps | JOIN types + ON vs WHERE filtering, NULL traps (`COUNT(*)` vs `COUNT(col)`, `NULL = NULL`), GROUP BY/HAVING | You can explain **WHERE vs HAVING** in 20s + 1 example | `MSTC/TECHNICAL-QUESTION-BANK.md` + [CodeForGeek SQL](https://codeforgeek.com/sql-interview-questions/) |
| 09:45–10:15 | DBMS — Indexing | Why indexes speed reads/slow writes, B-Tree intuition, composite index order, “covering index” idea | You can answer: “Query slow—what do you check?” in 40s | `MSTC/TECHNICAL-QUESTION-BANK.md` |
| 10:15–10:45 | DBMS — Transactions | ACID, anomalies (dirty/non-repeatable/phantom), conflict basics, deadlocks at DB level | You can explain **Serializable** and one anomaly in 40s | [ExamSIDE DBMS transactions](https://questions.examside.com/past-years/gate/gate-cse/database-management-system/transactions-and-concurrency) + [GateOverflow DBMS practice](https://gateoverflow.in/505837/gate-cs-practice-transaction-concurrency-control-dbms) |
| 10:45–11:05 | DBMS mini-mock (record) | 10 rapid-fire DBMS Qs (40s each). Record + write “Top 5 weak” | 10 Qs recorded + top-5 weak list | GateOverflow DBMS + your Q-bank |
| 11:05–11:20 | “Favorite subject” map | Decide: **DBMS** as favorite today. Make a chain map: keys → normalization → joins → indexes → transactions/isolation → deadlocks | One page map + 10s “why favorite” | `MSTC/MSTC.pdf` (pattern: intro → projects → favorite subject) |
| 11:20–11:30 | Buffer | Pack / move | You reach office/travel | — |
| 12:45–13:10 | HR snap prep | 2 deliveries of intro + “why MSTC” + “why PSU” + “weakness” (40s each) | 2 clean retakes (no stumble) | `MSTC/HR-QUESTION-BANK.md` |
| 13:15–13:25 | HR snap #1 | Focus: intro + why MSTC | You get 1 actionable correction | — |
| 13:25–13:30 | Notes | Write 3 bullets: what improved + what to fix | Notes captured | — |
| 13:30–13:45 | HR snap #2 | Focus: strength/weakness + relocation + scenario question | 1 actionable correction captured | — |
| 13:45–13:55 | Notes | Write 3 bullets: what improved + what to fix | Notes captured | — |
| 15:30–15:45 | Micro OS-1 flash | Read aloud: deadlock 4 conditions + 1 prevention | You can say it without looking | `MSTC/TECHNICAL-QUESTION-BANK.md` |
| 17:00–17:25 | HR snap prep | Focus: “colleague not doing work right”, “conflict handling”, “project follow-ups” | 2 crisp answers written | `MSTC/HR-QUESTION-BANK.md` |
| 17:35–17:50 | HR snap #3 | Focus: resume deep-dive + favorite subject | 1 actionable correction captured | — |
| 17:50–18:00 | Notes | Write 3 bullets: what improved + what to fix | Notes captured | — |
| 20:30–20:55 | Reset | Dinner + 10 min walk | Energy restored | — |
| 20:55–21:20 | HR backlog capture | Write 10 bullets from yesterday’s HR class + list recordings pending | Notes exist (not in your head) | Your HR class recording |
| 21:20–22:10 | OS-1 core | Process vs thread, context switch, scheduling goals, deadlock prevention/avoid/detect | You can explain deadlock + one fix clearly | `MSTC/TECHNICAL-QUESTION-BANK.md` + [BYJU’S OS Qs](https://byjus.com/gate/gate-operating-system-questions/) |
| 22:10–22:30 | OS-1 mini-mock (record) | 8 rapid-fire OS Qs (40s each). Record + top-4 weak list | 8 Qs recorded + top-4 weak list | [UseMyNotes OS top 50](https://usemynotes.com/top-50-most-important-questions-in-operating-systems-for-gate-2026-aspirants/) |
| 22:30–23:00 | Wind-down | Prep for 11pm sleep; quick reread only | You’re in bed by 11 | — |
| 23:00–02:00 | Sleep | 3 hours | Wake at 2 | — |
| 02:00–02:35 | OS-2 memory | Paging + virtual memory, page table, TLB basics | You can define paging + TLB in 40s | [GateOverflow OS (GATE 2026)](https://gateoverflow.in/521633/gate-cse-2026-set-1-operating-systems-memory-based-question-56) |
| 02:35–03:10 | OS-2 replacement | FIFO/LRU/Clock/Optimal (intuition + when they fail) | You can compare FIFO vs LRU in 40s | `revision-ebook-glm.md` + GateOverflow OS |
| 03:10–03:20 | Break | Water/walk | Back at desk | — |
| 03:20–04:00 | OS-2 sync | Race condition, critical section, mutex vs semaphore (definition + 1 example) | You can explain race condition in plain English | `MSTC/TECHNICAL-QUESTION-BANK.md` |
| 04:00–04:20 | OS-2 mini-mock (record) | 8 rapid-fire OS-2 Qs | 8 Qs recorded + top-4 weak list | GateOverflow OS + your Q-bank |
| 04:20–04:50 | Mixed mini-mock (record) | 15 mixed Qs (DBMS+OS). 40s + 1 follow-up each | Top-6 weak list | Your Q-bank |
| 04:50–05:00 | Set next | Write: top-6 weak fixes + first block for tomorrow | Next block decided | — |

## Drill sources (top-100 style lists)

- **DBMS (GATE-style)**: [ExamSIDE — Transactions and Concurrency](https://questions.examside.com/past-years/gate/gate-cse/database-management-system/transactions-and-concurrency), [GateOverflow — DBMS practice (transaction & concurrency)](https://gateoverflow.in/505837/gate-cs-practice-transaction-concurrency-control-dbms)
- **OS (GATE-style)**: [UseMyNotes — OS top 50](https://usemynotes.com/top-50-most-important-questions-in-operating-systems-for-gate-2026-aspirants/), [BYJU’S — OS questions](https://byjus.com/gate/gate-operating-system-questions/), GateOverflow OS memory-based: [Q56](https://gateoverflow.in/521633/gate-cse-2026-set-1-operating-systems-memory-based-question-56)
- **Data Structures (top-100 style)**: [AlmaBetter — DS top 100](https://www.almabetter.com/bytes/articles/data-structure-interview-questions-answers), [JavaGuides — DS top 100](https://www.javaguides.net/2026/04/top-100-data-structure-interview-questions-and-answers.html)
- **SQL (top-100 style)**: [DataInterview — top 100 SQL](https://www.datainterview.com/blog/top-100-sql-interview-questions), [Devart — SQL interview Qs](https://blog.devart.com/sql-interview-questions-and-answers.html)
- **React (top-100 style)**: [InterviewQuestions.guru — React](https://interviewquestions.guru/react-interview-questions-answers/), [Guru99 — React](https://www.guru99.com/react-js-interview-questions.html)
- **Node/Express (top-100 style)**: [InterviewQuestions.guru — Node.js](https://interviewquestions.guru/nodejs-interview-questions-answers/), [Devinterview — Express.js](https://devinterview.io/blog/express-interview-questions/)
- **Docker (high-yield)**: [Dataquest — Docker Qs](https://www.dataquest.io/blog/docker-interview-questions-and-answers/), [DataCamp — Docker Qs](https://www.datacamp.com/blog/docker-interview-questions)
- **OOP (high-yield)**: [Guru99 — OOP Qs](https://www.guru99.com/oops-interview-questions.html), [Hackr — OOP Qs](https://hackr.io/blog/oop-interview-questions)
- **TypeScript (high-yield)**: [DataCamp — TypeScript Qs](https://www.datacamp.com/blog/typescript-interview-questions), [Hackr — TypeScript Qs](https://hackr.io/blog/typescript-interview-questions-and-answers)

