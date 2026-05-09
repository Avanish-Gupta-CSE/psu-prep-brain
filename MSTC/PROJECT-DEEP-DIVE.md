# Resume Project Deep-Dive (MSTC Interview)

Source of truth for facts/metrics: `Resume-Berkadia.tex` (do not change metrics unless the resume changes).

## How to use this file

- Speak each project in **2 minutes** (what it is → what you built → why it mattered → result).
- Then take **3 follow-ups** (tradeoffs, failure modes, security, scaling, testing).
- If you can’t answer, write the missing topic into `MSTC/MOCK-INTERVIEW-TRACKER.md` as a repair target.

## Project 1 — ReservesAI (AI-Powered Document Processing) — Berkadia

### What it is (1 line)

- AI-assisted extraction workflow for Reserve Request Letters using Azure Document Intelligence and an async processing pipeline.

### What you built (resume-true)

- Frontend: React 19
- Backend: Node.js + Express
- AI/IDP integration: Azure Document Intelligence
- Async workflow: job processing + WebSocket updates
- Validation: bulk-validation test harness
- Delivery: CI/CD via Azure DevOps with Docker and Kubernetes (EKS)

### How to explain it (2-minute structure)

- Problem: manual extraction is slow/error-prone → need consistent data capture.
- Approach: upload → extract → validate → store → notify.
- Reliability: async jobs + user-visible status; retries and clear failure states.
- Quality: test harness for bulk validation to compare expected vs extracted values.

### Follow-up questions (practice answers)

- How do you handle extraction failures and partial extraction?
- How do you validate model accuracy without manual checking every document?
- Why WebSocket for status updates? What alternatives exist?
- What would you monitor in production for this pipeline?

## Project 2 — DMS (Document Management System) — Berkadia

### What it is (1 line)

- Document management for loan servicing workflows: upload, advanced search, bulk operations, recycle bin, and fine-grained access control.

### What you built (resume-true)

- Frontend: React 18 + TypeScript + Redux Toolkit + PrimeReact
- Backend APIs: Node.js/Express
- Storage + data: PostgreSQL + Elasticsearch + AWS S3
- Security: Keycloak SSO + OpenFGA authorization (fine-grained RBAC by document class)

### Core architecture (high-level)

- PostgreSQL = metadata/source-of-truth
- S3 = file/object storage
- Elasticsearch = search index for fast queries
- Keycloak = authentication
- OpenFGA = authorization decisions (policy-driven access)

### Follow-up questions

- Why both PostgreSQL and Elasticsearch? What consistency problems appear?
- How do you handle “delete” safely? (recycle bin; audit requirements)
- How do you design authorization so it’s flexible without being slow?
- What are the failure modes when Elasticsearch is down?

## Project 3 — CMS (Cash Management Service) — Berkadia

### What it is (1 line)

- Cash-management workflows with dashboards, search/filtering, notifications, and quality focus.

### What you built (resume-true)

- Microservices workflow with CQRS concepts
- Elasticsearch schema migrations
- REST APIs using Node.js + TypeScript
- Email notifications via Amazon SES
- React dashboards with Redux
- Testing: achieved 85%+ code coverage with Jest + React Testing Library

### Follow-up questions

- What is CQRS and when is it worth it?
- What goes wrong during a migration? What’s the rollback plan?
- How did you get to 85%+ coverage without writing brittle tests?

## Project 4 — eRFP-NPI (Quotation + TGA workflow) — STMicroelectronics

### What it is (1 line)

- Built an internal workflow product for Technical Gap Analysis and quotation management.

### What you built (resume-true)

- Built the application from the ground up
- Managed 500+ semiconductor quotations for 20+ external manufacturing partners
- Data scale: modules/schemas supporting 1 million+ price-quote records
- Performance: improved complex-query performance by 45%
- Integrity: maintained 99.8% data integrity
- Scale: served 200+ concurrent users with ~300 ms average API response times

### Security + delivery stories (resume-true)

- Resolved 30+ security findings from audit (BMC Helix workflow) → achieved 100% pass on follow-up penetration tests
- Built delivery pipelines with Jenkins CI/CD (cut deploy time by 50%), managed 100+ Git branches, scheduled 50+ batch jobs via TWS, raised automated test coverage to 90% (BDD in ALM)

### Follow-up questions

- What did you do to get 300 ms average API responses under concurrency?
- How did you verify “data integrity” and what does 99.8% mean operationally?
- How did you prioritize 30+ security findings?
- What was the most important tradeoff you made in the architecture?

## Universal cross-questions (practice across every project)

- What was the hardest bug you faced? (Answer only with a real incident you remember.)
- How did you handle unclear requirements?
- What would you redesign today if you had to rebuild it?
- How do you ensure security by default (auth, authz, input validation, secrets)?
- How do you ensure reliability (timeouts, retries, idempotency, monitoring)?
