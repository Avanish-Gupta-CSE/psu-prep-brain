# MSTC MT (Systems) — Technical Question Bank

This is a drill sheet for the MSTC MT (Systems) interview.

Reference for role signals (desirable areas like networking, Java/J2EE, REST/SOAP, DevOps, Azure, databases): [MSTC Recruitment Ad (01/2025)](https://www.madeeasy.in/uploads/RecentJobs/mstc-recruitment-2025-per-month-allowances-50k.pdf)

## How to Use (repeat loop)

- **Pass 1 (fast recall)**: answer each question in 20–40 seconds.
- **Pass 2 (follow-ups)**: pick 2 follow-ups and go 60–90 seconds.
- **Rule**: if you can’t explain it clearly, you don’t know it yet. Write the weak topic into `MSTC/MOCK-INTERVIEW-TRACKER.md`.

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
