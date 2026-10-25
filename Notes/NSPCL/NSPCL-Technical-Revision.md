# NSPCL — Sr. Assistant Engineer (IT/ERP) · Last-Minute Revision

**Exam:** Sun 25 Oct 2026 · 10:00–12:00 · 120 Q / 120 min
**Paper:** Subject Knowledge **80** + Aptitude **40** · 1 mark each · **−0.25 wrong** · **qualify SEPARATELY in both**
**Syllabus source:** official NSPCL syllabus screenshot (07:29, 25 Oct 2026) — verbatim topics below

> **Rule for this paper:** no blind guessing. Eliminate ≥1 option → guess. Otherwise skip.

---

## 0 · Syllabus map (what they actually listed)

| # | Technical topic | Weight guess |
|:-:|---|:-:|
| 1 | Programming — **C, Python, OOPS** | High |
| 2 | **Data Structures** — array, stack, queue, LL, tree, BST, heap, graph | High |
| 3 | **Algorithms** — searching, sorting, hashing, complexity, design, traversals, MST, shortest path | High |
| 4 | **OS** — syscalls, processes, threads, IPC, concurrency, deadlock, CPU/IO scheduling, memory, file systems | High |
| 5 | **DBMS** — ER, relational algebra, SQL, constraints, normal forms, file org, indexing, transactions, concurrency | High |
| 6 | **Networks** — OSI/TCP-IP, data link, routing, fragmentation, IP addressing, NAT, transport, application | High |
| 7 | **Web** — HTML, CSS, MVC, HTTP methods | Med |
| 8 | **ERP** architecture & enterprise systems | Med |
| 9 | **Cyber Security** | Med |

---

# PART A — PROGRAMMING

## A1 · C — the numbers they ask

| Type | Size (typical 64-bit) |
|---|---|
| char | 1 |
| short | 2 |
| int | 4 |
| long | 8 |
| float | 4 |
| double | 8 |
| pointer | 8 |

**Storage classes:** `auto` (default, local) · `register` (suggests CPU register) · `static` (lifetime = program, **retains value between calls**) · `extern` (global elsewhere)

**Traps:**
- `sizeof(arr)` vs `strlen(arr)` — sizeof includes `\0` and is compile-time; strlen stops at `\0`
- Array name **decays to pointer**; `a[i]` ≡ `*(a+i)`
- `i++` returns old value, `++i` returns new
- Uninitialised local variable → **garbage** (undefined behaviour); `static`/global → 0
- `static` inside a function: initialised **once**, persists across calls
- No bounds checking in C arrays
- `printf("%d", 10/3)` → 3 (integer division)
- Associativity: assignment `=` is **right-to-left**; most others left-to-right
- `&&` and `||` short-circuit

## A2 · Python

| Mutable | Immutable |
|---|---|
| list `[]` | tuple `()` |
| dict `{}` | str `""` |
| set `{}` | int, float, frozenset |

**Traps:**
- `is` → identity (same object); `==` → value equality
- `range(0,5)` → 0,1,2,3,4 (**stop exclusive**)
- `list[:]` = shallow copy; nested objects still shared → use `copy.deepcopy()`
- **Default mutable argument trap:** `def f(x=[]):` — the list persists across calls
- `//` floor division, `**` power
- GIL → threads don't give true CPU parallelism; use multiprocessing
- `dict` keys must be hashable/immutable

## A3 · OOPS

**Four pillars:** Encapsulation · Abstraction · Inheritance · Polymorphism

| Concept | Rule |
|---|---|
| **Overloading** | Same name, different params — **compile-time / static** |
| **Overriding** | Same signature in subclass — **runtime / dynamic** |
| **Abstract class** | Cannot instantiate; may have concrete methods |
| **Interface** | Contract only (traditionally) |
| **Multiple inheritance** | C++ ✅ · Java ❌ for classes, ✅ for interfaces |
| Virtual functions | C++ `virtual` → vtable → runtime dispatch |

**Constructor/destructor order:** base constructor → derived constructor; destruction reverse.

**SOLID:** Single responsibility · Open-closed · Liskov · Interface segregation · Dependency inversion

---

# PART B — DATA STRUCTURES

## B1 · Complexity table (memorise)

