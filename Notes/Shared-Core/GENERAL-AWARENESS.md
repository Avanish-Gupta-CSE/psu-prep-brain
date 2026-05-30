# General GK, English & NIELIT Patterns

This note is designed for rapid revision of general awareness, English spelling rules, and specialized **NIELIT exam patterns** (such as Scientist B and Scientific Assistant) before stepping into the exam hall.

---

## 🏛️ Part 0: NIELIT Core Exam Patterns & Solved PYQs

Unlike TCS or IBPS, NIELIT-conducted exams are heavily influenced by the **GATE computer science syllabus**, focusing on theoretical concepts, mathematical proofs, and system-level behaviors. 

### 1. Theory of Computation (TOC) & Automata
* **Phase-Structured Grammar**: Unrestricted Grammar (Type-0) is also known as *Phase-Structured Grammar*. It is the most general grammar.
* **Turing Machine Equivalences**: 
  * The power of a multi-tape Turing machine is **equal** to a single-tape Turing machine (it only increases speed, not power/capability).
  * Every Non-deterministic Turing Machine (NDTM) has an equivalent Deterministic Turing Machine (DTM) of equal power.
  * Determinism = Non-determinism holds true for **Turing Machines** and **Finite Automata**, but **fails for Pushdown Automata** ($\text{NPDA} > \text{DPDA}$).
* **Finite State Automata Limits**: Palindromes and arbitrary memory strings ($a^n b^n$) *cannot* be recognized by a Finite State Automaton because it lacks arbitrary memory storage.

### 2. Compiler Design
* **Parser Power & State Relations**: 
  * Power order: $\text{CLR} > \text{LALR} > \text{SLR} > \text{LR}(0)$.
  * State size relationship: If SLR has $n_1$ states, LALR has $n_2$ states, and CLR has $n_3$ states:
    $$n_1 (\text{SLR}) = n_2 (\text{LALR}) \le n_3 (\text{CLR})$$
  * Hence, SLR and LALR have exactly the **same number of states** because LALR merges common-core states of CLR.
* **Compilation Phases**: 
  * Lexical Analysis (output = tokens) $\to$ Syntax Analysis / Parsing (output = parse tree) $\to$ Semantic Analysis (type checking) $\to$ Intermediate Code Generation (AST/three-address code) $\to$ Code Optimization $\to$ Code Generation.
  * **Trap**: Type checking is done *after* parsing (during Semantic Analysis), not before!
* **Parser Conflicts**:
  * **Shift-Reduce Conflict**: Arises in LR parsers when the parser cannot decide whether to shift the next input symbol or reduce the current stack elements using a grammar rule. Often caused by grammar ambiguity.
  * **Shift-Reduce Parsing** is also called the **Reverse of Right Most Derivation (RMD in Reverse)**.

### 3. Databases & Transactions
* **Strict Two-Phase Locking (Strict 2PL)**: Generates schedules that are both conflict-serializable and **recoverable** (and cascade-less) because write locks are not released until transaction commit/abort.
* **Thomas' Write Rule**: Applied to Timestamp-Ordering protocols. It ignores out-of-date write operations (blind writes) and can generate **view-serializable** schedules that are *not* conflict-serializable.

### 4. Computer Networks
* **Class B Subnetting Calculations**:
  * In Class B: Default Net ID $= 14 \text{ bits}$, Host ID $= 16 \text{ bits}$.
  * Default number of networks $= 2^{14}$. Default hosts per network $= 2^{16} - 2$.
  * If a problem states: "Class B network has $2^m$ networks and $2^n - 2$ hosts," the relationship is:
    $$m = 14,\ n = 16 \implies 8m = 7n \quad (8 \times 14 = 7 \times 16 = 112)$$
  * To divide Class B for 64 departments: $64 = 2^6 \implies$ steal $6 \text{ bits}$ from Host ID. The subnet mask becomes $255.255.252.0$ (since $255.255.(11111100)_2.0 = 255.255.252.0$).
* **TCP Header & Congestion**:
  * **TCP Checksum**: Calculated over the TCP Header, TCP Data, and a 12-byte **Pseudo-Header** (which contains Source IP, Destination IP, Protocol, and TCP Segment Length). Calculated using 16-bit one's complement sum.
  * **Congestion Avoidance**: The congestion window increases **additively** ($+1 \text{ MSS}$ per RTT) during avoidance and decreases **multiplicatively** (halved) upon detecting packet loss via triple-duplicate ACKs (or drops to $1 \text{ MSS}$ on a Timeout).

