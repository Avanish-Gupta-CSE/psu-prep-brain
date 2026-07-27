# IFFCO GET CBT 1 - Actual Exam Questions & Detailed Answers

This document contains the verified questions from **IFFCO GET CBT 1** (Computer Science Technical Section). Use this question bank for **CBT 2 preparation**, rapid revision, and mock practice.

---

## 📊 Summary & Breakdown

| Category | Question Count | Core Topics Covered |
| :--- | :---: | :--- |
| **Database Management Systems (DBMS)** | 9 | Normalization/Anomalies, SQL Clauses, Constraints, ACID, 2PC, Partitioning, Primary Keys, Indexing, Eventual Consistency |
| **Operating Systems (OS)** | 12 | Fragmentation, Virtual Memory, Compaction, Round Robin, Memory Protection, Multithreading, Read-Write Locks, Priority Inheritance, Process Shared Resources, Deadlocks, File Systems, Linux Namespaces |
| **Computer Networks & Distributed Systems** | 6 | MFA, DNS Troubleshooting, Firewalls, DHCP, Aho-Corasick String Matching, Parallel Communication Overhead |
| **Data Structures & Algorithms (DSA)** | 13 | BST/AVL Trees, Dynamic Array Amortized Time, Dijkstra's, Dynamic Programming, BFS Shortest Path, Kruskal's MST, High Task Parallelism, Approximation Algorithms, Priority Queue (Binary Heap), Deque ADT, Bellman-Ford, Middle Insertion (Linked List) |
| **Compiler Design & Computer Architecture** | 9 | Common Subexpression Elimination, Retargetable IR, Out-of-Order Execution, Strength Reduction, Context-Free Grammar, Last-Level Cache, Grammar Ambiguity, Deterministic Parsing, Dynamic Branch Prediction |
| **Software Engineering & Information Retrieval** | 3 | Architectural Design Review, Waterfall SDLC Model, TF-IDF with Inverted Index |
| **Total Questions Captured** | **100 (Full 100% CBT 1 Paper)** | |

---

## 🗄️ Section 1: Database Management Systems (DBMS)

### Q1. Changing one employee department requires updates in many records. Which anomaly is present?
- [ ] Phantom Read
- [x] **Update Anomaly**
- [ ] Lost Update
- [ ] Dirty Read

> **Explanation:** An **Update Anomaly** occurs when data redundancy forces a single logical data change (e.g., updating a department name or manager) to be repeated across multiple records in an unnormalized table, leading to potential data inconsistency if any record is missed.

---

### Q2. Which SQL clause filters grouped results after aggregation?
- [ ] ORDER BY
- [x] **HAVING**
- [ ] WHERE
- [ ] DISTINCT

> **Explanation:** The **`HAVING`** clause filters groups after the `GROUP BY` clause and aggregation functions (`SUM`, `COUNT`, `AVG`, etc.) have been applied. The `WHERE` clause filters individual rows *before* aggregation.

---

### Q3. A database allows blank middle names but must prevent duplicate university email addresses. Which constraint fits?
- [ ] CHECK
- [x] **UNIQUE**
- [ ] NOT NULL
- [ ] DEFAULT

> **Explanation:** A **`UNIQUE`** constraint enforces that all non-null values in a column are distinct while still allowing `NULL` (or blank) entries. `NOT NULL` would incorrectly disallow blank middle names.

---

### Q4. A transaction updates inventory but fails before sales entry. Recovery restores the earlier state. Which ACID property applies?
- [ ] Durability
- [ ] Consistency
- [ ] Isolation
- [x] **Atomicity**

> **Explanation:** **Atomicity** (All-or-Nothing) guarantees that either all operations inside a transaction complete successfully, or all changes are rolled back to restore the database to its state prior to transaction execution.

---

### Q5. A transaction updates two databases; if one fails, both must roll back. Which protocol fits?
- [x] **Two-Phase Commit (2PC)**
- [ ] Raft Consensus
- [ ] Lamport Clock
- [ ] Gossip Protocol

> **Explanation:** **Two-Phase Commit (2PC)** is an atomic commitment protocol used in distributed database systems. It coordinates across multiple database nodes through a *Prepare Phase* and a *Commit/Rollback Phase* to ensure atomic updates across distributed boundaries.

---

### Q6. What is a key advantage of partitioning a large industrial database table?
- [ ] Removes indexes
- [ ] Eliminates backups
- [ ] Reduces user count
- [x] **Improves manageability and query performance**

> **Explanation:** **Table Partitioning** divides a very large table into smaller, more manageable physical units. This enables *partition pruning* (allowing the query optimizer to scan only relevant partitions) and significantly speeds up query performance and maintenance tasks.

---

### Q7. A banking table must uniquely identify each account and be referenced by transaction tables. What should be used?
- [x] **Primary Key on Account ID**
- [ ] Check constraint on Balance
- [ ] Unique Customer Name
- [ ] Index on Balance

> **Explanation:** A **Primary Key** uniquely identifies each row in a database table, prohibits `NULL` values, and acts as the target referenced by foreign key constraints in child/referencing tables (like transaction tables).

---

### Q8. Equality searches on a 40-million-row product-code column are slow; inserts are infrequent. What helps most?
- [ ] Increase VARCHAR length
- [ ] Normalize into more tables
- [ ] Store Product Code as BLOB
- [x] **Create an index on Product Code**

> **Explanation:** Creating an **Index** (e.g. B-Tree or Hash Index) on the queried column replaces a costly $O(N)$ full table scan across 40 million rows with a fast $O(\log N)$ or $O(1)$ lookup, dramatically reducing query response time.

---

### Q9. A database must remain available during partitions, accepting temporarily stale replica reads. Which model fits?
- [ ] Sequential Consistency
- [ ] Linearizability
- [x] **Eventual Consistency**
- [ ] Strict Serializability

> **Explanation:** Under the **CAP Theorem**, distributed systems that choose Availability and Partition Tolerance (AP) adopt **Eventual Consistency**, allowing local replicas to process reads and writes during network partitions even if data is temporarily stale, guaranteeing all replicas converge eventually.

