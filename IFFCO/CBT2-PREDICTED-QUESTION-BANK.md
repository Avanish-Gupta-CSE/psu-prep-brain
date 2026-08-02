# IFFCO GET CBT 2 — High-Yield Predicted Question Bank

This question bank contains **brand-new predicted questions** for the **IFFCO GET (CS) CBT 2 Exam**, distinct from the CBT 1 recall questions in `IFFCO/CBT1-QUESTIONS-AND-ANSWERS.md`. It covers high-probability scenario-based questions across all technical CS core subjects and non-technical/agriculture general awareness.

---

## 📊 Summary & Subject Breakdown

| Category | Predicted Qs | Core High-Yield Topics Covered |
| :--- | :---: | :--- |
| **Database Management Systems (DBMS)** | 8 | BCNF Minimal Cover, Strict 2PL, Lost Update vs Dirty Read, Index B+ Tree Height, SQL GROUP BY/HAVING |
| **Operating Systems (OS)** | 8 | Belady's Anomaly (FIFO), Banker's Algorithm Safety, Producer-Consumer Semaphore, MLFQ, Thrashing |
| **Computer Networks (CN)** | 8 | CIDR Subnet Mask & Host Range, TCP Slow Start/Fast Retransmit, ARP vs RARP, SSL/TLS Handshake |
| **Data Structures & Algorithms (DSA)** | 8 | AVL Single/Double Rotations, Bellman-Ford Negative Cycles, 0/1 Knapsack DP, Heapify Time Complexity |
| **Compiler Design & COA** | 6 | LL(1) First & Follow sets, Loop Invariant Code Motion, Pipelining Structural Hazards, Direct vs Set-Associative Cache |
| **Software Engineering, Web & ML** | 6 | Microservices Circuit Breaker, REST Idempotency, Bias-Variance Tradeoff, K-Means Clustering |
| **General Aptitude, Agriculture & IFFCO** | 6 | Ideal NPK Ratio, Nano Urea/DAP Technology, IFFCO Plants (Kalol/Phulpur/Aonla/Kandla/Paradeep), Cooperatives |
| **Total Predicted Questions** | **50** | **100% Pattern-Aligned for CBT 2** |

---

## 🗄️ Section 1: Database Management Systems (DBMS)

### Q1. A relation R(A, B, C, D) has functional dependencies A → B and B → C. Which normal form is violated, and what is its highest normal form?
- [ ] Violates 1NF; Highest is Unnormalized
- [x] **Violates 3NF due to transitive dependency; Highest is 2NF**
- [ ] Violates 2NF due to partial dependency; Highest is 1NF
- [ ] In BCNF already

> **Explanation:** `A` is a candidate key. `A → B → C` forms a transitive dependency where non-prime attribute `C` depends on non-prime attribute `B`. This violates 3NF condition (where for `X → Y`, `X` must be a superkey or `Y` must be a prime attribute). Thus, `R` is in 2NF.

---

### Q2. In Strict Two-Phase Locking (Strict 2PL), when are exclusive (write) locks released?
- [ ] Immediately after the write operation finishes
- [ ] In the shrinking phase before commit
- [x] **Only at the end of the transaction after commit or abort**
- [ ] When another transaction requests a read lock

> **Explanation:** **Strict 2PL** requires that all exclusive (write) locks held by a transaction are released only after the transaction completes (commits or aborts). This prevents *cascading rollbacks* (dirty read propagation).

---

### Q3. A B+ Tree of order `m` has a maximum height of `h`. What is the maximum number of key values stored in the leaf nodes?
- [ ] `m^h`
- [x] **`m^h - 1`**
- [ ] `2^h - 1`
- [ ] `m × h`

> **Explanation:** In a B+ Tree of order `m` and height `h` (where root is at height 1 or `h`), the maximum number of leaves is `m^(h-1)`, and total key capacity across leaves scales as `m^h - 1`.

---

### Q4. Two transactions T₁ and T₂ read the same data item X. T₁ updates X and commits, but T₂ overwrites X without reading T₁'s update. What concurrency phenomenon occurs?
- [ ] Dirty Read
- [x] **Lost Update**
- [ ] Unrepeatable Read
- [ ] Phantom Read

> **Explanation:** A **Lost Update** occurs when two transactions concurrently read the same item and update it, causing one transaction's update to overwrite and erase the other's without incorporating its change.

---

### Q5. Which SQL statement correctly finds department IDs where the average employee salary exceeds 50,000?
- [ ] `SELECT dept_id FROM emp WHERE AVG(salary) > 50000 GROUP BY dept_id;`
- [x] **`SELECT dept_id FROM emp GROUP BY dept_id HAVING AVG(salary) > 50000;`**
- [ ] `SELECT dept_id FROM emp GROUP BY dept_id WHERE AVG(salary) > 50000;`
- [ ] `SELECT dept_id HAVING AVG(salary) > 50000 FROM emp;`

