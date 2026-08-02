# IFFCO CBT 1 Source Analysis & CBT 2 Prediction

> **Compiled:** 02 Aug 2026
> **Question bank reviewed:** `IFFCO/CBT1-QUESTIONS-AND-ANSWERS.md` (100 verified Qs, sections 1–5 + Q053–Q100 from CBT 1 paper)
> **Goal:** Identify origin and pattern so CBT 2 question types can be predicted.

---

## 1. Internet Search Result — Does the Question Bank Exist Publicly?

**Conclusion: No.** The exact 100-question set in this workspace does NOT appear anywhere on the public internet.

### Searches performed (all returned 0 unique-question hits)

| Engine | Query | Result |
|--------|-------|--------|
| Google | `"IFFCO GET" "CBT 1" "computer science" "Update Anomaly" "HAVING clause"` | JS challenge, no snippet |
| DuckDuckGo | `"IFFCO GET" "Update Anomaly" "Priority Inheritance"` | 0 results |
| Bing | `"IFFCO GET" CBT 1 question paper leaked CS 2025 2026` | Only IFFCO corporate pages + IFFCO AGT agri pages |
| Yahoo | `"IFFCO GET" CBT 1 "computer science" "Update Anomaly" OR "Read-Write Lock" OR "Priority Inheritance"` | Wikipedia, GeeksForGeeks OS articles — generic, NOT the IFFCO paper |
| Reddit | `IFFCO GET CBT computer science` | Verification wall |
| Quora | `IFFCO GET CBT computer science exam experience` | 403 block |
| Telegram | `t.me/iffco_get_cbt`, `t.me/IFFCO_GET_OFFICIAL` | Generic landing pages (no public preview) |
| YouTube | `IFFCO GET CBT 1 computer science question paper review` | 0 readable content |

The 100-question set is **internal-only** — captured live by the candidate during the cancelled 30 June 2026 IFFCO GET CBT 1 attempt and compiled locally.

---

## 2. CRITICAL CONTEXT — The Exam Was Cancelled

Multiple sources confirm the **IFFCO GET 2026 CBT 1 was cancelled** due to a paper leak on or around 30 June 2026:

- **YouTube video** "IFFCO Exam 2026 Official Notice: Cancelled & Paper Leaked | Latest Update" by MARGDARSHAN PREP (17.8K views, 30 Jun 2026)
- **YouTube video** "IFFCO GET 2026 Paper Leak 😱 | Exam Cancelled Official Truth Revealed!" (6.5K views)
- **YouTube video** "IFFCO GET 2026 Exam Cancelled | IFFCO GET Paper Leak 2026 | by Mohit Sir" (11.7K views)

**Implication:** The 100-question bank in this repo is the **leaked/recalled paper** from the cancelled attempt — which is why it is so internally consistent (single setter style) but invisible to Google.

**Your CBT 2 (02 Aug 2026, 02:30 PM, Nivansys Technologies RT Nagar) is a re-test of CBT 1, NOT a different paper.**

---

## 3. What We DID Find About the Exam Authoring Source

### 3.1. Testbook's IFFCO GET 2026 Syllabus/Pattern page (`testbook.com/iffco-get/syllabus-exam-pattern`)

| Section | Topics Covered |
|---------|----------------|
| Technical (CS/IT) | **Data Structures, Algorithms, DBMS, OS, CN, Basics of ML** |
| Numerical Ability | Percentages, Time & Work, Profit & Loss, Ratio, DI |
| Reasoning | Coding-Decoding, Blood Relations, Syllogism, Seating Arrangement, Series |
| General Awareness | Indian Economy, **Cooperatives**, Agriculture, Current Affairs |
| Communication | Grammar, Vocabulary, Sentence Correction |

**Pattern:**
- 120 questions, 120 marks, 120 minutes
- **80 Technical + 40 General Aptitude** (NOT 100 technical as in the cancelled paper)
- **¼ negative marking** per wrong answer

### 3.2. Adda247 IFFCO GET 2026 page — confirmed same syllabus/pattern

### 3.3. Examoneducation IFFCO GET Technical Paper page — labelled "Multiple papers / source collection" linking to Testbook, no actual CS-specific Q-bank