---

## 💻 Section 2: Operating Systems (OS)

### Q10. Free memory is scattered into small non-contiguous blocks despite enough total memory. What is this?
- [ ] Thrashing
- [ ] Deadlock
- [x] **External Fragmentation**
- [ ] Internal Fragmentation

> **Explanation:** **External Fragmentation** occurs in contiguous memory allocation when total free memory is large enough to satisfy an allocation request, but the space is fragmented into small, non-contiguous blocks.

---

### Q11. RAM is insufficient, yet applications continue by moving inactive pages to storage. Which mechanism enables this?
- [ ] Memory Fragmentation
- [x] **Virtual Memory**
- [ ] Direct Memory Access
- [ ] Register Allocation

> **Explanation:** **Virtual Memory** uses secondary storage (swap space or page files) to extend physical RAM. Inactive pages are swapped out to disk so active applications can continue executing seamlessly.

---

### Q12. Variable-size allocations fail due to scattered free memory despite enough total space. What helps?
- [ ] Memory Mapping
- [ ] Demand Paging
- [x] **Memory Compaction**
- [ ] Copy-on-Write

> **Explanation:** **Memory Compaction** (defragmentation) shifts allocated memory processes in physical RAM to consolidate all free memory fragments into one large contiguous block.

---

### Q13. Which scheduling method allocates CPU time slices to processes?
- [ ] Segmentation
- [ ] Paging
- [x] **Round Robin**
- [ ] FIFO Scheduling

> **Explanation:** **Round Robin (RR)** scheduling allocates CPU time in fixed time quantum slices to processes in a circular queue, providing preemptive, fair time-sharing for interactive systems.

---

### Q14. Which OS mechanism prevents one application from accessing another application's memory?
- [x] **Memory Protection**
- [ ] Caching
- [ ] Multithreading
- [ ] Spooling

> **Explanation:** **Memory Protection** uses MMU hardware, base/limit registers, and page table permission flags to isolate address spaces, ensuring one process cannot illegally read or overwrite another process's memory.

---

### Q15. A server uses lightweight units sharing one address space instead of one process per request. Main benefit?
- [x] **Lower context-switch overhead and better scalability**
- [ ] No synchronization required
- [ ] Complete memory isolation
- [ ] Automatic race-condition elimination

> **Explanation:** **Multithreading** uses lightweight threads that share a single process address space. Thread context switches avoid page table switches and TLB flushes, resulting in substantially **lower context-switch overhead and higher request throughput/scalability**.

---

### Q16. Many threads contend for a shared structure in read-heavy workload. Which lock improves scalability?
- [ ] Counting Semaphore
- [ ] Binary Semaphore
- [ ] Barrier Synchronization
- [x] **Read-Write Lock**

> **Explanation:** A **Read-Write Lock** (shared-exclusive lock) allows multiple concurrent reader threads to hold the lock simultaneously while restricting writer threads to exclusive access. For read-heavy workloads, this eliminates reader contention and vastly improves concurrency.

---

### Q17. A low-priority thread holds a resource needed by a high-priority thread. What prevents priority inversion?
- [ ] Round Robin Scheduling
- [x] **Priority Inheritance**
- [ ] Multilevel Feedback Queue
- [ ] Time Slicing

> **Explanation:** **Priority Inheritance** is a synchronization protocol where a lower-priority thread holding a resource required by a higher-priority thread temporarily inherits the higher priority until it releases the resource, preventing medium-priority threads from preempting it (unbounded priority inversion).

---

### Q18. Which resource is shared among threads belonging to the same process?
- [ ] Program counter
- [x] **Virtual address space**
- [ ] Stack
- [ ] Register set

> **Explanation:** Threads belonging to the same process share the process's **Virtual Address Space** (code section, data section, heap, and open OS resources). However, each thread maintains its own private stack, program counter (PC), and register set.

---

### Q19. Two processes waiting on each other cause what issue?
- [ ] Fragmentation
- [ ] Paging
- [ ] Thrashing
- [x] **Deadlock**

> **Explanation:** A **Deadlock** is a state where two or more processes are blocked indefinitely because each process holds a resource that the other process is waiting to acquire, creating an unresolvable circular wait condition.

---

### Q20. Which operating system subsystem is primarily responsible for organizing files, directories and metadata on storage devices?
- [ ] Virtual Memory Manager
- [x] **File System**
- [ ] Process Scheduler
- [ ] I/O Scheduler

> **Explanation:** The **File System** is the OS subsystem responsible for structuring non-volatile storage into files and hierarchical directories, managing storage space allocation, and recording file metadata (e.g. inodes, permissions, timestamps).

---

### Q21. Lightweight environments share the host kernel while isolating processes and file systems. Key OS feature?
- [ ] Process Forking
- [ ] Demand Paging
- [x] **Namespaces**
- [ ] Memory-Mapped Files

> **Explanation:** Linux **Namespaces** (PID, Mount, Network, IPC, User namespaces) provide containerization isolation by giving processes isolated views of kernel resources, allowing lightweight container environments to run on a shared host kernel.

---

## 🌐 Section 3: Computer Networks & Security

### Q22. Login requires password plus approval on a registered mobile device. Which mechanism is used?
- [x] **Multi-Factor Authentication**
- [ ] CAPTCHA Verification
- [ ] Password Hashing
- [ ] Single Sign-On

> **Explanation:** **Multi-Factor Authentication (MFA)** requires two or more distinct types of authentication factors: *Something you know* (password) + *Something you have* (registered mobile phone / authenticator app).

---

### Q23. A site works by IP address but not by domain name. Which service should be checked first?
- [ ] FTP
- [ ] DHCP
- [ ] SMTP
- [x] **DNS**

> **Explanation:** **Domain Name System (DNS)** resolves human-readable domain names (e.g. `iffco.in`) into IP addresses. If accessing the site by IP works but the domain name fails, DNS name resolution is failing.

