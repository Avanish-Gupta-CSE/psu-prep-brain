# MSTC Technical Gaps — Emergency Repair Sheet

> 🚨 **URGENT**: Fix these 8 gaps before today's 8:30 AM mock
> ⏱️ Study time: 45 minutes MAX (5-6 minutes per gap)

---

## ❌ GAP 1: PRIMARY KEY vs UNIQUE KEY ⚠️ **BASIC ERROR**

### PRIMARY KEY
- **Definition**: Column(s) that uniquely identifies each row in a table
- **Properties**: UNIQUE + NOT NULL
- **Limit**: Only **ONE** Primary Key per table
- **Purpose**: Main identifier for table, used for relationships

### UNIQUE KEY  
- **Definition**: Column(s) that ensures uniqueness but can have NULL values
- **Properties**: UNIQUE but allows **ONE NULL** value
- **Limit**: **Multiple** Unique Keys allowed per table
- **Purpose**: Additional uniqueness constraints

**40s Script:**
"Primary Key uniquely identifies each row and cannot be NULL - only one per table. Unique Key also ensures uniqueness but allows one NULL value - multiple unique keys allowed per table. PK is the main identifier used for foreign key relationships, UK provides additional uniqueness constraints."

**Example:**
```sql
-- Employee table can have:
emp_id INT PRIMARY KEY        -- Only one PK
email VARCHAR(50) UNIQUE      -- UK 1: allows one NULL
phone VARCHAR(15) UNIQUE      -- UK 2: allows one NULL
```

---

## ❌ GAP 2: OPERATING SYSTEM DEFINITION ⚠️ **INTERVIEW KILLER**

**Technical Definition:**
"An Operating System is system software that acts as an interface between users and computer hardware. It manages and controls CPU, memory, files, I/O devices, and provides services through system calls."

**40s Script:**
"Operating System is system software that manages computer hardware and provides interface for users and applications. Key functions include process management, memory management, file system, and I/O control. It acts as a resource manager, allocating CPU time, memory space, and handling device drivers. Examples are Windows, Linux, macOS."

**Key Functions (remember 5):**
1. **Process Management** → scheduling, creation, termination
2. **Memory Management** → allocation, virtual memory
3. **File Management** → create, delete, organize files  
4. **I/O Management** → device drivers, interrupts
5. **Security & Protection** → user authentication, access control

---

## ❌ GAP 3: HAVING CLAUSE in SQL

**Definition**: Used with GROUP BY to filter grouped records (like WHERE for groups)

**Key Rule**: 
- **WHERE** → filters rows BEFORE grouping
- **HAVING** → filters groups AFTER grouping and aggregation

**40s Script:**
"HAVING clause filters grouped records after aggregation, unlike WHERE which filters individual rows before grouping. Use HAVING with aggregate functions like COUNT, SUM, AVG. It's applied after GROUP BY processing."

**Example:**
```sql
-- Find departments with more than 5 employees
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department 
HAVING COUNT(*) > 5;

-- WHERE would fail here because COUNT(*) doesn't exist yet
```

---

## ❌ GAP 4: IPv4 vs IPv6

### IPv4
- **Address Length**: 32 bits (4 bytes)
- **Format**: Dotted decimal (192.168.1.1)
- **Address Space**: ~4.3 billion addresses
- **Header Size**: 20-60 bytes (variable)
- **Security**: IPSec optional

### IPv6  
- **Address Length**: 128 bits (16 bytes)
- **Format**: Hexadecimal with colons (2001:db8::1)
- **Address Space**: 3.4 × 10³⁸ addresses
- **Header Size**: 40 bytes (fixed)
- **Security**: IPSec mandatory

**40s Script:**
"IPv4 uses 32-bit addresses in dotted decimal format with ~4.3 billion possible addresses. IPv6 uses 128-bit addresses in hexadecimal format with vastly more address space. IPv6 has fixed 40-byte headers vs IPv4's variable 20-60 bytes, and includes mandatory security features."

