# OS — Operating System Study Notes Index

> Format: Definition + Example + 40s script + Follow-ups. PSU MSTC interview ready.
> ★ OS definition was a mock interview gap — read this file first.

---

## Revision Order

```
Step 1 → 01-OS-BASICS-AND-PROCESSES.md    Definition, types, process states, PCB (10 min)
Step 2 → 02-THREADS-AND-SCHEDULING.md     Threads, ULT vs KLT, multithreading models (12 min)
```

> **Day-before quick revision:** Cheat sheets at bottom of each file only.
> **OS technical definition is #1 priority** — say the 40s script aloud right now.

---

## Files

| File | Topics | Read Time | Status |
|---|---|---|---|
| `01-OS-BASICS-AND-PROCESSES.md` | OS definition, 8 types, OS services, 10 OS functions, Process in memory, 5 process states, PCB (7 fields) | 10 min | ✅ Done |
| `02-THREADS-AND-SCHEDULING.md` | Thread definition, Thread vs Process (4 differences), ULT vs KLT, 3 Multithreading models, Advantages/Disadvantages | 12 min | ✅ Done |

---

## Master Cheat Sheet

```
OS Definition:
  "Software that acts as interface between user and hardware.
   Manages CPU, memory, devices. Takes user instructions → directs CPU → hardware acts."

OS Types (8): "Batch Multi Real Dist Embed Net Mobile Multi-proc"
  Batch → run jobs without user interaction
  Multi-tasking → multiple tasks on one CPU (time-sharing)
  Real-time → strict timing (RTOS)
  Distributed → multiple computers, appear as one
  Embedded → inside devices (car, microwave)
  Network → centralized resource sharing
  Mobile → smartphones (Android, iOS)
  Multi-processor → multiple CPUs

OS Functions (10):
  Memory, Process, File, Device, Networking, Security,
  Communication, Job Accounting, Secondary Storage, Command Interpretation

Process in Memory:
  Stack (top) → function params, return addresses, local vars (grows down)
  Heap ↑ → dynamic memory allocation (malloc/new)
  Data → global variables
  Text (bottom) → program code (read-only)

Process States (5): "New Ready Run Wait Terminated"
  New → being created
  Ready → waiting for CPU (in queue)
  Running → instructions executing on CPU
  Waiting → waiting for I/O or event
  Terminated → execution complete

Transitions:
  New → Ready: Admitted
  Ready → Running: Scheduler dispatch
  Running → Ready: Interrupt
  Running → Waiting: I/O or event wait
  Waiting → Ready: I/O or event completion
  Running → Terminated: Exit

PCB (7 fields): "PP-PPC-RML"
  Pointer, Process State, Process Number(PID), Program Counter,
  Registers, Memory Limits, List of Open Files

Thread: lightweight process, shares parent's address space
  Has: Program Counter + Register Set + Stack Space

ULT vs KLT:
  ULT → user space, fast create, no kernel awareness, blocking = entire process blocks
  KLT → kernel space, OS manages, slower create, blocking = only that thread blocks

Multithreading Models:
  Many-to-One   → many user → one kernel → no multiprocessing benefit
  One-to-One    → each user → own kernel → true parallelism, expensive
  Many-to-Many  → many user → ≤many kernel → BEST: flexible + no blocking
```

---

## Topics To Add Next

- [ ] CPU Scheduling algorithms — FCFS, SJF, Round Robin, Priority
- [ ] Deadlock — 4 conditions, Banker's Algorithm, Prevention
- [ ] Memory Management — Paging, Segmentation, Virtual Memory
- [ ] Synchronization — Mutex, Semaphore, Race Condition
- [ ] File System — Allocation methods (contiguous, linked, indexed)
