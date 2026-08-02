# IFFCO CBT 1 — Conceptual Revision Notes

> **Purpose:** Deep, by-heart revision notes built from the actual IFFCO CBT 1 question bank (`IFFCO/CBT1-QUESTIONS-AND-ANSWERS.md`). Each question is broken down into:
> 1. Correct answer with reasoning
> 2. Core concept explained with example
> 3. When each wrong option would have been the correct answer
>
> **Use:** Read these notes top-to-bottom for one full concept sweep, then revisit each section right before the exam.

### Q9. Which SQL clause filters grouped results after aggregation?

**Options:**
- [ ] ORDER BY
- [x] **HAVING**
- [ ] WHERE
- [ ] DISTINCT

#### Correct Answer: HAVING

**Why this is correct**

The `HAVING` clause is used to filter groups after `GROUP BY` and after aggregate functions such as:

- `SUM()`
- `COUNT()`
- `AVG()`
- `MIN()`
- `MAX()`

If you want to filter results based on an aggregate condition, use `HAVING`.

#### Example

Suppose we have an `Employees` table:

| Row | EmployeeID | Department | Salary |
|-----|------------|------------|--------|
| 1   | 1          | Sales      | 5000   |
| 2   | 2          | Sales      | 6000   |
| 3   | 3          | HR         | 4000   |
| 4   | 4          | HR         | 3500   |
| 5   | 5          | IT         | 7000   |

Suppose we want departments whose total salary is greater than 9000:

```sql
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department
HAVING SUM(Salary) > 9000;
```

#### What Happens Here

1. Rows are grouped by `Department`.
2. `SUM(Salary)` is calculated for each department.
3. `HAVING` filters those grouped results.

**Result:**

| Row | Department | TotalSalary |
|-----|------------|-------------|
| 1   | Sales      | 11000       |

Because:

- Sales = 5000 + 6000 = 11000
- HR = 4000 + 3500 = 7500
- IT = 7000

Only Sales satisfies `SUM(Salary) > 9000`.

#### Core Concept: WHERE vs HAVING

This is the most important distinction:

| Clause | Purpose | Applied When |
|--------|---------|--------------|
| `WHERE` | Filters individual rows | Before `GROUP BY` and aggregation |
| `HAVING` | Filters groups | After `GROUP BY` and aggregation |

**Example with `WHERE`:**

```sql
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
WHERE Salary > 4000
GROUP BY Department;
```

This first removes rows where `Salary <= 4000`, then groups what remains.

**Example with `HAVING`:**

```sql
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department
HAVING SUM(Salary) > 9000;
```

This groups all rows first, then filters groups by the aggregate result.

#### Why the Other Options Are Incorrect

**1. `ORDER BY`** — Sorts the final result.

```sql
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department
ORDER BY TotalSalary DESC;
```

This does not filter anything; it only sorts the grouped output.

**Would be correct if:** the question asked which clause sorts results or arranges output in ascending or descending order.

**2. `WHERE`** — Filters rows before aggregation, not grouped results after aggregation.

```sql
SELECT Department, COUNT(*) AS EmpCount
FROM Employees
WHERE Salary > 4000
GROUP BY Department;
```

This excludes rows before `GROUP BY`.

**Would be correct if:** the question asked which clause filters rows before grouping or removes records before aggregate functions are applied.

**3. `DISTINCT`** — Removes duplicate rows or duplicate values from the selected output.

```sql
SELECT DISTINCT Department
FROM Employees;
```

This returns each department once. It does not filter grouped aggregate results.

**Would be correct if:** the question asked which keyword removes duplicate values or how to return unique departments.

#### Important Exam Pattern

If the question mentions:

- grouped results
- after aggregation
- filtering results of `SUM()`, `COUNT()`, `AVG()`, `MIN()`, or `MAX()`

the answer is almost always `HAVING`.

If it mentions filtering rows before grouping, the answer is `WHERE`.

#### Quick Comparison Table

| Row | Clause | Purpose | Applied When |
|-----|--------|---------|--------------|
| 1   | `WHERE` | Filters rows | Before `GROUP BY` and aggregation |
| 2   | `HAVING` | Filters groups | After `GROUP BY` and aggregation |
| 3   | `ORDER BY` | Sorts results | After selection/grouping |
| 4   | `DISTINCT` | Removes duplicates | During result selection |

#### Memory Trick

- `WHERE` → Which rows should enter the grouping?
- `HAVING` → Which groups should remain after grouping?

Remember: **WHERE before, HAVING after.**

#### Final Answer: **HAVING**

---

## 🗄️ Section 1: Database Management Systems (DBMS)

### Q1. Changing one employee department requires updates in many records. Which anomaly is present?

**Options:**
- [ ] Phantom Read
- [x] **Update Anomaly**
- [ ] Lost Update
- [ ] Dirty Read

#### Correct Answer: Update Anomaly

**Why this is correct**

An update anomaly happens when the same fact is stored in multiple rows, so changing that fact requires updating many records.

In this question, the department information for one employee-related entity is repeated across several records. If the department changes, you must update it in multiple places. If even one row is missed, the database becomes inconsistent.

#### Core Concept

This usually happens because of data redundancy, often due to poor normalization.

**Example (unnormalized):**

| EmployeeID | EmployeeName | Department | DepartmentManager |
|------------|--------------|------------|-------------------|
| 1          | Alice        | Sales      | John              |
| 2          | Bob          | Sales      | John              |
| 3          | Carol        | Sales      | John              |

If the Sales manager changes from John to Mary, we must update **all** rows with Department = Sales.

If one row is missed:

| EmployeeID | EmployeeName | Department | DepartmentManager |
|------------|--------------|------------|-------------------|
| 1          | Alice        | Sales      | Mary              |
| 2          | Bob          | Sales      | John              |
| 3          | Carol        | Sales      | Mary              |

Now the same department has two different managers recorded — **that is an update anomaly.**

**How normalization fixes it:**

**Employees**
| EmployeeID | EmployeeName | DepartmentID |
|------------|--------------|--------------|
| 1          | Alice        | 10           |
| 2          | Bob          | 10           |
| 3          | Carol        | 10           |

**Departments**
| DepartmentID | DepartmentName | DepartmentManager |
|--------------|----------------|-------------------|
| 10           | Sales          | Mary              |

Now changing the department manager requires updating **only one row.**

#### Why the Other Options Are Incorrect

**1. Phantom Read** — A *transaction concurrency* problem, not a redundancy problem.
- Occurs when: a transaction runs the same query twice, and another transaction inserts/deletes rows between the two reads → second read returns a different set of rows.
- *Example:* T1 reads all Sales employees; T2 inserts a new Sales employee; T1 re-reads and sees an extra row.
- **Would be correct if:** the question said "a transaction reads a set of rows twice and sees new rows added in between" or "repeated query returns a different number of rows because of another concurrent insert."

**2. Lost Update** — Two transactions update the same data concurrently, and one update overwrites the other.
- *Example:*
  - T1 reads salary = 5000
  - T2 reads salary = 5000
  - T1 updates salary to 5500
  - T2 updates salary to 6000
  - T1's update is lost.
- **Would be correct if:** the question involved two users editing the same record at the same time, one update overwriting another, or concurrent transactions causing one change to disappear.

**3. Dirty Read** — One transaction reads data written by another transaction that has not yet been committed.
- *Example:*
  - T1 updates balance from 1000 to 500 but does not commit.
  - T2 reads balance = 500.
  - T1 rolls back.
  - T2 has read invalid data.
- **Would be correct if:** the question said "a transaction reads uncommitted changes made by another transaction" or "data was read before commit and later rolled back."

#### Quick Comparison Table

| Term          | Main Idea                                                           | Type of Problem                  |
|---------------|---------------------------------------------------------------------|----------------------------------|
| Update Anomaly| Same fact stored in many rows → must update multiple places        | Redundancy / poor normalization  |
| Phantom Read  | Re-running a query returns different rows due to insert/delete by another transaction | Concurrency issue |
| Lost Update   | One transaction overwrites another transaction's update            | Concurrency issue                |
| Dirty Read    | A transaction reads uncommitted data from another transaction      | Concurrency issue                |

#### Exam Tip

- If the question talks about **repeated data**, **updating many rows for one logical change**, or **inconsistency due to redundancy** → think **Update Anomaly.**
- If it talks about **simultaneous transactions** → more likely **Dirty Read, Lost Update, or Phantom Read.**

#### Final Answer: **Update Anomaly**

---

## 🔐 Section 2: Security & Networking (CBT 1 Part 1)

### Q2. Login requires password plus approval on a registered mobile device. Which mechanism is used?

**Options:**
- [x] **Multi-Factor Authentication (MFA / 2FA)**
- [ ] CAPTCHA Verification
- [ ] Password Hashing
- [ ] Single Sign-On (SSO)

#### Correct Answer: Multi-Factor Authentication (MFA / 2FA)

**Why this is correct**

This login requires **two independent factors**:

- **Password** → *something you know*
- **Approval/OTP on registered phone** → *something you have*

That is exactly **Multi-Factor Authentication** (most commonly **Two-Factor Authentication**).

#### Core Concept: Authentication Factors (High-Yield)

| Factor Type | Meaning | Examples |
|---|---|---|
| Something you know | Knowledge | Password, PIN, Security Qs |
| Something you have | Possession | OTP app, SMS OTP, push approval, hardware token |
| Something you are | Inherence | Fingerprint, Face ID, Iris |

If the question explicitly combines **password + OTP/push/biometric**, the answer is **MFA/2FA**.

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. CAPTCHA Verification**
- CAPTCHA is for **bot prevention** (distinguish human vs automated script).
- It is not an “authentication factor”; it doesn’t prove identity.
- **Would be correct if:** the question asked how to stop automated login attempts, fake registrations, or credential-stuffing bots at the UI layer.

**2. Password Hashing**
- Hashing (ideally **salted hashing**) is for **secure password storage** on the server.
- It does not mean the user is providing a second factor; it’s still password-only auth.
- **Would be correct if:** the question asked “How should passwords be stored securely?” or “Which technique prevents storing plaintext passwords?”

**3. Single Sign-On (SSO)**
- SSO means **login once** via an Identity Provider (IdP) and access multiple apps (SAML/OIDC).
- SSO can *use* MFA, but SSO itself is not “password + phone approval”.
- **Would be correct if:** the question said “one login for multiple services/apps” or “central corporate login via an IdP”.

#### Exam Trigger

- **Password + OTP/push/biometric** → **MFA / 2FA**
- **Stop bots** → **CAPTCHA**
- **Store passwords securely** → **Hashing (salted)**
- **One login for many apps** → **SSO**

#### Final Answer: **Multi-Factor Authentication (MFA / 2FA)**

---

### Q3. A site works by IP address but not by domain name. Which service should be checked first?

**Options:**
- [ ] FTP
- [ ] DHCP
- [ ] SMTP
- [x] **DNS**

#### Correct Answer: DNS

**Why this is correct**

If a site works using its **IP address**, the network path to the server is fine.
If it fails using the **domain name**, the problem is **name resolution** → **DNS**.

Typical root causes:
- Wrong/Down DNS resolver
- Bad DNS record (A/AAAA/CNAME)
- Local DNS cache/hosts file issues

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. FTP**
- FTP is a **file transfer** protocol/service, unrelated to domain name resolution.
- **Would be correct if:** the issue was “can’t upload/download files using FTP” or “FTP connection failing.”

**2. DHCP**
- DHCP assigns **IP configuration** (IP, gateway, DNS server).
- Here, IP connectivity already works (you can hit the site by IP).
- **Would be correct if:** the machine cannot get an IP / shows APIPA / wrong gateway / wrong DNS server auto-assigned.

**3. SMTP**
- SMTP is for **email sending**, unrelated to website name resolution.
- **Would be correct if:** the issue was “emails not sending” or “mail server connection failing.”

#### Exam Trigger

- **IP works, domain doesn’t** → **DNS**

#### Final Answer: **DNS**

---

## 🗄️ Section 1 (continued): DBMS — Distributed Transactions

### Q4. A transaction updates two databases; if one fails, both must roll back. Which protocol fits?

**Options:**
- [x] **Two-Phase Commit (2PC)**
- [ ] Raft Consensus
- [ ] Lamport Clock
- [ ] Gossip Protocol

#### Correct Answer: Two-Phase Commit (2PC)

**Why this is correct**

This is the classic **distributed transaction atomicity** requirement:
either **both databases commit** or **both roll back**.

**2PC** provides an **atomic commit** across multiple participants (databases) using a coordinator.

#### Core Concept: 2PC in 2 phases

**Phase 1 — Prepare/Vote**
- Coordinator asks all participants: **“Can you commit?”**
- Participants:
  - write a “prepared” record to log
  - lock needed resources
  - reply **YES** (vote-commit) or **NO** (vote-abort)

**Phase 2 — Commit/Abort**
- If **all YES** → coordinator sends **COMMIT** to all
- If **any NO** (or timeout) → coordinator sends **ABORT** to all

#### Important Limit (exam-friendly)

2PC can be **blocking** if the coordinator crashes after participants are prepared (they may wait holding locks).

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. Raft Consensus**
- Raft is for **replicated state machine consensus** (leader election + log replication).
- It’s not an atomic commit protocol across two independent DBs.
- **Would be correct if:** the question asked about keeping replicated logs consistent across nodes, leader election, or fault-tolerant replication.

**2. Lamport Clock**
- Lamport clocks provide **logical timestamps** to order events in a distributed system.
- They don’t commit/rollback transactions.
- **Would be correct if:** the question asked about partial ordering of events, “happened-before”, or ordering messages without synchronized physical clocks.

**3. Gossip Protocol**
- Gossip spreads information **eventually** and is used for membership/anti-entropy.
- It does not guarantee atomic commit across databases.
- **Would be correct if:** the question asked about “eventual propagation,” “epidemic dissemination,” or decentralized membership updates.

#### Exam Trigger

- **“Two DBs, commit all-or-nothing”** → **2PC**

#### Final Answer: **Two-Phase Commit (2PC)**

---

## 🧠 Section 3: Compiler / Code Optimization

### Q5. A loop recomputes an expression whose operands do not change. Which optimization removes this repetition?

**Options:**
- [ ] Loop Unrolling
- [ ] Register Spilling
- [ ] Dead Code Elimination
- [x] **Common Subexpression Elimination**

#### Correct Answer: Common Subexpression Elimination (CSE)

**Why this is correct**

If an expression is computed repeatedly with the **same operands and no side effects**, the compiler can compute it once and reuse the value.

In loops, this often appears as **loop-invariant** computation; the exam typically maps that to **CSE**.

#### Example (intuition)

If `a` and `b` don’t change inside the loop, then `a*b` is the same every time:

```c
for (int i = 0; i < n; i++) {
  x = (a*b) + i;
  y = (a*b) - i;
}
```

Compute `t = a*b` once, reuse inside the loop.

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. Loop Unrolling**
- Unrolling duplicates the loop body to reduce loop-control overhead and improve instruction-level parallelism.
- It does not specifically remove recomputation of an unchanged expression.
- **Would be correct if:** the question asked about reducing branch/jump overhead, increasing throughput, or enabling vectorization by expanding iterations.

**2. Register Spilling**
- Spilling is what happens when there aren’t enough registers: values are temporarily stored to memory (stack).
- It’s generally a **cost**, not the optimization asked here.
- **Would be correct if:** the question asked what the compiler does when register pressure is high or register allocation fails to fit all live variables.

**3. Dead Code Elimination**
- Removes code that **does not affect program output** (unused computations, unreachable statements).
- Here the computation is used; it’s just repeated unnecessarily.
- **Would be correct if:** the expression’s result is never used (e.g., assigned to a variable that is never read), or code is unreachable after `return`.

#### Exam Trigger

- **Repeated same expression** → **CSE**
- **Unused computation/unreachable code** → **DCE**
- **Reduce loop overhead** → **Unrolling**

#### Final Answer: **Common Subexpression Elimination (CSE)**

---

## 🧩 Section 4: Operating Systems — Memory Management

### Q6. Free memory is scattered into small non-contiguous blocks despite enough total memory. What is this?

**Options:**
- [ ] Thrashing
- [ ] Deadlock
- [x] **External Fragmentation**
- [ ] Internal Fragmentation

#### Correct Answer: External Fragmentation

**Why this is correct**

External fragmentation means:
- total free memory is enough, but
- it’s broken into **many small non-contiguous holes**, so a large contiguous allocation fails.

This is common with **variable-sized allocation** (contiguous allocation, segmentation).

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. Thrashing**
- Thrashing = extremely high paging/swapping activity due to too few frames (page fault rate explodes).
- **Would be correct if:** the question said CPU utilization drops while disk I/O spikes because of constant page faults.

**2. Deadlock**
- Deadlock = circular wait for resources; processes get stuck waiting forever.
- **Would be correct if:** the question described “P1 waits for R2, P2 waits for R1” etc.

**3. Internal Fragmentation**
- Internal fragmentation = wasted space **inside** an allocated block (fixed-size allocation).
- Classic example: paging frames of fixed size where the last page is partially used.
- **Would be correct if:** the question mentioned wasted space within fixed partitions/frames/pages.

#### Exam Trigger

- **Enough total memory but not contiguous** → **External fragmentation**
- **Wasted space inside a block/page** → **Internal fragmentation**

#### Final Answer: **External Fragmentation**

---

### Q8. RAM is insufficient, yet applications continue by moving inactive pages to storage. Which mechanism enables this?

**Options:**
- [ ] Memory Fragmentation
- [x] **Virtual Memory**
- [ ] Direct Memory Access
- [ ] Register Allocation

#### Correct Answer: Virtual Memory

**Why this is correct**

Virtual memory allows the system to run processes even when RAM is insufficient by using:
- **paging**
- **disk-backed swap space**
- **page replacement**

Inactive pages are moved to secondary storage; when needed again, a **page fault** brings them back into RAM.

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. Memory Fragmentation**
- Fragmentation describes wasted/fragmented memory layout, not the mechanism of using disk as RAM.
- **Would be correct if:** the question asked about internal/external fragmentation scenarios.

**2. Direct Memory Access (DMA)**
- DMA lets devices transfer data to/from memory without CPU intervention.
- **Would be correct if:** the question was about high-speed I/O transfers, disk/network cards copying buffers directly to RAM.

**3. Register Allocation**
- Compiler topic: mapping variables to CPU registers.
- **Would be correct if:** the question asked about compiler allocation/spilling.

#### Exam Trigger

- **“Move pages to disk / swap / page fault”** → **Virtual Memory**

#### Final Answer: **Virtual Memory**

---

## 🌳 Section 5: Data Structures — BST Performance Fix

### Q7. A BST becomes nearly sorted and search time approaches O(n). Which change best restores efficient search?

**Options:**
- [x] **Use a self-balancing tree such as AVL**
- [ ] Increase application RAM
- [ ] Store duplicate keys in lists
- [ ] Convert the tree into a queue

#### Correct Answer: Use a self-balancing tree such as AVL

**Why this is correct**

A normal BST can become **skewed** (like a linked list) if insertion order is sorted/nearly sorted.
Then height ≈ \(n\), and search becomes **O(n)**.

A self-balancing BST (AVL / Red-Black) maintains height **O(log n)** → search returns to **O(log n)**.

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. Increase application RAM**
- Memory doesn’t fix the BST height problem; complexity remains O(n).
- **Would be correct if:** the issue was out-of-memory errors or caching constraints, not algorithmic degradation.

**2. Store duplicate keys in lists**
- Duplicates handling doesn’t fix skewing for sorted unique inserts.
- **Would be correct if:** the question asked specifically how to store multiple values per key (multimap) or handle duplicates.

**3. Convert the tree into a queue**
- A queue destroys ordered search capability.
- **Would be correct if:** the goal was FIFO processing, not ordered lookup.

#### Exam Trigger

- **BST becomes skewed → O(n)** → **AVL/Red-Black tree**

#### Final Answer: **Use a self-balancing tree such as AVL**

---

## 🔥 Section 2 (continued): Network Security Controls

### Q10. An administrator must block unauthorized inbound connections while allowing approved traffic. Which control fits best?

**Options:**
- [ ] Repeater
- [x] **Firewall**
- [ ] Layer-2 Switch
- [ ] Network Hub

#### Correct Answer: Firewall

**Why this is correct**

A firewall enforces a network security policy by **filtering traffic** (commonly by IP/port/protocol and connection state):
- block unauthorized inbound connections
- allow explicitly approved traffic

#### Why the Other Options Are Incorrect (and when they would be correct)

**1. Repeater**
- Physical layer device: regenerates/boosts signals to extend distance.
- **Would be correct if:** the question was about extending cable length or signal degradation.

