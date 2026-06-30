# 01. Relational Databases (DBMS) in Banking

In a commercial bank like UCO Bank, database reliability, consistency, and speed are the cornerstones of operations. This note covers the core DBMS concepts with a direct banking lens.

---

## 1. ACID Properties (The Transactional Foundation)

A database transaction is a logical unit of work. In banking, every transaction must strictly adhere to ACID properties to prevent financial discrepancies.

### The Fund Transfer Scenario (The Standard Interview Example)
*Scenario*: Customer A (Avanish) wants to transfer ₹10,000 to Customer B.
*Database Operations*:
1. Read Balance of A ($B_A$)
2. Check if $B_A \ge 10,000$ (Constraint Check)
3. $B_A = B_A - 10,000$ (Debit)
4. Write $B_A$ back to database
5. Read Balance of B ($B_B$)
6. $B_B = B_B + 10,000$ (Credit)
7. Write $B_B$ back to database
8. Log transaction in ledger table

### ACID Breakdown

#### A - Atomicity (All-or-Nothing)
*   **Definition**: Ensures that either all operations of a transaction are executed successfully, or none are. There is no partial execution.
*   **Banking Context**: If the system crashes or network connection drops at step 5 (after debiting A but before crediting B), the database must perform a **ROLLBACK** operation. The ₹10,000 is returned to A's account.
*   **Mechanism**: Managed by the **Transaction Manager** using the **Undo/Redo Logs** (Write-Ahead Logging - WAL).

#### C - Consistency (State Integrity)
*   **Definition**: A transaction must transition the database from one valid state to another, preserving all integrity constraints, rules, and triggers.
*   **Banking Context**: 
    *   *Conservation of Money*: The sum of balances before and after the transaction must remain constant ($B_{A\_pre} + B_{B\_pre} = B_{A\_post} + B_{B\_post}$).
    *   *Schema Constraints*: If A's balance drops below a minimum threshold (e.g., zero), the database's check constraint must trigger a rollback.
*   **Mechanism**: Enforced by the database engine's constraint-checking systems (Foreign Keys, Check Constraints, Unique Keys).

#### I - Isolation (Concurrency Control)
*   **Definition**: Concurrent execution of transactions must leave the database in the same state as if they were executed sequentially.
*   **Banking Context**: If Avanish has ₹10,000 and attempts to withdraw ₹10,000 from an ATM at the exact same millisecond that an automated EMI debit of ₹10,000 hits his account, the database must isolate these transactions. One must execute first (succeeding), and the second must fail due to insufficient funds.
*   **Mechanism**: Managed by the **Concurrency Control Manager** using **Locking protocols** or **Multiversion Concurrency Control (MVCC)**.

#### D - Durability (Permanence)
*   **Definition**: Once a transaction commits, its changes are permanently written to non-volatile storage (disk) and will not be lost even in the event of a total system crash or power outage.
*   **Banking Context**: Once the ATM screen displays "Transaction Successful," that record is committed. If the bank's servers lose power a millisecond later, the balance remains updated when the system reboots.
*   **Mechanism**: Managed by the **Recovery Manager** using **Write-Ahead Logging (WAL)**. Changes are written to the log file on disk *before* they are written to the actual database pages.

---

## 2. Concurrency Phenomena & Isolation Levels

When multiple users access the database concurrently, several anomalies can occur if transactions are not properly isolated.

### Concurrency Anomalies
1.  **Dirty Read (Read Uncommitted Data)**: Transaction $T_1$ modifies a row. Transaction $T_2$ reads the modified row *before* $T_1$ commits. If $T_1$ rolls back, $T_2$ has read data that technically never existed.
    *   *Banking Risk*: A customer sees a credited amount that is subsequently rolled back due to a failure.
2.  **Non-Repeatable Read (Un-isolated Updates)**: Transaction $T_1$ reads a row. Transaction $T_2$ modifies or deletes that row and commits. If $T_1$ reads the same row again, it finds a different value.
    *   *Banking Risk*: A branch manager running an audit report sees an account balance change mid-report.
3.  **Phantom Read (Un-isolated Insertions)**: Transaction $T_1$ reads a set of rows matching a search condition. Transaction $T_2$ inserts new rows matching the condition and commits. If $T_1$ runs the query again, a "phantom" row appears.
    *   *Banking Risk*: A query counting the number of active high-value loans returns a different count within the same transaction.

### SQL Standard Isolation Levels
Databases trade off isolation for performance. Higher isolation levels prevent more anomalies but reduce concurrency.

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Locking Mechanism |
| :--- | :---: | :---: | :---: | :--- |
| **Read Uncommitted** | Allowed | Allowed | Allowed | No read locks. Writes hold exclusive locks. |
| **Read Committed** | Prevented | Allowed | Allowed | Shared locks on reads are released immediately after reading. |
| **Repeatable Read** | Prevented | Prevented | Allowed | Shared locks on reads are held until the transaction ends. |
| **Serializable** | Prevented | Prevented | Prevented | Range/Predicate locks are held until transaction ends. |

*Note*: PostgreSQL implements **Repeatable Read** in a way that also prevents Phantom Reads using MVCC, making it exceptionally robust for banking digital channels.

---

## 3. Database Indexing (B+ Trees)

