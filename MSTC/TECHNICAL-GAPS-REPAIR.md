# Technical Gaps Repair Sheet

> From: Mock Interview 1 (19 May 2026, 7 PM)
> Technical score: 40% — 8 gaps identified
> Each gap has a 40-second script + key points for rapid fire
> Read this BEFORE every mock and before the final interview

---

## GAP 1 — IS Clause in DBMS ❌ (could not explain)

**What IS clause is:** In DBMS context, this likely referred to `IS NULL` and `IS NOT NULL`.

**The Rule:**

> `NULL = NULL` is NOT TRUE in SQL — it returns UNKNOWN. You must use `IS NULL`.

**Wrong:**

```sql
WHERE col = NULL    -- always returns 0 rows
WHERE col != NULL   -- always returns 0 rows
```

**Correct:**

```sql
WHERE col IS NULL
WHERE col IS NOT NULL
```

**Why:** SQL uses 3-valued logic: TRUE / FALSE / UNKNOWN. Any comparison with NULL → UNKNOWN → row dropped by WHERE.

**40s Script:**

> *"In SQL, you cannot use = or != to check for NULL because NULL represents absence of value, not a value itself. Any comparison with NULL returns UNKNOWN — not TRUE. The IS NULL operator was specifically designed for this. So we use WHERE col IS NULL to find rows where a column has no value."*

---

## GAP 2 — PK vs UK ❌ (confused them)

**The Key Differences:**


| Feature      | Primary Key | Unique Key            |
| ------------ | ----------- | --------------------- |
| Uniqueness   | ✅ Enforced  | ✅ Enforced            |
| NULL allowed | ❌ NEVER     | ✅ ONE null per column |
| Per table    | Only ONE PK | MULTIPLE UKs allowed  |
| Index type   | Clustered   | Non-clustered         |


**40s Script:**

> *"Both Primary Key and Unique Key enforce uniqueness — no duplicates allowed. The difference: a Primary Key cannot be NULL under any circumstance, while a Unique Key allows one NULL. A table can have only one Primary Key, but can have multiple Unique Keys. Primary Key creates a clustered index, Unique Key creates a non-clustered index. Think of Unique Key as a backup identifier that's slightly more relaxed than the primary."*

---

## GAP 3 — Technical Definition of Operating System ❌ (gave informal definition)

**Technical Definition:**

> *"An Operating System is system software that acts as an interface between computer hardware and the user. It manages and controls all hardware resources — CPU, memory, disk drives, and I/O devices. It takes instructions from the user, directs the CPU to execute them, and manages the flow of data, instructions, and information within the system."*

**OS Functions (quick list):**
Memory Management, Process Management, File Management, Device Management, Security, Networking, Communication, Job Accounting, Secondary Storage, Command Interpretation

**40s Script:**

> *"An OS is system software that interfaces between hardware and user. It manages CPU scheduling, memory allocation, file systems, and I/O devices. Users interact via GUI or CLI — the OS translates those into hardware instructions. Without an OS, no application can run. Examples: Windows, Linux, Android."*

---

## GAP 4 — Eigenvalues ❌ (not covered)

**What is an Eigenvalue:**

For a square matrix A, if `Av = λv` where:

- v = non-zero vector (eigenvector)
- λ = scalar (eigenvalue)

Then λ is an eigenvalue of matrix A.

**How to find eigenvalues:**
Solve: `det(A - λI) = 0` (characteristic equation)

**Example:** For matrix A = [[4, 1], [2, 3]]:

- `det([[4-λ, 1], [2, 3-λ]]) = 0`
- `(4-λ)(3-λ) - 2 = 0`
- `λ² - 7λ + 10 = 0`
- `λ = 5` or `λ = 2`

**Properties:**

- Sum of eigenvalues = Trace of matrix (sum of diagonal)
- Product of eigenvalues = Determinant of matrix

**40s Script:**

> *"An eigenvalue λ of a matrix A is a scalar such that Av = λv — multiplying the matrix by its eigenvector v just scales the vector, it doesn't rotate it. To find eigenvalues, we solve the characteristic equation det(A - λI) = 0. For a 2×2 matrix this gives a quadratic. The sum of eigenvalues equals the trace, and the product equals the determinant."*

---

## GAP 5 — Multiplexer ❌ (not covered)

**What is a Multiplexer (MUX):**

A **combinational circuit** that selects one of several input signals and forwards it to a single output line based on select lines.

- n select lines → 2ⁿ input lines → 1 output
- Also called **Data Selector**

**2-to-1 MUX:**

```
I0 ──┐
     │──[MUX]── Output
I1 ──┘
      ↑
      S (select)
If S=0: Output = I0
If S=1: Output = I1
```

**4-to-1 MUX:** 4 inputs, 2 select lines (S1, S0)

**Truth Table (4-to-1):**


| S1  | S0  | Output |
| --- | --- | ------ |
| 0   | 0   | I0     |
| 0   | 1   | I1     |
| 1   | 0   | I2     |
| 1   | 1   | I3     |


**Boolean Expression:** `Y = S1'S0'I0 + S1'S0I1 + S1S0'I2 + S1S0I3`

**Applications:** Data routing, frequency selection, communication systems

**40s Script:**

> *"A Multiplexer is a combinational circuit that selects one of multiple input signals and routes it to a single output based on select lines. With n select lines, it can handle 2ⁿ inputs. It's essentially a data selector — used in data routing, communication systems, and implementing Boolean functions. The complement is a Demultiplexer which does the reverse — one input to multiple outputs."*

