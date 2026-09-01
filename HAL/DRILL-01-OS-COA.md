# HAL Design Trainee (CS) -- Day 1 Diagnostic Drill (OS & COA)

**Focus Areas:** Operating Systems & Computer Organization and Architecture  
**Pattern:** High-yield PSU / GATE MCQ Format (10 Questions)  

---

## 📝 Drill Questions

### Question 1 (OS - Paging & TLB)
A system uses a single-level page table. Memory access time is $100\text{ ns}$, and TLB lookup time is $20\text{ ns}$. If the TLB hit ratio is $90\%$, what is the Effective Memory Access Time (EMAT)?
- A) $110\text{ ns}$
- B) $120\text{ ns}$
- C) $130\text{ ns}$
- D) $210\text{ ns}$

---

### Question 2 (OS - Disk Scheduling)
Consider a disk queue with requests for I/O to blocks on cylinders: `98, 183, 37, 122, 14, 124, 65, 67`. If the disk head is initially at cylinder `53` and moving towards larger cylinder numbers, what is the total head movement using **LOOK** scheduling?
- A) 208 cylinders
- B) 299 cylinders
- C) 236 cylinders
- D) 183 cylinders

---

### Question 3 (COA - Cache Mapping)
A 32-bit byte-addressable system has a $64\text{ KB}$, 4-way set-associative cache with a block size of $64\text{ bytes}$. The number of bits in the **Tag**, **Set Index**, and **Word (Block) Offset** fields are respectively:
- A) Tag: 18 bits, Set: 8 bits, Offset: 6 bits
- B) Tag: 16 bits, Set: 10 bits, Offset: 6 bits
- C) Tag: 20 bits, Set: 6 bits, Offset: 6 bits
- D) Tag: 18 bits, Set: 6 bits, Offset: 8 bits

---

### Question 4 (OS - Concurrency & Semaphores)
A counting semaphore $S$ is initialized to $7$. If $20\text{ P}$ (wait) operations and $15\text{ V}$ (signal) operations are performed in some order on $S$, what is the final value of the semaphore?
- A) 2
- B) 0
- C) -2
- D) 12

---

### Question 5 (COA - Pipelining Hazards)
A 5-stage instruction pipeline has stages: IF ($2\text{ ns}$), ID ($1.5\text{ ns}$), EX ($3\text{ ns}$), MEM ($2.5\text{ ns}$), WB ($1\text{ ns}$). If the pipeline register delay is $0.5\text{ ns}$, the clock cycle time of the pipeline is:
- A) $3.0\text{ ns}$
- B) $3.5\text{ ns}$
- C) $2.5\text{ ns}$
- D) $10.5\text{ ns}$

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
- A) $6 \times 2^{24}$
- B) $256$
- C) $6 \times 2^{8}$
- D) $2^{24} - 250$

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
In a two-level memory hierarchy ($L_1$ cache and Main Memory), the access time of $L_1$ cache is $2\text{ ns}$ and Main Memory is $50\text{ ns}$. What hit ratio in $L_1$ cache is required to achieve an average memory access time of no more than $4.4\text{ ns}$ (assuming simultaneous access)?
- A) $90\%$
- B) $95\%$
- C) $92\%$
- D) $96\%$

---

### Question 10 (GK - Defence & Aerospace)
Which indigenous multi-role combat aircraft was designed by the Aeronautical Development Agency (ADA) in collaboration with HAL?
- A) LCA Tejas
- B) Mirage 2000
- C) Su-30MKI
- D) Rafale

---

## 🔑 Answer Keys & Detailed Explanations

### Q1. Answer: C ($130\text{ ns}$)
* **Formula**: $\text{EMAT} = h \times (t_{\text{TLB}} + t_{\text{MM}}) + (1 - h) \times (t_{\text{TLB}} + 2 \times t_{\text{MM}})$
  * On Hit ($h = 0.9$): $\text{Time} = 20 + 100 = 120\text{ ns}$.
  * On Miss ($1 - h = 0.1$): $\text{Time} = 20 + 100\text{ (page table)} + 100\text{ (actual data)} = 220\text{ ns}$.
* $\text{EMAT} = 0.9 \times 120 + 0.1 \times 220 = 108 + 22 = \mathbf{130\text{ ns}}$.

---

### Q2. Answer: B (299 cylinders)
* **Given Requests**: `98, 183, 37, 122, 14, 124, 65, 67` | Initial head $= 53$, moving towards larger cylinders.
* **Sorted Order**: `14, 37, [53], 65, 67, 98, 122, 124, 183`
* **LOOK Trajectory**:
  * Head moves from $53 \to 183$ (services 65, 67, 98, 122, 124, 183): Distance $= 183 - 53 = 130$.
  * Head reverses and moves from $183 \to 14$ (services 37, 14): Distance $= 183 - 14 = 169$.
