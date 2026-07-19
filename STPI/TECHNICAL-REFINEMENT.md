# STPI Scientist 'B' (Level-10) Technical Refinement Sheet

*Status: Confirmed & Refined for Scientist 'B' Interview Panel (2026)*

---

## 🌐 1. System Design & Architecture (Bridging Berkadia to STPI)

The STPI Scientist 'B' role requires a technical leader who can evaluate startup products, manage state-of-the-art labs, and design robust government/enterprise architectures. You must bridge your **Berkadia experience** directly to these responsibilities.

### Q1. Explain CQRS (Command Query Responsibility Segregation). Why did you use it, and what are its trade-offs?
*   **Core Concept**: CQRS segregates the write operations (Commands) from the read operations (Queries) of an application. Instead of using a single unified data model for both, we use separate models.
*   **Why We Used It (Berkadia Context)**: In financial transaction handling, write operations (creating transactions, updating ledgers) require strict validation, ACID transactions, and complex business logic. Read operations (dashboard analytics, transaction history) require high-speed, paginated, and aggregated data. By separating them:
    *   We optimized the write database (e.g., PostgreSQL with normalized schema) for transaction safety.
    *   We optimized the read database (e.g., Read Replicas or Elasticsearch/Redis) for high-speed queries.
*   **Synchronization**: Handled via asynchronous event publishing (using a Message Broker like Kafka or RabbitMQ) to update the read store when a command succeeds.
*   **Trade-offs**:
    *   *Pros*: High scalability, independent scaling of reads/writes, optimized read schemas, and separation of concerns.
    *   *Cons*: **Eventual Consistency** (reads might be slightly behind writes during sync lag), increased system complexity, and dual data model maintenance.

### Q2. How do you design fine-grained authorization in a Microservices architecture? (Keycloak + OpenFGA)
*   **Authentication**: Handled centrally via **Keycloak SSO** (OAuth 2.0 / OIDC). Keycloak issues a cryptographically signed JWT (JSON Web Token) containing the user's identity and global roles.
*   **Fine-Grained Authorization (FGA)**: Standard Role-Based Access Control (RBAC) fails when access depends on complex relationships (e.g., "User A can edit Document X only if they are the owner or belong to the parent organization").
*   **OpenFGA (Fine-Grained Authorization)**: Based on Google's Zanzibar paper. It represents authorization as a directed graph of relationships:
    *   *Tuple*: `(document:X, "viewer", user:A)`
    *   When a microservice receives a request, it extracts the user ID from the Keycloak JWT and queries OpenFGA: `Check(user:A, "editor", document:X)`.
    *   OpenFGA resolves this graph query in sub-millisecond time, keeping authorization logic completely out of the microservice's business code.

### Q3. Describe your AI-driven document extraction pipeline (ReservesAI).
*   **Architecture**: Built an asynchronous pipeline using **Azure Document Intelligence** and **Azure AI Foundry**.
*   **Flow**:
    1.  **Ingestion**: Financial documents (PDFs, TIFFs) are uploaded to secure cloud storage.
    2.  **Extraction**: An asynchronous worker sends the document to Azure Document Intelligence (Layout/Custom Model) to extract raw text, tables, and key-value pairs.
    3.  **Processing**: The extracted JSON is structured, validated against financial schemas, and enriched using LLMs hosted on Azure AI Foundry.
    4.  **Storage**: Final structured data is saved to PostgreSQL, and search indices are updated in Elasticsearch.

---

## 💾 2. Database Management Systems (DBMS) Deep-Dive

### Q1. Why do modern databases (PostgreSQL, MySQL) use B+ Trees instead of B-Trees or Hash Tables for indexing?
*   **B+ Tree vs. B-Tree**:
    *   In a **B-Tree**, both keys and actual record pointers (data) are stored in internal and leaf nodes.
    *   In a **B+ Tree**, internal nodes store *only keys* (acting as routers), while *all actual data/pointers are stored exclusively in leaf nodes*. Additionally, leaf nodes are linked together via a **doubly linked list**.
    *   *Advantages of B+ Tree*:
        1.  **Higher Fan-out / Lower Disk I/O**: Since internal nodes don't store data pointers, they are much smaller. More keys fit into a single disk block, resulting in a higher branching factor (fan-out) and a shorter tree height. This minimizes expensive disk reads.
        2.  **Efficient Range Queries**: To perform a range query (e.g., `WHERE age BETWEEN 20 AND 30`) in a B-Tree, you must perform multiple depth-first traversals. In a B+ Tree, you find the first leaf node (20) and simply traverse the linked list of leaf nodes until you hit 30.
