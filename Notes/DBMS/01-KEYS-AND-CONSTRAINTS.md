# DBMS — Keys & Constraints

> Target: Explain PK vs UK vs FK in 40s. Know the full key hierarchy cold.

---

## The Key Hierarchy

```
Super Key  (broadest — any combo that gives uniqueness, can be redundant)
    └── Candidate Key  (minimal super key — no column can be removed)
              ├── Primary Key    (chosen candidate key; NOT NULL, one per table)
              ├── Alternate Key  (remaining candidate keys not chosen)
              └── Unique Key     (like PK but allows one NULL; multiple per table)

Foreign Key   → links to another table's PK (referential integrity)
Composite Key → two or more columns together form the key
```

---

## One Table, All Keys Explained

**Table: students**

| StudentID | Email | Phone | Name |
|---|---|---|---|
| 101 | a@gmail.com | 9999 | Avanish |
| 102 | b@gmail.com | 8888 | Rahul |

| Key Type | Example | Why |
|---|---|---|
| Super Key | `{StudentID}`, `{Email}`, `{StudentID, Email}` | All uniquely identify a row |
| Candidate Key | `{StudentID}`, `{Email}`, `{Phone}` | Minimal — can't drop any column |
| Primary Key | `{StudentID}` | Chosen; no NULL allowed |
| Alternate Key | `{Email}`, `{Phone}` | Candidate keys not chosen |
| Unique Key | `{Email}` | Enforces uniqueness, allows one NULL |

---

## PK vs UK vs FK — Your 40-Second Script

> *"PK uniquely identifies every row — no NULLs allowed, and there can only be one per table.
> UK also enforces uniqueness but allows one NULL, and you can have multiple UKs in a table.
> FK is a column in one table that points to the PK of another table — it enforces referential
> integrity, meaning you can't reference a row that doesn't exist."*

---

## Primary Key vs Unique Key — Side by Side

| Feature | Primary Key | Unique Key |
|---|---|---|
| Uniqueness | ✅ | ✅ |
| NULL allowed | ❌ Never | ✅ One NULL per column |
| Count per table | Only **one** | **Multiple** allowed |
| Index created | Clustered index | Non-clustered index |
| Can be FK target | ✅ Yes | ✅ Yes (in most DBs) |

---

## Foreign Key — Referential Integrity

```sql
-- Parent table
CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);

-- Child table — dept_id references parent
CREATE TABLE employees (
  emp_id   INT PRIMARY KEY,
  name     VARCHAR(50),
  dept_id  INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- This INSERT will FAIL — dept_id 999 doesn't exist in departments
INSERT INTO employees VALUES (1, 'Avanish', 999);
```

**FK behaviors on DELETE/UPDATE of parent row:**

| Action | What happens to child rows |
|---|---|
| `CASCADE` | Child rows deleted/updated automatically |
| `SET NULL` | Child FK column set to NULL |
| `RESTRICT` | Delete blocked if child rows exist |
| `NO ACTION` | Same as RESTRICT (default in most DBs) |

---

## Composite Key (also called Compound Key)

- Two or more columns that **together** form a unique key
- Neither column alone is unique
- The ebook calls this a **Compound Key** — same concept, different name used in different books

```sql
-- Neither student_id nor course_id alone is unique
-- But (student_id, course_id) together is unique per enrollment
CREATE TABLE enrollments (
  student_id INT,
  course_id  INT,
  enrolled_on DATE,
  PRIMARY KEY (student_id, course_id)   -- composite/compound PK
);
```

---

## Surrogate Key

- An **artificial key** added purely to uniquely identify a record
- Not derived from any real-world/business data
- Usually an **auto-incremented integer** or UUID

**Why use it?**
- Natural keys (PAN, Aadhaar) can change or be long — bad for joins
- Surrogate keys are stable, short, numeric — ideal as PK

```sql
CREATE TABLE employees (
  emp_id   INT AUTO_INCREMENT PRIMARY KEY,  -- surrogate key
  pan_no   VARCHAR(10) UNIQUE,              -- natural key (business meaning)
  name     VARCHAR(50)
);
```

**Natural key vs Surrogate key:**

| | Natural Key | Surrogate Key |
|---|---|---|
| Source | Real-world data (PAN, email) | Artificially generated (1, 2, 3...) |
| Meaningful? | Yes | No (just an ID) |
| Can change? | Yes (risky) | No (stable) |
| Example | Aadhaar number | auto-increment `id` |

---

## The 6 Constraints — Quick Reference

| Constraint | Rule | Example |
|---|---|---|
| `NOT NULL` | Column must always have a value | `name VARCHAR(50) NOT NULL` |
| `UNIQUE` | No duplicate values in column | `email VARCHAR(100) UNIQUE` |
| `PRIMARY KEY` | NOT NULL + UNIQUE; one per table | `id INT PRIMARY KEY` |
| `FOREIGN KEY` | Value must exist in referenced table | `FOREIGN KEY (dept_id) REFERENCES dept(id)` |
| `CHECK` | Custom condition must be true | `CHECK (age >= 18)` |
| `DEFAULT` | Auto-fills value when none provided | `status VARCHAR(10) DEFAULT 'active'` |

> **Memory trick:** `N-U-P-F-C-D` → *"Never Use Primary Foreign Checks Defaultly"*

---

---

## Primary Key — SQL Examples (from ebook)

### CREATE TABLE with PK

```sql
CREATE TABLE PERSONS (
  ID        INT NOT NULL,
  LastName  VARCHAR(255),
  FirstName VARCHAR(255),
  Age       INT,
  PRIMARY KEY (ID)
);
```

### Add PK using ALTER TABLE

```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name
PRIMARY KEY (column1, column2, ...);
```

---

## Foreign Key — SQL Examples (from ebook)

### FK on CREATE TABLE

```sql
CREATE TABLE ORDERS (
  order_ID     INT NOT NULL,
  orderNumber  INT NOT NULL,
  personID     INT,
  PRIMARY KEY (orderID),
  FOREIGN KEY (personID) REFERENCES persons(personID)
);
```

> Rule: FK column (`personID`) and PK it references (`persons.personID`) must have the **same data type**.

---

## All Key Types — Final Summary

| Key | Definition | NULL? | Count per table |
|---|---|---|---|
| Super Key | Any combo that gives uniqueness | Allowed | Many |
| Candidate Key | Minimal super key | Not recommended | Multiple |
| Primary Key | Chosen candidate key | ❌ Never | **One only** |
| Alternate Key | Non-chosen candidate keys | Allowed | Multiple |
| Unique Key | Enforces uniqueness | ✅ One NULL | Multiple |
| Foreign Key | References PK of another table | ✅ Allowed | Multiple |
| Composite Key | 2+ columns forming a key together | Depends | Multiple |
| Surrogate Key | Artificial auto-generated key | ❌ Never | One (usually) |

---

## Follow-Up Questions (Expect These)

**Q: Can a table have no primary key?**
> Yes, technically. But it's bad practice — duplicates become possible and joins become unreliable.

**Q: Can a FK reference a Unique Key instead of a PK?**
> Yes, in most RDBMS (PostgreSQL, SQL Server). The referenced column just needs to be unique.

**Q: What is a surrogate key?**
> An artificial key added purely for identification (e.g., auto-increment `id`). Not derived from business data. Preferred when natural keys are long or composite.

**Q: What is a natural key?**
> A key that comes from real-world data (e.g., Aadhaar number, PAN). Risky if the data can change.
