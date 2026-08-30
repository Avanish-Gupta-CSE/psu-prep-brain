# ISRO Scientist/Engineer ‘SC’ (CS) -- Syllabus & Preparation Roadmap

**Recruitment:** ISRO ICRB Advt No. `ISRO:ICRB:03(EMC):2026`  
**Target Discipline:** Computer Science & Engineering (Post Code: `BE003`)  
**Exam Format:** 80 Technical MCQs (90 mins) + 15 Aptitude MCQs (30 mins)  

---

## 🎯 Technical Syllabus Breakdown (Part 'A' - 80 Questions)

The ISRO ICRB syllabus is benchmarked directly against the standard GATE CS core curriculum with an emphasis on conceptual clarity, memory-based questions, and core numerical computations:

### 1. Digital Logic & Computer Organization and Architecture (COA)
- Combinational Circuits (Adders, Multiplexers, Decoders), Sequential Circuits (Flip-Flops, Counters, Registers).
- Number representation (2's complement, IEEE 754 floating point format).
- Machine instructions, Addressing modes, ALU, Data path and Control Unit (Hardwired vs Microprogrammed).
- Instruction Pipelining, Pipeline Hazards (Data, Structural, Control), Branch Prediction, Speedup calculation.
- Memory Hierarchy: Cache memory (Direct mapped, Set Associative, Fully Associative), Cache write policies, Hit ratio, Virtual memory, TLB.
- I/O interface: Interrupts, DMA controller.

### 2. Programming and Data Structures
- Programming in C (Pointers, recursion, scoping, dynamic memory allocation).
- Arrays, Stacks, Queues, Linked Lists, Trees (Binary, BST, AVL Trees, Red-Black Trees, Heaps).
- Priority Queues, Binary Heaps (Min/Max Heap construction & operations), Disjoint Set Union (DSU).

### 3. Algorithms & Analysis
- Asymptotic notation (Big-O, Omega, Theta), Master Theorem, Recurrence relations.
- Divide and Conquer: Merge Sort, Quick Sort, Binary Search, Closest Pair.
- Greedy Algorithms: Huffman Coding, Fractional Knapsack, Activity Selection.
- Dynamic Programming: 0/1 Knapsack, LCS, Matrix Chain Multiplication, Warshall/Floyd-Warshall.
- Graph Algorithms: BFS, DFS, Shortest Paths (Dijkstra, Bellman-Ford), Minimum Spanning Trees (Prim, Kruskal).
- NP-Completeness, P vs NP, Reduction basics.

### 4. Theory of Computation & Compiler Design
- Regular Expressions, Finite Automata (DFA, NFA, Minimization), Pumping Lemma for Regular Languages.
- Context-Free Grammars (CFG), Pushdown Automata (PDA), Chomsky Hierarchy.
- Turing Machines, Decidability, Halting Problem, Undecidability.
- Lexical Analysis, Parsing (LL(1), LR(0), SLR(1), LALR(1), CLR(1)), Syntax Directed Translation (SDT).
- Intermediate Code Generation (Three-address code), Control Flow Graphs, Code Optimization, Dataflow analysis.

### 5. Operating Systems
- Processes, Threads, CPU Scheduling (FCFS, SJF, SRTF, Round Robin, Priority, Multi-level Queue).
- Inter-process Communication, Synchronization (Peterson's algorithm, Semaphores, Mutex, Classical IPC problems).
- Deadlocks (Resource Allocation Graph, Banker’s Algorithm, Prevention, Detection & Avoidance).
- Memory Management: Paging, Multi-level Paging, Inverted Page Tables, Segmentation, Page Replacement (FIFO, LRU, Optimal).
- File Systems, Directory structures, Disk Scheduling algorithms (SSTF, SCAN, LOOK, C-SCAN).

### 6. Databases (DBMS)
- ER Model, Relational Algebra, Tuple Relational Calculus, SQL (DDL, DML, DCL, Window functions).
- Functional Dependencies, Canonical Cover, Normal Forms (1NF, 2NF, 3NF, BCNF).
- Transaction Processing, ACID Properties, Serializability (Conflict & View Serializability).
- Concurrency Control: 2PL (Strict, Rigorous), Timestamp ordering, Multiversion protocols.
- File Organization, Indexing (Dense, Sparse, Multilevel, B-Trees, B+ Trees).

### 7. Computer Networks
- Concept of Layering (OSI and TCP/IP models).
- Data Link Layer: Framing, Flow control, Error control (CRC, Checksum), MAC protocols (CSMA/CD, Pure & Slotted ALOHA).
- Network Layer: IPv4/IPv6, CIDR Subnetting, Routing algorithms (Distance Vector, Link State), RIP, OSPF, BGP, ARP, DHCP, ICMP, NAT.
- Transport Layer: TCP & UDP, Flow control (Sliding Window), Congestion control (Slow start, Congestion avoidance, Fast retransmit/recovery), Connection management.
- Application Layer: DNS, HTTP/HTTPS, FTP, SMTP, SSH, Telnet.
- Security: Cryptography (AES, DES, RSA), Public Key Infrastructure, Digital Signatures, Firewalls.

---

## 🧠 Part 'B': Aptitude & Reasoning (15 Questions / 20 Marks)

- **Quantitative Ability:** Arithmetic, algebra, geometry, probability, permutations, data interpretation.
- **Analytical & Logical Reasoning:** Coding-decoding, series completion, syllogisms, visual patterns, analytical puzzles.
- **Deductive Logic:** Data sufficiency, premise-conclusion evaluation.

---

## 🚀 Strategic Prep Action Plan

1. **Leverage Shared-Core Repository:** All 7 CS core areas are already mapped in `Notes/Shared-Core/` and `CoalIndiaLimited-PSU/`.
2. **Speed Drill Strategy:** 80 questions in 90 minutes gives ~1.1 minutes per question. Prioritize quick formula applications and direct theoretical assertions.
3. **Previous Year Question (PYQ) Mastery:** Solve ISRO ICRB CS papers (2015–2024) available in the repository.