---

### Q24. An administrator must block unauthorized inbound connections while allowing approved traffic. Which control fits best?
- [ ] Repeater
- [x] **Firewall**
- [ ] Layer-2 Switch
- [ ] Network Hub

> **Explanation:** A **Firewall** inspects incoming and outgoing network traffic against defined security policies, blocking unauthorized access attempts while permitting legitimate connections.

---

### Q25. A workstation automatically receives IP address, subnet mask, gateway and DNS server. Which service assigns these?
- [x] **DHCP**
- [ ] NAT
- [ ] ARP
- [ ] DNS

> **Explanation:** **Dynamic Host Configuration Protocol (DHCP)** dynamically assigns IP addresses, subnet masks, default gateways, and DNS server addresses to hosts joining a network.

---

### Q26. A device must search thousands of malware signatures in a data stream. Which algorithm fits best?
- [ ] Binary Search
- [ ] Quick Sort
- [x] **Aho-Corasick**
- [ ] Boyer-Moore

> **Explanation:** The **Aho-Corasick Algorithm** is a multi-pattern string matching algorithm that constructs a finite state automaton with failure links to search thousands of dictionary patterns (malware signatures) simultaneously in a single linear pass over the input stream.

---

### Q27. A parallel graph algorithm slows due to frequent boundary-data exchange. What limits scalability?
- [x] **Communication Overhead**
- [ ] Branch Prediction
- [ ] Cache Coherence
- [ ] Instruction Pipelining

> **Explanation:** In parallel and distributed computing, **Communication Overhead** (latency and bandwidth spent transferring boundary data between worker nodes/threads) often dominates computation time as thread counts grow, bounding parallel speedup (Amdahl's/Gustafson's Law).

---

## 🌲 Section 4: Data Structures & Algorithms (DSA)

### Q28. A BST becomes nearly sorted and search time approaches O(n). Which change best restores efficient search?
- [x] **Use a self-balancing tree such as AVL**
- [ ] Increase application RAM
- [ ] Store duplicate keys in lists
- [ ] Convert the tree into a queue

> **Explanation:** Inserting sorted or nearly sorted elements into a standard Binary Search Tree (BST) creates a skewed tree with $O(n)$ search time. **Self-balancing BSTs** (AVL or Red-Black trees) perform rotations to keep tree height bounded to $O(\log n)$.

---

### Q29. A dynamic array doubles capacity when full. What is the amortized insertion complexity?
- [ ] O(log n)
- [x] **O(1)**
- [ ] O(n)
- [ ] O(n log n)

> **Explanation:** Resizing a dynamic array costs $O(n)$ time, but it only happens when array capacity is exhausted ($1, 2, 4, 8, \dots$). Amortized over $n$ insertions, the aggregate cost per insertion is $\frac{O(n)}{n} = \mathbf{O(1)}$.

---

### Q30. A weighted road graph has non-negative edge weights. Which algorithm gives single-source shortest paths?
- [ ] Depth-First Search
- [ ] Breadth-First Search
- [x] **Dijkstra's Algorithm**
- [ ] Prim's Algorithm

> **Explanation:** **Dijkstra's Algorithm** computes single-source shortest paths on weighted graphs with non-negative edge weights in $O((V + E) \log V)$ time. (BFS only works for unweighted graphs; Prim's finds Minimum Spanning Trees).

---

### Q31. A problem has overlapping subproblems and needs an optimal solution. Which technique fits best?
- [x] **Dynamic Programming**
- [ ] Greedy Algorithm
- [ ] Divide and Conquer
- [ ] Backtracking

> **Explanation:** **Dynamic Programming (DP)** is designed for optimization problems with **Optimal Substructure** and **Overlapping Subproblems**, storing subproblem results (memoization/tabulation) to eliminate redundant computation.

---

### Q32. An unweighted graph needs the minimum number of edges between two vertices. Which algorithm fits?
- [ ] Bellman-Ford Algorithm
- [x] **Breadth-First Search**
- [ ] Depth-First Search
- [ ] Prim's Algorithm

> **Explanation:** **Breadth-First Search (BFS)** traverses an unweighted graph level by level, ensuring that the first time a target vertex is reached, the path taken uses the **minimum number of edges** ($O(V + E)$ time).

---

### Q33. Which algorithm constructs a minimum-cost spanning tree in a connected weighted graph?
- [ ] Bellman-Ford Algorithm
- [ ] Dijkstra's Algorithm
- [x] **Kruskal's Algorithm**
- [ ] Topological Sort

> **Explanation:** **Kruskal's Algorithm** is a greedy algorithm that builds a Minimum Spanning Tree (MST) by sorting all graph edges and adding the smallest edge that does not form a cycle (using Disjoint Set Union) in $O(E \log E)$ time.

---

### Q34. Independent tasks have almost no communication. Which property enables near-linear speedup?
- [ ] Sequential Dependencies
- [ ] Shared Critical Sections
- [ ] Frequent Lock Contention
- [x] **High Task Parallelism**

> **Explanation:** **High Task Parallelism** (or embarrassingly parallel execution) allows independent tasks to run across multiple CPU cores simultaneously with zero lock contention or synchronization overhead, achieving near-linear speedup.

---

### Q35. An in-memory index is searched very frequently but updated only occasionally. It requires sorted records and worst-case O(log n) search, insert and delete. Which structure provides the fastest guaranteed lookup while still maintaining balance?
- [ ] Splay Tree
- [x] **AVL Tree**
- [ ] Red-Black Tree
- [ ] B+ Tree

> **Explanation:** **AVL Trees** are strictly height-balanced (height difference between subtrees $\le 1$). Because AVL trees maintain a tighter height bound ($\approx 1.44 \log_2 n$) compared to Red-Black trees ($\approx 2 \log_2 n$), they deliver faster guaranteed $O(\log n)$ lookup performance, making them superior for read-heavy in-memory indexes.

---

