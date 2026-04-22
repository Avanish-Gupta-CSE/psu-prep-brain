# BARC OCES CSE -- Last-Minute Revision (Read in 70 min)

**Exam: 100 MCQs | 120 min | +3 correct | -1 wrong | Pure CS (no aptitude/GK)**

---

## Section 1: C Programming Traps (~9 questions expected) [15 min]

### Pointer Arithmetic
```c
int a[] = {10, 20, 30, 40};
int *p = a;
```
- `*p++` = `*(p++)` --> returns `*p` (10), THEN increments p. Value: 10, p now points to a[1]
- `(*p)++` --> increments the VALUE at p. If p=&a[0], a[0] becomes 11
- `++*p` = `++(*p)` --> increments value at p first, then returns it
- `*++p` = `*(++p)` --> increments p first, then dereferences. Returns a[1]=20

### sizeof Traps
```c
int a[10];
int *p = a;
char s[] = "hello";
char *q = "hello";
```
- `sizeof(a)` = 40 (10 ints x 4 bytes)
- `sizeof(p)` = 4 or 8 (pointer size, NOT array size)
- `sizeof(s)` = 6 (5 chars + '\0')
- `sizeof(q)` = 4 or 8 (pointer size)
- `sizeof("hello")` = 6 (string literal includes '\0')

### Struct Padding
```c
struct S { char c; int i; char d; };
```
- Size is NOT 1+4+1=6. With padding: 4+4+4 = **12** (int needs 4-byte alignment)
- Rule: each member aligns to its own size, struct pads to largest member's alignment

```c
struct S { char c; char d; int i; };
```
- Reorder: 1+1+2(pad)+4 = **8** (smaller!)

### fork() Output Counting
```c
fork(); fork(); printf("A");
```
- Each fork doubles processes. After 2 forks: 2^2 = 4 processes, so "A" prints **4 times**
- `fork()` returns: 0 to child, child PID to parent, -1 on error

```c
fork(); fork(); fork();
printf("hello\n");
```
- 2^3 = **8** prints

### Macro Gotchas
```c
#define SQ(x) x*x
SQ(2+3)  // expands to 2+3*2+3 = 2+6+3 = 11, NOT 25
```
- Fix: `#define SQ(x) ((x)*(x))` --> ((2+3)*(2+3)) = 25

```c
#define DOUBLE(x) x+x
2 * DOUBLE(3)  // = 2*3+3 = 9, NOT 12
```

### Static vs Dynamic Scoping
```c
int x = 10;
void f() { printf("%d", x); }
void g() { int x = 20; f(); }
int main() { g(); }
```
- **Static scoping** (C, Java): f() sees global x = **10**
- **Dynamic scoping** (some Lisps): f() sees caller g()'s x = **20**

### Precedence Traps
- `a & b == c` is `a & (b == c)` because `==` has higher precedence than `&`
- `*p++` is `*(p++)` because postfix `++` has higher precedence than `*`
- Comma operator: `x = (1, 2, 3)` --> x = **3** (evaluates all, returns last)
- `printf("%d", i++ + ++i)` --> **undefined behavior** in C