*   **Why not Hash Tables?**: Hash Tables offer $O(1)$ lookup but do not support range queries, sorting, or prefix matching. They are useless for `ORDER BY` or inequality operators (`>`, `<`).

### Q2. What is MVCC (Multi-Version Concurrency Control)? How does it differ from 2PL?
*   **Two-Phase Locking (2PL)**: A pessimistic concurrency control mechanism. It uses locks (Shared and Exclusive) to ensure serializability.
    *   *Problem*: **Readers block Writers, and Writers block Readers**. This severely degrades read performance in high-concurrency environments.
*   **MVCC**: An optimistic concurrency control mechanism used by PostgreSQL and Oracle.
    *   *How it works*: Instead of overwriting data or locking a row, the database maintains **multiple physical versions** of a row.
    *   Each transaction is assigned a monotonically increasing Transaction ID ($T_{\text{id}}$). When a row is updated, a new version is created with a creation timestamp ($xmin$) and deletion timestamp ($xmax$).
    *   A transaction only "sees" row versions created by transactions that committed before its own start time.
    *   *Result*: **Readers never block Writers, and Writers never block Readers**. High-throughput reads are guaranteed.

### Q3. When and why would you intentionally denormalize a database schema?
*   **Normalization** (up to BCNF) eliminates data redundancy and update anomalies by splitting tables.
*   **Denormalization** is the deliberate introduction of redundancy to optimize read performance.
*   **Why Denormalize?**:
    *   In read-heavy systems (like analytical dashboards or reporting modules), joining 5 or 6 normalized tables on every query is extremely expensive.
    *   By pre-joining tables or storing aggregated columns (e.g., storing `total_orders` in a `Customer` table), we reduce CPU overhead and disk I/O.
*   **Trade-off**: Requires application-level logic or database triggers to maintain consistency across redundant fields, introducing write overhead.

---

## ⚡ 3. Operating Systems (OS) Deep-Dive

### Q1. Compare Mutex, Semaphore, and Monitors. When is each appropriate?
*   **Mutex (Mutual Exclusion)**: A locking mechanism used to synchronize access to a single shared resource. It is **owner-based**—only the thread that locked the mutex can unlock it.
*   **Semaphore**: A signaling mechanism that uses an integer value to control access to a finite pool of resources. It has no concept of ownership.
    *   *Binary Semaphore*: Value is 0 or 1 (similar to a mutex, but can be unlocked/signaled by any thread).
    *   *Counting Semaphore*: Value represents available resource instances (e.g., database connection pool of size 10).
*   **Monitor**: A high-level programming language construct (e.g., `synchronized` blocks in Java) that encapsulates shared variables and procedures. Only one thread can be active inside a monitor at any given time. It uses **Condition Variables** (`wait()`, `notify()`) to manage thread synchronization cleanly, preventing manual locking errors.

### Q2. What is Thrashing? How does the OS detect and prevent it?
*   **Thrashing**: A state where the CPU spends more time swapping pages in and out of virtual memory (disk I/O) than executing actual instructions. It occurs when the active processes do not have enough physical frames to hold their "working sets".
*   **Detection**: The OS monitors CPU utilization vs. paging rate. If CPU utilization drops while disk queuing/paging spikes, thrashing is occurring.
*   **Prevention**:
    *   **Working Set Model**: The OS tracks the set of pages actively referenced by a process in a recent time window $\Delta$. The sum of working set sizes of all active processes must be less than the total physical memory: $\sum W_i \le \text{Total Frames}$. If this condition is violated, the OS suspends/swaps out a process completely to free up frames for others.
    *   **Page Fault Frequency (PFF)**: Establish upper and lower bounds for page fault rates. If a process exceeds the upper bound, allocate it more frames. If it drops below the lower bound, reclaim some of its frames.

### Q3. Why is an RTOS (Real-Time Operating System) critical for IoT devices (relevant to STPI IoT OpenLab) compared to a General-Purpose OS (GPOS)?
*   **Determinism vs. Fairness**:
    *   A **GPOS** (like Linux, Windows) is designed for high throughput and fairness. Its scheduler tries to give every process a fair share of CPU, meaning task execution latency is non-deterministic (cannot guarantee exact execution times).
    *   An **RTOS** (like FreeRTOS, VxWorks) is designed for **determinism and predictability**. It guarantees that critical tasks (e.g., reading a sensor, controlling an actuator) will execute within strict, hard real-time deadlines.