| Structure | Access | Search | Insert | Delete |
|---|:-:|:-:|:-:|:-:|
| Array | **O(1)** | O(n) | O(n) | O(n) |
| Stack | O(n) | O(n) | **O(1)** | **O(1)** |
| Queue | O(n) | O(n) | **O(1)** | **O(1)** |
| Linked list | O(n) | O(n) | **O(1)*** | **O(1)*** |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| BST (skewed) | O(n) | O(n) | O(n) | O(n) |
| Hash table | — | **O(1)** avg / O(n) worst | O(1) | O(1) |
| Heap | O(1) peek | O(n) | O(log n) | O(log n) |

\* at a known position; finding it is O(n)

## B2 · Non-negotiable facts

- **Stack = LIFO**, **Queue = FIFO**
- Trees: `n` nodes → **`n−1` edges**
- Binary tree of height `h` → max **`2^(h+1) − 1`** nodes
- Complete binary tree with `n` nodes → height **`⌊log₂n⌋`**
- **Heap as array (0-indexed):** parent of `i` = `(i−1)/2`; children = `2i+1`, `2i+2`
- **Min-heap:** parent ≤ children. **Max-heap:** parent ≥ children
- **Build-heap = O(n)** (not O(n log n)); each insert O(log n)
- **BST inorder traversal = sorted order** ← asked constantly
- Graph: adjacency **matrix** space O(V²) · adjacency **list** space O(V+E)
- Dense graph → matrix; sparse graph → list

---

# PART C — ALGORITHMS

## C1 · Sorting — the one table that always pays

| Algorithm | Best | Average | Worst | Space | Stable |
|---|:-:|:-:|:-:|:-:|:-:|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Merge** | O(n log n) | O(n log n) | **O(n log n)** | **O(n)** | ✅ |
| **Quick** | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ |
| **Heap** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ |
| Radix | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ |

**Stable = Bubble, Insertion, Merge, Counting, Radix.** *Not* Selection, Quick, Heap.

- **Quick sort worst case** = already sorted array with bad pivot → O(n²)
- **Merge sort** needs O(n) extra space; preferred for linked lists
- **Selection sort** = always O(n²), minimum number of swaps

## C2 · Searching & hashing

- **Linear:** O(n). **Binary:** O(log n) — **requires sorted array**
- Binary search comparisons for `n` elements ≈ **log₂n**
- **Hashing collision handling:** chaining (linked list per bucket) vs open addressing (linear/quadratic probing, double hashing)
- **Load factor** α = n/m. Lower α → fewer collisions
- Hash worst case O(n) when all keys collide

## C3 · Graph algorithms

| Algorithm | Purpose | Complexity | Key fact |
|---|---|:-:|---|
| **BFS** | Traverse / shortest in unweighted | O(V+E) | Uses **queue** |
| **DFS** | Traverse / cycle detect | O(V+E) | Uses **stack** (or recursion) |
| **Kruskal** | MST | O(E log E) | Sort edges + **union-find** |
| **Prim** | MST | O(E log V) | Grow from a vertex |
| **Dijkstra** | Single-source shortest | O(E log V) | ❌ **no negative weights** |
| **Bellman-Ford** | Shortest with negatives | O(VE) | ✅ detects negative cycle |
| **Floyd-Warshall** | All-pairs shortest | O(V³) | DP on intermediate vertices |
| **Topological sort** | Ordering | O(V+E) | **DAG only** |

- MST has exactly **V−1** edges
- BFS/DFS on adjacency list O(V+E); on matrix O(V²)

## C4 · Complexity ladder

`O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)`

**Handy:** n=10⁶ → O(n log n) is fine; O(n²) is not.

---

# PART D — OPERATING SYSTEM

## D1 · Process vs thread

| | Process | Thread |
|---|---|---|
| Memory | Own address space | **Shares** code/data/heap |
| Has own | PCB, address space | **Stack, registers, PC** |
| Switch cost | High | Low |
| Crash | Isolated | Kills whole process |

**PCB contains:** PID, state, PC, registers, memory limits, open files, accounting.

**States:** New → Ready → Running → Waiting → Terminated

**System calls:** `fork()` (create child), `exec()` (replace image), `wait()`, `exit()`, `open/read/write`

## D2 · Scheduling

| Algorithm | Note |
|---|---|
| **FCFS** | Convoy effect; non-preemptive |
| **SJF** | **Optimal avg waiting time**; starvation possible |
| **SRTF** | Preemptive SJF |
| **Round Robin** | Time quantum; fair; more context switches |
| **Priority** | Starvation → solve with **aging** |
| **MLFQ** | Multiple queues, feedback |

**Formulas:** Turnaround = Completion − Arrival · Waiting = Turnaround − Burst

## D3 · Deadlock — 4 necessary conditions