---

## ❌ GAP 5: DIJKSTRA ALGORITHM ⚠️ **YOU GOT THIS WRONG**

**CORRECT FACTS:**
- ✅ **Works on BOTH directed AND undirected graphs**
- ✅ **Single-source shortest path** algorithm
- ❌ **Does NOT work with negative weights**
- ✅ **Greedy algorithm** using priority queue
- ✅ **Time Complexity**: O((V+E) log V)

**40s Script:**
"Dijkstra's algorithm finds shortest paths from a single source to all vertices in weighted graphs. It works on both directed and undirected graphs but requires non-negative weights. Uses greedy approach with min-priority queue, repeatedly selecting vertex with minimum distance and relaxing its neighbors. Time complexity is O((V+E) log V) with heap."

**Why No Negative Weights:**
Greedy choice assumes once a vertex is processed, its shortest distance is final. Negative weights could create shorter paths later.

---

## ❌ GAP 6: MULTIPLEXER (Digital Logic)

**Definition**: Combinational circuit that selects one of many input signals and forwards it to single output line.

**Properties:**
- **n select lines** can choose from **2ⁿ input lines**
- **1 output line**
- **Data selector** or **MUX**

**40s Script:**
"Multiplexer is a digital circuit that selects one input from multiple inputs using select lines and forwards it to output. With n select lines, we can choose from 2ⁿ inputs. It's like a digital switch - select lines act as control to choose which input reaches output."

**Example**: 4:1 MUX has 4 inputs, 2 select lines, 1 output.

---

## ❌ GAP 7: IS CLAUSE in DBMS (Context Needed)

**Most Likely Meant**: **EXISTS** clause or **IN** clause

### EXISTS Clause
```sql
-- Check if subquery returns any rows
SELECT * FROM employees e 
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.dept_id = e.dept_id);
```

### IN Clause  
```sql
-- Check if value exists in a list/subquery
SELECT * FROM employees 
WHERE dept_id IN (1, 2, 3);
```

**40s Script:**
"EXISTS checks if a subquery returns any rows - returns TRUE/FALSE. IN checks if a value matches any value in a list or subquery result. EXISTS is generally more efficient for large subqueries because it stops at first match."

---

## ❌ GAP 8: EIGENVALUES (Low Priority for Systems)

**Definition**: Special scalars associated with linear transformations represented by matrices.

**Formula**: Av = λv (where λ is eigenvalue, v is eigenvector)

**40s Script:**
"Eigenvalue is a scalar λ such that when matrix A multiplies eigenvector v, the result is λv - the vector is only scaled, not rotated. Used in machine learning for dimensionality reduction (PCA), stability analysis in systems, and Google's PageRank algorithm."

---

## 🎯 EMERGENCY DRILL PLAN (Next 30 Minutes)

**Sequence (6 minutes each):**
1. **Primary vs Unique Key** → Write 3 examples, practice 40s script
2. **Operating System Definition** → Memorize technical definition + 5 functions
3. **HAVING clause** → Write 2 SQL examples with GROUP BY
4. **Dijkstra Algorithm** → Correct the wrong facts, practice explanation
5. **IPv4 vs IPv6** → Make comparison table, memorize address formats

**Before 8:30 AM Mock:**
- Practice each 40s script aloud 2 times
- Write key points on paper without looking
- Test yourself: "What's the difference between PK and UK?" → immediate answer

---

## 📝 CONFIDENCE RECOVERY STRATEGY

**When You Don't Know Something:**
1. **Admit quickly**: "I don't recall the exact details of [topic]"
2. **Show reasoning**: "But based on the principle of [related concept]..."
3. **Stay confident**: Don't let one gap affect other answers
4. **Move forward**: "Could you clarify what specific aspect you'd like me to explain?"

**Remember**: 
- One wrong answer ≠ interview failure
- Systems role focuses on practical knowledge
- Your Berkadia experience is a strength
- Stay calm and systematic