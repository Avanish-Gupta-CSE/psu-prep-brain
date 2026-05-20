# DSA — Advanced Algorithms (Graph + DP + Greedy)

> 🎯 Target: Master interview-ready explanations for advanced algorithms
> ⏱️ Read time: 25 minutes

---

## ★ HIGH PRIORITY TOPICS ★

### 1. DYNAMIC PROGRAMMING

**Definition:**
- Optimization technique that breaks complex problems into simpler sub-problems
- Stores results of sub-problems to avoid redundant calculations (memoization)
- **Bottom-up approach**: solve smaller problems first, build to larger ones

**Key Properties:**
1. **Overlapping sub-problems**: same sub-problems solved multiple times
2. **Optimal substructure**: optimal solution contains optimal solutions to sub-problems

**Types:**
- **Multistage Graph**: weighted directed graph with stages, minimum cost path
- **Floyd-Warshall**: all-pairs shortest path algorithm
- **0/1 Knapsack**: include/exclude items to maximize value within weight constraint
- **Optimal Binary Tree**: minimize search cost for frequency-based searches

**Time Complexity**: Generally O(n²) to O(n³)

---

### 2. HUFFMAN CODING

**Definition:**
- Lossless data compression algorithm using variable-length encoding
- Assigns shorter codes to frequent characters, longer codes to rare characters

**Algorithm Steps:**
1. Build frequency table for all characters
2. Create leaf nodes, arrange in ascending order of frequency
3. Make new internal node with two lowest frequency nodes as children
4. Repeat until single tree formed

**Properties:**
- **Prefix property**: no code is prefix of another code
- **Optimal**: guarantees minimum average code length
- **Time Complexity**: O(n log n) using min-heap

**40s Script:**
"Huffman coding is a greedy algorithm for lossless compression. It assigns variable-length codes based on character frequency - frequent characters get shorter codes. We build a binary tree bottom-up by repeatedly combining the two nodes with lowest frequencies. The path from root to leaf gives each character's code. This ensures no code is a prefix of another, making it uniquely decodable."

---

### 3. KNAPSACK PROBLEM

**Types:**
1. **Fractional Knapsack**: can take fractions of items (greedy works)
2. **0/1 Knapsack**: can only take whole items (DP required)

**0/1 Knapsack Solution:**
```
If items are already arranged by value/weight ratio:
V[i,w] = max{V[i-1,w], V[i-1,w-wi] + vi}

Where: V[i,w] = maximum value with first i items and weight limit w
```

**Formula:**
- **Constraint**: Σ wi ≤ W (total weight ≤ capacity)
- **Objective**: max Σ vi (maximize total value)

**Time Complexity**: O(nW) where n = items, W = capacity

---

### 4. SHORTEST PATH ALGORITHMS

#### A. DIJKSTRA'S ALGORITHM ⚠️ **INTERVIEW CRITICAL**

**Definition:**
- **Single-source shortest path** for **non-negative weighted graphs**
- Uses greedy approach with priority queue (min-heap)

**Key Properties:**
- ✅ Works on **directed AND undirected** graphs
- ❌ Does **NOT work with negative weights**
- **Time Complexity**: O((V+E) log V) with heap

**Algorithm Steps:**
1. Initialize distance array: d[source] = 0, others = ∞
2. Add all vertices to min-priority queue
3. Extract vertex u with minimum distance
4. For each neighbor v of u: if d[u] + weight(u,v) < d[v], update d[v]
5. Repeat until queue empty

**40s Script:**
"Dijkstra finds shortest paths from a source to all vertices in weighted graphs with non-negative edges. It's a greedy algorithm using a priority queue. We start with source distance 0, others infinity. Repeatedly extract the minimum distance vertex and relax its neighbors. Works on both directed and undirected graphs but fails with negative weights."

#### B. BELLMAN-FORD ALGORITHM

**Key Difference from Dijkstra:**
- ✅ Handles **negative weights**
- ✅ Detects **negative cycles**
- ❌ Slower: **O(VE)** time complexity

**Algorithm:**
- Relax all edges (V-1) times
- Check for negative cycles in Vth iteration

