# CBT 2 Rapid-Recall Sheet — All 100 CBT 1 Questions

> **How to drill:** Cover the Answer + Trap columns. Read the cue, say the answer AND why aloud, uncover, check. Mark misses with ❌ in the last column. Re-run only ❌ rows at the end of each chunk.
> **Full detail:** `CBT1-QUESTIONS-AND-ANSWERS.md` | **Deep notes (Q1, Q2):** `cbt1-notes.md`

---

## Chunk A — Q1–Q20 (DBMS + OS)

| Q | Cue (discriminating keyword) | Answer | Trap to avoid | ❌ |
|---|---|---|---|---|
| 1 | One change → update MANY records | **Update Anomaly** | Lost Update = concurrent overwrite, not redundancy | |
| 2 | Filter **after aggregation** / grouped results | **HAVING** | WHERE filters rows BEFORE grouping | |
| 3 | Allow blanks BUT prevent duplicates | **UNIQUE** | NOT NULL would block the blanks; UNIQUE allows NULLs | |
| 4 | Failure → recovery restores earlier state | **Atomicity** | Durability = committed data survives crash | |
| 5 | Two databases: both commit or both roll back | **Two-Phase Commit (2PC)** | Raft = leader election/consensus, not atomic commit | |
| 6 | Advantage of partitioning a huge table | **Manageability + query performance** (partition pruning) | | |
| 7 | Uniquely identify + referenced by other tables | **Primary Key** | Unique name ≠ guaranteed unique; PK is FK target | |
| 8 | Slow equality search, 40M rows, few inserts | **Create an Index** | O(N) scan → O(log N) lookup | |
| 9 | Available during partition, stale reads OK | **Eventual Consistency** | AP side of CAP; linearizability = strong (CP) | |
| 10 | Free memory scattered, total is enough | **External Fragmentation** | Internal = waste INSIDE an allocated block | |
| 11 | Inactive pages moved to storage, apps continue | **Virtual Memory** | DMA = device↔memory transfer, unrelated | |
| 12 | FIX for scattered free memory | **Memory Compaction** | Q10 names the problem; Q12 asks the cure | |
| 13 | CPU **time slices** to processes | **Round Robin** | Paging/Segmentation = memory, not scheduling | |
| 14 | One app can't touch another's memory | **Memory Protection** | MMU + base/limit registers | |
| 15 | Threads share address space — main benefit | **Lower context-switch overhead + scalability** | NOT "no synchronization needed" — races still exist! | |
| 16 | Read-heavy shared structure, many threads | **Read-Write Lock** | Semaphores don't distinguish readers from writers | |
| 17 | Prevent priority inversion | **Priority Inheritance** | Low-prio thread temporarily inherits high priority | |
| 18 | SHARED among threads of one process | **Virtual address space** | Stack, PC, registers are PRIVATE per thread | |
| 19 | Two processes waiting on each other | **Deadlock** | Circular wait | |
| 20 | Files, directories, metadata on storage | **File System** | inodes, permissions, timestamps | |

## Chunk B — Q21–Q40 (OS + Networks + DSA)

| Q | Cue | Answer | Trap | ❌ |
|---|---|---|---|---|
| 21 | Share host kernel, isolated processes/filesystems (containers) | **Namespaces** | Not forking, not paging — Linux container isolation | |
| 22 | Password + approval on registered phone | **Multi-Factor Authentication** | SSO = one login many apps, opposite idea | |
| 23 | Works by IP, fails by domain name | **DNS** | The classic elimination question | |
| 24 | Block unauthorized inbound, allow approved | **Firewall** | Switch/hub don't filter by policy | |
| 25 | Auto-assign IP, subnet, gateway, DNS | **DHCP** | DNS resolves names; DHCP hands out configs | |
| 26 | Search THOUSANDS of patterns in a stream | **Aho-Corasick** | Boyer-Moore = single-pattern only | |
| 27 | Parallel algo slowed by boundary-data exchange | **Communication Overhead** | Not cache coherence — data crosses NODES | |
| 28 | BST nearly sorted → O(n) search | **Self-balancing tree (AVL)** | Rotations restore O(log n) | |
| 29 | Dynamic array doubles when full — insert cost | **Amortized O(1)** | Not O(n) — resize cost spreads over n inserts | |
| 30 | Shortest path, NON-NEGATIVE weights | **Dijkstra** | Prim's = MST, not paths | |
| 31 | Overlapping subproblems + optimal solution | **Dynamic Programming** | Divide&Conquer = independent subproblems | |
| 32 | MINIMUM EDGES in unweighted graph | **BFS** | Unweighted → BFS, weighted → Dijkstra | |
| 33 | Minimum-cost spanning tree | **Kruskal** | Sort edges + union-find, O(E log E) | |
| 34 | Independent tasks, near-linear speedup | **High Task Parallelism** | "Embarrassingly parallel" | |
| 35 | IN-MEMORY, read-heavy, strict O(log n), sorted | **AVL Tree** | B+ = disk; Red-Black = taller (2 log n vs 1.44 log n) | |
| 36 | Poly-time, WITHIN KNOWN FACTOR of optimal | **Approximation Algorithm** | Heuristic = NO guarantee; guarantee word = approximation | |
| 37 | Scheduler: pop highest priority + fast insert | **Binary Heap** | Fibonacci heap is theoretical, binary is the standard | |
| 38 | Insert/delete at BOTH front and rear | **Deque** | | |
| 39 | NEGATIVE edges, no negative cycles | **Bellman-Ford** | Dijkstra breaks on negative weights; O(V·E) | |
| 40 | Frequent insert/delete in the MIDDLE | **Linked List** | Array shifts O(n); list re-links O(1) | |

