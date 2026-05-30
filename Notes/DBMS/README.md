# DBMS — Study Notes Index

> Personal interview-prep notes. Format: Rule + Example + 40s script + Follow-ups.
> All topics are interview-answer ready. Update this file when new notes are added.

---

## Files in This Folder

| File | Topics Covered | Status |
|---|---|---|
| `01-KEYS-AND-CONSTRAINTS.md` | Super, Candidate, Primary, Alternate, FK, UK, Composite + 6 Constraints | ✅ Done |
| `02-NORMALIZATION.md` | 1NF, 2NF, 3NF, BCNF — with examples and 40s scripts | ✅ Done |
| `03-JOINS-AND-ER.md` | All JOIN types, ON vs WHERE, ER model basics | ✅ Done |
| `04-SQL-TRAPS.md` | 8 must-know SQL traps with Wrong/Correct/Follow-up | ✅ Done |
| `05-DBMS-TYPES.md` | Hierarchical, Network, Relational, Object-Oriented + ER Model clarification | ✅ Done |
| `06-3-TIER-ARCHITECTURE.md` | 3-tier architecture, layers, schema, 2-tier vs 3-tier | ✅ Done |
| `07-SQL-COMMANDS.md` | DDL/DML/DCL/TCL — all commands, DROP vs TRUNCATE vs DELETE | ✅ Done |
| `08-ACID-AND-RELATIONAL-MODEL.md` | ACID properties (with bank examples), Isolation levels + 3 anomalies, Relational model terms, Degree vs Cardinality | ✅ Done |
| `09-ER-MODEL.md` | ER Model components, 4 attribute types, 4 cardinalities, Integrity Constraints (Domain/Entity/Referential/Key) | ✅ Done |
| `10-RELATIONAL-ALGEBRA.md` | 6 RA operations (σ π ∪ − × ρ), SQL structure, WHERE clause, SET ops (UNION/INTERSECT/MINUS) | ✅ Done |
| `11-FUNCTIONAL-DEPENDENCY.md` | FD definition, Trivial/Non-Trivial/Completely Non-Trivial, Armstrong’s 3 Axioms | ✅ Done |
| `12-AGGREGATE-FUNCTIONS-AND-TRIGGERS.md` | COUNT/SUM/AVG/MIN/MAX with NULL traps, Triggers (BEFORE/AFTER), AVG trap | ✅ Done |

---

## Revision Order (Follow This Sequence)

This is the **ebook-aligned order** for revision. Go through files in this sequence — each one builds on the previous.

```
Step 01 → 05-DBMS-TYPES.md          DBMS types (Hierarchical/Network/Relational/OO)
Step 02 → 06-3-TIER-ARCHITECTURE.md 3-tier architecture + schema
Step 03 → 07-SQL-COMMANDS.md        DDL/DML/DCL/TCL + DROP vs TRUNCATE vs DELETE
Step 04 → 08-ACID-AND-RELATIONAL-MODEL.md  ACID + Isolation anomalies + Relational terms
Step 05 → 09-ER-MODEL.md            ER Model + Integrity constraints
Step 06 → 01-KEYS-AND-CONSTRAINTS.md  All key types + SQL examples
Step 07 → 10-RELATIONAL-ALGEBRA.md  6 RA ops + SQL structure + SET operations
Step 08 → 03-JOINS-AND-ER.md        JOIN types + ON vs WHERE + worked examples
Step 09 → 04-SQL-TRAPS.md           8 SQL traps (do these AFTER JOINs)
Step 10 → 11-FUNCTIONAL-DEPENDENCY.md  FD types + Armstrong's axioms
Step 11 → 02-NORMALIZATION.md       Anomalies + Decomposition + 1NF→3NF + BCNF
Step 12 → 12-AGGREGATE-FUNCTIONS-AND-TRIGGERS.md  Aggregates + Triggers
```

> **Quick revision (day before interview):** Steps 03, 04, 08, 09, 11 only.
> **Full revision (2–3 days out):** All 12 steps in order.

---

## Quick Cheat — One Line Per Topic