**2. Layer-2 Switch**
- Forwards frames by MAC address; reduces collisions, supports VLANs.
- Standard switching is not designed primarily for inbound security policy enforcement like a firewall.
- **Would be correct if:** the question asked about MAC-based forwarding, VLAN segmentation, or connecting devices in a LAN efficiently.

**3. Network Hub**
- Broadcasts to all ports; no filtering; insecure and obsolete.
- **Would be correct if:** the question asked about a simple physical-layer multiport repeater (rare in modern contexts).

#### Exam Trigger

- **Block/allow traffic based on rules** → **Firewall**

#### Final Answer: **Firewall**

---
## 📘 Part 2 (cbt1_011 – cbt1_020): Compiler, DSA & ACID

### Q11. A compiler must target multiple processors with minimal front-end changes. Which design supports this?

**Options:**
- [ ] Independent syntax analyzers
- [ ] Separate lexical analyzers
- [ ] Architecture-specific symbol tables
- [x] **Retargetable compiler using common IR**

#### Correct Answer: Retargetable compiler using common IR

**Why this is correct**

A compiler is naturally split into:
- **Front-End** (lexical → syntax → semantic analysis): machine-independent
- **Back-End** (code generation + optimization): machine-specific

The **Intermediate Representation (IR)** sits between them. To support a new processor, only the back-end needs rewriting; the front-end and IR stay untouched.

#### Core Concept

```
Source Code → Front-End → IR → Back-End → Target Machine Code
   (1 time)              (shared)        (1 per processor)
```

#### Example

GCC/LLVM compile the same C code for x86, ARM, and RISC-V by reusing one front-end + IR and swapping only the target-specific back-end.

#### Why the Other Options Are Incorrect

**1. Independent syntax analyzers** — Syntax analyzers are part of the machine-independent front-end. Duplicating them per processor adds work, not portability.
- **Would be correct if:** the question was about supporting multiple source languages (one parser per language), not multiple targets.

**2. Separate lexical analyzers** — Same idea: lexers are front-end components, not target-specific.
- **Would be correct if:** the question asked how to handle multiple source languages with different token rules.

**3. Architecture-specific symbol tables** — Symbol tables store identifiers/scopes (semantic info), which is machine-independent by nature.
- **Would be correct if:** the question asked where compiler bookkeeping of variables/types is stored.

#### Exam Trigger

- **"Multiple processors / targets, minimal front-end changes"** → **Retargetable compiler + common IR**

#### Final Answer: **Retargetable compiler using common IR**

---

### Q12. A dynamic array doubles capacity when full. What is the amortized insertion complexity?

**Options:**
- [ ] O(log n)
- [x] **O(1)**
- [ ] O(n)
- [ ] O(n log n)

#### Correct Answer: O(1)

**Why this is correct**

Amortized analysis spreads the rare expensive operations (resizes) over all cheap operations. When the array doubles, resizes happen only at sizes 1, 2, 4, 8, 16... Each resize costs O(n), but total resize work over n inserts = 1 + 2 + 4 + ... + n ≈ 2n = O(n). Dividing by n inserts → **O(1) per insert on average**.

#### Example

| Insert # | Capacity | Copy cost |
|----------|----------|-----------|
| 1–1      | 1 → 2    | 1         |
| 2        | 2 → 4    | 2         |
| 3–4      | —        | 0         |
| 5        | 4 → 8    | 4         |
| ...      | ...      | ...       |

Sum of copy costs up to n ≈ 2n → average = constant.

#### Why the Other Options Are Incorrect

**1. O(log n)** — No logarithmic component exists in array growth; doubling is geometric, not binary-search-like.
- **Would be correct if:** the question involved operations that halve search space (binary search, balanced BST).

**2. O(n)** — This is the cost of a **single worst-case insert** (the resize itself), not the average.
- **Would be correct if:** the question asked "worst-case cost of one insertion" or "cost when resizing occurs."

**3. O(n log n)** — Would imply sort-like per-operation work; not relevant to amortized array growth.
- **Would be correct if:** the question involved heapsort/mergesort-style per-insert maintenance.

#### Exam Trigger

- **"Doubles when full" + "amortized"** → **O(1)**
- **Worst single operation (the resize)** → **O(n)**

#### Final Answer: **O(1)**

---

### Q13. A weighted road graph has non-negative edge weights. Which algorithm gives single-source shortest paths?

**Options:**
- [ ] Depth-First Search
- [ ] Breadth-First Search
- [x] **Dijkstra's Algorithm**
- [ ] Prim's Algorithm

#### Correct Answer: Dijkstra's Algorithm

**Why this is correct**

Dijkstra's algorithm greedily picks the unvisited vertex with the smallest known distance and relaxes its edges. It is correct for **non-negative weights** and runs in O((V + E) log V) with a priority queue.

#### Core Concept

- Maintain `dist[]`, start with `dist[source] = 0`.
- Repeatedly extract the minimum-distance vertex and relax outgoing edges.
- When a vertex is extracted, its shortest distance is final (guaranteed only for non-negative weights).

#### Example

Graph: A→B(4), A→C(2), C→B(1), C→D(5), B→D(1). From A:
- Dist: B=4, C=2 → extract C (2) → relax C→B: B=3, C→D: D=7
- Extract B (3) → D = 4 → Final: A→B=3, A→C=2, A→D=4

#### Why the Other Options Are Incorrect

**1. Depth-First Search** — Explores one branch fully before others; finds no shortest paths in weighted graphs.
- **Would be correct if:** the question was about traversal, topological ordering, or cycle detection.

**2. Breadth-First Search** — Gives shortest paths **only for unweighted graphs** (equal edge cost 1).
- **Would be correct if:** the graph was unweighted and minimum edges/levels were asked.

**3. Prim's Algorithm** — Builds a **Minimum Spanning Tree**, not shortest paths. Both use a priority queue (common confusion).
- **Would be correct if:** the question asked for the minimum-cost tree connecting all vertices.

#### Quick Comparison Table

| Algorithm | Purpose | Weight constraint |
|-----------|---------|-------------------|
| Dijkstra  | Single-source shortest path | Non-negative |
| BFS       | Shortest path | Unweighted only |
| Bellman-Ford | Shortest path | Negative allowed, no neg cycles |
| Prim/Kruskal | MST | Any (spanning tree) |

#### Exam Trigger

- **"Non-negative weights, shortest path"** → **Dijkstra**
- **"Negative edges"** → **Bellman-Ford** (Q46)
- **"Spanning tree"** → **Prim/Kruskal** (Q27)

#### Final Answer: **Dijkstra's Algorithm**

---

### Q14. A processor executes independent later instructions before earlier ones finish while preserving correctness. Technique?

**Options:**
- [ ] Instruction Fusion
- [ ] Loop Unrolling
- [ ] Static Scheduling
- [x] **Out-of-Order Execution**

#### Correct Answer: Out-of-Order Execution

**Why this is correct**

Out-of-Order (OoO) execution lets hardware execute instructions as soon as their **operands are ready**, even if earlier instructions are stalled. Correctness is preserved by committing results **in program order** (in-order commit) via the reorder buffer.

#### Core Concept