*   **Interrupt Latency**: RTOS has extremely low and bounded interrupt latency.
*   **Preemption**: RTOS supports strict priority-based preemptive scheduling, where a high-priority task will immediately preempt any running low-priority task without waiting for a time slice to expire.

---

## 🔌 4. Computer Networks (CN) Deep-Dive

### Q1. Differentiate between Flow Control and Congestion Control in TCP.
*   **Flow Control**: A **point-to-point** mechanism that prevents a fast sender from overwhelming a slow receiver.
    *   *Mechanism*: Uses the **Sliding Window** protocol. The receiver advertises its available buffer space in the `Receiver Window (rwnd)` field of the TCP header. The sender must never send more data than `rwnd`.
*   **Congestion Control**: A **network-wide** mechanism that prevents senders from overwhelming the intermediate routers and links.
    *   *Mechanism*: Uses the **Congestion Window (cwnd)**. The sender dynamically adjusts `cwnd` using four phases:
        1.  **Slow Start**: Double `cwnd` every RTT (exponential growth) until it hits the Slow Start Threshold (`ssthresh`).
        2.  **Congestion Avoidance**: Increase `cwnd` by 1 MSS per RTT (linear growth) to probe for bandwidth.
        3.  **Fast Retransmit**: If 3 duplicate ACKs are received, assume a packet is lost and retransmit immediately without waiting for a timeout.
        4.  **Fast Recovery**: Set `ssthresh = cwnd / 2`, set `cwnd = ssthresh + 3`, and enter Congestion Avoidance directly (skipping Slow Start).

### Q2. Describe the step-by-step SSL/TLS 1.3 Handshake. How does it improve on TLS 1.2?
*   **TLS 1.3 Handshake (1-RTT)**:
    1.  **Client Hello**: Client sends supported cryptographic suites and a **key share** (pre-computing Diffie-Hellman public keys) in the very first message.
    2.  **Server Hello**: Server selects the cryptographic suite, sends its certificate, its own **key share**, and a finished message.
    3.  **Key Derivation**: Both parties derive the symmetric session keys using the exchanged key shares.
    4.  **Encrypted Data**: Subsequent communication is fully encrypted.
*   **Improvement over TLS 1.2**:
    *   *Latency*: TLS 1.2 required **2-RTT** (two round-trip times) to establish a secure connection. TLS 1.3 does it in **1-RTT** by combining key exchange with the initial hello.
    *   *Security*: Removed insecure, legacy cryptographic algorithms (like MD5, SHA-1, RC4, DES) and mandated **Perfect Forward Secrecy (PFS)** via Diffie-Hellman.

---

## 🌳 5. Data Structures & Algorithms (DSA) Deep-Dive

### Q1. Why does Dijkstra's algorithm fail on negative edge weights? How does Bellman-Ford resolve this?
*   **Dijkstra's Failure**: Dijkstra is a **Greedy** algorithm. It assumes that once a vertex is added to the "visited/closed" set, its shortest path from the source is finalized and will never decrease (since adding positive weights can only increase path lengths).
    *   If negative edges exist, a path through a negative edge could later yield a shorter distance to an already-visited node, but Dijkstra will never re-evaluate that node.
*   **Bellman-Ford Resolution**: Uses **Dynamic Programming**. It relaxes all $|V| - 1$ edges systematically $|V| - 1$ times.
    *   Since the shortest path in a graph with $|V|$ vertices can have at most $|V| - 1$ edges, $|V| - 1$ iterations are guaranteed to find the absolute shortest path even with negative edges.
    *   *Negative Cycle Detection*: On the $|V|$-th iteration, if any distance can still be relaxed, it proves the existence of a negative weight cycle (where path length can infinitely decrease).

### Q2. Compare AVL Trees and Red-Black Trees. When is each preferred?
*   **AVL Tree**: Strictly balanced. The height difference (balance factor) between left and right subtrees of any node is at most **1**.
    *   *Height*: $\approx 1.44 \log_2 N$ (shorter, tighter tree).
*   **Red-Black Tree**: Weakly balanced. No path from root to leaf is more than twice as long as any other path.
    *   *Height*: $\approx 2 \log_2 N$ (taller tree).
*   **Selection Rule**:
    *   **Use AVL Trees** when your workload is **Read-Heavy** (e.g., dictionary lookups, database indices). Because the tree is tightly balanced, lookup times ($O(\log N)$) are faster.
    *   **Use Red-Black Trees** when your workload is **Write-Heavy / Dynamic** (e.g., Java's `TreeMap`, C++'s `std::map`). Because it is weakly balanced, insertions and deletions require far fewer rotations to rebalance, making writes significantly faster.
