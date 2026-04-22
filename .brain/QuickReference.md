# Quick Reference & Cheat Sheet

## Time Complexity Cheat Sheet

### Sorting Algorithms
| Algorithm | Best | Average | Worst | Space | Stable? | In-place? |
|-----------|------|---------|-------|-------|---------|-----------|
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes | Yes |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | No |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes | No |

### Data Structure Operations
| Structure | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| Array | O(n) | O(n) | O(n) | O(n) |
| Sorted Array | O(log n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(1) | O(1)* | O(n) |
| Stack/Queue | O(n) | O(1) | O(1) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(n) |
| BST (worst) | O(n) | O(n) | O(n) | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) |
| B-Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(n) | O(log n) | O(log n) | O(n) |

*Delete from LL is O(1) if node reference given, O(n) to find the node first.

### Graph Algorithms
| Algorithm | Time | Space | Use |
|-----------|------|-------|-----|
| BFS | O(V+E) | O(V) | Shortest path (unweighted) |
| DFS | O(V+E) | O(V) | Connectivity, cycle detection |
| Dijkstra | O((V+E) log V) | O(V) | Shortest path (non-negative weights) |
| Bellman-Ford | O(VE) | O(V) | Shortest path (negative weights OK) |
| Floyd-Warshall | O(V^3) | O(V^2) | All-pairs shortest path |
| Prim (min-heap) | O((V+E) log V) | O(V) | MST |
| Kruskal | O(E log E) | O(V) | MST |
| Topological Sort | O(V+E) | O(V) | DAG ordering |

## OS Formulae

### CPU Scheduling
- **Turnaround Time (TAT)** = Completion Time - Arrival Time
- **Waiting Time (WT)** = TAT - Burst Time
- **Response Time (RT)** = First Response Time - Arrival Time
- **Throughput** = Number of processes / Total time
- **CPU Utilization** = (Busy time / Total time) x 100%

### Memory Management
- **Page Table Size** = (Number of pages) x (Page table entry size)
- **Number of pages** = Virtual address space / Page size
- **Number of frames** = Physical memory / Frame size
- **Logical Address** = [Page Number | Page Offset]
  - Page Number bits = ceil(log2(number of pages))
  - Offset bits = ceil(log2(page size))
- **Effective Memory Access Time (with TLB)** = h x (TLB access + Memory access) + (1-h) x (TLB access + 2 x Memory access)
  - h = TLB hit ratio