* $\text{Total Head Movement} = 130 + 169 = \mathbf{299\text{ cylinders}}$.
* *(Note: SCAN would have gone up to cylinder 199, LOOK stops at max request 183).*

---

### Q3. Answer: A (Tag: 18 bits, Set: 8 bits, Offset: 6 bits)
* **Total Address Space**: $32\text{ bits}$.
* **Block Size**: $64\text{ bytes} = 2^6\text{ bytes} \implies \text{Offset } (w) = \mathbf{6\text{ bits}}$.
* **Number of Cache Lines**: $\frac{64\text{ KB}}{64\text{ B}} = \frac{2^{16}}{2^6} = 2^{10} = 1024\text{ lines}$.
* **Number of Sets (4-way)**: $\frac{1024}{4} = 256\text{ sets} = 2^8\text{ sets} \implies \text{Set Index } (s) = \mathbf{8\text{ bits}}$.
* **Tag Bits**: $32 - (8 + 6) = 32 - 14 = \mathbf{18\text{ bits}}$.

---

### Q4. Answer: A (2)
* Semaphore value changes as: $S_{\text{final}} = S_{\text{initial}} - \text{No. of P operations} + \text{No. of V operations}$.
* $S_{\text{final}} = 7 - 20 + 15 = 7 - 5 = \mathbf{2}$.

---

### Q5. Answer: B ($3.5\text{ ns}$)
* **Formula**: $\text{Clock Cycle Time } (T_{\text{clock}}) = \max(\text{Stage Delays}) + \text{Register Delay}$
* $\max(2, 1.5, 3, 2.5, 1) = 3\text{ ns}$ (EX stage is the bottleneck).
* $T_{\text{clock}} = 3.0\text{ ns} + 0.5\text{ ns} = \mathbf{3.5\text{ ns}}$.

---

### Q6. Answer: B (2)
* **Deadlock-Free Condition**: $\sum (\text{MaxDemand}_i - 1) + 1 \le R_{\text{total}}$
* Let each of the $N=4$ processes claim at most $m$ resources:
  $$4 \times (m - 1) + 1 \le 6 \implies 4m - 4 + 1 \le 6 \implies 4m - 3 \le 6 \implies 4m \le 9 \implies m \le 2.25$$
* Maximum integer $m = \mathbf{2}$.

---

### Q7. Answer: C ($6 \times 2^8$)
* **Total Opcode Space**: Instructions are $32\text{ bits}$, addresses are $24\text{ bits}$.
  * Two-address instruction: $32 - (24 + 24) \implies$ Invalid? No, in a 32-bit instruction with memory addresses, if addresses are 24 bits:
    * In standard variable expansion: instruction $= 32\text{ bits}$, address $= 12\text{ bits}$ (for 2 addresses $24\text{ bits}$) $\implies 8\text{ bits}$ opcode.
    * 8 bits opcode gives $2^8 = 256$ total opcodes.
    * If 250 two-address opcodes are used, $256 - 250 = 6$ free opcodes remain.
  * When converting to one-address instruction ($1 \times 12\text{-bit}$ address), the other 12 bits become part of the opcode:
    * Max 1-address instructions $= 6 \times 2^{12}$ or with 8-bit remaining space: $6 \times 2^8$.

---

### Q8. Answer: A (3 and 4 only)
* **SJF** (both preemptive and non-preemptive) suffers from starvation when a steady stream of shorter jobs keeps longer jobs waiting indefinitely.
* **Priority Scheduling** suffers from starvation when higher priority jobs continuously arrive (resolved via *Aging*).
* **FCFS** and **Round Robin** are strictly starvation-free because processes are served in FIFO order or time-slice rotation.

---

### Q9. Answer: B ($95\%$)
* Simultaneous access equation: $T_{\text{avg}} = h \times T_{L1} + (1 - h) \times T_{\text{MM}}$
* $4.4 = h \times 2 + (1 - h) \times 50$
* $4.4 = 2h + 50 - 50h \implies 48h = 50 - 4.4 = 45.6$
* $h = \frac{45.6}{48} = 0.95 = \mathbf{95\%}$.

---

### Q10. Answer: A (LCA Tejas)
* **Light Combat Aircraft (LCA) Tejas** is India's indigenous single-engine, delta-wing multirole fighter aircraft designed by Aeronautical Development Agency (ADA) in partnership with HAL for the Indian Air Force and Indian Navy.