#### C. FLOYD-WARSHALL ALGORITHM

**Purpose**: **All-pairs shortest path**
**Time Complexity**: O(V³)
**Formula**: `A^k[i,j] = min{A^(k-1)[i,j], A^(k-1)[i,k] + A^(k-1)[k,j]}`

---

### 5. GREEDY ALGORITHMS

**Definition:**
- Makes locally optimal choice at each step
- Does **not** guarantee global optimum for all problems
- Works for problems with **greedy choice property**

**Classic Examples:**
1. **Minimum Spanning Tree**: Kruskal's, Prim's
2. **Single Source Shortest Path**: Dijkstra's  
3. **Huffman Coding**
4. **Fractional Knapsack**
5. **Optimal Merge Pattern**

#### KRUSKAL'S ALGORITHM (MST)
**Steps:**
1. Sort all edges by weight (ascending)
2. Add edges one by one if they don't create cycle
3. Use Union-Find to detect cycles

**Time Complexity**: O(E log E)

---

### 6. COMPLEXITY CLASSES

#### NP-HARD and NP-COMPLETE

**P**: Problems solvable in polynomial time
**NP**: Non-deterministic polynomial time (can verify solution in polynomial time)

**NP-Hard**: At least as hard as any problem in NP
**NP-Complete**: Both NP and NP-Hard

**Examples:**
- **NP-Complete**: Traveling Salesman, Hamiltonian Cycle, Graph Coloring
- **NP-Hard**: Halting Problem

**40s Script:**
"P problems can be solved in polynomial time. NP problems can have their solutions verified in polynomial time. NP-Complete problems are both in NP and as hard as any NP problem - if we solve one in polynomial time, we solve all. NP-Hard problems are at least as difficult as NP-Complete but might not be in NP themselves."

---

### 7. BACKTRACKING

**Definition:**
- Brute force approach that systematically explores solution space
- Abandons partial solutions that cannot lead to complete solution

**Examples:**
- **N-Queens Problem**: Place N queens on NxN chessboard so none attack
- **Graph Coloring**: Color graph vertices so no adjacent vertices same color
- **Hamiltonian Cycle**: Visit each vertex exactly once and return to start

**Template:**
```
if (solution found):
    return solution
if (no valid extension):
    return failure
for each extension:
    try extension
    if (backtrack succeeds):
        return solution
    undo extension
```

---

## Quick Cheat Sheet

```
Dynamic Programming:
  0/1 Knapsack    → V[i,w] = max{V[i-1,w], V[i-1,w-wi] + vi}
  Floyd-Warshall  → A^k[i,j] = min{A^(k-1)[i,j], A^(k-1)[i,k] + A^(k-1)[k,j]}

Shortest Path:
  Dijkstra        → Non-negative weights, O((V+E) log V), works on directed/undirected
  Bellman-Ford    → Negative weights OK, O(VE), detects negative cycles
  Floyd-Warshall  → All pairs, O(V³)

Greedy Works For:
  MST (Kruskal, Prim) → Always optimal
  Huffman Coding      → Always optimal  
  Fractional Knapsack → Always optimal
  Dijkstra           → Always optimal (non-negative weights)

NP Complexity:
  P        → Polynomial solvable
  NP       → Polynomial verifiable  
  NP-Hard  → As hard as any NP problem
  NP-Complete → NP + NP-Hard
```

---

## Follow-up Questions

**Q: Why doesn't Dijkstra work with negative weights?**
A: Because the greedy choice (always picking minimum distance vertex) fails. Once a vertex is processed, we assume its shortest path is found. With negative weights, a later path might give a shorter route through an already-processed vertex.

**Q: Difference between Kruskal's and Prim's?**
A: Both find MST. Kruskal sorts all edges globally and adds safe edges (edge-based). Prim grows tree from a starting vertex by adding minimum weight edge connected to current tree (vertex-based).

**Q: When to use DP vs Greedy?**
A: Use DP when problem has overlapping sub-problems and optimal substructure, but greedy choice doesn't work globally. Use Greedy when local optimal choices lead to global optimum.