## Chunk C — Q41–Q60 (Compilers + Architecture + Mixed)

| Q | Cue | Answer | Trap | ❌ |
|---|---|---|---|---|
| 41 | Loop recomputes unchanged expression | **Common Subexpression Elimination** | Dead code elim = removes UNUSED code | |
| 42 | Compile to many CPUs, minimal front-end change | **Retargetable compiler, common IR** | Front-end fixed, write new back-end per target | |
| 43 | Later independent instructions run first | **Out-of-Order Execution** | Commits in-order for correctness | |
| 44 | Multiply by power of 2 → shift | **Strength Reduction** | Expensive op → cheaper op | |
| 45 | Matching nested brackets — simplest grammar | **Context-Free Grammar** | Regular can't count nesting | |
| 46 | Program waits on MAIN MEMORY | **Larger Last-Level Cache** | More ALUs/clock don't fix memory-bound | |
| 47 | Multiple parse trees for same expression | **Eliminate grammar ambiguity** | Enforce precedence + associativity | |
| 48 | Left-to-right, no backtracking, early errors | **Deterministic Parsing** | LL(k)/LR(k) | |
| 49 | Branch mispredictions hurt performance | **Dynamic Branch Prediction** | 2-bit history + Branch Target Buffer | |
| 50 | Evaluate design: maintainability, scalability, security… | **Architectural Design Review** | Quality-attribute evaluation (ATAM) | |
| 51 | Requirements well-defined and STABLE | **Waterfall** | Agile is for CHANGING requirements | |
| 52 | Billions of docs, millisecond text retrieval | **TF-IDF + Inverted Index** | PageRank ranks by links, not text relevance | |
| 53 | Cycle check in DIRECTED graph | **DFS** | Back-edge to node in recursion stack = cycle | |
| 54 | Delayed writes + reliable crash recovery | **Journaling** | Write-ahead log for file systems | |
| 55 | More time synchronizing than computing | **Reduce synchronization frequency** | MORE threads makes contention WORSE | |
| 56 | Needs result of IMMEDIATELY preceding instruction | **Data Forwarding (Bypassing)** | RAW hazard; forwarding beats stalling | |
| 57 | DISK-resident index, minimize disk I/O | **B+ Tree** | High fan-out, shallow height; AVL is for RAM (vs Q35!) | |
| 58 | DAG → valid compilation ORDER | **Topological Sort** | u→v means u comes first | |
| 59 | Route between separate IP networks | **Router** | Layer 3; switch = Layer 2 same-network | |
| 60 | Millions of SORTED records, searched often | **Binary Search** | O(log n) on sorted arrays | |

## Chunk D — Q61–Q80 (Mixed)

| Q | Cue | Answer | Trap | ❌ |
|---|---|---|---|---|
| 61 | Dataset issue that hurts ML accuracy | **Missing & inconsistent values** | Normalization/more data/balance all HELP | |
| 62 | LRU cache O(1) lookup + O(1) eviction | **Hash Table + Doubly Linked List** | The canonical combo | |
| 63 | Nested parentheses — machine MODEL | **Pushdown Automaton** | Q45 asks grammar (CFG), Q63 asks machine (PDA) | |
| 64 | Server blocked on disk I/O, many clients | **Asynchronous I/O** | Non-blocking keeps CPU busy | |
| 65 | GUARANTEED O(n log n) + EXTERNAL sorting | **Merge Sort** | Quick = O(n²) worst; heap = poor locality for disk | |
| 66 | Same operation on thousands of data elements | **SIMD** | Single Instruction Multiple Data = vectors | |
| 67 | LEADER ELECTION + log replication | **Raft** | 2PC = atomic commit across DBs (vs Q5!) | |
| 68 | Text editor, edits near CURSOR | **Gap Buffer** | Rope suits whole-document operations | |
| 69 | Keywords/identifiers/literals BEFORE parsing | **Lexical Analysis** | Chars → tokens; parsing comes after | |
| 70 | Slow OLAP reports, daily batch updates | **Controlled denormalization** | Reduce joins; opposite of OLTP advice | |
| 71 | Undo in REVERSE order | **Stack** | LIFO | |
| 72 | Root → Left → Right | **Preorder** | In = L-Root-R; Post = L-R-Root | |
| 73 | Keep running if one app server fails | **Redundant load-balanced servers** | High availability = redundancy | |
| 74 | O(n) → average O(1) lookups, memory OK | **Hash Table** | | |
| 75 | Membership check, false positives OK, space-tight | **Bloom Filter** | Zero false NEGATIVES, some false positives | |
| 76 | Purpose of transaction log | **Recovery and auditing** | Write-ahead logging → durability | |
| 77 | DB object auto-executes on INSERT/UPDATE/DELETE | **Trigger** | View = stored query; cursor = row iterator | |
| 78 | Purpose of semaphore | **Synchronize access to shared resources** | | |
| 79 | FIXED-format headers, NO nesting | **Deterministic Finite Automaton** | No nesting = regular = DFA (vs Q63 nested = PDA) | |
| 80 | Resources as nouns + HTTP methods | **RESTful Design** | RPC = verbs/actions; SOAP = XML envelopes | |