```
Keys        → Super ⊃ Candidate ⊃ {Primary, Alternate}; FK links tables; UK allows one NULL
Constraints → NOT NULL, UNIQUE, PK, FK, CHECK, DEFAULT
1NF         → atomic values, no repeating groups
2NF         → no partial dependency (non-key depends on FULL composite PK)
3NF         → no transitive dependency (non-key depends on non-key)
JOINs       → INNER=match, LEFT=all left, RIGHT=all right, FULL=all both, CROSS=cartesian
ER Model    → Entity(rect), Attribute(oval), Relationship(diamond); Cardinality 1:1/1:N/M:N
SQL Trap 1  → COUNT(*) counts NULLs; COUNT(col) skips NULLs
SQL Trap 2  → WHERE on right table kills LEFT JOIN → move to ON clause
SQL Trap 3  → NOT IN + NULL subquery = empty result; use NOT EXISTS
SQL Trap 4  → WHERE before GROUP BY; HAVING after aggregation
SQL Trap 5  → NULL = NULL is UNKNOWN; use IS NULL
SQL Trap 6  → 1-to-many JOIN inflates SUM/COUNT; pre-aggregate first
SQL Trap 7  → UNION deduplicates (slow); UNION ALL keeps dupes (fast)
SQL Trap 8  → AND > OR precedence; always parenthesize mixed conditions
DBMS Types  → Hierarchical(tree), Network(graph), Relational(tables), OO(objects)
3-Tier      → Client(UI) → App Server(logic) → DB; no direct client-DB communication
DDL         → CREATE, ALTER, DROP, TRUNCATE → changes structure → auto-committed
DML         → SELECT, INSERT, UPDATE, DELETE → changes data → can rollback
DCL         → GRANT, REVOKE → controls access
TCL         → COMMIT, ROLLBACK, SAVEPOINT → controls transactions
DROP        → removes table+structure (DDL, no rollback)
TRUNCATE    → removes all rows, keeps structure (DDL, no rollback, fast)
DELETE      → removes specific rows (DML, can rollback, fires triggers)
ACID        → Atomicity(all-or-nothing), Consistency(valid→valid), Isolation(no interference), Durability(survives crash)
Isolation   → 3 anomalies: Dirty Read, Non-Repeatable Read, Phantom Read
            → 4 levels: Read Uncommitted < Read Committed < Repeatable Read < Serializable(strictest)
Degree      → number of columns in a table
Cardinality → number of rows in a table (different from ER cardinality!)
ER Model    → Entity(rect), Attribute(oval), Relationship(diamond) — design blueprint, NOT a DBMS type
Attributes  → Simple, Key(underlined), Composite(sub-ovals), Multivalued(double oval), Derived(dashed oval)
Cardinality → 1:1 (Passport), 1:M (Dept→Emp), M:1 (reverse), M:M (Emp→Project via junction table)
Integrity   → Domain(valid values), Entity(PK not null), Referential(FK matches PK), Key(PK unique)
Surrogate   → artificial auto-generated key (auto-increment id); stable, not from business data
Compound    → same as Composite key (2+ columns together form the key)
RA ops      → σ(WHERE/rows), π(SELECT/cols), ∪(UNION), −(EXCEPT), ×(CROSS JOIN), ρ(AS alias)
SQL struct  → FROM(cartesian), WHERE(select predicate), SELECT(project)
SET ops     → UNION(dedup), UNION ALL(keep dupes), INTERSECT(common), MINUS/EXCEPT(A not B)
FD          → X→Y means X determines Y; Trivial(Y⊆X), Non-Trivial(Y⊄X), Completely NT(X∩Y=∅)
Armstrong   → Reflexivity(Y⊆X ⇒ X→Y), Augmentation(X→Y ⇒ XZ→YZ), Transitivity(X→Y,Y→Z ⇒ X→Z)
Aggregates  → COUNT(*all), COUNT(col/no null), SUM, AVG(divides by non-NULLs!), MIN, MAX
Trigger     → auto-fires on INSERT/UPDATE/DELETE; BEFORE(validate) or AFTER(audit/log)
Anomalies   → Update(inconsistent copies), Delete(accidental loss), Insert(forced dummy data)
Decompose   → Lossless(rejoin = original) + Dependency Preserving(FDs checkable in sub-tables)
```

---

## Topics To Add Next

- [x] ER Model — entities, attributes, relationships, weak entity, cardinality, integrity constraints (✅ done in 09)
- [x] Relational Algebra — all 6 operations with examples (✅ done in 10)
- [x] Functional Dependency — trivial vs non-trivial, Armstrong’s Axioms (✅ done in 11)
- [x] Aggregate Functions + Triggers (✅ done in 12)
- [ ] Indexing — B-tree vs Hash, clustered vs non-clustered
- [ ] Concurrency control — locks, deadlock
