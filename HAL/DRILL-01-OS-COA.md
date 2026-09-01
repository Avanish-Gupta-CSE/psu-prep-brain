# HAL Design Trainee (CS) -- Day 1 Diagnostic Drill (OS & COA)

**Focus Areas:** Operating Systems & Computer Organization and Architecture  
**Pattern:** High-yield PSU / GATE MCQ Format (10 Questions)  

---

## Drill Questions

### Question 1 (OS - Paging & TLB)
A system uses a single-level page table. Memory access time is 100 ns, and TLB lookup time is 20 ns. If the TLB hit ratio is 90%, what is the Effective Memory Access Time (EMAT)?
- A) 110 ns
- B) 120 ns
- C) 130 ns
- D) 210 ns

---

### Question 2 (OS - Disk Scheduling)
Consider a disk queue with requests for I/O to blocks on cylinders: `98, 183, 37, 122, 14, 124, 65, 67`. If the disk head is initially at cylinder `53` and moving towards larger cylinder numbers, what is the total head movement using **LOOK** scheduling?
- A) 208 cylinders
- B) 299 cylinders
- C) 236 cylinders
- D) 183 cylinders

---

### Question 3 (COA - Cache Mapping)
A 32-bit byte-addressable system has a 64 KB, 4-way set-associative cache with a block size of 64 bytes. The number of bits in the **Tag**, **Set Index**, and **Word (Block) Offset** fields are respectively:
- A) Tag: 18 bits, Set: 8 bits, Offset: 6 bits
- B) Tag: 16 bits, Set: 10 bits, Offset: 6 bits
- C) Tag: 20 bits, Set: 6 bits, Offset: 6 bits
- D) Tag: 18 bits, Set: 6 bits, Offset: 8 bits

---

### Question 4 (OS - Concurrency & Semaphores)
A counting semaphore S is initialized to 7. If 20 P (wait) operations and 15 V (signal) operations are performed in some order on S, what is the final value of the semaphore?
- A) 2
- B) 0
- C) -2
- D) 12

---

### Question 5 (COA - Pipelining Hazards)
A 5-stage instruction pipeline has stages: IF (2 ns), ID (1.5 ns), EX (3 ns), MEM (2.5 ns), WB (1 ns). If the pipeline register delay is 0.5 ns, the clock cycle time of the pipeline is:
- A) 3.0 ns
- B) 3.5 ns
- C) 2.5 ns
- D) 10.5 ns

---

### Question 6 (OS - Deadlocks)
A system has 4 processes and 6 identical resource units. What is the maximum number of resources each process can claim such that the system is guaranteed to be deadlock-free?
- A) 1
- B) 2
- C) 3
- D) 4

---

### Question 7 (COA - Instruction Formats)
A computer has 32-bit instructions and 24-bit addresses. If there are 250 two-address instructions already defined, what is the maximum number of one-address instructions that can still be formulated?
- A) 6 * 2^24
- B) 256
- C) 6 * 2^8
- D) 2^24 - 250

---

### Question 8 (OS - CPU Scheduling)
Which of the following CPU scheduling algorithms can potentially cause starvation (indefinite blocking)?
1. Round Robin
2. First-Come, First-Served (FCFS)
3. Shortest Job First (SJF)
4. Priority Scheduling

- A) 3 and 4 only
- B) 1, 3, and 4
- C) 2 and 3 only
- D) 1 and 2 only

---

### Question 9 (COA - Memory Hierarchy)
In a two-level memory hierarchy (L1 cache and Main Memory), the access time of L1 cache is 2 ns and Main Memory is 50 ns. What hit ratio in L1 cache is required to achieve an average memory access time of no more than 4.4 ns (assuming simultaneous access)?
- A) 90%
- B) 95%
- C) 92%
- D) 96%

---

### Question 10 (GK - Defence & Aerospace)
Which indigenous multi-role combat aircraft was designed by the Aeronautical Development Agency (ADA) in collaboration with HAL?
- A) LCA Tejas
- B) Mirage 2000
- C) Su-30MKI
- D) Rafale

---

## Answer Keys & Detailed Explanations

