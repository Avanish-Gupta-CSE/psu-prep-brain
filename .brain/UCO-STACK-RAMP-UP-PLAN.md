# UCO Stack Ramp-Up — 12-Week Stabilisation Plan

**Created:** 21 Oct 2026 · **Status:** ACTIVE from Mon 26 Oct 2026
**Companions:** [`PHASE-8-TRAINING-AND-EXIT-STRATEGY.md`](../UCOBank/PHASE-8-TRAINING-AND-EXIT-STRATEGY.md) · `GATE-DECISION-MODEL.md` · `NextSteps.md`
**Live version:** https://avanish-gupta-cse.github.io/psu-prep-brain/stack.html

---

## §0 — The real problem, stated plainly

You have shipped code you cannot fully defend, written with AI assistance, and you now have to
work in a bank DIT where you will be asked to explain it — and to write new code without that assistance.

**That is not an unusual position in 2026.** It is the normal state of every developer who learned
during the AI era. But it is a position that must be *converted*, and it converts in about 90 days
of deliberate practice — not by going back to Chapter 1 of a Java tutorial.

### The three things that are actually true

| Fear | Reality |
| :--- | :--- |
| "I can't code without AI" | **True today, false in ~90 days** — if the practice is *reconstruction*, not tutorials. You already read and modify this codebase 8 hours a day. That is your practice ground; you need zero extra hours. |
| "The team will find out" | They will find out *something* eventually. The question is whether they find out from you, calmly, or from a production incident. **§7 makes it the former.** |
| "I have no time to learn" | You have ~40 minutes inside the workday that you currently spend re-reading. Redirecting it is the entire plan. **No evenings, no weekends, no extra hours.** |

### The single thesis

> **You do not need more hours. You need to stop reading code and start reconstructing it.**
>
> 15 deliberate minutes a day beats two hours of tutorials, because the artefact you are rebuilding
> is the exact system you must defend tomorrow morning.

---

## §1 — The actual stack (verified from the codebase, 21 Oct 2026)

| Layer | Component | Version | Where |
| :--- | :--- | :--- | :--- |
| Language | **Java** | 17 (records, sealed, switch expressions) | `backend/pom.xml` |
| Framework | **Spring Boot** | 3.2.5 → **Jakarta EE 10** (`jakarta.*`, not `javax.*`) | parent |
| Web | spring-boot-starter-web | — | MVC + embedded Tomcat |
| Data | spring-boot-starter-data-jpa | Hibernate 6.x | repositories |
| Security | spring-boot-starter-security | 6.x | filter chain |
| Tokens | **jjwt** api/impl/jackson | 0.12.5 | JWT issue + verify |
| Validation | spring-boot-starter-validation | Jakarta Bean Validation 3.0 | `@Valid` |
| Database | **Oracle** (XE 21c in Docker, 11g/19c at bank) | `ojdbc11` | `docker-compose.yml` |
| Exports | **Apache POI** | 5.2.5 | Excel generation |
| Migrations | **Plain SQL**, no Flyway | `00`–`03_*.sql` | `db_migrations/` |
| Frontend | **React** | 19.2 | `frontend/` |
| Routing | react-router-dom | 7.18 | SPA routes |
| Build | **Vite** + TypeScript | 8.3 / 6.0 | `npm run build:uat` |
| Lint | oxlint | 1.81 | CI-ish |
| Codebase | 32 Java files, package `in.co.ucobank.ucorealty` | | |

**Three gotchas that will bite a beginner specifically here:**

1. **Jakarta, not javax.** Every `javax.persistence.*` import is wrong in Spring Boot 3. It is `jakarta.persistence.*`. Tutorials older than 2023 will teach you the wrong one.
2. **Spring Security 6 has no `WebSecurityConfigurerAdapter`.** Every pre-2022 tutorial uses that class. It is deleted. You configure a `SecurityFilterChain` bean instead.
3. **jjwt 0.12.x changed its API** from 0.9/0.11. `Jwts.parser().verifyWith(key)` replaces `setSigningKey`. Old examples compile-fail.

> **Rule:** if a tutorial is older than 2023, it is teaching you a framework that no longer exists. Check the date before you read it.

---

## §2 — Skill-gap matrix

Honest self-assessment. Mark each row monthly in the ramp journal.