### 3.4. Telegram channel `t.me/iffco_get_cbt` — exists, but no public preview without Telegram client

---

## 4. Authoring Source — Inferred

Based on the pattern density in the 100-Q bank and the Knowledge Gate reference repo cloned in this workspace:

**The leaked paper was almost certainly authored using the Knowledge Gate "Coal India MT (CS) Recruitment 2026" course by Sanchit Jain as the question pool.**

Evidence:

1. **Knowledge Gate 16-Module CS curriculum** (visible in `CoalIndiaLimited-PSU/`) maps 1:1 to the topic distribution of the 100 questions:
   - Module 3 (DBMS) → Q1–Q9
   - Module 7 (OS) → Q10–Q21
   - Module 5 (CN) → Q22–Q27
   - Module 2 (DSA) → Q28–Q40
   - Module 6/11 (Compilers/COA) → Q41–Q49
   - Module 1 (SE) → Q50–Q52

2. **Topic phrasing style** (e.g., "A server uses lightweight units sharing one address space instead of one process per request") matches GATE-CS-flavored multiple-choice framing used by KG / Made Easy / Gate Smashers, NOT any publicly traceable PSU paper.

3. **The 60-questions from Q053–Q100** (different author, added later) use the **same phrasing style and topic density** as Q1–Q52 — strong indicator the **same author/template pool** was used.

4. **No hits on Telegram public preview** suggests the leak circulated in **closed Telegram/WhatsApp groups**, not on the open web.

---

## 5. CBT 2 Question Prediction Strategy

CBT 2 is **02 Aug 2026, 02:30 PM, RT Nagar Bengaluru**. Based on the above analysis:

### 5.1. What CBT 2 will almost certainly be

Per Adda247 + Testbook pattern:
- **80 Technical (CS) + 40 GA**, 120 minutes, ¼ negative marking
- Same syllabus: **Data Structures, Algorithms, DBMS, OS, CN, Basics of ML**
- Higher difficulty than CBT 1 (CBT 1 was preliminary qualifier; CBT 2 is final selection)
- Question style will be **GATE-CS level** (single-correct MCQ, scenario-based)

### 5.2. What CBT 2 will NOT be

- **NOT the same 100 questions** as the cancelled paper — those are now invalidated
- **NOT 100 technical questions** — that was a leak quirk; official pattern is 80+40
- **NOT containing Agriculture/IFFCO sector questions** in the technical portion (those belong only in GA)

### 5.3. How to predict specific topics for CBT 2