- Issue instructions dynamically as operands become available (e.g., Tomasulo's algorithm).
- Register renaming removes false dependencies (WAR/WAW).
- Results retire in original order → exceptions and writes appear sequential.

#### Example

```
I1: LOAD R1, [addr]   ← slow (cache miss)
I2: ADD R3, R4, R5    ← independent; can execute now
I3: SUB R6, R1, R2    ← waits for R1
```
I2 executes while I1 stalls; I3 still waits for I1's result.

#### Why the Other Options Are Incorrect

**1. Instruction Fusion** — Merges two instructions into one (e.g., `ADD` + `SHIFT` → fused op); doesn't reorder execution.
- **Would be correct if:** the question asked about combining consecutive instructions to reduce pipeline overhead.

**2. Loop Unrolling** — Duplicates loop bodies at compile time to reduce branch overhead; static transformation.
- **Would be correct if:** the question was about reducing loop-control overhead (see Q5 wrong-option analysis).

**3. Static Scheduling** — Reorders instructions **at compile time** in a fixed order; no runtime decision-making.
- **Would be correct if:** the question emphasized compile-time instruction reordering by the compiler (software pipelining).

#### Exam Trigger

- **"Executes later instructions before earlier ones finish, at runtime"** → **Out-of-Order Execution**

#### Final Answer: **Out-of-Order Execution**

---

### Q15. A database allows blank middle names but must prevent duplicate university email addresses. Which constraint fits?

**Options:**
- [ ] CHECK
- [x] **UNIQUE**
- [ ] NOT NULL
- [ ] DEFAULT

#### Correct Answer: UNIQUE

**Why this is correct**

`UNIQUE` guarantees **no duplicate non-NULL values** while still **allowing NULLs** (typically multiple NULLs). This exactly matches "blank middle names allowed, duplicate emails forbidden."

#### Core Concept

| Constraint | Rejects duplicates? | Allows NULLs? |
|------------|--------------------|---------------|
| UNIQUE     | Yes                | Yes           |
| NOT NULL   | No                 | No            |
| PRIMARY KEY| Yes                | No            |
| CHECK      | Depends on condition | Depends |

#### Example

```sql
CREATE TABLE Students (
  student_id INT PRIMARY KEY,
  middle_name VARCHAR(50),        -- UNIQUE not needed here
  email VARCHAR(100) UNIQUE       -- duplicates rejected, NULLs allowed
);
```
- `middle_name = NULL` → fine, multiple times.
- `email = 'a@uni.edu'` twice → rejected.

#### Why the Other Options Are Incorrect

**1. CHECK** — Validates a boolean condition on values (e.g., `salary > 0`); cannot by itself prevent duplicates.
- **Would be correct if:** the question asked to restrict values to a range/format (e.g., age ≥ 18, positive balance).

**2. NOT NULL** — Rejects all NULLs → would **incorrectly reject blank middle names**.
- **Would be correct if:** the question asked to ensure a column always has a value (e.g., employee ID required).

**3. DEFAULT** — Supplies a fallback value when none is given; does not restrict duplicates.
- **Would be correct if:** the question asked what value is inserted when the user omits a column (e.g., `status = 'active'`).

#### Exam Trigger

- **"Allow blank, but no duplicates"** → **UNIQUE** (not NOT NULL)
- **"Always required"** → **NOT NULL**
- **"Value range/format"** → **CHECK**

#### Final Answer: **UNIQUE**

---

### Q16. Design changes are evaluated for maintainability, scalability, reliability, security and performance. Which activity is this?

**Options:**
- [x] **Architectural Design Review**
- [ ] Database Backup
- [ ] Code Formatting
- [ ] Unit Testing

#### Correct Answer: Architectural Design Review

**Why this is correct**

An Architectural Design Review evaluates a system design against **non-functional requirements / quality attributes**: maintainability, scalability, reliability, security, performance. Formal methods like **ATAM (Architecture Tradeoff Analysis Method)** do exactly this.

#### Core Concept

- **Functional requirements** → what the system does (features).
- **Non-functional (quality) attributes** → how well it does it: performance, security, maintainability, scalability, reliability.
- A design review assesses whether the chosen architecture will meet these attributes **before full implementation**.

#### Example

Before building a bank's new core system, architects review the design: "Does the proposed microservice split scale to 1M users? Is it maintainable? Is failure isolation sufficient?" — that's an architectural design review.

#### Why the Other Options Are Incorrect

**1. Database Backup** — Operational data-protection activity (copying data for recovery).
- **Would be correct if:** the question asked about protecting against data loss/disaster recovery.

**2. Code Formatting** — Cosmetic standardization (indentation, style); no quality-attribute evaluation.
- **Would be correct if:** the question asked about style consistency or linting.

**3. Unit Testing** — Verifies individual functions behave correctly (functional, code-level).
- **Would be correct if:** the question asked about testing smallest components in isolation.

#### Exam Trigger

- **"Maintainability/scalability/reliability/security/performance evaluation"** → **Architectural Design Review**

#### Final Answer: **Architectural Design Review**

---

### Q17. A transaction updates inventory but fails before sales entry. Recovery restores the earlier state. Which ACID property applies?

**Options:**
- [ ] Durability
- [ ] Consistency
- [ ] Isolation
- [x] **Atomicity**

#### Correct Answer: Atomicity

**Why this is correct**

**Atomicity** = all-or-nothing. If a transaction fails partway, the DB rolls back **all** its changes, restoring the pre-transaction state. Here the inventory update must be undone because the transaction did not complete.

#### Core Concept

ACID:
- **Atomicity** — execute completely or not at all (rollback on failure)
- **Consistency** — valid state → valid state (constraints hold)
- **Isolation** — concurrent transactions don't see each other's partial work
- **Durability** — committed changes survive crashes

#### Example

```
BEGIN;
UPDATE inventory SET qty = qty - 10;   ← executes
INSERT INTO sales ...;                 ← FAILS here
-- Recovery: rollback undoes the inventory update
```
Result: inventory unchanged — the transaction is atomic.

#### Why the Other Options Are Incorrect

**1. Durability** — Applies to **committed** transactions surviving crashes. This transaction never committed.
- **Would be correct if:** the question asked "data survives power failure after COMMIT."

**2. Consistency** — Concerned with constraints/valid states, not partial-rollback behavior.
- **Would be correct if:** the question was about constraints being violated (FK, check) by a transaction.

**3. Isolation** — Concerned with concurrent transactions interfering (dirty read, lost update).
- **Would be correct if:** the question described two transactions running simultaneously.

#### Exam Trigger

- **"Fails partway, rolls back to earlier state"** → **Atomicity**
- **"Survives after commit"** → **Durability**
- **"Two transactions at once"** → **Isolation**

#### Final Answer: **Atomicity**

---

### Q18. Variable-size allocations fail due to scattered free memory despite enough total space. What helps?

**Options:**
- [ ] Memory Mapping
- [ ] Demand Paging
- [x] **Memory Compaction**
- [ ] Copy-on-Write

#### Correct Answer: Memory Compaction

**Why this is correct**

**Memory Compaction** moves all allocated blocks toward one end of memory, merging scattered free holes into **one large contiguous region** — the direct cure for external fragmentation (the condition in Q6).

#### Core Concept

- External fragmentation: many small non-adjacent free holes → a large request fails despite enough total free space.
- Compaction: relocate processes to consolidate free space.
- Cost: needs dynamic relocation (base+limit registers) and copying memory.

#### Example

Before: `[P1][hole][P2][hole][P3][hole]` → 3 small holes.
After compaction: `[P1][P2][P3][one large free block]`.

#### Why the Other Options Are Incorrect

**1. Memory Mapping (mmap)** — Maps files/devices into the address space; doesn't fix fragmentation.
- **Would be correct if:** the question asked about sharing files in memory or memory-mapped I/O.

**2. Demand Paging** — Loads pages only when accessed (lazy loading); unrelated to consolidating holes.
- **Would be correct if:** the question asked how pages are brought into RAM only on reference.

**3. Copy-on-Write** — Defers copying shared pages until a write occurs; a fork optimization.
- **Would be correct if:** the question asked how `fork()` shares pages cheaply.

#### Exam Trigger

- **"Scattered free memory, enough total space"** → **Compaction** (Q6 = disease, Q18 = cure)
- **"Wasted space inside allocated block"** → **Internal fragmentation** (paging)

#### Final Answer: **Memory Compaction**

---

### Q19. A problem has overlapping subproblems and needs an optimal solution. Which technique fits best?

**Options:**
- [x] **Dynamic Programming**
- [ ] Greedy Algorithm
- [ ] Divide and Conquer
- [ ] Backtracking

#### Correct Answer: Dynamic Programming

**Why this is correct**

**Dynamic Programming** is defined by two properties:
1. **Optimal substructure** — optimal solution built from optimal solutions of subproblems
2. **Overlapping subproblems** — same subproblem solved repeatedly

DP stores (memoizes) results to avoid recomputation → optimal solution efficiently.

#### Example

Fibonacci: `fib(n) = fib(n-1) + fib(n-2)` — naive recursion recomputes `fib(3)` many times. DP stores results:
`fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, ...` each computed once → O(n) instead of O(2ⁿ).

#### Why the Other Options Are Incorrect

**1. Greedy Algorithm** — Makes locally optimal choices with no reconsideration; works only when local choice is globally optimal (fails for knapsack, works for coin change in standard systems).
- **Would be correct if:** the problem has the greedy-choice property (activity selection, Huffman, Dijkstra, Prim).

**2. Divide and Conquer** — Splits into **independent** subproblems (no overlap) — e.g., merge sort, quick sort.
- **Would be correct if:** subproblems are independent and results are combined (merge sort, quicksort, binary search).

**3. Backtracking** — Exhaustive search with pruning; explores all candidates; exponential worst case; no reuse of subproblem results.
- **Would be correct if:** the question asked for all solutions / constraint satisfaction (N-Queens, Sudoku, subset-sum enumeration).

#### Exam Trigger

- **"Overlapping subproblems"** → **DP**
- **"Independent subproblems"** → **Divide and Conquer**
- **"Locally optimal choice"** → **Greedy**
- **"All possible solutions"** → **Backtracking**

#### Final Answer: **Dynamic Programming**

---

### Q20. A workstation automatically receives IP address, subnet mask, gateway and DNS server. Which service assigns these?

**Options:**
- [x] **DHCP**
- [ ] NAT
- [ ] ARP
- [ ] DNS

#### Correct Answer: DHCP

**Why this is correct**

**DHCP (Dynamic Host Configuration Protocol)** automatically assigns a host its complete IP configuration: IP address, subnet mask, default gateway, and DNS server addresses, when it joins a network.

#### Core Concept — DORA

1. **D**iscover — host broadcasts "I need an IP"
2. **O**ffer — server offers config
3. **R**equest — host requests the offered lease
4. **A**ck — server acknowledges; lease granted

#### Why the Other Options Are Incorrect

**1. NAT** — Translates private ↔ public IP addresses at the router edge.
- **Would be correct if:** the question asked how multiple private devices share one public IP.

**2. ARP** — Resolves **IP → MAC** on a local network.
- **Would be correct if:** the question asked which protocol finds the MAC address for a known IP.

**3. DNS** — Resolves **domain names → IP addresses**.
- **Would be correct if:** the question was about name resolution (see Q3 — IP works, domain fails → DNS).

#### Exam Trigger

- **"Auto-assigns IP+subnet+gateway+DNS"** → **DHCP**
- **"Name → IP"** → **DNS**
- **"IP → MAC"** → **ARP**

#### Final Answer: **DHCP**

---
## 📘 Part 3 (cbt1_021 – cbt1_030): OS Scheduling, Algo & TOC

### Q21. Which scheduling method allocates CPU time slices to processes?

**Options:**
- [ ] Segmentation
- [ ] Paging
- [x] **Round Robin**
- [ ] FIFO Scheduling

#### Correct Answer: Round Robin

**Why this is correct**

**Round Robin (RR)** is a **preemptive, time-sliced** scheduler: every process gets the CPU for one fixed **time quantum** in a circular order. If a process doesn't finish within the quantum, it's preempted and re-queued at the tail.

#### Core Concept

- Ready queue is treated as a **circular queue**.
- Each process runs for at most `quantum` ms, then is preempted.
- Fair: no process starves (bound on waiting time), good response time for interactive systems.

#### Example

Processes P1(5ms), P2(3ms), P3(2ms), quantum = 2ms:
Order: P1(2) → P2(2) → P3(2, done) → P1(2) → P2(1, done) → P1(1, done). Every process gets a fair share of CPU.

#### Why the Other Options Are Incorrect

**1. Segmentation** — Memory-management scheme dividing address space into variable-sized segments.
- **Would be correct if:** the question was about memory partitioning (external fragmentation, Q6).

**2. Paging** — Memory-management scheme with fixed-size pages/frames.
- **Would be correct if:** the question was about memory address translation or fragmentation (Q8, Q18).

**3. FIFO Scheduling** — Non-preemptive; runs each process to completion in arrival order; **no time slices**.
- **Would be correct if:** the question asked for the simplest non-preemptive scheduler by arrival order.

#### Exam Trigger

- **"Time slices / quantum / circular queue"** → **Round Robin**

#### Final Answer: **Round Robin**

---

### Q22. Which OS mechanism prevents one application from accessing another application's memory?

**Options:**
- [x] **Memory Protection**
- [ ] Caching
- [ ] Multithreading
- [ ] Spooling

#### Correct Answer: Memory Protection

**Why this is correct**

**Memory Protection** isolates each process's address space so one application cannot read or write another's memory. Hardware (MMU) enforces it via:
- **base/limit registers** (contiguous allocation)
- **page-table permission bits** (paging)

#### Core Concept

Every address generated by a process is checked against its allowed range:
```
Physical address = Base + Logical address
If address > Base + Limit → "segmentation fault" → access denied
```
Each process has its own page table → it can only map its own pages.

#### Example

Process A's page table maps only its frames. If A tries to access B's frame number, the MMU raises an access violation — A can never touch B's memory.

#### Why the Other Options Are Incorrect

**1. Caching** — Speeds up memory access by storing frequently used data closer to CPU.
- **Would be correct if:** the question asked about performance improvement via copy of data.

**2. Multithreading** — Runs multiple threads within a process for parallelism.
- **Would be correct if:** the question asked about lightweight concurrent execution (Q23).

**3. Spooling** — Buffers slow I/O jobs (e.g., print jobs) to a disk queue to overlap with computing.
- **Would be correct if:** the question asked how print jobs are queued/decoupled.

#### Exam Trigger

- **"One app can't touch another's memory"** → **Memory Protection**

#### Final Answer: **Memory Protection**

---

### Q23. A server uses lightweight units sharing one address space instead of one process per request. Main benefit?

**Options:**
- [x] **Lower context-switch overhead and better scalability**
- [ ] No synchronization required
- [ ] Complete memory isolation
- [ ] Automatic race-condition elimination

#### Correct Answer: Lower context-switch overhead and better scalability

**Why this is correct**

Threads are "lightweight" because they **share the process's address space** (code, data, heap). Switching threads:
- saves/restores only registers (no page-table switch, no TLB flush)
- hence **cheaper than process context switches**

Creating thousands of threads is far cheaper than thousands of processes → better scalability for per-request concurrency.

#### Core Concept

| Item | Process | Thread |
|------|---------|--------|
| Address space | Own | Shared |
| Page table switch on ctx switch | Yes | No |
| Inter-thread communication | IPC (slow) | Shared memory (fast) |
| Context-switch cost | High | Low |

#### Why the Other Options Are Incorrect

**1. No synchronization required** — **FALSE.** Shared address space means races are possible; synchronization is *required*. This is the most commonly picked wrong answer.
- **Would be correct if:** threads had no shared data — but that's not the case here.

**2. Complete memory isolation** — Threads share memory; isolation is a property of processes.
- **Would be correct if:** the question was about processes, not threads.

**3. Automatic race-condition elimination** — Sharing creates races; nothing is automatic.
- **Would be correct if:** the question asked about mutexes/locks providing *manual* protection.

#### Exam Trigger

- **"Lightweight units, shared address space"** → **Multithreading → lower context-switch overhead** — NOT "no sync needed."

#### Final Answer: **Lower context-switch overhead and better scalability**

---

### Q24. What is a key advantage of partitioning a large industrial database table?

**Options:**
- [ ] Removes indexes
- [ ] Eliminates backups
- [ ] Reduces user count
- [x] **Improves manageability and query performance**

#### Correct Answer: Improves manageability and query performance

**Why this is correct**

Partitioning splits a huge table into smaller, manageable **partitions** (by range/list/hash). Benefits:
- **Partition pruning** — queries touch only relevant partitions
- Easier maintenance — backup/archive/purge one partition at a time
- Parallel scans across partitions

#### Core Concept

Example: `Sales` table with 500M rows partitioned by year:
```sql
CREATE TABLE Sales (...) PARTITION BY RANGE (sale_date);
-- partition p2024, p2025, p2026 ...
SELECT * FROM Sales WHERE sale_date = '2026-01-15';
-- optimizer scans only partition p2026 → much faster
```

#### Why the Other Options Are Incorrect

**1. Removes indexes** — False; partitions can still have indexes (local/global).
- **Would be correct if:** it asked about dropping unused indexes for write speed.

**2. Eliminates backups** — False; you still back up (per-partition backups get easier).
- **Would be correct if:** it asked about per-partition backup granularity.

**3. Reduces user count** — Partitioning has nothing to do with users/concurrency.
- **Would be correct if:** it asked about connection pooling/limits.

#### Exam Trigger

- **"Huge table, manageability + speed"** → **Partitioning**

#### Final Answer: **Improves manageability and query performance**

---

### Q25. A device must search thousands of malware signatures in a data stream. Which algorithm fits best?

**Options:**
- [ ] Binary Search
- [ ] Quick Sort
- [x] **Aho-Corasick**
- [ ] Boyer-Moore

#### Correct Answer: Aho-Corasick

**Why this is correct**

**Aho-Corasick** builds a single trie-based **automaton with failure links** and matches **all patterns simultaneously** in **one linear pass** over the text: O(n + m + z) where n = text length, m = pattern lengths, z = matches. Perfect for thousands of signatures in one stream.

#### Core Concept

1. Build a trie of all signatures.
2. Add **failure links**: on mismatch, jump to the longest proper suffix that is also a prefix of some pattern.
3. Scan the stream once, following the automaton — every pattern found along the way is reported.

#### Example

Patterns: {he, she, his, hers}. Text: "ushers". One pass finds "she", "he", "hers" — all in a single scan without re-scanning text.

#### Why the Other Options Are Incorrect

**1. Binary Search** — Needs a sorted structure and exact-key lookup; can't match substrings at every position.
- **Would be correct if:** the question was about exact-key lookup in a sorted array.

**2. Quick Sort** — A sorting algorithm; irrelevant to pattern matching.
- **Would be correct if:** the question was about sorting a list.

**3. Boyer-Moore** — Very fast, but for **a single pattern** only; running it per signature kills performance.
- **Would be correct if:** the question mentioned one long pattern with a good alphabet-skip strategy.

#### Exam Trigger

- **"Thousands of patterns at once, single pass"** → **Aho-Corasick**
- **"One pattern, skip-based"** → **Boyer-Moore**

#### Final Answer: **Aho-Corasick**

---

### Q26. An unweighted graph needs the minimum number of edges between two vertices. Which algorithm fits?

**Options:**
- [ ] Bellman-Ford Algorithm
- [x] **Breadth-First Search**
- [ ] Depth-First Search
- [ ] Prim's Algorithm

#### Correct Answer: Breadth-First Search

**Why this is correct**

**BFS** explores the graph level by level. In an **unweighted graph**, the first time BFS reaches a target vertex, that path uses the **minimum number of edges** (shortest path). It uses a queue and visits vertices in order of increasing distance.

#### Core Concept

```
dist[source] = 0; queue = [source]
while queue not empty:
  v = dequeue
  for each neighbor u of v (unvisited):
    dist[u] = dist[v] + 1; enqueue u
```

#### Example

Graph: A—B, A—C, B—D, C—D, D—E. BFS from A: A(0) → B(1), C(1) → D(2) → E(3). A→E = 3 edges (minimum).

#### Why the Other Options Are Incorrect

**1. Bellman-Ford** — Handles weighted graphs with negative edges; overkill here and needs weights.
- **Would be correct if:** the graph had negative edge weights (Q46).

**2. Depth-First Search** — Finds *a* path but not the shortest; may go deep down a wrong branch.
- **Would be correct if:** the question asked for traversal, cycle detection, or topological order (Q53).

**3. Prim's Algorithm** — Builds an MST; not about paths between two vertices.
- **Would be correct if:** the question asked for minimum spanning tree.

#### Exam Trigger

- **"Unweighted, minimum edges/shortest path"** → **BFS**
- **"Weighted, non-negative"** → **Dijkstra** (Q13)
- **"Weighted, negative"** → **Bellman-Ford** (Q46)

#### Final Answer: **Breadth-First Search**

---

### Q27. Which algorithm constructs a minimum-cost spanning tree in a connected weighted graph?

**Options:**
- [ ] Bellman-Ford Algorithm
- [ ] Dijkstra's Algorithm
- [x] **Kruskal's Algorithm**
- [ ] Topological Sort

#### Correct Answer: Kruskal's Algorithm

**Why this is correct**

**Kruskal's** is a greedy MST algorithm:
1. Sort all edges by weight.
2. Add the smallest edge that does **not create a cycle** (checked with Union-Find).
3. Stop when V−1 edges are added.

Result: minimum-cost spanning tree (same cost as Prim's).

#### Example

Edges: A-B(1), C-D(2), A-C(3), B-D(4), B-C(5), A-D(6).
Kruskal adds: A-B(1), C-D(2), A-C(3) → total 6 (V−1 = 3 edges, no cycle). Done.

#### Why the Other Options Are Incorrect

**1. Bellman-Ford** — Single-source shortest path, not spanning tree.
- **Would be correct if:** shortest paths with negative weights were asked (Q46).

**2. Dijkstra's** — Single-source shortest paths; MST ≠ shortest-path tree.
- **Would be correct if:** single-source shortest path with non-negative weights (Q13).

**3. Topological Sort** — Orders DAG vertices (dependencies), no edge weights involved.
- **Would be correct if:** the question asked for a valid ordering of tasks/modules (Q58).

#### Exam Trigger

- **"Minimum-cost spanning tree"** → **Kruskal's** (edges) or **Prim's** (vertex-based)
- **"Shortest path"** → **Dijkstra/Bellman-Ford** — never confuse MST with SSSP

#### Final Answer: **Kruskal's Algorithm**

---

### Q28. Independent tasks have almost no communication. Which property enables near-linear speedup?

**Options:**
- [ ] Sequential Dependencies
- [ ] Shared Critical Sections
- [ ] Frequent Lock Contention
- [x] **High Task Parallelism**

#### Correct Answer: High Task Parallelism

**Why this is correct**

When tasks are **independent with negligible communication** ("embarrassingly parallel"), each core runs its own work with zero waiting. Total work is parallelized almost perfectly → **speedup ≈ number of cores** (near-linear, limited only by the tiny serial fraction per Amdahl's Law).

#### Core Concept

Speedup (Amdahl's Law): `Speedup = 1 / (s + p/N)` where s = serial fraction, p = parallel fraction, N = cores. If s ≈ 0 and p ≈ 1 → speedup ≈ N.

#### Example

Rendering 1000 independent image frames on 10 cores: each core renders ~100 frames with no communication → almost 10× speedup.

#### Why the Other Options Are Incorrect

**1. Sequential Dependencies** — Task B needs task A's output → serialization → no speedup.
- **Would be correct if:** the question asked what *limits* parallelism.

**2. Shared Critical Sections** — Serialize threads waiting for a lock → limits speedup.
- **Would be correct if:** the question asked about locks/contention (Q35, Q55).

**3. Frequent Lock Contention** — Threads waste time waiting; kills scalability.
- **Would be correct if:** the question asked what reduces performance in concurrent code.

#### Exam Trigger

- **"Independent tasks, no communication"** → **High Task Parallelism** (embarrassingly parallel)

#### Final Answer: **High Task Parallelism**

---

### Q29. A compiler replaces multiplication by a power of two with a shift. Which optimization is this?

**Options:**
- [x] **Strength Reduction**
- [ ] Loop Interchange
- [ ] Tail Recursion Elimination
- [ ] Peephole Optimization

#### Correct Answer: Strength Reduction

**Why this is correct**

**Strength Reduction** replaces an expensive operation with a cheaper equivalent:
- `x * 2^n` → `x << n`
- `x * 2` → `x + x`
- Loop: `i * k` → incrementing a running value

#### Core Concept

```c
// Before
int y = x * 8;
// After (strength reduction)
int y = x << 3;   // same result, cheaper
```
Common in loops: replace `4*i` with a variable that increments by 4 each iteration.

#### Why the Other Options Are Incorrect

**1. Loop Interchange** — Swaps nested loop order (e.g., i-outer/j-inner → j-outer/i-inner) for cache locality.
- **Would be correct if:** the question was about improving spatial/temporal locality of nested loops.

**2. Tail Recursion Elimination** — Converts tail-recursive calls into loops (no stack growth).
- **Would be correct if:** the question was about recursive functions where the call is the last statement.

**3. Peephole Optimization** — Applies local window-based rewrites on generated code (e.g., `mov r1,r1` removed).
- **Would be correct if:** the question was about small, local instruction-level cleanups.

#### Exam Trigger

- **"Multiply by power of 2 → shift"** → **Strength Reduction**

#### Final Answer: **Strength Reduction**

---

### Q30. A language needs matching brackets with arbitrary nesting. Simplest grammar class?

**Options:**
- [ ] Regular Grammar
- [ ] Unrestricted Grammar
- [x] **Context-Free Grammar**
- [ ] Context-Sensitive Grammar

#### Correct Answer: Context-Free Grammar

**Why this is correct**

Arbitrarily nested brackets (Dyck language, e.g., `((()))`) require **counting/stack memory**. Regular grammars (DFA) cannot count. A **Context-Free Grammar** — recognized by a **Pushdown Automaton (PDA) with a stack** — is the *minimum* sufficient class.

#### Core Concept

Grammar for balanced parentheses:
```
S → ( S ) | S S | ε
```
This generates `()`, `(())`, `()()`, ... — each `)` must match a `(` (stack pops).

#### Chomsky Hierarchy (quick)

| Type | Grammar | Machine |
|------|---------|---------|
| 3 | Regular | Finite Automaton |
| 2 | Context-Free | Pushdown Automaton |
| 1 | Context-Sensitive | Linear Bounded Automaton |
| 0 | Unrestricted | Turing Machine |

#### Why the Other Options Are Incorrect

**1. Regular Grammar** — No stack → can't match nested brackets (aⁿbⁿ is not regular).
- **Would be correct if:** the format is fixed with no nesting (Q79 — DFA).

**2. Unrestricted Grammar** — Type-0; far too powerful (Turing-complete) for bracket matching.
- **Would be correct if:** the question asked about any recursively enumerable language.

**3. Context-Sensitive Grammar** — More powerful than needed; nesting needs only a stack, not a linear bounded tape.
- **Would be correct if:** the language had context-sensitive patterns (e.g., aⁿbⁿcⁿ).

#### Exam Trigger

- **"Nested brackets / counting"** → **CFG** (grammar) / **PDA** (machine, Q63)
- **"No nesting, fixed format"** → **Regular Grammar / DFA** (Q79)

#### Final Answer: **Context-Free Grammar**

---
## 📘 Part 4 (cbt1_031 – cbt1_040): Cache, Indexing & Concurrency

### Q31. A program waits mostly for main-memory data rather than computing. Which enhancement helps most?

**Options:**
- [ ] Deeper Pipeline
- [ ] Higher Clock Frequency
- [ ] Additional ALUs
- [x] **Larger Last-Level Cache**

#### Correct Answer: Larger Last-Level Cache

**Why this is correct**

The program is **memory-bound** — it stalls waiting for DRAM data. A **larger last-level cache (LLC)** keeps more of the working set on-chip, cutting DRAM accesses and stall cycles. CPU-speed enhancements (clock, ALUs, pipeline) don't help because the CPU is already idle waiting.

#### Core Concept

- **Compute-bound**: CPU busy → clock speed / ALUs / ILP help.
- **Memory-bound**: CPU stalls on DRAM latency → cache capacity & memory bandwidth help.

#### Example

Workload with 100 MB working set but only 8 MB cache → most accesses hit DRAM. Doubling LLC to 16 MB captures more of the working set → dramatic stall reduction, while raising clock speed changes nothing (CPU already starved).

#### Why the Other Options Are Incorrect

**1. Deeper Pipeline** — Increases ILP; helps compute-bound workloads, not memory stalls.
- **Would be correct if:** the program was ALU/instruction-throughput limited.

**2. Higher Clock Frequency** — Makes a *busy* CPU faster; doesn't help a *waiting* CPU.
- **Would be correct if:** the program was compute-bound with high CPU utilization.

**3. Additional ALUs** — More execution units; irrelevant when data isn't arriving.
- **Would be correct if:** the program had heavy parallel arithmetic and enough memory bandwidth.

#### Exam Trigger

- **"Waits on main memory"** → **Larger LLC / cache**
- **"Computes all the time"** → **Faster clock / more ALUs / deeper pipeline**

#### Final Answer: **Larger Last-Level Cache**

---

### Q32. A banking table must uniquely identify each account and be referenced by transaction tables. What should be used?

**Options:**
- [x] **Primary Key on Account ID**
- [ ] Check constraint on Balance
- [ ] Unique Customer Name
- [ ] Index on Balance

#### Correct Answer: Primary Key on Account ID

**Why this is correct**

A **Primary Key** guarantees:
1. **Uniqueness** — no two rows share the key
2. **NOT NULL** — every account has a valid ID
3. **Reference target** — foreign keys in child tables (transactions) point to it

#### Core Concept

```sql
CREATE TABLE Accounts (
  account_id INT PRIMARY KEY,   -- identity of the row
  balance    NUMERIC CHECK (balance >= 0),
  customer   VARCHAR(100)
);
CREATE TABLE Transactions (
  txn_id    INT PRIMARY KEY,
  account_id INT REFERENCES Accounts(account_id)  -- FK → PK
);
```
A transaction always refers to exactly one account via its PK.

#### Why the Other Options Are Incorrect

**1. Check constraint on Balance** — Domain validation (balance ≥ 0); doesn't identify accounts.
- **Would be correct if:** the question was about restricting value ranges.

**2. Unique Customer Name** — Could be unique but names can change/be NULL; it identifies the customer, not the account, and can't serve as the account's identity.
- **Would be correct if:** the question was about enforcing no duplicate customer names.

**3. Index on Balance** — A performance structure only; no identity/constraint semantics.
- **Would be correct if:** the question was about speeding up range queries on balance.

#### Exam Trigger

- **"Uniquely identify + referenced by other tables"** → **Primary Key**
- **"No duplicates but NULLs allowed"** → **UNIQUE** (Q15)

#### Final Answer: **Primary Key on Account ID**

---

### Q33. Equality searches on a 40-million-row product-code column are slow; inserts are infrequent. What helps most?

**Options:**
- [ ] Increase VARCHAR length
- [ ] Normalize into more tables
- [ ] Store Product Code as BLOB
- [x] **Create an index on Product Code**

#### Correct Answer: Create an index on Product Code

**Why this is correct**

An index (B-tree/hash) turns an **O(N) full scan** into an **O(log N) / O(1) lookup**. Inserts are infrequent, so index-maintenance cost (the usual tradeoff) is negligible → the clear win.

#### Core Concept

Without index: `SELECT ... WHERE product_code = 'ABC'` scans all 40M rows.
With B-tree index: ~log(40M) ≈ 25-30 node visits → microseconds.

#### Why the Other Options Are Incorrect

**1. Increase VARCHAR length** — Wider column = more I/O per row; makes scans slower, not faster.
- **Would be correct if:** product codes were being truncated (data-loss fix).

**2. Normalize into more tables** — Correct normalization reduces redundancy but adds joins; doesn't speed up point lookups.
- **Would be correct if:** the issue was update anomalies/redundancy (Q1).

**3. Store Product Code as BLOB** — BLOBs are opaque, slow to compare, and unindexable for equality search.
- **Would be correct if:** the data was binary content (images/files).

#### Exam Trigger

- **"Slow equality search, huge table, few inserts"** → **Index**
- **"Frequent inserts"** → index maintenance cost matters → consider tradeoff

#### Final Answer: **Create an index on Product Code**

---

### Q34. A database must remain available during partitions, accepting temporarily stale replica reads. Which model fits?

**Options:**
- [ ] Sequential Consistency
- [ ] Linearizability
- [x] **Eventual Consistency**
- [ ] Strict Serializability

#### Correct Answer: Eventual Consistency

**Why this is correct**

The requirement is **availability + partition tolerance (AP)** from the CAP theorem. Accepting **eventually consistent** reads means replicas may be stale during partitions but converge once the partition heals.

#### Core Concept — CAP

| Model | Consistency strength | Tolerates stale reads? |
|-------|---------------------|------------------------|
| Strict serializability | Strongest (real-time order) | No |
| Linearizability | Strong | No |
| Sequential consistency | Medium (some order) | No |
| Eventual consistency | Weak | **Yes** |

#### Example

Dynamo-style key-value store: during a network partition, both sides serve reads from local replicas (availability). A read may return an old value; after the partition heals, updates propagate and replicas converge.

#### Why the Other Options Are Incorrect

**1. Sequential Consistency** — All operations must appear in *some* single order to all processes; no stale divergence.
- **Would be correct if:** weak-but-ordered semantics without real-time constraints were needed.

**2. Linearizability** — Every op takes effect atomically between its invocation and response; no stale reads.
- **Would be correct if:** a single-copy atomic behavior was mandatory (strong consistency).

**3. Strict Serializability** — Linearizability + real-time ordering; strongest model; not AP.
- **Would be correct if:** the system could sacrifice availability during partitions (CP).

#### Exam Trigger

- **"Available during partition, stale reads OK"** → **Eventual Consistency**
- **"Strong consistency required"** → **Linearizability / CP**

#### Final Answer: **Eventual Consistency**

---

### Q35. Many threads contend for a shared structure in read-heavy workload. Which lock improves scalability?

**Options:**
- [ ] Counting Semaphore
- [ ] Binary Semaphore
- [ ] Barrier Synchronization
- [x] **Read-Write Lock**

#### Correct Answer: Read-Write Lock

**Why this is correct**

A **Read-Write (shared-exclusive) lock** allows:
- **many readers simultaneously** (shared mode)
- writers exclusively (exclusive mode)

For a read-heavy workload, all readers proceed in parallel → vastly better scalability than a plain lock that serializes everything.

#### Core Concept

| Mode | Allowed holders | Used by |
|------|-----------------|---------|
| Shared (read) | Many threads | Readers |
| Exclusive (write) | One thread | Writers |

#### Example

A config store read by 100 worker threads, written rarely. With RW lock: 100 readers run concurrently; only writers serialize. With a binary semaphore: all 100 readers queue one-by-one → 100× slower reads.

#### Why the Other Options Are Incorrect

**1. Counting Semaphore** — Tracks availability of N identical resources; doesn't distinguish readers vs writers.
- **Would be correct if:** the question was about limiting N consumers (producer-consumer buffer).

**2. Binary Semaphore** — Mutex-like; serializes *all* accesses including reads.
- **Would be correct if:** the workload was write-heavy or all ops equally exclusive.

**3. Barrier Synchronization** — Waits until all threads reach a point; synchronization *rendezvous*, not access control.
- **Would be correct if:** the question was about "wait until everyone arrives" (e.g., parallel phase end).

#### Exam Trigger

- **"Read-heavy, many threads"** → **Read-Write Lock**

#### Final Answer: **Read-Write Lock**

---

### Q36. A low-priority thread holds a resource needed by a high-priority thread. What prevents priority inversion?

**Options:**
- [ ] Round Robin Scheduling
- [x] **Priority Inheritance**
- [ ] Multilevel Feedback Queue
- [ ] Time Slicing

#### Correct Answer: Priority Inheritance

**Why this is correct**

**Priority Inheritance** temporarily raises the priority of the low-priority lock holder to the level of the highest-priority waiter. This prevents **medium-priority threads from preempting the holder** and causing unbounded blocking of the high-priority thread (priority inversion).

#### Core Concept — The Inversion Scenario

1. **H** (high) needs lock held by **L** (low).
2. **M** (medium) preempts **L** (since L is low priority) → H waits forever behind M.
3. Fix: L **inherits H's priority** while holding the lock → M can't preempt L → L finishes fast → H proceeds.

Famous case: NASA's Mars Pathfinder — fixed with priority inheritance (RTOS).

#### Why the Other Options Are Incorrect

**1. Round Robin** — Fair time-slicing; doesn't address priority relationships at all.
- **Would be correct if:** the question was about fairness of CPU sharing (Q21).

**2. Multilevel Feedback Queue** — Dynamic queue levels; helps aging, not lock-based inversion.
- **Would be correct if:** the question was about adapting quantum by behavior (aging).

**3. Time Slicing** — Fixed quantum preemption; no priority-raising mechanism.
- **Would be correct if:** the question asked how preemption divides CPU.

#### Exam Trigger

- **"Priority inversion prevention"** → **Priority Inheritance**

#### Final Answer: **Priority Inheritance**

---

### Q37. Which resource is shared among threads belonging to the same process?

**Options:**
- [ ] Program counter
- [x] **Virtual address space**
- [ ] Stack
- [ ] Register set

#### Correct Answer: Virtual address space

**Why this is correct**

Threads of one process share **code, data, heap — the entire virtual address space**. Each thread has its **own**: program counter, register set, and stack (its call history).

#### Core Concept

| Resource | Process | Threads in same process |
|----------|---------|------------------------|
| Address space | Own | **Shared** |
| Code/data/heap | Own | **Shared** |
| Stack | Own | Separate per thread |
| Program counter | Own | Separate per thread |
| Registers | Own | Separate per thread |
| Open files | Own | Shared |

#### Example

Two threads in a web server both access the same global request counter (shared heap) but call different functions (separate stacks).

#### Why the Other Options Are Incorrect

**1. Program counter** — Each thread tracks its own next instruction (it's the PC that makes threads concurrent).
- **Would be correct if:** the question asked what's *private* per thread.

**2. Stack** — Each thread has its own stack for local variables and calls.
- **Would be correct if:** the question asked about per-thread local storage.

**3. Register set** — Registers belong to a thread while running; restored on context switch.
- **Would be correct if:** the question asked about thread-switch state.

#### Exam Trigger

- **"Shared among threads"** → **Address space** (private: stack/PC/registers)

#### Final Answer: **Virtual address space**

---

### Q38. Two processes waiting on each other cause what issue?

**Options:**
- [ ] Fragmentation
- [ ] Paging
- [ ] Thrashing
- [x] **Deadlock**

#### Correct Answer: Deadlock

**Why this is correct**

**Deadlock** = each process holds a resource the other needs and waits forever — a **circular wait**. No process can proceed.

#### Core Concept — 4 Necessary Conditions

1. **Mutual exclusion** — resources non-shareable
2. **Hold and wait** — holding one resource while waiting for another
3. **No preemption** — resources can't be force-taken
4. **Circular wait** — P1 waits on P2, P2 waits on P1

Remove any one condition → deadlock prevented.

#### Example

```
P1: holds R1, waits for R2
P2: holds R2, waits for R1
→ both wait forever (circular wait)
```

#### Why the Other Options Are Incorrect

**1. Fragmentation** — Memory layout issue (internal/external); no processes waiting (Q6).
- **Would be correct if:** the question was about scattered/wasted memory.

**2. Paging** — Memory-management scheme moving pages between RAM and disk.
- **Would be correct if:** the question was about address translation/virtual memory.

**3. Thrashing** — Excessive paging due to overcommitted memory (Q88), not process-resource waits.
- **Would be correct if:** the question mentioned high page-fault rate and low CPU utilization.

#### Exam Trigger

- **"Waiting on each other / circular wait"** → **Deadlock**
- **"One-sided indefinite wait"** → **Starvation** (Q90)

#### Final Answer: **Deadlock**

---

### Q39. Which operating system subsystem is primarily responsible for organizing files, directories and metadata on storage devices?

**Options:**
- [ ] Virtual Memory Manager
- [x] **File System**
- [ ] Process Scheduler
- [ ] I/O Scheduler

#### Correct Answer: File System

**Why this is correct**

The **File System** manages the on-disk structure of files and directories, plus **metadata** — inodes, permissions, timestamps, sizes, allocation maps.

#### Core Concept

- **Files**: named units of data
- **Directories**: hierarchical organization (trees)
- **Metadata**: inode blocks holding owner, permissions, size, timestamps, block pointers
- Examples: ext4 (Linux), NTFS (Windows)

#### Why the Other Options Are Incorrect

**1. Virtual Memory Manager** — Manages address spaces, page tables, swapping.
- **Would be correct if:** the question was about RAM/swap/page faults (Q8, Q88).

**2. Process Scheduler** — Chooses which process runs on the CPU.
- **Would be correct if:** the question was about CPU allocation (Q21, Q84).

**3. I/O Scheduler** — Orders disk requests (elevator algorithm) for efficiency.
- **Would be correct if:** the question was about reordering pending disk I/O for throughput.

#### Exam Trigger

- **"Files, directories, metadata"** → **File System**

#### Final Answer: **File System**

---

### Q40. Lightweight environments share the host kernel while isolating processes and file systems. Key OS feature?

**Options:**
- [ ] Process Forking
- [ ] Demand Paging
- [x] **Namespaces**
- [ ] Memory-Mapped Files

#### Correct Answer: Namespaces

**Why this is correct**

**Linux Namespaces** give each container its **own isolated view** of kernel resources — PID, Mount, Network, IPC, UTS, User — while all containers **share the same host kernel**. That is precisely the isolation mechanism behind containers (with cgroups for resource limits).

#### Core Concept

| Namespace | Isolates |
|-----------|----------|
| PID | Process IDs (container sees its own PID 1) |
| Mount | File system mount points |
| Network | Network interfaces, IPs, ports |
| IPC | Inter-process communication |
| UTS | Hostname |
| User | User/group IDs |

#### Example

Two containers on one host: each sees "its own" process tree, filesystem, and network stack — but both run on the single host kernel. No per-container kernel needed.

#### Why the Other Options Are Incorrect

**1. Process Forking** — Duplicates a *single* process (copy-on-write); no isolation domains.
- **Would be correct if:** the question was about creating child processes.

**2. Demand Paging** — Lazy loading of pages into RAM; memory concern.
- **Would be correct if:** the question was about page faults / swap (Q8).

**3. Memory-Mapped Files** — Maps file content into the address space; sharing mechanism, not isolation.
- **Would be correct if:** the question was about file-backed memory access.

#### Exam Trigger

- **"Containers, share kernel, isolated views"** → **Namespaces** (+ cgroups for limits)

#### Final Answer: **Namespaces**

---
## 📘 Part 5 (cbt1_041 – cbt1_050): Data Structures & Parsing

### Q41. A parallel graph algorithm slows due to frequent boundary-data exchange. What limits scalability?

**Options:**
- [x] **Communication Overhead**
- [ ] Branch Prediction
- [ ] Cache Coherence
- [ ] Instruction Pipelining

#### Correct Answer: Communication Overhead

**Why this is correct**

Parallel workers on different nodes/cores must exchange boundary data (vertices/edges on partition borders). The **communication overhead** (network/MPI messages) grows with partition count and eventually dominates compute — limiting scalability (Amdahl's Law / memory-wall for message passing).

#### Core Concept

- Partition graph among P workers.
- Boundary vertices belong to neighbors → results must be exchanged every iteration.
- As P grows, communication/partition ratio grows → speedup saturates or falls.

#### Example

PageRank on 100M nodes split across 64 workers: each iteration requires exchanging scores of ~1M boundary nodes → message traffic becomes the bottleneck, not the local PageRank math.

#### Why the Other Options Are Incorrect

**1. Branch Prediction** — CPU pipeline technique for control hazards; unrelated to distributed scaling.
- **Would be correct if:** the question was about mispredictions stalling a pipeline (Q50).

**2. Cache Coherence** — Ensures shared-memory cache consistency across cores (MESI).
- **Would be correct if:** the question was about shared-memory multicore caches (Q99) — note: message-passing graphs here avoid this by design.

**3. Instruction Pipelining** — Overlaps instruction stages in one core.
- **Would be correct if:** the question was about single-core instruction throughput.

#### Exam Trigger

- **"Boundary-data exchange between nodes/workers"** → **Communication Overhead**

#### Final Answer: **Communication Overhead**

---

### Q42. An in-memory index is searched very frequently but updated only occasionally. It requires sorted records and worst-case O(log n) search, insert and delete. Which structure provides the fastest guaranteed lookup while still maintaining balance?

**Options:**
- [ ] Splay Tree
- [x] **AVL Tree**
- [ ] Red-Black Tree
- [ ] B+ Tree

#### Correct Answer: AVL Tree

**Why this is correct**

- **AVL**: strictly balanced — height ≤ 1.44·log₂n → **fastest guaranteed lookup** among balanced BSTs.
- In-memory → B+ Tree's disk optimization is irrelevant.
- Occasional updates → AVL's extra rotations (its only downside) cost little.

#### Core Concept — Balance-factor Comparison

| Tree | Balance guarantee | Height bound | Best for |
|------|-------------------|--------------|----------|
| AVL | Strict (BF ≤ 1) | ≈ 1.44 log n | Read-heavy, in-memory |
| Red-Black | Loose (root-to-leaf black height) | ≤ 2 log n | Write-heavy |
| B+ Tree | High fan-out | ≤ ~3-4 levels | Disk, huge data |
| Splay | None (amortized) | amortized log n | Locality-based access |

#### Why the Other Options Are Incorrect

**1. Splay Tree** — Self-adjusting; single lookup can be O(n); only amortized O(log n). No strict worst-case guarantee.
- **Would be correct if:** the access pattern had strong locality (recently accessed = accessed again).

**2. Red-Black Tree** — Guarantees O(log n) but with a **looser balance** (up to 2·log n height) → worse worst-case lookup than AVL.
- **Would be correct if:** the workload was write-heavy (fewer rotations).

**3. B+ Tree** — Optimized for **disk** (high fan-out, shallow). In memory it wastes space and complexity.
- **Would be correct if:** the index were disk-resident with millions of records (Q57).

#### Exam Trigger

- **"In-memory, read-heavy, strictest balance"** → **AVL**
- **"Disk-resident, minimize I/O"** → **B+ Tree** (Q57) — the classic AVL-vs-B+ trap

#### Final Answer: **AVL Tree**

---

### Q43. An NP-hard optimization problem must be solved for very large instances. A polynomial-time algorithm returns a solution guaranteed to be within a known factor of the optimal. Which class of algorithms is described?

**Options:**
- [ ] Heuristic Search
- [ ] Randomized Algorithm
- [ ] Exact Algorithm
- [x] **Approximation Algorithm**

#### Correct Answer: Approximation Algorithm

**Why this is correct**

The **defining phrase is "guaranteed within a known factor"** — that provable worst-case bound is the signature of an **Approximation Algorithm** (e.g., 2-approximation for Vertex Cover, 1.5-approximation for metric TSP).

#### Core Concept

- Polynomial time ✓
- Solution quality ≤ c·OPT for known constant c (approximation ratio) ✓
- Works for NP-hard optimization (no exact poly-time solution possible)

#### Example

Vertex Cover: find minimum vertex set touching every edge. Greedy 2-approximation: pick both endpoints of uncovered edges — guaranteed ≤ 2× optimal, polynomial time.

#### Why the Other Options Are Incorrect

**1. Heuristic Search** — Practical but **no guarantee** on solution quality; the exact discriminator tested here.
- **Would be correct if:** the question dropped "guaranteed" — just "works well in practice" → heuristic.

**2. Randomized Algorithm** — Uses randomness in decisions; the guarantee asked here is deterministic (though randomized approximation exists, the *class described* is approximation).
- **Would be correct if:** the question emphasized random choices (e.g., randomized quicksort, Monte Carlo).

**3. Exact Algorithm** — Finds the optimal but **exponential time** for NP-hard problems.
- **Would be correct if:** small instances or optimality at any cost.

#### Exam Trigger

- **"Guaranteed approximation ratio"** → **Approximation Algorithm**
- **"No guarantee, just works well"** → **Heuristic**

#### Final Answer: **Approximation Algorithm**

---

### Q44. A scheduler repeatedly executes the highest-priority process and inserts new tasks efficiently. Best structure?

**Options:**
- [x] **Binary Heap**
- [ ] Fibonacci Heap
- [ ] Balanced BST
- [ ] Binomial Heap

#### Correct Answer: Binary Heap

**Why this is correct**

The **Binary Heap** is the standard array-backed **priority queue**:
- Peek max/min: **O(1)**
- Insert: **O(log n)**
- Extract max/min: **O(log n)**

Simple, compact (array), cache-friendly — ideal for a task scheduler.

#### Core Concept

```
       100          ← max-heap (scheduler picks this)
      /    \
    90     80
   /  \    /
 70   60  75
Insert task: bubble up O(log n). Extract max: swap, sift down O(log n).
```

#### Why the Other Options Are Incorrect

**1. Fibonacci Heap** — Better asymptotic (O(1) insert, O(log n) extract) but huge constant factors and complexity; overkill for schedulers.
- **Would be correct if:** the question emphasized theoretical asymptotic bounds (e.g., Dijkstra with many decrease-key ops).

**2. Balanced BST** — Supports O(log n) ops but with more overhead per node and no O(1) peek advantage; fine but not the standard choice.
- **Would be correct if:** the question also needed predecessor/successor queries.

**3. Binomial Heap** — Good for meld/merge; complex for simple scheduling.
- **Would be correct if:** the question required efficient merging of two heaps.

#### Exam Trigger

- **"Priority queue for a scheduler"** → **Binary Heap** (array-backed, O(1) peek, O(log n) ops)

#### Final Answer: **Binary Heap**

---

### Q45. A data structure must support efficient insertion and deletion at both the front and rear while providing these operations as part of its interface. Which abstract data type is most appropriate?

**Options:**
- [x] **Deque**
- [ ] Stack
- [ ] Priority Queue
- [ ] Queue

#### Correct Answer: Deque

**Why this is correct**

**Deque** (double-ended queue) explicitly supports O(1) insertion/deletion at **both ends**:
- push_front / pop_front
- push_back / pop_back

That's the entire point of its interface.

#### Core Concept

| ADT | Front insert/delete | Rear insert/delete | Priority order |
|-----|--------------------|--------------------|----------------|
| Deque | O(1) | O(1) | No (FIFO-ish both ways) |
| Queue | Dequeue O(1) | Enqueue O(1) | One direction only |
| Stack | Push/Pop only (same end) | — | LIFO |
| Priority Queue | — | — | By priority |

#### Why the Other Options Are Incorrect

**1. Stack** — Only one end (top) for push/pop → LIFO; no rear operations.
- **Would be correct if:** the requirement were LIFO only (Q71 — undo).

**2. Priority Queue** — Serves highest-priority item; insertion by value not by end position.
- **Would be correct if:** tasks must run by priority (Q44).

**3. Queue** — Insert at rear, remove at front only; no front-insertion.
- **Would be correct if:** strict FIFO were required.

#### Exam Trigger

- **"Both front and rear"** → **Deque**

#### Final Answer: **Deque**

---

### Q46. A graph has negative edge weights but no negative cycles. Which single-source shortest path algorithm works?

**Options:**
- [x] **Bellman-Ford Algorithm**
- [ ] Prim's Algorithm
- [ ] A* Search
- [ ] Dijkstra's Algorithm

#### Correct Answer: Bellman-Ford Algorithm

**Why this is correct**

**Bellman-Ford** handles **negative edge weights** correctly:
- Runs V−1 rounds of relaxing all edges
- Correct even with negative edges, **provided no negative cycle**
- O(V·E); also detects negative cycles with a V-th round

#### Core Concept

```
for i in 1..V-1:
  for each edge (u,v,w): relax: if dist[u]+w < dist[v]: dist[v] = dist[u]+w
# extra round: if any edge still relaxes → negative cycle exists
```

#### Example

A→B(5), A→C(4), C→B(−3), B→D(3). Path A→C→B = 4−3 = 1 < 5 → Bellman-Ford finds it; Dijkstra would lock A→B=5 first and miss the improvement.

#### Why the Other Options Are Incorrect

**1. Prim's Algorithm** — MST builder; not a shortest-path algorithm.
- **Would be correct if:** minimum spanning tree were asked (Q27).

**2. A\* Search** — Heuristic search needing admissible heuristics; typically for pathfinding with non-negative costs.
- **Would be correct if:** the question was about heuristic-guided pathfinding with a good heuristic.

**3. Dijkstra's Algorithm** — **Fails with negative weights**: once a vertex is "settled," a later negative edge can give a shorter path that Dijkstra ignores.
- **Would be correct if:** all weights were non-negative (Q13).

#### Exam Trigger

- **"Negative edges, no negative cycle"** → **Bellman-Ford**
- **"Negative cycle detection"** → **Bellman-Ford** (V-th round relaxation)

#### Final Answer: **Bellman-Ford Algorithm**

---

### Q47. A maintenance application frequently inserts and deletes records from the middle of a collection. Which data structure is most suitable?

**Options:**
- [x] **Linked List**
- [ ] Heap
- [ ] Array
- [ ] Stack

#### Correct Answer: Linked List

**Why this is correct**

Once positioned at a node, a **Linked List** inserts/deletes in **O(1)** by re-linking pointers — no shifting of other elements. An array needs **O(n) shifting** for middle operations.

#### Core Concept

```
[A] → [B] → [C] → [D]         insert X after B:
[A] → [B] → [X] → [C] → [D]   just re-point B.next and X.next → O(1)
```
Array middle delete: shift all later elements left → O(n).

#### Why the Other Options Are Incorrect

**1. Heap** — Priority structure; no notion of "middle of collection" — always removes max/min.
- **Would be correct if:** the application needed priority-based removal (Q44).

**2. Array** — O(n) shifting on middle insert/delete; also expensive reallocation.
- **Would be correct if:** the requirement was O(1) random access by index or cache-friendly iteration.

**3. Stack** — Only top-end operations; no middle access.
- **Would be correct if:** LIFO semantics were needed.

#### Exam Trigger

- **"Frequent middle insert/delete"** → **Linked List**
- **"Frequent random access by index"** → **Array**

#### Final Answer: **Linked List**

---

### Q48. A grammar gives multiple parse trees for the same expression. What correction is needed?

**Options:**
- [ ] Expand symbol table
- [ ] Introduce constant propagation
- [x] **Eliminate grammar ambiguity**
- [ ] Increase lexical lookahead

#### Correct Answer: Eliminate grammar ambiguity

**Why this is correct**

Multiple parse trees for one string = **ambiguous grammar**. Fix: rewrite the grammar to impose precedence and associativity so each input has exactly one parse tree.

#### Core Concept

Ambiguous: `E → E + E | E * E | id` — `1 + 2 * 3` parses as `(1+2)*3` OR `1+(2*3)`.

Unambiguous fix (precedence levels):
```
E → E + T | T
T → T * F | F
F → id | ( E )
```
Now `1+2*3` parses uniquely as `1+(2*3)`.

#### Why the Other Options Are Incorrect

**1. Expand symbol table** — Semantic bookkeeping; doesn't affect the *syntax* structure (parse trees).
- **Would be correct if:** the issue were undeclared variables/type errors (Q94).

**2. Introduce constant propagation** — An *optimization*; runs after parsing, can't fix parse-tree multiplicity.
- **Would be correct if:** the question were about compile-time constant evaluation (Q96/Q97 family).

**3. Increase lexical lookahead** — Tokenizer concern; lookahead doesn't remove grammar ambiguity.
- **Would be correct if:** the issue were lexer longest-match conflicts.

#### Exam Trigger

- **"Multiple parse trees"** → **Fix grammar ambiguity** (precedence/associativity)

#### Final Answer: **Eliminate grammar ambiguity**

---

### Q49. A parser must detect syntax errors early while scanning left to right without heavy backtracking. Desired property?

**Options:**
- [ ] Nondeterministic Recognition
- [ ] Left Recursion
- [ ] Ambiguous Grammar
- [x] **Deterministic Parsing**

#### Correct Answer: Deterministic Parsing

**Why this is correct**

**Deterministic parsers** (LL(k)/LR(k)) scan input **left to right in one pass** with no backtracking; the first invalid token is caught immediately → early error detection. This is exactly the required property.

#### Core Concept

- **LL(k)**: top-down, predictive, lookahead k.
- **LR(k)**: bottom-up, shift-reduce, most powerful deterministic class (handles left recursion naturally — Q85).
- Deterministic ⇒ single decision path ⇒ no re-scanning, no backtracking.

#### Why the Other Options Are Incorrect

**1. Nondeterministic Recognition** — May try multiple paths/backtrack → can rescan input, delaying error detection.
- **Would be correct if:** the question accepted exponential backtracking (e.g., naive recursive descent with backtracking).

**2. Left Recursion** — A grammar property that *breaks* top-down deterministic parsers (infinite loop).
- **Would be correct if:** the question asked why LL(1) fails for certain grammars (Q85).

**3. Ambiguous Grammar** — Multiple parses per string; non-deterministic by nature (Q48).
- **Would be correct if:** the question was about fixing grammar ambiguity.

#### Exam Trigger

- **"Left to right, no backtracking, early error detection"** → **Deterministic Parsing**

#### Final Answer: **Deterministic Parsing**

---

### Q50. Incorrect conditional-branch outcomes often reduce processor performance. Which feature addresses this?

**Options:**
- [ ] Memory Interleaving
- [x] **Dynamic Branch Prediction**
- [ ] Cache Prefetching
- [ ] SIMD Execution

#### Correct Answer: Dynamic Branch Prediction

**Why this is correct**

**Dynamic branch prediction** uses hardware history (2-bit saturating counters, branch target buffers) to **predict the direction/target of branches at runtime**, keeping the pipeline full. Wrong predictions stall the pipeline (flush) — exactly the problem described.

#### Core Concept

- 2-bit counter per branch: predict taken/not-taken based on recent outcomes.
- BTB stores branch targets → no wait for target computation.
- Misprediction → pipeline flush + refetch (the performance loss being fixed).

#### Example

A loop branch that takes 99% of the time: predictor learns "taken" → no stall on 99% of iterations; only the exit iteration mispredicts.

#### Why the Other Options Are Incorrect

**1. Memory Interleaving** — Staggers DRAM banks to improve memory bandwidth.
- **Would be correct if:** the issue were DRAM latency/bandwidth, not control flow.

**2. Cache Prefetching** — Brings *data* into cache early (data misses).
- **Would be correct if:** the issue were data cache misses, not branch stalls.

**3. SIMD Execution** — One instruction, many data elements (vectorization).
- **Would be correct if:** the workload were data-parallel arithmetic (Q66).

#### Exam Trigger

- **"Branch mispredictions hurt performance"** → **Dynamic Branch Prediction**

#### Final Answer: **Dynamic Branch Prediction**

---
## 📘 Part 6 (cbt1_051 – cbt1_060): SDLC, IR, B+ Trees & Networks

### Q51. Which SDLC model is best when requirements are well-defined and stable?

**Options:**
- [ ] Agile
- [ ] Spiral
- [ ] DevOps
- [x] **Waterfall**

#### Correct Answer: Waterfall

**Why this is correct**

**Waterfall** is linear-sequential: Requirements → Design → Implementation → Testing → Deployment. It works best when requirements are **fixed, complete, and well-understood** from the start, with no expectation of change.

#### Core Concept

| Model | Best when | Key trait |
|-------|-----------|-----------|
| Waterfall | Stable, well-defined requirements | Linear phases |
| Agile | Changing/evolving requirements | Iterative sprints |
| Spiral | High risk / large projects | Risk-driven iterations |
| DevOps | Continuous delivery | CI/CD culture |

#### Why the Other Options Are Incorrect

**1. Agile** — Built for **changing requirements**: short sprints, feedback loops, adaptive scope. Opposite scenario.
- **Would be correct if:** requirements were expected to evolve or customers give continuous feedback.

**2. Spiral** — Best for **high-risk** projects with heavy prototyping each cycle.
- **Would be correct if:** the project had high risk and uncertainty (e.g., novel defense systems).

**3. DevOps** — A delivery culture (CI/CD, automation, monitoring), not a requirements model.
- **Would be correct if:** the question asked about automated deployment pipelines.

#### Exam Trigger

- **"Requirements stable, well-defined"** → **Waterfall**
- **"Requirements changing"** → **Agile**

#### Final Answer: **Waterfall**

---

### Q52. A search engine processes billions of documents and needs to retrieve the most relevant ones within milliseconds. Which algorithmic approach is most fundamental for efficient text retrieval?

**Options:**
- [ ] A* Search
- [ ] Bellman-Ford Algorithm
- [x] **TF-IDF with Inverted Index**
- [ ] PageRank

#### Correct Answer: TF-IDF with Inverted Index

**Why this is correct**

The **Inverted Index** maps each term → list of documents containing it, allowing instant lookup of candidates. **TF-IDF** then scores each document's relevance (term frequency × inverse document frequency). Together they give millisecond retrieval over billions of docs.

#### Core Concept

```
Index: "solar" → [doc3, doc17, doc42]   (postings list)
        "energy" → [doc3, doc9, doc17]
Query "solar energy" → intersect lists → score each hit with TF-IDF → rank.
```
- **TF**: how often the term appears in the doc (more = more relevant)
- **IDF**: rarer terms weigh more (drops stop-words like "the")

#### Why the Other Options Are Incorrect

**1. A\* Search** — Pathfinding with heuristics; no text-indexing relevance.
- **Would be correct if:** the question were about shortest paths in a map/graph.

**2. Bellman-Ford** — Shortest paths with negative weights; unrelated to retrieval.
- **Would be correct if:** the question were about graph shortest paths (Q46).

**4. PageRank** — Ranks pages by **link structure**, not by text relevance to a query.
- **Would be correct if:** the question asked how to rank webpages by incoming links/importance.

#### Exam Trigger

- **"Billions of docs, millisecond retrieval"** → **TF-IDF + Inverted Index**
- **"Link-based ranking"** → **PageRank**

#### Final Answer: **TF-IDF with Inverted Index**

---

### Q53. A directed dependency graph must be checked for cycles before scheduling. Which traversal fits?

**Options:**
- [x] **Depth-First Search**
- [ ] Kruskal's Algorithm
- [ ] Dijkstra's Algorithm
- [ ] Breadth-First Search

#### Correct Answer: Depth-First Search

**Why this is correct**

**DFS** detects cycles in a directed graph: during DFS, if we reach a vertex **still on the current recursion stack** (back edge), a cycle exists. This is the standard O(V+E) technique.

#### Core Concept

```
DFS(u): mark u visited, push u on stack
  for each neighbor v:
    if v on stack → CYCLE found (back edge)
    else DFS(v)
  pop u from stack
```

#### Example

A→B→C→A: DFS from A hits A again via C while A is on the stack → cycle detected → cannot schedule.

#### Why the Other Options Are Incorrect

**1. Kruskal's** — MST algorithm; cycle checks there use Union-Find for undirected graphs, not dependency scheduling.
- **Would be correct if:** minimum spanning tree were asked (Q27).

**2. Dijkstra's** — Shortest paths; no cycle semantics.
- **Would be correct if:** shortest path with non-negative weights (Q13).

**3. Breadth-First Search** — BFS with a simple visited set **cannot reliably detect directed cycles** (it can't distinguish back vs cross edges without extra state).
- **Would be correct if:** unweighted shortest path were asked (Q26).

#### Exam Trigger

- **"Cycle check in directed graph"** → **DFS** (recursion-stack back edges)

#### Final Answer: **Depth-First Search**

---

### Q54. A file system delays writes but must recover reliably after crashes. Which mechanism supports this?

**Options:**
- [ ] Deadlock Detection
- [ ] Segmentation
- [x] **Journaling**
- [ ] Swapping

#### Correct Answer: Journaling

**Why this is correct**

**Journaling** (write-ahead logging) records each change in a **journal/log on disk before** applying it. After a crash, the file system replays or rolls back journal entries to reach a consistent state quickly — supporting delayed writes safely.

#### Core Concept — Write-Ahead Log

1. Write "intent" to journal (metadata changes).
2. Apply changes to the actual file system.
3. Commit/mark journal entry complete.

On crash recovery: replay committed entries, discard incomplete ones → consistent FS. (ext3/ext4, NTFS use this.)

#### Why the Other Options Are Incorrect

**1. Deadlock Detection** — Finds circular waits between processes; unrelated to storage.
- **Would be correct if:** the question was about process deadlocks (Q38).

**2. Segmentation** — Memory-partitioning scheme.
- **Would be correct if:** the question was about memory organization.

**3. Swapping** — Moving whole processes between RAM and disk.
- **Would be correct if:** the question was about virtual memory/swap space.

#### Exam Trigger

- **"Delayed writes + reliable crash recovery"** → **Journaling** (write-ahead log)

#### Final Answer: **Journaling**

---

### Q55. A parallel program spends more time synchronizing than computing. What improves performance?

**Options:**
- [x] **Reduce Synchronization Frequency**
- [ ] Increase Thread Count
- [ ] Deepen Instruction Pipeline
- [ ] Increase Cache Size

#### Correct Answer: Reduce Synchronization Frequency

**Why this is correct**

When **lock contention dominates runtime**, the fix is to synchronize less often:
- **Coarser locking** / fewer critical sections
- **Batch work** before sharing
- **Lock-free / per-thread data** where possible

Adding more threads would *worsen* contention.

#### Core Concept

- Synchronization serializes threads → total time ≈ sum of critical sections.
- Reduce critical-section count/size → more real parallelism.
- Amdahl's Law: the synchronized fraction directly caps speedup.

#### Example

A counter updated 1M times per thread under one lock → 1M sync ops. Fix: each thread accumulates locally, then merges once → sync overhead drops from 1M to P (thread count) — huge speedup.

#### Why the Other Options Are Incorrect

**1. Increase Thread Count** — More threads → more contention on the same lock → worse.
- **Would be correct if:** cores were idle *without* contention (embarrassingly parallel, Q28).

**2. Deepen Instruction Pipeline** — Single-core ILP; unrelated to cross-thread sync.
- **Would be correct if:** the bottleneck were instruction-level stalls in one core.

**3. Increase Cache Size** — Helps data-locality misses, not lock waiting.
- **Would be correct if:** the issue were cache misses (Q31).

#### Exam Trigger

- **"More time syncing than computing"** → **Reduce sync frequency** (coarser locks/batching)

#### Final Answer: **Reduce Synchronization Frequency**

---

### Q56. An instruction needs the result of the immediately preceding instruction. Which hardware minimizes the stall?

**Options:**
- [x] **Data Forwarding (Bypassing)**
- [ ] Branch Prediction
- [ ] Register Renaming
- [ ] Out-of-Order Execution

#### Correct Answer: Data Forwarding (Bypassing)

**Why this is correct**

**Data Forwarding** routes the result from the pipeline stage that produces it (EX/MEM) **directly to the ALU input** of the dependent instruction — eliminating the need to wait for the register write-back. This resolves **RAW (Read-After-Write) hazards** with zero/minimal stall.

#### Core Concept

```
ADD R1, R2, R3    (result ready at end of EX)
SUB R4, R1, R5    (needs R1 in EX next cycle)
```
Without forwarding: stall 2 cycles until R1 written back.
With forwarding: SUB's ALU input comes straight from ADD's EX output → no stall.

#### Why the Other Options Are Incorrect

**1. Branch Prediction** — Fixes *control* hazards (branches), not data dependencies.
- **Would be correct if:** the problem were branch mispredictions (Q50).

**2. Register Renaming** — Removes *false* dependencies (WAR/WAW) by using extra physical registers; doesn't fix true RAW.
- **Would be correct if:** the hazard were name conflicts on reuse of registers.

**3. Out-of-Order Execution** — Reorders instructions dynamically; a broader mechanism that *includes* forwarding but is not the minimal fix for one RAW pair.
- **Would be correct if:** the question asked for dynamic scheduling machinery (Q14).

#### Exam Trigger

- **"Needs result of immediately preceding instruction"** → **Data Forwarding (bypassing)**
- **"Two back-to-back dependent instructions stall"** → **Forwarding**

#### Final Answer: **Data Forwarding (Bypassing)**

---

### Q57. A disk-resident index must minimize disk I/O for millions of records. Which structure is best?

**Options:**
- [ ] Red-Black Tree
- [ ] AVL Tree
- [x] **B+ Tree**
- [ ] Trie

#### Correct Answer: B+ Tree

**Why this is correct**

The **B+ Tree** has a **high fan-out** (hundreds of keys per disk block). For millions of records, height stays at just **3–4 levels**, so a lookup costs 3–4 disk reads — minimal I/O. All keys live in ordered leaf nodes (linked) → excellent range scans too.

#### Core Concept

- Node size = one disk block (e.g., 8 KB holds ~1000 keys).
- Height ≈ log_fanout(N): 1M records → ~3 levels.
- Leaves: all data keys + sibling links → range scan efficient.

#### Why the Other Options Are Incorrect

**1. Red-Black Tree** — Binary (fan-out 2) → height ~20 for 1M records → ~20 disk reads per lookup. In-memory design.
- **Would be correct if:** the tree were in memory with write-heavy updates (Q42 discussion).

**2. AVL Tree** — Strictly balanced binary → even more I/O on disk; great in memory only.
- **Would be correct if:** the index were in-memory, read-heavy (Q42).

**3. Trie** — Prefix tree for **strings** (dictionary/autocomplete); not a general numeric-key disk index.
- **Would be correct if:** prefix queries over strings were needed (autocomplete, IP routing).

#### Exam Trigger

- **"Disk-resident, minimize I/O"** → **B+ Tree**
- **"In-memory, read-heavy"** → **AVL** (Q42) — know the pair

#### Final Answer: **B+ Tree**

---

### Q58. Module dependencies form a DAG. Which algorithm gives a valid compilation order?

**Options:**
- [ ] Breadth-First Search
- [ ] Kruskal's Algorithm
- [ ] Floyd-Warshall Algorithm
- [x] **Topological Sort**

#### Correct Answer: Topological Sort

**Why this is correct**

**Topological Sort** orders DAG vertices so that for every edge u→v, **u comes before v** — exactly "compile dependencies first" (Kahn's algorithm or DFS-based).

#### Core Concept

```
Dependencies: A→B (B needs A), A→C, B→D, C→D
Order: A, B, C, D   (A first, D last)
```
Every dependency appears before its dependents → valid build order.

#### Why the Other Options Are Incorrect

**1. Breadth-First Search** — Traverses by level, but produces no dependency-guaranteed ordering.
- **Would be correct if:** unweighted shortest paths were asked (Q26).

**2. Kruskal's** — MST algorithm; no ordering semantics.
- **Would be correct if:** minimum spanning tree were asked (Q27).

**3. Floyd-Warshall** — All-pairs shortest paths (O(V³)); unrelated.
- **Would be correct if:** the question asked shortest distance between *every* pair of vertices.

#### Exam Trigger

- **"DAG, valid order/dependencies"** → **Topological Sort**

#### Final Answer: **Topological Sort**

---

### Q59. Production, Finance and Research networks must communicate with separate IP schemes. Which device routes traffic?

**Options:**
- [ ] Ethernet Hub
- [ ] Layer-2 Switch
- [ ] Wireless Access Point
- [x] **Router**

#### Correct Answer: Router

**Why this is correct**

A **Router** operates at **Layer 3 (Network)** — it forwards IP packets **between different subnets/networks**, choosing paths by IP address. Separate IP schemes require routing between them.

#### Core Concept

| Device | Layer | Function |
|--------|-------|----------|
| Hub | 1 (Physical) | Broadcast signal to all ports |
| Switch | 2 (Data Link) | Forward frames by MAC address |
| Router | 3 (Network) | Forward packets by IP across subnets |
| WAP | 2 | Wireless bridging to LAN |

#### Why the Other Options Are Incorrect

**1. Ethernet Hub** — Layer 1 broadcast box; no address awareness, no segmentation.
- **Would be correct if:** the question asked for a simple signal repeater for short LAN wiring.

**2. Layer-2 Switch** — Forwards by MAC within one LAN/broadcast domain; can't cross subnets.
- **Would be correct if:** the question was about efficient MAC-based forwarding within a LAN.

**3. Wireless Access Point** — Bridges Wi-Fi clients to the wired LAN (Layer 2); no IP routing.
- **Would be correct if:** the question was about Wi-Fi coverage for mobile devices.

#### Exam Trigger

- **"Separate IP networks/subnets, communicate"** → **Router**

#### Final Answer: **Router**

---

### Q60. Millions of sorted shipment records are searched often and updated nightly. Which search strategy is best?

**Options:**
- [ ] Depth-First Search
- [ ] Linear Search
- [ ] Breadth-First Search
- [x] **Binary Search**

#### Correct Answer: Binary Search

**Why this is correct**

Data is **sorted** and **static between nightly updates** → **Binary Search** gives **O(log n)** lookup, which for millions of records is ~20-30 comparisons instead of millions. No graph structure needed; updates are batched, so re-sorting cost is amortized.

#### Core Concept

```
Binary search: compare mid, halve search space each step.
N = 1,000,000 → log₂N ≈ 20 comparisons per search.
Linear search: up to 1,000,000 comparisons.
```

#### Why the Other Options Are Incorrect

**1. Depth-First Search** — Graph traversal; irrelevant for sorted array search.
- **Would be correct if:** the question involved graph traversal/cycle detection (Q53).

**2. Linear Search** — O(n) per search; too slow for millions of records searched often.
- **Would be correct if:** data were unsorted, small, or searched rarely.

**3. Breadth-First Search** — Graph traversal for unweighted shortest paths.
- **Would be correct if:** the question were about graph distances (Q26).

#### Exam Trigger

- **"Sorted, searched often, batch-updated"** → **Binary Search**

#### Final Answer: **Binary Search**

---
## 📘 Part 7 (cbt1_061 – cbt1_070): ML, System Design & Architecture

### Q61. Which dataset characteristic is most likely to reduce the predictive accuracy of a supervised machine learning model?

**Options:**
- [ ] Feature normalization
- [ ] Larger training dataset
- [x] **Missing and inconsistent values**
- [ ] Balanced class distribution

#### Correct Answer: Missing and inconsistent values

**Why this is correct**

**Missing values** force imputation/removal (bias, lost signal); **inconsistent values** (typos, contradictory labels, mixed units) inject noise the model memorizes as wrong patterns → **lower accuracy**. The other three options all *help* accuracy — this is an elimination question.

#### Core Concept

| Characteristic | Effect on accuracy |
|----------------|--------------------|
| Missing/inconsistent values | **Reduces** (noise + bias) |
| Feature normalization | Helps (stable gradients, comparable scales) |
| Larger training dataset | Helps (more signal, less overfitting) |
| Balanced class distribution | Helps (no majority-class bias) |

#### Example

A fraud-detection dataset where 40% of "amount" values are missing and some labels are mis-entered → the model learns distorted thresholds → higher false negatives.

#### Why the Other Options Are Incorrect

**1. Feature normalization** — Scaling features to comparable ranges helps models converge and weigh features fairly.
- **Would be correct if:** the question asked how to handle differing feature scales.

**2. Larger training dataset** — More data generally improves generalization.
- **Would be correct if:** the question asked what reduces overfitting/improves learning.

**3. Balanced class distribution** — Balanced classes prevent the model from just predicting the majority class.
- **Would be correct if:** the question asked how to fix class-imbalance bias.

#### Exam Trigger

- **"Reduces accuracy"** → **Missing/inconsistent values** (everything else listed is positive)

#### Final Answer: **Missing and inconsistent values**

---

### Q62. An LRU cache needs O(1) lookup and O(1) least-recent eviction. Which implementation fits?

**Options:**
- [ ] B+ Tree + Dynamic Array
- [ ] AVL Tree + Queue
- [ ] Skip List + Circular Buffer
- [x] **Hash Table + Doubly Linked List**

#### Correct Answer: Hash Table + Doubly Linked List

**Why this is correct**

The canonical LRU implementation:
- **Hash Table**: O(1) key → node lookup
- **Doubly Linked List**: nodes ordered by recency — most-recent at head, least-recent at tail
  - access/move-to-head: O(1) (needs prev/next pointers)
  - evict tail: O(1)

#### Core Concept

```
get(k):  node = hash[k]; move node to head → O(1)
put(k,v): if exists → update, move to head
          else add at head; if over capacity → remove tail node (LRU) → O(1)
```

#### Example

Cache cap = 3: keys A, B, C. Access B → order C, A, B (B to head). Insert D → evict LRU = C.

#### Why the Other Options Are Incorrect

**1. B+ Tree + Dynamic Array** — B+ gives O(log n) lookup, not O(1); array shifts are O(n) for head moves.
- **Would be correct if:** range scans or disk-resident caches were needed.

**2. AVL Tree + Queue** — AVL lookup O(log n); a plain queue can't move an arbitrary element to front in O(1).
- **Would be correct if:** only O(log n) lookup was acceptable.

**3. Skip List + Circular Buffer** — Skip list O(log n); circular buffer needs O(n) search for key and O(n) reshuffles.
- **Would be correct if:** the workload tolerated log n access.

#### Exam Trigger

- **"LRU, O(1) lookup + O(1) eviction"** → **Hash Table + Doubly Linked List**

#### Final Answer: **Hash Table + Doubly Linked List**

---

### Q63. A compiler checks arbitrarily nested parentheses. Which model is most appropriate?

**Options:**
- [ ] Finite Automaton
- [ ] Turing Machine
- [x] **Pushdown Automaton**
- [ ] Linear Bounded Automaton

#### Correct Answer: Pushdown Automaton

**Why this is correct**

Nested structures require **counting/stack memory** (push `(` on open, pop on close). The **Pushdown Automaton (PDA)** = finite control + **stack** — the minimal machine that handles arbitrary nesting (equivalent to CFG — same idea as Q30, but asks for the *machine*).

#### Core Concept

- PDA = DFA + stack.
- Open paren → PUSH; close paren → POP; reject if pop from empty stack or leftover at end.
- Grammar version: `S → ( S ) | ε` (Q30).

#### Why the Other Options Are Incorrect

**1. Finite Automaton** — No stack → can't count nesting depth (aⁿbⁿ not regular).
- **Would be correct if:** the format were fixed with no nesting (Q79 — DFA).

**2. Turing Machine** — Full computation power; overkill (PDA suffices).
- **Would be correct if:** the question involved general computation (e.g., any computable function).

**3. Linear Bounded Automaton** — For context-sensitive languages (aⁿbⁿcⁿ); stronger than needed.
- **Would be correct if:** the language needed multi-relation counting (e.g., equal counts of three symbols).

#### Exam Trigger

- **"Nested parentheses — machine model"** → **Pushdown Automaton**
- **Grammar version** → **CFG** (Q30); **no nesting** → **DFA** (Q79)

#### Final Answer: **Pushdown Automaton**

---

### Q64. A server waits on disk I/O for many client requests. Which model improves CPU utilization?

**Options:**
- [ ] Cooperative Scheduling
- [ ] Static Partitioning
- [ ] Non-Preemptive Scheduling
- [x] **Asynchronous I/O**

#### Correct Answer: Asynchronous I/O

**Why this is correct**

**Asynchronous (non-blocking) I/O** lets a thread issue a disk request and **continue serving other clients** while the I/O completes in the background (via completion callbacks/events). CPU stays busy instead of sleeping on I/O waits → higher utilization and throughput.

#### Core Concept

- **Blocking I/O**: thread sleeps until disk returns → CPU idles (bad for many clients).
- **Asynchronous I/O**: request → return immediately → notify later → thread handles other requests meanwhile.

#### Example

A web server with 200 clients doing disk reads: with blocking I/O you'd need ~200 threads, mostly asleep. With async I/O (epoll/io_uring), a few threads service all 200 concurrently → CPU utilization stays high.

#### Why the Other Options Are Incorrect

**1. Cooperative Scheduling** — Processes voluntarily yield CPU; doesn't remove I/O blocking.
- **Would be correct if:** the question asked how threads voluntarily share the CPU.

**2. Static Partitioning** — Memory partition scheme; unrelated to I/O waits.
- **Would be correct if:** the question were about fixed memory partitions.

**3. Non-Preemptive Scheduling** — A process runs until it blocks/yields; doesn't make disk waits useful.
- **Would be correct if:** the question asked about simple scheduling without interrupts (FCFS-style).

#### Exam Trigger

- **"Waits on disk I/O, many clients"** → **Asynchronous I/O**

#### Final Answer: **Asynchronous I/O**

---

### Q65. A sort must guarantee O(n log n) worst-case performance and support external sorting. Which is preferred?

**Options:**
- [x] **Merge Sort**
- [ ] Quick Sort
- [ ] Heap Sort
- [ ] Shell Sort

#### Correct Answer: Merge Sort

**Why this is correct**

**Merge Sort**:
- Guaranteed **O(n log n)** worst case (unlike quicksort's O(n²))
- **Sequential access pattern** → merges run from disk sequentially → the standard **external sort** (sort-merge)

#### Core Concept

```
External sort: divide into runs that fit in RAM → sort each → k-way merge on disk.
Merge sort's sequential read/write pattern maps perfectly to disk.
```

#### Why the Other Options Are Incorrect

**1. Quick Sort** — Average O(n log n) but **worst-case O(n²)** (bad pivots); random-access-heavy (bad for disk).
- **Would be correct if:** the question asked for in-memory sorting with average-case speed (library sort).

**2. Heap Sort** — Guarantees O(n log n) in place, but **random access** pattern (sift-down jumps) → poor for external/disk sorting.
- **Would be correct if:** the question required in-place O(1) extra space.

**3. Shell Sort** — Gap-based; worst case O(n²) (gap-dependent), not a guaranteed O(n log n).
- **Would be correct if:** the question asked for a simple in-place improvement over insertion sort.

#### Exam Trigger

- **"Guaranteed O(n log n) + external sorting"** → **Merge Sort**
- **"In-place guaranteed O(n log n)"** → **Heap Sort**

#### Final Answer: **Merge Sort**

---

### Q66. The same arithmetic operation runs on thousands of independent data elements. Which feature helps most?

**Options:**
- [ ] Simultaneous Multithreading
- [ ] Superscalar Dispatch
- [x] **SIMD Execution**
- [ ] Out-of-Order Execution

#### Correct Answer: SIMD Execution

**Why this is correct**

**SIMD (Single Instruction, Multiple Data)** applies one instruction to **multiple data elements at once** via wide vector registers (SSE/AVX/NEON). Thousands of independent elements doing the same op = the textbook SIMD workload (data-level parallelism).

#### Core Concept

```
Scalar: for i: a[i] = b[i] + c[i]      → N instructions
SIMD:   a[0..7] = b[0..7] + c[0..7]    → 1 instruction for 8 elements (AVX)
```
Vectorization compilers auto-generate this for such loops.

#### Why the Other Options Are Incorrect

**1. Simultaneous Multithreading (SMT)** — Runs multiple threads on one core's execution units; helps when threads are independent but doesn't speed a single data-parallel loop.
- **Would be correct if:** the question asked about hiding latency with extra threads (Hyper-Threading).

**2. Superscalar Dispatch** — Issues **multiple different instructions** per cycle (ILP); not many-data-per-instruction.
- **Would be correct if:** the question asked about executing several independent instructions in parallel.

**3. Out-of-Order Execution** — Reorders instructions to hide stalls; no data-element parallelism.
- **Would be correct if:** the question asked about dynamic scheduling (Q14).

#### Exam Trigger

- **"Same op, thousands of elements"** → **SIMD** (vectorization)

#### Final Answer: **SIMD Execution**

---

### Q67. A system elects a new leader after coordinator failure and replicates logs. Which algorithm fits?

**Options:**
- [ ] Chandy-Lamport
- [ ] Vector Clocks
- [x] **Raft**
- [ ] Two-Phase Commit

#### Correct Answer: Raft

**Why this is correct**

**Raft** is a consensus algorithm built on:
1. **Leader election** — nodes vote; a new leader is chosen after failure
2. **Log replication** — leader replicates the log to followers with majorities (quorum)

This matches the requirement exactly (same as Q4/Q95 family of distributed primitives).

#### Core Concept

- Terms & votes: follower → candidate → leader on election timeout.
- Leader appends entries → replicates → commits once majority ACKs.
- Follower failure → leader re-sends; leader failure → new election.

#### Why the Other Options Are Incorrect

**1. Chandy-Lamport** — Distributed **snapshot** algorithm (consistent global states for recording/recovery).
- **Would be correct if:** the question asked how to capture consistent snapshots in a distributed system.

**2. Vector Clocks** — Causal ordering of events without synchronized clocks.
- **Would be correct if:** the question asked about "happened-before" ordering (Q95).

**3. Two-Phase Commit** — Atomic **commit across databases** (all-or-nothing), not leader election.
- **Would be correct if:** the question was "two DBs must both commit or both roll back" (Q4).

#### Exam Trigger

- **"Leader election + log replication"** → **Raft**
- **"Atomic commit across DBs"** → **2PC** (Q4)
- **"Causal ordering"** → **Vector Clocks** (Q95)

#### Final Answer: **Raft**

---

### Q68. A text editor supports frequent edits near cursor in very large documents. Which structure is most suitable?

**Options:**
- [ ] Doubly Linked List
- [ ] Rope
- [x] **Gap Buffer**
- [ ] Piece Table

#### Correct Answer: Gap Buffer

**Why this is correct**

A **Gap Buffer** keeps a **reserved empty gap at the cursor**. Typing inserts directly into the gap (O(1)); moving the cursor just shifts the gap. Ideal for *cursor-local edits* — the exact usage pattern of interactive editors.

#### Core Concept

```
Buffer: "Hello[      ]World"   (gap at cursor)
Type "X": "HelloX[     ]World" → O(1)
Move cursor → move gap (amortized O(distance))
```

#### Why the Other Options Are Incorrect

**1. Doubly Linked List** — Insert/delete O(1) only after O(n) traversal to the cursor position; no caching benefit.
- **Would be correct if:** edits happened at known positions after cheap location access.

**2. Rope** — Balanced tree of string chunks; excellent for **whole-document restructuring**, split/join operations, large edits anywhere.
- **Would be correct if:** edits were large/structural across the document rather than per-keystroke typing.

**3. Piece Table** — Stores pieces referencing an original file + appended blocks; great for **versioned/immutable documents** (undo history, minimal rewrites).
- **Would be correct if:** the requirement were cheap undo/versioning over frequent in-place typing.

#### Exam Trigger

- **"Edits near cursor"** → **Gap Buffer**
- **"Large structural edits anywhere"** → **Rope**
- **"Versioning/undo-friendly"** → **Piece Table**

#### Final Answer: **Gap Buffer**

---

### Q69. A compiler must identify keywords, identifiers and literals before parsing. Which phase does this?

**Options:**
- [ ] Semantic Analysis
- [ ] Syntax Analysis
- [ ] Intermediate Code Generation
- [x] **Lexical Analysis**

#### Correct Answer: Lexical Analysis

**Why this is correct**

**Lexical Analysis (scanning)** is the first phase: it groups raw characters into **tokens** — keywords (`if`, `while`), identifiers (`count`), literals (`42`, `"hi"`), operators — feeding them to the parser.

#### Core Concept — Compiler Phases

```
Source → Lexical → Syntax → Semantic → IR Generation → Optimization → Code Gen
         (tokens) (parse tree) (types/scope) (IR)      (optimize)     (assembly)
```
Lexical = before parsing (Q69); Syntax = parse tree (Q98); Semantic = type/scope checks (Q94).

#### Why the Other Options Are Incorrect

**1. Semantic Analysis** — Checks types, scopes, undeclared variables using the symbol table (after parsing).
- **Would be correct if:** the issue were type mismatch/undeclared variable (Q94).

**2. Syntax Analysis** — Builds the parse tree from tokens per the grammar.
- **Would be correct if:** the question asked which phase detects grammar violations (Q98).

**3. Intermediate Code Generation** — Produces machine-independent IR from the parse tree (after semantics).
- **Would be correct if:** the question asked about the middle-end representation (Q96).

#### Exam Trigger

- **"Before parsing, tokens"** → **Lexical Analysis**

#### Final Answer: **Lexical Analysis**

---

### Q70. A data warehouse has slow analytical reports despite indexing; updates occur once daily. What helps most?

**Options:**
- [ ] TEXT columns for indexed fields
- [ ] Unrelated table splits
- [x] **Controlled denormalization to reduce joins**
- [ ] More foreign key constraints

#### Correct Answer: Controlled denormalization to reduce joins

**Why this is correct**

OLAP queries join many tables over billions of rows — **joins are the bottleneck**. With writes only once daily (updates cost little), **denormalization** (pre-joining / duplicating columns into wide fact tables) eliminates runtime joins → dramatically faster reports. This is the *opposite* of OLTP advice.

#### Core Concept

| System | Writes | Strategy |
|--------|--------|----------|
| OLTP (transactions) | Heavy, frequent | Normalize (reduce redundancy) |
| OLAP (reports) | Rare (batch) | Denormalize (reduce joins) |

#### Example

A sales report joining `Sales`, `Customer`, `Region` daily: materialize `RegionName`, `CustomerName` into the Sales fact table (denormalized) → report query becomes a single-table scan → minutes → seconds.

#### Why the Other Options Are Incorrect

**1. TEXT columns for indexed fields** — TEXT is unindexable/slow for equality & sort; makes queries worse.
- **Would be correct if:** the question asked for storing large unstructured content.

**2. Unrelated table splits** — Splitting unrelated tables does nothing for join-heavy report queries.
- **Would be correct if:** the question were about dividing huge tables for manageability (Q24 partitioning).

**3. More foreign key constraints** — FKs enforce integrity but add **join overhead and validation cost**; the opposite of what's needed.
- **Would be correct if:** the question asked how to guarantee referential integrity.

#### Exam Trigger

- **"Slow OLAP reports, daily batch updates"** → **Denormalization** (opposite of OLTP advice)

#### Final Answer: **Controlled denormalization to reduce joins**

---
## 📘 Part 8 (cbt1_071 – cbt1_080): DBMS Triggers, Locks & REST

### Q71. Undo stores operations and removes them only in reverse order. Which implementation best fits?

**Options:**
- [ ] Deque
- [ ] Circular Buffer
- [x] **Stack**
- [ ] Doubly Linked List

#### Correct Answer: Stack

**Why this is correct**

Undo semantics = **LIFO (Last In, First Out)**: undo must reverse the **most recent operation first**. A **Stack** is exactly LIFO — push operations as performed, pop to undo.

#### Core Concept

```
Actions:  A → B → C     (stack: [A, B, C] top=C)
Undo:     pop C → undo C; stack [A, B]
Undo:     pop B → undo B; stack [A]
```
Reverse order of application = reverse order of push = pop.

#### Why the Other Options Are Incorrect

**1. Deque** — Allows insert/delete at both ends; no LIFO requirement (Q45's ADT).
- **Would be correct if:** operations needed at both ends (e.g., undo + redo queue at front).

**2. Circular Buffer** — Ring buffer; FIFO-ish overwrite semantics, not reverse-order.
- **Would be correct if:** the question asked for fixed-capacity streaming history (last N events).

**3. Doubly Linked List** — Arbitrary insertion/deletion; no inherent ordering constraint.
- **Would be correct if:** the question needed middle insert/delete (Q47).

#### Exam Trigger

- **"Undo, reverse order"** → **Stack** (LIFO)

#### Final Answer: **Stack**

---

### Q72. Which traversal visits root, left subtree, then right subtree?

**Options:**
- [ ] Postorder
- [ ] Level Order
- [x] **Preorder**
- [ ] Inorder

#### Correct Answer: Preorder

**Why this is correct**

**Preorder** = Root → Left → Right (root *first* — "pre"). The three depth-first orders differ only in *when* the root is visited:

#### Core Concept — The Three DFS Orders

| Traversal | Order | Mnemonic |
|-----------|-------|----------|
| Preorder  | Root, Left, Right | Root **pre** (first) |
| Inorder   | Left, Root, Right | Root in the **middle** (sorted for BST) |
| Postorder | Left, Right, Root | Root **post** (last) |

#### Example

```
     1
    / \
   2   3
  / \
 4   5
```
- Preorder: 1, 2, 4, 5, 3
- Inorder: 4, 2, 5, 1, 3
- Postorder: 4, 5, 2, 3, 1
- Level order: 1, 2, 3, 4, 5

#### Why the Other Options Are Incorrect

**1. Postorder** — Left, Right, **Root** (root last) — used for deleting trees / expression trees.
- **Would be correct if:** children must be processed before parents (delete tree, bottom-up evaluation).

**2. Level Order** — BFS by levels, root to leaves row by row.
- **Would be correct if:** the question asked about level-by-level (BFS) visiting.

**3. Inorder** — Left, **Root**, Right — gives sorted output on a BST.
- **Would be correct if:** the question asked for sorted traversal of a BST.

#### Exam Trigger

- **"Root first"** → **Preorder**; **"Root middle"** → **Inorder**; **"Root last"** → **Postorder**

#### Final Answer: **Preorder**

---

### Q73. An online exam system must keep running if one app server fails. Which design helps most?

**Options:**
- [ ] Higher CPU Clock Speed
- [ ] Compressed Static Images
- [x] **Redundant Load-Balanced Servers**
- [ ] Larger Database Cache

#### Correct Answer: Redundant Load-Balanced Servers

**Why this is correct**

**Redundancy + load balancing** = multiple app-server instances behind a load balancer. On server failure, the LB **health-checks and reroutes traffic** to healthy instances → the system keeps running (high availability / failover).

#### Core Concept

```
Clients → Load Balancer → [App1, App2, App3] → DB
App2 dies → LB stops sending it traffic → App1/App3 absorb load → no downtime
```

#### Why the Other Options Are Incorrect

**1. Higher CPU Clock Speed** — Makes one server faster; doesn't help when it fails.
- **Would be correct if:** the issue were compute performance, not availability.

**2. Compressed Static Images** — Reduces bandwidth/latency; irrelevant to failure.
- **Would be correct if:** the issue were slow page loads from large assets.

**3. Larger Database Cache** — Faster reads; single point of failure remains.
- **Would be correct if:** the issue were DB query latency (Q31/Q33 family).

#### Exam Trigger

- **"Keep running if one server fails"** → **Redundant load-balanced servers** (failover/HA)

#### Final Answer: **Redundant Load-Balanced Servers**

---

### Q74. Repeated key lookups must improve from O(n) to average O(1), accepting extra memory. What is best?

**Options:**
- [x] **Hash Table**
- [ ] Binary Heap
- [ ] Linked List
- [ ] Queue

#### Correct Answer: Hash Table

**Why this is correct**

A **Hash Table** maps keys to buckets via a hash function → **average O(1)** search/insert/delete. It trades memory (bucket array) for speed — exactly the stated tradeoff.

#### Core Concept

```
lookup(key): idx = hash(key) % size → check bucket (O(1) average)
```
Good hash + load factor ~0.7 → near-constant operations.

#### Why the Other Options Are Incorrect

**1. Binary Heap** — Priority structure; searching for an arbitrary key is O(n); no key→value mapping.
- **Would be correct if:** the question asked for max/min extraction (Q44).

**2. Linked List** — O(n) lookup by key; no hashing.
- **Would be correct if:** the question involved frequent middle insert/delete (Q47).

**3. Queue** — FIFO only; no key lookup at all.
- **Would be correct if:** the question asked for FIFO processing.

#### Exam Trigger

- **"O(n) → average O(1), memory OK"** → **Hash Table**

#### Final Answer: **Hash Table**

---

### Q75. A networking application needs to check millions of IP addresses against a blacklist that updates hourly. False positives must be minimized but occasional false positives are acceptable. Which data structure is most appropriate?

**Options:**
- [ ] Hash Table
- [x] **Bloom Filter**
- [ ] Binary Search Tree
- [ ] Trie

#### Correct Answer: Bloom Filter

**Why this is correct**

A **Bloom Filter** answers membership in **O(k) hash probes** with tiny, fixed memory:
- **Zero false negatives** — a blocked IP is never missed
- **Tunable false-positive rate** — minimized by more bits/hash functions
- Perfect for **millions of entries** in memory-constrained devices (the stated constraints)

#### Core Concept

- Bit array of m bits + k hash functions.
- Insert: set k bits. Query: if any bit is 0 → definitely absent; if all set → probably present.
- FP rate = (1 − e^(−kn/m))^k → tune m, k to minimize.

#### Why the Other Options Are Incorrect

**1. Hash Table** — Exact and O(1), but stores every key → memory cost for millions of IPs; also the question accepts FP (which bloom uses to save memory).
- **Would be correct if:** zero false positives were mandatory (exact membership).

**2. Binary Search Tree** — O(log n) with key storage; no FP but more memory; slower than bloom.
- **Would be correct if:** sorted iteration/range queries were needed.

**3. Trie** — Prefix structure for strings; heavier than a bloom filter for flat IP membership.
- **Would be correct if:** the question asked about prefix matching (CIDR ranges, autocomplete).

#### Exam Trigger

- **"False positives OK, space-tight membership"** → **Bloom Filter**
- **"Zero FP / exact"** → **Hash Table**

#### Final Answer: **Bloom Filter**

---

### Q76. What is the main purpose of a transaction log?

**Options:**
- [ ] Store passwords
- [ ] Create indexes
- [x] **Enable recovery and auditing**
- [ ] Manage sessions

#### Correct Answer: Enable recovery and auditing

**Why this is correct**

The **transaction log (write-ahead log)** records every transaction's changes *before* they hit the data files. It enables:
- **Recovery** — replay committed transactions, undo uncommitted ones after a crash (durability/atomicity)
- **Auditing** — a historical trail of changes

#### Core Concept — Write-Ahead Logging

```
BEGIN → write log records → COMMIT (log first) → apply to data files
Crash → use log to redo committed, undo uncommitted → consistent DB
```

#### Why the Other Options Are Incorrect

**1. Store passwords** — Passwords are stored hashed in user tables, never in transaction logs.
- **Would be correct if:** the question asked how to store credentials securely (salted hashing — Q2).

**2. Create indexes** — Indexes are created by DDL; logs *record* that DDL, they don't build indexes.
- **Would be correct if:** the question asked what speeds up lookups (Q33).

**3. Manage sessions** — Sessions are app-layer state; unrelated to transaction logging.
- **Would be correct if:** the question asked how login state is kept across requests.

#### Exam Trigger

- **"Purpose of transaction log"** → **Recovery + auditing**

#### Final Answer: **Enable recovery and auditing**

---

### Q77. Which database object automatically executes when specific events occur?

**Options:**
- [x] **Trigger**
- [ ] View
- [ ] Cursor
- [ ] Schema

#### Correct Answer: Trigger

**Why this is correct**

A **Trigger** is a stored program that **fires automatically** on specified events: `INSERT`, `UPDATE`, `DELETE` (before/after, row/statement level).

#### Core Concept

```sql
CREATE TRIGGER audit_salary
AFTER UPDATE OF salary ON employees
FOR EACH ROW
  INSERT INTO salary_audit(emp_id, old_sal, new_sal) ...;
-- Every salary update automatically writes an audit row — no app code needed.
```

#### Why the Other Options Are Incorrect

**1. View** — A **stored query** (virtual table); it doesn't execute anything until queried.
- **Would be correct if:** the question asked for a read-only logical projection of tables.

**2. Cursor** — An explicit **row-by-row iteration handle** used in procedural code; doesn't auto-fire.
- **Would be correct if:** the question asked how to process query results one row at a time.

**3. Schema** — The overall **structure** (tables, constraints, views) — a namespace, not executable.
- **Would be correct if:** the question asked about database structure/organization.

#### Exam Trigger

- **"Auto-executes on events"** → **Trigger**
- **"Stored query / virtual table"** → **View**

#### Final Answer: **Trigger**

---

### Q78. What is the purpose of a semaphore?

**Options:**
- [ ] Encrypt files
- [ ] Route packets
- [ ] Compress memory
- [x] **Synchronize access to shared resources**

#### Correct Answer: Synchronize access to shared resources

**Why this is correct**

A **semaphore** is a counter-based OS primitive used for **synchronization**: it limits how many threads/processes can access a shared resource (mutual exclusion with `mutex=1`, or N resources with counting semaphore).

#### Core Concept

```
wait(S):  if S > 0 then S-- else block
signal(S): S++; wake one waiter
S = 1 (binary): only one process in critical section
S = 3 (counting): at most 3 consumers
```
Classic use: producer-consumer (buffer slots), readers-writers, mutex.

#### Why the Other Options Are Incorrect

**1. Encrypt files** — Cryptography concern (AES/RSA); semaphores don't protect data secrecy.
- **Would be correct if:** the question asked how to protect data confidentiality.

**2. Route packets** — Network-layer task (routers, IP); semaphores don't forward packets.
- **Would be correct if:** the question asked how packets traverse subnets (Q59).

**3. Compress memory** — Memory optimization (paging/compaction); unrelated.
- **Would be correct if:** the question asked about memory efficiency.

#### Exam Trigger

- **"Purpose of semaphore"** → **Synchronize shared-resource access**

#### Final Answer: **Synchronize access to shared resources**

---

### Q79. A protocol validates fixed-format headers with no nesting. Which model is sufficient?

**Options:**
- [ ] Context-Sensitive Grammar
- [ ] Pushdown Automaton
- [ ] Turing Machine
- [x] **Deterministic Finite Automaton**

#### Correct Answer: Deterministic Finite Automaton

**Why this is correct**

**Fixed-format, non-nested** headers form a **regular language** — checkable with finite state and **no stack**. A **DFA** (or regex) is fully sufficient and minimal. The keyword is **"no nesting"**.

#### Core Concept

- Fixed fields: e.g., `[version(1 byte)][type(1 byte)][length(2 bytes)][payload...]` — validation = state transitions per byte.
- No counters, no nesting → no memory needed → DFA.
- Nesting would need a stack → PDA (Q63); more structure → LBA/TM.

#### Why the Other Options Are Incorrect

**1. Context-Sensitive Grammar** — Type-1; overkill (needed only for aⁿbⁿcⁿ-style dependencies).
- **Would be correct if:** the format had context-sensitive cross-field constraints.

**2. Pushdown Automaton** — Adds a stack for nesting; unnecessary and wasteful here.
- **Would be correct if:** the headers contained arbitrary nesting (Q63).

**3. Turing Machine** — Full computation power; massively overkill for fixed headers.
- **Would be correct if:** the question asked about general computation.

#### Exam Trigger

- **"Fixed format, NO nesting"** → **DFA**
- **"Arbitrary nesting"** → **PDA** (Q63) — the discriminator is the word "nesting"

#### Final Answer: **Deterministic Finite Automaton**

---

### Q80. A team is designing a web API for a resource-oriented system. They want to follow standard architectural principles where resources are represented as nouns and operations are represented by HTTP methods. Which design principle is this?

**Options:**
- [ ] SOAP-based Design
- [x] **RESTful Design**
- [ ] GraphQL Schema
- [ ] RPC-based Design

#### Correct Answer: RESTful Design

**Why this is correct**

**REST (Representational State Transfer)** models the system as **resources (nouns)** — `/users`, `/orders/123` — and uses **HTTP methods (verbs)** for operations: GET (read), POST (create), PUT (update), DELETE (remove). Stateless, uniform interface.

#### Core Concept

```
GET    /orders       → list orders
POST   /orders       → create order
GET    /orders/5     → read order 5
PUT    /orders/5     → update order 5
DELETE /orders/5     → delete order 5
```
Nouns in URI, verbs in HTTP methods.

#### Why the Other Options Are Incorrect

**1. SOAP-based Design** — XML-envelope protocol exposing **operations** (`GetUser`, `UpdateOrder`) via a WSDL contract.
- **Would be correct if:** the question asked about XML/SOAP enterprise web services with strict contracts.

**2. GraphQL Schema** — Single endpoint; clients query typed **schemas/fields**; operations are graph queries, not HTTP verbs.
- **Would be correct if:** the question asked about client-driven flexible queries from one endpoint.

**3. RPC-based Design** — Endpoints look like **verb/action calls** (`/getUser`, `/deleteOrder`) — the opposite noun/verb split.
- **Would be correct if:** the question described action-style endpoints or remote procedure calls.

#### Exam Trigger

- **"Nouns as resources + HTTP methods"** → **RESTful Design**
- **"Verbs in endpoint"** → **RPC**

#### Final Answer: **RESTful Design**

---
## 📘 Part 9 (cbt1_081 – cbt1_090): Complexity, SJF & Consistent Hashing

### Q81. Which algorithmic complexity grows fastest as data volume increases?

**Options:**
- [x] **O(n²)**
- [ ] O(1)
- [ ] O(n)
- [ ] O(log n)

#### Correct Answer: O(n²)

**Why this is correct**

Of the four given options, **quadratic** dominates: O(1) < O(log n) < O(n) < O(n²) for large n.

#### Core Concept — Growth Order

| Complexity | n=10 | n=1,000 | n=1,000,000 |
|------------|------|---------|-------------|
| O(1)       | 1    | 1       | 1           |
| O(log n)   | ~3   | ~10     | ~20         |
| O(n)       | 10   | 1,000   | 1,000,000   |
| O(n²)      | 100  | 1,000,000 | 10¹²      |

O(n²) always outgrows the rest once n is large.

#### Why the Other Options Are Incorrect

**1. O(1)** — Constant; doesn't grow at all with data size.
- **Would be correct if:** the question asked which complexity is fastest/independent of input size (hash lookup — Q74).

**2. O(n)** — Linear growth; slower than quadratic.
- **Would be correct if:** the question asked which grows linearly with input.

**3. O(log n)** — Logarithmic growth; barely grows (binary search — Q60).
- **Would be correct if:** the question asked which grows slowest besides constant.

#### Exam Trigger

- **"Fastest growth among these options"** → **O(n²)**
- **Growth ranking:** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

#### Final Answer: **O(n²)**

---

### Q82. An optimization problem is NP-Complete. What is practical for very large instances?

**Options:**
- [ ] Binary Search
- [x] **Approximation or heuristic algorithms**
- [ ] Exhaustive search
- [ ] Bubble Sort

#### Correct Answer: Approximation or heuristic algorithms

**Why this is correct**

**NP-Complete** problems have no known polynomial exact solution — exact algorithms are exponential. For **very large instances**, practice uses:
- **Approximation algorithms** (provable factor bound — Q43)
- **Heuristics** (good practical solutions, no guarantee)

#### Core Concept

```
Exact (exhaustive) → 2ⁿ time → impossible for large n
Approximation → poly-time, guaranteed within c·OPT
Heuristic → poly-time, works well in practice, no guarantee
```

#### Example

TSP over 10,000 cities: exhaustive = 10000! — impossible. Nearest-neighbor heuristic or 1.5-approx (Christofides) solves it in minutes with near-optimal tours.

#### Why the Other Options Are Incorrect

**1. Binary Search** — Requires sorted data & a monotonic property; not a solver for NP-complete optimization.
- **Would be correct if:** the question were about searching a sorted structure (Q60).

**2. Exhaustive search** — Guarantees optimum but is **exponential**; unusable for very large instances.
- **Would be correct if:** the instance were small or correctness-at-any-cost were required.

**3. Bubble Sort** — A polynomial *easy* problem's algorithm; irrelevant to NP-complete optimization.
- **Would be correct if:** the question asked to sort a small list simply.

#### Exam Trigger

- **"NP-Complete, very large instances"** → **Approximation / heuristic**
- **"Guaranteed factor"** → **Approximation** (Q43); **"no guarantee"** → **Heuristic**

#### Final Answer: **Approximation or heuristic algorithms**

---

### Q83. Which protocol is commonly used for network device monitoring?

**Options:**
- [ ] Syslog
- [ ] ICMP
- [ ] NetFlow
- [x] **SNMP**

#### Correct Answer: SNMP

**Why this is correct**

**SNMP (Simple Network Management Protocol)** is the standard for **monitoring network devices**: it reads device variables via **MIB** (Management Information Base) and pushes alerts via **traps** (UDP 161/162). Used by NMS tools (Nagios, PRTG, Zabbix).

#### Core Concept

- Manager ↔ Agent (on router/switch/server).
- Operations: **GET/GETNEXT/SET/TRAP**.
- Agent exposes OIDs (CPU, uptime, interface counters) through the MIB.

#### Why the Other Options Are Incorrect

**1. Syslog** — Generic **log message** transport (application/OS logs), not structured device metrics.
- **Would be correct if:** the question asked how devices send event logs to a central server.

**2. ICMP** — **Ping/error messages** (echo, unreachable); connectivity checks, not structured monitoring.
- **Would be correct if:** the question asked how to test reachability (ping).

**3. NetFlow** — **Traffic flow** statistics (who talks to whom, volumes); not device health metrics.
- **Would be correct if:** the question asked about network traffic accounting/analysis.

#### Exam Trigger

- **"Network device monitoring protocol"** → **SNMP** (MIB/OIDs/traps)

#### Final Answer: **SNMP**

---

### Q84. A scheduler always runs the process with the shortest estimated execution time. Which algorithm is used?

**Options:**
- [ ] Round Robin
- [ ] First Come First Served
- [ ] Lottery Scheduling
- [x] **Shortest Job First (SJF)**

#### Correct Answer: Shortest Job First (SJF)

**Why this is correct**

**SJF/SRTF** always picks the process with the **smallest (estimated) CPU burst**. It **provably minimizes average waiting time** among non-preemptive (SJF) and preemptive (SRTF) schedulers.

#### Core Concept — Example

| Process | Burst |
|---------|-------|
| P1 | 6 |
| P2 | 8 |
| P3 | 7 |
| P4 | 3 |

SJF order: P4(3) → P1(6) → P3(7) → P2(8).
Avg waiting = (0 + 3 + 9 + 16)/4 = 7 — minimum possible.

#### Why the Other Options Are Incorrect

**1. Round Robin** — Fixed quantum time-slicing, ignores burst lengths (Q21).
- **Would be correct if:** the question asked for fair time-sliced sharing.

**2. First Come First Served** — Runs in arrival order; can have convoy effects (long job blocks short ones).
- **Would be correct if:** the question asked for the simplest non-preemptive scheduler by arrival.

**3. Lottery Scheduling** — Probabilistic (tickets); not shortest-first.
- **Would be correct if:** the question asked about randomized fair-share scheduling.

#### Exam Trigger

- **"Shortest estimated execution time"** → **SJF/SRTF** (minimizes average waiting time)

#### Final Answer: **Shortest Job First (SJF)**

---

### Q85. Which parsing technique naturally handles left-recursive grammars without grammar transformation?

**Options:**
- [ ] Recursive Descent Parsing
- [ ] Predictive Parsing
- [x] **LR Parsing**
- [ ] LL(1) Parsing

#### Correct Answer: LR Parsing

**Why this is correct**

**LR parsing is bottom-up** (shift-reduce): it shifts tokens onto a **stack** and reduces handles when the top matches a production's RHS. Because decisions happen *after* consuming input, **left recursion causes no infinite loop** — unlike top-down parsers.

#### Core Concept

- Grammar `E → E + T | T` (left-recursive): LL(1) can't handle it; **LR can**, no transformation needed.
- LR(k): most powerful deterministic class; reads left-to-right, rightmost derivation.

#### Why the Other Options Are Incorrect

**1. Recursive Descent Parsing** — Top-down; a left-recursive rule makes it **call itself forever** (infinite recursion).
- **Would be correct if:** the question asked for a simple hand-written top-down parser for transformed grammars.

**2. Predictive Parsing** — Top-down table-driven (LL-like); requires **left-recursion elimination + left factoring**.
- **Would be correct if:** the grammar is already LL(1)-compatible.

**3. LL(1) Parsing** — Top-down; **cannot handle left recursion at all** (would loop).
- **Would be correct if:** the question asked which parsing requires grammar transformation for left recursion.

#### Exam Trigger

- **"Handles left recursion naturally"** → **LR parsing** (bottom-up)
- **"Infinite loop with left recursion"** → **LL/recursive descent** (top-down)

#### Final Answer: **LR Parsing**

---

### Q86. A compiler needs very fast average lookup for millions of identifiers; order is irrelevant. Best choice?

**Options:**
- [ ] Trie
- [ ] B+ Tree
- [ ] AVL Tree
- [x] **Hash Table**

#### Correct Answer: Hash Table

**Why this is correct**

- **"Order irrelevant"** rules out all tree structures (they exist to keep order).
- **Hash Table** gives **average O(1)** lookup — faster than the O(log n) of trees — and is the standard compiler symbol-table implementation.

#### Core Concept

- Symbol table: identifier → (type, scope, address).
- Hash: `hash(name) → bucket` → O(1) average insert/lookup.
- No need for ordered iteration → hash is optimal.

#### Why the Other Options Are Incorrect

**1. Trie** — Prefix tree over strings; good for prefix operations but heavier than a hash for exact lookup.
- **Would be correct if:** the question asked for prefix matching/autocomplete.

**2. B+ Tree** — Ordered + disk-optimized; overkill in memory and O(log n).
- **Would be correct if:** range scans or disk residency were required (Q57).

**3. AVL Tree** — Ordered with strict balance; O(log n) and ordered — the "order is irrelevant" phrase kills it.
- **Would be correct if:** sorted iteration or in-order traversal were needed.

#### Exam Trigger

- **"Order irrelevant, fast average lookup"** → **Hash Table**
- **"Ordered iteration needed"** → **AVL/B+ Tree**

#### Final Answer: **Hash Table**

---

### Q87. A key-value store adds and removes servers with minimal key movement. Which technique fits?

**Options:**
- [ ] Breadth-First Search
- [x] **Consistent Hashing**
- [ ] Dynamic Programming
- [ ] Huffman Coding

#### Correct Answer: Consistent Hashing

**Why this is correct**

**Consistent Hashing** places servers and keys on a **hash ring**. Adding/removing a server re-maps only **~K/n keys** (K = total keys, n = servers) instead of rehashing everything — the key requirement for distributed caches/stores (memcached, Dynamo).

#### Core Concept

```
Ring: keys & servers hashed to [0, 2^32)
Key → first server clockwise from its hash position
Server S dies → only keys between S and its predecessor move to next server
```
Remapping fraction = 1/n, not (n−1)/n.

#### Why the Other Options Are Incorrect

**1. Breadth-First Search** — Graph traversal; unrelated to data distribution.
- **Would be correct if:** unweighted shortest paths were asked (Q26).

**2. Dynamic Programming** — Optimization technique for overlapping subproblems (Q19).
- **Would be correct if:** the question described optimal-substructure problems.

**3. Huffman Coding** — Prefix-free **compression** codes by frequency.
- **Would be correct if:** the question asked for optimal lossless compression.

#### Exam Trigger

- **"Add/remove servers, minimal key movement"** → **Consistent Hashing** (ring, 1/n remap)

#### Final Answer: **Consistent Hashing**

---

### Q88. Demand paging causes high page faults and low CPU utilization. What should be done first?

**Options:**
- [ ] Increase Time Quantum
- [x] **Reduce Degree of Multiprogramming**
- [ ] Increase Interrupt Priority
- [ ] Disable Virtual Memory

#### Correct Answer: Reduce Degree of Multiprogramming

**Why this is correct**

High page faults + low CPU utilization = **thrashing**: too many processes compete for too few frames; the system spends all time paging. **Reducing the degree of multiprogramming** gives each process closer to its **working set** → faults drop → CPU utilization recovers.

#### Core Concept — The Thrashing Loop

```
Too many processes → each lacks frames → constant page faults → CPU idle → OS adds more processes → worse
Break: reduce concurrent processes → working sets fit → faults fall → CPU busy
```
Working-set model: sum of working sets must fit in available frames.

#### Why the Other Options Are Incorrect

**1. Increase Time Quantum** — CPU-scheduling knob; doesn't fix memory pressure.
- **Would be correct if:** the issue were excessive context switching from tiny quanta.

**2. Increase Interrupt Priority** — Changes interrupt handling; unrelated to page faults.
- **Would be correct if:** the question asked about interrupt latency.

**3. Disable Virtual Memory** — Drastic; programs larger than RAM simply won't run; doesn't fix overcommitment.
- **Would be correct if:** the question asked how to avoid paging overhead entirely (small workloads).

#### Exam Trigger

- **"High page faults + low CPU utilization"** → **Thrashing → reduce degree of multiprogramming** (Q88 is the fix; condition is Q88's scenario)

#### Final Answer: **Reduce Degree of Multiprogramming**

---

### Q89. Threads wait briefly for a very short critical section on multicore hardware. Which primitive is preferred?

**Options:**
- [ ] Counting Semaphore
- [ ] Mutex
- [ ] Condition Variable
- [x] **Spinlock**

#### Correct Answer: Spinlock

**Why this is correct**

For a **very short critical section** on **multicore**, a **spinlock** (busy-wait loop on an atomic flag) beats a sleeping mutex: the context switch + scheduler overhead of sleep/wake exceeds the time you'd wait. The waiting thread just spins a few cycles.

#### Core Concept

| Primitive | Behavior | Best for |
|-----------|----------|----------|
| Spinlock | Busy-wait until acquired | Very short CS, multicore |
| Mutex | Sleep if held (context switch) | Long CS, single/multicore |
| Condition variable | Wait until signaled | Event-driven waiting |
| Counting semaphore | N-resource limit | Producer-consumer |

#### Why the Other Options Are Incorrect

**1. Counting Semaphore** — Limits access to N identical resources; not about short critical sections.
- **Would be correct if:** the question asked to bound N consumers.

**2. Mutex** — Blocks (sleeps) the thread → **kernel context switch**, which costs more than the tiny wait itself.
- **Would be correct if:** the critical section were long or contended heavily.

**3. Condition Variable** — Requires mutex + wait/signal; for *event-driven* waiting, not short mutual exclusion.
- **Would be correct if:** the question asked how threads wait for a condition/event.

#### Exam Trigger

- **"Very short critical section, multicore"** → **Spinlock**
- **"Long critical section"** → **Mutex**

#### Final Answer: **Spinlock**

---

### Q90. High-priority tasks keep running while low-priority processes wait indefinitely. What issue is this?

**Options:**
- [x] **Starvation**
- [ ] Deadlock
- [ ] Thrashing
- [ ] Fragmentation

#### Correct Answer: Starvation

**Why this is correct**

**Starvation** = a process waits **indefinitely** while higher-priority processes keep arriving — one-sided blocking, *not* circular. Fix: **aging** (progressively raise priority of waiting processes).

#### Core Concept

| Issue | Nature |
|-------|--------|
| Starvation | Indefinite one-sided wait (low-priority never scheduled) |
| Deadlock | **Circular** mutual wait (Q38) |
| Thrashing | Memory overcommit → constant paging (Q88) |

#### Why the Other Options Are Incorrect

**1. Deadlock** — Requires a **cycle** (P1 waits for P2, P2 waits for P1). Here high-priority tasks don't wait for anything — no cycle.
- **Would be correct if:** processes waited on each other in a circle (Q38).

**2. Thrashing** — Memory-pressure phenomenon (high page faults, low CPU).
- **Would be correct if:** the question mentioned paging/swapping (Q88).

**3. Fragmentation** — Memory layout problem (internal/external).
- **Would be correct if:** the question mentioned wasted/scattered memory (Q6).

#### Exam Trigger

- **"Low-priority waits indefinitely (not circular)"** → **Starvation** (fix: aging)
- **"Circular waiting"** → **Deadlock**

#### Final Answer: **Starvation**

---
## 📘 Part 10 (cbt1_091 – cbt1_100): Idempotency, Cloud & Distributed Systems

### Q91. Retries after network failures must not duplicate transaction effects. Which property is required?

**Options:**
- [ ] Atomicity
- [ ] Durability
- [x] **Idempotency**
- [ ] Mutual Exclusion

#### Correct Answer: Idempotency

**Why this is correct**

**Idempotency**: applying an operation **multiple times** yields the **same result as once** — `f(f(x)) = f(x)`. If a request times out and is retried, an idempotent operation does **not duplicate effects** (e.g., same debit recorded once, not twice).

#### Core Concept

- **Idempotent HTTP**: GET, PUT, DELETE (repeating safe); POST is NOT idempotent (creates duplicates).
- APIs use **idempotency keys**: client sends a unique key; server ignores retries carrying the same key.
- Example: charging a card — retry with same request ID → single charge.

#### Why the Other Options Are Incorrect

**1. Atomicity** — All-or-nothing within one transaction; doesn't handle *repeated* executions.
- **Would be correct if:** the question was about partial failure/rollback of one transaction (Q17).

**2. Durability** — Committed data survives crashes.
- **Would be correct if:** the question asked about persistence after power loss.

**3. Mutual Exclusion** — One process at a time in a critical section.
- **Would be correct if:** the question asked about preventing concurrent access (Q78).

#### Exam Trigger

- **"Retries must not duplicate effects"** → **Idempotency**
- **"POST vs PUT/DELETE"** → POST is non-idempotent

#### Final Answer: **Idempotency**

---

### Q92. A small working set still causes cache misses due to competing blocks mapping together. Which miss is this?

**Options:**
- [ ] Cold Miss
- [ ] Coherence Miss
- [x] **Conflict Miss**
- [ ] Capacity Miss

#### Correct Answer: Conflict Miss

**Why this is correct**

**Conflict misses** happen when multiple addresses **map to the same cache set/line** (direct-mapped or set-associative) and evict each other — **even if the working set is small**. The small working set is the discriminator: capacity miss would require the working set to be *too large* for the cache.

#### Core Concept — The 3 C's

| Miss type | Cause |
|-----------|-------|
| Compulsory (cold) | First access to a block |
| Conflict | Addresses collide in the same set (mapping) |
| Capacity | Working set exceeds cache size |

#### Example

Working set of 8 blocks, cache 64 blocks, direct-mapped: if all 8 blocks hash to the **same set**, every access misses → conflict misses despite tiny working set. Fix: higher associativity.

#### Why the Other Options Are Incorrect

**1. Cold Miss** — First-ever access to a block; no "competing blocks" involved.
- **Would be correct if:** the question mentioned the first reference to data.

**2. Coherence Miss** — Another core invalidated the line (shared-memory updates).
- **Would be correct if:** the question involved multi-core invalidation (Q99).

**3. Capacity Miss** — Working set **bigger than the cache**. Here the working set is small → wrong by definition.
- **Would be correct if:** the question said "working set exceeds cache capacity."

#### Exam Trigger

- **"Small working set, still misses due to same-set mapping"** → **Conflict Miss**
- **"Working set too big"** → **Capacity Miss**; **"first access"** → **Cold Miss**

#### Final Answer: **Conflict Miss**

---

### Q93. A campus network must tolerate a single link failure without isolating other sites. Which topology fits best?

**Options:**
- [x] **Mesh Topology**
- [ ] Ring Topology
- [ ] Linear Daisy Chain
- [ ] Bus Topology

#### Correct Answer: Mesh Topology

**Why this is correct**

A **Mesh** provides **redundant paths** between nodes. If one link fails, traffic reroutes through alternate paths — **no site is isolated**. It's the standard choice for fault-tolerant backbone/enterprise networks.

#### Core Concept

| Topology | Single link failure | Notes |
|----------|--------------------|-------|
| Full/partial mesh | Survives (alt paths) | Redundant, costlier cabling |
| Ring | Breaks (unless dual ring) | Single cut = split |
| Linear daisy chain | Isolates downstream | No redundancy |
| Bus | Splits/terminates network | Single point of failure |

#### Why the Other Options Are Incorrect

**1. Ring Topology** — Data flows one direction; one broken link splits the ring → sites on each side can't talk.
- **Would be correct if:** the question asked for a simple low-cost loop (with dual-ring caveat).

**2. Linear Daisy Chain** — Devices in series; one failed link isolates everything downstream.
- **Would be correct if:** the question asked for a simple linear chain of devices.

**3. Bus Topology** — Shared single backbone; a break terminates/divides the network.
- **Would be correct if:** the question asked for the cheapest legacy layout for a few machines.

#### Exam Trigger

- **"Tolerate single link failure"** → **Mesh** (redundant paths)

#### Final Answer: **Mesh Topology**

---

### Q94. A variable is used before declaration, but syntax is valid. Which phase reports it?

**Options:**
- [ ] Code Optimization
- [ ] Lexical Analysis
- [x] **Semantic Analysis**
- [ ] Syntax Analysis

#### Correct Answer: Semantic Analysis

**Why this is correct**

The statement **parses fine** (syntax OK) — the problem is **meaning/scope**: the variable isn't declared. **Semantic Analysis** checks declarations, scopes, and types via the **symbol table** and reports "undeclared variable".

#### Core Concept — Phase Roles

| Phase | Checks | Example error |
|-------|--------|----------------|
| Lexical | Token formation | Illegal character |
| Syntax | Grammar/structure | Missing semicolon |
| Semantic | Meaning/scope/types | **Undeclared variable**, type mismatch |
| Optimization | Code improvement | (no errors) |

#### Example

```c
x = y + 1;   /* y never declared — parses OK, semantic error */
```
The parser builds a valid tree; semantic analysis flags `y`.

#### Why the Other Options Are Incorrect

**1. Code Optimization** — Runs *after* semantic analysis; improves code, doesn't report declarations.
- **Would be correct if:** the question asked about performance improvements (Q96/Q97).

**2. Lexical Analysis** — Only forms tokens from characters; no scope knowledge.
- **Would be correct if:** the problem were an illegal character/lexeme (Q69).

**3. Syntax Analysis** — Builds parse tree per grammar; the statement *is* syntactically valid here.
- **Would be correct if:** the question involved a grammar violation (Q98).

#### Exam Trigger

- **"Syntax valid, but a meaning/declaration/scope problem"** → **Semantic Analysis**

#### Final Answer: **Semantic Analysis**

---

### Q95. Distributed processes lack synchronized clocks. Which mechanism captures causal event ordering?

**Options:**
- [x] **Vector Clocks**
- [ ] CRC Checksum
- [ ] Checkpointing
- [ ] Consistent Hashing

#### Correct Answer: Vector Clocks

**Why this is correct**

**Vector Clocks** maintain a **per-node logical-clock vector**; comparing vectors determines **causal ordering ("happened-before")** without synchronized physical clocks — exactly what distributed systems need for causality (used in Dynamo, etc.).

#### Core Concept

- Each process keeps a vector `[t₁, t₂, ..., tₙ]`.
- Local event: increment own entry. Send: piggyback vector. Receive: element-wise max + increment own.
- Compare: V1 ≤ V2 (all entries) → V1 happened-before V2. Incomparable → concurrent.

#### Example

P1 increments to [1,0], sends to P2; P2 becomes [1,1]. Any event with [0,1] at P2 is concurrent to P1's [1,0] — distinguishable without wall clocks.

#### Why the Other Options Are Incorrect

**1. CRC Checksum** — Error detection for data transmission; no ordering semantics.
- **Would be correct if:** the question asked how to detect bit errors.

**2. Checkpointing** — Periodic state saving for fault recovery.
- **Would be correct if:** the question asked how to recover after a node crash.

**3. Consistent Hashing** — Data distribution across servers (Q87).
- **Would be correct if:** the question asked about key placement with minimal rehashing.

#### Exam Trigger

- **"No synchronized clocks, causal ordering"** → **Vector Clocks**
- **"Leader election"** → **Raft** (Q67); **"atomic commit"** → **2PC** (Q4) — three different primitives, don't mix

#### Final Answer: **Vector Clocks**

---

### Q96. A compiler needs machine-independent code for optimization before target generation. What is used?

**Options:**
- [x] **Intermediate Representation (IR)**
- [ ] Symbol Table
- [ ] Parse Tree
- [ ] Object Code

#### Correct Answer: Intermediate Representation (IR)

**Why this is correct**

The **IR** is the machine-independent representation (three-address code, LLVM IR) that the **middle-end optimizes** before the back-end generates target code. Optimizations run once on IR and benefit all targets.

#### Core Concept — Compiler Pipeline

```
Source → Front-End → IR → Optimizer → IR → Back-End → Target code
                      (machine-independent)         (machine-specific)
```

#### Why the Other Options Are Incorrect

**1. Symbol Table** — Bookkeeping of identifiers/types; not an executable representation to optimize.
- **Would be correct if:** the question asked where names/types are recorded.

**2. Parse Tree** — Syntax structure of the *source*; still source-level, not optimized.
- **Would be correct if:** the question asked about the syntax/semantic front-end output (Q69).

**3. Object Code** — Final machine code; already target-specific — too late for generic optimization.
- **Would be correct if:** the question asked about the back-end output (linking-ready binaries).

#### Exam Trigger

- **"Machine-independent, pre-target optimization"** → **IR**

#### Final Answer: **Intermediate Representation (IR)**

---

### Q97. A compiler removes code unreachable by control flow. Which optimization is used?

**Options:**
- [ ] Strength Reduction
- [x] **Dead Code Elimination**
- [ ] Loop Fusion
- [ ] Constant Folding

#### Correct Answer: Dead Code Elimination

**Why this is correct**

**Dead Code Elimination (DCE)** removes:
- **Unreachable code** — no control path reaches it (e.g., after an unconditional `return`)
- **Unused computations** — results never used

Shrinks binary, reduces execution time.

#### Core Concept

```c
int f(int x) {
  if (x > 0) return 1;
  else return 0;
  int y = x * 2;   /* unreachable — after return — DCE removes it */
  return y;
}
```

#### Why the Other Options Are Incorrect

**1. Strength Reduction** — Replaces expensive ops with cheaper ones (shift for multiply) — Q29.
- **Would be correct if:** the question asked to replace `x*8` with `x<<3`.

**2. Loop Fusion** — Merges two adjacent loops into one to reuse cache/loop overhead.
- **Would be correct if:** the question asked about combining loops that traverse the same data.

**3. Constant Folding** — Evaluates constant expressions at compile time (`2*3` → `6`).
- **Would be correct if:** the question asked about compile-time constant arithmetic.

#### Exam Trigger

- **"Removes unreachable/unused code"** → **Dead Code Elimination**
- **"Repeated same expression"** → **CSE** (Q5) — CSE removes *repeated computation of a used value*; DCE removes *unused/unreachable code*

#### Final Answer: **Dead Code Elimination**

---

### Q98. A compiler accepts syntactically invalid programs because its grammar is overly permissive. Which should be corrected first?

**Options:**
- [ ] Tokenizer
- [x] **Grammar specification**
- [ ] Parser lookahead
- [ ] Register allocation

#### Correct Answer: Grammar specification

**Why this is correct**

The **grammar defines the language's syntax** — what's valid/invalid. If invalid programs parse, the **grammar itself is wrong** (too loose). Fix the grammar specification first; tokenizer and lookahead are not the root cause.

#### Core Concept

```
Grammar too loose: accepts `if (x == ) { }` or `a b c = ;`
Fix: tighten productions (expression/statement rules) so invalid forms fail parsing.
```

#### Why the Other Options Are Incorrect

**1. Tokenizer** — Only splits characters into tokens; can't decide program validity.
- **Would be correct if:** the issue were wrong tokens (bad lexemes) — Q69.

**2. Parser lookahead** — Affects *which* deterministic parser fits (LL(k)/LR(k)) but doesn't change accepted *language*.
- **Would be correct if:** the question asked about LL(1)/LR(1) conflicts (Q85).

**3. Register allocation** — Back-end concern; runs after parsing, can't cause invalid programs to be accepted.
- **Would be correct if:** the question asked about variable placement in registers (spilling).

#### Exam Trigger

- **"Accepts invalid syntax, grammar too loose"** → **Fix grammar specification**

#### Final Answer: **Grammar specification**

---

### Q99. One core updates a shared cache line; other cores must see the latest value. What ensures this?

**Options:**
- [ ] Speculative Execution
- [ ] Instruction Pipelining
- [x] **Cache Coherence Protocol**
- [ ] Virtual Memory

#### Correct Answer: Cache Coherence Protocol

**Why this is correct**

A **cache coherence protocol** (MESI, MOESI, MSI) keeps all cores' caches consistent: when one core writes a shared line, the protocol **invalidates/updates copies** in other cores so every core reads the latest value.

#### Core Concept — MESI States

| State | Meaning |
|-------|---------|
| M (Modified) | Dirty in this cache only |
| E (Exclusive) | Clean, this cache only |
| S (Shared) | Clean, multiple caches |
| I (Invalid) | Stale — must fetch |

Writer asks for ownership → others set I → their next read fetches the fresh line.

#### Why the Other Options Are Incorrect

**1. Speculative Execution** — Executes instructions ahead of control decisions; doesn't manage cache consistency.
- **Would be correct if:** the question asked about branch speculation.

**2. Instruction Pipelining** — Overlaps instruction stages in one core.
- **Would be correct if:** the question asked about single-core throughput.

**3. Virtual Memory** — Address translation (page tables); unrelated to multi-core cache consistency.
- **Would be correct if:** the question asked about swapping/address mapping (Q8).

#### Exam Trigger

- **"Cores must see latest shared value"** → **Cache Coherence Protocol** (MESI/MOESI)

#### Final Answer: **Cache Coherence Protocol**

---

### Q100. A web application experiences sudden traffic spikes. The IT team wants to automatically add servers during peak load and remove them during low usage. Which cloud concept enables this?

**Options:**
- [ ] Serverless Computing
- [ ] Virtual Private Cloud
- [x] **Elastic Scaling**
- [ ] Container Orchestration

#### Correct Answer: Elastic Scaling

**Why this is correct**

**Elastic Scaling** (auto-scaling) automatically **provisions servers as load rises and de-provisions them as load falls**, based on metrics (CPU, request rate). Exactly the add/remove-with-traffic requirement.

#### Core Concept

```
Load ↑ → metric crosses threshold → scale-out (add instances)
Load ↓ → metric drops → scale-in (remove instances)
```
The cloud pays for what's running → cost efficiency + capacity on demand.

#### Why the Other Options Are Incorrect

**1. Serverless Computing** — Runs functions on demand without managing servers *at all*; a different model (no scaling knob needed, but the question asks about adding/removing servers).
- **Would be correct if:** the question asked about zero server management (AWS Lambda, Azure Functions).

**2. Virtual Private Cloud** — Isolated virtual network segment (subnets, security).
- **Would be correct if:** the question asked about isolated networking within the cloud.

**3. Container Orchestration** — Manages container lifecycle/deployment (Kubernetes) — it *can* auto-scale, but "automatically add/remove servers with load" is the definition of elastic scaling itself.
- **Would be correct if:** the question asked about deploying/managing containers across nodes.

#### Exam Trigger

- **"Auto add/remove servers with load"** → **Elastic Scaling**

#### Final Answer: **Elastic Scaling**

---

## 🎯 Master Discrimination Index (all 100 questions, grouped by trap-pair)

Use this as your final 10-minute sweep — these are the pairs CBT 2 is most likely to test against each other:

1. WHERE vs HAVING (Q9)
2. External Fragmentation vs Internal Fragmentation vs Compaction (Q6/Q18)
3. 2PC vs Raft vs Vector Clocks (Q4/Q67/Q95)
4. Deadlock vs Starvation vs Thrashing (Q38/Q90/Q88)
5. AVL (in-memory) vs B+ Tree (disk) vs Red-Black (Q42/Q57)
6. Dijkstra (non-neg) vs Bellman-Ford (neg edges) vs BFS (unweighted) (Q13/Q46/Q26)
7. CFG vs PDA vs DFA (nesting vs no nesting) (Q30/Q63/Q79)
8. CSE vs Dead Code Elimination vs Strength Reduction (Q5/Q97/Q29)
9. Lexical vs Syntax vs Semantic Analysis (Q69/Q94)
10. Conflict Miss vs Capacity Miss vs Cold Miss (Q92)
11. Approximation (guaranteed) vs Heuristic (no guarantee) (Q43/Q82)
12. Spinlock (short CS, multicore) vs Mutex (Q89)
13. Multithreading benefit ≠ "no sync needed" (Q23)
14. DNS vs DHCP vs ARP (Q3/Q20)
15. RESTful (nouns+HTTP verbs) vs RPC (verbs in endpoint) (Q80)
16. SJF (min avg waiting) vs RR vs FCFS (Q84/Q21)
17. LR (handles left recursion) vs LL/Recursive Descent (Q85)
18. UNIQUE (NULLs OK) vs PRIMARY KEY vs NOT NULL (Q15/Q32)
19. Idempotency (retries) vs Atomicity (rollback) vs Durability (Q91/Q17)
20. Starvation (one-sided) vs Deadlock (circular) (Q90/Q38)

---