| # | Layer | Component | Today | Day 90 | Day 180 | Proof of mastery |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Language | Java 17 core | Partial | Solid | Solid | Explain collections, generics, streams, exceptions, GC basics |
| 2 | Framework | Spring Boot lifecycle | Beginner | Working | Solid | Trace a request end-to-end from memory |
| 3 | Framework | Dependency injection | Beginner | Working | Solid | Explain constructor vs field injection and why order matters |
| 4 | Web | Controllers / REST | Partial | Working | Solid | Write a new endpoint unaided |
| 5 | Data | Spring Data JPA | Beginner | Working | Solid | Derived queries, pagination, N+1 diagnosis |
| 6 | Data | Transactions | Beginner | Working | Solid | Explain propagation + rollback rules |
| 7 | DB | Oracle SQL | Good | Strong | Strong | Window functions, joins, constraints |
| 8 | DB | EXPLAIN PLAN / indexing | None | Basic | Working | Tune a slow query and prove it |
| 9 | DB | PL/SQL | None | Read-only | Basic | Read a package and explain it |
| 10 | Security | Authn / authz | Beginner | Working | Solid | Audit every endpoint for missing role checks |
| 11 | Security | JWT | Beginner | Working | Solid | Issue, verify, expire, refresh |
| 12 | Security | OWASP / IDOR | None | Basic | Working | Find and fix a real vulnerability in own code |
| 13 | Testing | JUnit 5 + Mockito | Weak | Working | Solid | 80% coverage on one service |
| 14 | Build | Maven | Weak | Basic | Working | Profiles, dependency conflicts, packaging |
| 15 | Frontend | React 19 + TS | Partial | Working | Solid | Form + table + API + error states, unaided |
| 16 | Ops | Deploy / logs | Partial | Basic | Working | Clean-clone deploy + rollback |
| 17 | Domain | Banking / CBS | None | Aware | Basic | Explain GL, maker-checker, reconciliation |
| 18 | Governance | Change mgmt / audit | None | Aware | Basic | Know CAB, UAT, VAPT, IS-audit |

**Priority order if everything can't be done: 2 → 4 → 5 → 10 → 13 → 6.** Those six carry 80% of the "can he be trusted" question.

---

## §3 — The 12-week schedule

One theme per week. Each week has exactly one **deliverable** — something you can show.

| Wk | Dates | Theme | Deliverable (must exist by Friday) |
| :-: | :--- | :--- | :--- |
| **1** | 26 Oct – 1 Nov | **Terrain map** | One-page diagram: URL → Controller → Service → Repository → Oracle → JSON. Inventory of all 32 files with a one-line purpose each. |
| **2** | 2 – 8 Nov | **Framework skeleton** | Explain 5 files aloud, no notes: app class, one controller, one service, one repository, one entity |
| **3** | 9 – 15 Nov | **Controllers & HTTP** | New **read-only** endpoint written unaided (no AI, no copy-paste) |
| **4** | 16 – 22 Nov | **Services & transactions** | One service method + why `@Transactional` is or isn't needed on it, in writing |
| **5** | 23 – 29 Nov | **JPA & entities** | Map 3 entities to their Oracle tables by hand; verify in SQL client |
| **6** | 30 Nov – 6 Dec | **Oracle & performance** | Tune one slow query; before/after `EXPLAIN PLAN` saved |
| **7** | 7 – 13 Dec | **Security I — auth** | Written audit: every endpoint × required role × what happens with no role |
| **8** | 14 – 20 Dec | **Security II — flaws** | Two real vulnerabilities fixed in the repo (start with `adminList` fails-open and `submit` IDOR) |
| **9** | 21 – 27 Dec | **Testing** | 80% line coverage on one service class, tests written unaided |
| **10** | 28 Dec – 3 Jan | **React** | One page: form + validation + table + API call + loading/error states |
| **11** | 4 – 10 Jan | **Build & deploy** | Clean-clone deploy: `mvn package` → jar → run → logs → rollback note |
| **12** | 11 – 17 Jan | **Own something** | One small feature shipped end-to-end: design → code → test → one-page tech note → walkthrough to manager |
| **T** | 18 Jan – 14 Feb | **GATE taper** | Maintenance only: 20 min/day reading own code. No new learning. |

### Why this order

- **Weeks 1–2 are comprehension, not production.** You cannot author what you cannot trace.
- **Weeks 3–6 build the CRUD spine** — the 80% of every enterprise app.
- **Weeks 7–8 are security** because that is the one domain where an AI-generated gap becomes a *career* problem, not a bug.
- **Week 9 is testing** because tests are the cheapest proof of understanding.
- **Weeks 10–12 convert reading into authoring.** Frontend last because it is the least load-bearing at a bank.