## Chunk E — Q81–Q100 (Mixed)

| Q | Cue | Answer | Trap | ❌ |
|---|---|---|---|---|
| 81 | Complexity growing FASTEST | **O(n²)** | Of the given options, quadratic wins | |
| 82 | NP-Complete, very large instances, practical | **Approximation or heuristic algorithms** | Exhaustive = exponential = impossible | |
| 83 | Network device MONITORING protocol | **SNMP** | ICMP = ping/errors; syslog = logs | |
| 84 | Runs SHORTEST estimated execution time first | **Shortest Job First (SJF)** | | |
| 85 | Handles LEFT-RECURSIVE grammar naturally | **LR Parsing** | LL(1)/recursive descent infinite-loop on left recursion | |
| 86 | Symbol table: fast lookup, ORDER IRRELEVANT | **Hash Table** | "Order irrelevant" kills trees; O(1) beats O(log n) | |
| 87 | Add/remove servers, MINIMAL key movement | **Consistent Hashing** | Ring; only K/n keys move | |
| 88 | High page faults + LOW CPU utilization | **Reduce degree of multiprogramming** | This IS thrashing; fewer processes = more frames each | |
| 89 | VERY SHORT critical section, multicore | **Spinlock** | Busy-wait cheaper than context-switch; mutex sleeps | |
| 90 | Low-priority waits INDEFINITELY | **Starvation** | Deadlock = mutual circular wait; this is one-sided | |
| 91 | Retries must NOT duplicate effects | **Idempotency** | f(f(x)) = f(x) | |
| 92 | SMALL working set, blocks map to SAME set | **Conflict Miss** | Capacity miss = working set too BIG for cache | |
| 93 | Tolerate single LINK failure, no isolation | **Mesh Topology** | Ring/bus/daisy-chain die on one cut | |
| 94 | Used before declaration, syntax VALID | **Semantic Analysis** | Syntax is fine — it's a MEANING/scope error | |
| 95 | Causal ordering, NO synchronized clocks | **Vector Clocks** | Raft=consensus, 2PC=commit, VC=ordering (know all 3!) | |
| 96 | Machine-independent code for optimization | **Intermediate Representation (IR)** | Middle-end works on IR | |
| 97 | Remove UNREACHABLE code | **Dead Code Elimination** | CSE = removes REPEATED computation (vs Q41) | |
| 98 | Compiler ACCEPTS invalid programs | **Fix grammar specification** | Grammar defines validity, not the tokenizer | |
| 99 | Cores must see latest shared cache line | **Cache Coherence Protocol** | MESI/MOESI invalidate stale copies | |
| 100 | Auto add/remove servers with load | **Elastic Scaling** | Serverless = no server mgmt; orchestration = container lifecycle | |

---

## The 12 Killer Discriminations (where CBT 2 will try to trap you)

1. **WHERE vs HAVING** — before grouping vs after aggregation (Q2)
2. **2PC vs Raft vs Vector Clocks** — atomic commit vs leader election/consensus vs causal ordering (Q5, Q67, Q95)
3. **External vs Internal Fragmentation, + Compaction as the fix** (Q10, Q12)
4. **Deadlock vs Starvation vs Thrashing** — circular wait vs indefinite low-prio wait vs page-fault storm (Q19, Q88, Q90)
5. **AVL (RAM, strict) vs Red-Black (looser) vs B+ Tree (DISK)** (Q35, Q57)
6. **Dijkstra (non-negative) vs Bellman-Ford (negative edges) vs BFS (unweighted)** (Q30, Q32, Q39)
7. **CFG (grammar) vs PDA (machine) vs DFA (no nesting) vs Regular** (Q45, Q63, Q79)
8. **CSE (repeated expr) vs Dead Code Elim (unreachable) vs Strength Reduction (cheaper op)** (Q41, Q44, Q97)
9. **Lexical (tokens) vs Syntax (structure) vs Semantic (meaning/scope)** (Q69, Q94)
10. **Conflict miss (same set) vs Capacity miss (set too big) vs Cold miss (first touch)** (Q92)
11. **Approximation (guaranteed factor) vs Heuristic (no guarantee)** (Q36, Q82)
12. **Spinlock (short CS, multicore) vs Mutex (longer CS, sleeps)** (Q89)