---

## GAP 6 — HAVING Clause ❌ (could not explain why we use it)

**The Rule:**

- `WHERE` → filters **rows** BEFORE `GROUP BY` — cannot use aggregate functions
- `HAVING` → filters **groups** AFTER aggregation — aggregate functions allowed

**Execution Order:**

```
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

**Wrong:**

```sql
SELECT dept_id, COUNT(*)
FROM employees
WHERE COUNT(*) > 5    -- ❌ ERROR: aggregate not allowed in WHERE
GROUP BY dept_id;
```

**Correct:**

```sql
SELECT dept_id, COUNT(*) AS headcount
FROM employees
WHERE active = true          -- filters rows BEFORE grouping
GROUP BY dept_id
HAVING COUNT(*) > 5;         -- filters GROUPS after aggregation
```

**40s Script:**

> *"HAVING is used to filter groups after aggregation — WHERE can't do this because WHERE runs before GROUP BY and doesn't have access to aggregate results. We use HAVING when we want conditions on things like COUNT, SUM, or AVG. Example: WHERE filters out inactive employees first, then GROUP BY creates department groups, then HAVING COUNT > 5 keeps only large departments."*

---

## GAP 7 — IPv4 vs IPv6 ❌ (not covered)


| Feature          | IPv4                                       | IPv6                                       |
| ---------------- | ------------------------------------------ | ------------------------------------------ |
| Address size     | **32-bit**                                 | **128-bit**                                |
| Address notation | Dotted decimal: `192.168.1.1`              | Hexadecimal: `2001:0db8::1`                |
| Total addresses  | ~4.3 billion (2³²)                         | ~340 undecillion (2¹²⁸)                    |
| Header size      | 20-60 bytes                                | Fixed 40 bytes                             |
| Configuration    | Manual / DHCP                              | Auto-configuration (SLAAC)                 |
| NAT required?    | ✅ Yes (address shortage)                   | ❌ No (enough addresses)                    |
| Security (IPSec) | Optional                                   | Built-in mandatory                         |
| Checksum         | ✅ Has checksum field                       | ❌ No checksum (handled by transport layer) |
| Fragmentation    | By routers and hosts                       | By source host only                        |
| Broadcast        | ✅ Has broadcast                            | ❌ Uses multicast instead                   |
| Speed            | Slightly faster routing (mature ecosystem) | More efficient header processing           |


**Why we need IPv6:**

> IPv4 is exhausted — only ~4.3 billion addresses, not enough for all devices. IPv6 provides virtually unlimited addresses.

**40s Script:**

> *"IPv4 uses 32-bit addresses in dotted decimal format like 192.168.1.1, giving about 4.3 billion addresses which are now exhausted. IPv6 uses 128-bit addresses in hexadecimal, providing 2¹²⁸ addresses — effectively unlimited. IPv6 has a fixed 40-byte header for faster processing, has IPSec built-in for security, doesn't need NAT, and uses multicast instead of broadcast. The main driver for IPv6 is address space exhaustion in IPv4."*

---

## GAP 8 — Dijkstra Algorithm (gave WRONG explanation) ❌

**What you said wrong:** "Dijkstra does not work on directed graphs"

**CORRECT FACTS:**

- ✅ Dijkstra works on **both directed AND undirected** graphs
- ❌ The only restriction: **no negative edge weights (use** Bellman-Ford algorithm**)**
- Time complexity: O(E log V) with min-heap
- Application: Google Maps, GPS routing

**Algorithm in 3 lines:**

1. Initialize d[source] = 0, d[all others] = ∞
2. Extract vertex u with minimum distance. Relax all outgoing edges.
3. If d[u] + w(u,v) < d[v], update d[v]. Repeat until all vertices processed.

**Edge relaxation:** `if d[u] + w(u,v) < d[v]: d[v] = d[u] + w(u,v)`

**40s Script:**

> *"Dijkstra is a greedy algorithm for single-source shortest paths in weighted graphs. It works on BOTH directed and undirected graphs — the only restriction is no negative edge weights. We maintain a priority queue of unvisited vertices, always extracting the one with minimum current distance, then relaxing its neighbors. If a shorter path is found, we update the distance. Time complexity is O(E log V) with a min-heap. The classic application is Google Maps routing."*

---

## QUICK DRILL — Say Each Answer Aloud (30 seconds each)

1. What is `IS NULL` and why can't you use `= NULL`?
2. PK vs UK — three key differences
3. Technical definition of OS in one sentence
4. What is an eigenvalue? How do you find it?
5. What is a multiplexer and when do you use it?
6. WHERE vs HAVING — one sentence + one example
7. IPv4 vs IPv6 — address size + one key difference
8. Dijkstra — works on directed? Any restriction?

> ⏱️ Target: 30 seconds per answer, cold, no notes.
> If you hesitate > 5 seconds on any: re-read that gap and drill again.

---

## CONFIDENCE RECOVERY NOTE

> If you get a question wrong in the interview: **don't let it cascade.**
>
> Strategy: "That's a good question. Let me think — [pause 3 seconds] — 
> I'm not fully confident on that specific point, but here's what I know..."
>
> One wrong answer does not fail an interview. Confidence collapse after one wrong answer does.
> Move on immediately. The next question is a fresh start.