### The week-12 test (the only one that matters)

> **Can you describe a feature you built — and answer five "why" questions about it — without notes, to a senior developer?**

If yes, you are stabilised. If no, repeat weeks 9–12.

---

## §4 — The daily 45-minute workday method

No evenings. No weekends. Everything happens inside 10:00–18:30.

| Slot | Duration | What | Why |
| :--- | :--- | :--- | :--- |
| **End of day** | **30 min** | Take the **one file you touched today**. Explain it aloud, sentence by sentence, to an empty room. | Speaking forces retrieval; reading does not. |
| **Last 10 min** | **10 min** | Write down the **one thing you could not explain**. | That becomes tomorrow's question to a colleague. |
| **Last 5 min** | **5 min** | One line in the ramp journal: date · file · gap found · question asked. | Creates the probation evidence pack for free. |
| **Saturday** | **20 min** | **Defence drill** (§5): random file from your module, cold, explain it. | Simulates the actual risk event. |
| **Sunday** | **15 min** | Read the week's journal. Anything unexplained twice is a real gap. | Prevents silent accumulation. |

**Total: ~4 hours/week, all inside work hours.** This is the entire cost of the plan.

### The rule that makes it work

> **Never read a file twice the same way.**
> If you re-read a file and understand it "because you've seen it before," you have learned nothing.
> Close it and rewrite the core method from memory. The diff is the lesson.

---

## §5 — The defence drill

The anxiety is specific: *being asked to explain code you didn't really write.* The drill trains exactly that.

### The five questions (ask them of every file, in order)

1. **What is this file for?** — one sentence, no jargon.
2. **Who calls it, and what does it call?** — the neighbours.
3. **What breaks if I delete it?** — the blast radius.
4. **What is the single most important line, and why?** — the crux.
5. **What would I change if I owned it?** — the judgement.

If you can answer all five for a file, you own that file. If you can't answer #4, you don't.

### The reconstruct technique (the AI-dependency cure)

```
1. Open the file. Read it once, slowly.
2. CLOSE IT.
3. In a scratch file, retype the core method from memory.
4. Diff against the original.
5. Study ONLY the diff. That is your actual gap.
6. Next week, repeat. Target: empty diff.
```

**This is the highest-leverage 15 minutes in the entire plan.** AI wrote the code; reconstruction is how
you take ownership of it. Do one method per day.

### Exposure management

| Situation | Do | Don't |
| :--- | :--- | :--- |
| Asked how something works and you don't know | *"Let me trace it and come back by end of day."* Then actually come back. | Improvise. One bluff destroys more trust than ten honest "I'll check". |
| Presenting your module | Volunteer the risks before anyone asks. | Wait to be caught. |
| A senior reviews your code | Ask *"what would you have done differently?"* | Defend it. |
| You find a bug you introduced | Say so immediately, with the fix. | Fix it quietly and hope. |

> **The bank rewards reliability over brilliance.** A JMGS-I who says "I don't know yet, I'll confirm by 5 pm" and does it
> is worth more than a genius who guesses. This is genuinely true in PSU banking.

---

## §6 — The no-AI unblock protocol

When you are stuck and cannot ask an AI. **Timebox each step to 5 minutes, total 20, then ask a human.**

1. **Read the stack trace from the bottom up.** The root cause is the last "Caused by", not the first line.
2. **Reproduce it in 10 lines.** Strip everything until it breaks in isolation.
3. **Grep the codebase** for the same annotation or pattern. If it works there, diff the two.
4. **Read the official doc section**, not a blog. `spring.io/docs`, `docs.oracle.com`.
5. **Set a breakpoint.** Inspect the actual values. Beginners assume; debuggers don't.
6. **Write the question** (below), then decide whether to ask.

### The structured question script

> "I'm looking at `X`. I expected `Y` because `Z`. What I actually see is `W`. Is my mental model wrong, or is this a known quirk of the framework?"

This does three things: proves you traced it, gives the helper the exact failure, and makes you look
like an engineer rather than someone asking for code.

### Questions never to ask

- "How do I write X?" → ask *"where is an existing example of X in our codebase?"*
- "Why is this broken?" → attach the trace and your hypothesis.
- Anything answerable by 30 seconds of grepping.

---

## §7 — Question bank for the first month