### Bitwise Operators
- `x & (x-1)` --> clears the lowest set bit (used to count set bits)
- `x | (x+1)` --> sets the lowest unset bit
- `x ^ x` = 0 (any number XOR itself = 0)
- `x ^ 0` = x (XOR with 0 = identity)
- `~0` = -1 (all bits set in 2's complement)
- Check if power of 2: `x > 0 && (x & (x-1)) == 0`

### String Pitfalls
```c
char *s = "hello";
s[0] = 'H';  // UNDEFINED BEHAVIOR -- string literal is read-only
```
```c
char s[] = "hello";
s[0] = 'H';  // OK -- s is a mutable array copy
```

---

## Section 2: OS -- Synchronization + Memory (~8 questions) [12 min]

### Semaphores
- **wait(S) / P(S) / down(S):** if S > 0, decrement S; else block
- **signal(S) / V(S) / up(S):** increment S; wake up one blocked process
- **Binary semaphore:** S = 0 or 1 (like mutex)
- **Counting semaphore:** S = any non-negative integer

### Classical Problems (Key Constraints)
**Producer-Consumer (Bounded Buffer):**
- 3 semaphores: `mutex=1`, `empty=N`, `full=0`
- Producer: `wait(empty), wait(mutex), produce, signal(mutex), signal(full)`
- Consumer: `wait(full), wait(mutex), consume, signal(mutex), signal(empty)`
- TRAP: Swapping wait(empty) and wait(mutex) in producer causes **deadlock**

**Reader-Writer:**
- Multiple readers can read simultaneously
- Writer needs exclusive access
- `readcount` variable protected by `mutex` semaphore
- First reader locks `wrt`; last reader unlocks `wrt`

**Dining Philosophers:**
- 5 philosophers, 5 forks. Deadlock if all pick left fork simultaneously
- Solutions: pick up both or none, allow only 4 to sit, asymmetric (one picks right first)

### Mutex vs Semaphore vs Monitor
- **Mutex:** binary, only owner can unlock, for mutual exclusion
- **Semaphore:** integer counter, any process can signal, for synchronization + mutual exclusion
- **Monitor:** high-level construct, automatic mutual exclusion, uses condition variables (wait/signal)

### Paging Numericals
- **Logical address (m bits):** page number (m-n bits) + offset (n bits where page size = 2^n)
- **Physical address:** frame number + offset (same offset bits)
- **Page table size** = number of pages x entry size = (2^(m-n)) x entry_size
- **Multilevel:** split page number into multiple levels. 2-level with 10+10+12 bits = 1K entries per table

### TLB + Effective Access Time
- **EAT** = h(TLB_time + Mem_time) + (1-h)(TLB_time + 2*Mem_time)
- With page fault: add page_fault_rate x page_fault_service_time

### Page Replacement Quick Trace
Given reference string and N frames:
- **FIFO:** Replace oldest page in memory. Circular queue approach.
- **LRU:** Replace page not used for longest time in the PAST
- **Optimal:** Replace page not used for longest time in the FUTURE (theoretical best)
- **Belady's anomaly:** MORE frames = MORE faults. Happens in **FIFO**. Does NOT happen in LRU, Optimal (stack algorithms)

### Fragmentation
- **Internal:** Allocated memory > requested (fixed-size partitions, paging -- last page)
- **External:** Total free memory enough but NOT contiguous (variable partitions, segmentation)
- Paging: internal (yes), external (no)
- Segmentation: internal (no), external (yes)

### CPU Scheduling Quick Rules
- **FCFS:** Non-preemptive, convoy effect (short jobs wait behind long)
- **SJF:** Non-preemptive, optimal average WT among non-preemptive
- **SRTF:** Preemptive SJF, optimal average WT overall
- **Round Robin:** Preemptive, time quantum. Large Q = FCFS, small Q = high overhead
- **Priority:** Can be preemptive or non-preemptive. Starvation possible. Fix: aging

### Deadlock
- 4 conditions (ALL must hold): Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait
- **Banker's Algorithm:** Safe state = at least one safe sequence exists
- **RAG (Resource Allocation Graph):** Cycle with single instances = deadlock. Cycle with multiple instances = MAYBE deadlock.

---

## Section 3: Computer Networks (~8 questions) [12 min]

### Subnetting Quick Method
Given IP: 192.168.1.130/26
- /26 means 26 network bits, 6 host bits
- Block size = 2^6 = 64
- Subnets: .0, .64, .128, .192
- 130 falls in 128-191 subnet
- Network: 192.168.1.128, Broadcast: 192.168.1.191
- Usable hosts: .129 to .190 (2^6 - 2 = 62 hosts)

### CRC Calculation
1. Append (divisor length - 1) zeros to data
2. XOR divide data by generator polynomial
3. Remainder = CRC, append to original data
4. Receiver divides received data by same generator. Remainder 0 = no error.

**Example:** Data = 1101, Generator = 1011 (4 bits, so append 3 zeros)
- Divide 1101000 by 1011 using XOR
- Key: XOR same bits = 0, different = 1

### IP Fragmentation
- **MTU** = Maximum Transmission Unit (e.g., 1500 bytes for Ethernet)
- Header = 20 bytes (minimum), so max data per fragment = MTU - 20
- **Offset** = measured in units of 8 bytes
- **MF (More Fragments) flag:** 1 for all fragments except last, 0 for last
- Total data = 4000 bytes, MTU = 1500:
  - Fragment 1: 1480 bytes data, offset=0, MF=1
  - Fragment 2: 1480 bytes data, offset=185 (1480/8), MF=1
  - Fragment 3: 1040 bytes data, offset=370, MF=0

### Routing Protocols
- **Distance Vector (RIP):** Share routing table with neighbors, Bellman-Ford, count-to-infinity problem, max 15 hops
- **Link State (OSPF):** Flood topology to all, Dijkstra locally, faster convergence, no count-to-infinity
- **BGP:** Path vector, inter-AS routing

### Sliding Window Protocols
- **Stop-and-Wait:** Window=1, Efficiency = 1/(1+2a) where a = T_prop/T_trans
- **Go-Back-N:** Sender window = 2^m - 1, Receiver window = 1
- **Selective Repeat:** Sender window = Receiver window = 2^(m-1)
- Rule: Sender window + Receiver window <= 2^m

### TCP Congestion Control
- **Slow Start:** cwnd starts at 1 MSS, doubles each RTT (exponential) until ssthresh
- **Congestion Avoidance:** After ssthresh, cwnd increases by 1 MSS per RTT (linear/additive)
- **On timeout (Tahoe & Reno):** ssthresh = cwnd/2, cwnd = 1 MSS
- **On 3 dup ACKs (Reno only):** ssthresh = cwnd/2, cwnd = ssthresh (fast recovery)
- **Tahoe:** Always resets cwnd to 1 on any loss

### Key Port Numbers
| Port | Service |
|------|---------|
| 20/21 | FTP (data/control) |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS (UDP+TCP) |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |

### OSI vs TCP/IP Quick Map
- Application (7) + Presentation (6) + Session (5) --> Application layer in TCP/IP
- Transport (4) --> Transport (TCP, UDP)
- Network (3) --> Internet (IP, ICMP, ARP)
- Data Link (2) + Physical (1) --> Network Access

---

## Section 4: SQL + DBMS (~5 questions) [10 min]

### SQL Output Traps
```sql
SELECT COUNT(*), COUNT(col) FROM t;
-- COUNT(*) counts ALL rows including NULLs
-- COUNT(col) skips NULL values in col
```

```sql
SELECT * FROM t WHERE col = NULL;    -- Returns NOTHING (wrong!)
SELECT * FROM t WHERE col IS NULL;   -- Correct way
```

```sql
SELECT dept, COUNT(*) FROM emp GROUP BY dept HAVING COUNT(*) > 5;
-- WHERE filters rows BEFORE grouping
-- HAVING filters groups AFTER grouping
```

```sql
SELECT dept, MAX(sal) FROM emp;
-- ERROR: dept not in GROUP BY and not aggregated
```

### JOIN Types
- **INNER JOIN:** Only matching rows from both tables
- **LEFT JOIN:** All rows from left + matching from right (NULL if no match)
- **RIGHT JOIN:** All rows from right + matching from left
- **FULL OUTER JOIN:** All rows from both (NULL where no match)
- **CROSS JOIN:** Cartesian product. m rows x n rows = m*n rows
- **Self JOIN:** Table joined with itself

### Normalization

**Finding Candidate Keys:**
1. Find attribute closure of each attribute/combination
2. If closure = all attributes, it's a superkey
3. Minimal superkey = candidate key
4. Attribute NOT on RHS of any FD MUST be in every candidate key

**Normal Forms:**
- **1NF:** Atomic values (no sets/lists in a cell)
- **2NF:** 1NF + no partial dependency (non-prime depends on part of candidate key)
- **3NF:** 2NF + no transitive dependency (non-prime -> non-prime). For X->A: X is superkey OR A is prime
- **BCNF:** For every FD X->A, X must be a superkey (stricter than 3NF)

**Key fact:** BCNF decomposition is always lossless but may NOT preserve all FDs. 3NF decomposition is lossless AND dependency-preserving.

### Conflict Serializability
1. Build **precedence graph**: for each pair of conflicting operations (same data item, at least one write) from different transactions, draw edge from earlier to later
2. If graph has **no cycle** --> conflict serializable
3. Conflicting operations: R-W, W-R, W-W on same item (R-R is NOT a conflict)

### 2PL (Two-Phase Locking)
- **Growing phase:** acquire locks, cannot release
- **Shrinking phase:** release locks, cannot acquire
- Guarantees conflict serializability
- **Strict 2PL:** hold all exclusive locks until commit/abort (prevents cascading rollback)
- **Rigorous 2PL:** hold ALL locks until commit/abort

### Relational Algebra
- **Selection (sigma):** filter rows
- **Projection (pi):** select columns (removes duplicates)
- **Natural Join:** join on common attributes, remove duplicate columns
- **Division:** "for all" queries (e.g., students who took ALL courses)

---

## Section 5: Compiler Design + TOC (~5 questions) [10 min]

### FIRST and FOLLOW Sets

**FIRST(X) rules:**
1. If X is terminal: FIRST(X) = {X}
2. If X -> epsilon: add epsilon to FIRST(X)
3. If X -> Y1Y2...Yk: add FIRST(Y1) minus epsilon. If epsilon in FIRST(Y1), add FIRST(Y2), etc.

**FOLLOW(X) rules:**
1. FOLLOW(S) always contains $ (end marker)
2. If A -> aBC: add FIRST(C) minus epsilon to FOLLOW(B)
3. If A -> aB or A -> aBC where epsilon in FIRST(C): add FOLLOW(A) to FOLLOW(B)

### Parser Comparison
| Parser | Direction | Power | Key Property |
|--------|-----------|-------|-------------|
| LL(1) | Top-down, left-to-right, leftmost derivation | Weakest | No left recursion, no left factoring issues |
| LR(0) | Bottom-up | Handles left recursion | Shift-reduce, may have conflicts |
| SLR | Bottom-up | More powerful than LR(0) | Uses FOLLOW for reduce |
| CLR (LR(1)) | Bottom-up | Most powerful | Uses lookahead in items |
| LALR | Bottom-up | Between SLR and CLR | Merges CLR states with same core |

**Power:** LL(1) < LR(0) < SLR < LALR < CLR(LR(1))

### Regular Languages (Quick Checks)
**Regular (DFA/NFA/RE can handle):**
- Strings of fixed pattern, even/odd length, starts/ends with specific char
- Divisibility by a constant

**NOT Regular (need PDA or more):**
- a^n b^n (equal a's and b's in order)
- Palindromes
- Anything requiring "counting" or "matching"

**Pumping Lemma (to prove NOT regular):**
1. Assume L is regular with pumping length p
2. Choose a string s in L with |s| >= p
3. For ALL ways to split s = xyz where |xy| <= p, |y| >= 1:
4. Show that xy^i z is NOT in L for some i >= 0
5. Contradiction --> L is not regular

### CFG Ambiguity
- A grammar is **ambiguous** if a string has 2+ different parse trees (or 2+ leftmost derivations)
- Classic example: `E -> E+E | E*E | id` is ambiguous for `id+id*id`
- Fix: introduce precedence levels with separate non-terminals

---

## Section 6: COA + Digital Logic (~4 questions) [8 min]

### Cache Mapping Formulas
- **Direct mapped:** Line = Block mod (Number of lines). 1 comparator. Fast but high conflict misses.
- **Fully associative:** Block can go anywhere. N comparators (expensive). Fewest conflict misses.
- **Set-associative (k-way):** Set = Block mod (Number of sets), then k-way within set.
- **Cache size** = Number of lines x Block size
- **Number of sets** = Number of lines / Associativity

**Tag bits, index bits, offset bits (for direct/set-associative):**
- Offset bits = log2(block size)
- Index bits = log2(number of sets) [direct: number of lines]
- Tag bits = address bits - index bits - offset bits

### Pipelining
- **k stages, n instructions:**
  - Without pipeline: n x k cycles
  - With pipeline: k + (n-1) cycles (ideal)
  - Speedup = nk / (k + n-1). For large n: speedup approaches k
- **Hazards:**
  - **Data (RAW):** Read After Write -- true dependency. Fix: forwarding, stalling
  - **Data (WAR):** Write After Read -- anti-dependency. Fix: register renaming
  - **Data (WAW):** Write After Write -- output dependency. Fix: register renaming
  - **Control:** Branch instruction. Fix: branch prediction, delayed branch
  - **Structural:** Two instructions need same resource. Fix: duplicate hardware

### IEEE 754
| Format | Sign | Exponent | Mantissa | Bias |
|--------|------|----------|----------|------|
| Single (32-bit) | 1 | 8 | 23 | 127 |
| Double (64-bit) | 1 | 11 | 52 | 1023 |

- Value = (-1)^S x 1.M x 2^(E-bias) [normalized]
- Special: E=0,M=0 --> zero. E=all 1s,M=0 --> infinity. E=all 1s,M!=0 --> NaN

### K-Map Quick Rules (4-variable)
- Group sizes: 1, 2, 4, 8, 16 (powers of 2 only)
- Larger groups = simpler terms
- Groups can wrap around edges
- Each 1 must be covered by at least one group
- Don't-care (X) can be included in groups but don't need to be covered

### Flip-Flop Characteristic Equations
| FF | Equation | Toggle Condition |
|----|----------|-----------------|
| SR | Q(next) = S + R'Q, constraint: SR=0 | S=1,R=1 invalid |
| JK | Q(next) = JQ' + K'Q | J=1,K=1 toggles |
| D | Q(next) = D | Always follows D |
| T | Q(next) = T XOR Q | T=1 toggles |

---

## Section 7: Algorithms + DS (~5 questions) [8 min]

### Master Theorem: T(n) = aT(n/b) + f(n)
Let c = log_b(a):
1. **f(n) = O(n^(c-e))** for some e>0: **T(n) = Theta(n^c)**
2. **f(n) = Theta(n^c)**: **T(n) = Theta(n^c log n)**
3. **f(n) = Omega(n^(c+e))** for some e>0 AND af(n/b) <= kf(n): **T(n) = Theta(f(n))**

**Common examples:**
- T(n) = 2T(n/2) + n --> c=1, f(n)=n=Theta(n^1) --> Case 2: **O(n log n)** (merge sort)
- T(n) = 2T(n/2) + 1 --> c=1, f(n)=O(n^0) --> Case 1: **O(n)**
- T(n) = T(n/2) + 1 --> c=0, f(n)=Theta(n^0) --> Case 2: **O(log n)** (binary search)
- T(n) = 2T(n/2) + n^2 --> c=1, f(n)=Omega(n^2) --> Case 3: **O(n^2)**

### Graph Algorithms Application Map
| Problem | Algorithm | Complexity |
|---------|-----------|-----------|
| Shortest path (unweighted) | BFS | O(V+E) |
| Shortest path (non-negative weights) | Dijkstra | O((V+E)log V) |
| Shortest path (negative weights) | Bellman-Ford | O(VE) |
| All-pairs shortest path | Floyd-Warshall | O(V^3) |
| MST | Prim (dense) or Kruskal (sparse) | O(E log V) |
| Topological sort | DFS-based or Kahn's (BFS) | O(V+E) |
| Cycle detection (directed) | DFS (back edge) | O(V+E) |
| Cycle detection (undirected) | DFS or Union-Find | O(V+E) |
| Strongly Connected Components | Kosaraju or Tarjan | O(V+E) |

### Hashing
- **Load factor (alpha)** = n/m (n items, m slots)
- **Chaining:** Expected search = 1 + alpha (unsuccessful), 1 + alpha/2 (successful)
- **Open addressing:** Expected probes = 1/(1-alpha) (unsuccessful), -(1/alpha)ln(1-alpha) (successful)
- **Collision resolution:** Chaining (linked list at each slot), Linear probing (next slot), Quadratic probing (i^2), Double hashing (second hash function)
- **Linear probing problem:** Primary clustering

### Tree Properties (Quick Facts)
- **Full binary tree:** Every node has 0 or 2 children. L = I + 1 (leaves = internal + 1)
- **Complete binary tree:** All levels filled except possibly last (filled left to right). Used for heaps.
- **BST inorder traversal** = sorted order
- **AVL tree:** Balance factor = |height(left) - height(right)| <= 1 for every node
- **Min nodes in AVL of height h:** N(h) = N(h-1) + N(h-2) + 1 (Fibonacci-like)
- **B-Tree of order m:** Each node has at most m children, at least ceil(m/2) children (except root)

---

## Exam Strategy

### BARC Specifics
- **100 MCQs, 120 minutes, +3/-1**
- Time per question: **1.2 min average**
- Negative marking is **harsh** (lose 33% of what you'd gain) -- skip if < 50% confident
- No aptitude/GK -- purely CS, so every topic matters

### 3-Pass Approach
1. **Pass 1 (0-50 min):** Do all questions you're confident about. Target: 50-60 questions. Mark skipped ones.
2. **Pass 2 (50-90 min):** Return to skipped questions. Attempt those where you can eliminate 2+ options.
3. **Pass 3 (90-120 min):** Review marked answers. Only change if you find a clear error. Attempt remaining ONLY if confident.

### When to Guess
- If you can eliminate 2 options: Expected value = (1/2)(+3) + (1/2)(-1) = +1. **Guess.**
- If you can eliminate 1 option: EV = (1/3)(+3) + (2/3)(-1) = +0.33. **Borderline, lean toward guessing.**
- If you can eliminate 0 options: EV = (1/4)(+3) + (3/4)(-1) = 0. **Skip.**

### Mental Checklist Before Submitting
- Did I misread any "NOT" or "FALSE" in the question?
- Did I account for negative marking on uncertain answers?
- Any questions where I changed my answer -- was the change justified?