1. **Mutual exclusion**
2. **Hold and wait**
3. **No preemption**
4. **Circular wait**

*All four must hold.* Break any one → no deadlock.

**Handling:** Prevention (break a condition) · **Avoidance = Banker's algorithm** · Detection & recovery · Ignore (ostrich)

## D4 · Memory

- **Paging** → **internal** fragmentation (no external)
- **Segmentation** → **external** fragmentation
- **TLB** = cache for page table entries
- **Page fault** → page not in memory
- **Thrashing** = excessive paging, CPU utilisation collapses
- **Belady's anomaly** = FIFO can give *more* faults with *more* frames
- **Optimal page replacement** = lowest fault rate, not implementable

## D5 · Synchronisation

- **Mutex** = locking mechanism (ownership) · **Semaphore** = signalling (counter)
- **Binary semaphore** ≈ mutex
- **Critical section** needs: mutual exclusion, progress, bounded waiting
- Classic problems: producer-consumer, readers-writers, dining philosophers

---

# PART E — DBMS

## E1 · Normal forms

| NF | Rule |
|---|---|
| **1NF** | Atomic values only |
| **2NF** | 1NF + **no partial dependency** on a composite key |
| **3NF** | 2NF + **no transitive dependency** |
| **BCNF** | Every **determinant is a candidate key** |

**ACID:** Atomicity · Consistency · Isolation · Durability

## E2 · Keys

**Super key** ⊇ **Candidate key** → one becomes **Primary key**; others = **Alternate keys**; referencing = **Foreign key**

## E3 · Relational algebra

| Symbol | Operation |
|:-:|---|
| σ | Select (rows / filter) |
| π | Project (columns) |
| ⋈ | Join |
| ρ | Rename |
| ∪ − × | Union, Difference, Cartesian product |

## E4 · SQL traps

- **WHERE** filters rows **before** grouping · **HAVING** filters **after** GROUP BY
- `COUNT(*)` counts all rows · `COUNT(col)` ignores NULLs
- `NULL` comparisons need `IS NULL`, never `= NULL`
- `DELETE` = DML (rollback-able) · `TRUNCATE` = DDL (faster, resets)
- `UNION` removes duplicates; `UNION ALL` keeps them
- JOIN types: INNER · LEFT · RIGHT · FULL OUTER · CROSS

## E5 · Indexing & transactions

- **B+ tree** — all data in **leaf nodes**, leaves linked → range queries. Standard DB index.
- **Clustered index** = physical order of rows (one per table) · **Non-clustered** = separate structure (many)
- Index speeds **read**, slows **write**
- **Concurrency problems:** dirty read · lost update · non-repeatable read · phantom read
- **Isolation levels:** Read Uncommitted → Read Committed → Repeatable Read → Serializable
- **2PL** (two-phase locking): growing + shrinking phase
- **Serializable** schedule = equivalent to some serial order

---

# PART F — COMPUTER NETWORKS

## F1 · Layers

**OSI (7):** Physical → Data Link → Network → Transport → Session → Presentation → Application
**TCP/IP (4):** Network Access → Internet → Transport → Application
**Mnemonic:** *Please Do Not Throw Sausage Pizza Away*

| Layer | PDU | Devices |
|---|---|---|
| Physical | bit | hub, repeater |
| Data Link | frame | **switch**, bridge |
| Network | packet | **router** |
| Transport | segment | — |

## F2 · Protocol → layer

| Layer | Protocols |
|---|---|
| Application | HTTP, HTTPS, FTP, SMTP, DNS, Telnet, SNMP, POP3, IMAP |
| Transport | **TCP, UDP** |
| Network | **IP, ICMP, ARP**, IGMP |
| Data Link | Ethernet, PPP, HDLC |

## F3 · TCP vs UDP

| TCP | UDP |
|---|---|
| Connection-oriented | Connectionless |
| Reliable, ordered | Unreliable |
| 3-way handshake | No handshake |
| Flow + congestion control | None |
| Slower | Faster — DNS, streaming, VoIP, TFTP |

**Handshake:** SYN → SYN-ACK → ACK

## F4 · Ports (asked a lot)

| Port | Service | Port | Service |
|:-:|---|:-:|---|
| 20/21 | FTP | 80 | **HTTP** |
| 22 | **SSH** | 110 | POP3 |
| 23 | Telnet | 143 | IMAP |
| 25 | **SMTP** | 443 | **HTTPS** |
| 53 | **DNS** | 161 | SNMP |

## F5 · IP addressing