### Page Replacement
- **Page Fault Rate** = Page faults / Total references
- **Belady's Anomaly:** FIFO can have MORE page faults with MORE frames (does NOT occur in LRU, Optimal)
- **Optimal (OPT):** Replace page that won't be used for longest time (theoretical best)
- **LRU:** Replace least recently used page (stack algorithm, no Belady's)
- **FIFO:** Replace oldest page (can have Belady's anomaly)

### Disk Scheduling
- **Seek Time** = Number of tracks traversed x Time per track
- **SCAN (Elevator):** Head moves in one direction, reverses at end
- **C-SCAN:** Like SCAN but returns to start without servicing
- **SSTF:** Shortest Seek Time First (can cause starvation)

## DBMS Formulae

### Normalization Quick Rules
- **1NF:** No multi-valued attributes, atomic values only
- **2NF:** 1NF + no partial dependencies (all non-key attributes fully depend on entire candidate key)
- **3NF:** 2NF + no transitive dependencies (non-key -> non-key)
- **BCNF:** For every FD X->Y, X must be a superkey
- **3NF vs BCNF:** 3NF allows X->Y where Y is part of a candidate key; BCNF does not

### Decomposition Tests
- **Lossless Join:** R1 intersection R2 -> R1 or R1 intersection R2 -> R2
- **Dependency Preservation:** Union of F1, F2, ... = F+ (closure of original FDs)

### Transaction Isolation
- **Dirty Read:** Reading uncommitted data
- **Non-repeatable Read:** Same query, different results (data modified)
- **Phantom Read:** Same query, different number of rows (rows added/deleted)

### SQL Traps (Examiner Favorites)
- `NULL` comparisons: `NULL = NULL` is UNKNOWN, not TRUE. Use `IS NULL`.
- `COUNT(*)` counts all rows; `COUNT(column)` skips NULLs
- `GROUP BY` requires all non-aggregate SELECT columns to be in GROUP BY
- `HAVING` filters groups; `WHERE` filters rows before grouping
- `UNION` removes duplicates; `UNION ALL` keeps them
- `IN` vs `EXISTS`: EXISTS is correlated, IN is not (performance difference on large datasets)
- Self-join: joining a table with itself (e.g., find employees who earn more than their manager)

## Computer Networks Formulae

### Subnetting
- **Number of subnets** = 2^(subnet bits borrowed)
- **Hosts per subnet** = 2^(host bits) - 2 (subtract network and broadcast)
- **Subnet mask:** /24 = 255.255.255.0, /25 = 255.255.255.128, /26 = 255.255.255.192, /27 = 255.255.255.224, /28 = 255.255.255.240
- **Block sizes:** /25=128, /26=64, /27=32, /28=16, /29=8, /30=4

### Transmission Formulas
- **Transmission Delay** = Packet size / Bandwidth
- **Propagation Delay** = Distance / Speed of signal
- **Total Delay** = Transmission + Propagation + Processing + Queuing
- **Throughput** = Data transferred / Time taken
- **Efficiency** = Useful data / (Useful + Overhead)

### Sliding Window
- **Go-Back-N:** Window size = 2^m - 1 (m = sequence number bits)
- **Selective Repeat:** Window size = 2^(m-1)
- **Stop-and-Wait:** Efficiency = T_transmission / (T_transmission + 2 x T_propagation)
- **Bandwidth-Delay Product** = Bandwidth x RTT

### TCP
- **3-way handshake:** SYN -> SYN-ACK -> ACK
- **Congestion Window:** Slow start (exponential) until threshold, then congestion avoidance (linear)
- **Fast Retransmit:** After 3 duplicate ACKs
- **Tahoe:** On loss: cwnd = 1, threshold = cwnd/2
- **Reno:** On 3 dup ACKs: cwnd = cwnd/2 (fast recovery); On timeout: cwnd = 1

## COA Formulae

### Cache
- **Hit Rate (h)** = Cache hits / Total accesses
- **Miss Rate** = 1 - h
- **Effective Access Time** = h x Cache_time + (1-h) x (Cache_time + Memory_time)
- **Direct Mapping:** Block# mod Number_of_cache_lines
- **Set-Associative:** Set# = Block# mod Number_of_sets
- **Fully Associative:** Any block can go anywhere

### Pipelining
- **Speedup** = Time without pipeline / Time with pipeline
- **Ideal CPI** = 1 (one instruction per cycle)
- **Pipeline throughput** = 1 / max(stage delays)
- **Hazards:** Data (RAW, WAR, WAW), Control (branch), Structural (resource conflict)
- **Stall cycles:** Reduce effective speedup

### Number Conversions
- **2's complement (n bits):** Range = -2^(n-1) to 2^(n-1) - 1
- **1's complement:** Flip all bits
- **2's complement:** Flip all bits + 1
- **IEEE 754 Single:** 1 sign + 8 exponent + 23 mantissa (bias = 127)
- **IEEE 754 Double:** 1 sign + 11 exponent + 52 mantissa (bias = 1023)

## MCQ Traps to Watch For

### Common Examiner Tricks
1. **Off-by-one errors** in array indexing and loop bounds
2. **Pointer vs value** in C: `*p++` vs `(*p)++` vs `*(p++)`
3. **Precedence confusion:** `a & b == c` is `a & (b == c)`, not `(a & b) == c`
4. **Static vs dynamic scoping** giving different outputs for same code
5. **Post-increment in expressions:** `i = i++ + ++i` is undefined behavior in C
6. **NULL in SQL:** Any arithmetic with NULL = NULL, any comparison with NULL = UNKNOWN
7. **Deadlock conditions:** All 4 must hold simultaneously (mutual exclusion, hold & wait, no preemption, circular wait)
8. **Virtual memory:** Page fault does NOT always mean page is not in RAM (could be protection fault)
9. **TCP vs UDP:** TCP is reliable but NOT real-time guaranteed; UDP is not reliable but has less overhead
10. **Normalization:** A relation in BCNF is always in 3NF, but not vice versa

## Exam-Day Checklists

### General Strategy (All CBTs)
1. First pass (0-60 min): Attempt all confident questions, skip doubtful ones
2. Second pass (60-90 min): Return to skipped questions, attempt moderate ones
3. Final pass (90-end): Review marked answers, attempt remaining if confident
4. Never leave a question blank if there's no negative marking
5. With negative marking: Skip if less than 50% confident

### Per-Exam Notes
| Exam | Time per Q | Negative Marking | Strategy |
|------|-----------|-----------------|----------|
| BARC OCES | 1.2 min | -1 per wrong (+3 correct) | Skip uncertain, 33% penalty is harsh |
| BSNL SET | 0.9 min | -0.25 per wrong | Attempt more, penalty is mild |
| HPCL | TBD | TBD | Update when pattern confirmed |
| UPPSC Lecturer | 1.2 min | -1 per wrong (+3 correct) | Same as BARC strategy |