### Q36. An NP-hard optimization problem must be solved for very large instances. A polynomial-time algorithm returns a solution guaranteed to be within a known factor of the optimal. Which class of algorithms is described?
- [ ] Heuristic Search
- [ ] Randomized Algorithm
- [ ] Exact Algorithm
- [x] **Approximation Algorithm**

> **Explanation:** An **Approximation Algorithm** runs in polynomial time for NP-hard problems and provides a mathematical guarantee that the returned solution is within a proven factor $\rho(n)$ (approximation ratio) of the optimal solution.

---

### Q37. A scheduler repeatedly executes the highest-priority process and inserts new tasks efficiently. Best structure?
- [x] **Binary Heap**
- [ ] Fibonacci Heap
- [ ] Balanced BST
- [ ] Binomial Heap

> **Explanation:** A **Binary Heap** is the standard, array-backed data structure used to implement priority queues for process schedulers, offering $O(1)$ peek at the top-priority process and fast $O(\log n)$ task insertions and deletions with minimal memory overhead.

---

### Q38. A data structure must support efficient insertion and deletion at both the front and rear while providing these operations as part of its interface. Which abstract data type is most appropriate?
- [x] **Deque**
- [ ] Stack
- [ ] Priority Queue
- [ ] Queue

> **Explanation:** A **Deque** (Double-Ended Queue) is an Abstract Data Type that explicitly exposes efficient $O(1)$ operations to insert and delete elements at both the front and the rear of the sequence.

---

### Q39. A graph has negative edge weights but no negative cycles. Which single-source shortest path algorithm works?
- [x] **Bellman-Ford Algorithm**
- [ ] Prim's Algorithm
- [ ] A* Search
- [ ] Dijkstra's Algorithm

> **Explanation:** The **Bellman-Ford Algorithm** correctly handles graphs with negative edge weights in $O(V \cdot E)$ time and detects negative-weight cycles. (Dijkstra's algorithm fails on graphs with negative edge weights because greedy choices become invalid).

---

### Q40. A maintenance application frequently inserts and deletes records from the middle of a collection. Which data structure is most suitable?
- [x] **Linked List**
- [ ] Heap
- [ ] Array
- [ ] Stack

> **Explanation:** Once a position in a **Linked List** is reached, inserting or deleting a node requires only updating pointers in $O(1)$ time, avoiding the expensive $O(n)$ contiguous memory element shifting required by arrays.

---

## ⚙️ Section 5: Compiler Design, Computer Architecture & Software Engineering

### Q41. A loop recomputes an expression whose operands do not change. Which optimization removes this repetition?
- [ ] Loop Unrolling
- [ ] Register Spilling
- [ ] Dead Code Elimination
- [x] **Common Subexpression Elimination**

> **Explanation:** **Common Subexpression Elimination (CSE)** identifies identical expressions evaluated repeatedly (such as loop-invariant subexpressions) and replaces them with a single computed value stored in a temporary variable.

---

### Q42. A compiler must target multiple processors with minimal front-end changes. Which design supports this?
- [ ] Independent syntax analyzers
- [ ] Separate lexical analyzers
- [ ] Architecture-specific symbol tables
- [x] **Retargetable compiler using common IR**

> **Explanation:** A **Retargetable Compiler** decouples language parsing (Front-End) from machine code generation (Back-End) by converting source code into a target-independent **Intermediate Representation (IR)**. Porting to a new processor requires only writing a new Back-End generator.

---

### Q43. A processor executes independent later instructions before earlier ones finish while preserving correctness. Technique?
- [ ] Instruction Fusion
- [ ] Loop Unrolling
- [ ] Static Scheduling
- [x] **Out-of-Order Execution**

> **Explanation:** **Out-of-Order (OoO) Execution** (dynamic scheduling) allows processor execution units to run independent instructions out of program sequence when operands become available, while committing results in-order to ensure program correctness.

---

### Q44. A compiler replaces multiplication by a power of two with a shift. Which optimization is this?
- [x] **Strength Reduction**
- [ ] Loop Interchange
- [ ] Tail Recursion Elimination
- [ ] Peephole Optimization

> **Explanation:** **Strength Reduction** is a compiler optimization that replaces computationally expensive operations (like integer multiplication $x \times 8$) with equivalent cheaper machine instructions (like bitwise left shift $x \ll 3$).

---

### Q45. A language needs matching brackets with arbitrary nesting. Simplest grammar class?
- [ ] Regular Grammar
- [ ] Unrestricted Grammar
- [x] **Context-Free Grammar**
- [ ] Context-Sensitive Grammar

> **Explanation:** Matching arbitrarily nested brackets (Dyck language $a^n b^n$) requires memory/stack tracking. Regular grammars (finite automata) cannot maintain unbounded counts, making **Context-Free Grammar (CFG)** (recognized by Pushdown Automata) the simplest grammar class required.

---

### Q46. A program waits mostly for main-memory data rather than computing. Which enhancement helps most?
- [ ] Deeper Pipeline
- [ ] Higher Clock Frequency
- [ ] Additional ALUs
- [x] **Larger Last-Level Cache**

> **Explanation:** For memory-bound workloads bottlenecked by DRAM latency (memory stalls), increasing the **Last-Level Cache (L3/LLC)** capacity retains a larger working set near the CPU cores, dramatically reducing main-memory latency penalties.

---

### Q47. A grammar gives multiple parse trees for the same expression. What correction is needed?
- [ ] Expand symbol table
- [ ] Introduce constant propagation
- [x] **Eliminate grammar ambiguity**
- [ ] Increase lexical lookahead

> **Explanation:** A grammar that produces multiple parse trees for a single valid string is an **Ambiguous Grammar**. To fix this, the compiler designer must rewrite the grammar rules to explicitly enforce operator precedence and associativity levels.

---

### Q48. A parser must detect syntax errors early while scanning left to right without heavy backtracking. Desired property?
- [ ] Nondeterministic Recognition
- [ ] Left Recursion
- [ ] Ambiguous Grammar
- [x] **Deterministic Parsing**

> **Explanation:** **Deterministic Parsing** (e.g. LL(k) or LR(k) parsers) processes input strings in a single deterministic pass without backtracking, enabling immediate syntax error detection at the first illegal token.

---

### Q49. Incorrect conditional-branch outcomes often reduce processor performance. Which feature addresses this?
- [ ] Memory Interleaving
- [x] **Dynamic Branch Prediction**
- [ ] Cache Prefetching
- [ ] SIMD Execution

> **Explanation:** **Dynamic Branch Prediction** uses hardware history tables (like 2-bit branch history registers and Branch Target Buffers) to guess the direction of conditional branches, preventing pipeline stalls and misprediction penalties in superscalar processors.

---

### Q50. Design changes are evaluated for maintainability, scalability, reliability, security and performance. Which activity is this?
- [x] **Architectural Design Review**
- [ ] Database Backup
- [ ] Code Formatting
- [ ] Unit Testing

> **Explanation:** An **Architectural Design Review** (such as ATAM - Architecture Tradeoff Analysis Method) systematically evaluates software architecture against non-functional quality attributes including maintainability, scalability, reliability, security, and performance.

---

### Q51. Which SDLC model is best when requirements are well-defined and stable?
- [ ] Agile
- [ ] Spiral
- [ ] DevOps
- [x] **Waterfall**

> **Explanation:** The **Waterfall Model** is a linear-sequential software development framework where each phase must be completed before the next begins. It is optimal for projects where requirements are completely understood, fixed, and highly stable.

---

### Q52. A search engine processes billions of documents and needs to retrieve the most relevant ones within milliseconds. Which algorithmic approach is most fundamental for efficient text retrieval?
- [ ] A* Search
- [ ] Bellman-Ford Algorithm
- [x] **TF-IDF with Inverted Index**
- [ ] PageRank

> **Explanation:** An **Inverted Index** maps every word/term to a list of documents containing it for sub-millisecond document lookup, while **TF-IDF** (Term Frequency-Inverse Document Frequency) scores the statistical relevance of matching documents for query ranking.

---

## 📌 Usage & Next Steps for CBT 2

1. **Practice via CBT Simulator:** All 52 questions are loaded in `IFFCO/simulator/question-bank.js`.
2. **Review High-Yield Notes:** Cross-reference weak topics with shared core notes:
   - DBMS $\rightarrow$ `Notes/Shared-Core/DBMS.md`
   - OS $\rightarrow$ `Notes/Shared-Core/OPERATING-SYSTEMS.md`
   - Networks $\rightarrow$ `Notes/Shared-Core/COMPUTER-NETWORKS.md`
   - DSA $\rightarrow$ `Notes/Shared-Core/DATA-STRUCTURES-ALGORITHMS.md`
   - Compilers $\rightarrow$ `Notes/Shared-Core/PROGRAMMING-CONCEPTS.md`


### Q053. A directed dependency graph must be checked for cycles before scheduling. Which traversal fits?

- **Options:**
  - A) Depth-First Search
  - B) Kruskal's Algorithm
  - C) Dijkstra's Algorithm
  - D) Breadth-First Search
