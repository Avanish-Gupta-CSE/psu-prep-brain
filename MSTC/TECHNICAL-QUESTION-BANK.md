# MSTC MT (Systems) — Technical Question Bank

This is a drill sheet for the MSTC MT (Systems) interview.

Reference for role signals (desirable areas like networking, Java/J2EE, REST/SOAP, DevOps, Azure, databases): [MSTC Recruitment Ad (01/2025)](https://www.madeeasy.in/uploads/RecentJobs/mstc-recruitment-2025-per-month-allowances-50k.pdf)

## How to Use (repeat loop)

- **Pass 1 (fast recall)**: answer each question in 20–40 seconds.
- **Pass 2 (follow-ups)**: pick 2 follow-ups and go 60–90 seconds.
- **Rule**: if you can’t explain it clearly, you don’t know it yet. Write the weak topic into `MSTC/MOCK-INTERVIEW-TRACKER.md`.

## 0A) 7-minute lightning mode (Systems)

Use this when panel time is short (intro → rapid fundamentals → done).

**Structure (7 minutes):**

- 0:00–0:30: self-intro (30–40 seconds)
- 0:30–6:30: ~10 questions (aim **15–20 seconds** per answer; expand only if asked)
- 6:30–7:00: close (“Thank you”)

**Rules:**

- Start with **definition**, add **one key tradeoff**, give **one example**.
- Stop talking after your core answer. Let them ask follow-ups.
- If you don’t know: say so quickly, then offer a safe reasoning attempt (“I don’t recall the exact term, but the idea is …”).

**Core lightning set (pick any 10 daily, rotate):**

- **DBMS**
  - PK vs UK vs FK (with 1 example)
  - 1NF→3NF: what it prevents (one-liner)
  - JOIN types + a LEFT JOIN trap (WHERE vs ON)
  - Index: speeds reads, slows writes (why)
  - ACID + one isolation anomaly (dirty/non-repeatable/phantom)
- **OS**
  - Process vs thread (1 real example)
  - Context switch: what is “saved/restored” (high-level)
  - Scheduling: goal of RR vs SJF (1 tradeoff)
  - Deadlock: 4 conditions + 1 prevention
  - Paging/virtual memory: what it solves
- **Computer Networks**
  - TCP vs UDP (when to use each)
  - TCP 3-way handshake (why it exists)
  - DNS: what happens when you type a URL (high-level)
  - HTTP vs HTTPS + what TLS gives you
  - Common ports: 80/443/22/53 (what they are)
- **DSA**
  - Big-O: what it means (time vs space)
  - Stack vs queue (use cases)
  - Hashing: collision handling (chaining vs open addressing)
  - BFS vs DFS (when/why)
  - BST property + lookup complexity (average vs worst-case)

### Lightning answer scripts (15–20 seconds each)

Memorize this structure: **Definition → 1 tradeoff → 1 example**. Then stop talking.

**DBMS**
- **PK vs UK vs FK**: “Primary key uniquely identifies a row and can’t be NULL; a unique constraint also enforces uniqueness and you can have multiple unique keys; a foreign key references a primary/unique key to enforce relationships. Example: `users.id` PK, `users.email` unique, `orders.user_id` FK.”
- **1NF→3NF**: “1NF = atomic values; 2NF removes partial dependency on a composite key; 3NF removes transitive dependencies. Goal is to reduce redundancy and update anomalies.”
- **JOIN + LEFT JOIN trap**: “INNER gives matches only; LEFT keeps all left rows. Trap: filtering right table columns in WHERE turns LEFT into INNER; put that filter inside the ON clause.”
- **Index basics**: “An index is an extra data structure that maps key → row location; it speeds reads/joins but slows writes and uses space. Example: index on email speeds login lookup.”
- **ACID + anomaly**: “Atomicity all-or-nothing, Consistency keeps constraints valid, Isolation behaves like serial execution, Durability persists after commit. Example anomaly: dirty read = reading uncommitted data.”

**OS**
- **Process vs thread**: “A process has its own address space; threads are multiple execution units within a process sharing memory. Threads are cheaper to context switch. Example: one app process with UI + worker threads.”
- **Context switch**: “OS saves current thread’s CPU state (PC, registers, stack pointer) and restores another’s; this overhead is why too many threads can hurt performance.”
- **RR vs SJF**: “Round-robin improves fairness/response time with time slices; SJF minimizes average waiting time but can starve long jobs. Interactive → RR, batch → SJF.”
- **Deadlock**: “Deadlock needs mutual exclusion, hold-and-wait, no preemption, circular wait. Prevent by breaking one—e.g., enforce global resource ordering.”
- **Paging/virtual memory**: “Virtual memory gives each process the illusion of large memory; paging maps virtual pages to physical frames, enabling isolation and using disk on demand via page faults.”

**Computer Networks**
- **TCP vs UDP**: “TCP is reliable and ordered with congestion control; UDP is best-effort and low overhead. TCP for web/files; UDP for streaming/VoIP/DNS.”
- **3-way handshake**: “SYN, SYN-ACK, ACK establishes a connection and initial sequence numbers so both sides agree on state before sending data.”
- **Type URL (high-level)**: “DNS resolves name to IP, then TCP handshake, then TLS handshake for HTTPS, then HTTP request/response, then browser renders.”
- **HTTP vs HTTPS/TLS**: “HTTP is plain text; HTTPS is HTTP over TLS. TLS provides encryption, integrity, and server authentication via certificates.”
- **Ports**: “80=HTTP, 443=HTTPS, 22=SSH, 53=DNS.”

**DSA**
- **Big‑O**: “Big‑O describes how time/space grows with input size—an upper bound used to compare algorithms.”
- **Stack vs queue**: “Stack is LIFO (call stack, undo); queue is FIFO (scheduling, BFS).”
- **Hash collisions**: “Collisions happen when two keys map to same bucket. Handle with chaining (list per bucket) or open addressing (probe next slots).”
- **BFS vs DFS**: “BFS uses a queue and finds shortest paths in unweighted graphs; DFS uses recursion/stack and is good for traversal/connectivity. Both are O(V+E).”
- **BST**: “BST keeps left < node < right. Average search is O(log n) if balanced; worst is O(n) if skewed.”

### Lecture patch rule (only when you blank out)

If you cannot deliver the 15–20s script, do **20 minutes lecture** on that exact topic, then immediately retake the same script.

- DBMS: [Gate Smashers DBMS playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y)
- OS: [Gate Smashers OS playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiGz9donHRrE9I3Mwn6XdP8p)
- CN: [Neso Academy CN playlist](https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx&feature=shared) or [Gate Smashers CN playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_)
- DSA: [Abdul Bari DSA playlist](https://www.youtube.com/playlist?list=PL03of0rPCur_NZ9Rr4w1a5RDMU2qegBQl&cbrd=1&ucbcb=1)

**MSTC lightning add-ons (1–2 questions, if they ask non-technical quickly):**

- What is a **forward auction** vs **reverse auction**? (one-liner + example)
- Name 1–2 **e-auction platform competitors** in India (one-liner only)
- “In 1 line, what does MSTC do?” (PSU + e-auction/e-commerce services)
- “Why MSTC?” (10–15 seconds: platforms + public impact + fit)

**15-minute extension pack (if they keep going after basics):**

- **DBMS follow-ups**: covering index (idea), DB deadlock (what happens), conflict vs view serializable (one-liner)
- **OS follow-ups**: race condition example, mutex vs semaphore, page fault (high-level)
- **CN follow-ups**: 502 vs 504 meaning (high-level), latency vs throughput (one-liner)
- **DSA follow-ups**: why collisions happen, average vs worst-case lookup in hash table, BFS/DFS complexity
- **1 project follow-up**: “Explain one system you built at Berkadia — what happens on failure and what you log.”

## 0) Opening: “What do you do?”

- “I build production web applications using React + Node/Express + TypeScript, with PostgreSQL/Elasticsearch, AWS, CI/CD and security-aware workflows. I’m comfortable learning new stacks and I focus on reliability, auditability, and clean APIs.”

## 1) Networking (must not fumble)

### Core questions

- TCP vs UDP — differences, tradeoffs, and examples
- What happens when you type a URL in the browser?
- DNS basics (A/AAAA/CNAME), caching, TTL
- HTTP vs HTTPS, what TLS gives you
- NAT vs routing, private/public IP
- CIDR and subnetting (be able to do quick host counts)
- Common ports (80/443/22/53/25/110/143) and what they mean
- Load balancer vs reverse proxy (high-level)

### Fast answers (one-liners)

- **TCP vs UDP**: TCP is reliable/ordered/connection-oriented; UDP is best-effort/low-overhead; pick based on loss tolerance vs latency.
- **TLS**: encrypts data-in-transit + authenticates server identity (and optionally client); prevents sniffing/tampering.
- **DNS caching**: improves latency; TTL controls freshness; stale DNS = “it works on my machine” failures.

### Follow-ups interviewers ask

- Why does TCP handshake exist? What’s SYN/SYN-ACK/ACK?
- What’s latency vs throughput? Which one impacts page load more?
- What is a 502/504 from a reverse proxy usually telling you?

## 2) DBMS + SQL (PSU interviews love clarity here)

### Core questions

- Primary key vs unique key vs foreign key
- Normalization (what it prevents), when denormalization is acceptable
- Index basics: why they speed reads and slow writes
- ACID, transactions, isolation anomalies (dirty/non-repeatable/phantom)
- JOIN types and when each is needed
- SQL NULL traps (`COUNT(*)` vs `COUNT(col)`, `NULL = NULL` is not TRUE)

### Follow-ups

- B-Tree vs hash index (high-level)
- What is a deadlock in DB? How does the DB handle it?
- Explain “covering index” idea in simple terms

## 3) Operating Systems (only fundamentals)

### Core questions

- Process vs thread, context switching
- CPU scheduling: what’s the goal (throughput/latency/fairness)
- Deadlock: 4 necessary conditions + one prevention strategy
- Mutex vs semaphore (definition-level clarity is enough)
- Memory basics: paging/virtual memory (what it solves)

### Follow-ups

- What is a race condition? Example in plain English.
- What happens if one thread holds a lock and crashes?

## 4) Web + APIs (must be crisp)

### Core questions

- What is REST? What makes an API “RESTful”?
- HTTP methods + idempotency (GET/POST/PUT/PATCH/DELETE)
- Status codes: 200/201/204/400/401/403/404/409/429/500/502/503
- What is CORS and why does it exist?
- Cookies vs local storage (security angle)
- REST vs SOAP (when SOAP still appears in government/enterprise)

### Follow-ups

- Authentication vs authorization
- JWT: why it’s used, where it fails (revocation, storage, key rotation)
- CSRF vs XSS (difference, prevention basics)

## 5) Security (baseline)

### Core questions

- SQL injection, XSS, CSRF — what they are and how to mitigate
- Hashing vs encryption, salt, and password storage
- Least privilege and why it matters
- Audit logging: what to log (and what not to)

### Follow-ups

- What is “defense in depth”?
- What is rate limiting and where to apply it?

## 6) DevOps + Cloud (interviewers test practical thinking)

### Core questions

- Docker image vs container; what goes into a Dockerfile
- CI vs CD; what should a CI pipeline guarantee
- Kubernetes basics: why it exists, what Deployments/Services do (high-level)
- Secrets management basics (never hardcode; use secret stores)

### Follow-ups

- Rolling deployment vs blue/green (tradeoffs)
- What metrics/logs would you check first in a production incident?

## 7) Java/J2EE + .NET (awareness level)

You don’t need to claim production expertise here. You must be able to explain fundamentals and learnability.

### J2EE fundamentals

- What is a servlet? What does a servlet container (Tomcat) do?
- JSP vs servlet (high-level)
- Session management basics (cookie-backed session id)
- Spring Boot in one line (opinionated app framework; simplifies config + dependency injection)

### .NET basics

- ASP.NET: server-side web framework in the Microsoft ecosystem
- C# vs JavaScript/TypeScript: compiled strongly typed vs dynamic runtime model (high-level)

## 8) “MSTC systems thinking” questions (role-fit)

- If you were designing an e-auction platform, what are the top 5 non-functional requirements?
- How do you ensure auditability and tamper resistance in bidding workflows?
- How do you handle peak traffic and avoid downtime during closing minutes of an auction?

Answer structure:

1) availability + performance, 2) security + access control, 3) audit logs, 4) correctness under concurrency, 5) monitoring + incident response.
