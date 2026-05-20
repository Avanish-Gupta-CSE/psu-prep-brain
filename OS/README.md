# OS — Operating System Study Notes Index

> Format: Definition + Example + 40s script + Follow-ups. MSTC Systems interview ready.

---

## Revision Order (Follow This)

```
Step 1 → 01-PROCESS-AND-THREADS.md    Process states, PCB, Process vs Thread (25 min)
```

> **Day-before quick revision:** Cheat sheet at bottom of 01-PROCESS-AND-THREADS.md only.

---

## Files

| File | Topics | Status |
|---|---|---|
| `01-PROCESS-AND-THREADS.md` | OS definition, Process states, PCB, Process vs Thread, Threading models | ✅ Done |

---

## Master Cheat Sheet

```
OS Definition:
  System software interface between user and hardware
  Manages: CPU, Memory, Files, I/O, Security, Networking

Process vs Program:
  Process → program in execution (active)
  Program → code on disk (passive)

Process States (5):
  New → Ready → Running → Waiting → Terminated
  Ready ↔ Running (scheduler dispatch/interrupt)

Process vs Thread:
  Process → separate memory space, heavy, independent
  Thread  → shared memory space, light, dependent
  IPC vs direct memory communication

PCB (Process Control Block):
  PID, State, Program Counter, CPU Registers, Memory Limits, Open Files
  Used for: context switching, scheduling, memory management

Thread Types:
  User-Level   → library managed, fast, blocking problem
  Kernel-Level → OS managed, slower, true parallelism
```

---

## Topics To Add (Next Pages)

- [ ] CPU Scheduling — FCFS, SJF, RR, Priority
- [ ] Deadlocks — conditions, prevention, avoidance, detection
- [ ] Memory Management — paging, segmentation, virtual memory
- [ ] Synchronization — mutex, semaphore, monitors