- **Correct Answer:** **A) Depth-First Search**
- **Explanation:** Depth-First Search (DFS) detects cycles in directed graphs by maintaining a recursion stack. A back-edge pointing to an ancestor node in the active DFS stack confirms a cycle.

---

### Q054. A file system delays writes but must recover reliably after crashes. Which mechanism supports this?

- **Options:**
  - A) Deadlock Detection
  - B) Segmentation
  - C) Journaling
  - D) Swapping
- **Correct Answer:** **C) Journaling**
- **Explanation:** Journaling file systems record metadata/data changes in a dedicated transaction log before committing them to main disk storage, enabling fast, crash-consistent recovery.

---

### Q055. A parallel program spends more time synchronizing than computing. What improves performance?

- **Options:**
  - A) Reduce Synchronization Frequency
  - B) Increase Thread Count
  - C) Deepen Instruction Pipeline
  - D) Increase Cache Size
- **Correct Answer:** **A) Reduce Synchronization Frequency**
- **Explanation:** When lock contention dominates runtime, reducing synchronization frequency (e.g., coarsening lock granularity or batching shared operations) minimizes thread waiting overhead.

---

### Q056. An instruction needs the result of the immediately preceding instruction. Which hardware minimizes the stall?

- **Options:**
  - A) Data Forwarding (Bypassing)
  - B) Branch Prediction
  - C) Register Renaming
  - D) Out-of-Order Execution
- **Correct Answer:** **A) Data Forwarding (Bypassing)**
- **Explanation:** Data Forwarding (or Execution Bypassing) routes output results directly from the EX/MEM pipeline stage back to the ALU inputs, resolving Read-After-Write (RAW) data hazards without pipeline stalls.

---

### Q057. A disk-resident index must minimize disk I/O for millions of records. Which structure is best?

- **Options:**
  - A) Red-Black Tree
  - B) AVL Tree
  - C) B+ Tree
  - D) Trie
- **Correct Answer:** **C) B+ Tree**
- **Explanation:** B+ Trees feature high fan-out, storing hundreds of keys per disk block node. This keeps the tree height shallow (3-4 levels for millions of records) and minimizes disk block I/O.

---

### Q058. Module dependencies form a DAG. Which algorithm gives a valid compilation order?

- **Options:**
  - A) Breadth-First Search
  - B) Kruskal's Algorithm
  - C) Floyd-Warshall Algorithm
  - D) Topological Sort
- **Correct Answer:** **D) Topological Sort**
- **Explanation:** Topological Sort produces a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u -> v, vertex u appears before vertex v.

---

### Q059. Production, Finance and Research networks must communicate with separate IP schemes. Which device routes traffic?

- **Options:**
  - A) Ethernet Hub
  - B) Layer-2 Switch
  - C) Wireless Access Point
  - D) Router
- **Correct Answer:** **D) Router**
- **Explanation:** A Router operates at Layer 3 (Network Layer) of the OSI model and forwards IP packets across different logical subnets and networks.