| Class | Range | Default mask |
|---|---|---|
| A | 1–126 | /8 |
| B | 128–191 | /16 |
| C | 192–223 | /24 |
| D | 224–239 | **Multicast** |
| E | 240–255 | Reserved |

**Private:** `10.0.0.0/8` · `172.16.0.0/12` · `192.168.0.0/16`
**Loopback:** `127.0.0.1`
**APIPA:** `169.254.x.x`

**Usable hosts = 2^h − 2** (network + broadcast reserved)
/24 → 256 addresses, **254 usable**

## F6 · Everything else

- **ARP** = IP → MAC · **RARP** = MAC → IP · **DHCP** = dynamic IP assignment · **ICMP** = ping/errors
- **NAT** = private → public IP translation
- **Fragmentation** at Network layer when packet > **MTU**
- **RIP** = distance vector, max **15 hops** · **OSPF** = link state · **BGP** = path vector (inter-AS)
- **CSMA/CD** = wired Ethernet · **CSMA/CA** = wireless
- **CRC** = error **detection** · parity = single-bit detection

---

# PART G — WEB TECHNOLOGIES

## G1 · HTTP methods

| Method | Idempotent | Safe | Use |
|---|:-:|:-:|---|
| GET | ✅ | ✅ | Read |
| POST | ❌ | ❌ | Create |
| PUT | ✅ | ❌ | Replace |
| PATCH | ❌ | ❌ | Partial update |
| DELETE | ✅ | ❌ | Remove |
| HEAD | ✅ | ✅ | Headers only |

**Idempotent = GET, PUT, DELETE, HEAD** (and OPTIONS). **NOT POST, NOT PATCH.**

## G2 · Status codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 301 | Moved Permanently |
| 302 | Found (temp redirect) |
| 304 | Not Modified |
| **400** | Bad Request |
| **401** | **Unauthorized (not authenticated)** |
| **403** | **Forbidden (authenticated, no permission)** |
| 404 | Not Found |
| 405 | Method Not Allowed |
| **500** | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

> 401 = *who are you?* · 403 = *I know you, you can't.*

## G3 · MVC

| Layer | Job |
|---|---|
| **Model** | Data + business rules |
| **View** | Rendering / UI |
| **Controller** | Receives input, coordinates |

Separates presentation from logic. Spring MVC, Django, Rails, Angular all follow it.

**HTML:** semantic tags, forms, `input` types
**CSS:** specificity = **inline > id > class > element** · box model = content + padding + border + margin

---

# PART H — ERP

- **ERP = integrated suite, single shared database**, replacing disconnected departmental systems
- **Core idea: single source of truth**
- **Modules:** Finance (FI) · Controlling (CO) · HR · Materials Management (MM) · Sales & Distribution (SD) · Production Planning (PP) · SCM · CRM
- **Vendors:** SAP · Oracle ERP/Fusion · Microsoft Dynamics · Odoo · Infor
- **Architecture:** 3-tier — Presentation → Application → Database
- **Pros:** integration, no duplication, real-time reporting, standard processes
- **Cons:** high cost, long implementation, rigid, heavy customisation risk
- **Implementation approaches:** big-bang · phased · parallel
- **Master data vs transaction data** — master is stable (vendor, material), transaction is events (invoice, PO)

---

# PART I — CYBER SECURITY

**CIA triad:** Confidentiality · Integrity · Availability

| Type | Keys | Examples |
|---|---|---|
| **Symmetric** | Same key | AES, DES, 3DES, Blowfish |
| **Asymmetric** | Public + private | **RSA**, ECC, DSA |
| **Hash** | One-way | MD5, SHA-1, **SHA-256** |

- **AES** = current standard, 128/192/256-bit
- **DES** = 56-bit, broken
- **Digital signature** = hash + private key → proves authenticity + integrity + non-repudiation
- **SSL/TLS** secures transport (HTTPS)
- **Firewall:** packet filter · stateful · application/proxy
- **IDS** = detects & alerts · **IPS** = detects & **blocks**

**Attack → defence:**

| Attack | Meaning | Defence |
|---|---|---|
| **SQL Injection** | Malicious SQL via input | **Parameterised queries / prepared statements** |
| **XSS** | Injected script runs in browser | Output encoding, CSP |
| **CSRF** | Forged request with user's session | CSRF token, SameSite |
| **Phishing** | Social engineering | Awareness, MFA |
| **MITM** | Intercept traffic | TLS |
| **DoS/DDoS** | Flood resources | Rate limiting, WAF |