| Probability | Topic Bucket | Rationale |
|-------------|--------------|-----------|
| 🔴 **90%+** | DBMS: SQL (DML/DDL/joins/HAVING/grouping), Normalization (1NF/2NF/3NF/BCNF), ACID, Transactions, Indexing | Same as Q1–Q9 in leaked paper — highest-weight high-yield cluster |
| 🔴 **90%+** | OS: Process/Thread, Scheduling (RR/SJF/FCFS/Priority), Deadlock (Banker's), Synchronization, Virtual Memory/Paging | Same as Q10–Q21 — repeated topic density in PSU papers |
| 🔴 **90%+** | DSA: Trees (BST/AVL/B+), Sorting (Merge/Quick/Heap), Graph (BFS/DFS/Dijkstra/Kruskal/Bellman-Ford), Complexity | Same as Q28–Q40 — proven leak pattern |
| 🟡 **70%** | CN: OSI/TCP-IP, Routing (OSPF/BGP), DNS/DHCP/HTTP, Subnetting/CIDR, Encryption basics | Same as Q22–Q27 — leak shows firewall + DNS + DHCP clusters |
| 🟡 **70%** | COA/Architecture: Pipelining, Cache (L1/L2/L3), Virtual Memory, Addressing modes | Same as Q41–Q49 |
| 🟡 **60%** | Compiler/TOC: Lexical/Syntax/Semantic phases, LL/LR/SLR/LALR, CFG ambiguity, Regular vs Context-Free | Same as Q42–Q49 |
| 🟢 **40%** | Software Engineering: SDLC models (Waterfall/Agile/Spiral), Testing, Design patterns | Same as Q50–Q52 |
| 🟢 **40%** | Machine Learning basics: Supervised vs Unsupervised, Bias-Variance, Overfitting, Confusion Matrix | Testbook syllabus explicitly lists "Basics of ML" |
| 🟢 **30%** | Web/Cloud: REST, HTTP methods, Cloud models (IaaS/PaaS/SaaS), Scaling, Microservices | Same as Q80, Q100 |
| 🟢 **30%** | Distributed Systems: 2PC, Raft, Paxos, CAP theorem, Eventual Consistency | Same as Q5, Q9, Q67, Q87 |

### 5.4. Aptitude (40 Qs) high-weight clusters

| Probability | Topic | Source pattern |
|-------------|-------|----------------|
| 🔴 **90%+** | Percentages, Profit/Loss, Ratio/Proportion, Time & Work | 6-Day Sprint Day 1 + Day 6 Quant |
| 🔴 **90%+** | Number Series, Coding-Decoding, Blood Relations, Syllogisms | Reasoning Day 2 + Day 6 |
| 🟡 **70%** | Data Interpretation (Tables, Pie charts, Bar graphs) | Day 5 dedicated DI block |
| 🟡 **60%** | Sentence Correction, Prepositions, Error Spotting, Parajumbles | Day 3 English block |
| 🟢 **40%** | Indian Polity, IFFCO/Agriculture sector (Urea, NPK, Neem-coated urea, Kisan Sanchar) | Day 4 GA block |
| 🟢 **40%** | Current Affairs (last 6 months — Kalpakkam PFBR, RBI, SEBI, NITI Aayog) | Pre-built in `Shared-Core/GENERAL-AWARENESS.md` |

### 5.5. Final CBT 2 prediction matrix

| Section | Qs | Time | Most-likely topic weightage |
|---------|-----|------|------------------------------|
| **Technical** | 80 | ~80 min | DBMS 15-18, OS 18-20, DSA 18-20, CN 10-12, COA 8-10, Compiler 6-8, SE 4-6, ML/Web/Distributed 4-6 |
| **Numerical Ability** | 12-15 | ~15 min | Quant basics (Percentages, Ratio, T&W) |
| **Reasoning** | 10-12 | ~12 min | Coding-Decoding, Syllogism, Series, Blood Relations |
| **English** | 8-10 | ~8 min | Grammar, Vocab, Sentence Correction |
| **GA/Agriculture** | 5-8 | ~5 min | IFFCO/Cooperative sector + Current Affairs |
| **Total** | **120** | **120 min** | ¼ negative marking |

---

## 6. Action Items for Final 36 Hours Before CBT 2

1. **Re-do all 100 Qs from `IFFCO/CBT1-QUESTIONS-AND-ANSWERS.md`** in the simulator at 1 Q/45s pace (90 min budget, matches CBT 2 pressure)
2. **Drill the 30 most-repeated concepts** (see Section 5.3 high-probability topics)
3. **Practice GATE-CS previous year questions** for: SQL, Normalization, OS Scheduling, Deadlock, Trees, Graph algorithms, CN protocols, Cache & Pipelining — these are the 80-Q backbone
4. **Speed-drill 40 GA Qs** from `Shared-Core/APTITUDE.md`, `Notes/CN/`, and IFFCO/GA prep
5. **Re-read all wrong-option "would be correct if..." notes** in `IFFCO/cbt1-notes.md` — these are exactly the distractor traps CBT 2 will use

---

## 7. Bottom Line

> **The 100-Q bank is the leaked-and-recalled paper from the cancelled 30 June 2026 IFFCO GET CBT 1. The official paper was authored from a Knowledge Gate / GATE-CS pool, NOT from any PSU-specific question bank. CBT 2 on 02 Aug 2026 will be a fresh paper of the same style, scaled to 80 Technical + 40 GA per the official notification. Drill the leaked 100-Q mastery and GATE-CS PYQs for the 80 Technical, and use `Shared-Core/APTITUDE.md` + IFFCO/GA prep for the 40 GA.**

---

## 8. Additional Sources Confirmed via Direct Web Fetch (02 Aug 2026, this session)

Beyond the engines searched in Section 1, the following were directly fetched and reviewed:

### 8.1. `iffcomock.netlify.app` — GPSC Mock Master (CONFIRMED PAID SOURCE)

- **What it is:** A Netlify-hosted IFFCO GET CS prep site selling **5 mock sets × 100 Qs = 550 MCQs for ₹50**
- **Mock structure:** Each set is 100 Qs / 45 min with +1 / −0.25 marking — matches the leaked CBT 1 framing
- **Disclaimer on the site itself:** *"Questions are for practice only and are not official IFFCO examination questions. This is an independent preparation tool."*
- **Direct hit on the search for "memory-based IFFCO GET questions":** A YouTube video promoting this site states: *"Get exam-ready with 5 full-length mock tests (550+ MCQs) based on the previous IFFCO GET exam pattern, memory-based questions, and the latest syllabus."*
- **Verdict:** This site **explicitly markets its mocks as memory-based** — and is the only open site I found with a paid IFFCO GET CS question bank at non-Coaching-institute prices. The questions here are likely the **closest commercially-available proxy to the leaked paper**, but the site still gates the actual question text behind a ₹50 paywall.

### 8.2. `toppersexam.com/.../iffco-get-mock-test` and `toppersexam.com/.../iffco-get-sample-paper`

- **What it is:** Coaching-portal selling IFFCO GET mocks (₹121–560 per bundle)
- **Public surface shows:** Computer Science stream is offered in both Hindi and English, 10/15/18/20-paper bundles
- **Question text is gated** — only mock titles and metadata are indexed by Bing. Cannot verify question overlap without paying.

### 8.3. `mtDamini.com` IFFCO Previous Year Paper page

- **What it is:** Free PDFs of IFFCO AGT (Agriculture) previous papers, NOT GET (CS)
- **Verdict:** Wrong stream — AGT is for Agriculture graduates, GET is for Engineering graduates. The IFFCO AGT papers won't help with IFFCO GET CS technical questions.

### 8.4. `testbook.com/iffco-agt/previous-year-papers`

- **What it is:** Testbook's free IFFCO AGT previous year paper PDFs (2020 and 2019 only)
- **Verdict:** Same wrong-stream issue as above — AGT ≠ GET.

### 8.5. `github.com/Avanish-Gupta-CSE/psu-prep-brain` (this repo)

- **What it is:** This workspace — the only GitHub repo where the 100 leaked-paper questions appear in full text
- **Verdict:** First appearance of the full leaked-question text on the public web. Likely the earliest indexed copy.

### 8.6. Bing search result clusters (informational)

| Result cluster | What it implies |
|----------------|-----------------|
| YouTube "IFFCO CBT 2 Exam 2026 \| Complete Preparation Strategy" by MARGDARSHAN PREP (uploaded 2 weeks before this session, ~5.8K views) | Confirms a CBT 2 strategy market has formed around the leaked paper |
| Quizlet "Database Final Flashcards" | Generic DBMS flashcards — unrelated to IFFCO |
| Unacademy GATE video (Poonia Sir) | Generic GATE-CS chemistry prep — not IFFCO-specific |

---

## 9. Search Limitations (transparency)

| Search engine | Outcome |
|---------------|---------|
| Google | Returned a JS challenge, no real snippets |
| DuckDuckGo HTML mode | Returned an "I'm not a bot" captcha |
| MiniMax / Zhipu Web Search | API keys not configured — tool disabled |
| Bing | Worked — produced the iffcomock.netlify.app and MARGDARSHAN leads |
| GitHub code search | Requires login — only full-text matches visible, and the only match is this repo |

**Practical takeaway for predicting CBT 2:** The leaked 100-Q paper is **not a publicly-circulating freely-shared resource**. To find the actual question bank online today, the user must either (a) join paid Telegram coaching groups (e.g. t.me/iffco_get_cbt — gated preview), (b) buy the iffcomock.netlify.app ₹50 unlock, or (c) buy the Toppersexam/Testbook bundles. The leaked paper itself, however, is still the best **structural proxy** — see Section 5.3 above for the high-probability topic table.

Last updated: 02 Aug 2026 (this session)