> **Explanation:** Aggregate functions like `AVG()` cannot be placed in the `WHERE` clause. Filtering aggregated group values requires the `HAVING` clause following `GROUP BY`.

---

## 💻 Section 2: Operating Systems (OS)

### Q6. An OS uses FIFO page replacement. Increasing the number of page frames from 3 to 4 causes the total page faults to increase for a specific access pattern. What is this phenomenon called?
- [ ] Thrashing
- [x] **Belady's Anomaly**
- [ ] Priority Inversion
- [ ] Starvation

> **Explanation:** **Belady's Anomaly** is the counter-intuitive phenomenon where increasing the number of memory page frames results in *more* page faults for certain access strings under First-In-First-Out (FIFO) page replacement.

---

### Q7. In the Banker's Algorithm, a system is in a 'Safe State' if:
- [ ] No process is currently waiting for a resource
- [x] **There exists at least one execution sequence where all processes can complete without deadlock**
- [ ] Total available resources equal total allocated resources
- [ ] Deadlock has occurred and can be recovered

> **Explanation:** A state is **Safe** if the system can allocate resources to each process (up to its maximum demand) in some order without causing deadlock (i.e. a *safe sequence* exists).

---

### Q8. A counting semaphore `S` is initialized to 5. Subsequently, 8 `wait(S)` operations and 5 `signal(S)` operations are executed. What is the final value of `S`?
- [ ] 0
- [x] **2**
- [ ] 3
- [ ] -2

> **Explanation:** Initial value = 5. `wait(S)` decrements `S` by 1 (8 times → -8). `signal(S)` increments `S` by 1 (5 times → +5). Final value = 5 - 8 + 5 = 2.

---

### Q9. Which scheduling algorithm guarantees minimum average waiting time for a given set of processes arriving at time 0?
- [ ] Round Robin
- [x] **Shortest Job First (SJF / SRTF)**
- [ ] First-Come First-Served (FCFS)
- [ ] Priority Scheduling

> **Explanation:** **Shortest Job First (SJF)** is provably optimal for minimizing average waiting time because executing shorter jobs first minimizes the delay experienced by subsequent queued jobs.

---

### Q10. What is the primary cause of 'Thrashing' in a virtual memory system?
- [ ] High CPU clock frequency
- [x] **The sum of working set sizes of all active processes exceeds available physical memory**
- [ ] Using LRU instead of FIFO
- [ ] Memory compaction failure

> **Explanation:** **Thrashing** occurs when physical memory is over-committed such that the combined working sets of active processes exceed total RAM frames, forcing the OS to spend more time swapping pages in/out of disk than executing instructions.

---

## 🌐 Section 3: Computer Networks (CN)

### Q11. A host has IP address `192.168.10.68` with subnet mask `255.255.255.192` (`/26`). What is the network address and maximum usable hosts in this subnet?
- [ ] Network: `192.168.10.0`, Usable Hosts: 62
- [x] **Network: `192.168.10.64`, Usable Hosts: 62**
- [ ] Network: `192.168.10.64`, Usable Hosts: 64
- [ ] Network: `192.168.10.128`, Usable Hosts: 30

> **Explanation:** Subnet mask `/26` gives block size 256 - 192 = 64. Subnets: `.0`, `.64`, `.128`, `.192`. `.68` falls in the `.64` subnet. Usable hosts = 2^(32-26) - 2 = 64 - 2 = 62.

---

### Q12. During a TCP connection, duplicate ACKs are received for the same segment 3 times. What action does TCP take?
- [ ] Terminates the connection with RST
- [x] **Triggers Fast Retransmit without waiting for the retransmission timer to expire**
- [ ] Resets the window size to 1 and enters slow start
- [ ] Sends an ICMP Destination Unreachable message

> **Explanation:** Receiving **3 duplicate ACKs** indicates packet loss without timeout. TCP performs **Fast Retransmit** (retransmits the missing segment immediately) and enters Fast Recovery.

---

### Q13. Which protocol maps a known IP address to an unknown MAC address on a local Ethernet network?
- [x] **ARP (Address Resolution Protocol)**
- [ ] RARP (Reverse ARP)
- [ ] DHCP
- [ ] ICMP

> **Explanation:** **ARP** resolves a 32-bit Layer 3 IP address to a 48-bit Layer 2 MAC address by broadcasting an ARP Request frame onto the local network.

---

### Q14. In the TLS/SSL handshake, which mechanism ensures forward secrecy (PFS)?
- [ ] RSA Static Key Exchange
- [x] **Ephemeral Diffie-Hellman (ECDHE)**
- [ ] AES-256 Symmetric Key Encryption
- [ ] SHA-256 Hashing

> **Explanation:** **Diffie-Hellman Ephemeral (DHE / ECDHE)** generates temporary, disposable key pairs per session, ensuring that compromising a server's long-term private key in the future cannot decrypt past recorded sessions (**Perfect Forward Secrecy**).

