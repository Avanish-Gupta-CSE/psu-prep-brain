# DBMS — 3-Tier Architecture

> Target: Explain 3-tier architecture in 30s + name each layer's job clearly.

---

## What Is 3-Tier Architecture?

A way of organizing a web application into **3 separate layers**, each with a single responsibility.
All web applications are essentially 3-tier in nature.

```
         USER (Browser / Mobile App)
               |
               | HTTP Request
               ↓
     ┌─────────────────────┐
     │   PRESENTATION LAYER │  ← Client Layer (UI)
     │   (Client 1, 2, 3)  │
     └─────────────────────┘
               |
               | Business logic call
               ↓
     ┌─────────────────────┐
     │  APPLICATION LAYER  │  ← Business Layer (App Server)
     │  (Application Server│
     │  / Business Server) │
     └─────────────────────┘
               |
               | DB query
               ↓
     ┌─────────────────────┐
     │     DATA LAYER      │  ← Database Layer
     │   (Database Server) │
     └─────────────────────┘
```

---

## The 3 Layers — What Each Does

| Layer | Also Called | Responsibility | Examples |
|---|---|---|---|
| **Presentation Layer** | Client Layer | What the user sees and interacts with | Browser, Mobile App, React UI |
| **Application Layer** | Business Layer | Processes requests, applies business logic, acts as middleman | Node.js, Express, Spring Boot |
| **Data Layer** | Database Layer | Stores and retrieves actual data | MySQL, PostgreSQL, MongoDB |

---

## Key Rules from the Ebook

- **No direct communication between Client and Database** — the Application layer always sits in between
- **Application Server** = the middle layer; exchanges partially processed data between client and DB
- **Schema** = a logical representation of the database. One database can have multiple schemas.

---

## Why 3-Tier? (Interview Explanation)

| Problem with 1-tier / 2-tier | How 3-tier solves it |
|---|---|
| Client talks directly to DB — security risk | App layer acts as a gatekeeper |
| Business logic mixed with UI — hard to maintain | Separation of concerns |
| Scaling is hard if everything is together | Each layer can scale independently |
| One change breaks everything | Changes in one layer don't affect others |

---

## Real-World Example (Your Work at Berkadia)

```
Browser (React UI)
      ↓
Node.js / Express API Server   ← middle layer, applies auth (Keycloak), business logic
      ↓
PostgreSQL / Elasticsearch     ← stores documents, search indexes
```

---

## Your 30-Second Script

> *"3-tier architecture splits an application into three layers. The presentation layer is what
> the user sees — the browser or mobile app. The application layer, also called the business
> layer, sits in the middle — it processes requests, applies business logic, and talks to both
> sides. The data layer is the database — it stores and retrieves data. The key rule is that
> the client never talks directly to the database — all communication goes through the
> application server."*

---

## Follow-Up Questions (Expect These)

**Q: What is the difference between 2-tier and 3-tier architecture?**
> In 2-tier, the client talks directly to the database — no application server. Faster but less secure and harder to scale. 3-tier adds the middle application layer for security, logic separation, and scalability.

**Q: What is a schema in DBMS?**
> A schema is a logical representation of the database — it defines the tables, columns, relationships, and constraints. One database server can host multiple schemas.

**Q: Can there be more than 3 tiers?**
> Yes — n-tier architecture. Microservices is an example where the application layer is split into many independent services. But the classic interview answer is 3-tier.
