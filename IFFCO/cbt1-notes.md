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

---