### Q1. Answer: C (130 ns)
* **Formula**: `EMAT = h * (t_TLB + t_MM) + (1 - h) * (t_TLB + 2 * t_MM)`
  * On Hit (h = 0.9): Time = 20 + 100 = 120 ns.
  * On Miss (1 - h = 0.1): Time = 20 + 100 (page table lookup) + 100 (actual data access) = 220 ns.
* `EMAT = 0.9 * 120 + 0.1 * 220 = 108 + 22 = 130 ns`.

---

### Q2. Answer: B (299 cylinders)
* **Given Requests**: `98, 183, 37, 122, 14, 124, 65, 67` | Initial head = 53, moving towards larger cylinders.
* **Sorted Order**: `14, 37, [53], 65, 67, 98, 122, 124, 183`
* **LOOK Trajectory**:
  * Head moves from 53 -> 183 (services 65, 67, 98, 122, 124, 183): Distance = 183 - 53 = 130.
  * Head reverses and moves from 183 -> 14 (services 37, 14): Distance = 183 - 14 = 169.
* `Total Head Movement = 130 + 169 = 299 cylinders`.
* *(Note: SCAN would have traversed up to cylinder 199, whereas LOOK stops at the maximum request cylinder 183).*

---

### Q3. Answer: A (Tag: 18 bits, Set: 8 bits, Offset: 6 bits)
* **Total Address Space**: 32 bits.
* **Block Size**: 64 bytes = 2^6 bytes -> Word/Block Offset = **6 bits**.
* **Number of Cache Lines**: (64 KB) / (64 B) = 2^16 / 2^6 = 2^10 = 1024 lines.
* **Number of Sets (4-way)**: 1024 / 4 = 256 sets = 2^8 sets -> Set Index = **8 bits**.
* **Tag Bits**: 32 - (8 + 6) = 32 - 14 = **18 bits**.

---

### Q4. Answer: A (2)
* **Formula**: `S_final = S_initial - (No. of P operations) + (No. of V operations)`
* `S_final = 7 - 20 + 15 = 7 - 5 = 2`.

---

### Q5. Answer: B (3.5 ns)
* **Formula**: `Clock Cycle Time (T_clock) = max(Stage Delays) + Register Delay`
* `max(2, 1.5, 3, 2.5, 1) = 3 ns` (EX stage is the bottleneck).
* `T_clock = 3.0 ns + 0.5 ns = 3.5 ns`.

---

### Q6. Answer: B (2)
* **Deadlock-Free Condition**: `Sum(MaxDemand_i - 1) + 1 <= R_total`
* Let each of the N = 4 processes claim at most `m` resources:
  * `4 * (m - 1) + 1 <= 6`
  * `4m - 4 + 1 <= 6`
  * `4m - 3 <= 6`
  * `4m <= 9` -> `m <= 2.25`
* Maximum integer `m = 2`.

---

### Q7. Answer: C (6 * 2^8)
* **Total Opcode Space**: Instructions are 32 bits, memory addresses are 12 bits each (2 addresses = 24 bits total address fields).
  * 32 - 24 = 8 bits for opcode.
  * 8-bit opcode space gives `2^8 = 256` total opcodes.
  * 250 two-address instructions are assigned, leaving `256 - 250 = 6` free opcodes.
  * For one-address instructions, the second 12-bit address field joins the opcode space, yielding `6 * 2^8` possible encodings (or `6 * 2^12` depending on register encoding width).

---

### Q8. Answer: A (3 and 4 only)
* **SJF** (both preemptive and non-preemptive) suffers from starvation when shorter jobs continuously arrive.
* **Priority Scheduling** suffers from starvation when higher priority jobs continuously arrive (mitigated via Aging).
* **FCFS** and **Round Robin** are strictly starvation-free because processes are served in FIFO order or time-slice rotation.

---

### Q9. Answer: B (95%)
* Simultaneous access equation: `T_avg = h * T_L1 + (1 - h) * T_MM`
* `4.4 = h * 2 + (1 - h) * 50`
* `4.4 = 2h + 50 - 50h`
* `48h = 50 - 4.4 = 45.6`
* `h = 45.6 / 48 = 0.95 = 95%`.

---

### Q10. Answer: A (LCA Tejas)
* **Light Combat Aircraft (LCA) Tejas** is India's indigenous single-engine, delta-wing multirole fighter aircraft designed by Aeronautical Development Agency (ADA) in partnership with HAL for the Indian Air Force and Indian Navy.
