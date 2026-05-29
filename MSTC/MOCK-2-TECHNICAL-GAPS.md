# MOCK 2 Technical Gaps - Emergency Fix Sheet

> ⏰ **Timeline**: Fix in 2 hours (1-3 PM today)
> 🎯 **Target**: Zero gaps in tomorrow's interview

---

## ❌ GAP 1: 2PL (Two-Phase Locking Protocol)

**What is 2PL:**
Two-Phase Locking is a concurrency control protocol in DBMS to ensure serializability.

**Two Phases:**
1. **Growing Phase**: Transaction can acquire locks but cannot release any locks
2. **Shrinking Phase**: Transaction can release locks but cannot acquire new locks

**Types:**
- **Basic 2PL**: May cause deadlocks
- **Strict 2PL**: Hold all locks until transaction commits/aborts
- **Rigorous 2PL**: Hold all locks until transaction ends

**40s Script:**
*"Two-Phase Locking is a database concurrency control protocol with two phases. In the growing phase, transactions can only acquire locks, not release them. In the shrinking phase, they can only release locks, not acquire new ones. This ensures serializability by preventing conflicts between concurrent transactions. Strict 2PL holds all locks until commit to prevent cascading rollbacks."*

---

## ❌ GAP 2: Minimum Number of Swaps in Sorting

**CORRECT ANSWER: Selection Sort**

**Why Selection Sort:**
- Selection sort minimizes the number of swaps
- It makes at most **n-1 swaps** (one swap per position)
- Each swap places an element in its final correct position

**Comparison:**
| Algorithm | Swaps |
|-----------|-------|
| **Selection Sort** | **O(n) - MINIMUM** |
| Bubble Sort | O(n²) |
| Insertion Sort | O(n²) |
| Merge Sort | No swaps (uses temporary array) |

**Why your answer (Merge Sort) was wrong:**
Merge sort doesn't use swaps - it creates new arrays during merging.

**40s Script:**
*"Selection sort requires the minimum number of swaps among comparison-based sorting algorithms. It performs at most n-1 swaps because in each iteration, it finds the minimum element and swaps it to its correct position. Other algorithms like bubble sort and insertion sort can perform O(n²) swaps in worst case."*

---

## ❌ GAP 3: Tree Traversal Techniques

**3 Standard Traversals:**

### 1. **Inorder Traversal** (Left → Root → Right)
- **For BST**: Gives elements in **sorted order**
- **Code pattern**: `inorder(left) → visit(root) → inorder(right)`

### 2. **Preorder Traversal** (Root → Left → Right)
- **Use**: Tree copying, expression tree evaluation
- **Code pattern**: `visit(root) → preorder(left) → preorder(right)`

### 3. **Postorder Traversal** (Left → Right → Root)
- **Use**: Tree deletion, calculating directory sizes
- **Code pattern**: `postorder(left) → postorder(right) → visit(root)`

**Mnemonic**: "**I**n **P**re **P**ost" → "**I**nside **P**rint **P**arent" 
- **In**order: print inside (between children)
- **Pre**order: print before children  
- **Post**order: print after children

**Example Tree:**
```
    A
   / \
  B   C
 / \
D   E
```

- **Inorder**: D, B, E, A, C
- **Preorder**: A, B, D, E, C  
- **Postorder**: D, E, B, C, A

**40s Script:**
*"There are three tree traversal techniques. Inorder visits left subtree, then root, then right subtree - for BST this gives sorted order. Preorder visits root first, then left and right subtrees - used for tree copying. Postorder visits left and right subtrees first, then root - used for tree deletion and calculating sizes."*

---

## ❌ GAP 4: Node.js Advanced Topics

### **Child Process: fork() vs spawn()**

**fork():**
- Creates a new V8 instance (separate memory)
- Can communicate via IPC (Inter-Process Communication)
- **Use**: CPU-intensive tasks

**spawn():**
- Launches a command in a new process
- Streams data (stdout/stderr)
- **Use**: Running system commands

**40s Script:**
*"Fork creates a new Node.js process with separate V8 engine, useful for CPU-intensive tasks with IPC communication. Spawn launches any system command in a new process with streaming I/O, useful for running shell commands or other executables."*

### **Callback Hell Solution:**
**Answer: Promises, Async/Await, Promise.all**

You mentioned `Promise.all` correctly, but complete answer:
1. **Promises**: Chain with `.then()`
2. **Async/Await**: Write synchronous-looking code
3. **Promise.all**: Wait for multiple promises concurrently

---

## 🎯 2-HOUR DRILL PLAN (1:00-3:00 PM)

### **1:00-1:30 PM: Database Concepts**
- Read about 2PL protocol
- Practice explaining ACID with examples
- Review transaction isolation levels

### **1:30-2:00 PM: Algorithms & Data Structures** 
- **Selection sort**: Why it minimizes swaps
- **Tree traversals**: Practice with examples
- **Sorting comparison**: Time complexity table

### **2:00-2:30 PM: Node.js Deep Dive**
- Fork vs Spawn with examples
- Async patterns: Promises, Async/Await
- Event loop and callback queue

### **2:30-3:00 PM: Integration Practice**
- Practice all gap topics in 40s scripts
- Random question simulation
- Confidence building exercises

---

## 💪 CONFIDENCE BOOSTERS

**What Went RIGHT in Mock 2:**
1. ✅ Introduction was professional and clear
2. ✅ DBMS basics (CREATE, FK, ACID) - solid understanding
3. ✅ Node.js core concepts (promises, async/sync) - good explanations  
4. ✅ Networking (IPv4/IPv6, TCP/UDP) - accurate answers
5. ✅ HR responses - much more structured and confident
6. ✅ Overall communication - clear and systematic

**Interviewer Feedback:**
- "Very good" multiple times on database answers
- Recognized your Node.js experience as a strength
- HR feedback was positive
- Only suggestion: brush up on basic CS concepts (which we're doing now!)

---

## 🎯 TOMORROW'S STRATEGY

### **Technical Approach:**
1. **Start with strengths**: DBMS, Node.js experience
2. **Quick recovery**: If you blank, say "Let me think for a moment" and reason through
3. **Admit and pivot**: "I don't recall the exact term, but the concept involves..."
4. **Stay confident**: One gap doesn't define the entire interview

### **Key Message for Tomorrow:**
*"You have 2 years of real software development experience + strong fundamentals. You belong in that room. Trust your preparation and experience."*