**OWASP Top 10** — top 3: Broken Access Control · Cryptographic Failures · Injection

---

# PART J — APTITUDE (40 marks)

## J1 · Formulas that actually get used

| Topic | Formula |
|---|---|
| Simple Interest | `SI = PRT/100` |
| Compound Interest | `A = P(1 + r/n)^(nt)` |
| Profit/Loss | `Profit% = (SP−CP)/CP × 100` |
| Discount | `SP = MP × (100−d)/100` |
| Average | Sum / Count |
| Speed | `D = S × T` |
| Train crossing pole | time = length/speed |
| Alligation | `(Cheaper qty)/(Dearer qty) = (Dearer − Mean)/(Mean − Cheaper)` |
| LCM × HCF | `= product of two numbers` |
| % change | `(New − Old)/Old × 100` |

## J2 · Speed multipliers

| Fraction | % |
|---|---|
| 1/2 | 50 |
| 1/3 | 33.33 |
| 1/4 | 25 |
| 1/5 | 20 |
| 1/6 | 16.67 |
| 1/8 | 12.5 |
| 2/3 | 66.67 |
| 3/4 | 75 |

## J3 · Speed maths

- **Squares 1–30**, cubes 1–15, tables to 20
- `a² − b² = (a+b)(a−b)`
- Multiply by 11: add adjacent digits
- `×5` = `×10 / 2` · `×25` = `×100 / 4`
- Percentage of: `x% of N = N × x/100`

## J4 · Reasoning — quick rules

| Type | Rule |
|---|---|
| **Blood relations** | Draw a tree; never hold it in your head |
| **Direction** | Draw axes; left/right reverses when facing south |
| **Coding-decoding** | Check letter positions A=1…Z=26; try ±1, ±2, reversal |
| **Series** | Check differences, then ratios, then squares/cubes |
| **Ranking** | `Total = Left rank + Right rank − 1` |
| **Classification** | Find the odd property, not the odd word |

**Alphabet positions:** A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K11 L12 M13 N14 O15 P16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26

**Opposite pairs:** A–Z, B–Y, C–X, D–W, E–V, F–U, G–T, H–S, I–R, J–Q, K–P, L–O, M–N

## J5 · English — the fast calls

| Term | Meaning |
|---|---|
| Synonym | Same meaning |
| Antonym | Opposite |
| One-word substitution | Single word for a phrase |
| Idiom | Figurative meaning, not literal |

---

# ⚡ FINAL 30-SECOND SHEET

```
BST inorder        → sorted
Build heap         → O(n)
BST skewed worst   → O(n)
Quick worst        → O(n²), sorted array + bad pivot
Merge space        → O(n)
Stable sorts       → Bubble, Insertion, Merge, Counting, Radix
Unstable           → Quick, Heap, Selection
Dijkstra           → no negative weights
Bellman-Ford       → detects negative cycle, O(VE)
MST edges          → V−1
Deadlock           → 4 conditions, all required
Banker's           → avoidance
Paging             → internal frag
Segmentation       → external frag
Belady's anomaly   → FIFO
3NF                → no transitive dependency
BCNF               → every determinant is candidate key
WHERE vs HAVING    → before vs after GROUP BY
B+ tree            → all data in leaves, linked
401 vs 403         → not authenticated vs no permission
Idempotent         → GET PUT DELETE HEAD
TCP handshake      → SYN, SYN-ACK, ACK
Private IP         → 10/8, 172.16/12, 192.168/16
RIP max hops       → 15
ARP                → IP → MAC
Usable hosts       → 2^h − 2
Symmetric          → AES/DES (one key)
Asymmetric         → RSA (two keys)
SQL injection fix  → parameterised queries
```

---

## Exam-day tactics (from the admit card)

| Rule | |
|---|---|
| No entry after test starts | Reach by 08:30 entry |
| Can't leave until 12:00 | Plan for it |
| **Professional attire** | Shirt + trousers |
| No phone/smartwatch/calculator | No storage — leave at home |
| Sign admit card + attendance sheet | Or marked absent |
| Bilingual paper | **English prevails** on discrepancy |
| **Qualify separately** | Subject 80 **and** Aptitude 40 |

> **Section strategy:** don't sink 40 minutes into the 80-mark technical half and run out of time for aptitude. Both cutoffs are independent — clearing subject knowledge does **not** compensate for a failed aptitude section.

---

*Compiled 25 Oct 2026, 07:38 — from the official NSPCL syllabus (screenshots) + admit card instructions. Exam at 10:00.*