---

### Q060. Millions of sorted shipment records are searched often and updated nightly. Which search strategy is best?

- **Options:**
  - A) Depth-First Search
  - B) Linear Search
  - C) Breadth-First Search
  - D) Binary Search
- **Correct Answer:** **D) Binary Search**
- **Explanation:** Binary Search offers O(log n) worst-case lookup performance on sorted contiguous arrays/records, making it ideal for static or batch-updated search workloads.

---

### Q061. Which dataset characteristic is most likely to reduce the predictive accuracy of a supervised machine learning model?

- **Options:**
  - A) Feature normalization
  - B) Larger training dataset
  - C) Missing and inconsistent values
  - D) Balanced class distribution
- **Correct Answer:** **C) Missing and inconsistent values**
- **Explanation:** Missing and inconsistent values introduce noise, bias feature distributions, and degrade algorithm learning performance during supervised training.

---

### Q062. An LRU cache needs O(1) lookup and O(1) least-recent eviction. Which implementation fits?

- **Options:**
  - A) B+ Tree + Dynamic Array
  - B) AVL Tree + Queue
  - C) Skip List + Circular Buffer
  - D) Hash Table + Doubly Linked List
- **Correct Answer:** **D) Hash Table + Doubly Linked List**
- **Explanation:** A Hash Table maps keys to Doubly Linked List nodes in O(1) time. The Doubly Linked List allows O(1) removal, insertion, and recency repositioning.

---

### Q063. A compiler checks arbitrarily nested parentheses. Which model is most appropriate?

- **Options:**
  - A) Finite Automaton
  - B) Turing Machine
  - C) Pushdown Automaton
  - D) Linear Bounded Automaton
- **Correct Answer:** **C) Pushdown Automaton**
- **Explanation:** Arbitrarily nested structures represent Context-Free Languages (Dyck language), which require stack memory provided by a Pushdown Automaton (PDA).

---

### Q064. A server waits on disk I/O for many client requests. Which model improves CPU utilization?

- **Options:**
  - A) Cooperative Scheduling
  - B) Static Partitioning
  - C) Non-Preemptive Scheduling
  - D) Asynchronous I/O
- **Correct Answer:** **D) Asynchronous I/O**
- **Explanation:** Asynchronous (non-blocking) I/O allows worker threads to continue executing other client tasks while disk operations run in the background, maximizing CPU utilization.

---

### Q065. A sort must guarantee O(n log n) worst-case performance and support external sorting. Which is preferred?

- **Options:**
  - A) Merge Sort
  - B) Quick Sort
  - C) Heap Sort
  - D) Shell Sort
- **Correct Answer:** **A) Merge Sort**
- **Explanation:** Merge Sort guarantees O(n log n) worst-case time complexity and accesses memory sequentially, making External Merge Sort the standard choice for disk-based data.

---

### Q066. The same arithmetic operation runs on thousands of independent data elements. Which feature helps most?

- **Options:**
  - A) Simultaneous Multithreading
  - B) Superscalar Dispatch
  - C) SIMD Execution
  - D) Out-of-Order Execution
- **Correct Answer:** **C) SIMD Execution**
- **Explanation:** SIMD (Single Instruction Multiple Data) architecture executes a single instruction across vector registers processing thousands of data elements concurrently.

---

### Q067. A system elects a new leader after coordinator failure and replicates logs. Which algorithm fits?

- **Options:**
  - A) Chandy-Lamport
  - B) Vector Clocks
  - C) Raft
  - D) Two-Phase Commit
- **Correct Answer:** **C) Raft**
- **Explanation:** Raft is a distributed consensus algorithm designed for leader election, log replication, and maintaining state machine consistency across cluster nodes.

---

### Q068. A text editor supports frequent edits near cursor in very large documents. Which structure is most suitable?

- **Options:**
  - A) Doubly Linked List
  - B) Rope
  - C) Gap Buffer
  - D) Piece Table
- **Correct Answer:** **C) Gap Buffer**
- **Explanation:** A Gap Buffer maintains an unused memory gap at the insertion cursor position, allowing O(1) typing, insertions, and deletions at the current cursor.

---

### Q069. A compiler must identify keywords, identifiers and literals before parsing. Which phase does this?

- **Options:**
  - A) Semantic Analysis
  - B) Syntax Analysis
  - C) Intermediate Code Generation
  - D) Lexical Analysis
- **Correct Answer:** **D) Lexical Analysis**
- **Explanation:** Lexical Analysis (Scanning) converts character streams from source code into meaningful tokens such as keywords, identifiers, operators, and literals.

---

### Q070. A data warehouse has slow analytical reports despite indexing; updates occur once daily. What helps most?

- **Options:**
  - A) TEXT columns for indexed fields
  - B) Unrelated table splits
  - C) Controlled denormalization to reduce joins
  - D) More foreign key constraints
- **Correct Answer:** **C) Controlled denormalization to reduce joins**
- **Explanation:** In OLAP data warehousing with infrequent write updates, controlled denormalization pre-aggregates and joins tables, eliminating costly runtime SQL join operations.

---

### Q071. Undo stores operations and removes them only in reverse order. Which implementation best fits?

- **Options:**
  - A) Deque
  - B) Circular Buffer
  - C) Stack
  - D) Doubly Linked List
- **Correct Answer:** **C) Stack**
- **Explanation:** A Stack operates on a Last-In, First-Out (LIFO) principle, naturally matching undo mechanisms where the most recent operation is reverted first.

---

### Q072. Which traversal visits root, left subtree, then right subtree?

- **Options:**
  - A) Postorder
  - B) Level Order
  - C) Preorder
  - D) Inorder
- **Correct Answer:** **C) Preorder**
- **Explanation:** Preorder tree traversal visits the current node (Root) first, followed recursively by the Left subtree, and finally the Right subtree.

---

### Q073. An online exam system must keep running if one app server fails. Which design helps most?