---

## ⚛️ Part 1: General Knowledge & Current Milestones (2026 Updates)

### 1. India's Historic Nuclear Energy Milestone (April 2026)
* **What**: Achieving first **criticality** (self-sustaining controlled nuclear fission chain reaction).
* **When**: **6th April 2026** at 08:25 PM.
* **Where**: **Prototype Fast Breeder Reactor (PFBR)** at the Kalpakkam Nuclear Complex, Tamil Nadu.
* **Significance**:
  * Officially transitions India into **Stage-2** of its three-stage nuclear power program first envisioned by **Dr. Homi Jehangir Bhabha**.
  * PFBR is a **500 MWe (MegaWatt electrical)** sodium-cooled fast breeder reactor.
  * Built entirely using indigenous technology by **BHAVINI** (Bharatiya Nabhikiya Vidyut Nigam Limited) and developed with **IGCAR** (Indira Gandhi Centre for Atomic Research).
  * **Stage-2 Action**: Uses Plutonium-239 recovered from Stage-1 Pressurized Heavy Water Reactors (PHWRs). Fast neutrons convert Uranium-238 into more Plutonium-239 (producing more fuel than it consumes—"breeding").
  * **Thorium Bridge**: It will eventually blanket with Thorium-232, transmuting it to Uranium-233 to power Stage-3, tapping India’s massive thorium reserves.
* **Policy Context**:
  * The Union Budget 2025–26 launched the **Nuclear Energy Mission** targeting **100 GW** of nuclear capacity by 2047.
  * **SHANTI Act, 2025** (*Sustainable Harnessing and Advancement of Nuclear Energy for Transforming India Act, 2025*) consolidates India's nuclear legal framework and allows limited private sector participation.

### 2. High-Profile Appointments & National Leadership (May 2026 Status)
* **NITI Aayog**:
  * **Chairman**: Prime Minister Narendra Modi (Ex-officio).
  * **Vice-Chairman**: **Ashok Kumar Lahiri** (Appointed in April 2026, replacing Suman Bery; noted economist, former Chief Economic Advisor).
  * **Interim CEO**: **Nidhi Chhibber** (Assumed additional charge in February 2026 as B.V.R. Subrahmanyam's tenure ended).
* **Reserve Bank of India (RBI)**:
  * **Governor**: **Sanjay Malhotra** (26th Governor, in office since December 11, 2024).
* **SEBI (Securities and Exchange Board of India)**:
  * **Chairperson**: **Madhabi Puri Buch**.

---

## 🔤 Part 2: English Spell-Check & Vocabulary High-Yield Drill

NIELIT exams include multiple-choice questions where you must identify the correctly spelled word.

### 1. Highly Confused Spellings Matrix
| Confused / Pitfall Spelling | Correct Spelling | Why it Traps |
|---|---|---|
| etiqutte, ettiquette | **Etiquette** | Single 't', double 't' in the middle, and ends in 'ette'. |
| paracial, palasial | **Palatial** | From "palace". Uses 't' instead of 'c'. |
| accomodate | **Accommodate** | Double **'c'** and double **'m'**. |
| homogeneous, homogenious | **Homogeneous** | Contains 'eou', not 'iou'. |
| paralleled, paralell | **Parallel** | Double 'l' first, then single 'l': **P-a-r-a-l-l-e-l**. |
| guarantee, guaranty | **Guarantee** | Ends with 'double e' for the verb, 'y' for the financial noun. |
| supercede | **Supersede** | The only word ending in **-sede** (from Latin *supersedere*), not -cede. |
| maintainance | **Maintenance** | Changes from "maintain" to **main-te-nance**. |
| occurance, occurrence | **Occurrence** | Double 'c', double 'r', and ends in **-ence**. |
| independent, independant | **Independent** | Ends with **-ent**, never -ant. |

### 2. Vocabulary Tricks (Antonyms & Synonyms)
* **Elimination by Tone**: Check if options have a positive (+), negative (-), or neutral (0) tone. If the question asks for a synonym of a positive word, eliminate negative options immediately.
* **Suffix Clues**: Words ending in *-less*, *-anti-*, or *-de-* are usually negative, while *-ful*, *-bene-*, or *-pro-* are positive.
* **Root Association**:
  * *Crave* $\to$ desire strongly (+)
  * *Confront* $\to$ face or match directly (neutral/assertive)
  * *Accept* $\to$ receive (+)
  * *Deny* $\to$ refuse (-)