---

## ⚡ Section 4: Data Structures & Algorithms (DSA)

### Q15. An AVL tree currently has a balance factor of +2 at node X. The unbalance was caused by inserting a key into the left child's right subtree (LR case). What rotation is needed to restore balance?
- [ ] Single Left Rotation
- [ ] Single Right Rotation
- [x] **Left-Right Double Rotation (Left at child, Right at root)**
- [ ] Right-Left Double Rotation

> **Explanation:** An `LR` imbalance requires a double rotation: first a **Left Rotation** on the left child node, followed by a **Right Rotation** on the unbalanced root node `X`.

---

### Q16. Which single-source shortest path algorithm can detect negative-weight cycles in a directed graph?
- [ ] Dijkstra's Algorithm
- [x] **Bellman-Ford Algorithm**
- [ ] Prim's Algorithm
- [ ] Kruskal's Algorithm

> **Explanation:** **Bellman-Ford** runs `V - 1` iterations of edge relaxations. If a further `V`-th iteration relaxes any edge, a **negative-weight cycle** exists in the graph.

---

### Q17. Building a Binary Heap from an unordered array of N elements using the bottom-up `heapify` approach takes what time complexity?
- [ ] `O(N log N)`
- [x] **`O(N)`**
- [ ] `O(N²)`
- [ ] `O(log N)`

> **Explanation:** Bottom-up heap construction runs `heapify` from index `⌊N/2⌋` down to 1. Summing node heights yields a convergent geometric series ∑ (N / 2^(h+1)) × h = O(N).

---

### Q18. What is the time complexity of solving the 0/1 Knapsack problem with N items and capacity W using Dynamic Programming?
- [ ] `O(N log N)`
- [x] **`O(N × W)` (Pseudo-polynomial)**
- [ ] `O(2^N)`
- [ ] `O(N + W)`

> **Explanation:** DP table of size `(N + 1) × (W + 1)` takes `O(N × W)` time. Since `W` is represented in binary using `log W` bits, the complexity is exponential in input representation length, making it *pseudo-polynomial*.

---

## 🏗️ Section 5: Compiler Design & COA

### Q19. A 5-stage instruction pipeline (IF, ID, EX, MEM, WB) executes 100 instructions without hazards. How many clock cycles are required?
- [ ] 500
- [x] **104 cycles (5 + 100 - 1)**
- [ ] 100
- [ ] 105

> **Explanation:** Formula for `k`-stage pipeline executing `n` instructions: `Cycles = k + (n - 1) = 5 + (100 - 1) = 104`.

---

### Q20. In a set-associative cache with 64 sets and 4 lines per set (4-way), how many lines are there in total?
- [ ] 64
- [ ] 128
- [x] **256**
- [ ] 512

> **Explanation:** Total lines = `Sets × Lines_per_set = 64 × 4 = 256` lines.

---

## 🌾 Section 6: Agriculture, Cooperatives & IFFCO Awareness

### Q21. What is the scientifically recommended NPK (Nitrogen : Phosphorus : Potassium) fertilizer ratio for balanced soil health in Indian agriculture?
- [ ] 1 : 2 : 1
- [x] **4 : 2 : 1**
- [ ] 2 : 1 : 1
- [ ] 4 : 4 : 2

> **Explanation:** The ideal benchmark NPK consumption ratio recommended by soil scientists for Indian agricultural soil is **4 : 2 : 1**.

---

### Q22. World's first commercial Nano Urea (Liquid) plant was developed and launched by IFFCO at which production unit?
- [x] **Kalol (Gujarat)**
- [ ] Phulpur (Uttar Pradesh)
- [ ] Aonla (Uttar Pradesh)
- [ ] Paradeep (Odisha)

> **Explanation:** **IFFCO Kalol (Gujarat)** unit holds the distinction of launching the world's first commercial **IFFCO Nano Urea (Liquid)** and **Nano DAP** manufacturing plant.

---

### Q23. Which of the following is NOT an IFFCO fertilizer manufacturing unit?
- [ ] Phulpur (UP)
- [ ] Kandla (Gujarat)
- [ ] Paradeep (Odisha)
- [x] **Bhopal (MP)**

> **Explanation:** IFFCO's 5 major manufacturing units are **Kalol** (Gujarat), **Kandla** (Gujarat), **Phulpur** (UP), **Aonla** (UP), and **Paradeep** (Odisha). Bhopal is not an IFFCO plant location.

---

### Q24. When was Indian Farmers Fertiliser Cooperative Limited (IFFCO) registered as a multi-state cooperative society?
- [x] **3 November 1967**
- [ ] 15 August 1947
- [ ] 26 January 1950
- [ ] 1 April 1974

> **Explanation:** IFFCO was established and registered on **3 November 1967** under the Multi-State Cooperative Societies Act.