- **Options:**
  - A) Higher CPU Clock Speed
  - B) Compressed Static Images
  - C) Redundant Load-Balanced Servers
  - D) Larger Database Cache
- **Correct Answer:** **C) Redundant Load-Balanced Servers**
- **Explanation:** Deploying multiple redundant application servers behind a load balancer ensures high availability; if one server fails, the load balancer reroutes traffic to healthy instances.

---

### Q074. Repeated key lookups must improve from O(n) to average O(1), accepting extra memory. What is best?

- **Options:**
  - A) Linked List
  - B) Binary Heap
  - C) Hash Table
  - D) Queue
- **Correct Answer:** **C) Hash Table**
- **Explanation:** A Hash Table uses hash functions to map keys directly to array buckets, achieving average O(1) time complexity for search, insertion, and deletion.

---

### Q075. A networking application needs to check millions of IP addresses against a blacklist that updates hourly. False positives must be minimized but occasional false positives are acceptable. Which data structure is most appropriate?

- **Options:**
  - A) Hash Table
  - B) Bloom Filter
  - C) Binary Search Tree
  - D) Trie
- **Correct Answer:** **B) Bloom Filter**
- **Explanation:** A Bloom Filter is a space-efficient probabilistic data structure that tests set membership with zero false negatives and controllable false positive rates.

---

### Q076. What is the main purpose of a transaction log?

- **Options:**
  - A) Store passwords
  - B) Create indexes
  - C) Enable recovery and auditing
  - D) Manage sessions
- **Correct Answer:** **C) Enable recovery and auditing**
- **Explanation:** Transaction logs (Write-Ahead Logs) store sequential records of database modifications to ensure crash recovery (ACID durability) and audit capability.

---

### Q077. Which database object automatically executes when specific events occur?

- **Options:**
  - A) Trigger
  - B) View
  - C) Cursor
  - D) Schema
- **Correct Answer:** **A) Trigger**
- **Explanation:** A database Trigger is a stored procedural code block that automatically fires in response to specific events (INSERT, UPDATE, DELETE) on a target table.

---

### Q078. What is the purpose of a semaphore?

- **Options:**
  - A) Encrypt files
  - B) Route packets
  - C) Compress memory
  - D) Synchronize access to shared resources
- **Correct Answer:** **D) Synchronize access to shared resources**
- **Explanation:** A Semaphore is an OS synchronization primitive (an integer counter) used to regulate concurrent thread access to shared critical resources.

---

### Q079. A protocol validates fixed-format headers with no nesting. Which model is sufficient?

- **Options:**
  - A) Context-Sensitive Grammar
  - B) Pushdown Automaton
  - C) Turing Machine
  - D) Deterministic Finite Automaton
- **Correct Answer:** **D) Deterministic Finite Automaton**
- **Explanation:** Fixed-format, non-nested headers define Regular Languages, which can be fully validated by a Deterministic Finite Automaton (DFA) without stack memory.

---

### Q080. A team is designing a web API for a resource-oriented system. They want to follow standard architectural principles where resources are represented as nouns and operations are represented by HTTP methods. Which design principle is this?

- **Options:**
  - A) SOAP-based Design
  - B) RESTful Design
  - C) GraphQL Schema
  - D) RPC-based Design
- **Correct Answer:** **B) RESTful Design**
- **Explanation:** RESTful (Representational State Transfer) architecture uses resource URIs (nouns) and standard HTTP methods (GET, POST, PUT, DELETE) to represent state transfers.

---

### Q081. Which algorithmic complexity grows fastest as data volume increases?

- **Options:**
  - A) O(n^2)
  - B) O(1)
  - C) O(n)
  - D) O(log n)
- **Correct Answer:** **A) O(n^2)**
- **Explanation:** Quadratic growth O(n^2) increases far faster than linear O(n), logarithmic O(log n), or constant O(1) growth rates.

---

### Q082. An optimization problem is NP-Complete. What is practical for very large instances?

- **Options:**
  - A) Binary Search
  - B) Approximation or heuristic algorithms
  - C) Exhaustive search
  - D) Bubble Sort
- **Correct Answer:** **B) Approximation or heuristic algorithms**
- **Explanation:** Because exact algorithms for NP-Complete problems require exponential time, practical large-scale applications rely on approximation or heuristic algorithms.

---

### Q083. Which protocol is commonly used for network device monitoring?

- **Options:**
  - A) Syslog
  - B) ICMP
  - C) NetFlow
  - D) SNMP
- **Correct Answer:** **D) SNMP**
- **Explanation:** Simple Network Management Protocol (SNMP) is the standard application-layer protocol for collecting metrics, performance data, and monitoring network devices.

---

### Q084. A scheduler always runs the process with the shortest estimated execution time. Which algorithm is used?

- **Options:**
  - A) Round Robin
  - B) First Come First Served
  - C) Lottery Scheduling
  - D) Shortest Job First (SJF)
- **Correct Answer:** **D) Shortest Job First (SJF)**
- **Explanation:** Shortest Job First (SJF) CPU scheduling assigns execution priority to the process with the smallest estimated next CPU burst time.

---

### Q085. Which parsing technique naturally handles left-recursive grammars without grammar transformation?

- **Options:**
  - A) Recursive Descent Parsing
  - B) Predictive Parsing
  - C) LR Parsing
  - D) LL(1) Parsing
- **Correct Answer:** **C) LR Parsing**
- **Explanation:** Bottom-up LR parsers shift tokens onto a stack and reduce handles, inherently handling left-recursive grammar rules without getting trapped in infinite loops.

---

### Q086. A compiler needs very fast average lookup for millions of identifiers; order is irrelevant. Best choice?

- **Options:**
  - A) Trie
  - B) B+ Tree
  - C) AVL Tree
  - D) Hash Table
- **Correct Answer:** **D) Hash Table**
- **Explanation:** For unordered symbol table identifier lookups, a Hash Table delivers average O(1) lookup time, superior to O(log n) tree searches.

---

### Q087. A key-value store adds and removes servers with minimal key movement. Which technique fits?