An index is a separate data structure that speeds up query retrieval at the cost of additional write overhead and disk space.

### B-Trees vs. B+ Trees
Most relational databases (including PostgreSQL and Oracle used in banking) use **B+ Trees** for indexing.

```
          [  50  ]             <-- Root Node (Index keys only)
         /        \
     [ 25 ]      [ 75 ]        <-- Internal Nodes (Index keys only)
     /    \      /    \
  [10,20]->[30,40]->[60,70]->[80,90] <-- Leaf Nodes (Keys + Data Pointers + Linked List)
```

### Why B+ Trees are Superior for Databases:
1.  **High Fan-Out / Branching Factor**: B+ Trees are extremely wide and shallow. A node can hold hundreds of keys. This keeps the tree height low (typically 3 or 4 levels even for millions of rows), minimizing slow **Disk I/O** operations.
2.  **Data Only in Leaf Nodes**: In a B-Tree, keys and data pointers are stored in all nodes. In a B+ Tree, internal nodes only store keys (routing guides), and actual data pointers are stored **only** in the leaf nodes. This allows internal nodes to hold more keys, further increasing fan-out.
3.  **Leaf Node Linked List**: All leaf nodes in a B+ Tree are linked together in a doubly-linked list. This makes **Range Queries** (e.g., `SELECT * FROM tx WHERE date BETWEEN '2026-06-01' AND '2026-06-15'`) incredibly fast. The database engine performs a binary search to find the start node, and then simply traverses the linked list.

### Banking Application
*   **Scenario**: A customer requests their transaction history. The database table `transactions` has 500 million rows.
*   **Without Index**: The database must perform a **Full Table Scan** (sequential read of all 500M rows), taking several minutes and crashing database performance.
*   **With Index on `(account_id, transaction_date)`**: The database traverses the B+ Tree in $O(\log N)$ steps (typically 3-4 disk reads), finding the customer's records in under 10 milliseconds.

---

## 4. Normalization vs. De-normalization

### Normalization (Data Integrity)
Normalization is the process of decomposing tables to eliminate data redundancy and prevent update, insertion, and deletion anomalies.
*   **1NF**: Atomic values (no multi-valued attributes).
*   **2NF**: In 1NF + no partial dependencies (non-prime attributes must depend on the *entire* primary key).
*   **3NF**: In 2NF + no transitive dependencies (non-prime attributes cannot depend on other non-prime attributes).
*   **BCNF (Boyce-Codd Normal Form)**: A stronger version of 3NF. For every functional dependency $X \rightarrow Y$, $X$ must be a super key.

*Why Core Banking is Highly Normalized*: Core Banking Solutions (CBS) like Finacle use highly normalized relational databases (3NF/BCNF). This ensures that customer details, balances, and account statuses are stored in exactly **one** place. An update to a mobile number or balance happens in a single row, eliminating any risk of data inconsistency across the system.

### De-normalization (Read Performance)
De-normalization is the intentional introduction of redundancy to optimize read performance by avoiding expensive SQL joins.

*Your Berkadia Connection*:
> "In our Document Management System (DMS) at Berkadia, we used a highly normalized **PostgreSQL** database to ensure transactional integrity and strict access control. However, for read-heavy, complex search queries across millions of files, SQL joins were too slow. To solve this, we de-normalized the document metadata and synced it in real-time into **Elasticsearch**. This allowed us to perform sub-second full-text searches without putting any query load on our core transactional database. This hybrid approach is highly relevant for UCO Bank's digital channels: keeping the core ledger highly normalized and consistent, while de-normalizing customer-facing search indexes for speed."

---

## 5. Locking Mechanisms & Concurrency Control

To enforce isolation, database engines use locks to restrict concurrent access to data rows.

### Lock Types
1.  **Shared Lock (S-Lock / Read Lock)**: Multiple transactions can hold a shared lock on a row simultaneously to read it. No transaction can modify the row while an S-lock is held.
2.  **Exclusive Lock (X-Lock / Write Lock)**: Only one transaction can hold an exclusive lock on a row to modify it. No other transaction can read or write to this row while the X-lock is held.

### Two-Phase Locking (2PL)
A protocol that guarantees serializability. It consists of two phases:
1.  **Growing Phase**: Transaction may acquire locks but cannot release any.
2.  **Shrinking Phase**: Transaction may release locks but cannot acquire new ones.

### Pessimistic vs. Optimistic Locking
*   **Pessimistic Locking**: Assumes conflicts are highly likely. It locks the row immediately when read (e.g., `SELECT ... FOR UPDATE` in SQL). Other transactions must wait until this transaction commits and releases the lock.
    *   *Banking Use Case*: Processing a high-frequency account balance debit where double-spending must be prevented.
*   **Optimistic Locking**: Assumes conflicts are rare. It does not lock the row during reading. Instead, it includes a version number or timestamp in the row. When updating, it checks if the version has changed (e.g., `UPDATE accounts SET balance = 5000, version = version + 1 WHERE id = 123 AND version = 2`). If the update returns 0 affected rows, a conflict occurred, and the transaction is retried.
    *   *Banking Use Case*: Updating non-critical customer profile details (e.g., email address) where concurrent updates are extremely rare.