Ask **one per day**. These are designed to be useful *and* to signal seriousness.

**Architecture**
1. Which module is the most critical path, and why?
2. What's the one piece of this system nobody wants to touch?
3. Where is the line between what we build and what the vendor (Finacle/CBS) owns?

**Process**
4. How does a change get from my laptop to production here?
5. Who signs off, and in what order?
6. What happens if a release breaks — who rolls it back?
7. Is there a code review step, or does it go straight to UAT?

**Data**
8. Which tables are shared with other departments, and which are ours alone?
9. Is there a data-retention or masking rule I should know before I query production?
10. How do I get read-only production access, and what's the approval chain?

**Security**
11. Where are secrets (DB passwords, JWT keys) stored, and who can read them?
12. Is there a VAPT cycle, and when is the next one?
13. What's the audit-trail requirement for the actions my module performs?

**Team**
14. What does a good week look like for you?
15. What's the most common mistake new joiners make here?
16. Who should I go to for Oracle questions vs Spring questions?
17. Is there a design doc or an architecture diagram anywhere?

**Growth**
18. What would make you confident I can own a module on my own?
19. Which part of this codebase would you want rewritten, if you had a month?
20. What should I read to be useful faster?

> **Question 18 is the most important one in this list.** It tells you the actual promotion criteria,
> and it tells your manager that you are thinking about ownership rather than survival.

---

## §8 — Probation confirmation evidence

PSU bank probation is confirmed on **conduct, attendance, integrity and work quality** — not on
whether you can invert a binary tree. But "work quality" needs evidence, and evidence needs to be collected
before it is asked for.

### The evidence pack (update weekly, 5 minutes)

| Item | Cadence | Where |
| :--- | :--- | :--- |
| Ramp journal (file · gap · question) | Daily | notebook |
| Weekly 1-page manager update (done / next / blocked) | Weekly | email |
| Delivered items log (what shipped, when) | Weekly | journal |
| Known-risks list (volunteered, not discovered) | Monthly | email to manager |
| Code reviews received and acted on | Per review | journal |
| One security/quality fix you found yourself | By week 8 | repo + note |

### The monthly 15-minute 1:1 script

> "Here's what I shipped this month. Here's what I found and fixed. Here's what I still don't understand.
> Is there anything you'd want me to prioritise differently?"

That single sentence does more for probation than any amount of silent effort, because it converts
invisible work into visible judgement.

---

## §9 — Risk register

| Risk | Likelihood | Impact | Mitigation | Owner |
| :--- | :-: | :-: | :--- | :--- |
| Asked to explain code, can't | **High** | High | §5 defence drill, §5 reconstruct | You |
| AI-written code has a security flaw that reaches prod | **High** | High | Weeks 7–8 audit; fix `adminList` fails-open + `submit` IDOR | You |
| Tutorials teach obsolete APIs (javax, WebSecurityConfigurerAdapter) | High | Medium | §1 gotcha list; check publish date | You |
| Burnout from job + exam track | Medium | High | 45-min cap; no weekend coding; GATE taper week 13 | You |
| Manager forms a low opinion in month 1–2 | Low | High | Weekly 1-page update; monthly 1:1 | You |
| Probation extended | Low | High | §8 evidence pack | You |
| Silent gap accumulation | Medium | Medium | Sunday 15-min journal review | You |
| Production access misuse / data exposure | Low | **Critical** | Never query prod without approval; no data on personal devices | You |

---

## §10 — Measurement rubric

Score yourself 0–5 on the first of each month. **Target: 3 by day 90, 4 by day 180.**

| # | Capability | Day 0 | Day 30 | Day 90 | Day 180 |
| :-: | :--- | :-: | :-: | :-: | :-: |
| 1 | Explain any file in my module, cold | 0 | 2 | 4 | 5 |
| 2 | Make a change to existing code without AI | 0 | 1 | 3 | 4 |
| 3 | Write a new endpoint without AI | 0 | 0 | 3 | 4 |
| 4 | Read a stack trace and locate the fault | 1 | 2 | 4 | 5 |
| 5 | Write a unit test without AI | 0 | 1 | 3 | 4 |
| 6 | Read an EXPLAIN PLAN and act on it | 0 | 0 | 2 | 4 |
| 7 | Spot a security flaw in a review | 0 | 1 | 3 | 4 |
| 8 | Design a small feature and defend it | 0 | 1 | 3 | 4 |
| **Mean** | | **0.1** | **1.0** | **3.1** | **4.3** |

