# Operating Systems Revision Sheet

This note is designed for rapid recall of paging structures, virtual memory calculations, effective memory access times, and fragmentation properties.

---

## 💾 1. Virtual Memory & Paging Structures

Paging maps non-contiguous physical memory into a contiguous virtual address space.

```
       Virtual Address (VA)                      Physical Address (PA)
+-----------------------+-----------+    +-----------------------+-----------+
|    Page Number (p)    | Offset(d) |    |    Frame Number (f)   | Offset(d) |
+-----------------------+-----------+    +-----------------------+-----------+
            |                                         ^
            v                                         |
    +---------------+                                 |
    |  PAGE TABLE   | --------------------------------+
    +---------------+
```

### Core Equations
Let:
* $\text{VAS}$ = Virtual Address Space Size $= 2^V$ bytes $\implies$ Virtual Address length $= V$ bits.
* $\text{PAS}$ = Physical Address Space Size $= 2^P$ bytes $\implies$ Physical Address length $= P$ bits.
* $\text{Page Size} = \text{Frame Size} = 2^d$ bytes $\implies$ Page Offset $= d$ bits.

1. **Page Number Length** ($p$ bits):
   $$p = V - d$$
2. **Frame Number Length** ($f$ bits):
   $$f = P - d$$
3. **Number of Pages** ($N_{\text{pages}}$):
   $$N_{\text{pages}} = \frac{\text{VAS}}{\text{Page Size}} = 2^p$$
4. **Number of Frames** ($N_{\text{frames}}$):
   $$N_{\text{frames}} = \frac{\text{PAS}}{\text{Page Size}} = 2^f$$
5. **Page Table Entry (PTE) size**:
   $$\text{PTE Size} = f \text{ bits} + \text{Auxiliary bits (Dirty, Valid, Reference, Protection)}$$
   * *Rule*: Round the PTE size up to the nearest byte (or power of 2 bytes) if specified by word-aligned system rules.
6. **Page Table Size** ($\text{PTS}$):
   $$\text{PTS} = N_{\text{pages}} \times \text{PTE Size} = 2^p \times \text{PTE Size}$$

---

## ⚡ 2. Effective Memory Access Time (EMAT)

Without a TLB, every logical memory access requires **two physical memory accesses** (one to read the page table, and one to read the actual data).

### 1. EMAT with Translation Lookaside Buffer (TLB)
A TLB is a fast hardware cache that stores recently accessed page-to-frame mappings.
$$\text{EMAT} = h \cdot (T_{\text{TLB}} + T_{\text{mem}}) + (1 - h) \cdot (T_{\text{TLB}} + 2 \cdot T_{\text{mem}})$$
Where:
* $h$ = TLB hit ratio.
* $T_{\text{TLB}}$ = TLB lookup time.
* $T_{\text{mem}}$ = Main memory access time.

* **Trap (Overlapping Lookup)**: If the system searches TLB and main memory *in parallel* (highly unusual but sometimes asked), the miss time becomes $T_{\text{mem}} + T_{\text{mem}}$ instead of $T_{\text{TLB}} + 2 \cdot T_{\text{mem}}$. Read the question wording carefully!

### 2. EMAT with Multi-Level Paging
If a system uses $k$-level hierarchical paging and does *not* have a TLB, we need $k$ accesses to traverse the page table hierarchy plus 1 access to read the actual data:
$$\text{EMAT}_{\text{no-TLB}} = (k + 1) \cdot T_{\text{mem}}$$
If a TLB is present:
$$\text{EMAT} = h \cdot (T_{\text{TLB}} + T_{\text{mem}}) + (1 - h) \cdot (T_{\text{TLB}} + (k + 1) \cdot T_{\text{mem}})$$

---

## 🧩 3. Fragmentation Demystified

Fragmentation is wasted memory that cannot be allocated to active processes.

```
+------------------------------------+------------------------------------+
|       INTERNAL FRAGMENTATION       |       EXTERNAL FRAGMENTATION       |
+------------------------------------+------------------------------------+
| Memory allocated to a process is   | Total free memory is large enough  |
| larger than requested, leaving a   | to satisfy a request, but it is    |
| wasted gap *inside* the block.     | split into non-contiguous slices.  |
+------------------------------------+------------------------------------+
| Occurs in: Fixed-size partition    | Occurs in: Variable-size partition |
| schemes (such as standard Paging). | schemes (such as Segmentation).    |
+------------------------------------+------------------------------------+
| Remedy: Reduce page size.          | Remedy:                            |
|                                    | 1. Compaction (relocate blocks).   |
|                                    | 2. Paging (virtual memory maps     |
|                                    |    non-contiguous frames).         |
+------------------------------------+------------------------------------+
```

---

## 📊 4. Worked Paging Example
* *Problem*: A 32-bit virtual address system has a page size of 4 KB. Main memory is 512 MB, and the system uses a single-level page table. Each page table entry contains the frame address plus 4 auxiliary bits. 
  * *Goal*: Find the page table size.

### Step 1: Extract Bit Lengths
* Virtual Address Length $V = 32 \text{ bits} \implies \text{VAS} = 2^{32} \text{ bytes}$.
* Page Size $= 4 \text{ KB} = 2^{12} \text{ bytes} \implies$ Offset offset $d = 12 \text{ bits}$.
* Physical Memory Size $= 512 \text{ MB} = 2^{29} \text{ bytes} \implies P = 29 \text{ bits}$.

### Step 2: Calculate Page & Frame Bits
* Page Number bits:
  $$p = V - d = 32 - 12 = 20 \text{ bits} \implies N_{\text{pages}} = 2^{20}$$
* Frame Number bits:
  $$f = P - d = 29 - 12 = 17 \text{ bits}$$

### Step 3: Calculate PTE Size
$$\text{PTE Size} = f + 4 \text{ aux bits} = 17 + 4 = 21 \text{ bits}$$
* Since page tables must be byte-addressable, we round 21 bits up to the nearest byte boundary:
  $$\text{PTE Size rounded} = 3 \text{ bytes (24 bits)}$$

### Step 4: Calculate Page Table Size (PTS)
$$\text{PTS} = N_{\text{pages}} \times \text{PTE Size} = 2^{20} \times 3 \text{ bytes} = 3 \text{ MB}$$

---

## ⚠️ OS Common Traps
* **PTE Rounding**: Always check if a question asks for the exact bit-level size of the page table or requires byte rounding. In real hardware, PTEs are rounded to whole bytes (e.g., 2, 3, or 4 bytes).
* **Multi-Level Page Table Levels**: If page size is $2^d$ bytes and page table entry is $e$ bytes, a single page can hold $\frac{2^d}{e}$ entries. In multi-level paging, the size of each level's table is bounded to fit exactly inside a single page frame!
* **Belady's Anomaly**: Remember that increasing the number of page frames can *increase* the page fault rate under FIFO, but **never** under LRU or Optimal replacement!