- **Options:**
  - A) Breadth-First Search
  - B) Consistent Hashing
  - C) Dynamic Programming
  - D) Huffman Coding
- **Correct Answer:** **B) Consistent Hashing**
- **Explanation:** Consistent Hashing maps keys and servers onto a circular ring. Adding or removing a server reassigns only K/n keys on average rather than rehashing the entire keyspace.

---

### Q088. Demand paging causes high page faults and low CPU utilization. What should be done first?

- **Options:**
  - A) Increase Time Quantum
  - B) Reduce Degree of Multiprogramming
  - C) Increase Interrupt Priority
  - D) Disable Virtual Memory
- **Correct Answer:** **B) Reduce Degree of Multiprogramming**
- **Explanation:** High page faults coupled with low CPU utilization indicate Thrashing. Reducing the degree of multiprogramming frees RAM pages for active working sets.

---

### Q089. Threads wait briefly for a very short critical section on multicore hardware. Which primitive is preferred?

- **Options:**
  - A) Counting Semaphore
  - B) Mutex
  - C) Condition Variable
  - D) Spinlock
- **Correct Answer:** **D) Spinlock**
- **Explanation:** A Spinlock busy-waits in a CPU loop. On multi-core systems with very short critical sections, this avoids thread context-switch kernel overhead.

---

### Q090. High-priority tasks keep running while low-priority processes wait indefinitely. What issue is this?

- **Options:**
  - A) Starvation
  - B) Deadlock
  - C) Thrashing
  - D) Fragmentation
- **Correct Answer:** **A) Starvation**
- **Explanation:** Starvation (indefinite blocking) occurs when a process is perpetually denied required resources or CPU scheduling due to continuous high-priority task arrival.

---

### Q091. Retries after network failures must not duplicate transaction effects. Which property is required?

- **Options:**
  - A) Atomicity
  - B) Durability
  - C) Idempotency
  - D) Mutual Exclusion
- **Correct Answer:** **C) Idempotency**
- **Explanation:** Idempotency ensures that performing an operation multiple times yields the exact same state outcome as performing it a single time.

---

### Q092. A small working set still causes cache misses due to competing blocks mapping together. Which miss is this?

- **Options:**
  - A) Cold Miss
  - B) Coherence Miss
  - C) Conflict Miss
  - D) Capacity Miss
- **Correct Answer:** **C) Conflict Miss**
- **Explanation:** Conflict Misses occur in direct-mapped or set-associative caches when multiple memory addresses map to the exact same cache set, evicting active blocks.

---

### Q093. A campus network must tolerate a single link failure without isolating other sites. Which topology fits best?

- **Options:**
  - A) Mesh Topology
  - B) Ring Topology
  - C) Linear Daisy Chain
  - D) Bus Topology
- **Correct Answer:** **A) Mesh Topology**
- **Explanation:** A Mesh Topology provides redundant interconnects between nodes, offering alternative routing paths if a single link fails.

---

### Q094. A variable is used before declaration, but syntax is valid. Which phase reports it?

- **Options:**
  - A) Code Optimization
  - B) Lexical Analysis
  - C) Semantic Analysis
  - D) Syntax Analysis
- **Correct Answer:** **C) Semantic Analysis**
- **Explanation:** Semantic Analysis verifies variable declaration, type compatibility, and scope rules using the symbol table after syntax parsing completes.

---

### Q095. Distributed processes lack synchronized clocks. Which mechanism captures causal event ordering?

- **Options:**
  - A) Vector Clocks
  - B) CRC Checksum
  - C) Checkpointing
  - D) Consistent Hashing
- **Correct Answer:** **A) Vector Clocks**
- **Explanation:** Vector Clocks maintain logical clock vectors across nodes to track causal relationships and establish partial ordering of events in distributed systems.

---

### Q096. A compiler needs machine-independent code for optimization before target generation. What is used?

- **Options:**
  - A) Intermediate Representation (IR)
  - B) Symbol Table
  - C) Parse Tree
  - D) Object Code
- **Correct Answer:** **A) Intermediate Representation (IR)**
- **Explanation:** Intermediate Representation (IR) is a machine-independent code format used by compiler middle-ends to perform target-agnostic optimizations.

---

### Q097. A compiler removes code unreachable by control flow. Which optimization is used?

- **Options:**
  - A) Strength Reduction
  - B) Dead Code Elimination
  - C) Loop Fusion
  - D) Constant Folding
- **Correct Answer:** **B) Dead Code Elimination**
- **Explanation:** Dead Code Elimination removes instructions or code blocks that cannot be reached or whose outputs are never evaluated.

---

### Q098. A compiler accepts syntactically invalid programs because its grammar is overly permissive. Which should be corrected first?

- **Options:**
  - A) Tokenizer
  - B) Grammar specification
  - C) Parser lookahead
  - D) Register allocation
- **Correct Answer:** **B) Grammar specification**
- **Explanation:** The Grammar Specification defines valid syntax. Restricting overly broad production rules in the grammar prevents the parser from accepting invalid syntax.

---

### Q099. One core updates a shared cache line; other cores must see the latest value. What ensures this?

- **Options:**
  - A) Speculative Execution
  - B) Instruction Pipelining
  - C) Cache Coherence Protocol
  - D) Virtual Memory
- **Correct Answer:** **C) Cache Coherence Protocol**
- **Explanation:** Cache Coherence Protocols (such as MESI/MOESI) maintain memory consistency across multi-core processor caches by invalidating or updating stale lines.

---

### Q100. A web application experiences sudden traffic spikes. The IT team wants to automatically add servers during peak load and remove them during low usage. Which cloud concept enables this?

- **Options:**
  - A) Serverless Computing
  - B) Virtual Private Cloud
  - C) Elastic Scaling
  - D) Container Orchestration
- **Correct Answer:** **C) Elastic Scaling**
- **Explanation:** Elastic Scaling dynamically provisions or de-provisions compute instances in response to real-time workload fluctuations.

---