If the day-90 mean is below 2, **do not continue to week 13** — repeat weeks 3–6. A repeated month is cheaper than a probation year.

---

## §11 — Reading list (short, and dated for a reason)

| Priority | Resource | Scope | Time |
| :-: | :--- | :--- | :--- |
| **1** | `spring.io/guides` — *Building a RESTful Web Service* | The canonical CRUD | 2 h |
| **2** | Spring Boot 3.2 **reference docs**, sections: *Core Features* → *External Configuration*, *Profiles* | How the app boots | 3 h |
| **3** | Spring Security 6 reference — *Authentication* → *Form/HTTP Basic*, *Method Security* | The filter chain | 2 h |
| **4** | Oracle **Concepts** guide, Ch. 3 (Data Access) + Ch. 12 (Indexes) | How Oracle reads | 3 h |
| **5** | `docs.oracle.com` — *EXPLAIN PLAN* + *Autotrace* | Query tuning | 1 h |
| **6** | OWASP **Top 10 (2021)** — just A01, A03, A07 | What auditors check | 2 h |
| **7** | *Effective Java* (Bloch, 3rd ed) — Items 1, 10, 17, 34, 50 | How seniors think | 4 h |
| **8** | React docs — *Describing the UI*, *Adding Interactivity*, *Managing State* | Hooks mental model | 4 h |
| **9** | Hibernate 6 user guide — *Associations*, *Fetching* | The N+1 problem | 2 h |

**Excluded deliberately:** video courses, "complete bootcamp" series, and anything teaching `javax.*`.
They cost 40+ hours and produce reading fluency, not writing ability.

---

## §12 — What "stabilised" actually looks like

| Day | You can | You are not yet |
| :--- | :--- | :--- |
| **30** | Explain every file in your module. Trace any endpoint. Name the three riskiest spots. | Authoring anything new unaided |
| **60** | Modify existing code without AI. Write a stack trace down to the line. Pass a code review with only minor comments. | Designing |
| **90** | **Author a small feature end-to-end, test it, document it, defend it under five "why" questions.** | Owning a module |
| **180** | Own a module. Estimate work. Spot flaws in others' code. Be the person asked about one subsystem. | Leading |
| **365** | Design features, defend architecture, mentor a newer joiner. | — |

> **Day 90 is the real goal.** It is the point where the question stops being
> *"can he do this?"* and becomes *"when can he start the next thing?"*

---

## §13 — What this buys you outside the bank

The same 12 weeks produce a second asset, for free:

| Skill | Bank value | Corporate value |
| :--- | :--- | :--- |
| Spring Boot 3.2 + Java 17 | Ship internal apps | **The single most in-demand backend stack in India** |
| JPA + Oracle | Internal systems | Directly transferable to any enterprise |
| Spring Security + JWT | Pass IS-audit | Top-3 interview topic |
| JUnit + Mockito | Probation quality proof | Every interview asks for it |
| React 19 + TypeScript | The UCO Realty UI | Front-end qualification |
| Explaining code under questioning | Manager confidence | **Literally the interview** |

> The stabilisation plan and the exit plan are the same plan. You are not choosing between
> being good at this job and leaving it. **Competence is the prerequisite for both.**

---

## §14 — First seven days (26 Oct – 1 Nov)

Concrete, doable, no ambiguity.

| Day | Action | Time |
| :--- | :--- | :--- |
| **Mon 26** | `docker compose up -d oracle` · `mvn spring-boot:run` · `npm run dev`. Get it running locally. | 45 min |
| **Tue 27** | Open `pom.xml`. For each dependency, write one line: what it enables. | 30 min |
| **Wed 28** | Pick ONE endpoint. Trace URL → Controller → Service → Repository → table. Draw it. | 40 min |
| **Thu 29** | *(ISRO exam — no ramp work)* | — |
| **Fri 30** | Reconstruct one method from memory. Diff. Study the diff. | 20 min |
| **Sat 31** | Defence drill on the file you traced Wednesday. | 20 min |
| **Sun 1** | Read the week's journal. List the 3 biggest gaps. | 15 min |

**Week 1 deliverable:** one page containing the architecture diagram, the dependency list, and the
three biggest gaps. That page is the starting point for the whole plan.

---

> **One line:** *You don't need to become a great programmer. You need to become a programmer who can
> explain his own code — and that is a 90-day, 45-minutes-a-day problem, not a talent problem.*
