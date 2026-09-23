# KnowledgeGate — COMPLETE Granular Video Index

> **Auto-generated** by `tools/kg_video_index.py` (API: `api.knowledgegate.ai/api/v1/course-content/public`).
> **Purpose:** when a question can't be solved, look up the exact topic → subtopic → video below.
> Companion: `tools/kg-index.json` (machine-readable, for precise lookups).
> See also: `IOCL/KG-COURSE-INVENTORY-19SEPT.md` (course-level stats) · `IOCL/SYLLABUS.md` (official pattern).

**How to read a row:** `SUBTOPIC — video (dur) [PQ n] · video (dur) [PYQ n]`
Where `[PQ]` = practice questions in that lesson, `[PYQ]` = previous-year questions.
**Coverage:** 5075 concept videos · 693h · 5145 PYQs · 8475 practice questions across 5 owned courses.

---

## 🎯 GAP-FILL PROTOCOL — how to use this file (question-first mode)

**The rule:** *never watch a lecture to "cover a subject."* Watch a lecture **only** because a specific question beat you.

### The loop (repeat all day)
1. **ATTEMPT** — take a mock / PYQ set / PQ set. Work it properly.
2. **MARK** — after each question, tag it: ✅ sure · 🟡 guessed · ❌ blanked / no clue.
3. **HARVEST** — collect every 🟡 and ❌. These are your *only* valid study targets; ✅ questions need nothing.
4. **ASK** — send me the question (paste it or name the topic). Best format:
   > `Q: <text or screenshot>` · `Subject: CN` · `Stuck on: <what confused you>`
5. **I RETURN** (from this index):
   - the exact **subtopic** it belongs to,
   - the **specific videos + durations** (so you know if it's a 5-min or 40-min fix),
   - the **PYQ / PQ count** for that subtopic (how hot it is),
   - and the **drill** — which questions to re-attempt right after.
6. **FIX** — watch only those videos at **2x**, then immediately re-attempt the question.
7. **LOG** — one line on your one-pager: rule + trap. Move on.

### How I find the video for your question
I search this file and `tools/kg-index.json` by keyword. Worked examples:
- **"subnetting"** → `CN → IP Addressing > Subnetting & FLSM Design` → Basics of SubNetting (11m) · SubNetting Example (5m) · Variable Length SubNetting (6m) · SubNetting In CIDR (4m)
- **"banker"** → `OS → Deadlock > Avoidance & Banker's Algo` → Understanding Bankers Algorithm (11m)

### What to give me (so the answer is fast and exact)
| Give me | Why |
| :--- | :--- |
| The **question text** or a screenshot | pins the exact sub-concept, not the whole subject |
| **Which option you picked** and why | separates "no knowledge" from "misread" from "trap" |
| **Subject name** (if obvious) | speeds up lookup |
| Whether you **had no idea** vs **knew it but couldn't finish** | "no idea" → concept videos · "couldn't finish" → practice + speed drills |

### Two different fixes — don't confuse them
| Symptom | Fix | Where |
| :--- | :--- | :--- |
| **"I've never seen this"** | Concept videos for that subtopic (2x), then its PYQs | this index |
| **"I know it but keep getting it wrong"** | Skip videos. Do the **PQ set** for that subtopic, then the **PYQ set** | same subtopic row |

### Guardrails
- **Max 2 videos per gap.** If 2 videos don't fix it, it is out of scope for a 1-day sprint — mark it and move on.
- **Never exceed 25 min of video per gap.** Video is your most expensive resource (693h available, almost no clock left).
- **Always re-attempt immediately.** A video without an immediate re-attempt is entertainment, not study.
- **When gaps compete, priority order:** OS > DBMS > CN > DS > COA > DL > Eng Maths > Algo > TOC > Compiler.

### Timeline compression (if only hours remain)
| Time left | Mode |
| :--- | :--- |
| 1 day | Full mock → gap-fill top 6 gaps → one-pagers |
| 4 hours | PYQ sets only → gap-fill top 3 gaps |
| 90 min | Two 20Q speed sets → fix only what repeats |
| 30 min | One-pagers + formula card (zero video) |

---

---

## IOCL Paper-2 (CS/IT)

`IOCL-ENGINEERS-OFFICERS-GRADE-A-PAPER-2` · **1811 videos / 197.1h** · 3201 PYQs · 2416 PQs · 458 subtopics · 23 tests · 558 notes

### 0. About Course — 1 vids · 7m · 0 PYQs · 0 PQs

- **About the Course**
  - *Exam Syllabus*
  - *Study Plan & Test Schedule*
  - *Course Overview*
      · Course Overview (7m)

### 1. Engineering Mathematics — 313 vids · 38.5h · 493 PYQs · 261 PQs

- **Set Theory**
  - *Sets, Representation of Sets and Hierarchy of numbers*
      · What is SET (6m)
      · Representation Of Set (3m)
      · Natural number, Whole number, Integer (3m)
      · Rational Number, Irrational Number, Complex Number (3m)
      · PQ ×2
  - *Finite, Infinite, Countable, and Uncountable Sets*
      · Finite, Infinite, Countable, Uncountable Set (4m)
      · PQ ×3
  - *Null, Universal, Subsets, Proper Subsets*
      · NullEmpty Set and Universal Set (5m)
      · SubSet and Proper SubSet Of a Set (5m)
      · Equality Of a Sets (3m)
      · PQ ×2
  - *Power Set and its Cardinality*
      · Power Set of a Set (4m)
      · Practice Question (5m)
      · 9.2 Practice Question (3m)
      · PYQ ×6
      · PQ ×1
  - *Set Operations – Union, Intersection, Set Difference, Symmetric Difference, and Complement*
      · Complement, Union and Intersection of Sets (5m)
      · Practice Question (5m)
      · Set Difference and Symmetric Difference (3m)
      · Laws of Set Theory (3m)
      · 12.5 Practice Question (3m)
      · 12.6 Practice Question (2m)
      · 12.7 Practice Question (3m)
      · 12.8 Practice Question (3m)
      · 12.24 Practice Question (2m)
      · PYQ ×18
      · PQ ×7
      · PYQ ×24
      · PQ ×15
- **Relations**
  - *Cartesian Product, Relation, Inverse & Complement*
      · Cartesian Product of Sets (4m)
      · What is a Relation (4m)
      · Complement of a Relation (3m)
      · Inverse of a Relation (2m)
      · PYQ ×7
      · PQ ×1
  - *Reflexive Irreflexive Relation – Count, and Properties*
      · Reflexive Relation (7m)
      · Irreflexive Relation (5m)
      · PYQ ×2
      · PQ ×1
  - *Symmetric Anti-Symmetric Asymmetric Relation and Properties*
      · Symmetric Relation (9m)
      · Anti-Symmetric Relation (8m)
      · Asymmetric Relation (7m)
      · PYQ ×3
      · PQ ×3
  - *Transitive Relation – Definition, Count, and Properties*
      · Transitive Relation (7m)
      · Transitive Closure (4m)
      · PYQ ×7
      · PQ ×2
  - *Equivalence Relation, Equivalence Classes, Partitions of a Set*
      · Equivalence Relation (1m)
      · PYQ ×12
      · PQ ×6
  - *Partial Order Relation – Properties, Partially Ordered Set (Poset), and Total Order Relation*
      · Partial Order Relation (1m)
      · PYQ ×3
  - *Hasse Diagram, Greatest Element, Least Element, Upper Bound, Lower Bound*
      · Conversion of POSET to Hasse Diagram (9m)
      · Identify valid Hasse Diagram (7m)
      · Maximal & Minimal Element (6m)
      · Greatest & Least Element (6m)
      · Upper Bound & Lower Bound (7m)
      · Least Upper Bound & Greatest Lower Bound (7m)
      · PYQ ×3
      · PQ ×1
  - *Lattice – Definition, Formation, and Examples of Join and Meet Operations*
      · Lattice Part-1 (8m)
      · Lattce part-2 (6m)
      · PYQ ×3
  - *Bounded, Unbounded, Distributive, Complemented Lattices and Boolean Algebr*
      · Unbounded,Bounded, Complement & Distributed Lattice (5m)
      · Practice Question Part-1 (8m)
      · Practice Question Part-2 (5m)
      · Practice Question (9m)
      · Practice Question (4m)
      · 24.5 Practice Question (2m)
      · 24.6 Practice Question (3m)
      · Gate 1988 (1m)
      · PYQ ×1
      · PQ ×1
  - *Elements in Poset – Greatest Element, Least Element, Upper Bound, and Lower Bound*
      · PYQ ×1
  - *Operations on Relations – Inverse and Complement of a Relation*
      · PYQ ×1
      · PYQ ×43
      · PQ ×15
- **Functions**
  - *Definition of a Function – Domain, Co-domain, Range, and Count of Possible Functions*
      · What is Function (6m)
      · How Many Different Function are Possible (3m)
      · Gate 1998 (2m)
      · PYQ ×8
      · PQ ×4
  - *Composition of Functions – Definition, Properties, and Examples*
      · Compostion of Functions (5m)
      · PYQ ×1
      · PQ ×3
  - *One-to-One (Injective) Function – Definition, Count, and Properties*
      · One-To-One (Injective Function) (3m)
      · Number of Injective Functions are Possible (4m)
      · PYQ ×2
      · PQ ×1
  - *Onto (Surjective) Function – Definition, Count, and Properties*
      · Onto (Surjective Function) (3m)
      · Number of Onto (Surjective are Possible) (5m)
      · PYQ ×5
  - *Bijective Function – Definition, Count, and Properties*
      · Bijective Function (3m)
      · Onto (Surjective Function) (3m)
      · Number of Onto (Surjective are Possible) (5m)
      · PYQ ×3
      · PQ ×3
  - *Inverse of a Function – Definition, Existence Conditions, and Examples*
      · Inverse of a Function (5m)
      · PYQ ×2
      · PYQ ×21
      · PQ ×11
- **Graph Theory**
  - *Introduction to Graphs – Definitions, Terminology (Loops, Parallel Edges, Adjacent Vertices)*
      · Basic Terminology of Graph (6m)
      · PQ ×2
  - *Types of Graphs – Finite, Infinite, Null, Trivial, Complete*
      · Finite Graph (3m)
      · Null Graph Vs Trivial Graph (3m)
      · Complete Graph (5m)
      · PYQ ×3
      · PQ ×3
  - *Bipartite, Cycle, Regular, and Complement of a Graph*
      · Cycle, Wheel & Regular Graph (3m)
      · Complement Of a Graph (4m)
      · Bi-Partie Graph (4m)
      · PYQ ×3
      · PQ ×3
  - *Number of Graphs – Counting of Simple, Undirected, Unlabeled*
      · Number Of Simple Graph With n Vertices (5m)
      · Number Of Simple Graph  With n Vertices e Edges (3m)
      · Gate 1994 (2m)
      · Cycle, Wheel & Regular Graph (3m)
      · Complement Of a Graph (4m)
      · Bi-Partie Graph (4m)
      · PYQ ×7
      · PQ ×2
  - *Degree of Vertex – Isolated and Pendant Vertices, Handshaking Lemma, and Degree Sequence*
      · Degree of Vertex, Isolated & Pendant Vertex (4m)
      · Hand-Shaking Theorem Part-1 (5m)
      · 8.3 Practice Question (3m)
      · 8.4 Practice Question (1m)
      · 8.5 Practice Question (2m)
      · 8.7 Practice Question (2m)
      · PYQ ×7
      · PQ ×3
  - *Minimum and Maximum Degree – Relationships, Degree Constraints, and Havel-Hakimi Theorem*
      · Max, Min Degree (4m)
      · Degree Sequence Problem (8m)
      · 9.2 Practice Question (2m)
      · 13.1 Practice Question (2m)
      · PYQ ×3
      · PQ ×1
  - *Graph Traversal – Walk, Path, Trail, Circuit, and Connected Graphs*
      · Walk , Trail & Path (21m)
      · Connected Graph (6m)
      · Practice Question (5m)
      · PYQ ×7
      · PQ ×3
  - *Euler and Hamiltonian Graphs – Definitions, Conditions, and Examples*
      · Euler Graph (6m)
      · Hamiltonian Graph (4m)
      · PYQ ×4
      · PQ ×4
  - *Planar Graphs – Kuratowski’s Theorems, Homorphism and examples*
      · Planner Graph (7m)
      · PYQ ×4
      · PQ ×1
  - *Euler Formula – Planar Graph Formula, Applications, and Derived Relations*
      · Euler Formula (4m)
      · Euler Formula and its Version (4m)
      · PYQ ×6
      · PQ ×1
  - *Graph Coloring – Vertex Coloring, Edge Coloring, Chromatic Number, and Coloring Theorems*
      · Graph Coloring (6m)
      · Practice Question (6m)
      · Important Conclusion of Graph Coloring (3m)
      · PYQ ×9
      · PQ ×2
  - *Trees – Definitions, Properties, Eccentricity, Diameter, Radius, and Center*
      · Tree (6m)
      · Eccentricity of Vertex (5m)
      · PYQ ×5
      · PQ ×3
  - *Spanning Tree and Spanning Forest – Definition, Construction, and Applications*
      · Spanning Tree (6m)
      · Spanning Forest (4m)
      · PYQ ×7
  - *Cut Set and Connectivity – Edge Connectivity, Vertex Connectivity, and Cut Set Concepts*
      · Edges CutSet and Edges Connectivity (7m)
      · Vertex CutSet and Vertex Connectivity (4m)
      · Practice Question (4m)
      · PYQ ×7
  - *Graph Isomorphism – Definition, Detection, and Problem Solving*
      · Isomorphism (4m)
      · Isomorphism ShortCut Trick (3m)
      · Practice Questions (7m)
      · Practice Question (4m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (4m)
      · PYQ ×2
      · PQ ×1
  - *Graph Matching – Maximal, Maximum, Perfect Matching, and Related Concepts*
      · Matching (9m)
      · PYQ ×3
      · PQ ×1
  - *Graph Covering – Line and Vertex Covering, Independent Set, and Minimal/Maximal Variants*
      · Minimum line covering (5m)
      · Maximum independent line set (4m)
      · Minimum vertex covering (3m)
      · Maximumj independent line set (3m)
      · PYQ ×4
      · PQ ×1
      · PYQ ×81
      · PQ ×31
- **Group Theory**
  - *Closure-Algebraic Structure, Associative-SemiGroup,  Identity-Monoid*
      · Basics of Group Theory (4m)
      · Closure Property and Algebraic Structure (5m)
      · Problems on Closure Property and Algebraic Structure (4m)
      · Associative Property and Semi-Groups (5m)
      · Problems on Associative Property and Semi-Groups (4m)
      · Identity Property and Monoid (4m)
      · Problems on Identity Property and Monoid (4m)
      · PYQ ×2
      · PQ ×2
  - *Inverse Property and  Group*
      · Inverse Property and Group (3m)
      · Questions on Inverse Property and Group (5m)
      · Properties of Group (3m)
      · PYQ ×8
      · PQ ×4
  - *Commutative Property and Abelian Groups*
      · Commutative Property and Abelian Group (3m)
      · 11.1 Practice Question (5m)
      · 11.2 Practice Question (2m)
      · 11.3 Practice Question (3m)
      · 11.4 Practice Question (4m)
      · 11.5 Practice Question (4m)
      · 11.6 Practice Question (2m)
      · Practice Question (3m)
      · 11.4 Practice Question (4m)
      · PYQ ×8
      · PQ ×2
  - *Classification of Finite and Infinite Groups*
      · Finite Group Practice Question (4m)
      · Finite Group & Order of group (4m)
      · Addition Modulo & Multiplication (5m)
      · Practice Questions (9m)
      · Practice Questions (5m)
      · 14.5 Practice Question (1m)
      · Practice Question (1m)
      · PYQ ×2
  - *Subgroup Definition, Examples, and Verification Techniques*
      · SubGroup (4m)
      · 15.3 Practice Question (1m)
      · PYQ ×1
      · PQ ×2
  - *Determining the Order of Elements within Groups*
      · Order Of an Element (6m)
      · Practice Questions (5m)
      · Generating Element and Cyclic Group (4m)
      · Lagrange's Theorem (3m)
      · PYQ ×1
      · PQ ×1
      · PYQ ×22
      · PQ ×11
- **Propositional and Predicate Logic**
  - *Introduction to Propositions, Laws of Contradiction and Excluded Middle*
      · History Of Proposition (6m)
      · Definition Of Proposition (5m)
      · Understanding Argument (4m)
      · Law Of Contradiction (2m)
      · Law of Excluded Middle (1m)
      · PQ ×1
  - *Types of Propositions – Atomic and Compound*
      · Compound Proposition (2m)
      · PQ ×1
  - *Logical Operators – Negation, Conjunction, and Disjunction*
      · Conjuction Operation With Question (5m)
      · Disjunction Operation With Questions (3m)
      · PYQ ×5
      · PQ ×1
  - *Implication and Bi-Conditional Operators in Logic*
      · Implication Operation With Properties (7m)
      · Practice Questions (7m)
      · Practice Questions (7m)
      · Biconditional operator (2m)
      · PYQ ×10
      · PQ ×3
  - *Types of Logical Cases – Tautology, Contradiction, Contingency, Satisfiability, and Validity*
      · Type of cases (4m)
      · PYQ ×14
      · PQ ×2
  - *Introduction to First Order Predicate Logic*
      · First order Predicate Logic (8m)
      · PYQ ×2
      · PQ ×1
  - *Quantifiers – Universal and Existential*
      · Quantifiers (2m)
      · More on Quantifiers (6m)
      · Quantifier Negation (4m)
      · Ordering of Quantifiers (9m)
      · Existential Quantifier with Conjunction and Disjunction (5m)
      · Universal Quantifier with Conjunction and Disjunction (3m)
      · PYQ ×29
      · PQ ×3
  - *Wheel Graph Concept and Representation in Logic*
      · PYQ ×5
  - *Practice Problems on Quantifiers and Predicate Logic*
      · Practice Questions (2m)
      · 19.1 Practice Questions (2m)
      · 19.3 Practice Questions (4m)
      · 19.4 Practice Questions (4m)
      · PQ ×1
  - *Functional Completeness*
      · Functionality Complete Set (1m)
  - *Questions and Practice Problems on Propositions*
      · PYQ ×10
      · PQ ×1
  - *Negation of Quantifiers and Rule Applications*
      · Gate 1992 (1m)
      · PYQ ×4
      · PQ ×3
      · PYQ ×79
      · PQ ×17
- **Linear Algebra**
  - *Matrix and Vectors - Definition and Types*
      · Introduction to Matrix & Vectors (12m)
      · Dot Product of Vectors (4m)
      · Types of Matrices (18m)
      · Special Matrices : Orthogonal Matrix (6m)
      · Special Matrices : Idempotent Matrix (5m)
      · Special Matrices : Involutary Matrix (11m)
      · Special Matrices : Nilpotent Matrix (8m)
      · Equality of Matrices (2m)
      · PYQ ×5
      · PQ ×2
  - *Matrix Addition and Multiplication*
      · Matrix Addition & Multiplication (14m)
      · PYQ ×3
  - *Transpose of a Matrix*
      · Transpose of a Matrix (9m)
      · PYQ ×2
      · PQ ×1
  - *Elementary Row and Column Operations*
      · Elementary Row & Column Operations (5m)
      · PYQ ×1
  - *Determinant of a Matrix*
      · Determinant of a Matrix (12m)
      · Finding Determinant of Big Matrices (3m)
      · Properties of Determinants (6m)
      · Co-Factor Matrix (5m)
      · PYQ ×14
      · PQ ×7
  - *Adjoint and Inverse of a Matrix*
      · Adjoint of a Matrix (8m)
      · Properties of Adjoint, Inverse & Determinants (8m)
      · PYQ ×3
      · PQ ×3
  - *Rank of a Matrix*
      · Rank of a Matrix (19m)
      · Finding Rank using Gauss Elimination Method (8m)
      · Properties of Rank (6m)
      · Practice Question on Finding Rank (Q1) (5m)
      · Practice Question on Finding Rank (Q2) (4m)
      · PYQ ×2
      · PQ ×2
  - *System of Linear Equations*
      · System of Linear Equations (7m)
      · Solution Set (3m)
      · Under-determined & Over-determined System (6m)
      · Independence of System of Linear Equations (2m)
      · Consistent System of Equations (10m)
      · Elimination of Variables (Solving System of Linear Equation) (4m)
      · Echelon Form - Gauss Elimination Method (Solving Equations) (9m)
      · Diagonal Matrix- Gauss Elimination Method- Solving Equations (9m)
      · Shortcut Tricks for Solving System of Linear Equation (4m)
      · Cramer's Rule (Solving System of Linear Equation) (4m)
      · Matrix Solution (Solving System of Linear Equation) (4m)
      · Homogeneous System of Linear Equations (12m)
      · PYQ ×15
      · PQ ×3
  - *Trace of a Matrix*
      · Trace of a Matrix (17m)
      · PYQ ×1
      · PQ ×1
  - *Eigen Values and Eigen Vectors*
      · Eigen Values and Eigen Vectors (14m)
      · Properties of Eigen Values and Eigen Vectors (24m)
      · PYQ ×16
      · PQ ×8
  - *Diagonalization*
  - *LU Decomposition*
      · PYQ ×1
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×4
      · PQ ×1
      · PYQ ×67
      · PQ ×30
- **Calculus**
  - *Limits*
      · Introduction to Limits (18m)
      · Important Properties of Limits (6m)
      · Indeterminate Forms (12m)
      · Non-Indeterminate Forms (6m)
      · Solving Limits : Substitution Method (8m)
      · Solving Limits: Tabular & Approximation Method (6m)
      · Solving Limits: Factorization Method (18m)
      · Solving Limits: Expansion Method (14m)
      · Solving Limits: L Hopital's Rule (6m)
      · Questions on L Hopital's Rule (Part 1) (23m)
      · Questions on L Hopital's Rule (Part 2) (11m)
      · Proof of L Hopital's Rule (5m)
      · Some Notable Special Limits (6m)
      · PYQ ×7
      · PQ ×6
  - *Continuity*
      · continuity (7m)
      · Continuity in intervals (5m)
      · Properties of Continuous Functions (1m)
      · Let's Solve Questions on Continuity (12m)
      · Types of Discontinuity (8m)
      · Gate CS 2013 - 1 Mark Question (3m)
      · Gate CS 2015 - Set 2 - 1 Mark Question (5m)
      · Gate CS 2014 - Set 1 - 2 Marks Question (6m)
      · PYQ ×3
      · PQ ×5
  - *Differentiability and Differentiation*
      · Differentiation Rules & Formulas (2m)
      · DIFFERENTIABILITY - Mathematical Definition (6m)
      · Differentiability - Geometric Definition (8m)
      · How to Geometrically identify Non-Differentiability? (5m)
      · GATE CS 2016 - Set 2 - 1 Mark Question (3m)
      · GATE CS 2014 - Set 1 - 2 Marks Question (2m)
      · Rolle’s Theorem (8m)
      · GATE CS 2014 – Set 1 – 1 Mark Question (7m)
      · Lagrange's Mean Value Theorem (6m)
      · Applications of Mean Value Theorem (8m)
      · Cauchy’s Extended Mean Value Theorem (6m)
      · PYQ ×9
      · PQ ×5
  - *Maxima and Minima*
      · Stationary Point & Critical Point (7m)
      · Maxima & Minima (13m)
      · Monotonic Functions (4m)
      · How to Mathematically find Maxima & Minima? (7m)
      · Finding Maxima & Minima (Practice Questions Set 1) (10m)
      · Finding Maxima & Minima (Practice Questions Set 2) (7m)
      · Finding Maxima & Minima (Practice Questions Set 3) (6m)
      · Finding Maxima & Minima (Practice Questions Set 4) (4m)
      · Finding Maxima & Minima (Practice Questions Set 5) (5m)
      · Finding Maxima & Minima (Practice Questions Set 6) (10m)
      · PYQ ×6
      · PQ ×4
  - *Integration*
      · Integration & Indefinite Integrals (6m)
      · Definite Integrals (10m)
      · Properties of Definite Integrals (10m)
      · All Formulas of Integration (1m)
      · Solving Integration: Substitution Method (16m)
      · Solving Integration: Partial Fractions Method (14m)
      · Complications in Partial Fractions Method (11m)
      · Solving Integration: Integration by Parts Method (10m)
      · GATE Question on Integration by Parts Method (7m)
      · GATE CS 2000 Question (7m)
      · GATE CS 2009 Question (4m)
      · GATE CS 2011 – 2 Marks Question (11m)
      · GATE CS 2014 – Set 3 Question (8m)
      · PYQ ×14
      · PQ ×7
  - *Multiple Topics*
      · PYQ ×4
      · PQ ×7
  - *Numerical Methods*
      · PYQ ×30
      · PQ ×2
      · PYQ ×73
      · PQ ×36
- **Permutation and Combination**
  - *Basic Concepts & Counting Principles*
      · Demo: Permutation & Combination (Quick Revision & Practice Questions) (1.2h)
      · PYQ ×3
      · PQ ×2
  - *Permutations (with & without Repetition)*
      · Demo: Permutations with No Repetition (17m)
      · Demo: Permutations with Unlimited Repetitions (8m)
      · Permutations with Limited Repetitions (9m)
      · Tricks to Solve The Famous MISSISSIPPI Problem in P&C (13m)
      · Vowels & Consonants Type Questions in P&C (9m)
      · Tricks to Solve Questions on  Arrangement of Letters (9m)
      · Tricks to Solve Questions on  Arrangement of Digits  (1) (14m)
      · Tricks to Solve Questions on  Arrangement of Digits  (2) (6m)
      · PYQ ×2
      · PQ ×5
  - *Circular & Grouping Permutations*
      · Tricks to Solve Grouping Type Questions in P&C (12m)
      · Tricks for Problems on Choosing Items from Group of Items (14m)
      · Circular Arrangements (10m)
      · Circular Arrangements on Groups (10m)
      · Tricks to Solve  Necklace Based Problems (8m)
      · PQ ×1
  - *Combinations (with & without Repetition)*
      · Combinations with No Repetitions & Unlimited Repetitions (13m)
      · Solving Some Basic Questions on Permutation & Combination (14m)
      · An Important Property (Binomial Theorem) (6m)
      · Total Outcomes, MCQ Paper Solving, Unlimited Repetitions (10m)
      · PYQ ×6
      · PQ ×4
  - *Special Applied Problems*
      · Tricks to Solve Questions on  Binary Strings (10m)
      · Trick for Sum of all numbers formed from given digits (11m)
      · Finding Rank of a Word (Concept + Short Trick) (13m)
      · Question on Finding Rank of a Word Without Repetition (11m)
      · Short Trick to Find Rank of a Word With Repetitions (9m)
      · Short Trick to Find Number of Handshakes (10m)
      · Chocolate Picking Problem (6m)
      · Counting Sticks Approach (11m)
      · Short Tricks to Solve  Dice Sum Problem  (1) (10m)
      · Short Tricks to Solve  Dice Sum Problem  (2) (12m)
      · Conventional Method of Solving  Dice Sum Problem (7m)
      · Short Tricks for  Alphabet Selection Problem  in P&C (8m)
      · PYQ ×1
      · PQ ×2
  - *Advanced Counting Theorems*
      · Principle of Inclusion & Exclusion, Use of Venn Diagram (13m)
      · Number of Intersection Points & Parallelogram (7m)
      · Concept & Short Tricks of Derangement in P&C (11m)
      · Important Questions on Derangements (10m)
      · PYQ ×6
      · PQ ×4
  - *Multiple Topics*
      · PYQ ×18
      · PQ ×18
- **Probability**
  - *Basic Concepts and Terminology*
      · What is Sure Event, Impossible Event, Complementary Event (14m)
      · Short Trick to find total outcomes in an experiment (12m)
      · Mutually Exclusive Events & Exhaustive Events (17m)
      · Odds in Favour of an event & Odds Against An Event (11m)
      · Demo: What is Experiment, Event, Favorable & Total Outcome (15m)
      · PYQ ×3
      · PQ ×6
  - *Classical Problems (Cards, Dice, Coins, Digits, Number, Objects)*
      · Short Tricks to deal with cases of 'At least' & 'At most' (9m)
      · Tricks & Techniques to Solve Dice Sum Problems (16m)
      · Tricks & Techniques to Solve Playing Cards Problem (9m)
      · Finding Probability of 53 Sundays in a Leap Year (12m)
      · PYQ ×18
      · PQ ×17
  - *Probability Using Venn Diagrams & Set Theory*
      · Some Important Events (A AND B, A OR B, A BUT NOT B) (15m)
      · PYQ ×4
      · PQ ×4
  - *Conditional Probability*
      · PYQ ×4
      · PQ ×7
  - *Law of Total Probability*
      · PYQ ×6
      · PQ ×1
  - *Bayes Theorem (Inverse Probability)*
      · PYQ ×2
      · PQ ×1
  - *Probability Using Permutation & Combination Logic*
      · PYQ ×4
      · PQ ×7
  - *Continuous Probability Distribution, Random Variables & Expected Value*
      · PYQ ×18
      · PQ ×11
  - *Multiple Topics*
      · Quick Revision & Practice Questions - Part 1 (1.1h)
      · Quick Revision & Practice Questions - Part 2 (34m)
      · PYQ ×1
      · PYQ ×60
      · PQ ×54
- **Statistics**
  - *Introduction & Types of Data*
      · Basic Concepts (1.3h)
      · PQ ×2
  - *Mean, Median, and Mode for ungrouped data*
      · PQ ×8
  - *Mean, Median, and Mode for grouped data*
      · Advance Concepts (56m)
      · PYQ ×1
      · PQ ×1
  - *Range, Mean Deviation, Variance, and Standard Deviation*
      · PYQ ×4
      · PQ ×8
  - *Multiple Topics*
      · PQ ×4
      · PYQ ×5
      · PQ ×23
      · PYQ ×493
      · PQ ×261
      · IOCL - Unit Test - Engineering Mathematics (45m)

### 2. Digital Logic — 147 vids · 16.2h · 284 PYQs · 236 PQs

- **Digital Systems & Boolean Basics**
  - *Digital Fundamentals & Boolean Algebra*
      · Blueprint of Digital Electronics (10m)
      · Demo: History of Digital electronics (8m)
      · Advantage of Digital System (9m)
      · History of Digital System (11m)
      · Digital System Designing (13m)
      · Boolean Algebra Laws (12m)
      · De Morgan's Law (2m)
      · PYQ ×9
      · PQ ×17
      · PYQ ×9
      · PQ ×17
- **Logic Gates & Hardware**
  - *Evolution, NOT, OR & AND Gates*
      · basics of logic gates (6m)
      · Not Gate (3m)
      · OR Gate (3m)
      · AND Gate (3m)
      · PYQ ×2
      · PQ ×8
  - *Universal Gates: NAND & NOR*
      · NOR Gate (9m)
      · NAND Gate (6m)
      · PYQ ×4
      · PQ ×12
  - *Ex-OR, Ex-NOR Gate & Relation*
      · EX OR gate (11m)
      · Practice Question_ (1m)
      · EX NOR gate (7m)
      · EX OR gate vs EX NOR gate relationship part 1 (4m)
      · EX OR gate vs EX NOR gate relationship part 2 (5m)
      · PYQ ×17
      · PQ ×10
      · PYQ ×23
      · PQ ×30
- **Boolean Expression**
  - *SOP & POS Canonical Forms*
      · Basics of Boolean expression (6m)
      · SOP (10m)
      · Canonical SOP form (6m)
      · POS (7m)
      · Canonical POS form (3m)
      · PYQ ×7
      · PQ ×9
  - *Boolean Function Counts*
      · No of Function possible (8m)
      · Complement of a function (9m)
      · Idea of Duality (10m)
      · Neutral functions (3m)
      · Self Dual Functions (4m)
      · How to find Self Dual Functions (7m)
      · Orthogonal Function (4m)
      · No of Orthogonal Function (5m)
      · PYQ ×4
      · PQ ×10
  - *Functional Completeness*
      · Functionally Complete Function (7m)
      · Practice Question (4m)
      · Partially complete Function (3m)
      · Practice Questions (2m)
      · PYQ ×5
      · PQ ×5
  - *Universal Realization*
      · Implementing every gate with NAND Gate (7m)
      · Implementing every gate with NOR Gate (6m)
      · Relationship between AND & OR gates (6m)
      · AND-OR (NAND-NAND Implementation) (5m)
      · OR-AND (NOR-NOR Implementation) (3m)
      · PYQ ×5
      · PQ ×3
      · PYQ ×21
      · PQ ×27
- **Boolean Minimization**
  - *K-Map Structure & PIs*
      · Basics of Simplification (10m)
      · Understanding K MAP part 1 (9m)
      · Understanding K MAP part 2 (10m)
      · Understanding K MAP part 3 (6m)
      · POS K Map (3m)
      · What is minimal Boolean expression (3m)
      · Rules of grouping (14m)
      · Don't care condition (5m)
      · Practice on K Map (7m)
      · More than one solution (4m)
      · Prime Implicant (7m)
      · Practice Question (2m)
      · Practice Questions (3m)
      · Practice Question (3m)
      · Practice Question (4m)
      · Solving K Map in reverse fashion (2m)
      · PYQ ×29
      · PQ ×15
  - *Function Equivalence*
      · Gate 2000_ (3m)
      · gate 2002_ (2m)
      · PYQ ×10
      · PQ ×4
  - *Logic Circuit Analysis*
      · Understanding direct operations on Functions part 1 (5m)
      · Understanding direct operations on Functions part 2 (5m)
      · Irredundant Function (6m)
      · PYQ ×10
      · PQ ×2
  - *Adv. Laws & Optimization*
      · Absorption Law (6m)
      · Practice Question (2m)
      · PYQ ×4
      · PQ ×11
      · PYQ ×53
      · PQ ×32
- **Combinational Circuit**
  - *Adders & Subtractors*
      · Basics of combinational circuit (6m)
      · Fundamental of Adders (8m)
      · Half Adder (8m)
      · Full Adder (9m)
      · Implementing Full Adder Using Half Adder (4m)
      · Half Subtractor (11m)
      · Full Subtractor (33m)
      · PYQ ×9
      · PQ ×13
  - *CLA & Arithmetic Logic*
      · Four-bit Parallel Adder  Ripple Adder (7m)
      · Four-bit Parallel-Ripple Adder-Subractor (7m)
      · Look Ahead Carry Adder (14m)
      · PYQ ×7
      · PQ ×1
  - *Multiplexers (MUX)*
      · Basics of Multiplexer (11m)
      · Implementing 2x1 Multiplexer (7m)
      · Implementing 4x1 Multiplexer (5m)
      · Practice Question (2m)
      · Multiplexer Expansion Part-1 (5m)
      · Multiplexer Expansion Part-2 (6m)
      · PYQ ×21
      · PQ ×5
  - *DeMux, Decoder & Encoder*
      · Basics of DeMultiplexer (4m)
      · Implementing 1x2 DeMultiplexer (5m)
      · Implementing 1x4 DeMultiplexer (5m)
      · DEMux_practice_question (2m)
      · Basics of Decoder (8m)
      · Implementing 1x2 Decoder (4m)
      · Implementing 2x4 Decoder (3m)
      · Understanding Decoder Application (4m)
      · Decoder Expansion (3m)
      · Decoders (5m)
      · Decoder_Practice_Question (2m)
      · Decoder (1m)
      · Understanding Encoder (3m)
      · Implementing 2x1 Encoder (4m)
      · Priority Encoder (4m)
      · PYQ ×9
      · PQ ×4
  - *Special Logic Circuits*
      · PYQ ×10
      · PQ ×5
  - *Hazards & Timing*
      · Hazard (16m)
      · static hazard (3m)
      · static hazard_pq (2m)
      · PYQ ×4
      · PQ ×1
      · PYQ ×60
      · PQ ×29
- **Sequential Circuits**
  - *Seq. Logic & Latches*
      · Idea of Sequential Circuits (5m)
      · What are Latches (5m)
      · Nor Latch (12m)
      · NAND Latch (6m)
      · PYQ ×2
      · PQ ×2
  - *Flip-Flops & Conversion*
      · RSSR Flip Flop (15m)
      · Understanding Flip-Flop Triggering (15m)
      · Understanding Flip-Flop Further (5m)
      · JK Flip-Flop (12m)
      · T Flip-Flop (7m)
      · D Flip-Flop (5m)
      · Flip-Flop Conversion (6m)
      · Convert T Flip-Flop To JK Flip Flop (3m)
      · PYQ ×13
      · PQ ×9
  - *Sync Counter Analysis*
      · Basics of Counters (8m)
      · Understanding Counting of a Flip Flop Part-1 (6m)
      · Gate 2001_ (3m)
      · Gate 2000_ (3m)
      · PYQ ×14
      · PQ ×5
  - *Sync Counter Design*
      · Understanding Counting of a Flip Flop Part-2 (4m)
      · Practice Question (29m)
      · Practice Question (3m)
      · PYQ ×5
      · PQ ×3
  - *Ripple (Async) Counters*
      · Ripple and Asynchronious Counter (9m)
      · Ripple and Asynchronous Counter Further (7m)
      · Ripple and Asynchronous Counter Using Clock (8m)
      · Synchronous Vs Asynchronous Counter (4m)
      · Self-Staring And Free-Running Counter (4m)
      · Restricted Mode Counter (4m)
      · Restricted Mode Counter further (1m)
      · PYQ ×4
  - *Shift Registers*
      · Basics of register (5m)
      · Serial In Serial Out Register (8m)
      · Serial In Parallel Out Register (3m)
      · Parallel In Serial Out Register (4m)
      · Parallel In Parallel Out Register (2m)
      · Practice Question (2m)
      · PYQ ×3
      · PQ ×3
  - *Ring & Johnson Counters*
      · Ring Counter (5m)
      · Johnson Counter (3m)
      · PYQ ×5
      · PQ ×2
      · PYQ ×46
      · PQ ×24
- **Number System**
  - *Basics & Decimal Convert*
      · Basics of Number System Part-1 (9m)
      · Basics of Number System Part-2 (7m)
      · PYQ ×1
      · PQ ×7
  - *General Base Conversion*
      · Any Base to Decimal (5m)
      · Decimal to Any Base (5m)
      · 720p_5.15 Net 2013 (2m)
      · PYQ ×13
      · PQ ×8
  - *Binary, Octal & Hex*
      · Base 2 Conversion Directly (4m)
      · PYQ ×15
      · PQ ×25
      · PYQ ×29
      · PQ ×40
- **Number Representation**
  - *Basics to 1s Complement*
      · Unsigned Number representation (5m)
      · Basics of Signed Binary Number (5m)
      · Signed Magnitude Representation Part-1 (5m)
      · Signed Magnitude Representation Part-2 (4m)
      · 1's Complement Representation (6m)
      · PYQ ×5
      · PQ ×3
  - *2s Complement & Math*
      · 2's Complement Representation (5m)
      · PYQ ×26
      · PQ ×13
  - *BCD & Special Codes*
      · BCD (7m)
      · Excess 3 Code (8m)
      · Gray Code (29m)
      · Gray Code to Binary Code Conversion (9m)
      · PYQ ×12
      · PQ ×21
      · PYQ ×43
      · PQ ×37
      · PYQ ×284
      · PQ ×236
      · IOCL - Unit Test - Digital Logic (45m)

### 3. Computer Architecture — 119 vids · 11.7h · 258 PYQs · 230 PQs

- **Basics of COA**
  - *Introduction, H/W & S/W*
      · Demo: Introduction to Computer System (12m)
      · PYQ ×1
      · PQ ×4
  - *Input Output Devices*
      · Input and Output Devices (8m)
      · PYQ ×3
      · PQ ×15
  - *Basics of Memory*
      · Units of Memory (7m)
      · Memory (Primary, Secondary, Cache) (7m)
      · SRAM DRAM (7m)
      · ROM (6m)
      · Secondary Memory (4m)
      · PYQ ×1
      · PQ ×47
  - *Evolution & History*
      · Evolution and History (13m)
      · History (4m)
      · PQ ×16
  - *CPU Organization Basics*
      · CPU Components (12m)
      · General Operations Order (4m)
      · Types of Registers Part-1 (9m)
      · Types of Registers Part-2 (6m)
      · Register Transfer (6m)
      · Memory Extension (6m)
      · PYQ ×4
      · PQ ×24
      · PYQ ×9
      · PQ ×106
- **Floating Point Rep**
  - *Floating Point Basics*
      · Demo: Floating Point Representation (12m)
      · Implicit Normalisation in Floating Point (5m)
      · PYQ ×8
      · PQ ×3
  - *IEEE 754 Standards*
      · IEEE 754 Representation (8m)
      · IEEE 754 Single Precision (5m)
      · Practice Question (1m)
      · Practice Question (4m)
      · Practice Question (5m)
      · Practice Question (4m)
      · PYQ ×16
      · PQ ×16
  - *Booth’s Algorithm*
      · Booth's Algorithm (9m)
      · PYQ ×7
      · PQ ×3
      · PYQ ×31
      · PQ ×22
- **Cache Memory Organization**
  - *Memory Chip Configuration*
      · Memory Organization (3m)
      · Memory Chip Configuration (9m)
      · Cell Size Classification (8m)
      · Memory Address Information (2m)
      · Memory Interpretation Mechanism (7m)
      · PYQ ×3
      · PQ ×1
  - *Hierarchy & Locality*
      · Introduction to Memory Hierarchy Part-1 (9m)
      · Introduction to Memory Hierarchy Part-2 (9m)
      · Locality of Reference (7m)
      · Cache Hit, Cache Miss & Mapping Type (5m)
      · PYQ ×13
      · PQ ×7
  - *Units & Cache Mapping Techniques Basics*
      · Units for Memory Management (9m)
      · Cache Mapping Technique (8m)
      · PYQ ×3
      · PQ ×3
  - *Direct Mapping*
      · Direct Mapping Part-1 (7m)
      · Direct Mapping Part-2 (7m)
      · Direct Mapping Part-3 (6m)
      · Practice Question - 1 (3m)
      · Practice Question - 2 (2m)
      · Practice Question - 3 (3m)
      · Practice Question - 4 (3m)
      · PYQ ×13
      · PQ ×2
  - *Associative Mapping*
      · Associative Mapping part-1 (5m)
      · Associative Mapping part-2 (5m)
      · Practice Question - 1 (2m)
      · PYQ ×2
      · PQ ×1
  - *Set Associative Mapping*
      · Set Associative Mapping Part-1 (5m)
      · Set Associative Mapping Part-2 (4m)
      · Practice Question (2m)
      · Practice Questions (4m)
      · Practice Question (Gate 1990) (2m)
      · PYQ ×22
      · PQ ×4
  - *Cache Replacement Policies & Miss Types*
      · Cache replacement policies (2m)
      · FIFO (3m)
      · Optimal (3m)
      · LRU (2m)
      · Miss Type (3m)
      · PYQ ×5
      · PQ ×3
  - *Memory Organisation & Performance*
      · Basics of Memory Organization (3m)
      · Practice Question (2m)
      · PYQ ×15
      · PQ ×5
  - *Coherence & Write Policy*
      · Cache Coherence Problem (5m)
      · PYQ ×5
      · PQ ×1
      · PYQ ×81
      · PQ ×27
- **Input Output Organisation**
  - *Interface & Addressing*
      · Basics of IO Devices and Interface (6m)
      · Data Bus, Address Bus and Control Bus (6m)
      · Memory Mapped IO (6m)
      · Isolated IO (4m)
      · IO Processor (4m)
      · PYQ ×8
      · PQ ×6
  - *Programmed IO*
      · Programmed IO (8m)
      · PQ ×1
  - *Interrupt Driven IO*
      · Interrupt Cycle (13m)
      · Types of Interrupts (11m)
      · Interrupt Priority (6m)
      · Interrupt Initiated IO (7m)
      · PYQ ×20
      · PQ ×2
  - *Direct Memory Access DMA*
      · Direct Memory Access (DMA) (6m)
      · PYQ ×17
      · PQ ×5
  - *Disk Structure & Address*
      · Secondary Memory Transfer Time (10m)
      · Practice Questions (2m)
      · PYQ ×8
      · PQ ×7
  - *Disk Access Time & Performance*
      · Basics of Transfer Time (10m)
      · Practice Questions (6m)
      · Practice Questions (4m)
      · Practice Question (Gate 1993) (3m)
      · Disk Interleaving (4m)
      · PYQ ×8
      · PQ ×4
      · PYQ ×61
      · PQ ×25
- **Pipelining**
  - *Pipelining Basics*
      · Demo: Uniprocessing (6m)
      · Uniprocessing Vs Multiprocessing (4m)
      · IBM 801 Architecture (13m)
      · Basics of Pipelining (8m)
      · Practice Question (8m)
      · Practice Question (2m)
      · PYQ ×4
      · PQ ×4
  - *Performance & Speedup*
      · Speed up Derivation (6m)
      · Clock Per Instruction=1 (4m)
      · Problem with Pipelining (5m)
      · PYQ ×10
      · PQ ×12
  - *Structural & Control Hazards*
      · Structural Hazards (4m)
      · Control Hazards (4m)
      · Solution of Control Hazards (7m)
      · PYQ ×10
      · PQ ×1
  - *Data Hazards & Soln*
      · Data Hazards (4m)
      · Practice Question (Gate 2010) (6m)
      · PYQ ×10
      · PQ ×6
  - *Vector Processing Unit*
      · Vector Processing (6m)
      · How Vector Processing Works (10m)
      · Types of Vector Processing (6m)
      · PYQ ×1
      · PYQ ×35
      · PQ ×23
- **Instr Formats & Modes**
  - *Instruction Structure*
      · 4 Address (5m)
      · 3 Address (3m)
      · 2 Address (3m)
      · 1 Address (3m)
      · 0 Address (2m)
      · Practice Question (3m)
      · Practice Question (3m)
      · Practice Question (2m)
      · PYQ ×6
      · PQ ×4
  - *Basic Addressing Modes*
      · Addressing Modes (5m)
      · Immediate Mode Addressing (4m)
      · Absolute Addressing Mode (4m)
      · Indirect Mode Addressing (4m)
      · Implied Mode (1m)
      · Register Mode (2m)
      · Register Indirect Mode (3m)
      · PYQ ×13
      · PQ ×12
  - *Complex & Rel Modes*
      · Base Register (3m)
      · Index Addressing (2m)
      · PYQ ×10
      · PYQ ×29
      · PQ ×16
- **Control Unit Design**
  - *Instruction Types*
      · IR (10m)
      · Instruction (5m)
      · IR (4m)
      · Memory References (5m)
  - *Hardwired & Microprogrammed CU*
      · Hardwired Control Unit (9m)
      · Microprogrammed Control Unit (7m)
      · Practice Question-1 (4m)
      · Practice Question-2 (8m)
      · PYQ ×10
      · PQ ×5
  - *RISC vs CISC Arch*
      · RISC Vs CISC (7m)
      · PYQ ×2
      · PQ ×6
      · PYQ ×12
      · PQ ×11
      · PYQ ×258
      · PQ ×230
      · IOCL - Unit Test - Computer Architecture (45m)

### 4. Programming and Data Structures — 241 vids · 22.6h · 471 PYQs · 367 PQs

- **C Fundamentals**
  - *Intro & Data Types*
      · Introduction of C (7m)
      · UNDERSTANDING LANGUAGE (7m)
      · Types of Variables (9m)
      · C PROGRAMMING - OUR FIRST PROGRAM (14m)
      · Printf & Scanf (7m)
      · Main & Command Line Arguments (25m)
      · Garbage Values (12m)
      · PYQ ×4
      · PQ ×15
  - *Operators & Expressions*
      · Instructions and Operations (8m)
      · Integer to float conversion (type casting) (8m)
      · Practice Question-Arithmetic Exp (1m)
      · PYQ ×7
      · PQ ×10
  - *Understanding Operators*
      · SizeOf Operator (8m)
      · Unary Operator (4m)
      · Bitwise Operator (7m)
      · Types of Swapping (5m)
      · Increment decrement operator (3m)
      · Logical Operator (6m)
      · Practice Questions - Logical Operator (6m)
      · Ternery Operator (4m)
      · PQ ×2
  - *Data Type Fundamentals*
      · Data Types (8m)
      · chars,signed and unsigned (6m)
      · Data Types (3m)
      · PYQ ×3
      · PQ ×5
  - *Integral Datatypes*
      · IDTs (3m)
      · Cyclic nature of Integral Data Type (Int) (11m)
      · Cyclic nature of Integral Data Type (Char) (3m)
      · Practice Question IDT - 1 (2m)
      · Practice Question IDT - 2 (2m)
  - *Intro of Flowcharts*
      · Flowcharts (32m)
      · PQ ×11
      · PYQ ×14
      · PQ ×43
- **Control Flow**
  - *If-Else Statements – Basic, Advanced & Nested If–Else Structures*
      · Conditional Statements(Decision Control) in C (10m)
      · If-Else Statements_PQ (9m)
      · PYQ ×5
      · PQ ×5
  - *Loops & Iteration*
      · The While Loop (11m)
      · For Loop (8m)
      · Break Statement (7m)
      · The Do While Loop (3m)
      · PYQ ×18
      · PQ ×9
  - *Switch & Jump Stmts*
      · Control statement (4m)
      · The GOTO Keyword (3m)
      · Avoid goto (3m)
      · PYQ ×1
      · PQ ×4
      · PYQ ×24
      · PQ ×18
- **Functions**
  - *Function Basics – Definition, Declaration, and Calling Mechanisms*
      · WHAT IS FUNCTIONS (9m)
      · TYPES OF FUNCTION (7m)
      · SCOPE RULE OF FUNCTION (3m)
      · PYQ ×6
      · PQ ×6
  - *Basic Recursion*
      · Function_Practice Question (3m)
      · PYQ ×24
      · PQ ×3
      · PYQ ×30
      · PQ ×9
- **Arrays & Pointers**
  - *Array Basics*
      · Demo: Introduction of Array -1 (4m)
      · Introduction of Array -2 (13m)
      · PYQ ×20
      · PQ ×2
  - *Pointer Basics – Declaration, Initialization, and Dereferencing*
      · AN INTRODUCTION TO POINTERS (11m)
      · POINTERS DECLARATION (4m)
      · PYQ ×10
      · PQ ×6
  - *Relationship Between Arrays and Pointers*
      · Relationship between Array and Pointers (7m)
      · Address Representation (17m)
      · Address Operation (3m)
      · Address Operation - Substraction (2m)
      · Key points of Array (2m)
      · Practice question on Pointer (4m)
      · PYQ ×13
      · PQ ×8
  - *Character Pointer (String)*
      · Character Pointer (1m)
      · Character Pointer & String (6m)
      · PYQ ×7
      · PQ ×3
  - *Call By Value/Address/Reference*
      · Back to Function Calls (Parameter Passing) (6m)
      · Call by Address (2m)
      · PYQ ×14
      · PQ ×4
  - *Recursion with pointer*
      · PYQ ×4
      · PQ ×1
      · PYQ ×68
      · PQ ×24
- **Storage Classes, Structures & Enums**
  - *Storage classes*
      · Storage Class (5m)
      · Register Storage Class (2m)
      · Static Storage Class (3m)
      · External Storage Class (3m)
      · PYQ ×10
      · PQ ×10
  - *Structures - Declaration, Initialization & Union Comparison*
      · Structure in C (10m)
      · Union (3m)
      · PYQ ×7
      · PQ ×6
  - *Enums*
      · Enums in C (25m)
      · PYQ ×17
      · PQ ×16
- **DMA, Macros, Scoping & File Handling**
  - *Dynamic Memory Allocation*
      · DMA - malloc (10m)
      · DMA - calloc (5m)
      · DMA-Memory Leak Problem (3m)
      · PYQ ×2
      · PQ ×6
  - *Static and Dynamic Scoping*
      · Static & Dynamic Scoping (25m)
      · PYQ ×2
  - *Macros*
      · Macros (4m)
      · Types of Macros (1m)
      · Benifits of Macros (2m)
      · Practice Question - Macros (2m)
      · Practice Question - Macros 2 (1m)
      · Practice Question - Macro 4 (1m)
      · Practice Question - Macro 3 (1m)
      · PQ ×1
  - *File Handiling in C*
      · Introduction of File Handling (15m)
      · Create a File (6m)
      · Open a File in C (12m)
      · Write to a File (6m)
      · Read from a File (10m)
      · Close & Move a File (12m)
      · PYQ ×1
      · PQ ×1
      · PYQ ×5
      · PQ ×8
- **Introduction to DS**
  - *DS Basics & Types*
      · Why we study data structure and algorithm (5m)
      · What is data structure (5m)
      · Effects of Data Structure (3m)
      · Primitive Vs Non-Primitive Data Structure (5m)
      · Linear Vs Non-Linear Data Structure (3m)
      · Demo: Why we study data structure and algorithm (5m)
      · Demo: What is data structure (5m)
      · PYQ ×1
      · PQ ×7
      · PYQ ×1
      · PQ ×7
- **Array**
  - *Array Basics & Ops*
      · What is an Array (5m)
      · How to Declare & Initialize Array in C (3m)
      · Size of an Array (5m)
      · PYQ ×6
      · PQ ×10
  - *1D & 2D Addressing*
      · One Dimensional Array Access Formula (5m)
      · Practice question (2m)
      · Practice question (2m)
      · Two Dimensional Array (5m)
      · 2D Array Row Major Implementation (10m)
      · 2D Array Column Major Implementation (5m)
      · Practice Question (3m)
      · Practice Question (7m)
      · PYQ ×8
      · PQ ×13
  - *3D & Multi-dim Arrays*
      · 3D Array Implementation (6m)
      · PYQ ×2
      · PQ ×3
  - *Matrix Storage*
      · Lower Triangular Matrix | RMO (31m)
      · Lower Triangular Matrix |  CMO (16m)
      · Upper Triangular Matrix | CMO (11m)
      · Upper Triangular Matrix | RMO (11m)
      · Practice Question (8m)
      · Practice Question (3m)
      · Practice Question (5m)
      · Practice Question (7m)
      · PYQ ×2
      · PQ ×1
      · PYQ ×18
      · PQ ×27
- **Stack**
  - *Stack Basics & Ops*
      · Basic Idea Of Stack (8m)
      · Static Vs Dynamic Implementation Of Stack (4m)
      · Push Operation On Stack (6m)
      · Pop Operation on Stack (5m)
      · Stack Permutation (4m)
      · Practice Question (Gate 1994) (3m)
      · Practice Question (1m)
      · PYQ ×12
      · PQ ×23
  - *Infix Postfix Prefix*
      · Representation Of Expression (5m)
      · Infix To Prefix Conversion Of Expression (5m)
      · Infix To Postfix Conversion Of Expression (3m)
      · Tree method for conversion (3m)
      · Prefix and postfix conversion_pq (3m)
      · Conversion of Expression _PQ (1m)
      · PYQ ×10
      · PQ ×11
  - *Eval of Expressions*
      · Evaluation of expression Using Stack (4m)
      · Evaluation of Postfix Expression (2m)
      · Practice Question (2m)
      · PYQ ×8
      · PQ ×3
  - *Recursion & Stack*
      · Introduction to Recursion (6m)
      · Recursion Practice Question (4m)
      · Functions (5m)
      · Recursive Functions (7m)
      · recursive functions (7m)
      · Stack Practice questions (5m)
      · Stack Practice questions (5m)
      · Stack recursion Practice questions (3m)
      · Stack recursion Practice question (2m)
      · Stack recursion Practice questions (3m)
      · Recursion Practice questions (3m)
      · Stack Practice questions (10m)
      · Stack Practice questions (7m)
      · PYQ ×6
      · PQ ×8
  - *TOH & Classic Apps*
      · Tower of Hanoi (10m)
      · Practice Question (1m)
      · Fibonacci Number (10m)
      · Ackermann Function (4m)
      · PQ ×2
      · PYQ ×36
      · PQ ×47
- **Queue**
  - *Basics & Stack Mix*
      · Basic Idea Of Queue (5m)
      · Representation Of Queue (5m)
      · Enqueue Operation On Queue (5m)
      · Dequeue Operation On Queue (5m)
      · Problem With Simple Linear Queue (3m)
      · Queue_Practice Questions (1m)
      · Queue_Practice Questions (1m)
      · Queue_Practice Questions (2m)
      · PYQ ×14
      · PQ ×40
  - *Circular Queue*
      · Enqueue Operation On Circular Queue (6m)
      · Dequeue Operation On Circular Queue (4m)
      · PYQ ×3
      · PQ ×8
  - *Priority Queues & Variants*
      · Priority Queue (3m)
      · Stack_Practice Questions (1m)
      · PYQ ×1
      · PQ ×6
      · PYQ ×18
      · PQ ×54
- **Linked List**
  - *SLL Basics & Standard Operations*
      · Introduction To Link List (6m)
      · Analysis Of Link List (4m)
      · Link List Traversal Using Loop (4m)
      · Link List Traversal Using Recusrion (3m)
      · Searching An Element In Link List Using Loop (5m)
      · Searching An Element In LL Using Recursion (5m)
      · Insertion in Link List (4m)
      · Deletion From Link List (5m)
      · PYQ ×18
      · PQ ×17
  - *Structure Modification & Pointer Logic*
      · Reversing a Link List using Loop (6m)
      · Reversing a Link List using Recursion (4m)
      · Linked list Practice Questions (1m)
      · Linked listPractice Question (3m)
      · Stack Practice Questions (4m)
      · PYQ ×3
      · PQ ×2
  - *Doubly, Circular & Variants*
      · Header Link List (5m)
      · Doubly Link List (3m)
      · Header circular Doubly Link List (1m)
      · Linked List Practice Question (1m)
      · PYQ ×9
      · PQ ×6
      · PYQ ×30
      · PQ ×25
- **Tree**
  - *Binary Tree Basics & Props*
      · Introduction To Tree (5m)
      · Important Tree Terminology (7m)
      · Introduction To Binary Tree (5m)
      · Tree Practice Question (2m)
      · Binary Tree Practice question (7m)
      · PYQ ×23
      · PQ ×10
  - *Traversals & Construction*
      · Preorder Treversal of Binary Tree (5m)
      · Inorder Traversal Of Binary Tree (3m)
      · Post Order Traversal Of Binary Tree (2m)
      · Tree traversal Practice Question (2m)
      · Tree traversal Practice Question (1m)
      · Tree traversal Practice Question (1m)
      · Tree Practice Question (2m)
      · Tree Traversal Pseudocode (Pre-order) (8m)
      · Tree traversal Pseudocode (Inorder) (10m)
      · Tree Traversal Pseudocode (Post-Order ) (8m)
      · Tree Traversal Pseudocode PQ (7m)
      · Tree Traversal Pseudocode PQ (6m)
      · PYQ ×24
      · PQ ×7
  - *BST Basics & Operations*
      · Binary Search Tree (6m)
      · Insertion in Binary Search Tree (2m)
      · Deletion in BST (7m)
      · BST Practice Question (1m)
      · BST Practice Question (2m)
      · BST Practice Question (2m)
      · BST Practice Question (7m)
      · BST Practice Question (13m)
      · PYQ ×38
      · PQ ×14
  - *AVL Trees & Balancing*
      · AVL Tree (5m)
      · Insertion In AVL Tree (8m)
      · AVL Practice Question (11m)
      · AVL TREE Practice Question (1m)
      · AVL TREE Practice Questions (2m)
      · Deletion in AVL (8m)
      · Analysis of AVL (3m)
      · AVL TREE Practice Questions (3m)
      · PYQ ×12
      · PQ ×3
  - *Complete Binary Trees*
      · CBT (4m)
      · PYQ ×6
      · PQ ×3
  - *Advanced & k-ary Trees*
      · Threaded Binary Tree (15m)
      · K-ary Tree (9m)
      · K-ary Tree Practice Question 1 (8m)
      · K-ary Tree Practice Question 2 (3m)
      · K-ary Tree Practice Question 3 (2m)
      · K-ary Tree Practice Question 4 (6m)
      · K-ary Tree Practice Question 6 (3m)
      · K-ary Tree Practice Question 7 (2m)
      · K-ary Tree Practice Question 8 (2m)
      · Practice Question (1m)
      · PYQ ×13
      · PQ ×3
  - *Heaps & Priority Queues*
      · Heap (4m)
      · Practice Question-1 (3m)
      · Practice Question-2 (2m)
      · Practice Question-3( Insertion ) (2m)
      · Practice Question-4( deletion ) (3m)
      · PYQ ×34
      · PQ ×9
      · PYQ ×150
      · PQ ×49
- **Graphs**
  - *Graph Reps & Basics*
      · Introduction To Graph (5m)
      · Adjacency Matrix Representation (6m)
      · Adjacency List Representation (5m)
      · PYQ ×8
      · PQ ×4
  - *DFS & Applications*
      · Depth First Traversal (6m)
      · DFS Algo (5m)
      · Practice Question-1 (DFS) (3m)
      · Practice Question-2 (DFS) (2m)
      · PYQ ×8
      · PQ ×6
  - *BFS & Applications*
      · Breadth First Traversal (5m)
      · BFS Algo (3m)
      · Practice Question-1 (BFS) (1m)
      · Practice Question-2 (BFS) (2m)
      · PYQ ×11
      · PQ ×6
  - *Topological Sort & SCC*
      · classification of edges (15m)
      · types of edges (tree edge, backward edge ,forward edge ..) (5m)
      · PYQ ×7
      · PQ ×4
      · PYQ ×34
      · PQ ×20
- **Hashing**
  - *Hashing Basics & Functions*
      · Basics of Hashing (9m)
      · Characteristics of Good hash function (3m)
      · Most Popular Hash Function (3m)
      · Collision Resolution Technique (3m)
      · PYQ ×10
      · PQ ×6
  - *Open Addressing (Probing)*
      · Performance of Open Addressing (2m)
      · Linear Probing (6m)
      · Primary Secondary Clustering (3m)
      · Quadratic Probing (2m)
      · Double Hashing (2m)
      · Gate 2010 (3m)
      · PYQ ×12
      · PQ ×7
  - *Chaining & Perf Analysis*
      · Chaining (3m)
      · Practice Question-1 (Chaining) (3m)
      · PYQ ×4
      · PQ ×7
      · PYQ ×26
      · PQ ×20
      · PYQ ×471
      · PQ ×367
      · IOCL - Unit Test - Programming & Data Structures (45m)

### 5. Algorithms — 138 vids · 25.7h · 250 PYQs · 171 PQs

- **Algorithm Analysis**
  - *Algo Basics & Analysis*
      · What is Algorithm (5m)
      · Algorithm Development Cycle (6m)
      · Need for Analysis of Algorithm (4m)
      · Types of Analysis (5m)
      · Worst Best Average Case Analysis (7m)
      · Demo: Algorithm Classification (15m)
      · PYQ ×5
      · PQ ×12
  - *Asymptotic Notations*
      · Asymptotic Notations- Big O (9m)
      · Asymptotic Notations- Big Omega (3m)
      · Asymptotic Notations- Big Theta (5m)
      · Small Notations (2m)
      · Properties of Asymptotics Notations (6m)
      · PYQ ×7
      · PQ ×7
  - *Growth Rate Comparisons*
      · Practice Question 1 (11m)
      · Practice Question 2 (4m)
      · Log Basic Properties (13m)
      · Demo: Types of Functions (7m)
      · Decreasing Functions (9m)
      · Constant Functions (5m)
      · Logarithmic Functions (22m)
      · Ignore Logarithm Bases (2m)
      · Polynomial Functions (3m)
      · Exponential Functions (1m)
      · Logarithm Method - Asymptotic Comparison (12m)
      · Practice Questions (33m)
      · PYQ ×15
      · PQ ×2
      · PYQ ×27
      · PQ ×21
- **Time Complexity Analysis**
  - *Iterative Loops & Code*
      · Demo: Basics of Time Complexity (11m)
      · Space Complexity (12m)
      · Loops Time Complexity - 1 (8m)
      · Loops Time Complexity - 2 (22m)
      · Loops Time Complexity - 3 (19m)
      · Loops Time Complexity - 4 (16m)
      · Loops Time Complexity - 5 (17m)
      · Loops Time Complexity - 6 (17m)
      · Loops Time Complexity - 7 (18m)
      · Loops Time Complexity - 8 (12m)
      · Loops Time Complexity - 9 (18m)
      · Loops Time Complexity - 10 (35m)
      · PYQ ×20
      · PQ ×15
  - *Advance Iterative Loops & Code*
      · Loops Time Complexity - 1 (29m)
      · Loops Time Complexity - 2 (23m)
      · Loops Time Complexity - 3 (17m)
      · Loops Time Complexity - 4 (33m)
      · Loops Time Complexity - 5 (15m)
      · Loops Time Complexity - 6 (15m)
      · Loops Time Complexity - 7 (14m)
      · PQ ×2
  - *Substitution Method*
      · AP and GP Series (29m)
      · Recurrence Relation - 1 (19m)
      · Recurrence Relation - 2 (20m)
      · Recurrence Relation - 3 (26m)
      · Recurrence Relation - 4 (11m)
      · Recurrence Relation - 5 (15m)
      · Recurrence Relation - 6 (18m)
      · Recurrence Relation - 7 (11m)
      · Recurrence Relation - 8 (7m)
      · Recurrence Relation - 9 (4m)
      · Recurrence Relation - 10 (20m)
      · Recurrence Relation - 11 (18m)
      · Recurrence Relation - 12 (14m)
      · Recurrence Relation - 13 (8m)
      · Recurrence Relation - 14 (17m)
      · PYQ ×23
      · PQ ×7
  - *Recursion Tree Method*
      · Divide and Conquer Approach (35m)
      · Recurrence Relation - 1 (27m)
      · Recurrence Relation - 2 (22m)
      · Recurrence Relation - 3 (14m)
      · Recurrence Relation - 4 (19m)
      · Recurrence Relation - 5 (13m)
      · PYQ ×3
      · PQ ×2
  - *Master Theorem*
      · Master Theorem Case 1 (12m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Master Theorem Case 2 (4m)
      · Practice Question (3m)
      · Master Theorem Case 3 (5m)
      · Subtract and Conquer (2m)
      · PYQ ×14
      · PQ ×4
  - *Change of Variable Method*
      · Change of Variable Method (10m)
      · Practice Question - 1 (5m)
      · Practice Question - 2 (6m)
      · PYQ ×60
      · PQ ×30
- **Sorting Algorithms**
  - *Introduction to Sorting*
      · Introduction to Sorting Algo (7m)
      · PYQ ×6
      · PQ ×1
  - *Selection Sort*
      · Selection Sort (9m)
      · Analysis of Selection Sort (6m)
      · PYQ ×3
      · PQ ×4
  - *Bubble Sort*
      · Bubble sort (10m)
      · Analysis of Bubble Sort (7m)
      · Practice Questions (1m)
      · PYQ ×2
      · PQ ×2
  - *Insertion Sort*
      · Insertion Sort (10m)
      · Analysis of Insertion Sort (4m)
      · Practice Question (2m)
      · PYQ ×3
      · PQ ×5
  - *Merge Sort*
      · Merge Sort (10m)
      · Analysis of Merge Sort (8m)
      · Practice Question (2m)
      · Practice Question (1m)
      · PYQ ×11
      · PQ ×12
  - *Heap Sort*
      · Heap Sort (10m)
      · Analysis of Heap Sort (5m)
      · PYQ ×3
  - *Quick Sort*
      · Quick sort (8m)
      · Analysis of Quick Sort (4m)
      · Practice Question (2m)
      · Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · PYQ ×22
      · PQ ×17
  - *Radix & Counting Sort*
      · Demo: Counting Sort (34m)
      · Radix Sort Using Queue (23m)
      · Radix Sort Using Couting Sort (32m)
      · Radix Sort Practice Question (7m)
      · PYQ ×3
      · PQ ×1
  - *Comparisons & Searching*
      · Demo: Linear Search (12m)
      · Straight Binary Search (28m)
      · Recursive Binary Search (22m)
      · Straight Min Max Algorithm (31m)
      · DAC Min Max Algorithm (23m)
      · DAC Min Max Time Complexity (5m)
      · DAC Min Max Count Comparison (17m)
      · Min Max Practice Question (3m)
      · PYQ ×23
      · PQ ×26
      · PYQ ×76
      · PQ ×68
- **Greedy Algorithms**
  - *Greedy Basics & Huffman*
      · Introduction to Greedy Algorithm (7m)
      · Introduction to Huffman Coding (6m)
      · Practice Question (7m)
      · Practice Question (18m)
      · Practice Question (0m)
      · PYQ ×11
      · PQ ×8
  - *Optimal Merge Pattern*
      · Optimal Merge Patern (5m)
      · PYQ ×1
  - *Fractional Knapsack*
      · Knap Sack Problem (13m)
      · PQ ×1
  - *Job & Activity Selection*
      · Job Scheduling Problem (7m)
      · PYQ ×5
      · PQ ×1
      · PYQ ×17
      · PQ ×10
- **Dynamic Programming**
  - *Introduction to DP*
      · Introduction to Dynamic Algorithm (7m)
      · PYQ ×1
      · PQ ×7
  - *LCS & Subsequences*
      · Longest commom Subsequence Part-1 (14m)
      · Longest common Subsequence Part-2 (7m)
      · PYQ ×3
      · PQ ×3
  - *Matrix Chain Order*
      · Matrix Chain Multiplication Part - 1 (6m)
      · Matrix Chain Multiplication Part - 2 (14m)
      · Matrix chain Multiplication Part - 3 (2m)
      · PYQ ×5
  - *Floyd & Subset Sum*
      · Floyd Warshall Problem (7m)
      · Sum of Subset (7m)
      · PYQ ×14
      · PQ ×3
      · PYQ ×23
      · PQ ×13
- **Minimum Spanning Trees**
  - *MST & Kruskal's Algo*
      · Introduction to Spanning Tree (4m)
      · Kruskal Algo Part-1 (4m)
      · Kruskal Algo Part-2 (6m)
      · PYQ ×5
      · PQ ×4
  - *MST & Prim's Algo*
      · Prim's Algorithm (9m)
      · PYQ ×22
      · PQ ×4
      · PYQ ×27
      · PQ ×8
- **Shortest Path Algos**
  - *Dijkstra’s Algorithm*
      · Dijkastra Algorithm (10m)
      · 2019(2) (3m)
      · PYQ ×5
      · PQ ×11
  - *Bellman-Ford Algo*
      · Bellman- Ford Algorithm Part-1 (4m)
      · Bellman- Ford Algorithm Part-2 (6m)
      · Dijakstra and bellaman ford algorithim (5m)
      · DIjakstra algorithim and bellaman ford Practice questions (4m)
      · single source shortest path practice question (4m)
      · Practice Question (1m)
      · Greedy alogrithims (1m)
      · PYQ ×15
      · PQ ×10
      · PYQ ×20
      · PQ ×21
      · PYQ ×250
      · PQ ×171
      · IOCL - Unit Test - Algorithms (45m)

### 6. Theory Of Computation/Automata Theory — 187 vids · 19.7h · 320 PYQs · 127 PQs

- **Introduction to TOC**
  - *Basics & String Ops*
      · Introduction to Toc (5m)
      · Requirement Of TOC (6m)
      · What is symbol, Alphabet, String and Language (7m)
      · How to represent a Language (4m)
      · Some basic operations on strings (3m)
      · Reverse of a string (1m)
      · Empty-Null String (2m)
      · Substring (7m)
      · PRACTICE QUESTION STRINGS (2m)
      · Prefix and suffix (3m)
      · Practice question Proper prefixes (2m)
      · Kleene Closure (6m)
      · Practice Question Strings (3m)
      · PYQ ×2
      · PQ ×2
  - *Language Ops & Sets*
      · Set Operations on Languages (4m)
      · Practice Question Language (1m)
      · PYQ ×1
      · PQ ×2
      · PYQ ×3
      · PQ ×4
- **Deterministic FA (DFA)**
  - *DFA Basics & Definitions*
      · Basics of Finite Automata (7m)
      · Definition of deterministic Finite Automata (9m)
      · Representation of DFA (5m)
      · Acceptance By a DFA (4m)
      · Practice Question Strings (3m)
      · Practice Question Finite State Machine (1m)
      · PYQ ×9
  - *DFA Construction & Design*
      · DFA Designing where L={a} (4m)
      · DFA Designing where starts with substring s (8m)
      · DFA Designing where string ends with substring ‘s’ (12m)
      · DFA Designing string contains sub string s (6m)
      · DFA Designing string start and end with a (3m)
      · Practice Question Language (2m)
      · DFA Designing string start and end with same symbol (3m)
      · DFA Designing string start and end with different symbol (5m)
      · DFA Designing where starts with s = aaa or bbb (6m)
      · DFA Designing string ends with s = aaa or bbb (8m)
      · DFA Designing sting with substring s = aaa or bbb (4m)
      · Practice Questions Language (4m)
      · DFA Designing sting where |w| = 3, |w| <= 3, |w| >= 3 (6m)
      · DFA Designing sting where number of a = 2 (3m)
      · DFA Designing sting where number of a >= 2 (3m)
      · DFA Designing sting where |w|=0(mod3), |w|=1(mod4) (4m)
      · DFA Designing sting where number of a =0(mod3) (3m)
      · 720p _ 19.1 Gate 2015 (2m)
      · Practice Questions DFA (2m)
      · DFA Designing sting where odd occurance of subsring 'ab' (4m)
      · DFA Designing sting where even occurance of subsring 'baa' (3m)
      · How Many Different DFA's Can Be Designed Part-1 (5m)
      · How Many Different DFA's Can Be Designed Part-2 (5m)
      · Empty Language Acceptance (5m)
      · Universal Language Acceptance (3m)
      · DFA Designing where string contain b as 2nd symbol from left (4m)
      · DFA Designing where string contain b as 2nd symbol fromRight (10m)
      · DFA Designing where string start with a and w=omod3 (7m)
      · DFA Designing where string contain even number of a and b (9m)
      · |a|= 0(mod2) |b|= 0(mod3) |c|= 0(mod5) (2m)
      · DFA Design For String Has a Decimal (6m)
      · Design DFA for Language Part-1 (6m)
      · Design DFA for Language Part-2 (4m)
      · Design DFA for Language Part-3 (5m)
      · Design DFA for Language Part-4 (3m)
      · PYQ ×19
      · PQ ×9
  - *Complement & Minimization*
      · DFA Designing string contains sub string aaa (7m)
      · Basics of Minimization of DFA (10m)
      · Understanding Equal States (7m)
      · Practise Problem on Minimization  Part-1 (6m)
      · Practice Questions (7m)
      · PYQ ×10
      · PQ ×2
      · PYQ ×38
      · PQ ×11
- **Non-Deterministic FA**
  - *NFA Basics & Design*
      · Basics of NDFA (8m)
      · Important Points of NDFA (3m)
      · Acceptance By NDFA (4m)
      · NDFA Designing where starts with substring s (5m)
      · NDFA Designing where every string ends with substring s (7m)
      · NDFA Designing where every string contains  substring s (4m)
      · NDFA Designing where every string starts and ends with same (6m)
      · NDFA where every string starts and ends with different symbo (2m)
      · NDFA where every string starts with aaa or bbb (5m)
      · NDFA where every string of length =w, <=w, >=w (3m)
      · NDFA where every string contains exactly two a (4m)
      · NDFA where 3 symbol from right end is a (5m)
      · Practice Question (2m)
      · PYQ ×4
      · PQ ×1
  - *NFA to DFA Conversion*
      · Nfa and Dfa Equivalence (4m)
      · Nfa and Dfa Conversion Example - 1 (10m)
      · Nfa and Dfa Conversion Example - 2 (6m)
      · Nfa and Dfa Conversion Example - 3 (5m)
      · PYQ ×4
      · PQ ×5
  - *Epsilon NFA & Conversion*
      · NFA with Epsilon Moves (6m)
      · Conversion from Epsilon NFA to NFA (12m)
      · Practice Question (3m)
      · PYQ ×5
      · PQ ×3
  - *Regularity & Identification*
      · Regular Language Indetification Part-1 (9m)
      · Regular Language Indetification Part-2 (5m)
      · Regular Language Indetification Part-3 (7m)
      · Regular Language Indetification Part-4 (9m)
      · Regular Language Indetification Part-5 (7m)
      · Regular Language Indetification Part-6 (10m)
      · Regular Language Indetification Part-7 (4m)
      · PYQ ×9
      · PQ ×3
      · PYQ ×22
      · PQ ×12
- **Regular Expressions**
  - *Regex Basics & Definitions*
      · Basics of Regular Expressions (10m)
      · Equivalence between two Regular Expressions (5m)
      · Regular Expression to Regular Language (2m)
      · PYQ ×7
      · PQ ×2
  - *Regex Design & Algebra*
      · Regular Language to Regular Expression Part-1 (5m)
      · Regular Language to Regular Expression Part-2 (3m)
      · Regular Language to Regular Expression Part-3 (4m)
      · Regular Language to Regular Expression Part-4 (6m)
      · Regular Language to Regular Expression Part-5 (5m)
      · Regular Language to Regular Expression Part-6 (3m)
      · Regular Language to Regular Expression Part-7 (7m)
      · Regular Language to Regular Expression Part-8 (6m)
      · Regular Language to Regular Expression Part-9 (4m)
      · Algebraic Properties of Regular Expression (9m)
      · Identities of Regular Expression Part-1 (9m)
      · Identities of Regular Expression Part-2 (4m)
      · Practice Questions_RE (2m)
      · Practice Question_Language (1m)
      · PYQ ×15
      · PQ ×9
  - *FA to Regex Conversion*
      · Adern's Theorem (8m)
      · Conversion from Epsilon FA to RE Part-1 (7m)
      · Conversion from Epsilon FA to RE Part-2 (6m)
      · Conversion from Epsilon FA to RE Part-3 (7m)
      · PYQ ×11
      · PQ ×1
  - *Regex & FA Equivalence*
      · Conversion From RE in FA Part-1 (7m)
      · Conversion From RE in FA Part-2 (7m)
      · PYQ ×10
      · PQ ×1
      · PYQ ×43
      · PQ ×13
- **Grammar**
  - *Chomsky & Basics*
      · Definining Formal Grammar (11m)
      · Defining language by grammar (6m)
      · Equivalence between two Grammar (3m)
      · Chomoksy Classification of language (7m)
      · Type 0 Grammar (3m)
      · Type 1 Grammar (6m)
      · Type 2 Grammar (3m)
      · Type 3 Grammar (3m)
      · PYQ ×17
      · PQ ×8
  - *Grammar Design via Regex*
      · Practice Question (5m)
      · Practice Question (4m)
      · Practice Question (4m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Grammar Design form Regular Expression part-1 (6m)
      · Grammar Design form Regular Expression part-2 (7m)
      · Regular grammar to regular expression (5m)
      · Regular grammar to regular expression (4m)
      · PYQ ×9
      · PQ ×3
  - *Regular Grammar & FA*
      · Regular Grammar to Finite Automata (6m)
      · Finite Automata to Regular Grammar (6m)
      · PYQ ×4
      · PQ ×1
      · PYQ ×30
      · PQ ×12
- **Regular Language Properties**
  - *Decidability & Basics*
      · What Computer Science Deals With (5m)
      · Solvable Vs Unsolvable Problem Part-1 (10m)
      · Solvable Vs Unsolvable Problem Part-2 (9m)
      · Decidable Vs Undecidable Problem (5m)
      · P Vs NP Problem (2m)
      · Decision Properties for regular Language (9m)
      · PYQ ×2
      · PQ ×1
  - *Closure Properties*
      · Closure Properties of Regular Language (5m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (9m)
      · PYQ ×11
      · PQ ×7
  - *Pumping Lemma*
      · Pumping Lemma (8m)
      · PYQ ×5
      · PQ ×4
      · PYQ ×18
      · PQ ×12
- **Moore & Mealy Machines**
  - *Basics & Moore Machine*
      · Basic of moore vs mealy Machine (3m)
      · Moore machine (7m)
      · Practice problem on moore machine part-1 (5m)
      · PQ ×1
  - *Mealy Machine*
      · Mealy Machine (5m)
      · Practice Problem on mealy Machine (5m)
      · PYQ ×5
      · PQ ×4
  - *Conversion & Equivalence*
      · Conversion form moore to mealy machine (4m)
      · Conversion form mealy machine to moore (6m)
      · PYQ ×5
      · PQ ×5
- **Pushdown Automata & CFG**
  - *PDA Design & Basics*
      · Fundamental of CFL and PDA (6m)
      · Formal Definition of DPDA (6m)
      · Push, Pop and Skip Operations (6m)
      · PDA Design Practice Problem Part - 1 (8m)
      · PDA Design Practice Problem Part-2 (7m)
      · Design Practice Problem Part - 3 (5m)
      · PDA Design Practice Problem Part - 4 (7m)
      · PDA Design Practice Problem Part - 5 (4m)
      · Practice Question - 1 (5m)
      · Practice Question - 2 (4m)
      · Practice Question - 3 (4m)
      · PYQ ×13
      · PQ ×5
  - *CFL Identification*
      · CFL Identification - 1 (43m)
      · CFL Identification - 2 (32m)
      · CFL Identification - 3 (20m)
      · CFL Identification - 4 (28m)
      · CFL Identification - 5 (23m)
      · CFL Identification - 6 (21m)
      · CFL Identification - 7 (15m)
      · PYQ ×23
      · PQ ×7
  - *Context-Free Grammars*
      · Linear Grammar (4m)
      · PYQ ×31
      · PQ ×4
  - *Decision Properties*
      · Empty Vs Non-Empty Decision Properties for CFL (6m)
      · Finiteness Vs Infiniteness Decision Properties for CFL (4m)
      · Membership Decison Properties for CFL (9m)
      · decidability  of CFG (2m)
      · PYQ ×4
      · PQ ×2
  - *Closure Properties*
      · Closure Properties  of DCFL vs CFL (3m)
      · PYQ ×17
      · PQ ×10
      · PYQ ×88
      · PQ ×28
- **Turing Machines**
  - *TM Basics & Design*
      · Fundamentals of Turing Machine (6m)
      · Formal Defination of Turing machine with components (8m)
      · Turing Machine Design Practice Problem Part-1 (10m)
      · Turing Machine Design Practice Problem Part-2 (7m)
      · Turing Machine Design Practice Problem Part-3_ (9m)
      · Adding Two Unary Number (6m)
      · Converting Unary to Binary (7m)
      · Turing Machine_Practice Questions_1 (10m)
      · Halting Problem (8m)
      · PYQ ×6
      · PQ ×6
  - *TM Variations & UTM*
      · Versions of Turing Machine (3m)
      · Universal Turing Machine (7m)
      · PYQ ×5
      · PQ ×1
  - *Decision Properties*
      · Decision Properties for RS and REL (1m)
      · PYQ ×22
      · PQ ×11
  - *Closure Properties*
      · Closure Properties for Recursive Set and REL (2m)
      · PYQ ×14
      · PQ ×5
  - *Linear Bounded Automata*
      · LBA (4m)
      · PYQ ×2
      · PYQ ×49
      · PQ ×23
- **Complexity Theory**
  - *P, NP & Reducibility*
      · Fundamentals of Complexity Theory (5m)
      · PYQ ×24
      · PQ ×7
      · PYQ ×24
      · PQ ×7
      · PYQ ×320
      · PQ ×127
      · IOCL - Unit Test - Theory of Computation (45m)

### 7. Compiler Design — 120 vids · 12.6h · 191 PYQs · 121 PQs

- **Intro to Compilers**
  - *Lang Processing System*
      · Introduction To Compiler Design (3m)
      · What is Preprocessing (5m)
      · What is Compiler (5m)
      · What is Assembling (2m)
      · Loaded and Linker (3m)
      · Compiler Vs Interpreter (6m)
      · History of Compiler (3m)
      · PYQ ×6
      · PQ ×4
  - *Phases of Compiler*
      · Phases of Compiler (9m)
      · PYQ ×9
      · PQ ×4
  - *Sym Table, Errors & Passes*
      · Symbol Table (3m)
      · Compiler  Error Handler (1m)
      · Compiler  passes (3m)
      · PYQ ×9
      · PQ ×5
      · PYQ ×24
      · PQ ×13
- **Lexical Analysis**
  - *Lexical Analysis & Tokens*
      · What is Lexical Analyser (7m)
      · Secondary Functions of Lexical Analyser (3m)
      · Implementation of Lexical Analyser (4m)
      · Token_Practice Questions (2m)
      · PYQ ×11
      · PQ ×21
      · PYQ ×11
      · PQ ×21
- **Grammar & CFG**
  - *Grammar Basics & Chomsky*
      · Introduction to Formal Grammar (11m)
      · Defining Langugae by Grammar (6m)
      · Equivalence Between Grammar (3m)
      · Chomsky Classification of Grammar (7m)
      · Type-0 Grammar (3m)
      · Type-1 Grammar (6m)
      · Type-2 Grammar (3m)
      · Type-3 Grammar (3m)
      · PYQ ×5
  - *Derivation & Recursion*
      · Understanding Derivation of String (3m)
      · Recursive Grammar (5m)
      · Process of making Grammar Compiler Friendly (6m)
      · Removing Left Recursion (6m)
      · Practice Questions (4m)
      · Practice Questions (2m)
      · Practice Questions (6m)
      · PYQ ×3
      · PQ ×2
  - *Ambiguity & Inherent Amb*
      · What is Ambiguous Grammar (4m)
      · What is Inherently Ambiguous Grammar (2) (5m)
      · Practice Questions (4m)
      · Practice Questions (2m)
      · PYQ ×3
      · PQ ×5
  - *Left Factoring & Prefixes*
      · Non-Deterministic Grammar (5m)
      · Converting a Grammar Into Deterministic Grammar (4m)
      · Practice Question (4m)
  - *Simplification of CFG*
      · Simplification of CFG (7m)
      · Removal of Unit Productions (4m)
      · Removal of Useless Symbols (3m)
      · Practice Questions (3m)
      · PYQ ×2
  - *Normal Forms & BNF*
      · Chomsky Normal Form (6m)
      · Greibeck Normal Form (4m)
      · BNF-Backus normal formal (1m)
      · PYQ ×1
      · PQ ×2
  - *Decidability & CYK Algo*
      · CYK Algorithim (1m)
      · PQ ×1
      · PYQ ×14
      · PQ ×10
- **Syntax Analysis: Top-Down**
  - *Parser Basics & Top-Down*
      · What is Syntax Analysis (5m)
      · Understanding Top Down Parser (6m)
      · Brute Force Technique (6m)
      · PYQ ×7
      · PQ ×2
  - *First and Follow Sets*
      · Understanding First Function (7m)
      · Practice Problem on First Function (8m)
      · Practice Questions (2m)
      · Understanding Follow Function (7m)
      · Practice Problem on Follow Function (3m)
      · PYQ ×4
      · PQ ×1
  - *LL(1) Parser & Table*
      · Basic Requirement For LL(1) Parser (5m)
      · Designing LL(1) Parser Part-1 (8m)
      · Designing LL(1) Parser Part-2 (6m)
      · Designing LL(1) Parser Part-3 (6m)
      · Block Diagram of LL(1) Parser (7m)
      · Short Cut Techniques for LL(1) Grammar (5m)
      · Practice Question (3m)
      · LL(1)-Practicce question (3m)
      · LL(1)-Practice question (1m)
      · PYQ ×13
      · PQ ×8
      · PYQ ×24
      · PQ ×11
- **Syntax Analysis: Bottom-Up**
  - *Intro to Bottom-Up & LR(0)*
      · Bottom Up Parser Fundamentals Part-1 (8m)
      · Bottom Up Parser Fundamentals Part-2 (5m)
      · Designing LR(O) Parser Part-1 (8m)
      · Designing LR(O) Parser Part-2 (7m)
      · Designing LR(O) Parser Part-3 (6m)
      · Designing LR(O) Parser Part-4 (7m)
      · Designing LR(O) Parser Part-5 (4m)
      · Practice Questions (1m)
      · PYQ ×9
      · PQ ×5
  - *SLR(1) Parser & Conflicts*
      · SLR(1) Praser 1 (5m)
      · Practice Questions (2m)
      · PYQ ×2
      · PQ ×1
  - *CLR(1) Parser & Items*
      · CLR(1) Praser Part-1 (11m)
      · CLR(1) Praser Part-2 (5m)
      · Practice Questions (1m)
      · PYQ ×5
      · PQ ×5
  - *LALR(1) Parser & Merging*
      · LALR(1) Part - 1 (8m)
      · LALR(1) Part - 2 (8m)
      · LALR(1) Part-3 (8m)
      · Gate 2001 (1m)
      · PYQ ×15
      · PQ ×8
  - *Operator Precedence*
      · OPG (3m)
      · PYQ ×14
      · PQ ×4
      · PYQ ×45
      · PQ ×23
- **Semantic Analysis & SDT**
  - *Semantic Analysis & SDT*
      · Basic of Syntax Directed Translation (5m)
      · Practice Question (3m)
      · Practice Question (3m)
      · Practice Question (4m)
      · Practice Question (3m)
      · practice questions (1m)
      · Practice Question (2m)
      · PYQ ×11
      · PQ ×9
  - *Attributes & SDT Types*
      · Classification of Attributes (4m)
      · Types of SDT (3m)
      · PYQ ×4
      · PQ ×7
      · PYQ ×15
      · PQ ×16
- **Intermediate Code Gen**
  - *3AC, Quads & Triples*
      · Intermediate Code (6m)
      · DAG Practice Question 1 (5m)
      · DAG Practice Question 2 (5m)
      · DAG Practice Question 3 (6m)
      · DAG Practice Question 4 (3m)
      · DAG Practice Question 5 (4m)
      · 3 Address Code (4m)
      · Representation of 2 Address Code (4m)
      · Fill in Blank (2m)
      · DAG Practice Questions (22m)
      · PYQ ×7
      · PQ ×7
  - *SSA*
      · SSA-SINGLE STATIC ASSINGMENT FORM (2m)
      · SSA - PQ - 1 (13m)
      · SSA PQ - 2 (9m)
      · SSA PQ - 3 (16m)
      · PYQ ×5
      · PQ ×1
  - *Basic Blocks & CFG*
      · Basic Blocks & CFG (25m)
      · Basic Block & CFG PQ - 1 (24m)
      · Basic Block & CFG PQ - 2 (15m)
      · PYQ ×5
      · PQ ×2
      · PYQ ×17
      · PQ ×10
- **Code Optimization**
  - *Blocks, Loops & Methods*
      · Optimization (3m)
      · Constant Folding (1m)
      · Constant Propogation (2m)
      · Strength Reduction (2m)
      · Redundant Code Elimination (1m)
      · Algebraic Simplification (1m)
      · Control Flow Analysis (9m)
      · Loop Jamming (4m)
      · Loop Unrolling (4m)
      · C programming Code Movement (2m)
      · PYQ ×11
      · PQ ×8
  - *Liveness Analysis*
      · Compiler  Liveness Analysis (5m)
      · Liveness Analysis (29m)
      · PYQ ×16
      · PQ ×4
      · PYQ ×27
      · PQ ×12
- **Run Time Environment**
  - *Runtime Memory Organization*
      · Memory Organization (44m)
      · Storage Organization (38m)
      · PYQ ×14
      · PQ ×5
      · PYQ ×14
      · PQ ×5
      · PYQ ×191
      · PQ ×121
      · IOCL - Unit Test - Compiler Design (45m)

### 8. Operating System — 160 vids · 18.0h · 341 PYQs · 230 PQs

- **Introduction to OS**
  - *OS Basics & Goals*
      · Demo: Introduction to Operating System (13m)
      · What is Operating System (10m)
      · Abstract View of a System (3m)
      · Goals and Functions of OS (5m)
      · PYQ ×1
      · PQ ×11
  - *OS Types & Evolution*
      · Batch Operating System (9m)
      · Spooling (7m)
      · Multiprogramming OS (6m)
      · Multitasking OS (6m)
      · multiprocessing operating system (4m)
      · Types of Multiprocessing Operating System (6m)
      · Real Time Operating System (6m)
      · Types of Real Time Operating System (4m)
      · Distributed Operating System (3m)
      · PYQ ×2
      · PQ ×15
  - *OS Structure & Interface*
      · CLI Vs GUI (5m)
      · Structure of operating system (5m)
      · Micro-Kernel Approach (3m)
      · PYQ ×2
      · PQ ×4
  - *System Calls & Dual Mode*
      · System Call (3m)
      · Mode Bit (3m)
      · PYQ ×5
      · PQ ×5
      · PYQ ×10
      · PQ ×35
- **Process Management**
  - *Process Basics & PCB*
      · Basics of a Process (9m)
      · Process Control Block (5m)
      · PYQ ×5
      · PQ ×9
  - *Process State & Lifecycle*
      · Demo: Process Life Cycle (9m)
      · Process State Diagram (6m)
      · Practice Question (3m)
      · Practice Question (2m)
      · Process (os) Practice Question (1m)
      · Practice Question (1m)
      · System Queues (5m)
      · PYQ ×12
      · PQ ×6
  - *Schedulers & Switching*
      · Schedulers (11m)
      · CPU and IO Bound Process (3m)
      · PYQ ×8
      · PQ ×10
      · PYQ ×25
      · PQ ×25
- **CPU Scheduling**
  - *Basics & Criteria*
      · Pre-emptive Vs Non-Pre-emptive Scheduling (5m)
      · Scheduling Criteria (10m)
      · Terminology for CPU Scheduling (9m)
      · PYQ ×11
      · PQ ×6
  - *FCFS Scheduling*
      · FCFS Scheduling (10m)
      · Practice Question (3m)
      · FCFS Advantage Vs Disadvantage (10m)
      · PYQ ×3
      · PQ ×4
  - *SJF & SRTF Scheduling*
      · SJF Scheduling (10m)
      · SRTF Scheduling (7m)
      · SRTF Advantage Vs Disadvantage (8m)
      · SRTF Implementation (7m)
      · PYQ ×15
      · PQ ×8
  - *Priority Scheduling*
      · Non-Pre-emptive Priority Scheduling (12m)
      · Practice Question (8m)
      · Pre-emptive Priority Scheduling (6m)
      · Priority Scheduling Advantage Vs Disadvantage (6m)
      · PYQ ×9
      · PQ ×6
  - *Round Robin Scheduling*
      · Round Robin Scheduling (12m)
      · Round Robin_Practice (7m)
      · Round Robin Advantage Vs Disadvantage (9m)
      · PYQ ×22
      · PQ ×10
  - *LJF & HRRN*
      · LRTF (4m)
      · HRRN (6m)
      · PYQ ×2
  - *Multilevel Queues*
      · Multi Level Queue Scheduling (5m)
      · Multi Level Feedback Queue Scheduling (4m)
      · PYQ ×2
      · PQ ×1
      · PYQ ×64
      · PQ ×35
- **Process Synchronization**
  - *Intro & Critical Section*
      · Race Condition (8m)
      · Critical Section Problem (7m)
      · Criterion to Solve Critical Section Problem (10m)
      · PYQ ×10
      · PQ ×6
  - *Two Process Solutions*
      · Two Process Solution Using Turn Variable (13m)
      · Two Process Solution Using Flag (10m)
      · Peterson Solution using Turn and Flag both (12m)
      · PYQ ×7
      · PQ ×5
  - *Semaphores & Ordering*
      · Understanding Semaphore (8m)
      · N Process Solution using Semaphore (8m)
      · Ordering Among Different Process Using Semaphore (8m)
      · Avoiding Deadlock While Using Multiple Semaphore (6m)
      · PYQ ×15
      · PQ ×4
  - *Classical Problems*
      · Understanding Producer Consumer Problem (8m)
      · Producer Consumer Problem Solution using Semaphores (14m)
      · Reader Writer Problem (6m)
      · Reader Writer Problem Solution using semaphore (12m)
      · Dining Philosopher (12m)
      · PYQ ×10
      · PQ ×3
  - *Types of Semaphores*
      · Types of Semaphores (8m)
      · Gate 2008 (4m)
      · PYQ ×8
      · PQ ×1
  - *Hardware Synchronization*
      · Hardware Solution-Disable Interrupt (4m)
      · Hardware Solution-Test & Set (7m)
      · PYQ ×5
      · PQ ×5
      · PYQ ×55
      · PQ ×24
- **Threads & Process Creation**
  - *Fork System Call*
      · Understanding Fork Command (6m)
      · PYQ ×5
      · PQ ×12
  - *Threading & Models*
      · Understanding Threading (4m)
      · Model of Threading (3m)
      · PYQ ×13
      · PQ ×7
      · PYQ ×18
      · PQ ×19
- **Deadlock**
  - *Basics & Conditions*
      · Basics of Deadlock (10m)
      · System Model Which Every Process Will Follow (4m)
      · Necessary Conditions For Deadlock (12m)
      · Deadlock Handling Methods (5m)
      · PYQ ×4
      · PQ ×4
  - *Deadlock Prevention*
      · Understanding Basics of Prevention (5m)
      · Understanding Hold and Wait (5m)
      · No Pre-Emption (3m)
      · Circular Wait (6m)
      · Problem With Prevention (4m)
      · PYQ ×17
      · PQ ×3
  - *Avoidance & Banker's Algo*
      · Understanding Avoidance (8m)
      · Understanding Bankers Algorithm (11m)
      · Safety Algorithm (2m)
      · Resource Request Algorithm (6m)
      · Resource Allocation Graph (7m)
      · PYQ ×14
      · PQ ×10
  - *Detection & Recovery*
      · Deadlock Detection and Recovery (4m)
      · Methods of Recovery (4m)
      · Ignorance Ostrich Algorithm (2m)
      · PYQ ×3
      · PQ ×2
      · PYQ ×38
      · PQ ×19
- **Memory Management**
  - *Basics & Hierarchy*
      · Requirement of Memory Hierarchy (9m)
      · How Memory hierarchy works (9m)
      · Locality of Reference (7m)
      · Duty of Operating System (4m)
      · PYQ ×4
      · PQ ×4
  - *Contiguous Allocation*
      · Contiguous Allocation Policy and Address Translation (9m)
      · Improvement in Address Translation (5m)
      · Basics of Space Allocation in Contiguous Allocation (11m)
      · First Fit Policy (6m)
      · Best Fit Policy (5m)
      · Worst Fit Policy (4m)
      · Next Fit Policy (3m)
      · External Fragmentation (5m)
      · Internal Fragmentation (3m)
      · Conclusion of External Fragmentation (2m)
      · PYQ ×8
      · PQ ×4
  - *Paging & TLB*
      · Basic of Paging (15m)
      · Understanding Paging Further (8m)
      · Logical to Physical Address Translation in Paging (7m)
      · Page Table in Paging (4m)
      · Advantage and Disadvantage of Paging (9m)
      · Address to Memory Translation (10m)
      · Memory to Address Translation (5m)
      · Numerical background of Paging (8m)
      · Numerical of Page Table (7m)
      · Understanding Translation Look Aside Buffer (10m)
      · Disadvantage of TLB (8m)
      · PYQ ×12
      · PQ ×16
  - *Multilevel Paging*
      · Page Size (10m)
      · Multilevel Paging (8m)
      · PYQ ×3
      · PQ ×5
  - *Segmentation & Hybrid*
      · Segmentation (9m)
      · Practice_Question_Os_physical Addressing (2m)
      · Segmentation with Paging (4m)
      · PYQ ×6
      · PQ ×5
      · PYQ ×33
      · PQ ×34
- **Virtual Memory**
  - *Demand Paging Basics*
      · Basics of Virtual Memory and  Pure Demand Paging (8m)
      · Advantage and Disadvatage of Virtual Memory (7m)
      · Understanding Page Fault and Page Fault Service (7m)
      · Performance of Demand Paging (4m)
      · PYQ ×29
      · PQ ×12
  - *FIFO Page Replacement*
      · Understanding Page Replacement (8m)
      · First In First Out Page Replacement Algorithm (7m)
      · BeLady's Anomaly (8m)
      · PYQ ×8
      · PQ ×4
  - *Optimal Replacement*
      · Optimal Page Replacement Algorithm (7m)
      · 720p_8.2 Gate 2007 (2m)
      · PYQ ×5
      · PQ ×1
  - *LRU Page Replacement*
      · Least Recently Used Page Replacement Algorithm (6m)
      · Implementing LRU (4m)
      · PYQ ×6
      · PQ ×5
  - *Stack & Counting Algos*
      · Counting Based Page Replacement (4m)
  - *Thrashing & Allocation*
      · Frame Allocation Policy Equal Allocation (4m)
      · Proportional Allocation (4m)
      · Working Set Strategy (6m)
      · Thrashing (4m)
      · Local Vs Global Replacement (3m)
      · PYQ ×18
      · PQ ×3
      · PYQ ×66
      · PQ ×25
- **Disc Scheduling**
  - *FCFS & SSTF Scheduling*
      · Basics of Magnetic Disk Architecture (7m)
      · First Come First Serve Scheduling (6m)
      · Shortest Seek Time First Scheduling (12m)
      · PYQ ×11
      · PQ ×2
  - *SCAN & C-SCAN Algos*
      · SCAN Scheduling (7m)
      · C-Scan Scheduling (4m)
      · Practice Question (4m)
      · Gate 2015 (4m)
      · PQ ×1
  - *LOOK & C-LOOK Algos*
      · Look Scheduling (3m)
      · C-Look Scheduling (2m)
      · PYQ ×4
      · PYQ ×15
      · PQ ×3
- **File Management**
  - *File Allocation Methods*
      · Basics of File Allocation Methods (3m)
      · Contiguous File Allocation (9m)
      · Linked File Allocation (7m)
      · Index File Allocation (11m)
      · PYQ ×10
      · PQ ×4
  - *Free Space Management*
      · Free Space Management (2m)
      · Bit Vector (3m)
      · Linked List File Management System (2m)
      · PYQ ×2
      · PQ ×2
  - *Directories & Structure*
      · File Access Methods and their types- (15m)
      · Directory and Disk Structure (8m)
      · Directory Structure (9m)
      · Acyclic Graph Directory (9m)
      · General Graph Directory (3m)
      · File System Mounting (5m)
      · File sharing (3m)
      · File System Structure and Implementation- (7m)
      · PYQ ×5
      · PQ ×5
      · PYQ ×17
      · PQ ×11
      · PYQ ×341
      · PQ ×230
      · IOCL - Unit Test - Operating Systems (45m)

### 9. DataBase Management System/DBMS — 181 vids · 18.1h · 310 PYQs · 363 PQs

- **Basics of DBMS**
  - *DBMS Fundamentals*
      · Demo: Blue Print Of DBMS (7m)
      · Demo: What is Data and Information (6m)
      · Demo: What is Data Base Management System (4m)
      · Problem With File System (7m)
      · Views Of DataBase (4m)
      · Instance Vs Schema (2m)
      · PYQ ×3
      · PQ ×22
  - *Types & DBA Functions*
      · OLAP Vs OLTP (5m)
      · Types of Databases (11m)
      · Who is DataBase Administrator (1m)
      · PYQ ×1
      · PQ ×9
      · PYQ ×4
      · PQ ×31
- **ER Diagram**
  - *ER Modeling Fundamentals*
      · Introduction To ER Diagram (6m)
      · Understanding What is Entity (6m)
      · What Is Entity Set (4m)
      · Basics Of Attributes (3m)
      · Single Vs Multivalued Attributes (6m)
      · Simple Vs Composite Attributes (5m)
      · What Is Relationship (5m)
      · Degree Of a Relationship (5m)
      · PYQ ×5
      · PQ ×15
  - *Cardinalities, Participation & Entity Strength*
      · Cardinality Ratios and Mapping (7m)
      · Participation Constraints (8m)
      · Strong Vs Weak Entity Set (9m)
      · PYQ ×9
      · PQ ×12
  - *Conversion of ER Diagram into Relational Model*
      · Conversion ER Diagram to Relational Model (9m)
      · Fan Trap (4m)
      · Chasm Trap (5m)
      · PYQ ×7
      · PQ ×7
      · PYQ ×21
      · PQ ×34
- **Relational Model & Functional Dependencies**
  - *Basics of Relational Model & Anomalies*
      · Basics of Relational Model (5m)
      · Update Anomalies In Relational Model (6m)
      · Understanding Redundancy In Detail (6m)
      · PYQ ×1
      · PQ ×16
  - *Functional Dependencies & Axioms*
      · What Is Functional Dependency (5m)
      · Understanding Functional Dependency Further (6m)
      · What Is Trivial Functional Dependency (4m)
      · Practice Questions Functional Dependency (2m)
      · Understanding Armstrong's Axioms (9m)
      · PYQ ×10
      · PQ ×3
  - *Attribute Closure & Equivalence of Sets*
      · Closure Set of Attributes (6m)
      · Practice Questions Functional Dependency (7m)
      · Comparing Two Set Of Functional Dependencies (7m)
      · Practice Questions (3m)
      · Practice Questions on Functional Dependencies (1m)
      · Practice Questions Functional Dependency (3m)
      · PYQ ×3
      · PQ ×3
  - *Minimal Cover (Canonical Cover)*
      · Minimal Cover Of Functional Dependency (11m)
      · PYQ ×1
      · PQ ×1
      · PYQ ×15
      · PQ ×23
- **Keys & Integrity Constraints**
  - *Super Key, Candidate Key & Primary Key*
      · What Is Key (3m)
      · Super Key (5m)
      · Candidate Key (5m)
      · Primary Key (3m)
      · DBMS PRACTICE QUESTIONS (5m)
      · Chap-2_4_2022 (3m)
      · PYQ ×14
      · PQ ×16
  - *Foreign Key & Referential Integrity*
      · Foreign Key (4m)
      · PRACTICE QUESTION (7m)
      · PYQ ×9
      · PQ ×16
  - *Composite & Alternate Keys*
      · Composite Key (2m)
      · PYQ ×1
      · PQ ×3
      · PYQ ×24
      · PQ ×35
- **Normalization (1NF - BCNF)**
  - *Introduction to Normalization & 1NF*
      · Demo: What is Normalisation (5m)
      · First Normal Form (5m)
      · PQ ×7
  - *Second Normal Form (2NF)*
      · Demo: Second Normal Form (8m)
      · PYQ ×5
      · PQ ×6
  - *Third Normal Form (3NF)*
      · Gate 2018 (4m)
      · Demo: Third Normal Form (6m)
      · PYQ ×4
      · PQ ×6
  - *Boyce-Codd Normal Form (BCNF)*
      · BCNF (4m)
      · Practice Questions-1 (6m)
      · Practice Questions-2 (7m)
      · Practice Questions-3 (3m)
      · Practice Questions-4 (3m)
      · PYQ ×21
      · PQ ×17
      · PYQ ×30
      · PQ ×36
- **Decomposition Properties & 4NF**
  - *Multivalued Dependency (MVD) & 4NF*
      · Multivaluated and Functional Dependency Relationship (2m)
      · All About Multivaluated Dependency (8m)
      · Fourth Normal Form (4m)
      · PYQ ×1
      · PQ ×3
  - *Lossless Join Decomposition*
      · Lossy-Lossless Decomposition Using FD (7m)
      · Check for Lossless Decomposition using FD (5m)
      · PYQ ×4
      · PQ ×2
  - *Dependency Preserving Decomposition*
      · Dependency Preserving Decomposition (4m)
      · PYQ ×4
      · PQ ×8
      · PYQ ×9
      · PQ ×13
- **File Organization & Indexing**
  - *Basics & Types of Indexing*
      · BackGround of Indexing (5m)
      · What is Indexing (5m)
      · Practice Question -  Primary Indexing (7m)
      · Practice Question - Primary Indexing Cont... (8m)
      · Important Terminology of Indexing (6m)
      · Primary Indexing (3m)
      · Clustered Indexing (9m)
      · Practice Question - Clustered Indexing (2m)
      · Secondary Indexing (7m)
      · Practice question on secondary indexing (8m)
      · Multilevel indexing (7m)
      · PYQ ×17
      · PQ ×11
  - *B-Trees & B+ Trees (Structure & Insertion)*
      · Insertion in B-Tree (7m)
      · Practice question on B Tree Insertion (8m)
      · Reason for B+ Tree (5m)
      · Structure of Nodes in B Tree and B+ Tree (7m)
      · Insertion in B+ Tree Part-1 (8m)
      · Insertion in B+ Tree Part-2 (5m)
      · PYQ ×21
      · PQ ×16
  - *Deletion in B-Trees & B+ Trees*
      · Deletion From B Tree (9m)
      · Practice question on B Tree Deletion (10m)
      · Deletion From B+ Tree (5m)
      · PYQ ×2
      · PYQ ×40
      · PQ ×27
- **Relational Algebra**
  - *Introduction to Query Languages*
      · What is Query Language (6m)
      · Basics of Relational Algebra (5m)
      · PYQ ×1
      · PQ ×2
  - *Unary Operators (Selection & Projection)*
      · Project Operator (4m)
      · Select Operator (4m)
      · PYQ ×7
      · PQ ×5
  - *Set Operations & Cartesian Product*
      · Set Operators (5m)
      · Cartesian Product In RA (6m)
      · Problem With Cartesian Product (6m)
      · PYQ ×6
      · PQ ×5
  - *Join Operations (Inner & Outer)*
      · Natural Join Operator (4m)
      · Thetha Join-Conditional Join (4m)
      · Outer Join (3m)
      · PYQ ×26
      · PQ ×7
  - *Rename Operation*
      · Rename Operation (6m)
      · PYQ ×1
  - *Division Operator*
      · Division Operator (6m)
      · Implementing Division Operator Using Basic Operators (3m)
      · PYQ ×4
      · PQ ×1
      · PYQ ×45
      · PQ ×20
- **SQL**
  - *Introduction, Components & Structure*
      · Introduction To SQL (7m)
      · Components Of SQL (4m)
      · Basic Structure Of SQL (9m)
      · 720p_2.3 Net 1999 (2m)
      · PYQ ×3
      · PQ ×12
  - *Select, Where, Distinct*
      · Select Clause (5m)
      · Where Clause (6m)
      · Demo: Distinct (7m)
      · PYQ ×8
      · PQ ×11
  - *Datatypes, Operators & Null*
      · SQL Data Types (17m)
      · SQL Operators (5m)
      · Null in SQL (3m)
      · PYQ ×2
      · PQ ×5
  - *DDL, DML, DCL, TCL & Desc*
      · DDL (10m)
      · DML (8m)
      · DCL & TCL (6m)
      · Desc & Show Tables (3m)
      · PYQ ×6
      · PQ ×26
  - *Order By & Rename Operation (Alias)*
      · Order by clause (4m)
      · Rename Operations (8m)
      · PQ ×5
  - *Library Functions (Math, Aggregate, String, Date)*
      · Aggregate Functions (5m)
      · String Operations in SQL (10m)
      · String Function (9m)
      · Numeric & Math Functions (4m)
      · Date & Time Functions (3m)
      · PYQ ×5
      · PQ ×9
  - *Set Operations & Cartesian Product*
      · Set Operations In SQL (4m)
      · Cartesian Product In SQL Part-1 (6m)
      · Cartesian Product In SQL Part-2 (6m)
      · PYQ ×3
      · PQ ×2
  - *Join Operations (Inner & Outer)*
      · Natural Join (5m)
      · Join With Using (2m)
      · Different Versions Of Natual Join (4m)
      · PYQ ×9
      · PQ ×7
  - *Group By Clause*
      · Group by Clause (5m)
      · SQL query (8m)
      · Group By Contd... (19m)
      · PYQ ×4
      · PQ ×7
  - *Nested & Correlated Subqueries*
      · Introduction - Part 1 (5m)
      · Introduction - Part 2 (6m)
      · Correlated Introduction (8m)
      · Practice Question - Corelated Subquery (7m)
      · PYQ ×22
      · PQ ×9
      · PYQ ×62
      · PQ ×93
- **Relational Calculus**
  - *Tuple Relational Calculus (TRC)*
      · Introduction to Tuple  Relational Calculus (6m)
      · Tuple Relational Calculus Practice (9m)
      · PYQ ×8
      · PQ ×6
  - *Domain Relational Calculus (DRC)*
      · Introduction to Domain Relational Calculus (4m)
      · Domain Relational Calculus Practice Questions (4m)
      · PYQ ×1
  - *Safety of Expressions & Power*
      · Power of TRC & Safe TRC (3m)
      · Power of DRC & safe DRC (2m)
      · PYQ ×4
      · PQ ×1
      · PYQ ×13
      · PQ ×7
- **Transaction Management**
  - *Introduction & ACID Properties*
      · What is Transaction (6m)
      · Fundamental Operations On DBMS (2m)
      · ACID Properties of Transaction (4m)
      · Isolation Property (4m)
      · Durability Property (3m)
      · Consistency Property (3m)
      · PYQ ×7
      · PQ ×11
  - *Transaction States*
      · Transaction States (7m)
      · PYQ ×1
      · PQ ×2
  - *Concurrency Problems*
      · Problem With Concurrent Execution (5m)
      · Lost Update Problem (5m)
      · Dirty Read Problem (4m)
      · Unrepeatable Read Problem (5m)
      · PYQ ×1
      · PQ ×5
  - *Schedules & Conflict Serializability*
      · What is Schedule (4m)
      · Serial Schedule (5m)
      · Non-Serial Schedule (5m)
      · Conclusion Of Schedule (4m)
      · Conflict Serializable (9m)
      · Conflict Equivalent Schedule (4m)
      · Procedure for determining conflict serializability of a schedule (14m)
      · PYQ ×15
      · PQ ×7
  - *View Serializability*
      · view serializability Part-1 (7m)
      · view serializability Part-2 (8m)
      · Practice Questions on View Serializability (6m)
      · PQ ×2
  - *Recoverability, Cascadeless & Strict Schedules*
      · Recoverable Schedule (5m)
      · Cascadeless Schedule (4m)
      · Strict Schedule (3m)
      · Practice Questions on Recoverability, Cascadeless & Strict Schedules (4m)
      · Practice Question (8m)
      · PYQ ×6
      · PQ ×1
      · PYQ ×30
      · PQ ×28
- **Concurrency Control**
  - *Introduction to Concurrency Control*
      · Idea of Concurrency control (8m)
      · PYQ ×1
      · PQ ×2
  - *Timestamp Ordering Protocols*
      · Time stamp protocol part-1 (7m)
      · Time stamp protocol part-2 (4m)
      · Time stamp protocol part-3 (8m)
      · Properties of the stamping protocol (4m)
      · Thomas write Rule (6m)
      · Practice Questions (3m)
      · PYQ ×3
      · PQ ×6
  - *Lock-Based Protocols & Basic 2PL*
      · Locked based protocols (7m)
      · PYQ ×8
      · PQ ×2
  - *Variations of 2PL (Strict, Rigorous, Conservative)*
      · Basic 2PL (8m)
      · Conservative 2PL (7m)
      · Rigorous 2PL (5m)
      · Strict 2PL (3m)
      · PYQ ×3
      · PYQ ×15
      · PQ ×10
- **Database Recovery**
  - *Failure Types & Recovery Fundamentals*
      · Storage Structure (20m)
      · Recovery and Atomicity (7m)
      · Database Recovery Techniques (DRT) (9m)
      · Database Recovery & Approaches (11m)
      · Failure Classifications (5m)
      · PQ ×2
  - *Log-Based Recovery Techniques*
      · Log Based Recovery (8m)
      · Write Ahead Logging (12m)
      · PYQ ×2
      · PQ ×4
      · PYQ ×2
      · PQ ×6
      · PYQ ×310
      · PQ ×363
      · IOCL - Unit Test - Database Management Systems (45m)

### 10. Computer Networks — 204 vids · 22.1h · 283 PYQs · 310 PQs

- **Introduction to CN**
  - *Basics & Criteria*
      · Goals and Applications (12m)
      · Five components of Data Communication (5m)
      · Effectiveness of DataCommunication (6m)
      · PYQ ×1
      · PQ ×7
  - *Modes & Connections*
      · Transmission Mode in Data Communication (7m)
      · Type of Connection Point-to-Point and Multi-Point (3m)
      · PQ ×7
  - *Network Topologies*
      · Mesh Topology (9m)
      · Star Topology (5m)
      · Bus Topology (4m)
      · Ring Topology (4m)
      · Tree (2m)
      · Hybrid (2m)
      · PYQ ×3
      · PQ ×20
  - *Switching Techniques*
      · Demo: Circuit Switching (13m)
      · Packet Switching (19m)
      · PYQ ×1
      · PQ ×5
  - *Transmission Media*
      · Transmission Medium (5m)
      · Wireless (6m)
      · PYQ ×1
      · PQ ×6
  - *OSI Model & Layers*
      · Basics of Open System Interconnection OSI model (10m)
      · Working of Open System Interconnection OSI model (7m)
      · Basics of Physical Layer with functionality and duties (4m)
      · Data Link Layer duties, services and functionality (7m)
      · Network Layer duties, services and functionality (4m)
      · Transport Layer duties, services and functionality (6m)
      · Session Presentation Application Layer duties, services (5m)
      · PYQ ×9
      · PQ ×17
      · PYQ ×15
      · PQ ×62
- **DLL: Access Control**
  - *DLL Overview & MAC*
      · Basics Of Multiple Access Protocol (8m)
      · Fundamentals of Random Access Protocols (5m)
      · PQ ×3
  - *ALOHA Protocols*
      · Pure Aloha Part - 1 (10m)
      · Pure Aloha Part-2 (19m)
      · Practice Question (4m)
      · Practice Question (3m)
      · Practice Question (Throughput) (6m)
      · Slotted Aloha (4m)
      · PYQ ×5
      · PQ ×5
  - *CSMA Variants*
      · CSMA (10m)
      · Persistence Methods in CSMA (11m)
  - *CSMA/CD*
      · CSMA-CD Part - 1 (11m)
      · CSMA-CD Part - 2 (5m)
      · PYQ ×7
      · PQ ×6
  - *CSMA/CA (Wireless)*
      · CSMA-CA Part-1 (4m)
      · CSMA-CA Part-2 (10m)
      · CSMA-CA Part-3 (4m)
      · PYQ ×3
      · PQ ×2
  - *Controlled Access*
      · Reservation - Controlled Access (7m)
      · Polling - Controlled Access Protocol (6m)
      · Token Passing - Controlled Access Protocol (4m)
      · PYQ ×6
  - *Channelization*
      · FDMA - Channelization (4m)
      · TDMA - Channelization (2m)
      · CDMA - Channelization (4m)
      · PYQ ×6
      · PYQ ×27
      · PQ ×16
- **DLL: Flow Control**
  - *Basics & Delay Analysis*
      · Basics of Flow Control in Data Link Layer (7m)
      · Simplest Protocol (4m)
      · Stop and Wait Protocol (3m)
  - *Stop-and-Wait ARQ*
      · Stop and Wait Protocol - ARQ (13m)
      · Performance of Stop and Wait Protocol - ARQ (11m)
      · Efficiency of Stop and Wait Protocol - ARQ (6m)
      · PYQ ×7
      · PQ ×4
  - *Go-Back-N Protocol*
      · Go Back N - ARQ (13m)
      · Performance of Go Back N - ARQ (4m)
      · Gate 2008_ (11m)
      · PYQ ×9
      · PQ ×2
  - *Selective Repeat ARQ*
      · Selective Repeat - ARQ (5m)
      · PYQ ×11
      · PQ ×2
      · PYQ ×27
      · PQ ×8
- **DLL: Error Control**
  - *Basics & Hamming Dist*
      · Types of Error - Single Bit Error - Burst Error (6m)
      · Idea of Redundancy for Error Detection (8m)
      · Idea of Block Coding for Error Detection (11m)
      · Basics of Hamming Distance (8m)
      · Minimum Hamming Distance for Error Detection (7m)
      · Minimum Hamming Distance for Error Detection and Correction (7m)
      · PYQ ×8
      · PQ ×7
  - *Linear Block Codes*
      · Basics of One-Dimesional Parity Check (6m)
      · Two-Dimesional Parity Check (5m)
      · Hamming Codes with error detection and Correction Part-1 (12m)
      · Hamming Codes with error detection and Correction Part-2 (5m)
      · PYQ ×3
      · PQ ×2
  - *Checksum & CRC*
      · CheckSum Part-1 (6m)
      · CheckSum Part-2 (7m)
      · Cyclic Redundancy Check Part-1 (8m)
      · Cyclic Redundancy Check Part-2 (4m)
      · Cyclic Redundancy Check Using Polynomials Part-1 (6m)
      · Cyclic Redundancy Check Using Polynomials Part-2 (6m)
      · PYQ ×9
      · PQ ×3
      · PYQ ×20
      · PQ ×12
- **DLL: Framing**
  - *Intro & Byte Stuffing*
      · Basics of Framing (5m)
      · Character Oriented Framing (4m)
      · PYQ ×3
      · PQ ×1
  - *Bit Stuffing Algo*
      · Byte Stuffing Strategy (4m)
      · Bit-Oriented Approach (3m)
      · PYQ ×7
      · PQ ×3
      · PYQ ×10
      · PQ ×4
- **Data Link Layer - Ethernet**
  - *Overview and Evolution of Ethernet – IEEE 802.3*
      · Basics of Ethernet (5m)
      · PYQ ×6
      · PQ ×6
  - *Ethernet Frame Format – Preamble, SFD*
      · Preamble and SFD (3m)
      · Destination and Source Address (2m)
      · Length Field (4m)
      · CRC Field in Ethernet (1m)
      · PYQ ×7
      · PQ ×3
  - *Manchester Encoding – G.E. Thomas, IEEE, and Differential Manchester Schemes*
      · Manchester Coding (4m)
      · PYQ ×4
      · PYQ ×17
      · PQ ×9
- **Net Layer: IPv4 & Proto**
  - *Net Layer & IPv4 Basics*
      · Basics Of Network Layer Part - 1 (7m)
      · Basics Of Network Layer Part - 2 (18m)
      · Basics of IPv4 and Datagram Structure (7m)
      · Version Field in IPv4 (3m)
      · Header Length in IPv4 (5m)
      · Service Field in IPv4 (7m)
      · Total Length Field in IPv4 (5m)
      · PYQ ×3
      · PQ ×18
  - *Fragmentation & MTU*
      · Identification Field in IPv4 (3m)
      · Example of Fragmentation (5m)
      · Basics of Fragmentation (6m)
      · Flag Field in IPv4 (5m)
      · Fragmentation Field in IPv4 (8m)
      · PYQ ×11
      · PQ ×8
  - *TTL, Protocol & Checksum*
      · Time-To-Live Field in IPv4 (5m)
      · Protocol Field in IPv4 (2m)
      · Header CheckSum Field in IPv4 (3m)
      · PYQ ×4
      · PQ ×2
  - *IP Options & Padding*
      · Source and Destination Address in IPv4 (2m)
      · Options Field in IPv4 (7m)
      · PYQ ×1
  - *Net Layer Protocols*
      · ARP-Address Resolution Protocol (5m)
      · RARP - Reverse Address Resolution Protocol (3m)
      · Basics Of ICMP (4m)
      · ICMP Error Reporting (10m)
      · ICMP - Query Messages (9m)
      · IGMP - Internet Group Message Protocol (4m)
      · PYQ ×5
      · PQ ×12
      · PYQ ×24
      · PQ ×40
- **Net Layer: IP Addressing**
  - *Classful Addr & Casting*
      · Basics of IP Addressing (9m)
      · Notations Of IP Address (4m)
      · Fundamental Of IP Addressing (8m)
      · Class A (9m)
      · Class B (6m)
      · Class C (6m)
      · Class D & E (6m)
      · Types of Casting (8m)
      · PYQ ×9
      · PQ ×22
  - *Subnetting & FLSM Design*
      · Basics of SubNetting (11m)
      · SubNetting Example (5m)
      · Understanding SubNet Mask (6m)
      · Variable Length SubNetting (6m)
      · PYQ ×15
      · PQ ×15
  - *CIDR & VLSM*
      · Address Depletion in ClassFull Addressing (6m)
      · ClassLess Interdomain Routing - CIDR With Example (4m)
      · Rules of Creating CIDR Block (4m)
      · SubNetting In CIDR (4m)
      · CIDR block representation practice question (4m)
      · CIDR Practice Question_ (3m)
      · CIDR Practice Question_ (3m)
      · CIDR Practice Question_ (5m)
      · CIDR Practice Question_ (4m)
      · CIDR Practice Question (8m)
      · Designing subnets for CIDR (5m)
      · PYQ ×11
      · PQ ×6
  - *Supernetting & Spl IPs*
      · Super Netting in ClassFul Addressing (6m)
      · Special Address 127.0.0.1 (2m)
      · Supernetting CIDR (6m)
      · CIDR  supernetting (5m)
      · PYQ ×3
      · PQ ×7
      · PYQ ×38
      · PQ ×50
- **Net Layer:Routing Protocol**
  - *Routing Basics & Flooding*
      · Basics of Routing and Flooding (6m)
      · Static and Dynamic Routing (4m)
      · Basics of Unicast Routing Protocol (6m)
      · Intra-Domain Vs Inter-Domain Routing (4m)
      · PYQ ×8
      · PQ ×3
  - *DVR, RIP & Split Horizon*
      · Basics of Distance Vector Routing (9m)
      · Periodic Vs Triggered Update (4m)
      · Two-Node Loop Instability (6m)
      · Split Horizon (2m)
      · Routing Information Protocol (RIP) (8m)
      · PYQ ×10
      · PQ ×5
  - *LSR, OSPF & Comparison*
      · Link State Routing Part-1 (5m)
      · Link State Routing Part-2 (8m)
      · Open Shortest Path First (OSPF) (6m)
      · PYQ ×16
      · PQ ×3
      · PYQ ×34
      · PQ ×11
- **Transport Layer Services**
  - *Services, Ports & UDP/TCP*
      · Basics of Transport Layer and Duties (9m)
      · Understanding Port Numbers for Service Addressing (7m)
      · Socket Address in Transport Layer Encapsulation Decapsulation (4m)
      · Basics of Transmission Control Protocol (3m)
      · PYQ ×7
      · PQ ×9
  - *TCP Header & Fields*
      · TCP Header-Source-Destination Port Address (4m)
      · TCP Header-Sequence Number-Acknowledgement Number (13m)
      · Idea of Wrap-Around Time (10m)
      · TCP Header-Header Length Field (3m)
      · TCP Header-Check Sum Field (4m)
      · TCP Header-Window Size Field (8m)
      · TCP Header-Urgent Pointer Field (4m)
      · TCP Header-Control Flags (5m)
      · Option Field in TCP Header (4m)
      · PYQ ×8
      · PQ ×3
  - *Conn. Mgmt & Reliability*
      · Three-way Handshaking for TCP Connection Establishment (8m)
      · TCP Connection Termination Three-Way Handshake (4m)
      · SYN Flooding Attack (Denial of Service) (3m)
      · TCP Retransmission (4m)
      · PYQ ×5
      · PQ ×6
  - *TCP State Transition Diag*
      · RFC 793 (10m)
      · PYQ ×4
      · PYQ ×24
      · PQ ×18
- **TL: Congestion & UDP**
  - *Congestion Control Policy*
      · Basics of Congestion Control (4m)
      · Basics of Windows in TCP (6m)
      · Congestion Window (3m)
      · Slow Start Phase (Exponential Increase) (6m)
      · Congestion Avoidance Phase (2m)
      · Congestion Detection Phase Phase-1 (4m)
      · Congestion Detection Phase Phase-2 (4m)
      · PYQ ×9
      · PQ ×4
  - *Timers, RTT & SWS*
      · Different timers used in transport layer (7m)
      · Basics of time out timer (4m)
      · Basic Algo for time out Timer (7m)
      · Jacobson Algo for time out timer (8m)
      · Karn's Algorithm for Time out Timer (3m)
      · Silly Window Syndrome & Nagle's Algo (6m)
      · PYQ ×2
      · PQ ×2
  - *UNIX Socket Programming*
      · UNIX Socket API (2m)
      · PYQ ×4
  - *UDP Protocol & Header*
      · User Datagram Protocol (4m)
      · PYQ ×5
      · PQ ×6
      · PYQ ×20
      · PQ ×12
- **Application Layer**
  - *Email: SMTP, POP & IMAP*
      · Basics of Application Layer (7m)
      · Email (7m)
      · Electronic Mail Part-1 (9m)
      · Electronic Mail Part-2 (6m)
      · Electronic Mail Part-3 (5m)
      · PYQ ×6
      · PQ ×11
  - *WWW Basics & Cookies*
      · Understanding WWW Architecture (6m)
      · Client-Server Architecture and Uniform Resource Locator (5m)
      · Understanding Cookies (7m)
      · PYQ ×1
      · PQ ×8
  - *HTTP Protocol*
      · Understanding HTTP (4m)
      · Proxy Server and Non-Persistent Vs Persistent Connections (7m)
      · HTTPS (3m)
      · PYQ ×3
      · PQ ×10
  - *FTP, DNS & Telnet*
      · Understanding File Transfer Protocol (7m)
      · Domain Name System (5m)
      · Hierarchical Name Space (4m)
      · Telnet (2m)
      · DHCP (5m)
      · PYQ ×10
      · PQ ×13
  - *PPP, TCP/IP & VoIP Protocols*
      · PPP (3m)
      · TCP / IP (3m)
      · VoIP (2m)
      · Hierarchical Name Space (4m)
      · Understanding File Transfer Protocol (7m)
      · Domain Name System (5m)
      · Telnet (2m)
      · DHCP (5m)
      · PYQ ×4
      · PQ ×6
      · PYQ ×24
      · PQ ×48
- **Hardware Basics**
  - *Repeater, Hub, Bridge & Switch*
      · Demo: Repeater (7m)
      · Hub (6m)
      · Bridge (14m)
      · Switch (13m)
      · PYQ ×2
      · PQ ×7
  - *Router & Gateway*
      · Router (18m)
      · Gateway (15m)
      · PYQ ×1
      · PQ ×13
      · PYQ ×3
      · PQ ×20
      · PYQ ×283
      · PQ ×310
      · IOCL - Unit Test - Computer Networks (45m)
      · IOCL - Unit Test - Computer Networks (45m)

### 11. CS/IT Sectional Mock Tests — 0 vids · 7.5h · 0 PYQs · 0 PQs

      · IOCL - Mock Test - CS/IT Sectional — Test 1 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 2 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 3 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 4 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 5 (1.5h)

### 12. Complete Paper Full Mock Test — 0 vids · 17.5h · 0 PYQs · 0 PQs

      · IOCL - Complete Paper Mock Tests — Test 1 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 2 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 3 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 4 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 5 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 6 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 7 (2.5h)

---

## IOCL Paper-1 (Aptitude)

`IOCL-ENGINEERS-OFFICER-GRADE-A-PAPER-1` · **297 videos / 94.6h** · 708 PYQs · 861 PQs · 269 subtopics · 15 tests · 291 notes

### 0. Quantitative Aptitude — 149 vids · 42.8h · 276 PYQs · 196 PQs

- **Speed Mathematics and Basic Mathematics**
  - *Speed Math*
      · Find Square Root of Any Number in Just 5 Seconds (9m)
      · Multiply 2-Digit Numbers in Just 5 Seconds (4m)
      · Multiply 3-Digit Numbers in Just 5 Seconds (5m)
      · Find Square Root of Imperfect Numbers in Just 10 Seconds (5m)
      · Tricks to Calculate Number of Triangles in Any Figure (11m)
      · Tricks to Calculate Number of Triangles in Any Figure (2) (12m)
      · Tricks to Calculate Number of Triangles in Any Figure (3) (8m)
      · Tricks to Find No. of Triangles & Squares in Any Figure (11m)
      · Trick To Check if a Number is Divisible by 7 or Not (6m)
      · Short Trick to find angle between hands of a clock (9m)
      · More Short Tricks for Fast Calculation (1.0h)
- **Percentage**
  - *Basic Concepts, Terminologies & Properties*
      · What is Covered in this Course (12m)
      · Pre-requisite required to understand Percentages (14m)
      · Complete Percentage in One Shot (1.1h)
      · PQ ×2
  - *Conversion Between Fractions (Ratio) & Percentages*
      · Demo: Basics of Percentages, Percentage - Fraction Conversions (13m)
      · Important Property, Trick to find 10 & 1 percent of any number (10m)
      · Short Tricks to Remember Ratio to Percentage Table Part 1 (9m)
      · Short Tricks to Remember Ratio to Percentage Table Part 2 (11m)
      · Short Tricks to Remember Ratio to Percentage Table Part 3 (9m)
      · Short Tricks to Remember Ratio to Percentage Table Part 4 (8m)
      · Practice Problems on Ratio to Percentage Conversion (10m)
      · Practice Problems on Percentage to Ratio Conversion (8m)
      · Question on Ratio to Percentage Conversion (5m)
      · PYQ ×1
      · PQ ×3
  - *Finding Percentage*
      · Few Important Points for Percentages (7m)
      · The Three Confusing Questions of Percentages (9m)
      · PYQ ×3
      · PQ ×3
  - *Percentage Relationship Questions*
      · PYQ ×4
      · PQ ×2
  - *Successive Percentage Change*
      · PYQ ×2
      · PQ ×4
  - *Percentage Difference & Reverse Comparison*
      · PYQ ×4
      · PQ ×4
  - *Expenditure, Consumption, & Price Relationship*
      · PYQ ×3
      · PQ ×3
  - *Percentage in Population / Growth / Successive Years*
      · PYQ ×3
      · PQ ×5
  - *Multiple Topics*
      · Important Practice Questions on Percentages (Part 1) (53m)
      · Important Practice Questions on Percentages (Part 2) (46m)
      · PYQ ×1
      · PYQ ×21
      · PQ ×26
- **Ratio and Proportion (Ratios)**
  - *Basic Concepts & Properties of Ratio*
      · Demo: What is Ratio & Proportion, Definition & Examples (12m)
      · Demo: Properties of Ratios, Properties of Proportions (14m)
      · PYQ ×1
      · PQ ×8
  - *Types of Ratio*
      · Demo: Types of Ratios with Examples (15m)
      · Short Tricks to Combine Two or More Ratios (16m)
  - *Direct, Inverse & Joint Variation*
      · What is Variation, What is Direct & Indirect Variation (13m)
      · PYQ ×1
  - *Basic Concepts & Properties of Proportion*
      · Invertendo, Alternendo, Componendo & Dividendo Property (15m)
      · Addendo Property & Equivalent Ratio Property (16m)
      · PQ ×4
  - *Division of Quantity in a Given Ratio*
      · Short Trick to Divide a Given Number X in ratio of M N (16m)
      · Short Trick to bring given set of numbers in proportion (14m)
      · Short Trick to convert given ratio into required ratio (8m)
      · Finding ratio of 2 numbers from their sum & difference (3m)
      · PYQ ×5
      · PQ ×3
  - *Mean / Extreme / Continued Proportion*
      · PQ ×2
  - *Successive & Combined Ratio Problems*
      · Short Trick to Find A   C when A   B & B   C is given (6m)
      · Short Trick to Find A   B   C given some mA = nB = pC (5m)
      · Short Trick to find (mX + nY)   (pX + qY) given x   y (10m)
      · Short Trick to Find bigger ratio out of given 2 ratios (9m)
      · PYQ ×4
      · PQ ×5
  - *Multiple Topics*
      · Quick Revision and Practice Questions (1.1h)
      · PYQ ×11
      · PQ ×22
- **Powers and Exponents (Surds and Indices)**
  - *Basic Concepts & Laws of Exponents (Indices)*
      · PYQ ×1
  - *Negative & Fractional Exponents*
      · PYQ ×1
  - *Simplification Using Laws of Exponents*
      · PYQ ×3
      · PQ ×3
  - *Laws of Surds & Simplification*
      · Surds and Indices Part 1 (17m)
      · Surds and Indices Part 2 (13m)
      · PYQ ×5
      · PQ ×1
  - *Rationalization of Surds*
      · Surds and Indices Part 3 (10m)
      · PYQ ×2
      · PQ ×2
  - *Comparing & Simplifying Complex Powers*
      · Surds and Indices Part 4 (3m)
  - *Multiple Topics*
      · UPDATED_surds and indices (1.1h)
      · PYQ ×12
      · PQ ×6
- **Logarithm**
  - *Basic Concepts and Terminologies*
      · Demo: Basic Concepts of Logarithms, Types of log (19m)
      · PQ ×1
  - *Laws or Properties or Rules of Logarithms*
      · Demo: Properties of Logarithms - Part 1 (16m)
      · Demo: Properties of Logarithms - Part 2 (21m)
      · Properties of Logarithms - Part 3 (13m)
      · Some Important Log values to remember (14m)
      · PYQ ×1
  - *Conditions for Existence of Logarithm*
  - *Solving Logarithmic Expressions and Equations*
      · Set 1 - Important Questions on Logarithms (12m)
      · Set 2 - Important Questions on Logarithms (4m)
      · Set 3 - Important Questions on Logarithms (6m)
      · Set 4 - Important Questions on Logarithms (9m)
      · Set 5 - Important Questions on Logarithms (14m)
      · Set 6- Important Questions on Logarithms (11m)
      · 12 Logarithm (Quick Revision & Practice Problems) (1.4h)
      · GATE 2018 - Computer Science - Logarithm - 2 Marks (4m)
      · PYQ ×7
      · PQ ×1
  - *Antilog & Application of Logarithmic Concepts*
  - *Multiple Topics*
      · PYQ ×8
      · PQ ×2
- **Sequence and Series (Series)**
  - *Basic Concepts & Terminologies*
      · Demo: Basic Concepts of Sequence & Series (13m)
      · Demo: Important Formulas of Sequence & Series (13m)
      · PYQ ×2
  - *Arithmetic Progression (AP)*
      · Demo: Short Tricks to Quickly Solve Problems of Sequence Series (10m)
      · Basics Questions on Sequence & Series (6m)
      · PYQ ×8
      · PQ ×2
  - *Geometric Progression (GP)*
      · PYQ ×7
      · PQ ×2
  - *Harmonic Progression (HP)*
      · PYQ ×1
  - *Arithmetic Mean & Geometric Mean (AM-GM)*
      · Concept of Arithmetic Mean & Geometric Mean (7m)
      · PQ ×1
  - *Multiple Topics*
      · Some Important Questions on Sequence & Series (11m)
      · Effect of Addition, Subtraction, Multiplication, Division (8m)
      · Quick Revision and Practice Questions (1.0h)
      · PYQ ×1
      · PYQ ×19
      · PQ ×5
- **Permutation and Combination**
  - *Basic Concepts & Counting Principles*
      · Demo: Permutation & Combination (Quick Revision & Practice Questions) (1.2h)
      · PYQ ×4
      · PQ ×1
  - *Permutations (with & without Repetition)*
      · Demo: Permutations with No Repetition (17m)
      · Demo: Permutations with Unlimited Repetitions (8m)
      · Permutations with Limited Repetitions (9m)
      · Tricks to Solve The Famous MISSISSIPPI Problem in P&C (13m)
      · Vowels & Consonants Type Questions in P&C (9m)
      · Tricks to Solve Questions on  Arrangement of Letters (9m)
      · Tricks to Solve Questions on  Arrangement of Digits  (1) (14m)
      · Tricks to Solve Questions on  Arrangement of Digits  (2) (6m)
      · PYQ ×7
      · PQ ×2
  - *Circular & Grouping Permutations*
      · Tricks to Solve Grouping Type Questions in P&C (12m)
      · Tricks for Problems on Choosing Items from Group of Items (14m)
      · Circular Arrangements (10m)
      · Circular Arrangements on Groups (10m)
      · Tricks to Solve  Necklace Based Problems (8m)
      · PQ ×1
  - *Combinations (with & without Repetition)*
      · Combinations with No Repetitions & Unlimited Repetitions (13m)
      · Solving Some Basic Questions on Permutation & Combination (14m)
      · An Important Property (Binomial Theorem) (6m)
      · Total Outcomes, MCQ Paper Solving, Unlimited Repetitions (10m)
      · PYQ ×7
      · PQ ×4
  - *Special Applied Problems*
      · Tricks to Solve Questions on  Binary Strings (10m)
      · Trick for Sum of all numbers formed from given digits (11m)
      · Finding Rank of a Word (Concept + Short Trick) (13m)
      · Question on Finding Rank of a Word Without Repetition (11m)
      · Short Trick to Find Rank of a Word With Repetitions (9m)
      · Short Trick to Find Number of Handshakes (10m)
      · Chocolate Picking Problem (6m)
      · Counting Sticks Approach (11m)
      · Short Tricks to Solve  Dice Sum Problem  (1) (10m)
      · Short Tricks to Solve  Dice Sum Problem  (2) (12m)
      · Conventional Method of Solving  Dice Sum Problem (7m)
      · Short Tricks for  Alphabet Selection Problem  in P&C (8m)
      · PYQ ×1
      · PQ ×2
  - *Advanced Counting Theorems*
      · Principle of Inclusion & Exclusion, Use of Venn Diagram (13m)
      · Number of Intersection Points & Parallelogram (7m)
      · Concept & Short Tricks of Derangement in P&C (11m)
      · Important Questions on Derangements (10m)
      · PYQ ×9
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×28
      · PQ ×12
- **Probability**
  - *Basic Concepts and Terminology*
      · What is Sure Event, Impossible Event, Complementary Event (14m)
      · Short Trick to find total outcomes in an experiment (12m)
      · Mutually Exclusive Events & Exhaustive Events (17m)
      · Odds in Favour of an event & Odds Against An Event (11m)
      · Demo: What is Experiment, Event, Favorable & Total Outcome (15m)
      · PYQ ×3
      · PQ ×6
  - *Classical Problems (Cards, Dice, Coins, Digits, Number, Objects)*
      · Short Tricks to deal with cases of 'At least' & 'At most' (9m)
      · Tricks & Techniques to Solve Dice Sum Problems (16m)
      · Tricks & Techniques to Solve Playing Cards Problem (9m)
      · Finding Probability of 53 Sundays in a Leap Year (12m)
      · PYQ ×31
      · PQ ×14
  - *Probability Using Venn Diagrams & Set Theory*
      · Some Important Events (A AND B, A OR B, A BUT NOT B) (15m)
      · PYQ ×7
      · PQ ×2
  - *Conditional Probability*
      · PYQ ×4
      · PQ ×7
  - *Law of Total Probability*
      · PYQ ×6
      · PQ ×1
  - *Bayes Theorem (Inverse Probability)*
      · PYQ ×3
      · PQ ×1
  - *Probability Using Permutation & Combination Logic*
      · PYQ ×7
      · PQ ×4
  - *Continuous Probability Distribution, Random Variables & Expected Value*
      · PYQ ×21
      · PQ ×8
  - *Multiple Topics*
      · Quick Revision & Practice Questions - Part 1 (1.1h)
      · Quick Revision & Practice Questions - Part 2 (34m)
      · PYQ ×1
      · PYQ ×83
      · PQ ×43
- **Mensuration and Geometry**
  - *Basic Concepts and Geometric Terminology*
      · Triangle & Circle, Basic Concepts & Formulas (55m)
      · PYQ ×4
      · PQ ×2
  - *2D Mensuration (Plane Figures)*
      · Practice Questions - Part 1 (44m)
      · Practice Questions - Part 2 (56m)
      · Practice Questions - Part 3 (1.1h)
      · PYQ ×26
      · PQ ×9
  - *3D Mensuration (Solid Figures)*
      · 3D Geometry Introduction (16m)
      · Surface Area, Volume and Capacity Are Different (17m)
      · 3D Geometry Important Question (5m)
      · PYQ ×12
      · PQ ×9
  - *Relation Between 2D & 3D Figures*
      · PYQ ×1
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×43
      · PQ ×22
- **Statistics**
  - *Introduction & Types of Data*
      · Basic Concepts (1.3h)
      · PQ ×2
  - *Mean, Median, and Mode for ungrouped data*
      · PYQ ×3
      · PQ ×6
  - *Mean, Median, and Mode for grouped data*
      · Advance Concepts (56m)
      · PYQ ×2
      · PQ ×1
  - *Range, Mean Deviation, Variance, and Standard Deviation*
      · PYQ ×5
      · PQ ×7
  - *Multiple Topics*
      · PYQ ×2
      · PQ ×2
      · PYQ ×12
      · PQ ×18
- **Data Interpretation**
  - *Basic Concepts & Terminologies*
      · Demo: Pre-requisites & Basic Concepts (7m)
      · Demo: Types of Graphs (11m)
      · Demo: Tricks Ratio to Percentage Table (22m)
      · Ratio - Percentage Conversion (12m)
  - *Table Graph*
      · Table Graph (Part 1) (25m)
      · Table Graph (Part 2) (8m)
      · PYQ ×8
      · PQ ×5
  - *Bar Graph*
      · Bar Graph (8m)
      · PYQ ×3
      · PQ ×3
  - *Pie Chart (Pie Graph)*
      · Pie Chart (Pie Graph) (14m)
      · PYQ ×4
      · PQ ×4
  - *Line Graph*
      · Line Graph (Part 1) (9m)
      · Line Graph (Part 2) (7m)
      · PYQ ×2
      · PQ ×2
  - *2D-3D Plots and Maps*
      · PYQ ×5
  - *Caselet / Paragraph DI*
  - *Multiple Topics*
      · PYQ ×22
      · PQ ×14
- **Average**
  - *Basic Concepts and Formulas*
      · Basic Concepts, Formulas & Questions (6m)
      · PYQ ×3
      · PQ ×5
  - *Average of Consecutive / Odd / Even / Natural Numbers*
      · Average of First N Odd, Even, Consecutive No (8m)
      · Average of N Consecutive Odd & Even Numbers (7m)
      · PQ ×3
  - *Average of Arithmetic Series, Squares, and Cubes*
      · Average of Arithmetic Series, Squares, Cubes (5m)
  - *Change in Average (When Members Join, Leave, or Replace)*
      · Change on Average when person join or leave (7m)
      · Change on Average when a person replaces (8m)
      · PYQ ×2
      · PQ ×4
  - *Effect on Average by Arithmetic Operations*
      · Effect on Average by Arithmetic Operations (6m)
      · PQ ×1
  - *Weighted Average, Combined / Mixture Average Problems*
      · Weighted Average - Concept & Short Tricks (9m)
      · PYQ ×5
      · PQ ×3
  - *Practical and Contextual Word Problems*
      · 8 (7m)
      · Cricket Based Problems on Average (Part 1) (8m)
      · Average - Cricket Based Problems on Average (Part 2) (10m)
      · PYQ ×1
  - *Multiple Topics*
      · Average (Quick Revision & Practice Problems) Part 1 (32m)
      · Average (Quick Revision & Practice Problems) Part 2 (1.2h)
  - *Error Correction Problems*
      · PYQ ×1
      · PYQ ×12
      · PQ ×16
- **Arithmetic**
  - *Basic Arithmetic*
      · Arithmetic - Part 1 (1.1h)
      · Arithmetic - Part 2 (27m)
      · PYQ ×5
      · PQ ×10
  - *Advance Arithmetic*
  - *Multiple Topics*
      · PYQ ×5
      · PQ ×10
      · PYQ ×276
      · PQ ×196

### 1. Logical Reasoning — 47 vids · 15.9h · 154 PYQs · 219 PQs

- **Non Verbal Reasoning (Spatial Aptitude) (Spatial Reasoning) (Visual Reasoning)**
  - *Image Analysis and Rotation Problems*
      · Demo: Image Analysis (15m)
      · PYQ ×10
      · PQ ×3
  - *Translation*
  - *Scaling*
  - *Mirror and Water Images*
      · Demo: Mirror Images (14m)
      · Demo: Water Images (13m)
      · PYQ ×7
      · PQ ×9
  - *Grouping, Assembling and Shape Construction*
      · Group of Images (14m)
      · Shape Construction (15m)
      · PYQ ×5
      · PQ ×4
  - *Paper Folding and Paper Cutting*
      · Paper Cutting (16m)
      · Paper Folding (12m)
      · PYQ ×4
      · PQ ×1
  - *Dot Situation Problems*
      · Dot Situation (15m)
  - *Series & Pattern Recognition (Patterns in 2D) (Symbol Series)*
      · Series (25m)
      · PYQ ×10
      · PQ ×4
  - *Patterns in 3D*
      · PYQ ×1
  - *Classification (Odd-One-Out)*
      · Classification (17m)
      · PYQ ×5
      · PQ ×19
  - *Embedded and Hidden Figures*
      · Embedded Images (15m)
  - *Figure Matrix (Figure Analogy)*
      · Figure Matrix (16m)
      · PYQ ×2
      · PQ ×2
  - *Rule Detection (Logical Pattern Rules)*
      · Rule Detection (12m)
      · PYQ ×4
  - *Pattern Completion & Figure Completion*
      · Pattern Completion (10m)
      · PYQ ×5
      · PQ ×2
  - *Multiple Topics*
      · Spatial Aptitude - Concepts, Short Tricks & Questions (33m)
      · Visual Reasoning (2m)
      · PYQ ×53
      · PQ ×44
- **Series (Number and Letter Series) (Numerical Relations and Reasoning)**
  - *Basic Concepts and Terminologies*
      · Demo: Types of Series, Question Types, Pre-requisites (14m)
      · Demo: Tricks to Remember Alphabet to Number Mapping (15m)
      · Demo: Story for Reverse Alphabet to Number Mapping (11m)
      · PQ ×1
  - *Number Series*
      · All Possible Series that can be formed (11m)
      · Some Important Observations and Short Tricks (22m)
      · Series with combination (12m)
      · Find the next term (Important Questions) (9m)
      · Important Practice Questions (Part 2) (18m)
      · Brute Force Short Trick for Tough Questions (18m)
      · HOT (Higher Ordered Thinking) Questions (14m)
      · PYQ ×15
      · PQ ×34
  - *Letter or Alphabet Series*
      · Alphabet Series (Important Questions) (15m)
      · Important Practice Questions (Part 3) (11m)
      · Important Practice Questions (Part 4) (15m)
      · PYQ ×10
      · PQ ×17
  - *Alpha-Numeric Series*
      · PYQ ×1
      · PQ ×8
  - *Multiple Topics*
      · Find the missing term (Important Questions) (11m)
      · Find the odd one out (Important Questions) (15m)
      · Important Practice Questions (Part 1) (18m)
      · NUMBER AND LETTER SERIES (Revision & Practice Problems) (1.1h)
      · PYQ ×26
      · PQ ×60
- **Deductive and Inductive Reasoning (Logical Deduction and Induction) (Prepositional Reasoning)**
  - *Statement and Conclusion*
      · Statement & Conclusion (Part 1) (32m)
      · Statement & Conclusion (Part 2) (22m)
      · PYQ ×7
      · PQ ×7
  - *Statement and Arguement*
      · Statement & Argument (26m)
      · PQ ×8
  - *Statement and Assumption*
      · Statement & Assumption (11m)
      · PYQ ×2
      · PQ ×6
  - *Statement and Course of Action*
      · Statement & Course of Action (10m)
      · PYQ ×6
      · PQ ×7
  - *Assertion and Reasoning*
      · PYQ ×1
  - *Inference*
      · PYQ ×5
      · PQ ×4
  - *Cause and Effect*
      · PYQ ×2
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×23
      · PQ ×34
- **Analogy**
  - *Basic Concept of Analogy*
      · 1: Non Verbal Reasoning - Analogy (16m)
      · PYQ ×12
      · PQ ×33
  - *Number-Based Analogy*
      · PYQ ×8
      · PQ ×5
  - *Letter or Alphabet Analogy*
      · PYQ ×6
      · PQ ×15
  - *Symbol or Figure or Diagram-Based Analogy (Non-Verbal Analogy)*
      · PYQ ×2
  - *Multiple Topics*
      · PYQ ×1
      · PYQ ×29
      · PQ ×53
- **Cubes & Dices**
  - *Basic Concepts & Properties*
      · PQ ×2
  - *Closed Dice*
      · Closed Dice Tricks & Questions (29m)
      · PYQ ×2
      · PQ ×1
  - *Cubes and Open Dice*
      · Cubes & Dice (Part 1) (11m)
      · Cubes & Dice (Part 2) (19m)
      · PYQ ×4
  - *Painted & Cut Cube Problems, Rotation & Comparison of Dice*
      · Painted & Cut Cube Problems (42m)
      · Dice (31m)
      · PYQ ×4
      · PQ ×1
  - *Multiple Topics*
      · PYQ ×10
      · PQ ×4
- **Syllogisms**
  - *Basic Syllogism*
      · Concepts, Short Tricks & Questions (Part 1) (1.0h)
      · Venn Diagram Concepts for Syllogism (9m)
      · PYQ ×11
      · PQ ×22
  - *Advance Syllogism*
      · Concepts, Short Tricks & Questions (Part 2) (1.6h)
      · PYQ ×1
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×1
      · PYQ ×13
      · PQ ×24
      · PYQ ×154
      · PQ ×219

### 2. English Language — 101 vids · 35.9h · 278 PYQs · 446 PQs

- **Vocabulary**
  - *Word Meanings (Contextual Vocabulary)*
      · Demo: Part 1 (1.8h)
      · Demo: Part 2 (1.7h)
      · Demo: Part 3 (1.1h)
      · Part 4 (1.1h)
      · PYQ ×9
      · PQ ×15
  - *Synonyms & Antonyms*
      · Introduction - Synonyms & Antonyms (23m)
      · Building vocabulary the  smart way (18m)
      · Root Words, Prefixes, Suffixes (17m)
      · High Frequency  Synonyms (24m)
      · High Frequency  Antonyms (15m)
      · PART A - Commonly confused pairs (14m)
      · Word Relationships Vocabulary Networks (13m)
      · Question Solving  Strategies (10m)
      · 55 Synonyms&Antonyms NVS 2014 (2m)
      · PYQ ×47
      · PQ ×66
  - *Homophones / Homonyms / Confusing Words*
      · Module 1: Homophones, Homonyms, Confusing Words (24m)
      · Module 2: Homophones, Homonyms, Confusing Words (17m)
      · PYQ ×3
  - *One-Word Substitutions*
      · Concepts, Tricks & Questions (53m)
      · Practice Questions (22m)
      · PYQ ×11
      · PQ ×12
  - *Idioms, Phrases, Pharasal Verbs and Collocations*
      · Idioms, Phrases and Collocations 1 (20m)
      · Idioms, Phrases and Collocations 2 (9m)
      · Idioms, Phrases and Collocations 3 (12m)
      · PYQ ×16
      · PQ ×29
  - *Root Words, Prefixes & Suffixes*
      · Part-1 Root Words, Prefixes, Suffixes (22m)
      · Part-2 Root Words, Prefixes, Suffixes (23m)
      · PQ ×1
  - *Foreign Origin Words (Commonly Used)*
      · Foreign Words (10m)
      · PQ ×1
  - *Spelling & Commonly Mis-spelt Words*
      · Concepts, Rules, Short Tricks & Questions (31m)
      · Spellings, Commonly Misspelt Words 1 (19m)
      · Spellings, Commonly Misspelt Words 2 (5m)
      · Spellings, Commonly Misspelt Words 3 (10m)
      · PYQ ×17
      · PQ ×7
  - *Multiple Topics*
      · PQ ×8
      · PYQ ×103
      · PQ ×139
- **Noun**
  - *Concepts & Terminologies*
      · Demo: Concepts, Types, Rules, Tricks & Questions (1.1h)
      · Demo: Practice Questions (36m)
      · PYQ ×1
      · PQ ×2
  - *Types of Nouns*
      · PQ ×5
  - *Singular vs Plural Forms (Regular & Irregular)*
      · PQ ×2
  - *Plural-Only & Plural-Looking Singular Nouns*
      · PQ ×3
  - *Collective Nouns (Sense-Based VERB Agreement)*
  - *Uncountable Noun Measurement Units*
  - *Possessive Case (Apostrophe Rules)*
  - *Hyphenated & Number-Based Compound Nouns*
  - *Multiple Topics*
      · PYQ ×1
      · PQ ×12
- **Pronoun**
  - *Concepts & Terminologies*
      · Concepts, Types, Rules, Tricks & Question (60m)
  - *Types of Pronouns (Basic Classification)*
  - *Subjective vs Objective Case*
      · PQ ×3
  - *Pronouns After “Let” & in Comparison (as/than)*
      · PQ ×2
  - *Reflexive Pronouns (Correct vs Wrong Use)*
      · PYQ ×3
      · PQ ×2
  - *Each Other vs One Another*
  - *Who / Whom / That (Error-Prone Relative Pronouns)*
      · PYQ ×1
      · PQ ×1
  - *Pronoun–Antecedent Agreement & Ambiguity*
      · PYQ ×1
      · PQ ×1
  - *Multiple Topics*
      · PYQ ×5
      · PQ ×9
- **Verb**
  - *Concepts, Terminologies, Types of Verbs, Usage*
      · Concept,Types (18m)
      · PQ ×3
  - *Regular & Irregular Verbs*
  - *Finite & Non-Finite Verbs*
      · Non Finite Verbs(Gerunds,Infinitives,Participles) (9m)
  - *Auxiliary (Helping) Verbs*
      · Primary Auxillaries,Modals (16m)
      · PYQ ×2
      · PQ ×1
  - *Agreement of Verb with Subject (Concord)*
      · Conditional Sentence,Subject Verb Agreement (15m)
      · PQ ×2
  - *Voice & Verb Use (Active–Passive Impact)*
      · Active vs Passive Voice (4m)
  - *Verb Usage Errors*
      · Common Verb Error Questions (4m)
  - *Verb Forms & Principal Parts (V1–V5)*
      · 5 forms of verbs ,Regular vs Irregular Verbs (10m)
  - *Multiple Topics*
      · Exam Style Practice Questions (Part 1) (2m)
      · Exam Style Practice Questions (Part 2) (6m)
      · PYQ ×2
      · PQ ×6
- **Adjectives**
  - *Concepts & Terminologies*
      · Demo: Concepts, Rules, Short Tricks & Questions (1.3h)
      · PQ ×2
  - *Types of Adjectives*
  - *Degrees of Comparison*
      · PQ ×2
  - *Common Errors*
  - *Quantifier Adjectives (Some, Any, Few, Little, Much, Many)*
      · PQ ×1
  - *Less vs Fewer / Whole vs All*
  - *Order of Adjectives*
  - *Adjectives vs Adverbs Confusion*
      · PQ ×1
  - *Multiple Topics*
      · PQ ×6
- **Adverb**
  - *Introduction, Importance & Functions of Adverbs*
      · Introduction,Importance,Function (7m)
  - *Types of Adverbs*
      · Types of Adverbs (5m)
      · PQ ×1
  - *Position of Adverbs (Placement Rules)*
      · Position of Adverbs (8m)
  - *Common Adverb Placement Errors*
      · Common Adverb Placement Errors (4m)
  - *Degrees of Comparison (Positive/Comparative/Superlative)*
      · PQ ×1
  - *Adverbs vs Adjectives Confusion*
      · PQ ×1
  - *Formation of Adverbs (Suffix Rules)*
  - *Adverbial Phrase & Adverbial Clause (Usage Patterns)*
      · Adverb Clauses and it's examples (6m)
      · Adverb Phrase,Adverb Practice Questions (8m)
      · PQ ×1
  - *Negative Adverbs (Inversion Trigger)*
  - *Multiple Topics*
      · Understanding Adverbs  Forms, Degrees and Adverbs vs. Adjectives (4m)
      · Adverbs Practice Questions (6m)
      · PQ ×4
- **Preposition**
  - *Concepts & Terminologies*
      · Concepts, Types, Rules, Short Tricks & Questions (42m)
  - *Basic Preposition Usage*
      · Practice Questions (25m)
      · PYQ ×10
      · PQ ×40
  - *Between vs Among Rule*
      · PQ ×1
  - *Preposition Errors*
      · PQ ×3
  - *Multiple Topics*
      · PYQ ×10
      · PQ ×44
- **Conjunction**
  - *Concepts & Terminologies*
      · Concepts, Rules, Short Tricks & Questions (34m)
  - *Types of Conjunctions*
      · PYQ ×1
  - *Contrast / Condition / Reason Conjunctions*
      · PYQ ×1
      · PQ ×3
  - *Correlative Conjunction Rules*
      · PYQ ×1
      · PQ ×1
  - *Conjunction Error Patterns (Redundancy Traps)*
  - *Parallel Structure with Conjunctions*
      · PQ ×1
  - *Multiple Topics*
      · PYQ ×3
      · PQ ×5
- **Interjection**
  - *Concepts, Definitions, Purpose*
      · PQ ×1
  - *Types of Emotions Expressed*
  - *Punctuation & Position Rules*
      · PQ ×1
  - *Multiple Topics*
      · PQ ×2
- **Articles**
  - *Basic Concepts, Terminologies and Rules*
      · Concepts, Types, Rules, Short Tricks & Questions (35m)
      · 2 50347 Artciles Basic Concepts BPSC-_1 (2m)
      · PYQ ×1
  - *"A or An" article*
      · PYQ ×2
      · PQ ×4
  - *"The" article*
      · PQ ×6
  - *No article cases*
      · PQ ×6
  - *Articles Before Adjectives + Nouns*
      · PQ ×2
  - *Articles in Sound Confusion Words*
      · PYQ ×1
      · PQ ×6
  - *Multiple Topics*
      · PYQ ×4
      · PQ ×24
- **Tenses**
  - *Basics, Terminologies, Time & Action Concept*
      · Demo: Introduction (2m)
      · Demo: The Three Tenses - Past, Present and Future (2m)
      · Demo: Four Aspects (Nature) of an Action (8m)
  - *Present Tense*
      · Present Tense (12m)
      · PQ ×1
  - *Past Tense*
      · Past Tense (9m)
      · PYQ ×4
      · PQ ×5
  - *Future Tense*
      · Future Tense (8m)
      · PYQ ×1
      · PQ ×3
  - *Tense Selection Guide*
      · Concepts, Rules, Short Tricks & Questions (36m)
      · Selection guide (Tips and Tricks) (4m)
      · PYQ ×2
  - *Common Tense Errors*
      · PQ ×2
  - *Application in Active-Passive*
  - *Application in Direct-Indirect*
  - *Multiple Topics*
      · PYQ ×7
      · PQ ×11
- **Subject Verb Agreement (Verb Noun Agreement)**
  - *Basic Concepts, Terminologies and Rules*
      · Demo: Concepts, Rules & Questions (35m)
      · Demo: Practice Questions (50m)
      · PYQ ×1
      · PQ ×3
  - *Subject Separated by Phrase like "as well as, along with, together with etc"*
      · PQ ×2
  - *Words Linked by "either or, neither nor etc"*
      · PQ ×3
  - *Collective Nouns*
      · PQ ×1
  - *Indefinite Pronouns - Words Linked with "Each, Every, Everyone, Someone, Many, Few, Several etc."*
      · PYQ ×1
      · PQ ×1
  - *Amount, Quantity, Distance, Period Expressions*
      · PQ ×1
  - *Common Errors*
      · PYQ ×1
      · PQ ×1
  - *Multiple Topics*
      · PYQ ×3
      · PQ ×12
- **Modals**
  - *Introduction to Modals and Their Functions*
      · Introduction to Modal Verbs (4m)
  - *Modals of Ability, Permission and Possibility*
      · CAN - Expressing Ability and Capacity (6m)
      · COULD - Past Ability and Polite Requests (5m)
      · MAY - Formal Permission and Possibility (6m)
      · MIGHT - Weaker Possibility and Suggestions (4m)
  - *Modals of Obligation, Necessity and Advice*
      · (Part 1) - Strong Obligation or Necessity (4m)
      · (Part 2) Logical Conclusions and Certainy (6m)
      · Moral Duty and Ideal Actions (4m)
      · HAVE TO_HAS TO_HAD TO - External Obligation (6m)
      · NEED - Requirements and Necessity (4m)
      · SHOULD - Advice and Expressing Probability (4m)
  - *Modals of Future Intentions, Polite Requests and Hypotheticals*
      · WILL - Future Intentions and Certainty (5m)
      · WOULD - Polite Requests ,Past Habits,Hypotheticals (3m)
      · PYQ ×1
  - *Comparison of Modals + Mixed Usage Questions*
      · Modal comparision _ Practice Questions (11m)
      · Modals - Concepts, Rules, Short Tricks & Questions (19m)
      · PYQ ×1
  - *Multiple Topics*
      · PYQ ×2
- **Determiner**
  - *Introduction to Determiners and Their Types*
  - *Quantifiers and Numbers*
      · PYQ ×1
      · PQ ×2
  - *Demonstratives, Possessives and Distributives*
  - *Advanced Usage and Common Confusions*
  - *Multiple Topics*
      · PYQ ×1
      · PQ ×2
- **Sentence Correction (Error Correction)**
  - *Basic Concepts, Terminologies and Rules*
      · Concepts, Rules, Tricks & Questions (1.2h)
      · Concept, Rules, Tricks, Questions (28m)
      · Practice Questions (39m)
      · Practice Questions (1) (12m)
      · Practice Questions (2) (15m)
  - *Subject–Verb Agreement Errors*
      · PYQ ×6
      · PQ ×7
  - *Tense & Verb Form Errors*
      · PYQ ×4
      · PQ ×5
  - *Pronoun & Reference Errors*
      · PQ ×1
  - *Preposition & Connector Errors*
      · PYQ ×5
      · PQ ×4
  - *Modifier Placement Errors*
      · PQ ×1
  - *Adjective vs Adverb Errors*
      · PQ ×2
  - *Parallelism / Comparison Errors*
      · PYQ ×1
      · PQ ×1
  - *Redundancy & Word Choice Errors*
      · PYQ ×2
  - *Vocabulary Error*
  - *Sentence Improvement*
      · Concepts, Tricks & Questions (11m)
      · PQ ×4
  - *Logical Error*
      · PYQ ×1
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×1
      · PQ ×5
      · PYQ ×20
      · PQ ×32
- **Sentence Completion (Fill in the blanks)**
  - *Basic Concepts, Terminologies and Rules*
      · Concepts, Rules & Short Tricks (27m)
      · Easy Questions (26m)
      · Tough Questions (22m)
      · Practice Questions (30m)
      · Practice Questions (46m)
      · PYQ ×3
  - *Context Understanding (Meaning of the Sentence)*
      · PYQ ×10
      · PQ ×7
  - *Signal Words (Logic Clues)*
      · PQ ×3
  - *Parts of Speech Fit*
      · 123 Sentence Completion Context Understanding 7522 NVS 2019 (2m)
      · PYQ ×8
      · PQ ×5
  - *Vocabulary in Context (Tone/Emotion Fit)*
      · PYQ ×6
      · PQ ×17
  - *Idioms and Pharases Usage*
      · PYQ ×5
      · PQ ×5
  - *Verb Tense or Verb Form Based on Clues*
      · PYQ ×7
      · PQ ×6
  - *Multiple Topics*
      · PYQ ×2
      · PYQ ×41
      · PQ ×43
- **Comprehension / Reading Comprehension / Unseen Passages (Critical Reasoning) (Paragraph Questions)**
  - *Basic Reading & Understanding (Literal Comprehension)*
      · Concepts, Tricks, Questions (14m)
      · Concepts, Rules & Tricks (29m)
      · Practice Questions (1) (43m)
      · Practice Questions (2) (21m)
      · Practice Questions (3) (56m)
      · Practice Questions (4) (27m)
      · Comprehension - UGC NET June 2025 (10m)
      · PYQ ×18
      · PQ ×31
  - *Vocabulary in Context*
      · PYQ ×3
      · PQ ×11
  - *Central Idea and Main Theme Identification*
      · PYQ ×7
      · PQ ×4
  - *Tone & Attitude Detection*
      · PYQ ×4
      · PQ ×3
  - *Inference-Based Questions, Assumption and Implication Recognition*
      · PYQ ×24
      · PQ ×3
  - *Data / Example Interpretation*
      · PYQ ×1
      · PQ ×1
  - *True / False / Cannot Say Type Questions*
      · PYQ ×3
      · PQ ×1
  - *Logical Structure & Flow Understanding (Cause-effect, comparision-contrast, problem-solution)*
      · PYQ ×1
      · PQ ×2
  - *Multiple Topics*
      · Critical Reasoning - Concepts, Short Tricks & Questions (1) (11m)
      · PQ ×3
      · PYQ ×61
      · PQ ×59
- **Sentence Re-arrangements (Para Jumbles) (Narrative Sequencing)**
  - *Basic Sentence Re-arrangement (Para Jumbles)  (Narrative Sequencing)*
      · Concepts, Rules, Short Tricks & Questions (1.2h)
      · PYQ ×9
      · PQ ×21
  - *Advance Sentence Re-arrangement (Para Jumbles)  (Narrative Sequencing)*
      · Practice Questions (22m)
      · PQ ×3
  - *Multiple Topics*
      · PYQ ×9
      · PQ ×24
- **Sentence Construction**
  - *Basics of Sentence Construction*
      · Concepts, Tricks & Questions (8m)
      · PYQ ×1
      · PQ ×3
  - *Parts of Speech Placement in Sentence Construction*
      · PQ ×1
  - *Sentence Sequencing and Coherence (Micro Sentence Construction)*
      · PYQ ×2
  - *Constructing Grammatically Correct Sentences (Error-Free Writing)*
      · PYQ ×2
      · PQ ×8
  - *Advanced Sentence Construction (Context + Meaning Accuracy)*
  - *Multiple Topics*
      · PYQ ×1
      · PYQ ×6
      · PQ ×12
      · PYQ ×278
      · PQ ×446

### 3. Unit Tests — 0 vids · 1.0h · 0 PYQs · 0 PQs

      · IOCL Unit Test - Quantitative Aptitude (20m)
      · IOCL Unit Test - Logical Reasoning (20m)
      · IOCL Unit Test - Verbal Ability (20m)

### 4. Full-Length Mock Tests — 0 vids · 5.0h · 0 PYQs · 0 PQs

      · IOCL Mock Test - 1 - General Aptitude (1.0h)
      · IOCL Mock Test - 2 - General Aptitude (1.0h)
      · IOCL Mock Test - 3 - General Aptitude (1.0h)
      · IOCL Mock Test - 4 - General Aptitude (1.0h)
      · IOCL Mock Test - 5 - General Aptitude (1.0h)

### 5. Complete Paper Full Mock Test — 0 vids · 17.5h · 0 PYQs · 0 PQs

      · IOCL - Complete Paper Mock Tests — Test 1 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 2 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 3 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 4 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 5 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 6 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 7 (2.5h)

---

## CIL MT (CS) superset

`COAL-INDIA-MANAGEMENT-TRAINEE` · **2967 videos / 401.1h** · 1236 PYQs · 5198 PQs · 959 subtopics · 19 tests · 1397 notes

### 0. About Course — 1 vids · 7m · 0 PYQs · 0 PQs

- **About the Course**
  - *Exam Syllabus*
  - *Study Plan & Test Schedule*
  - *Course Overview*
      · Course Overview (7m)
  - *Live Class Schedule*

### 1. Paper-2 | Programming & Data Structures — 224 vids · 18.7h · 169 PYQs · 451 PQs

- **C Fundamentals**
  - *Intro & Data Types*
      · Introduction of C (7m)
      · UNDERSTANDING LANGUAGE (7m)
      · Types of Variables (9m)
      · C PROGRAMMING - OUR FIRST PROGRAM (14m)
      · Printf & Scanf (7m)
      · Main & Command Line Arguments (25m)
      · Garbage Values (12m)
      · PYQ ×4
      · PQ ×13
  - *Operators & Expressions*
      · Instructions and Operations (8m)
      · Integer to float conversion (type casting) (8m)
      · Practice Question-Arithmetic Exp (1m)
      · PYQ ×7
      · PQ ×9
  - *Understanding Operators*
      · SizeOf Operator (8m)
      · Unary Operator (4m)
      · Bitwise Operator (7m)
      · Types of Swapping (5m)
      · Increment decrement operator (3m)
      · Logical Operator (6m)
      · Practice Questions - Logical Operator (6m)
      · Ternery Operator (4m)
      · PQ ×2
  - *Data Type Fundamentals*
      · Data Types (8m)
      · chars,signed and unsigned (6m)
      · Data Types (3m)
      · PYQ ×2
      · PQ ×4
  - *Integral Datatypes*
      · IDTs (3m)
      · Cyclic nature of Integral Data Type (Int) (11m)
      · Cyclic nature of Integral Data Type (Char) (3m)
      · Practice Question IDT - 1 (2m)
      · Practice Question IDT - 2 (2m)
      · PYQ ×13
      · PQ ×28
- **Control Flow**
  - *If-Else Statements – Basic, Advanced & Nested If–Else Structures*
      · Conditional Statements(Decision Control) in C (10m)
      · If-Else Statements_PQ (9m)
      · PYQ ×3
      · PQ ×3
  - *Loops & Iteration*
      · The While Loop (11m)
      · For Loop (8m)
      · Break Statement (7m)
      · The Do While Loop (3m)
      · PYQ ×11
      · PQ ×8
  - *Switch & Jump Stmts*
      · Control statement (4m)
      · The GOTO Keyword (3m)
      · Avoid goto (3m)
      · PQ ×5
      · PYQ ×14
      · PQ ×16
- **Functions**
  - *Function Basics – Definition, Declaration, and Calling Mechanisms*
      · WHAT IS FUNCTIONS (9m)
      · TYPES OF FUNCTION (7m)
      · SCOPE RULE OF FUNCTION (3m)
      · PYQ ×4
      · PQ ×6
  - *Basic Recursion*
      · Function_Practice Question (3m)
      · PYQ ×5
      · PQ ×2
      · PYQ ×9
      · PQ ×8
- **Arrays & Pointers**
  - *Array Basics*
      · Demo: Introduction of Array -1 (4m)
      · Introduction of Array -2 (13m)
      · PYQ ×3
      · PQ ×3
  - *Pointer Basics – Declaration, Initialization, and Dereferencing*
      · AN INTRODUCTION TO POINTERS (11m)
      · POINTERS DECLARATION (4m)
      · PYQ ×5
      · PQ ×7
  - *Relationship Between Arrays and Pointers*
      · Relationship between Array and Pointers (7m)
      · Address Representation (17m)
      · Address Operation (3m)
      · Address Operation - Substraction (2m)
      · Key points of Array (2m)
      · Practice question on Pointer (4m)
      · PYQ ×4
      · PQ ×8
  - *Character Pointer (String)*
      · Character Pointer (1m)
      · Character Pointer & String (6m)
      · PYQ ×1
      · PQ ×4
  - *Call By Value/Address/Reference*
      · Back to Function Calls (Parameter Passing) (6m)
      · Call by Address (2m)
      · PYQ ×4
      · PQ ×4
  - *Recursion with pointer*
      · PQ ×1
      · PYQ ×17
      · PQ ×27
- **Storage Classes, Structures & Enums**
  - *Storage classes*
      · Storage Class (5m)
      · Register Storage Class (2m)
      · Static Storage Class (3m)
      · External Storage Class (3m)
      · PQ ×10
  - *Structures - Declaration, Initialization & Union Comparison*
      · Structure in C (10m)
      · Union (3m)
      · PYQ ×3
      · PQ ×7
      · PYQ ×3
      · PQ ×17
- **DMA, Macros, Scoping & File Handling**
  - *Dynamic Memory Allocation*
      · DMA - malloc (10m)
      · DMA - calloc (5m)
      · DMA-Memory Leak Problem (3m)
      · PYQ ×1
      · PQ ×7
  - *Macros*
      · Macros (4m)
      · Types of Macros (1m)
      · Benifits of Macros (2m)
      · Practice Question - Macros (2m)
      · Practice Question - Macros 2 (1m)
      · Practice Question - Macro 4 (1m)
      · Practice Question - Macro 3 (1m)
      · PYQ ×1
      · PQ ×7
- **Introduction to DS**
  - *DS Basics & Types*
      · Why we study data structure and algorithm (5m)
      · What is data structure (5m)
      · Effects of Data Structure (3m)
      · Primitive Vs Non-Primitive Data Structure (5m)
      · Linear Vs Non-Linear Data Structure (3m)
      · Demo: Why we study data structure and algorithm (5m)
      · Demo: What is data structure (5m)
      · PYQ ×1
      · PQ ×7
      · PYQ ×1
      · PQ ×7
- **Array**
  - *Array Basics & Ops*
      · What is an Array (5m)
      · How to Declare & Initialize Array in C (3m)
      · Size of an Array (5m)
      · PYQ ×2
      · PQ ×13
  - *1D & 2D Addressing*
      · One Dimensional Array Access Formula (5m)
      · Practice question (2m)
      · Practice question (2m)
      · Two Dimensional Array (5m)
      · 2D Array Row Major Implementation (10m)
      · 2D Array Column Major Implementation (5m)
      · Practice Question (3m)
      · Practice Question (7m)
      · PYQ ×5
      · PQ ×13
  - *3D & Multi-dim Arrays*
      · 3D Array Implementation (6m)
      · PYQ ×1
      · PQ ×3
      · PYQ ×8
      · PQ ×29
- **Stack**
  - *Stack Basics & Ops*
      · Basic Idea Of Stack (8m)
      · Static Vs Dynamic Implementation Of Stack (4m)
      · Push Operation On Stack (6m)
      · Pop Operation on Stack (5m)
      · Stack Permutation (4m)
      · Practice Question (Gate 1994) (3m)
      · Practice Question (1m)
      · PYQ ×6
      · PQ ×27
  - *Infix Postfix Prefix*
      · Representation Of Expression (5m)
      · Infix To Prefix Conversion Of Expression (5m)
      · Infix To Postfix Conversion Of Expression (3m)
      · Tree method for conversion (3m)
      · Prefix and postfix conversion_pq (3m)
      · Conversion of Expression _PQ (1m)
      · PYQ ×7
      · PQ ×10
  - *Eval of Expressions*
      · Evaluation of expression Using Stack (4m)
      · Evaluation of Postfix Expression (2m)
      · Practice Question (2m)
      · PYQ ×3
      · PQ ×7
  - *Recursion & Stack*
      · Introduction to Recursion (6m)
      · Recursion Practice Question (4m)
      · Functions (5m)
      · Recursive Functions (7m)
      · recursive functions (7m)
      · Stack Practice questions (5m)
      · Stack Practice questions (5m)
      · Stack recursion Practice questions (3m)
      · Stack recursion Practice question (2m)
      · Stack recursion Practice questions (3m)
      · Recursion Practice questions (3m)
      · Stack Practice questions (10m)
      · Stack Practice questions (7m)
      · PYQ ×3
      · PQ ×9
  - *TOH & Classic Apps*
      · Tower of Hanoi (10m)
      · Practice Question (1m)
      · Fibonacci Number (10m)
      · Ackermann Function (4m)
      · PQ ×1
      · PYQ ×19
      · PQ ×54
- **Queue**
  - *Basics & Stack Mix*
      · Basic Idea Of Queue (5m)
      · Representation Of Queue (5m)
      · Enqueue Operation On Queue (5m)
      · Dequeue Operation On Queue (5m)
      · Problem With Simple Linear Queue (3m)
      · Queue_Practice Questions (1m)
      · Queue_Practice Questions (1m)
      · Queue_Practice Questions (2m)
      · PYQ ×6
      · PQ ×40
  - *Circular Queue*
      · Enqueue Operation On Circular Queue (6m)
      · Dequeue Operation On Circular Queue (4m)
      · PYQ ×1
      · PQ ×9
  - *Priority Queues & Variants*
      · Priority Queue (3m)
      · Stack_Practice Questions (1m)
      · PYQ ×1
      · PQ ×5
      · PYQ ×8
      · PQ ×54
- **Linked List**
  - *SLL Basics & Standard Operations*
      · Introduction To Link List (6m)
      · Analysis Of Link List (4m)
      · Link List Traversal Using Loop (4m)
      · Link List Traversal Using Recusrion (3m)
      · Searching An Element In Link List Using Loop (5m)
      · Searching An Element In LL Using Recursion (5m)
      · Insertion in Link List (4m)
      · Deletion From Link List (5m)
      · PYQ ×4
      · PQ ×24
  - *Structure Modification & Pointer Logic*
      · Reversing a Link List using Loop (6m)
      · Reversing a Link List using Recursion (4m)
      · Linked list Practice Questions (1m)
      · Linked listPractice Question (3m)
      · Stack Practice Questions (4m)
      · PYQ ×1
      · PQ ×4
  - *Doubly, Circular & Variants*
      · Header Link List (5m)
      · Doubly Link List (3m)
      · Header circular Doubly Link List (1m)
      · Linked List Practice Question (1m)
      · PYQ ×5
      · PQ ×10
      · PYQ ×10
      · PQ ×38
- **Tree**
  - *Binary Tree Basics & Props*
      · Introduction To Tree (5m)
      · Important Tree Terminology (7m)
      · Introduction To Binary Tree (5m)
      · Tree Practice Question (2m)
      · Binary Tree Practice question (7m)
      · PYQ ×9
      · PQ ×13
  - *Traversals & Construction*
      · Preorder Treversal of Binary Tree (5m)
      · Inorder Traversal Of Binary Tree (3m)
      · Post Order Traversal Of Binary Tree (2m)
      · Tree traversal Practice Question (2m)
      · Tree traversal Practice Question (1m)
      · Tree traversal Practice Question (1m)
      · Tree Practice Question (2m)
      · Tree Traversal Pseudocode (Pre-order) (8m)
      · Tree traversal Pseudocode (Inorder) (10m)
      · Tree Traversal Pseudocode (Post-Order ) (8m)
      · Tree Traversal Pseudocode PQ (7m)
      · Tree Traversal Pseudocode PQ (6m)
      · PYQ ×12
      · PQ ×10
  - *BST Basics & Operations*
      · Binary Search Tree (6m)
      · Insertion in Binary Search Tree (2m)
      · Deletion in BST (7m)
      · BST Practice Question (1m)
      · BST Practice Question (2m)
      · BST Practice Question (2m)
      · BST Practice Question (7m)
      · BST Practice Question (13m)
      · PYQ ×13
      · PQ ×29
  - *AVL Trees & Balancing*
      · AVL Tree (5m)
      · Insertion In AVL Tree (8m)
      · AVL Practice Question (11m)
      · AVL TREE Practice Question (1m)
      · AVL TREE Practice Questions (2m)
      · Deletion in AVL (8m)
      · Analysis of AVL (3m)
      · AVL TREE Practice Questions (3m)
      · PYQ ×3
      · PQ ×12
  - *Complete Binary Trees*
      · CBT (4m)
      · PYQ ×2
      · PQ ×5
  - *Advanced & k-ary Trees*
      · Threaded Binary Tree (15m)
      · K-ary Tree (9m)
      · K-ary Tree Practice Question 1 (8m)
      · K-ary Tree Practice Question 2 (3m)
      · K-ary Tree Practice Question 3 (2m)
      · K-ary Tree Practice Question 4 (6m)
      · K-ary Tree Practice Question 6 (3m)
      · K-ary Tree Practice Question 7 (2m)
      · K-ary Tree Practice Question 8 (2m)
      · Practice Question (1m)
      · PYQ ×3
      · PQ ×9
  - *Heaps & Priority Queues*
      · Heap (4m)
      · Practice Question-1 (3m)
      · Practice Question-2 (2m)
      · Practice Question-3( Insertion ) (2m)
      · Practice Question-4( deletion ) (3m)
      · PYQ ×5
      · PQ ×26
      · PYQ ×47
      · PQ ×104
- **Graphs**
  - *Graph Reps & Basics*
      · Introduction To Graph (5m)
      · Adjacency Matrix Representation (6m)
      · Adjacency List Representation (5m)
      · PYQ ×2
      · PQ ×9
  - *DFS & Applications*
      · Depth First Traversal (6m)
      · DFS Algo (5m)
      · Practice Question-1 (DFS) (3m)
      · Practice Question-2 (DFS) (2m)
      · PYQ ×1
      · PQ ×9
  - *BFS & Applications*
      · Breadth First Traversal (5m)
      · BFS Algo (3m)
      · Practice Question-1 (BFS) (1m)
      · Practice Question-2 (BFS) (2m)
      · PYQ ×4
      · PQ ×11
  - *Topological Sort & SCC*
      · classification of edges (15m)
      · types of edges (tree edge, backward edge ,forward edge ..) (5m)
      · PQ ×6
      · PYQ ×7
      · PQ ×35
- **Hashing**
  - *Hashing Basics & Functions*
      · Basics of Hashing (9m)
      · Characteristics of Good hash function (3m)
      · Most Popular Hash Function (3m)
      · Collision Resolution Technique (3m)
      · PYQ ×5
      · PQ ×10
  - *Open Addressing (Probing)*
      · Performance of Open Addressing (2m)
      · Linear Probing (6m)
      · Primary Secondary Clustering (3m)
      · Quadratic Probing (2m)
      · Double Hashing (2m)
      · Gate 2010 (3m)
      · PYQ ×6
      · PQ ×7
  - *Chaining & Perf Analysis*
      · Chaining (3m)
      · Practice Question-1 (Chaining) (3m)
      · PYQ ×1
      · PQ ×9
      · PYQ ×12
      · PQ ×26
      · PYQ ×169
      · PQ ×450
      · Coal India - Unit Test - Programming & Data Structures (45m)

### 2. Paper-2 | Databases / DBMS & SQL — 176 vids · 17.5h · 111 PYQs · 398 PQs

- **Basics of DBMS**
  - *DBMS Fundamentals*
      · Demo: Blue Print Of DBMS (7m)
      · Demo: What is Data and Information (6m)
      · Demo: What is Data Base Management System (4m)
      · Problem With File System (7m)
      · Views Of DataBase (4m)
      · Instance Vs Schema (2m)
      · PYQ ×2
      · PQ ×23
  - *Types & DBA Functions*
      · OLAP Vs OLTP (5m)
      · Types of Databases (11m)
      · Who is DataBase Administrator (1m)
      · PYQ ×1
      · PQ ×9
      · PYQ ×3
      · PQ ×32
- **ER Diagram**
  - *ER Modeling Fundamentals*
      · Introduction To ER Diagram (6m)
      · Understanding What is Entity (6m)
      · What Is Entity Set (4m)
      · Basics Of Attributes (3m)
      · Single Vs Multivalued Attributes (6m)
      · Simple Vs Composite Attributes (5m)
      · What Is Relationship (5m)
      · Degree Of a Relationship (5m)
      · PYQ ×2
      · PQ ×18
  - *Cardinalities, Participation & Entity Strength*
      · Cardinality Ratios and Mapping (7m)
      · Participation Constraints (8m)
      · Strong Vs Weak Entity Set (9m)
      · PYQ ×4
      · PQ ×13
  - *Conversion of ER Diagram into Relational Model*
      · Conversion ER Diagram to Relational Model (9m)
      · Fan Trap (4m)
      · Chasm Trap (5m)
      · PYQ ×3
      · PQ ×7
      · PYQ ×9
      · PQ ×38
- **Relational Model & Functional Dependencies**
  - *Basics of Relational Model & Anomalies*
      · Basics of Relational Model (5m)
      · Update Anomalies In Relational Model (6m)
      · Understanding Redundancy In Detail (6m)
      · PYQ ×1
      · PQ ×16
  - *Functional Dependencies & Axioms*
      · What Is Functional Dependency (5m)
      · Understanding Functional Dependency Further (6m)
      · What Is Trivial Functional Dependency (4m)
      · Practice Questions Functional Dependency (2m)
      · Understanding Armstrong's Axioms (9m)
      · PYQ ×5
      · PQ ×5
  - *Attribute Closure & Equivalence of Sets*
      · Closure Set of Attributes (6m)
      · Practice Questions Functional Dependency (7m)
      · Comparing Two Set Of Functional Dependencies (7m)
      · Practice Questions (3m)
      · Practice Questions on Functional Dependencies (1m)
      · Practice Questions Functional Dependency (3m)
      · PQ ×2
  - *Minimal Cover (Canonical Cover)*
      · Minimal Cover Of Functional Dependency (11m)
      · The following functional dependencies hold true for the relational schema (5m)
      · PYQ ×6
      · PQ ×23
- **Keys & Integrity Constraints**
  - *Super Key, Candidate Key & Primary Key*
      · What Is Key (3m)
      · Super Key (5m)
      · Candidate Key (5m)
      · Primary Key (3m)
      · DBMS PRACTICE QUESTIONS (5m)
      · Chap-2_4_2022 (3m)
      · PYQ ×7
      · PQ ×15
  - *Foreign Key & Referential Integrity*
      · Foreign Key (4m)
      · PRACTICE QUESTION (7m)
      · PYQ ×5
      · PQ ×17
  - *Composite & Alternate Keys*
      · Composite Key (2m)
      · PYQ ×1
      · PQ ×3
      · PYQ ×13
      · PQ ×35
- **Normalization (1NF - BCNF)**
  - *Introduction to Normalization & 1NF*
      · Demo: What is Normalisation (5m)
      · First Normal Form (5m)
      · PQ ×7
  - *Second Normal Form (2NF)*
      · Demo: Second Normal Form (8m)
      · PYQ ×4
      · PQ ×7
  - *Third Normal Form (3NF)*
      · Gate 2018 (4m)
      · Demo: Third Normal Form (6m)
      · PYQ ×1
      · PQ ×7
  - *Boyce-Codd Normal Form (BCNF)*
      · BCNF (4m)
      · Practice Questions-1 (6m)
      · Practice Questions-2 (7m)
      · Practice Questions-3 (3m)
      · Practice Questions-4 (3m)
      · PYQ ×5
      · PQ ×20
      · PYQ ×10
      · PQ ×41
- **Decomposition Properties & 4NF**
  - *Multivalued Dependency (MVD) & 4NF*
      · Multivaluated and Functional Dependency Relationship (2m)
      · All About Multivaluated Dependency (8m)
      · Fourth Normal Form (4m)
      · PQ ×3
  - *Fifth Normal Form (5NF)*
      · 5NF (18m)
      · PYQ ×1
      · PQ ×1
  - *Lossless Join Decomposition*
      · Lossy-Lossless Decomposition Using FD (7m)
      · Check for Lossless Decomposition using FD (5m)
      · PYQ ×1
      · PQ ×1
  - *Dependency Preserving Decomposition*
      · Dependency Preserving Decomposition (4m)
      · PQ ×10
      · PYQ ×2
      · PQ ×15
- **File Organization & Indexing**
  - *Basics & Types of Indexing*
      · BackGround of Indexing (5m)
      · What is Indexing (5m)
      · Practice Question -  Primary Indexing (7m)
      · Practice Question - Primary Indexing Cont... (8m)
      · Important Terminology of Indexing (6m)
      · Primary Indexing (3m)
      · Clustered Indexing (9m)
      · Practice Question - Clustered Indexing (2m)
      · Secondary Indexing (7m)
      · Practice question on secondary indexing (8m)
      · Multilevel indexing (7m)
      · PYQ ×11
      · PQ ×10
  - *B-Trees & B+ Trees (Structure & Insertion)*
      · Insertion in B-Tree (7m)
      · Practice question on B Tree Insertion (8m)
      · Reason for B+ Tree (5m)
      · Structure of Nodes in B Tree and B+ Tree (7m)
      · Insertion in B+ Tree Part-1 (8m)
      · Insertion in B+ Tree Part-2 (5m)
      · Deletion From B+ Tree (5m)
      · PYQ ×4
      · PQ ×25
  - *Deletion in B-Trees & B+ Trees*
      · Deletion From B Tree (9m)
      · Practice question on B Tree Deletion (10m)
      · Deletion From B+ Tree (5m)
      · PYQ ×15
      · PQ ×35
- **Relational Algebra**
  - *Introduction to Query Languages*
      · What is Query Language (6m)
      · Basics of Relational Algebra (5m)
      · PQ ×3
  - *Unary Operators (Selection & Projection)*
      · Project Operator (4m)
      · Select Operator (4m)
      · PYQ ×3
      · PQ ×6
  - *Set Operations & Cartesian Product*
      · Set Operators (5m)
      · Cartesian Product In RA (6m)
      · Problem With Cartesian Product (6m)
      · PYQ ×2
      · PQ ×6
  - *Join Operations (Inner & Outer)*
      · Natural Join Operator (4m)
      · Thetha Join-Conditional Join (4m)
      · Outer Join (3m)
      · PYQ ×3
      · PQ ×14
  - *Rename Operation*
      · Rename Operation (6m)
      · PYQ ×1
  - *Division Operator*
      · Division Operator (6m)
      · Implementing Division Operator Using Basic Operators (3m)
      · PYQ ×3
      · PYQ ×12
      · PQ ×29
- **SQL**
  - *Introduction, Components & Structure*
      · Introduction To SQL (7m)
      · Components Of SQL (4m)
      · Basic Structure Of SQL (9m)
      · 720p_2.3 Net 1999 (2m)
      · PYQ ×2
      · PQ ×13
  - *Select, Where, Distinct*
      · Select Clause (5m)
      · Where Clause (6m)
      · Demo: Distinct (7m)
      · PYQ ×4
      · PQ ×12
  - *Datatypes, Operators & Null*
      · SQL Data Types (17m)
      · SQL Operators (5m)
      · Null in SQL (3m)
      · PYQ ×1
      · PQ ×5
  - *DDL, DML, DCL, TCL & Desc*
      · DDL (10m)
      · DML (8m)
      · DCL & TCL (6m)
      · Desc & Show Tables (3m)
      · PYQ ×4
      · PQ ×25
  - *Order By & Rename Operation (Alias)*
      · Order by clause (4m)
      · Rename Operations (8m)
      · PQ ×5
  - *Library Functions (Math, Aggregate, String, Date)*
      · Aggregate Functions (5m)
      · String Operations in SQL (10m)
      · String Function (9m)
      · Numeric & Math Functions (4m)
      · Date & Time Functions (3m)
      · PYQ ×4
      · PQ ×10
  - *Set Operations & Cartesian Product*
      · Set Operations In SQL (4m)
      · Cartesian Product In SQL Part-1 (6m)
      · Cartesian Product In SQL Part-2 (6m)
      · PYQ ×2
      · PQ ×1
  - *Join Operations (Inner & Outer)*
      · Natural Join (5m)
      · Join With Using (2m)
      · Different Versions Of Natual Join (4m)
      · PYQ ×4
      · PQ ×9
  - *Group By Clause*
      · Group by Clause (5m)
      · SQL query (8m)
      · Group By Contd... (19m)
      · PYQ ×2
      · PQ ×7
  - *Nested & Correlated Subqueries*
      · Introduction - Part 1 (5m)
      · Introduction - Part 2 (6m)
      · Correlated Introduction (8m)
      · Practice Question - Corelated Subquery (7m)
      · PYQ ×5
      · PQ ×5
      · PYQ ×28
      · PQ ×92
- **Relational Calculus**
  - *Tuple Relational Calculus (TRC)*
      · Introduction to Tuple  Relational Calculus (6m)
      · Tuple Relational Calculus Practice (9m)
      · PYQ ×1
      · PQ ×6
  - *Domain Relational Calculus (DRC)*
      · Introduction to Domain Relational Calculus (4m)
      · Domain Relational Calculus Practice Questions (4m)
      · Consider the following relational schema. Students( rollno: integer sname: string) (4m)
  - *Safety of Expressions & Power*
      · Power of TRC & Safe TRC (3m)
      · Power of DRC & safe DRC (2m)
      · PQ ×5
      · PYQ ×1
      · PQ ×11
- **Transaction Management**
  - *Introduction & ACID Properties*
      · What is Transaction (6m)
      · Fundamental Operations On DBMS (2m)
      · ACID Properties of Transaction (4m)
      · Isolation Property (4m)
      · Durability Property (3m)
      · Consistency Property (3m)
      · PYQ ×3
      · PQ ×14
  - *Transaction States*
      · Transaction States (7m)
      · PYQ ×1
      · PQ ×2
  - *Concurrency Problems*
      · Problem With Concurrent Execution (5m)
      · Lost Update Problem (5m)
      · Dirty Read Problem (4m)
      · Unrepeatable Read Problem (5m)
      · PYQ ×1
      · PQ ×3
  - *Schedules & Conflict Serializability*
      · What is Schedule (4m)
      · Serial Schedule (5m)
      · Non-Serial Schedule (5m)
      · Conclusion Of Schedule (4m)
      · Conflict Serializable (9m)
      · Conflict Equivalent Schedule (4m)
      · Procedure for determining conflict serializability of a schedule (14m)
      · PYQ ×2
      · PQ ×7
  - *View Serializability*
      · view serializability Part-1 (7m)
      · view serializability Part-2 (8m)
      · Practice Questions on View Serializability (6m)
      · PQ ×1
  - *Recoverability, Cascadeless & Strict Schedules*
      · Recoverable Schedule (5m)
      · Cascadeless Schedule (4m)
      · Strict Schedule (3m)
      · Practice Questions on Recoverability, Cascadeless & Strict Schedules (4m)
      · Practice Question (8m)
      · PQ ×2
      · PYQ ×7
      · PQ ×29
- **Concurrency Control**
  - *Introduction to Concurrency Control*
      · Idea of Concurrency control (8m)
      · PYQ ×1
      · PQ ×2
  - *Timestamp Ordering Protocols*
      · Time stamp protocol part-1 (7m)
      · Time stamp protocol part-2 (4m)
      · Time stamp protocol part-3 (8m)
      · Properties of the stamping protocol (4m)
      · Thomas write Rule (6m)
      · Practice Questions (3m)
      · PYQ ×2
      · PQ ×4
  - *Lock-Based Protocols & Basic 2PL*
      · Locked based protocols (7m)
      · PYQ ×1
      · PQ ×5
  - *Variations of 2PL (Strict, Rigorous, Conservative)*
      · Basic 2PL (8m)
      · Conservative 2PL (7m)
      · Rigorous 2PL (5m)
      · Strict 2PL (3m)
      · PYQ ×1
      · PQ ×1
      · PYQ ×5
      · PQ ×12
      · PYQ ×111
      · PQ ×392
      · Coal India - Unit Test - Databases / DBMS & SQL (45m)

### 3. Paper-2 | Algorithms — 128 vids · 23.0h · 82 PYQs · 249 PQs

- **Algorithm Analysis**
  - *Algo Basics & Analysis*
      · What is Algorithm (5m)
      · Algorithm Development Cycle (6m)
      · Need for Analysis of Algorithm (4m)
      · Types of Analysis (5m)
      · Worst Best Average Case Analysis (7m)
      · Demo: Algorithm Classification (15m)
      · PYQ ×2
      · PQ ×14
  - *Asymptotic Notations*
      · Asymptotic Notations- Big O (9m)
      · Asymptotic Notations- Big Omega (3m)
      · Asymptotic Notations- Big Theta (5m)
      · Small Notations (2m)
      · Properties of Asymptotics Notations (6m)
      · PYQ ×1
      · PQ ×9
  - *Growth Rate Comparisons*
      · Practice Question 1 (11m)
      · Practice Question 2 (4m)
      · Log Basic Properties (13m)
      · Demo: Types of Functions (7m)
      · Decreasing Functions (9m)
      · Constant Functions (5m)
      · Logarithmic Functions (22m)
      · Ignore Logarithm Bases (2m)
      · Polynomial Functions (3m)
      · Exponential Functions (1m)
      · Logarithm Method - Asymptotic Comparison (12m)
      · Practice Questions (33m)
      · PYQ ×1
      · PQ ×7
      · PYQ ×4
      · PQ ×30
- **Time Complexity Analysis**
  - *Iterative Loops & Code*
      · Demo: Basics of Time Complexity (11m)
      · Space Complexity (12m)
      · Loops Time Complexity - 1 (8m)
      · Loops Time Complexity - 2 (22m)
      · Loops Time Complexity - 3 (19m)
      · Loops Time Complexity - 4 (16m)
      · Loops Time Complexity - 5 (17m)
      · Loops Time Complexity - 6 (17m)
      · Loops Time Complexity - 7 (18m)
      · Loops Time Complexity - 8 (12m)
      · Loops Time Complexity - 9 (18m)
      · Loops Time Complexity - 10 (35m)
      · PYQ ×7
      · PQ ×16
  - *Substitution Method*
      · AP and GP Series (29m)
      · Recurrence Relation - 1 (19m)
      · Recurrence Relation - 2 (20m)
      · Recurrence Relation - 3 (26m)
      · Recurrence Relation - 4 (11m)
      · Recurrence Relation - 5 (15m)
      · Recurrence Relation - 6 (18m)
      · Recurrence Relation - 7 (11m)
      · Recurrence Relation - 8 (7m)
      · Recurrence Relation - 9 (4m)
      · Recurrence Relation - 10 (20m)
      · Recurrence Relation - 11 (18m)
      · Recurrence Relation - 12 (14m)
      · Recurrence Relation - 13 (8m)
      · Recurrence Relation - 14 (17m)
      · PYQ ×6
      · PQ ×14
  - *Recursion Tree Method*
      · Divide and Conquer Approach (35m)
      · Recurrence Relation - 1 (27m)
      · Recurrence Relation - 2 (22m)
      · Recurrence Relation - 3 (14m)
      · Recurrence Relation - 4 (19m)
      · Recurrence Relation - 5 (13m)
      · PQ ×4
  - *Master Theorem*
      · Master Theorem Case 1 (12m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Master Theorem Case 2 (4m)
      · Practice Question (3m)
      · Master Theorem Case 3 (5m)
      · Subtract and Conquer (2m)
      · PYQ ×3
      · PQ ×10
      · PYQ ×16
      · PQ ×44
- **Sorting Algorithms**
  - *Introduction to Sorting*
      · Introduction to Sorting Algo (7m)
      · PYQ ×4
      · PQ ×3
  - *Selection Sort*
      · Selection Sort (9m)
      · Analysis of Selection Sort (6m)
      · PYQ ×2
      · PQ ×5
  - *Bubble Sort*
      · Bubble sort (10m)
      · Analysis of Bubble Sort (7m)
      · Practice Questions (1m)
      · PYQ ×2
      · PQ ×1
  - *Insertion Sort*
      · Insertion Sort (10m)
      · Analysis of Insertion Sort (4m)
      · Practice Question (2m)
      · PYQ ×1
      · PQ ×7
  - *Merge Sort*
      · Merge Sort (10m)
      · Analysis of Merge Sort (8m)
      · Practice Question (2m)
      · Practice Question (1m)
      · PYQ ×5
      · PQ ×15
  - *Heap Sort*
      · Heap Sort (10m)
      · Analysis of Heap Sort (5m)
      · PYQ ×2
      · PQ ×1
  - *Quick Sort*
      · Quick sort (8m)
      · Analysis of Quick Sort (4m)
      · Practice Question (2m)
      · Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · Sorting Array_Practice Question (1m)
      · PYQ ×8
      · PQ ×30
  - *Radix & Counting Sort*
      · Demo: Counting Sort (34m)
      · Radix Sort Using Queue (23m)
      · Radix Sort Using Couting Sort (32m)
      · Radix Sort Practice Question (7m)
      · PYQ ×3
      · PQ ×1
  - *Comparisons & Searching*
      · Demo: Linear Search (12m)
      · Straight Binary Search (28m)
      · Recursive Binary Search (22m)
      · Straight Min Max Algorithm (31m)
      · DAC Min Max Algorithm (23m)
      · DAC Min Max Time Complexity (5m)
      · DAC Min Max Count Comparison (17m)
      · Min Max Practice Question (3m)
      · PYQ ×8
      · PQ ×34
      · PYQ ×35
      · PQ ×97
- **Greedy Algorithms**
  - *Greedy Basics & Huffman*
      · Introduction to Greedy Algorithm (7m)
      · Introduction to Huffman Coding (6m)
      · Practice Question (7m)
      · Practice Question (18m)
      · Practice Question (0m)
      · PYQ ×7
      · PQ ×8
  - *Optimal Merge Pattern*
      · Optimal Merge Patern (5m)
      · PYQ ×1
  - *Fractional Knapsack*
      · Knap Sack Problem (13m)
      · PQ ×1
  - *Job & Activity Selection*
      · Job Scheduling Problem (7m)
      · PYQ ×2
      · PQ ×2
      · PYQ ×10
      · PQ ×11
- **Dynamic Programming**
  - *Introduction to DP*
      · Introduction to Dynamic Algorithm (7m)
      · PQ ×8
  - *LCS & Subsequences*
      · Longest commom Subsequence Part-1 (14m)
      · Longest common Subsequence Part-2 (7m)
      · PQ ×5
  - *Matrix Chain Order*
      · Matrix Chain Multiplication Part - 1 (6m)
      · Matrix Chain Multiplication Part - 2 (14m)
      · Matrix chain Multiplication Part - 3 (2m)
      · PYQ ×3
  - *Floyd & Subset Sum*
      · Floyd Warshall Problem (7m)
      · Sum of Subset (7m)
      · PYQ ×6
      · PQ ×11
      · PYQ ×9
      · PQ ×24
- **Minimum Spanning Trees**
  - *MST & Kruskal's Algo*
      · Introduction to Spanning Tree (4m)
      · Kruskal Algo Part-1 (4m)
      · Kruskal Algo Part-2 (6m)
      · PYQ ×1
      · PQ ×4
  - *MST & Prim's Algo*
      · Prim's Algorithm (9m)
      · PYQ ×3
      · PQ ×10
      · PYQ ×4
      · PQ ×14
- **Shortest Path Algos**
  - *Dijkstra’s Algorithm*
      · Dijkastra Algorithm (10m)
      · 2019(2) (3m)
      · PQ ×13
  - *Bellman-Ford Algo*
      · Bellman- Ford Algorithm Part-1 (4m)
      · Bellman- Ford Algorithm Part-2 (6m)
      · Dijakstra and bellaman ford algorithim (5m)
      · DIjakstra algorithim and bellaman ford Practice questions (4m)
      · single source shortest path practice question (4m)
      · Practice Question (1m)
      · Greedy alogrithims (1m)
      · PYQ ×4
      · PQ ×16
      · PYQ ×4
      · PQ ×29
      · PYQ ×82
      · PQ ×249
      · Coal India - Unit Test - Algorithms (45m)

### 4. Paper-2 | Computer Networks & Security — 234 vids · 25.6h · 167 PYQs · 419 PQs

- **Introduction to CN**
  - *Basics & Criteria*
      · Goals and Applications (12m)
      · Evolution (6m)
      · Five components of Data Communication (5m)
      · Effectiveness of DataCommunication (6m)
      · PYQ ×1
      · PQ ×7
  - *Modes & Connections*
      · Transmission Mode in Data Communication (7m)
      · Type of Connection Point-to-Point and Multi-Point (3m)
      · PQ ×7
  - *Network Topologies*
      · Mesh Topology (9m)
      · Star Topology (5m)
      · Bus Topology (4m)
      · Ring Topology (4m)
      · Tree (2m)
      · Hybrid (2m)
      · PYQ ×3
      · PQ ×20
  - *Types of Networks*
      · Types of network (5m)
      · PQ ×6
  - *Switching Techniques*
      · Demo: Circuit Switching (13m)
      · Packet Switching (19m)
      · X Series (7m)
      · PQ ×6
  - *Transmission Media*
      · Transmission Medium (5m)
      · Wireless (6m)
      · PYQ ×1
      · PQ ×6
  - *OSI Model & Layers*
      · Basics of Open System Interconnection OSI model (10m)
      · Working of Open System Interconnection OSI model (7m)
      · Basics of Physical Layer with functionality and duties (4m)
      · Data Link Layer duties, services and functionality (7m)
      · Network Layer duties, services and functionality (4m)
      · Transport Layer duties, services and functionality (6m)
      · Session Presentation Application Layer duties, services (5m)
      · PYQ ×5
      · PQ ×21
      · PYQ ×10
      · PQ ×73
- **Data Communication**
  - *Signals & Metrics*
      · Analog Vs Digital (4m)
      · Period Vs Frequency (3m)
      · Bit Rate Baud Rate (8m)
      · Bandwidht Vs Throughput (4m)
      · Transmission Vs Propogation delay (6m)
      · PYQ ×9
      · PQ ×12
      · PYQ ×9
      · PQ ×12
- **DLL: Access Control**
  - *DLL Overview & MAC*
      · Basics Of Multiple Access Protocol (8m)
      · Fundamentals of Random Access Protocols (5m)
      · PQ ×3
  - *ALOHA Protocols*
      · Pure Aloha Part - 1 (10m)
      · Pure Aloha Part-2 (19m)
      · Practice Question (4m)
      · Practice Question (3m)
      · Practice Question (Throughput) (6m)
      · Slotted Aloha (4m)
      · PYQ ×2
      · PQ ×6
  - *CSMA Variants*
      · CSMA (10m)
      · Persistence Methods in CSMA (11m)
  - *CSMA/CD*
      · CSMA-CD Part - 1 (11m)
      · CSMA-CD Part - 2 (5m)
      · PYQ ×3
      · PQ ×4
  - *CSMA/CA (Wireless)*
      · CSMA-CA Part-1 (4m)
      · CSMA-CA Part-2 (10m)
      · CSMA-CA Part-3 (4m)
      · PYQ ×2
      · PQ ×3
  - *Controlled Access*
      · Reservation - Controlled Access (7m)
      · Polling - Controlled Access Protocol (6m)
      · Token Passing - Controlled Access Protocol (4m)
      · PYQ ×1
      · PQ ×2
  - *Channelization*
      · FDMA - Channelization (4m)
      · TDMA - Channelization (2m)
      · CDMA - Channelization (4m)
      · PQ ×2
      · PYQ ×8
      · PQ ×20
- **DLL: Flow Control**
  - *Basics & Delay Analysis*
      · Basics of Flow Control in Data Link Layer (7m)
      · Simplest Protocol (4m)
      · Stop and Wait Protocol (3m)
  - *Stop-and-Wait ARQ*
      · Stop and Wait Protocol - ARQ (13m)
      · Performance of Stop and Wait Protocol - ARQ (11m)
      · Efficiency of Stop and Wait Protocol - ARQ (6m)
      · PYQ ×3
      · PQ ×4
  - *Go-Back-N Protocol*
      · Go Back N - ARQ (13m)
      · Performance of Go Back N - ARQ (4m)
      · Gate 2008_ (11m)
      · PYQ ×3
      · PQ ×1
  - *Selective Repeat ARQ*
      · Selective Repeat - ARQ (5m)
      · PYQ ×1
      · PQ ×4
      · PYQ ×7
      · PQ ×9
- **DLL: Error Control**
  - *Basics & Hamming Dist*
      · Types of Error - Single Bit Error - Burst Error (6m)
      · Idea of Redundancy for Error Detection (8m)
      · Idea of Block Coding for Error Detection (11m)
      · Basics of Hamming Distance (8m)
      · Minimum Hamming Distance for Error Detection (7m)
      · Minimum Hamming Distance for Error Detection and Correction (7m)
      · PYQ ×6
      · PQ ×7
  - *Linear Block Codes*
      · Basics of One-Dimesional Parity Check (6m)
      · Two-Dimesional Parity Check (5m)
      · Hamming Codes with error detection and Correction Part-1 (12m)
      · Hamming Codes with error detection and Correction Part-2 (5m)
      · PQ ×2
  - *Checksum & CRC*
      · CheckSum Part-1 (6m)
      · CheckSum Part-2 (7m)
      · Cyclic Redundancy Check Part-1 (8m)
      · Cyclic Redundancy Check Part-2 (4m)
      · Cyclic Redundancy Check Using Polynomials Part-1 (6m)
      · Cyclic Redundancy Check Using Polynomials Part-2 (6m)
      · PYQ ×3
      · PQ ×2
      · PYQ ×9
      · PQ ×11
- **DLL: Framing**
  - *Intro & Byte Stuffing*
      · Basics of Framing (5m)
      · Character Oriented Framing (4m)
      · PYQ ×2
      · PQ ×2
  - *Bit Stuffing Algo*
      · Byte Stuffing Strategy (4m)
      · Bit-Oriented Approach (3m)
      · PYQ ×3
      · PQ ×6
      · PYQ ×5
      · PQ ×8
- **Data Link Layer - Ethernet**
  - *Overview and Evolution of Ethernet – IEEE 802.3*
      · Basics of Ethernet (5m)
      · PYQ ×5
      · PQ ×7
  - *Ethernet Frame Format – Preamble, SFD*
      · Preamble and SFD (3m)
      · Destination and Source Address (2m)
      · Length Field (4m)
      · CRC Field in Ethernet (1m)
      · PYQ ×3
      · PQ ×6
  - *Manchester Encoding – G.E. Thomas, IEEE, and Differential Manchester Schemes*
      · Manchester Coding (4m)
      · PYQ ×1
      · PQ ×2
  - *Baud Rate, Bit Rate, and Signal Representation in Ethernet*
      · PYQ ×3
      · PQ ×2
      · PYQ ×12
      · PQ ×17
- **Net Layer: IPv4 & Proto**
  - *Net Layer & IPv4 Basics*
      · Basics Of Network Layer Part - 1 (7m)
      · Basics Of Network Layer Part - 2 (18m)
      · Basics of IPv4 and Datagram Structure (7m)
      · Version Field in IPv4 (3m)
      · Header Length in IPv4 (5m)
      · Service Field in IPv4 (7m)
      · Total Length Field in IPv4 (5m)
      · PYQ ×2
      · PQ ×18
  - *Fragmentation & MTU*
      · Identification Field in IPv4 (3m)
      · Example of Fragmentation (5m)
      · Basics of Fragmentation (6m)
      · Flag Field in IPv4 (5m)
      · Fragmentation Field in IPv4 (8m)
      · PYQ ×2
      · PQ ×7
  - *TTL, Protocol & Checksum*
      · Time-To-Live Field in IPv4 (5m)
      · Protocol Field in IPv4 (2m)
      · Header CheckSum Field in IPv4 (3m)
      · PYQ ×1
      · PQ ×5
  - *IP Options & Padding*
      · Source and Destination Address in IPv4 (2m)
      · Options Field in IPv4 (7m)
      · PQ ×1
  - *Net Layer Protocols*
      · ARP-Address Resolution Protocol (5m)
      · RARP - Reverse Address Resolution Protocol (3m)
      · Basics Of ICMP (4m)
      · ICMP Error Reporting (10m)
      · ICMP - Query Messages (9m)
      · IGMP - Internet Group Message Protocol (4m)
      · PYQ ×2
      · PQ ×13
  - *Congestion & Traffic Shap*
      · PYQ ×1
      · PQ ×2
      · PYQ ×8
      · PQ ×46
- **Net Layer: IP Addressing**
  - *Classful Addr & Casting*
      · Basics of IP Addressing (9m)
      · Notations Of IP Address (4m)
      · Fundamental Of IP Addressing (8m)
      · Class A (9m)
      · Class B (6m)
      · Class C (6m)
      · Class D & E (6m)
      · Types of Casting (8m)
      · PYQ ×8
      · PQ ×22
  - *Subnetting & FLSM Design*
      · Basics of SubNetting (11m)
      · SubNetting Example (5m)
      · Understanding SubNet Mask (6m)
      · Variable Length SubNetting (6m)
      · PYQ ×2
      · PQ ×18
  - *CIDR & VLSM*
      · Address Depletion in ClassFull Addressing (6m)
      · ClassLess Interdomain Routing - CIDR With Example (4m)
      · Rules of Creating CIDR Block (4m)
      · SubNetting In CIDR (4m)
      · CIDR block representation practice question (4m)
      · CIDR Practice Question_ (3m)
      · CIDR Practice Question_ (3m)
      · CIDR Practice Question_ (5m)
      · CIDR Practice Question_ (4m)
      · CIDR Practice Question (8m)
      · Designing subnets for CIDR (5m)
      · PYQ ×5
      · PQ ×4
  - *Supernetting & Spl IPs*
      · Super Netting in ClassFul Addressing (6m)
      · Special Address 127.0.0.1 (2m)
      · Supernetting CIDR (6m)
      · CIDR  supernetting (5m)
      · PYQ ×3
      · PQ ×6
      · PYQ ×18
      · PQ ×50
- **Net Layer:Routing Protocol**
  - *Routing Basics & Flooding*
      · Basics of Routing and Flooding (6m)
      · Static and Dynamic Routing (4m)
      · Basics of Unicast Routing Protocol (6m)
      · Intra-Domain Vs Inter-Domain Routing (4m)
      · PYQ ×8
      · PQ ×3
  - *DVR, RIP & Split Horizon*
      · Basics of Distance Vector Routing (9m)
      · Periodic Vs Triggered Update (4m)
      · Two-Node Loop Instability (6m)
      · Split Horizon (2m)
      · Routing Information Protocol (RIP) (8m)
      · PYQ ×2
      · PQ ×5
  - *LSR, OSPF & Comparison*
      · Link State Routing Part-1 (5m)
      · Link State Routing Part-2 (8m)
      · Open Shortest Path First (OSPF) (6m)
      · PYQ ×8
      · PQ ×8
      · PYQ ×18
      · PQ ×16
- **Transport Layer Services**
  - *Services, Ports & UDP/TCP*
      · Basics of Transport Layer and Duties (9m)
      · Understanding Port Numbers for Service Addressing (7m)
      · Socket Address in Transport Layer Encapsulation Decapsulation (4m)
      · Basics of Transmission Control Protocol (3m)
      · PYQ ×5
      · PQ ×10
  - *TCP Header & Fields*
      · TCP Header-Source-Destination Port Address (4m)
      · TCP Header-Sequence Number-Acknowledgement Number (13m)
      · Idea of Wrap-Around Time (10m)
      · TCP Header-Header Length Field (3m)
      · TCP Header-Check Sum Field (4m)
      · TCP Header-Window Size Field (8m)
      · TCP Header-Urgent Pointer Field (4m)
      · TCP Header-Control Flags (5m)
      · Option Field in TCP Header (4m)
      · PYQ ×3
      · PQ ×6
  - *Conn. Mgmt & Reliability*
      · Three-way Handshaking for TCP Connection Establishment (8m)
      · TCP Connection Termination Three-Way Handshake (4m)
      · SYN Flooding Attack (Denial of Service) (3m)
      · TCP Retransmission (4m)
      · PYQ ×1
      · PQ ×7
  - *TCP State Transition Diag*
      · RFC 793 (10m)
      · PQ ×3
      · PYQ ×9
      · PQ ×26
- **TL: Congestion & UDP**
  - *Congestion Control Policy*
      · Basics of Congestion Control (4m)
      · Basics of Windows in TCP (6m)
      · Congestion Window (3m)
      · Slow Start Phase (Exponential Increase) (6m)
      · Congestion Avoidance Phase (2m)
      · Congestion Detection Phase Phase-1 (4m)
      · Congestion Detection Phase Phase-2 (4m)
      · PYQ ×1
      · PQ ×6
  - *Timers, RTT & SWS*
      · Different timers used in transport layer (7m)
      · Basics of time out timer (4m)
      · Basic Algo for time out Timer (7m)
      · Jacobson Algo for time out timer (8m)
      · Karn's Algorithm for Time out Timer (3m)
      · Silly Window Syndrome & Nagle's Algo (6m)
      · PYQ ×1
      · PQ ×2
  - *UNIX Socket Programming*
      · UNIX Socket API (2m)
      · PYQ ×1
      · PQ ×2
  - *UDP Protocol & Header*
      · User Datagram Protocol (4m)
      · PQ ×8
      · PYQ ×3
      · PQ ×18
- **Application Layer**
  - *Email: SMTP, POP & IMAP*
      · Basics of Application Layer (7m)
      · Email (7m)
      · Electronic Mail Part-1 (9m)
      · Electronic Mail Part-2 (6m)
      · Electronic Mail Part-3 (5m)
      · PYQ ×3
      · PQ ×14
  - *WWW Basics & Cookies*
      · Understanding WWW Architecture (6m)
      · Client-Server Architecture and Uniform Resource Locator (5m)
      · Understanding Cookies (7m)
      · PYQ ×1
      · PQ ×8
  - *HTTP Protocol*
      · Understanding HTTP (4m)
      · Proxy Server and Non-Persistent Vs Persistent Connections (7m)
      · HTTPS (3m)
      · PQ ×12
  - *FTP, DNS & Telnet*
      · Understanding File Transfer Protocol (7m)
      · Domain Name System (5m)
      · Hierarchical Name Space (4m)
      · Telnet (2m)
      · DHCP (5m)
      · PYQ ×2
      · PQ ×20
      · PYQ ×6
      · PQ ×54
- **Hardware Basics**
  - *Repeater, Hub, Bridge & Switch*
      · Demo: Repeater (7m)
      · Hub (6m)
      · Bridge (14m)
      · Switch (13m)
      · PYQ ×1
      · PQ ×8
  - *Router & Gateway*
      · Router (18m)
      · Gateway (15m)
      · PQ ×14
      · PYQ ×1
      · PQ ×22
- **Network Access Technologies**
  - *Wi-Fi*
      · Basics of Wi-Fi (7m)
      · Application of Wi-Fi (3m)
      · Evolution of Wi-Fi (4m)
      · Wi-Fi Network Structure (9m)
      · CSMA / CA (4m)
      · Wi-Fi Security (1m)
      · Advantages of Wi-fi (2m)
      · PQ ×3
      · PQ ×3
- **Network Security**
  - *Basics of Network Security*
      · Basics of Network Security (17m)
      · Security Attacks (10m)
      · Security Services (11m)
      · PYQ ×5
      · PQ ×1
  - *Cryptography*
      · Cryptography (12m)
      · Cryptanalysis (15m)
      · PYQ ×8
      · PQ ×5
  - *Encryption Algorithms*
      · Block & Stream Cipher (8m)
      · DES (6m)
      · DES Analysis (2m)
      · AES (5m)
      · Modes of Operation (18m)
      · RSA (6m)
      · Diffie - Helman (13m)
      · PYQ ×7
      · PQ ×5
  - *Hash & MAC*
      · Hash Function (12m)
      · MD5 (11m)
      · SHA (6m)
      · MAC (6m)
      · PYQ ×1
      · PQ ×2
  - *Digital Security*
      · Digital Signature (10m)
      · Digital Certificate (10m)
      · PYQ ×9
      · PQ ×5
  - *Authentication Security*
      · Authentication Methods (14m)
      · PYQ ×3
      · PQ ×4
  - *Network Security Tools*
      · Firewall (11m)
      · IDS & IPS (5m)
      · VPN (4m)
      · SSL / TLS (3m)
      · PYQ ×11
      · PQ ×12
      · PYQ ×44
      · PQ ×34
      · PYQ ×167
      · PQ ×419
      · Coal India - Unit Test - Computer Networks & Security (45m)

### 5. Paper-2 | Digital Logic — 156 vids · 17.1h · 140 PYQs · 284 PQs

- **Digital Systems & Boolean Basics**
  - *Digital Fundamentals & Boolean Algebra*
      · Blueprint of Digital Electronics (10m)
      · Demo: History of Digital electronics (8m)
      · Advantage of Digital System (9m)
      · History of Digital System (11m)
      · Digital System Designing (13m)
      · Boolean Algebra Laws (12m)
      · De Morgan's Law (2m)
      · PYQ ×7
      · PQ ×16
      · PYQ ×7
      · PQ ×16
- **Logic Gates & Hardware**
  - *Evolution, NOT, OR & AND Gates*
      · basics of logic gates (6m)
      · Not Gate (3m)
      · OR Gate (3m)
      · AND Gate (3m)
      · PYQ ×1
      · PQ ×8
  - *Universal Gates: NAND & NOR*
      · NOR Gate (9m)
      · NAND Gate (6m)
      · PYQ ×2
      · PQ ×12
  - *Ex-OR, Ex-NOR Gate & Relation*
      · EX OR gate (11m)
      · Practice Question_ (1m)
      · EX NOR gate (7m)
      · EX OR gate vs EX NOR gate relationship part 1 (4m)
      · EX OR gate vs EX NOR gate relationship part 2 (5m)
      · PYQ ×7
      · PQ ×14
  - *Logic Families & Hardware*
      · PYQ ×5
      · PQ ×7
      · PYQ ×15
      · PQ ×41
- **Boolean Expression**
  - *SOP & POS Canonical Forms*
      · Basics of Boolean expression (6m)
      · SOP (10m)
      · Canonical SOP form (6m)
      · POS (7m)
      · Canonical POS form (3m)
      · PYQ ×5
      · PQ ×8
  - *Boolean Function Counts*
      · No of Function possible (8m)
      · Complement of a function (9m)
      · Idea of Duality (10m)
      · Neutral functions (3m)
      · Self Dual Functions (4m)
      · How to find Self Dual Functions (7m)
      · Orthogonal Function (4m)
      · No of Orthogonal Function (5m)
      · PYQ ×1
      · PQ ×13
  - *Functional Completeness*
      · Functionally Complete Function (7m)
      · Practice Question (4m)
      · Partially complete Function (3m)
      · Practice Questions (2m)
      · PYQ ×3
      · PQ ×6
  - *Universal Realization*
      · Implementing every gate with NAND Gate (7m)
      · Implementing every gate with NOR Gate (6m)
      · Relationship between AND & OR gates (6m)
      · AND-OR (NAND-NAND Implementation) (5m)
      · OR-AND (NOR-NOR Implementation) (3m)
      · PYQ ×2
      · PQ ×3
      · PYQ ×11
      · PQ ×30
- **Boolean Minimization**
  - *K-Map Structure & PIs*
      · Basics of Simplification (10m)
      · Understanding K MAP part 1 (9m)
      · Understanding K MAP part 2 (10m)
      · Understanding K MAP part 3 (6m)
      · POS K Map (3m)
      · What is minimal Boolean expression (3m)
      · Rules of grouping (14m)
      · Don't care condition (5m)
      · Practice on K Map (7m)
      · More than one solution (4m)
      · Prime Implicant (7m)
      · Practice Question (2m)
      · Practice Questions (3m)
      · Practice Question (3m)
      · Practice Question (4m)
      · Solving K Map in reverse fashion (2m)
      · PYQ ×4
      · PQ ×14
  - *Function Equivalence*
      · Gate 2000_ (3m)
      · gate 2002_ (2m)
      · PYQ ×3
      · PQ ×4
  - *Logic Circuit Analysis*
      · Understanding direct operations on Functions part 1 (5m)
      · Understanding direct operations on Functions part 2 (5m)
      · Irredundant Function (6m)
      · PYQ ×3
  - *Adv. Laws & Optimization*
      · Absorption Law (6m)
      · Practice Question (2m)
      · PYQ ×2
      · PQ ×9
      · PYQ ×12
      · PQ ×27
- **Combinational Circuit**
  - *Adders & Subtractors*
      · Basics of combinational circuit (6m)
      · Fundamental of Adders (8m)
      · Half Adder (8m)
      · Full Adder (9m)
      · Implementing Full Adder Using Half Adder (4m)
      · Half Subtractor (11m)
      · Full Subtractor (33m)
      · PYQ ×8
      · PQ ×14
  - *CLA & Arithmetic Logic*
      · Four-bit Parallel Adder  Ripple Adder (7m)
      · Four-bit Parallel-Ripple Adder-Subractor (7m)
      · Look Ahead Carry Adder (14m)
      · PQ ×3
  - *Multiplexers (MUX)*
      · Basics of Multiplexer (11m)
      · Implementing 2x1 Multiplexer (7m)
      · Implementing 4x1 Multiplexer (5m)
      · Practice Question (2m)
      · Multiplexer Expansion Part-1 (5m)
      · Multiplexer Expansion Part-2 (6m)
      · PYQ ×5
      · PQ ×11
  - *DeMux, Decoder & Encoder*
      · Basics of DeMultiplexer (4m)
      · Implementing 1x2 DeMultiplexer (5m)
      · Implementing 1x4 DeMultiplexer (5m)
      · DEMux_practice_question (2m)
      · Basics of Decoder (8m)
      · Implementing 1x2 Decoder (4m)
      · Implementing 2x4 Decoder (3m)
      · Understanding Decoder Application (4m)
      · Decoder Expansion (3m)
      · Decoders (5m)
      · Decoder_Practice_Question (2m)
      · Decoder (1m)
      · Understanding Encoder (3m)
      · Implementing 2x1 Encoder (4m)
      · Priority Encoder (4m)
      · PYQ ×6
      · PQ ×3
  - *Special Logic Circuits*
      · PYQ ×6
      · PQ ×7
  - *Hazards & Timing*
      · Hazard (16m)
      · static hazard (3m)
      · static hazard_pq (2m)
      · PYQ ×3
      · PQ ×1
      · PYQ ×28
      · PQ ×39
- **Sequential Circuits**
  - *Seq. Logic & Latches*
      · Idea of Sequential Circuits (5m)
      · What are Latches (5m)
      · Nor Latch (12m)
      · NAND Latch (6m)
      · PYQ ×1
      · PQ ×2
  - *Flip-Flops & Conversion*
      · RSSR Flip Flop (15m)
      · Understanding Flip-Flop Triggering (15m)
      · Understanding Flip-Flop Further (5m)
      · JK Flip-Flop (12m)
      · T Flip-Flop (7m)
      · D Flip-Flop (5m)
      · Flip-Flop Conversion (6m)
      · Convert T Flip-Flop To JK Flip Flop (3m)
      · PYQ ×8
      · PQ ×7
  - *Sync Counter Analysis*
      · Basics of Counters (8m)
      · Understanding Counting of a Flip Flop Part-1 (6m)
      · Gate 2001_ (3m)
      · Gate 2000_ (3m)
      · PYQ ×1
      · PQ ×6
  - *Sync Counter Design*
      · Understanding Counting of a Flip Flop Part-2 (4m)
      · Practice Question (29m)
      · Practice Question (3m)
      · PQ ×2
  - *Ripple (Async) Counters*
      · Ripple and Asynchronious Counter (9m)
      · Ripple and Asynchronous Counter Further (7m)
      · Ripple and Asynchronous Counter Using Clock (8m)
      · Synchronous Vs Asynchronous Counter (4m)
      · Self-Staring And Free-Running Counter (4m)
      · Restricted Mode Counter (4m)
      · Restricted Mode Counter further (1m)
      · PYQ ×2
  - *Shift Registers*
      · Basics of register (5m)
      · Serial In Serial Out Register (8m)
      · Serial In Parallel Out Register (3m)
      · Parallel In Serial Out Register (4m)
      · Parallel In Parallel Out Register (2m)
      · Practice Question (2m)
      · PYQ ×1
      · PQ ×2
  - *Ring & Johnson Counters*
      · Ring Counter (5m)
      · Johnson Counter (3m)
      · PYQ ×3
      · PQ ×4
      · PYQ ×16
      · PQ ×23
- **Number System**
  - *Basics & Decimal Convert*
      · Basics of Number System Part-1 (9m)
      · Basics of Number System Part-2 (7m)
      · PYQ ×1
      · PQ ×7
  - *General Base Conversion*
      · Any Base to Decimal (5m)
      · Decimal to Any Base (5m)
      · 720p_5.15 Net 2013 (2m)
      · PYQ ×9
      · PQ ×3
  - *Binary, Octal & Hex*
      · Base 2 Conversion Directly (4m)
      · PYQ ×8
      · PQ ×23
  - *Binary Arithmetic Operations*
      · PYQ ×3
      · PQ ×7
      · PYQ ×21
      · PQ ×40
- **Number Representation**
  - *Basics to 1s Complement*
      · Unsigned Number representation (5m)
      · Basics of Signed Binary Number (5m)
      · Signed Magnitude Representation Part-1 (5m)
      · Signed Magnitude Representation Part-2 (4m)
      · 1's Complement Representation (6m)
      · PQ ×7
  - *2s Complement & Math*
      · 2's Complement Representation (5m)
      · PYQ ×8
      · PQ ×17
  - *BCD & Special Codes*
      · BCD (7m)
      · Excess 3 Code (8m)
      · Gray Code (29m)
      · Gray Code to Binary Code Conversion (9m)
      · PYQ ×10
      · PQ ×22
      · PYQ ×18
      · PQ ×46
- **Floating Point Rep**
  - *Floating Point Basics*
      · Demo: Floating Point Representation (12m)
      · Implicit Normalisation in Floating Point (5m)
      · PYQ ×3
      · PQ ×2
  - *IEEE 754 Standards*
      · IEEE 754 Representation (8m)
      · IEEE 754 Single Precision (5m)
      · Practice Question (1m)
      · Practice Question (4m)
      · Practice Question (5m)
      · Practice Question (4m)
      · PYQ ×4
      · PQ ×16
  - *Booth’s Algorithm*
      · Booth's Algorithm (9m)
      · PYQ ×5
      · PQ ×4
      · PYQ ×12
      · PQ ×22
      · PYQ ×140
      · PQ ×284
      · Coal India - Unit Test - Digital Logic (45m)

### 6. Paper-2 | Operating System — 160 vids · 18.0h · 160 PYQs · 315 PQs

- **Introduction to OS**
  - *OS Basics & Goals*
      · Demo: Introduction to Operating System (13m)
      · What is Operating System (10m)
      · Abstract View of a System (3m)
      · Goals and Functions of OS (5m)
      · PYQ ×1
      · PQ ×11
  - *OS Types & Evolution*
      · Batch Operating System (9m)
      · Spooling (7m)
      · Multiprogramming OS (6m)
      · Multitasking OS (6m)
      · multiprocessing operating system (4m)
      · Types of Multiprocessing Operating System (6m)
      · Real Time Operating System (6m)
      · Types of Real Time Operating System (4m)
      · Distributed Operating System (3m)
      · PYQ ×2
      · PQ ×15
  - *OS Structure & Interface*
      · CLI Vs GUI (5m)
      · Structure of operating system (5m)
      · Micro-Kernel Approach (3m)
      · PYQ ×1
      · PQ ×5
  - *System Calls & Dual Mode*
      · System Call (3m)
      · Mode Bit (3m)
      · PYQ ×1
      · PQ ×9
      · PYQ ×5
      · PQ ×40
- **Process Management**
  - *Process Basics & PCB*
      · Basics of a Process (9m)
      · Process Control Block (5m)
      · PYQ ×5
      · PQ ×8
  - *Process State & Lifecycle*
      · Demo: Process Life Cycle (9m)
      · Process State Diagram (6m)
      · Practice Question (3m)
      · Practice Question (2m)
      · Process (os) Practice Question (1m)
      · Practice Question (1m)
      · System Queues (5m)
      · PYQ ×7
      · PQ ×10
  - *Schedulers & Switching*
      · Schedulers (11m)
      · CPU and IO Bound Process (3m)
      · PYQ ×5
      · PQ ×12
      · PYQ ×17
      · PQ ×30
- **CPU Scheduling**
  - *Basics & Criteria*
      · Pre-emptive Vs Non-Pre-emptive Scheduling (5m)
      · Scheduling Criteria (10m)
      · Terminology for CPU Scheduling (9m)
      · PYQ ×9
      · PQ ×8
  - *FCFS Scheduling*
      · FCFS Scheduling (10m)
      · Practice Question (3m)
      · FCFS Advantage Vs Disadvantage (10m)
      · PYQ ×2
      · PQ ×5
  - *SJF & SRTF Scheduling*
      · SJF Scheduling (10m)
      · SRTF Scheduling (7m)
      · SRTF Advantage Vs Disadvantage (8m)
      · SRTF Implementation (7m)
      · PYQ ×6
      · PQ ×11
  - *Priority Scheduling*
      · Non-Pre-emptive Priority Scheduling (12m)
      · Practice Question (8m)
      · Pre-emptive Priority Scheduling (6m)
      · Priority Scheduling Advantage Vs Disadvantage (6m)
      · PYQ ×7
      · PQ ×5
  - *Round Robin Scheduling*
      · Round Robin Scheduling (12m)
      · Round Robin_Practice (7m)
      · Round Robin Advantage Vs Disadvantage (9m)
      · PYQ ×10
      · PQ ×16
  - *LJF & HRRN*
      · LRTF (4m)
      · HRRN (6m)
      · PQ ×1
  - *Multilevel Queues*
      · Multi Level Queue Scheduling (5m)
      · Multi Level Feedback Queue Scheduling (4m)
      · PYQ ×1
      · PQ ×1
      · PYQ ×35
      · PQ ×47
- **Process Synchronization**
  - *Intro & Critical Section*
      · Race Condition (8m)
      · Critical Section Problem (7m)
      · Criterion to Solve Critical Section Problem (10m)
      · PYQ ×5
      · PQ ×9
  - *Two Process Solutions*
      · Two Process Solution Using Turn Variable (13m)
      · Two Process Solution Using Flag (10m)
      · Peterson Solution using Turn and Flag both (12m)
      · PQ ×7
  - *Semaphores & Ordering*
      · Understanding Semaphore (8m)
      · N Process Solution using Semaphore (8m)
      · Ordering Among Different Process Using Semaphore (8m)
      · Avoiding Deadlock While Using Multiple Semaphore (6m)
      · PYQ ×4
      · PQ ×7
  - *Classical Problems*
      · Understanding Producer Consumer Problem (8m)
      · Producer Consumer Problem Solution using Semaphores (14m)
      · Reader Writer Problem (6m)
      · Reader Writer Problem Solution using semaphore (12m)
      · Dining Philosopher (12m)
      · PYQ ×3
      · PQ ×4
  - *Types of Semaphores*
      · Types of Semaphores (8m)
      · Gate 2008 (4m)
      · PYQ ×5
      · PQ ×4
  - *Hardware Synchronization*
      · Hardware Solution-Disable Interrupt (4m)
      · Hardware Solution-Test & Set (7m)
      · PYQ ×1
      · PQ ×7
      · PYQ ×18
      · PQ ×38
- **Threads & Process Creation**
  - *Fork System Call*
      · Understanding Fork Command (6m)
      · PYQ ×3
      · PQ ×13
  - *Threading & Models*
      · Understanding Threading (4m)
      · Model of Threading (3m)
      · PYQ ×4
      · PQ ×16
      · PYQ ×7
      · PQ ×29
- **Deadlock**
  - *Basics & Conditions*
      · Basics of Deadlock (10m)
      · System Model Which Every Process Will Follow (4m)
      · Necessary Conditions For Deadlock (12m)
      · Deadlock Handling Methods (5m)
      · PYQ ×3
      · PQ ×5
  - *Deadlock Prevention*
      · Understanding Basics of Prevention (5m)
      · Understanding Hold and Wait (5m)
      · No Pre-Emption (3m)
      · Circular Wait (6m)
      · Problem With Prevention (4m)
      · PYQ ×6
      · PQ ×11
  - *Avoidance & Banker's Algo*
      · Understanding Avoidance (8m)
      · Understanding Bankers Algorithm (11m)
      · Safety Algorithm (2m)
      · Resource Request Algorithm (6m)
      · Resource Allocation Graph (7m)
      · PYQ ×6
      · PQ ×14
  - *Detection & Recovery*
      · Deadlock Detection and Recovery (4m)
      · Methods of Recovery (4m)
      · Ignorance Ostrich Algorithm (2m)
      · PYQ ×1
      · PQ ×3
      · PYQ ×16
      · PQ ×33
- **Memory Management**
  - *Basics & Hierarchy*
      · Requirement of Memory Hierarchy (9m)
      · How Memory hierarchy works (9m)
      · Locality of Reference (7m)
      · Duty of Operating System (4m)
      · PYQ ×3
      · PQ ×4
  - *Contiguous Allocation*
      · Contiguous Allocation Policy and Address Translation (9m)
      · Improvement in Address Translation (5m)
      · Basics of Space Allocation in Contiguous Allocation (11m)
      · First Fit Policy (6m)
      · Best Fit Policy (5m)
      · Worst Fit Policy (4m)
      · Next Fit Policy (3m)
      · External Fragmentation (5m)
      · Internal Fragmentation (3m)
      · Conclusion of External Fragmentation (2m)
      · PYQ ×3
      · PQ ×4
  - *Paging & TLB*
      · Basic of Paging (15m)
      · Understanding Paging Further (8m)
      · Logical to Physical Address Translation in Paging (7m)
      · Page Table in Paging (4m)
      · Advantage and Disadvantage of Paging (9m)
      · Address to Memory Translation (10m)
      · Memory to Address Translation (5m)
      · Numerical background of Paging (8m)
      · Numerical of Page Table (7m)
      · Understanding Translation Look Aside Buffer (10m)
      · Disadvantage of TLB (8m)
      · PYQ ×3
      · PQ ×14
  - *Multilevel Paging*
      · Page Size (10m)
      · Multilevel Paging (8m)
      · PYQ ×2
      · PQ ×3
  - *Segmentation & Hybrid*
      · Segmentation (9m)
      · Practice_Question_Os_physical Addressing (2m)
      · Segmentation with Paging (4m)
      · PYQ ×4
      · PQ ×5
      · PYQ ×15
      · PQ ×30
- **Virtual Memory**
  - *Demand Paging Basics*
      · Basics of Virtual Memory and  Pure Demand Paging (8m)
      · Advantage and Disadvatage of Virtual Memory (7m)
      · Understanding Page Fault and Page Fault Service (7m)
      · Performance of Demand Paging (4m)
      · PYQ ×14
      · PQ ×17
  - *FIFO Page Replacement*
      · Understanding Page Replacement (8m)
      · First In First Out Page Replacement Algorithm (7m)
      · BeLady's Anomaly (8m)
      · PYQ ×4
      · PQ ×7
  - *Optimal Replacement*
      · Optimal Page Replacement Algorithm (7m)
      · 720p_8.2 Gate 2007 (2m)
      · PYQ ×3
      · PQ ×2
  - *LRU Page Replacement*
      · Least Recently Used Page Replacement Algorithm (6m)
      · Implementing LRU (4m)
      · PYQ ×4
      · PQ ×3
  - *Stack & Counting Algos*
      · Counting Based Page Replacement (4m)
  - *Thrashing & Allocation*
      · Frame Allocation Policy Equal Allocation (4m)
      · Proportional Allocation (4m)
      · Working Set Strategy (6m)
      · Thrashing (4m)
      · Local Vs Global Replacement (3m)
      · PYQ ×6
      · PQ ×9
      · PYQ ×31
      · PQ ×38
- **Disc Scheduling**
  - *FCFS & SSTF Scheduling*
      · Basics of Magnetic Disk Architecture (7m)
      · First Come First Serve Scheduling (6m)
      · Shortest Seek Time First Scheduling (12m)
      · PYQ ×4
      · PQ ×4
  - *SCAN & C-SCAN Algos*
      · SCAN Scheduling (7m)
      · C-Scan Scheduling (4m)
      · Practice Question (4m)
      · Gate 2015 (4m)
  - *LOOK & C-LOOK Algos*
      · Look Scheduling (3m)
      · C-Look Scheduling (2m)
      · PYQ ×1
      · PQ ×2
      · PYQ ×5
      · PQ ×6
- **File Management**
  - *File Allocation Methods*
      · Basics of File Allocation Methods (3m)
      · Contiguous File Allocation (9m)
      · Linked File Allocation (7m)
      · Index File Allocation (11m)
      · PYQ ×3
      · PQ ×8
  - *Free Space Management*
      · Free Space Management (2m)
      · Bit Vector (3m)
      · Linked List File Management System (2m)
      · PYQ ×1
      · PQ ×3
  - *Directories & Structure*
      · File Access Methods and their types- (15m)
      · Directory and Disk Structure (8m)
      · Directory Structure (9m)
      · Acyclic Graph Directory (9m)
      · General Graph Directory (3m)
      · File System Mounting (5m)
      · File sharing (3m)
      · File System Structure and Implementation- (7m)
      · PYQ ×2
      · PQ ×6
  - *Storage & RAID Management*
      · PYQ ×5
      · PQ ×6
      · PYQ ×11
      · PQ ×23
      · PYQ ×160
      · PQ ×314
      · Coal India - Unit Test - Operating System (45m)

### 7. Paper-2 | Theory of Computation — 186 vids · 19.6h · 75 PYQs · 215 PQs

- **Introduction to TOC**
  - *Basics & String Ops*
      · Introduction to Toc (5m)
      · Requirement Of TOC (6m)
      · What is symbol, Alphabet, String and Language (7m)
      · How to represent a Language (4m)
      · Some basic operations on strings (3m)
      · Reverse of a string (1m)
      · Empty-Null String (2m)
      · Substring (7m)
      · PRACTICE QUESTION STRINGS (2m)
      · Prefix and suffix (3m)
      · Practice question Proper prefixes (2m)
      · Kleene Closure (6m)
      · Practice Question Strings (3m)
      · PYQ ×2
      · PQ ×2
  - *Language Ops & Sets*
      · Set Operations on Languages (4m)
      · Practice Question Language (1m)
      · PQ ×2
      · PYQ ×2
      · PQ ×4
- **Deterministic FA (DFA)**
  - *DFA Basics & Definitions*
      · Basics of Finite Automata (7m)
      · Definition of deterministic Finite Automata (9m)
      · Representation of DFA (5m)
      · Acceptance By a DFA (4m)
      · Practice Question Strings (3m)
      · Practice Question Finite State Machine (1m)
      · PYQ ×2
      · PQ ×4
  - *DFA Construction & Design*
      · DFA Designing where L={a} (4m)
      · DFA Designing where starts with substring s (8m)
      · DFA Designing where string ends with substring ‘s’ (12m)
      · DFA Designing string contains sub string s (6m)
      · DFA Designing string start and end with a (3m)
      · Practice Question Language (2m)
      · DFA Designing string start and end with same symbol (3m)
      · DFA Designing string start and end with different symbol (5m)
      · DFA Designing where starts with s = aaa or bbb (6m)
      · DFA Designing string ends with s = aaa or bbb (8m)
      · DFA Designing sting with substring s = aaa or bbb (4m)
      · Practice Questions Language (4m)
      · DFA Designing sting where |w| = 3, |w| <= 3, |w| >= 3 (6m)
      · DFA Designing sting where number of a = 2 (3m)
      · DFA Designing sting where number of a >= 2 (3m)
      · DFA Designing sting where |w|=0(mod3), |w|=1(mod4) (4m)
      · DFA Designing sting where number of a =0(mod3) (3m)
      · 720p _ 19.1 Gate 2015 (2m)
      · Practice Questions DFA (2m)
      · DFA Designing sting where odd occurance of subsring 'ab' (4m)
      · DFA Designing sting where even occurance of subsring 'baa' (3m)
      · How Many Different DFA's Can Be Designed Part-1 (5m)
      · How Many Different DFA's Can Be Designed Part-2 (5m)
      · Empty Language Acceptance (5m)
      · Universal Language Acceptance (3m)
      · DFA Designing where string contain b as 2nd symbol from left (4m)
      · DFA Designing where string contain b as 2nd symbol fromRight (10m)
      · DFA Designing where string start with a and w=omod3 (7m)
      · DFA Designing where string contain even number of a and b (9m)
      · |a|= 0(mod2) |b|= 0(mod3) |c|= 0(mod5) (2m)
      · DFA Design For String Has a Decimal (6m)
      · Design DFA for Language Part-1 (6m)
      · Design DFA for Language Part-2 (4m)
      · Design DFA for Language Part-3 (5m)
      · Design DFA for Language Part-4 (3m)
      · PYQ ×7
      · PQ ×13
  - *Complement & Minimization*
      · DFA Designing string contains sub string aaa (7m)
      · Basics of Minimization of DFA (10m)
      · Understanding Equal States (7m)
      · Practise Problem on Minimization  Part-1 (6m)
      · Practice Questions (7m)
      · PYQ ×1
      · PQ ×5
      · PYQ ×10
      · PQ ×22
- **Non-Deterministic FA**
  - *NFA Basics & Design*
      · Basics of NDFA (8m)
      · Important Points of NDFA (3m)
      · Acceptance By NDFA (4m)
      · NDFA Designing where starts with substring s (5m)
      · NDFA Designing where every string ends with substring s (7m)
      · NDFA Designing where every string contains  substring s (4m)
      · NDFA Designing where every string starts and ends with same (6m)
      · NDFA where every string starts and ends with different symbo (2m)
      · NDFA where every string starts with aaa or bbb (5m)
      · NDFA where every string of length =w, <=w, >=w (3m)
      · NDFA where every string contains exactly two a (4m)
      · NDFA where 3 symbol from right end is a (5m)
      · Practice Question (2m)
      · PQ ×3
  - *NFA to DFA Conversion*
      · Nfa and Dfa Equivalence (4m)
      · Nfa and Dfa Conversion Example - 1 (10m)
      · Nfa and Dfa Conversion Example - 2 (6m)
      · Nfa and Dfa Conversion Example - 3 (5m)
      · PYQ ×1
      · PQ ×8
  - *Epsilon NFA & Conversion*
      · NFA with Epsilon Moves (6m)
      · Conversion from Epsilon NFA to NFA (12m)
      · Practice Question (3m)
      · PYQ ×1
      · PQ ×3
  - *Regularity & Identification*
      · Regular Language Indetification Part-1 (9m)
      · Regular Language Indetification Part-2 (5m)
      · Regular Language Indetification Part-3 (7m)
      · Regular Language Indetification Part-4 (9m)
      · Regular Language Indetification Part-5 (7m)
      · Regular Language Indetification Part-6 (10m)
      · Regular Language Indetification Part-7 (4m)
      · PQ ×11
      · PYQ ×2
      · PQ ×25
- **Regular Expressions**
  - *Regex Basics & Definitions*
      · Basics of Regular Expressions (10m)
      · Equivalence between two Regular Expressions (5m)
      · Regular Expression to Regular Language (2m)
      · PYQ ×4
      · PQ ×4
  - *Regex Design & Algebra*
      · Regular Language to Regular Expression Part-1 (5m)
      · Regular Language to Regular Expression Part-2 (3m)
      · Regular Language to Regular Expression Part-3 (4m)
      · Regular Language to Regular Expression Part-4 (6m)
      · Regular Language to Regular Expression Part-5 (5m)
      · Regular Language to Regular Expression Part-6 (3m)
      · Regular Language to Regular Expression Part-7 (7m)
      · Regular Language to Regular Expression Part-8 (6m)
      · Regular Language to Regular Expression Part-9 (4m)
      · Algebraic Properties of Regular Expression (9m)
      · Identities of Regular Expression Part-1 (9m)
      · Identities of Regular Expression Part-2 (4m)
      · Practice Questions_RE (2m)
      · Practice Question_Language (1m)
      · PYQ ×3
      · PQ ×11
  - *FA to Regex Conversion*
      · Adern's Theorem (8m)
      · Conversion from Epsilon FA to RE Part-1 (7m)
      · Conversion from Epsilon FA to RE Part-2 (6m)
      · Conversion from Epsilon FA to RE Part-3 (7m)
      · PYQ ×1
      · PQ ×2
  - *Regex & FA Equivalence*
      · Conversion From RE in FA Part-1 (7m)
      · Conversion From RE in FA Part-2 (7m)
      · PYQ ×4
      · PQ ×4
      · PYQ ×12
      · PQ ×21
- **Grammar**
  - *Chomsky & Basics*
      · Definining Formal Grammar (11m)
      · Defining language by grammar (6m)
      · Equivalence between two Grammar (3m)
      · Chomoksy Classification of language (7m)
      · Type 0 Grammar (3m)
      · Type 1 Grammar (6m)
      · Type 2 Grammar (3m)
      · Type 3 Grammar (3m)
      · PYQ ×11
      · PQ ×10
  - *Grammar Design via Regex*
      · Practice Question (5m)
      · Practice Question (4m)
      · Practice Question (4m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Grammar Design form Regular Expression part-1 (6m)
      · Grammar Design form Regular Expression part-2 (7m)
      · Regular grammar to regular expression (5m)
      · Regular grammar to regular expression (4m)
      · PYQ ×1
      · PQ ×3
  - *Regular Grammar & FA*
      · Regular Grammar to Finite Automata (6m)
      · Finite Automata to Regular Grammar (6m)
      · PYQ ×1
      · PQ ×2
      · PYQ ×13
      · PQ ×15
- **Regular Language Properties**
  - *Decidability & Basics*
      · What Computer Science Deals With (5m)
      · Solvable Vs Unsolvable Problem Part-1 (10m)
      · Solvable Vs Unsolvable Problem Part-2 (9m)
      · Decidable Vs Undecidable Problem (5m)
      · P Vs NP Problem (2m)
      · Decision Properties for regular Language (9m)
      · PYQ ×2
      · PQ ×1
  - *Closure Properties*
      · Closure Properties of Regular Language (5m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (9m)
      · PYQ ×3
      · PQ ×12
  - *Pumping Lemma*
      · Pumping Lemma (8m)
      · PYQ ×1
      · PQ ×6
      · PYQ ×6
      · PQ ×19
- **Moore & Mealy Machines**
  - *Basics & Moore Machine*
      · Basic of moore vs mealy Machine (3m)
      · Moore machine (7m)
      · Practice problem on moore machine part-1 (5m)
      · PQ ×1
  - *Mealy Machine*
      · Mealy Machine (5m)
      · Practice Problem on mealy Machine (5m)
      · PQ ×5
  - *Conversion & Equivalence*
      · Conversion form moore to mealy machine (4m)
      · Conversion form mealy machine to moore (6m)
      · PQ ×6
- **Pushdown Automata & CFG**
  - *PDA Design & Basics*
      · Fundamental of CFL and PDA (6m)
      · Formal Definition of DPDA (6m)
      · Push, Pop and Skip Operations (6m)
      · PDA Design Practice Problem Part - 1 (8m)
      · PDA Design Practice Problem Part-2 (7m)
      · Design Practice Problem Part - 3 (5m)
      · PDA Design Practice Problem Part - 4 (7m)
      · PDA Design Practice Problem Part - 5 (4m)
      · Practice Question - 1 (5m)
      · Practice Question - 2 (4m)
      · Practice Question - 3 (4m)
      · PYQ ×1
      · PQ ×9
  - *CFL Identification*
      · CFL Identification - 1 (43m)
      · CFL Identification - 2 (32m)
      · CFL Identification - 3 (20m)
      · CFL Identification - 4 (28m)
      · CFL Identification - 5 (23m)
      · CFL Identification - 6 (21m)
      · CFL Identification - 7 (15m)
      · PYQ ×1
      · PQ ×23
  - *Context-Free Grammars*
      · Linear Grammar (4m)
      · PYQ ×10
      · PQ ×8
  - *Decision Properties*
      · Empty Vs Non-Empty Decision Properties for CFL (6m)
      · Finiteness Vs Infiniteness Decision Properties for CFL (4m)
      · Membership Decison Properties for CFL (9m)
      · decidability  of CFG (2m)
      · PYQ ×1
      · PQ ×4
  - *Closure Properties*
      · Closure Properties  of DCFL vs CFL (3m)
      · PYQ ×4
      · PQ ×19
      · PYQ ×17
      · PQ ×63
- **Turing Machines**
  - *TM Basics & Design*
      · Fundamentals of Turing Machine (6m)
      · Formal Defination of Turing machine with components (8m)
      · Turing Machine Design Practice Problem Part-1 (10m)
      · Turing Machine Design Practice Problem Part-2 (7m)
      · Turing Machine Design Practice Problem Part-3_ (9m)
      · Adding Two Unary Number (6m)
      · Converting Unary to Binary (7m)
      · Turing Machine_Practice Questions_1 (10m)
      · Halting Problem (8m)
      · PYQ ×2
      · PQ ×9
  - *TM Variations & UTM*
      · Versions of Turing Machine (3m)
      · Universal Turing Machine (7m)
      · PYQ ×3
      · PQ ×3
  - *Decision Properties*
      · Decision Properties for RS and REL (1m)
      · PYQ ×1
      · PQ ×21
  - *Closure Properties*
      · Closure Properties for Recursive Set and REL (2m)
      · PYQ ×5
      · PQ ×7
  - *Linear Bounded Automata*
      · LBA (4m)
      · PYQ ×2
      · PYQ ×13
      · PQ ×40
      · PYQ ×75
      · PQ ×215
      · Coal India - Unit Test - Theory of Computation (45m)

### 8. Paper-2 | Computer Organization & Architecture — 139 vids · 15.5h · 108 PYQs · 311 PQs

- **Basics of COA**
  - *Introduction, H/W & S/W*
      · Demo: Introduction to Computer System (12m)
      · PYQ ×1
      · PQ ×4
  - *Input Output Devices*
      · Input and Output Devices (8m)
      · PYQ ×2
      · PQ ×16
  - *Basics of Memory*
      · Units of Memory (7m)
      · Memory (Primary, Secondary, Cache) (7m)
      · SRAM DRAM (7m)
      · ROM (6m)
      · Secondary Memory (4m)
      · PYQ ×1
      · PQ ×45
  - *Evolution & History*
      · Evolution and History (13m)
      · History (4m)
      · PQ ×16
  - *Computer Classification & Flynn’s Taxonomy*
      · Computer Classification (11m)
      · Types of Computers (4m)
      · Von Neumann Architecture (2m)
      · PYQ ×2
      · PQ ×8
  - *CPU Organization Basics*
      · CPU Components (12m)
      · General Operations Order (4m)
      · Types of Registers Part-1 (9m)
      · Types of Registers Part-2 (6m)
      · Register Transfer (6m)
      · Memory Extension (6m)
      · PYQ ×3
      · PQ ×24
  - *Instruction Set Architecture (ISA) & Design*
      · Instruction Set Architecture (ISA) & Design (23m)
      · PQ ×4
  - *Encoding Schemes*
      · Encoding Schemes (7m)
      · PYQ ×1
      · PQ ×12
  - *Types of Software*
      · Types of Software (16m)
      · PQ ×7
  - *Computer Interfaces*
      · Demo: Introduction of Computer Interfaces (13m)
      · Types of Computer Interfaces (9m)
      · Serial Interfaces (13m)
      · Parallel Interfaces (10m)
      · Synchronous & Asynchronous Interfaces (8m)
      · PYQ ×1
      · PQ ×3
      · PYQ ×11
      · PQ ×139
- **Cache Memory Organization**
  - *Memory Chip Configuration*
      · Memory Organization (3m)
      · Memory Chip Configuration (9m)
      · Cell Size Classification (8m)
      · Memory Address Information (2m)
      · Memory Interpretation Mechanism (7m)
      · PYQ ×2
      · PQ ×1
  - *Hierarchy & Locality*
      · Introduction to Memory Hierarchy Part-1 (9m)
      · Introduction to Memory Hierarchy Part-2 (9m)
      · Locality of Reference (7m)
      · Cache Hit, Cache Miss & Mapping Type (5m)
      · PYQ ×8
      · PQ ×10
  - *Units & Cache Mapping Techniques Basics*
      · Units for Memory Management (9m)
      · Cache Mapping Technique (8m)
      · PYQ ×3
      · PQ ×2
  - *Direct Mapping*
      · Direct Mapping Part-1 (7m)
      · Direct Mapping Part-2 (7m)
      · Direct Mapping Part-3 (6m)
      · Practice Question - 1 (3m)
      · Practice Question - 2 (2m)
      · Practice Question - 3 (3m)
      · Practice Question - 4 (3m)
      · PYQ ×3
      · PQ ×3
  - *Associative Mapping*
      · Associative Mapping part-1 (5m)
      · Associative Mapping part-2 (5m)
      · Practice Question - 1 (2m)
      · PYQ ×1
      · PQ ×1
  - *Set Associative Mapping*
      · Set Associative Mapping Part-1 (5m)
      · Set Associative Mapping Part-2 (4m)
      · Practice Question (2m)
      · Practice Questions (4m)
      · Practice Question (Gate 1990) (2m)
      · PYQ ×6
      · PQ ×6
  - *Cache Replacement Policies & Miss Types*
      · Cache replacement policies (2m)
      · FIFO (3m)
      · Optimal (3m)
      · LRU (2m)
      · Miss Type (3m)
      · PYQ ×1
      · PQ ×3
  - *Memory Organisation & Performance*
      · Basics of Memory Organization (3m)
      · Practice Question (2m)
      · PYQ ×8
      · PQ ×4
  - *Coherence & Write Policy*
      · Cache Coherence Problem (5m)
      · PYQ ×3
      · PQ ×1
      · PYQ ×35
      · PQ ×31
- **Input Output Organisation**
  - *Interface & Addressing*
      · Basics of IO Devices and Interface (6m)
      · Data Bus, Address Bus and Control Bus (6m)
      · Memory Mapped IO (6m)
      · Isolated IO (4m)
      · IO Processor (4m)
      · PYQ ×6
      · PQ ×8
  - *Programmed IO*
      · Programmed IO (8m)
      · PQ ×1
  - *Interrupt Driven IO*
      · Interrupt Cycle (13m)
      · Types of Interrupts (11m)
      · Interrupt Priority (6m)
      · Interrupt Initiated IO (7m)
      · PYQ ×8
      · PQ ×12
  - *Direct Memory Access DMA*
      · Direct Memory Access (DMA) (6m)
      · PYQ ×6
      · PQ ×11
  - *Disk Structure & Address*
      · Secondary Memory Transfer Time (10m)
      · Practice Questions (2m)
      · PYQ ×3
      · PQ ×8
  - *Disk Access Time & Performance*
      · Basics of Transfer Time (10m)
      · Practice Questions (6m)
      · Practice Questions (4m)
      · Practice Question (Gate 1993) (3m)
      · Disk Interleaving (4m)
      · PYQ ×5
      · PQ ×7
      · PYQ ×28
      · PQ ×47
- **Pipelining**
  - *Pipelining Basics*
      · Demo: Uniprocessing (6m)
      · Uniprocessing Vs Multiprocessing (4m)
      · IBM 801 Architecture (13m)
      · Basics of Pipelining (8m)
      · Practice Question (8m)
      · Practice Question (2m)
      · PYQ ×1
      · PQ ×5
  - *Performance & Speedup*
      · Speed up Derivation (6m)
      · Clock Per Instruction=1 (4m)
      · Problem with Pipelining (5m)
      · PYQ ×4
      · PQ ×11
  - *Structural & Control Hazards*
      · Structural Hazards (4m)
      · Control Hazards (4m)
      · Solution of Control Hazards (7m)
      · PYQ ×2
      · PQ ×4
  - *Data Hazards & Soln*
      · Data Hazards (4m)
      · Practice Question (Gate 2010) (6m)
      · PYQ ×2
      · PQ ×8
  - *Vector Processing Unit*
      · Vector Processing (6m)
      · How Vector Processing Works (10m)
      · Types of Vector Processing (6m)
      · PYQ ×1
      · PYQ ×10
      · PQ ×28
- **Instr Formats & Modes**
  - *Instruction Structure*
      · 4 Address (5m)
      · 3 Address (3m)
      · 2 Address (3m)
      · 1 Address (3m)
      · 0 Address (2m)
      · Practice Question (3m)
      · Practice Question (3m)
      · Practice Question (2m)
      · PYQ ×2
      · PQ ×5
  - *Basic Addressing Modes*
      · Addressing Modes (5m)
      · Immediate Mode Addressing (4m)
      · Absolute Addressing Mode (4m)
      · Indirect Mode Addressing (4m)
      · Implied Mode (1m)
      · Register Mode (2m)
      · Register Indirect Mode (3m)
      · PYQ ×8
      · PQ ×14
  - *Complex & Rel Modes*
      · Base Register (3m)
      · Index Addressing (2m)
      · PYQ ×5
      · PQ ×3
      · PYQ ×15
      · PQ ×22
- **Control Unit Design**
  - *Instruction Types*
      · IR (10m)
      · Instruction (5m)
      · IR (4m)
      · Memory References (5m)
  - *Hardwired & Microprogrammed CU*
      · Hardwired Control Unit (9m)
      · Microprogrammed Control Unit (7m)
      · Practice Question-1 (4m)
      · Practice Question-2 (8m)
      · PYQ ×3
      · PQ ×6
  - *RISC vs CISC Arch*
      · RISC Vs CISC (7m)
      · PYQ ×1
      · PQ ×7
      · PYQ ×4
      · PQ ×13
- **Programming the Basic Computer**
  - *8085 & 8086 Basics*
      · Demo: 8085 Introduction (11m)
      · 8085 Functional Units (10m)
      · 8085 ISA & AM (6m)
      · 8086 Introduction (14m)
      · PYQ ×3
      · PQ ×27
  - *Computer Instruction*
      · Instruction Codes (15m)
      · Operation Code (14m)
      · Addressing of Operand (15m)
      · Computer Registers (5m)
      · Computer Instructions (3m)
      · PYQ ×1
  - *Assembly & Assembler Design*
      · Computer Languages (8m)
      · Machine Language (5m)
      · Assembly Language Part-1 (9m)
      · Assembly Language Part-2 (12m)
      · Assembler (6m)
      · Types of Assembler (8m)
      · PQ ×1
  - *Program Control & I/O Handling*
      · Program Loop (11m)
      · Subroutine (9m)
      · Input Output Programming (6m)
      · PYQ ×1
      · PQ ×3
      · PYQ ×5
      · PQ ×31
      · PYQ ×108
      · PQ ×311
      · Coal India - Unit Test - Computer Organization & Architecture (45m)

### 9. Paper-2 | Compiler Design — 117 vids · 11.6h · 63 PYQs · 191 PQs

- **Intro to Compilers**
  - *Lang Processing System*
      · Introduction To Compiler Design (3m)
      · What is Preprocessing (5m)
      · What is Compiler (5m)
      · What is Assembling (2m)
      · Loaded and Linker (3m)
      · Compiler Vs Interpreter (6m)
      · History of Compiler (3m)
      · PYQ ×2
      · PQ ×8
  - *Phases of Compiler*
      · Phases of Compiler (9m)
      · PYQ ×6
      · PQ ×7
  - *Sym Table, Errors & Passes*
      · Symbol Table (3m)
      · Compiler  Error Handler (1m)
      · Compiler  passes (3m)
      · PYQ ×5
      · PQ ×9
      · PYQ ×13
      · PQ ×24
- **Lexical Analysis**
  - *Lexical Analysis & Tokens*
      · What is Lexical Analyser (7m)
      · Secondary Functions of Lexical Analyser (3m)
      · Implementation of Lexical Analyser (4m)
      · Token_Practice Questions (2m)
      · PYQ ×4
      · PQ ×27
      · PYQ ×4
      · PQ ×27
- **Grammar & CFG**
  - *Grammar Basics & Chomsky*
      · Introduction to Formal Grammar (11m)
      · Defining Langugae by Grammar (6m)
      · Equivalence Between Grammar (3m)
      · Chomsky Classification of Grammar (7m)
      · Type-0 Grammar (3m)
      · Type-1 Grammar (6m)
      · Type-2 Grammar (3m)
      · Type-3 Grammar (3m)
      · PYQ ×2
      · PQ ×3
  - *Derivation & Recursion*
      · Understanding Derivation of String (3m)
      · Recursive Grammar (5m)
      · Process of making Grammar Compiler Friendly (6m)
      · Removing Left Recursion (6m)
      · Practice Questions (4m)
      · Practice Questions (2m)
      · Practice Questions (6m)
      · PYQ ×1
      · PQ ×3
  - *Ambiguity & Inherent Amb*
      · What is Ambiguous Grammar (4m)
      · What is Inherently Ambiguous Grammar (2) (5m)
      · Practice Questions (4m)
      · Practice Questions (2m)
      · PYQ ×1
      · PQ ×4
  - *Left Factoring & Prefixes*
      · Non-Deterministic Grammar (5m)
      · Converting a Grammar Into Deterministic Grammar (4m)
      · Practice Question (4m)
  - *Simplification of CFG*
      · Simplification of CFG (7m)
      · Removal of Unit Productions (4m)
      · Removal of Useless Symbols (3m)
      · Practice Questions (3m)
      · PYQ ×1
  - *Normal Forms & BNF*
      · Chomsky Normal Form (6m)
      · Greibeck Normal Form (4m)
      · BNF-Backus normal formal (1m)
      · PQ ×3
  - *Decidability & CYK Algo*
      · CYK Algorithim (1m)
      · PQ ×1
      · PYQ ×5
      · PQ ×14
- **Syntax Analysis: Top-Down**
  - *Parser Basics & Top-Down*
      · What is Syntax Analysis (5m)
      · Understanding Top Down Parser (6m)
      · Brute Force Technique (6m)
      · PYQ ×5
      · PQ ×3
  - *First and Follow Sets*
      · Understanding First Function (7m)
      · Practice Problem on First Function (8m)
      · Practice Questions (2m)
      · Understanding Follow Function (7m)
      · Practice Problem on Follow Function (3m)
      · PYQ ×2
      · PQ ×2
  - *LL(1) Parser & Table*
      · Basic Requirement For LL(1) Parser (5m)
      · Designing LL(1) Parser Part-1 (8m)
      · Designing LL(1) Parser Part-2 (6m)
      · Designing LL(1) Parser Part-3 (6m)
      · Block Diagram of LL(1) Parser (7m)
      · Short Cut Techniques for LL(1) Grammar (5m)
      · Practice Question (3m)
      · LL(1)-Practicce question (3m)
      · LL(1)-Practice question (1m)
      · PYQ ×3
      · PQ ×9
      · PYQ ×10
      · PQ ×14
- **Syntax Analysis: Bottom-Up**
  - *Intro to Bottom-Up & LR(0)*
      · Bottom Up Parser Fundamentals Part-1 (8m)
      · Bottom Up Parser Fundamentals Part-2 (5m)
      · Designing LR(O) Parser Part-1 (8m)
      · Designing LR(O) Parser Part-2 (7m)
      · Designing LR(O) Parser Part-3 (6m)
      · Designing LR(O) Parser Part-4 (7m)
      · Designing LR(O) Parser Part-5 (4m)
      · Practice Questions (1m)
      · PYQ ×4
      · PQ ×8
  - *SLR(1) Parser & Conflicts*
      · SLR(1) Praser 1 (5m)
      · Practice Questions (2m)
      · PYQ ×1
      · PQ ×2
  - *CLR(1) Parser & Items*
      · CLR(1) Praser Part-1 (11m)
      · CLR(1) Praser Part-2 (5m)
      · Practice Questions (1m)
      · PYQ ×3
      · PQ ×7
  - *LALR(1) Parser & Merging*
      · LALR(1) Part - 1 (8m)
      · LALR(1) Part - 2 (8m)
      · LALR(1) Part-3 (8m)
      · Gate 2001 (1m)
      · PYQ ×5
      · PQ ×17
  - *Operator Precedence*
      · OPG (3m)
      · PYQ ×5
      · PQ ×12
      · PYQ ×18
      · PQ ×46
- **Semantic Analysis & SDT**
  - *Semantic Analysis & SDT*
      · Basic of Syntax Directed Translation (5m)
      · Practice Question (3m)
      · Practice Question (3m)
      · Practice Question (4m)
      · Practice Question (3m)
      · practice questions (1m)
      · Practice Question (2m)
      · PYQ ×1
      · PQ ×9
  - *Attributes & SDT Types*
      · Classification of Attributes (4m)
      · Types of SDT (3m)
      · PQ ×6
      · PYQ ×1
      · PQ ×15
- **Intermediate Code Gen**
  - *3AC, Quads & Triples*
      · Intermediate Code (6m)
      · DAG Practice Question 1 (5m)
      · DAG Practice Question 2 (5m)
      · DAG Practice Question 3 (6m)
      · DAG Practice Question 4 (3m)
      · DAG Practice Question 5 (4m)
      · 3 Address Code (4m)
      · Representation of 2 Address Code (4m)
      · Fill in Blank (2m)
      · DAG Practice Questions (22m)
      · PYQ ×1
      · PQ ×10
  - *SSA*
      · SSA-SINGLE STATIC ASSINGMENT FORM (2m)
      · SSA - PQ - 1 (13m)
      · SSA PQ - 2 (9m)
      · SSA PQ - 3 (16m)
      · PQ ×4
      · PYQ ×1
      · PQ ×14
- **Code Optimization**
  - *Blocks, Loops & Methods*
      · Optimization (3m)
      · Constant Folding (1m)
      · Constant Propogation (2m)
      · Strength Reduction (2m)
      · Redundant Code Elimination (1m)
      · Algebraic Simplification (1m)
      · Control Flow Analysis (9m)
      · Loop Jamming (4m)
      · Loop Unrolling (4m)
      · C programming Code Movement (2m)
      · PYQ ×4
      · PQ ×14
  - *Liveness Analysis*
      · Compiler  Liveness Analysis (5m)
      · Liveness Analysis (29m)
      · PYQ ×5
      · PQ ×8
      · PYQ ×9
      · PQ ×22
- **Run Time Environment**
  - *Runtime Memory Organization*
      · Memory Organization (44m)
      · Storage Organization (38m)
      · PYQ ×2
      · PQ ×15
      · PYQ ×2
      · PQ ×15
      · PYQ ×63
      · PQ ×191
      · Coal India - Unit Test - Compiler Design (45m)

### 10. Paper-1 | General Awareness — 740 vids · 72.4h · 10 PYQs · 802 PQs

- **Polity**
  - *Historical Background & Constitution Making*
      · Demo: Polity 01 - The Constitution and Its Making (16m)
      · Demo: Making of Indian Constitution (5m)
      · Introduction & Syllabus (14m)
      · Organs of Governance (0m)
      · Constitution , Political Science & State System (1m)
      · Type of Constitution (7m)
      · Constitutional Evolution of India (3m)
      · Constitutional Development in India (11m)
      · Battle of Plassey (West Bengal) & Battle of Buxar (Bihar) (2m)
      · Act (14m)
      · Regulating Act, 1773 & Revised Act of 1781 (2m)
      · Pitt’s India Act, 1784 (3m)
      · Act of 1786 (1m)
      · Charter Act of 1793 (1m)
      · Charter Act of 1813 (2m)
      · Charter Act of 1833 (6m)
      · Charter Act of 1853 & Government of India Act 1858 (7m)
      · Indian Councils Act, 1861 (3m)
      · Act of 1873 & Royal Titles Act, 1876 & Indian Councils Act, 1892 (4m)
      · Indian Councils Act, 1909 (4m)
      · Government of India Act 1919 (9m)
      · Government of India Act 1935 (2m)
      · Indian Independence Act 1947 (3m)
      · Constituent Assembly (3m)
      · Constituent Assembly of India (10m)
      · Formation of the Constituent Assembly (8m)
      · Key Events in the Formation of the Indian Constitution (10m)
      · Major Committees of the Constituent Assembly and their Members (3m)
      · Lord Mountbatten's Plan (4m)
      · Drafting Committee (7m)
      · Reading of the Constitution (3m)
      · First Cabinet of Independent India (1947) (1m)
      · Constitution System of India (3m)
      · PQ ×6
  - *Philosophy of the Constitution*
      · Demo: Preamble of the Constitution (5m)
      · Preamble to the Constitution (11m)
      · Important Cases for Preamble (2m)
      · Important facts of Preamble (2m)
      · Sources of the Indian Constitution (15m)
      · Sources of the Indian Constitution - Canada , Ireland (6m)
      · Sources of the Indian Constitution - Germany , Japan (3m)
      · Sources of the Indian Constitution - Australia , France (2m)
      · Sources of the Indian Constitution - USSR (Russia) , South Africa (3m)
      · PQ ×2
  - *Union, Territory & Constitutional Structure*
      · Schedules of the Indian Constitution (10m)
      · Schedules of Indian Constitution with Related Articles (15m)
      · Main features of the Constitution (3m)
      · Merger of princely states into India (5m)
      · Union and its territory (7m)
      · Classification of States of the Union (1949) (12m)
      · History of State Formation in India (10m)
      · 22 Parts of the Indian Constitution (14m)
      · Basic Structure of the Constitution (1m)
      · Important Facts (1m)
      · Union Territories (2m)
      · Special Powers (5m)
      · Speaker and Deputy Speaker of Lok Sabha (3m)
      · PQ ×8
  - *Citizenship*
      · Citizenship (5m)
      · Indian Citizenship Act 1955 (3m)
      · Indian Citizenship Amendment Act 1986 (1m)
      · Termination of Indian citizenship - Based on the 1955 Act on 3 Grounds (1m)
      · Person of Indian Origin (PIO) Card & Overseas Citizen of India (OCI) Card (2m)
      · PQ ×2
  - *Fundamental Rights, DPSP & Fundamental Duties*
      · Fundamental Rights (4m)
      · DPSP (5m)
      · Fundamental Duties (6m)
      · Polity 02 - Fundamental Duties & Key Amendments (21m)
      · Fundamental Right - General Introduction (4m)
      · Fundamental Right - Constitutional Provisions (2m)
      · Key Fundamental Rights (11m)
      · Right to Equality (Articles 14–18) (14m)
      · Right to Freedom (Articles 19) (6m)
      · Right to Freedom (Articles 20-22) (11m)
      · Right against Exploitation (Articles 23 - 24) & Right to Freedom of Religion (Articles 25-28) (5m)
      · Rights on Culture and Education (Articles 29 - 30) (2m)
      · Right to Constitutional Remedies (Article 32) (7m)
      · Article 32 vs Article 226 (1m)
      · (Article 33) ,(Article 34),(Article 35) (2m)
      · Fundamental Rights (Rights of Citizens and Foreigners vs. Rights Available Only to Citizens) (1m)
      · Supreme Court's Judgment on Amendment of Fundamental Rights (1m)
      · MCQs FD DPSP (8m)
      · State Policy Directive Principles (DPSP) (4m)
      · Article 36 - Definition of State  & Article 37 (2m)
      · Socialist Theory (12m)
      · Gandhian Theory (4m)
      · Articles - 44, 45, 48,49, 50,51 (6m)
      · Difference Between Fundamental Rights and Directive Principles (3m)
      · DPSP MCQ'S (4m)
      · Fundamental Duties (7m)
      · Questions FD (3m)
      · PYQ ×1
      · PQ ×18
  - *Union Govt (Executive & Legislature)*
      · Polity 05 - Qualification of President, PM & Others (12m)
      · Qualification of President (2m)
      · Parliament (2m)
      · PM of India (2m)
      · Union Gov of India (8m)
      · Qualification of Vice President (1m)
      · Council of Minister (1m)
      · Federal Executive (9m)
      · President and Article 54 (8m)
      · Article 55 (5m)
      · Article 56 (1m)
      · Article 58 (1m)
      · Article 59 (0m)
      · Article 60 (1m)
      · Article 61 (4m)
      · Presidential Vacancy (4m)
      · President Salary , Allowances (1m)
      · Key Points (2m)
      · Executive Powers (1m)
      · Legislative Powers (1m)
      · Judicial Powers (2m)
      · Financial Powers (1m)
      · Emergency Powers (1m)
      · Other Powers & List of Presidents (7m)
      · MCQS (8m)
      · Vice President (2m)
      · Qualifications of the Vice President of India (1m)
      · List of Vice Presidents of India (2m)
      · About Vice President (1m)
      · Article 66 Election of the Vice President of India (3m)
      · Article 69 Oath of office of the Vice President (2m)
      · Prime Minister (9m)
      · Types of Ministers (2m)
      · Salary and Allowances of the PM & Functions & Powers of the Prime Minister (1m)
      · Important Points PM (3m)
      · List of Prime Minister of India (12m)
      · Prime Minister MCQS (6m)
      · Council of Ministers MCQS (5m)
      · Parliament (8m)
      · Organs of Parliament (2m)
      · Number of seats in Rajya Sabha and Lok Sabha (2m)
      · Rajya Sabha (Council of States) (7m)
      · Important facts related to Rajya Sabha (6m)
      · Special Powers (5m)
      · Lok Sabha (House of the People) (3m)
      · Lok Sabha & Rajya Sabha – Duration, Dissolution aur Qualifications of Members (4m)
      · Speaker and Deputy Speaker of Lok Sabha (3m)
      · Speaker & Deputy Speaker of Lok Sabha Vacancy  Vacancy Resignation Letter disjunction (1m)
      · Powers and Functions of the Speaker of Lok Sabha (4m)
      · Amendments to the Constitution (3m)
      · Attorney General of India (5m)
      · Advocate General of the State (2m)
      · Comptroller and Auditor General of India (CAG) (7m)
      · Functions of the Comptroller and Auditor General (CAG) of India (2m)
      · PQ ×30
  - *Judiciary & Constitutional Control*
      · Judges of SC, HC & Chief Election Commissioner of India (3m)
      · Judiciary of India (3m)
      · Amendment to the Constitution (2m)
      · About Supreme Court (8m)
      · Article 124 - Establishment and constitution of the Supreme Court structure (8m)
      · Article 124(3) Qualifications of Judges (4m)
      · Article 125 Salaries and allowances of judges (2m)
      · Dismissal of Supreme Court judges. (6m)
      · Important facts (1m)
      · Important Article (8m)
      · About High Court (9m)
      · High Courts under whose jurisdiction comes the State as well as the Union Territories (4m)
      · High Courts under whose jurisdiction 2 or more States are under their jurisdiction (1m)
      · Important Facts (2m)
      · MCQ (13m)
      · PQ ×6
  - *State Government & Local Self-Government*
      · Governor of a State (1m)
      · State Government (3m)
      · CM (1m)
      · Local Gov (Panchayati Raj) (2m)
      · State Part – 6 (5m)
      · Executive of the State (1m)
      · governor (3m)
      · Governor of the State (7m)
      · Powers and functions of the Governor of the State (9m)
      · Constitutional provisions of the Chief Minister and Council of Ministers (4m)
      · MCQ (governor) (4m)
      · MCQ (Chief Minister) (6m)
      · Legislative Council (12m)
      · Assembly (6m)
      · Powers and functions of the Assembly (2m)
      · State Legislative Assemblies (Vidhan Sabha)- Capitals and Number of Seats (1m)
      · Important Officials and Their Salaries (0m)
      · Oath and Resignation Letter (1m)
      · MCQ (8m)
      · Panchayati Raj (6m)
      · History of Panchayati Raj (3m)
      · Major Committees (6m)
      · Attempts at Constitutionalization (0m)
      · 73rd Constitutional Amendment 1993 (4m)
      · Voluntary Provisions & important Articles (10m)
      · Municipal committee (1m)
      · History (Municipality) (1m)
      · 74th Constitutional Amendment, 1992 (0m)
      · Types of Municipalities (1m)
      · Important articles (1m)
      · MCQ Panchayti raj (7m)
      · PQ ×37
  - *Centre–State Relations & Emergency Provisions*
      · Emergency Provisions (1m)
      · Union Territories (2m)
      · Center-State Relations (6m)
      · Conditions of Enactment of Law by the Centre in the State List (1m)
      · Commissions to resolve disputes between the Centre and the States (2m)
      · Official Language or State Language (5m)
      · Emergency Provisions (1m)
      · Article 352 National Emergency (7m)
      · Article 356 & 365 President's Rule (3m)
      · Article 360 Financial Emergency (1m)
      · Constitutional Amendment (2m)
      · Types of Constitutional Amendments (4m)
      · Important Constitutional Amendments of India (Year and Key Provisions) (14m)
      · MCQ (1m)
      · MCQ_1 (3m)
      · PQ ×7
  - *Democracy, Elections & Accountability*
      · Election in India (3m)
      · Constitutional Bodies (1m)
      · Right to Information Act, 2005 (3m)
      · Purpose of the RTI Act (1m)
      · RTI Act Key Definitions (Section 2) (1m)
      · Obligations of Public Authorities (Sec 4) (1m)
      · Request for Information (Sec 6) (3m)
      · RTI Act Time Limits (Sec 7) (5m)
      · Exemptions from Disclosure (Sec 8) (2m)
      · Central Information Commission(Sec12-13) (5m)
      · State Information Commission (Sec 15-16) (0m)
      · Appeal and Penalties (Sec19-20) (2m)
      · RTI Amendment Act, 2019 - Crucial Changes (1m)
      · Removal of Election Commissioners - Sec 14 & 17 (1m)
      · Miscellaneous (Sec 23-24) (0m)
      · Important Sections Checklist (1m)
      · CIC vs SIC (1m)
      · Political Parties and Party System (0m)
      · What is a Political party (1m)
      · Definition of Political Party (1m)
      · Definition by Thinkers (1m)
      · Essential Components of a Party (1m)
      · Political Recruitment (1m)
      · Function - II Policy Formulation (0m)
      · Functions - III: Linkage & Accountability (1m)
      · Function - IV Role of Opposition (1m)
      · Types Of Party Systems (2m)
      · One-Party System Details (0m)
      · Two-Party System Details (1m)
      · Multi-Party System Details (1m)
      · Nature of Indian Party System - I (1m)
      · Nature of Indian Party System - II (1m)
      · Political Spectrum (2m)
      · Regional parties (1m)
      · Legal Basis (1m)
      · Types Of Parties by ECI (1m)
      · National Party Criteria - condition A (2m)
      · National Party Criteria - condition B (2m)
      · National Party Criteria - condition C (1m)
      · Criteria For National Party (1m)
      · State party Criteria - Condition A & B (1m)
      · State party Criteria - Condition C & D (0m)
      · State party Criteria - Condition E (2011 Amendment) (0m)
      · Benefits of Recognition (1m)
      · List of 6 National Parties (1m)
      · Indian National Congress (INC) (1m)
      · Bharatiya Janata Party (BJP) (0m)
      · Bahujan Samaj Party(BSP) (1m)
      · CPI (Marxist) [CPI-M] (0m)
      · National People's Party (NPP) (0m)
      · Aam Aadmi party (AAP) (0m)
      · Revision  (List of 6 National Parties ) (1m)
      · Recognition Of Regional Parties (0m)
      · Anti-Defection Law (Background) (0m)
      · Grounds For Disqualification - I (1m)
      · Grounds For Disqualification - II (0m)
      · Exceptions (Merger) (1m)
      · Deciding Authority (1m)
      · Electoral Reforms Committees (1m)
      · Challenges Criminalization (1m)
      · Challenges Internal Democracy (0m)
      · Challenges Funding (1m)
      · Model code of Conduct (MCC) (1m)
      · Whip System (1m)
      · Summary Political Parties & Party System (1m)
      · Important Amendments & Committees (0m)
      · Introduction - Democracy Definition, Importance, and Characteristics (2m)
      · Classical vs Modern View (1m)
      · Majority Rule with Minority Rights (1m)
      · Two main forms of democracy (2m)
      · Elite theory of Democracy (0m)
      · CharacteristicsFeatures (1m)
      · Political Equality (0m)
      · Independent Judiciary (1m)
      · Fundamental Rights (0m)
      · Constitutionalism & Accountability & Responsibility (0m)
      · Robert Dahl's 'Polyarchy' (0m)
      · Differences between Democracy, Monarchy, and Dictatorship (0m)
      · Democracy in india & Article 326 (1m)
      · Election Commission (Article 324) & Three Pillars of Indian Democracy (1m)
      · Democratic Decentralization (0m)
      · Right to Information (RTI Act, 2005) & Challenges to Indian Democracy – I,II (1m)
      · Democracy Index (Current Data) (1m)
      · Dr. Ambedkar on Democracy & Democracy – Successes and Merits (1m)
      · Accountability  &  Delay in Decision Making (1m)
      · Rule of Amateurs (0m)
      · Substantive vs Procedural Democracy , Deliberative Democracy, Participatory Democracy (2m)
      · Future Of Democracy (0m)
      · Election Commision (13m)
      · Election Commision Structure (1m)
      · Appointment and Tenure (EC & ECI) (4m)
      · Functions and Powers of Election Commission (1m)
      · (Recent Reforms  Initiatives) (2m)
      · ECI Structure & Functions (1m)
      · Key Terminology and Reforms (2m)
      · Electoral System in India (3m)
      · Steps of Election Process (1m)
      · Electoral Reforms & Terminology (2m)
      · Conclusion (Election Commission) (1m)
      · (Major Electoral Reforms)  (Reduction in Voting Age) (0m)
      · Multi-Member Commission (0m)
      · Disclosure of Criminal Records (2m)
      · (EVM and VVPAT) (0m)
      · (NOTA and EPIC) (0m)
      · Other Statutory Reforms (1m)
      · Key Committees (1m)
      · Former Chief Election Commissioner (2m)
      · संवैधानिक, वैधानिक और कार्यकारी संस्थाएँ →Constitutional Bodies, Statutory Bodies, and Executive Bodies (2m)
      · Important Commissions (13m)
      · Structure of NITI Aayog (5m)
      · Important Facts about NITI Ayog (1m)
      · Women's Commission & National Human Rights Commission (7m)
      · Constitution of a National Human Rights Commission (3m)
      · Appointment of Chairman and other members (1m)
      · National Green Tribunal  & Commission for Protection of Child Rights  &  Central Vigilance Commission (5m)
      · National Green Tribunal (1m)
      · Central Information Commission (1m)
      · REPORTS (1m)
      · State information commission (0m)
      · Questions (ECI Appointment) (4m)
      · Questions (8m)
      · Practice Questions (1m)
      · PYQ ×1
      · PQ ×11
  - *Multi-Topic Content (Cross-Concept Material)*
      · Polity 03 - Parliament, Judiciary and State Government (17m)
      · Important Articles of Indian Constitution (25m)
      · Polity 06 - Top 100 Polity Questions for Exams (11m)
      · Polity (1m)
      · PYQs (16m)
      · Important Points (4m)
      · Quesrions (0m)
      · Quesrions 2 (1m)
      · Quesrions 3 (1m)
      · Quesrions 4 (3m)
      · Quesrions 5 (1m)
      · Quesrions 6 (0m)
      · Quesrions 7 (3m)
      · Previous Year & Practice MCQ’s 2 (5m)
      · Previous Year & Practice MCQ’s (4m)
      · Questions (7m)
      · MCQs (4m)
      · MCQs (10m)
      · PQ ×6
      · PYQ ×2
      · PQ ×133
- **Physics**
  - *Motion & Laws of Motion*
      · Demo: 1. Speed, Velocity & Acceleration (23m)
      · Demo: 2. Newton's Laws of Motion (22m)
      · Demo: 3. Momentum & Impulse (7m)
      · 4. Friction (14m)
      · PQ ×4
  - *Gravitation & Properties of Matter*
      · Physics 05 - Gravitation (11m)
      · Physics 06 - Mass, Weight & Acceleration due to Gravity (g) (13m)
      · Physics 07 - ESCAPE VELOCITY (6m)
      · Physics 08 - SATELLITES and ARCHIMEDES’ PRINCIPLE (16m)
      · PQ ×2
  - *Work, Power, Energy & Simple Machines*
      · Physics 09 - Work, Power & Energy (16m)
      · Physics 10 - Work, Power & Energy (13m)
      · PQ ×8
  - *Light & Optics*
      · LIGHT & OPTICS (19m)
      · PQ ×3
  - *Waves & Sound*
      · Sound (16m)
      · Oscillations & Waves and Resonance (19m)
      · PHOTOELECTRIC EFFECT (14m)
      · PQ ×4
  - *Electricity & Magnetism (Electromagnetic Effects)*
      · Electricity (17m)
      · SEMICONDUCTORS & COMMUNICATION and LED (18m)
      · PQ ×2
  - *Heat & Thermal Phenomena*
      · Heat & Thermodynamics (24m)
      · PQ ×1
  - *Applied Physics*
      · MODERN PHYSICS (18m)
      · Physics in daily Life (13m)
      · PQ ×2
  - *Physical Quantities & Measurement*
      · PQ ×1
  - *Multi-Topic Content (Cross-Concept Material)*
      · Physics 20 - PHYSICS MEMORY TRICKS (15m)
      · Physics 21 - Top 100+ Physics Questions for Exams (37m)
      · Defence Technology- Developments and Strategic Importance (Role of DRDO) (10m)
      · Missiles- Types, Features, and Strategic Importance (5m)
      · Ballistic Missiles- Range, Trajectory, and Applications (19m)
      · Agni-V Missile- Features, Range, and Strategic Significance(Part-1) (4m)
      · Agni-V Missile- Features, Range, and Strategic Significance(Part-2) (13m)
      · Agni-P (Agni Prime)- Next-Generation Ballistic Missile (8m)
      · Introduction to Cruise Missiles (6m)
      · Types of Cruise Missiles (4m)
      · Nirbhay- Long-Range Subsonic Cruise Missile of India (6m)
      · Key Points and Important Notes (8m)
      · BrahMos Missile- Supersonic Cruise Missile of India(Part-1) (6m)
      · BrahMos Missile- Supersonic Cruise Missile of India(Part-2) (5m)
      · Shaurya Missile- Features, Range, and Strategic Importance (12m)
      · Other Important Missiles of India (4m)
      · Akash Missile- An Introduction (3m)
      · Submarines (6m)
      · Project 75 (7m)
      · Diesel Electric Submarines (Scorpene Class) (6m)
      · Diesel Electric Submarines (17m)
      · Project 75 (India) (13m)
      · SONAR (7m)
      · Arighat Submarine (8m)
      · Nuclear Powered Submarine in India (2m)
      · SMART Torpedo (6m)
      · Project 15(B) (13m)
      · Project 17(A) (12m)
      · INS Vikrant (5m)
      · Types of warships (8m)
      · Anti Ballistic Defence (15m)
      · Unmanned Aereal Vehical (UAV) (9m)
      · kamikaze (suicide) Drone & NETRA Drone (1m)
      · Tejas Aircraft (2m)
      · Rafale Fighter Jet (3m)
      · Sukhoi 30 Mark 1 (1m)
      · Helicopter in News (6m)
      · PQ ×27
- **Biology**
  - *Cell: Structure & Division*
      · Demo: Biological Classification (12m)
      · Demo: Tissues and Human Anatomy (15m)
      · Cell Introduction (7m)
      · Prokaryotic and Eukaryotic cells (25m)
      · Nucleous (4m)
      · Lysosomes (4m)
      · Mitochondria (3m)
      · Ribosomes (10m)
      · Endoplasmic Reticulam (11m)
      · Golgi Complex (8m)
      · Comparison of RER, SER, and Golgi bodies (6m)
      · Plastids & its types (10m)
      · Vacuole (4m)
      · Pseudo Vacuole (8m)
      · Why Lysosomes is suicidal bag of cell (6m)
      · Difference between Lysosomes & Vacuole (7m)
      · Prokaryotic Cell (12m)
      · Eukaryotic cell, Plant Vs Animal Cell (21m)
      · Cell wall (6m)
      · Prokaryotes i.e Bacteria (9m)
  - *Diversity in Living Organisms*
      · Demo: Microorganisms, Yeast And Their Applications (11m)
      · Biology 13 - Human Heart and Its Working (20m)
      · Nervous System (14m)
      · Excretory System (10m)
      · Nutrition in Plants and Animals (9m)
      · Body System (17m)
      · PYQ ×1
      · PQ ×6
  - *Life Processes*
      · Biology 13 - Human Heart and Its Working (20m)
      · Nervous System (14m)
      · Excretory System (10m)
      · Nutrition in Plants and Animals (9m)
      · Body System (17m)
      · PQ ×13
  - *Reproduction in Living Organisms*
      · Biology 04 - Health, Disease and Reproduction (23m)
      · PQ ×2
  - *Heredity & Genetics*
      · Basics of DNA, RNA, Chromosomes (31m)
      · DNA Vs RNA (6m)
      · Hydrogen bond in DNA (3m)
      · Base Pairing (4m)
      · Chromatin, Gene, DNA, chromatid (10m)
      · Chromosomes (28m)
      · Turner Syndrome and Other Syndromes (24m)
      · LGBTQIA+ (12m)
      · Down Syndrom (5m)
      · Basics of Gender (5m)
      · Ploids (5m)
      · Ploids in Plants (5m)
      · Somatic Cell (4m)
      · Basics of haploids (8m)
      · Concept of Twins (31m)
      · PQ ×2
  - *Evolution & Human Origin*
      · Biology 06 - Darwin’s Theory and Evolution Basics (20m)
  - *Health, Diseases & Immunity*
      · Disease (5m)
      · Skeletal system diseases (3m)
      · Mascular system diseases (4m)
      · Nervous system diseases (8m)
      · Endocrine system diseases (4m)
      · Circulatory system diseases (6m)
      · Lymphetic system diseases (4m)
      · Respiratory system diseases (9m)
      · Digestive system diseases (7m)
      · Urinary system diseases (5m)
      · Reproductive system diseases (8m)
      · Sexually transmitted diseases (1m)
      · Imortant diseases table (27m)
      · Biology 15 - Basics of Plant and Animal Diseases (10m)
      · PQ ×8
  - *Environment & Ecology*
      · Ecology and Diversity of Life final (13m)
      · Biology 09 -  Food Chain And Food Web (11m)
      · Environment and Organism Interactions (12m)
      · Biology and Technology in Daily Life (9m)
      · PQ ×1
  - *Biotechnology*
      · Concept of Cloning (21m)
      · Cloning of Male or Female (20m)
      · Genetic Parent (3m)
      · Biological Parents (4m)
      · Types of cloning (8m)
      · Stem Cell (9m)
      · Artificial Semination (4m)
      · Issue with Cloning (4m)
      · ART & Surrogcy Act, 2021 (7m)
      · How to preserve somatic cell (3m)
      · Three Parent Baby (16m)
      · Mutation (7m)
      · Genetics and Biotechnology (20m)
      · Current Developments in Biology (10m)
      · Basics of DNA, RNA, Chromosomes (31m)
      · Chromatin, Gene, DNA, chromatid (10m)
      · Hydrogen bond in DNA (3m)
      · DNA Vs RNA (6m)
      · Base Pairing (4m)
      · Basics of Gender (5m)
      · Chromosomes (28m)
      · Ploids in Plants (5m)
      · Concept of Twins (31m)
      · Ploids (5m)
      · Basics of haploids (8m)
      · Turner Syndrome and Other Syndromes (24m)
      · LGBTQIA+ (12m)
      · Down Syndrom (5m)
      · Somatic Cell (4m)
      · PQ ×2
  - *Multi-Topic Content (Cross-Concept Material)*
      · Food Production & Revolution (9m)
      · Short Tricks, Types of Leafs and Roots (31m)
      · Top 100 Biology Questions for Exams (31m)
      · PYQ ×1
      · PQ ×34
- **Chemistry**
  - *Fundamentals of Chemistry & States of Matter*
      · PQ ×1
  - *Atomic Structure*
      · Atomic Number, Mass Number, and Important Concepts in Atomic Structure (28m)
      · PQ ×3
  - *Periodic Classification of Elements*
      · Periodic Classification of Elements (15m)
  - *Chemical Bonding & Molecular Structure*
      · Other Important Series and Hacks (43m)
  - *Chemical Reactions, Redox & Electrochemistry*
      · Chemical Reactions and Equations (18m)
      · Balancing Chemical Equations (12m)
      · Important Reactions and Their Uses (8m)
      · PQ ×1
  - *Acids, Bases & Salts*
      · Acid, Base and Salt (13m)
      · PQ ×2
  - *Metals, Non-Metals & Metallurgy*
      · Metals and Non-Matals (22m)
      · PQ ×3
  - *Carbon & Its Compounds*
      · Carbon and Its Compounds (23m)
      · PQ ×2
  - *Applied Chemistry*
      · Surface Chemistry (26m)
      · Chemical Thermodynamics (18m)
      · PQ ×5
  - *Multi-Topic Content (Cross-Concept Material)*
      · Life and Living Organisms – Biology in Chemistry Context (12m)
      · Top 100 Questions for Exams (25m)
      · PQ ×17
- **Static General Knowledge**
  - *Govt Schemes – PMAY, Ayushman, PM-Kisan, Digital & Make in India*
      · Miscellaneous GK 01- Government Schemes, Capitals, HQs (25m)
      · PQ ×3
  - *Global Bodies – UN, WHO, IMF, World Bank, WTO, UNESCO, BRICS, G20, SAARC*
      · PQ ×10
  - *Books & Authors – Wings of Fire, Why Bharat Matters, Truth, White Tiger*
      · PQ ×13
  - *Awards & Honours – Bharat Ratna, Padma Awards, Nobel, Oscars, Booker*
      · Miscellaneous GK 02- Awards, Books, Sports, Wildlife NP (15m)
      · PQ ×12
  - *Sports Highlights – Olympics, ICC, Asian Games,Tennis,Football, Hockey*
      · PYQ ×1
      · PQ ×33
  - *Important Days – Republic Day, Independence Day, Gandhi Jayanti, WED*
      · PQ ×18
  - *Currencies & Capitals – USD, GBP, Yen, Rupee, Yuan of Major Nations*
      · PQ ×2
  - *National Parks – Corbett, Kaziranga, Ranthambore, Gir, Sundarbans*
      · PQ ×4
  - *Airports & Ports – IGI Delhi, Mumbai Port, Chennai Port, Hirakud Dam*
      · PQ ×5
  - *Science & Tech – Chandrayaan-3, Aditya-L1, Gaganyaan, Quantum, 5G*
      · PYQ ×1
      · PQ ×21
  - *Science Facts – DNA, Blood Groups, Photosynthesis, Ozone, Sun Basics*
  - *Environment – Chipko, Project Tiger, Paris Pact, NGT, ISA, COP Meets*
      · PQ ×5
  - *Tech Updates – IndiaAI Compute, AI Kosha, Cyber Refund, EV Platforms*
      · PQ ×1
  - *Climate Policies – Climate Change Impact, Treaties & Key Agreements*
      · PQ ×3
  - *Coal Sector in India: CIL, Coal Types, Coalfields, Mining & Sustainable Development*
      · PQ ×1
  - *National Bodies – RBI, SEBI, NABARD, NITI Aayog, ECI, CAG, UPSC etc.*
      · PQ ×2
      · PYQ ×2
      · PQ ×133
- **GK- Current Affairs**
  - *Daily Current Affairs*
      · PQ ×2
  - *Weekly Current Affairs*
  - *Monthly Current Affairs*
      · PQ ×4
  - *Government Policies & Schemes – Key Policies, Flagship Schemes & Updates*
      · PQ ×10
  - *Committees & Commissions – Key Panels, Reports & Recommendations*
      · PQ ×2
  - *Economic Affairs & Budget – Economy Trends, Policy Measures & Budgeting*
      · PQ ×1
  - *RBI & Monetary Policy – Policy Rates, Reviews & RBI Guidelines*
  - *Banking & Financial Reforms – Reforms, Mergers & Regulatory Changes*
      · PQ ×3
  - *Economic Surveys & Reports – Key Findings, Themes & Insights*
      · PQ ×2
  - *Budget Highlights – Allocations, Priorities & Fiscal Announcements*
      · PQ ×2
  - *Agriculture & Rural Development – Schemes, Reforms & Rural Initiatives*
      · PQ ×5
  - *Social Welfare & Development – Welfare Schemes, Inclusion Measures*
      · PQ ×10
  - *Environment & Climate – Policies, Conservation & Climate Actions*
      · PQ ×3
  - *Infrastructure & Transport – Projects, Corridors & Transport Initiatives*
      · PQ ×3
  - *Defence & Security – Defence Deals, Exercises & Security Measures*
      · PQ ×8
  - *Science & Technology – Innovations, Research & New Technologies*
      · PQ ×12
  - *Cyber Initiatives – Digital Policies, Cybersecurity & IT Updates*
  - *Space Missions – Launches, Satellites & ISRO Missions*
      · PQ ×2
  - *Scientific Discoveries & Innovations – Breakthroughs & Key Findings*
      · PQ ×1
  - *Global Summits & Conferences – Themes, Outcomes & Agreements*
      · PQ ×6
  - *International Relations – Bilateral, Multilateral Events & Diplomacy*
      · PQ ×9
  - *Global Organisations & Governance – UN, WTO, IMF Initiatives & Updates*
      · PQ ×2
  - *Regional Groupings – ASEAN, SAARC, QUAD & Other Alliances*
  - *Global Conflicts & Crises – Major Events, Geopolitical Tensions*
  - *National & International Awards – Recipients, Fields & Highlights*
      · PQ ×3
  - *Sports & Personalities – Tournaments, Achievements & Records*
      · PQ ×22
  - *Major Appointments – New Appointments & Constitutional Positions*
      · PQ ×19
  - *Eminent Personalities & Obituaries – Notable Figures & Tributes*
      · PQ ×2
  - *Books & Authors – New Releases, Notable Authors & Themes*
  - *Important Day Themes – Observances, Themes & Significance*
      · PQ ×3
  - *Government Portals & Digital Initiatives – New Launches & E-Governance*
      · PQ ×6
  - *State-Level Current Affairs – Policies, Schemes & State Updates*
      · PQ ×6
  - *Rankings & Data – National & Global Rankings & Statistics*
      · PQ ×3
  - *New Institute & Organisations–  IIT, AIIMS, Statue, Org.*
      · PQ ×2
  - *Awards & Honours – Bharat Ratna, Padma Awards, Nobel, Oscars, Booker*
      · PQ ×14
  - *International Current News*
      · PQ ×8
  - *First in India/Indian- Launch, Inaugration, Winner, Achievement,Agreement*
      · PQ ×6
  - *Multi-Topic Content (Cross-Concept Material)*
      · PQ ×181
- **History**
  - *History Video Lectures*
      · 1 - Complete History (55m)
      · 2 - [PYQ] History - top 100 Questions of Exams (14m)
  - *Prehistoric India*
      · PQ ×2
  - *Harappan Civilization*
      · PQ ×4
  - *Vedic Age & Religious Developments*
      · PQ ×9
  - *Ancient Empires & Regional States*
      · PYQ ×1
      · PQ ×19
  - *Delhi Sultanate*
      · PQ ×7
  - *Mughal Empire*
      · PQ ×6
  - *Regional Kingdoms after the Mughals*
  - *British Expansion & Early Colonial Rule*
      · PQ ×12
  - *Socio-Religious Reform Movements*
      · PYQ ×1
      · PQ ×3
  - *Revolt of 1857*
      · PQ ×2
  - *British Administration (1858–1947)*
      · PQ ×2
  - *Peasant, Tribal & Workers’ Movements*
      · PQ ×1
  - *Indian National Movement (1885–1947)*
      · PQ ×23
      · PYQ ×2
      · PQ ×90
- **Geography**
  - *Earth, Universe & Fundamentals*
      · Shape and Size of Earth (3m)
      · Rotation, Revolution and Effects (2m)
      · Universe Origin, Big Bang Theory (9m)
      · Planets, Satellites, Asteroids, Comets (10m)
      · Day–Night, Seasons, Tides (7m)
      · Latitudes, Longitudes, Time Calculation (1m)
      · MCQ (0m)
      · PQ ×4
  - *Physical Geography - Earth Structure & Landforms*
      · Geological Structure of India (19m)
      · Movement of the Indian Plate (9m)
      · Major Geological Divisions of India (4m)
      · The Peninsular Block (2m)
      · Geological Composition & Tectonic Stability (7m)
      · Rivers And Drainage (2m)
      · The Himalayas and Other Peninsular Mountains (2m)
      · Landforms (3m)
      · The Indo-Ganga-Brahmaputra Plain (2m)
      · Important Terms And Meaning (2m)
      · Physiography (1m)
      · Overall Physical Characteristics Of India (4m)
      · Major Physiographic Divisions of India (1m)
      · The Northern and North-Eastern Mountains (4m)
      · Dimensions (1m)
      · The Northern Plains (2m)
      · Division (From North To South) (7m)
      · Characteristic Landforms (6m)
      · Meaning of Hard Terms (0m)
      · The Peninsular Plateau (1m)
      · Outer Extent of the Peninsular Plateau (2m)
      · General Features (1m)
      · Divisions of Peninsular Plateau (1m)
      · The Deccan Plateau (7m)
      · Western Ghats (4m)
      · Eastern Ghats (2m)
      · The Central Highlands (2m)
      · Slope and Rivers (2m)
      · The Northern Plateau (1m)
      · Divisions of Meghalaya Plateau (3m)
      · The Indian Desert (4m)
      · The Coastal plains (6m)
      · The Islands (1m)
      · Bay of Bengal Islands (1m)
      · Arabian Sea Islands (2m)
      · Types of Sand Dunes (2m)
      · Mountains, Plateaus, Plains (1m)
      · Crust, Mantle, Core (1m)
      · Questions (1m)
      · MCQ (3m)
      · PQ ×8
  - *Climate & Weather System*
      · Climate And Vegetation (10m)
      · Climate (1m)
      · Factors Determining the Climate of India (4m)
      · Onset of the Monsoon (11m)
      · Onset of the Monsoon II (2m)
      · The Rhythm of Seasons in India (1m)
      · Pressure, Winds & Wind Direction (4m)
      · Seasons & Calendar (1m)
      · Indian and Gregorian Calendar Seasons (3m)
      · Composition and Importance of Atmosphere (2m)
      · Structure and Elements of Atmosphere (4m)
      · Troposphere to Exosphere (4m)
      · Weather vs Climate, Climatic Factors (9m)
      · Climate Zones and Trade Routes (1m)
      · Questions (4m)
      · PQ ×5
  - *Water Bodies & Drainage Systems*
      · Drainage System (4m)
      · Perennial and Ephemeral Rivers & Direction of flow of Rivers (3m)
      · Key Drainage Terms & Relationship between River Basin and Watershed (6m)
      · Classification of Indian Drainage system (3m)
      · Classification Based on Origin and Nature (1m)
      · Drainage Systems of India (1m)
      · The Himalayan Drainage System (1m)
      · Landforms and Characteristics (3m)
      · Dismemberment (Breaking-Up) Of Indo-Brahma River (3m)
      · Tributaries in Detail (1m)
      · The Brahmaputra System (4m)
      · Extent of Usability of River Water (1m)
      · Causes of River Pollution (1m)
      · Important Drainage Patterns (8m)
      · Namami Gange Programme (1m)
      · River Yamuna & its Drainage States (1m)
      · Important River Interlinking and Diversion Schemes (9m)
      · Oceans, Seas and Water Bodies (7m)
      · Major Gulfs, Straits and Canals (6m)
      · Himalayan and Peninsular Rivers (4m)
      · Natural and Artificial Lakes (3m)
      · Practice Question (1m)
      · Practice Question (1m)
      · PQ ×15
  - *Vegetation & Wildlife*
      · Natural Vegetations (16m)
      · Type of Natural vegetation in India (0m)
      · Distribution of Natural Vegetation in India (4m)
      · Classification of Indian Forests (4m)
      · Tropical Evergreen and Semi-Evergreen Forests (4m)
      · Tropical Deciduous Forests (Monsoon Forests) (4m)
      · Tropical Thorn Forests (2m)
      · Montane Forests (1m)
      · Northern Mountain Forests (Himalayas) – Altitudinal Zonation of Natural Vegetation (2m)
      · Important Terms and their Meanings (7m)
      · National Forest Policy of India (3m)
      · Wildlife Conservation in India (4m)
      · List of Biosphere Reserves (4m)
      · International Convention (2m)
      · Major Wildlife Projects (1m)
      · Meaning of Key Terms (2m)
      · Types of Grasslands, Hot & Cold Deserts (5m)
      · Protected Areas and Wetlands (1m)
      · Important Wildlife Species (1m)
      · Ramsar Wetlands of India (1m)
      · PQ ×3
  - *Indian Geography - Core Static*
      · What is Longitude and Latitude (13m)
      · Territorial Limits (2m)
      · Geographical Extent (3m)
      · Reason for difference in North- South and East-West Distance (2m)
      · Latitude and its Effects (9m)
      · Longitudinal Extend and Time Difference (3m)
      · Indian Standard Time (IST) (6m)
      · India's Size In World Context (1m)
      · Sequence of Events and Concepts (1m)
      · Size of India and its Physical Diversity (3m)
      · India's Boundaries and Natural Barriers (3m)
      · The Indian Subcontinent (3m)
      · Mountain Passes and Connectivity (5m)
      · Regional Identity of the Subcontinent (2m)
      · Physical Variations Across India (3m)
      · Peninsular India and Coastline (4m)
      · India and its Neighbours (6m)
      · Overcoming Physical Barriers in Modern Times (3m)
      · Measurement Units of Distance on Land and Sea (3m)
      · Indian Standard Time (IST) and Standard Meridian (6m)
      · Time zones and Global Practice (4m)
      · Do you Remember - School Bhuvan NCERT Portal (5m)
      · Gulf vs Strait (4m)
      · India Shares Land Boundaries with Seven Countries (9m)
      · Location of India (4m)
      · Mainland and Island Territories (1m)
      · Major States and Capitals (1m)
      · Strategic Positions (2m)
      · Location of India in the Eastern World (2m)
      · Standard Meridian of India & India's Global Connectivity (1m)
      · Strategic Maritime Importance & Neighbouring Countries and Water Bodies (2m)
      · Andaman–Nicobar, Lakshadweep (1m)
      · Himalayas, Peninsular Plateau (2m)
      · Crops, Seasons, Irrigation (1m)
      · Location, Extent and Population (5m)
      · Soil Types, Crops, Resources (1m)
      · MCQ (2m)
      · MCQ (3m)
      · Questions (1m)
      · PYQ ×1
      · PQ ×41
  - *Resources & Economic Geography*
      · Major Ports of India (3m)
      · Metallic and Non-Metallic Minerals (1m)
      · Road, Rail, Air and Water Transport (2m)
      · Industries and Population Census (1m)
      · PQ ×16
  - *Natural Disaster & Environmental Geography*
      · Introduction to Natural Disasters (2m)
      · Disasters: Natural and Human-Made (6m)
      · Natural Hazards & Disasters (13m)
      · Disaster Management and Global Efforts (2m)
      · Global Response to Disasters (0m)
      · Earthquakes (4m)
      · Earthquake Zones in India (Based on Damage Risk) (3m)
      · Tsunami (1m)
      · Areas Prone to Tsunamis (3m)
      · Floods (2m)
      · Landslides - Definition & Nature (2m)
      · Causes & Controlling Factors of Landslides (1m)
      · Landslides Vulnerability Zones in India (4m)
      · Drought-Prone Areas in India (3m)
      · Yokohama Strategy and IDNDR (1990 - 2000) (1m)
      · Volcanoes, Earthquakes, Monsoon (1m)
      · Questions (4m)
      · Questions (1m)
      · PQ ×3
  - *Cities, Places & Mapping*
      · Important Cities of India and World (1m)
      · Major Multipurpose Dams (1m)
      · PQ ×11
  - *World Geography*
      · Major Islands of India and World (5m)
      · Physical Overview of Continents (4m)
      · World Capitals and Currencies (4m)
      · International and Interstate Borders (2m)
      · Top 100 Geography Questions for Exams (8m)
      · PQ ×16
      · PYQ ×1
      · PQ ×122
- **Indian Economy**
  - *Nature of Economy – Mixed, Developing, Federal, Open Structure*
      · Key Features of Indian Economy Part 1 (14m)
      · Key Features of Indian Economy Part 2 (8m)
      · Sectors of the Indian Economy (Based on Activity) (9m)
      · Major Features of Indian Economy (4m)
      · Sectors of the Indian Economy (Based on Econmic Activity) (3m)
      · PQ ×3
  - *Basics of Economy – GDP, GNP, NNP, PCI: Definitions & Examples*
      · The Indian Economy 01 - Introduction and Fundamentals of Economics (60m)
      · PQ ×3
  - *Basics of Economy – Inflation, Repo Rate, Fiscal & Current Account Deficit*
      · The Indian Economy 07 - Important Economic Terms and Definitions (40m)
      · Policy Instruments (Monetary Policy) (8m)
      · Tools of Monetary Policy (4m)
      · Fiscal Policy (2m)
      · PQ ×1
  - *Basics of Economy – Post-1991 LPG Reforms & Economic Transition*
      · Economic Reforms in India (10m)
      · Major Phases of Economic Reforms (5m)
      · Key Components of Economic Reforms (8m)
      · Key Achievements of Economic Reforms (2m)
      · Challenges and Limitations (2m)
      · Policy Recommendation  for Sustained Reforms (1m)
  - *Basics of Economy – 5-Trillion Economy: Challenges & Opportunities*
  - *National Income & Growth – Three Methods of GDP Calculation*
  - *National Income & Growth – Gini Coefficient & Lorenz Curve*
  - *Agriculture & Allied Sectors – Share in GDP, Employment, Rural Economy*
      · PQ ×4
  - *Agriculture & Allied Sectors – APMC, e-NAM, MSP Policies & Land Reforms*
      · PQ ×1
  - *Agriculture & Allied Sectors – PM-KISAN, PMFBY, PMKSY & Soil Health Card*
      · PQ ×1
  - *Agriculture & Allied Sectors – Climate-Resilient Farming & Carbon Agriculture*
  - *Agriculture & Allied Sectors – AgriTech, Drones, FPOs & Digital Agriculture*
      · PQ ×1
  - *Agriculture & Allied Sectors – WTO & Agricultural Subsidy Reforms*
  - *Industrial Sector – Industrial Growth Phases & Policy Evolution*
      · PQ ×2
  - *Industrial Sector – Make in India, PLI & Atmanirbhar Bharat*
      · The Indian Economy 04 - GST with EPM and Atmanirbhar Bharat (16m)
  - *Industrial Sector – MSME Policies & Financing*
      · The Indian Economy 03 - Economics Terminologies Part 02 & Budget (16m)
      · PQ ×1
  - *Industrial Sector – Industrial Corridors & Logistics*
  - *Industrial Sector – Disinvestment & Privatisation*
  - *Industrial Sector – Global Value Chains & FDI*
  - *Services Sector – IT, Tourism, Financial & Education Services*
      · PQ ×1
  - *Services Sector – Gig Economy, Freelancers & Platform Workers*
  - *Services Sector – ONDC, Gati Shakti, National Logistics Policy*
  - *Services Sector – Digital Infrastructure – Aadhaar, UPI, DigiLocker*
  - *Services Sector – Data Governance, AI & Automation*
  - *Fiscal Policy & Budget – Revenue, Capital, Deficits*
      · Introduction (4m)
      · Objective of Budget (16m)
      · Components of Budget part 1 (5m)
      · Components of Budget part 2 (1m)
      · Types of Budget (8m)
      · Budget Preparation and Process (3m)
      · Fiscal Policy and Budget (2m)
      · Constitutional Budget (1m)
      · The Indian Economy 02 - Terminologies of Economic Part 01s (14m)
      · PQ ×4
  - *Fiscal Policy & Budget – FRBM Act & Fiscal Rules*
  - *Fiscal Policy & Budget – GST & Tax Structure*
      · PQ ×5
  - *Fiscal Policy & Budget – Finance Commissions (15th–16th)*
      · PQ ×1
  - *Fiscal Policy & Budget – State Finances & Fiscal Federalism*
  - *Fiscal Policy & Budget – Subsidy Rationalisation & Tax Buoyancy*
  - *Fiscal Policy & Budget – Performance-Based Budgeting*
  - *Monetary Policy & RBI – Repo, Reverse Repo, CRR, SLR, MSF, LAF*
  - *Monetary Policy & RBI – Inflation: Types, Causes, Control*
  - *Monetary Policy & RBI – Inflation Targeting & MPC*
  - *Monetary Policy & RBI – Liquidity Management & Monetary Transmission*
  - *Monetary Policy & RBI – CBDC (Digital Rupee), Crypto Regulation*
  - *Monetary Policy & RBI – Interest Rate Corridor Framework*
  - *Banking & Financial System – Types of Banks: PSB, Private, Cooperative*
  - *Banking & Financial System – PMJDY, Mudra, Microfinance*
      · The Indian Economy 06 - Important Government Schemes (23m)
  - *Banking & Financial System – NPAs, IBC & SARFAESI Mechanisms*
  - *Banking & Financial System – Basel Norms & PCA Framework*
  - *Banking & Financial System – FinTech, Digital Lending & Payment Banks*
      · PQ ×1
  - *Banking & Financial System – Capital Markets, SEBI Reforms, ESG Investing*
  - *Planning & Economic Reforms – Five-Year Plans to NITI Aayog*
      · NITI Ayog (Post Five Years Plans ) (3m)
      · Economic Planning and NITI Ayog (4m)
      · Five Years Plans Made in India  Part 1 (16m)
      · PQ ×4
  - *Planning & Economic Reforms – 1991 LPG Reforms*
  - *Planning & Economic Reforms – Atmanirbhar Bharat & Viksit Bharat @2047*
  - *Planning & Economic Reforms – Cooperative Federalism & Aspirational Districts*
      · PQ ×1
  - *Planning & Economic Reforms – Outcome-Based Planning & SDG Localisation*
  - *International Trade & BoP – Current vs Capital Account*
      · PQ ×1
  - *International Trade & BoP – Forex Reserves, NEER/REER*
  - *International Trade & BoP – Export-Import, FTAs, RoDTEP*
      · PQ ×2
  - *International Trade & BoP – Global Value Chains*
  - *International Trade & BoP – Rupee Trade Settlement & De-dollarisation*
  - *FDI, FPI & External Debt – FDI Policy, FPI Trends & External Borrowings*
  - *FDI, FPI & External Debt – External Debt, Debt Service Ratio*
  - *FDI, FPI & External Debt – Sovereign Ratings & Hot-Money Risks*
  - *FDI, FPI & External Debt – FDI in Defence & Infrastructure*
  - *Sustainable Development & Environment – SDGs (India Rank & Progress)*
  - *Sustainable Development & Environment – Green GDP & Circular Economy*
  - *Sustainable Development & Environment – ESG, Carbon Credits & Green Finance*
  - *Sustainable Development & Environment – COP Commitments & NDCs*
  - *Sustainable Development & Environment – Energy Transition & Just Transition*
  - *Employment & Labour – Types of Unemployment*
      · The Indian Economy 05 - Types of Goods in Economics & Index (18m)
  - *Employment & Labour – Labour Codes 2020*
  - *Employment & Labour – MGNREGA, Skill India*
      · PQ ×1
  - *Employment & Labour – Gig Workers & Informalisation*
  - *Employment & Labour – Demographic Dividend & LFPR*
  - *Poverty & Inequality – Poverty Line (Tendulkar, Rangarajan)*
      · Defination and Concept of Poverty (2m)
      · Types of Poverty (7m)
      · Measurements of Poverty (7m)
      · Causes of Poverty in India (7m)
      · Trends in Poverty in India (3m)
      · Poverty Alleviation Policies and Programs (5m)
      · Global Context and Comparisons (3m)
      · Unemployment in India (3m)
      · Types of Unemployment (9m)
      · Causes of Unemployment in India (5m)
      · Measurement of Unemployment in India (2m)
      · Unempolyment Scenario in India (0m)
      · Government Initiatives to Reduce Unemployment (8m)
  - *Poverty & Inequality – MPI (NITI), NRLM, Antyodaya*
  - *Poverty & Inequality – Food Subsidy, FCI, PDS*
  - *Poverty & Inequality – Income vs Multidimensional Poverty Debate*
  - *Poverty & Inequality – Social Protection Floor & Universal Basic Services*
  - *Human Development – HDI, NEP 2020*
  - *Human Development – Health & Education Schemes*
  - *Human Development – Gender Parity Index*
  - *Human Development – Public Health Expenditure Challenges*
  - *Human Development – Human Capital Formation*
  - *Infrastructure & Connectivity – Roads, Ports, Airports (UDAN)*
      · PYQ ×1
      · PQ ×6
  - *Infrastructure & Connectivity – Power Grid, Saubhagya, Urban (AMRUT, Smart Cities)*
  - *Infrastructure & Connectivity – Housing (PMAY), Water (Jal Jeevan Mission)*
  - *Infrastructure & Connectivity – Gati Shakti, National Logistics Policy, NIP*
      · PQ ×1
  - *Infrastructure & Connectivity – PPP Models, InvITs, REITs*
  - *Infrastructure & Connectivity – Energy Transition & Sustainable Infrastructure*
  - *Innovation & Technology – Start-up India, IPR, R&D*
  - *Innovation & Technology – AI, Blockchain, Robotics*
  - *Innovation & Technology – Semiconductor Mission*
  - *Innovation & Technology – Digital Skilling & Cybersecurity*
  - *Population & Urbanisation – Census 2011, Sex Ratio, Dependency Ratio*
      · Demographics of India (4m)
      · Population Composition (6m)
      · Population Growth Rate and Trends (5m)
      · PQ ×10
  - *Population & Urbanisation – Migration & Urban Growth*
      · Migration Patterns (6m)
      · Demographic Challenges (2m)
      · Government Policies Related to Demographics (4m)
      · Opportunities from Demographics (3m)
      · Policy Recommendation (3m)
  - *Population & Urbanisation – Smart Cities & AMRUT*
  - *Population & Urbanisation – Urban Finance & Municipal Bonds*
  - *Population & Urbanisation – Ageing & Social Security*
  - *Global Organisations & Governance – IMF, World Bank, WTO*
  - *Global Organisations & Governance – G20, AIIB, BRICS Bank*
  - *Global Organisations & Governance – Global Minimum Tax & SDR Reforms*
  - *Global Organisations & Governance – India & Global South Cooperation*
  - *Contemporary Economic Issues – Inflation Trends & Causes*
  - *Contemporary Economic Issues – Fiscal Consolidation vs Growth Debate*
  - *Contemporary Economic Issues – Climate Transition & Energy Security*
      · PQ ×1
  - *Contemporary Economic Issues – Digital Economy Taxation*
      · PQ ×1
  - *Contemporary Economic Issues – Post-COVID Growth Recovery*
  - *Multi-Topic Content (Cross-Concept Material)*
      · The Indian Economy 08 - Top 100 Economics Questions for Exams (16m)
      · PYQ ×1
      · PQ ×57
- **Environment**
  - *Sustainable Development – SDGs, Agenda 21,Basic*
      · PYQ ×1
      · PQ ×8
      · PYQ ×1
      · PQ ×8
      · PYQ ×10
      · PQ ×802
      · Coal India - Unit Test - General Knowledge & Awareness (45m)

### 11. Paper-1 | Logical Reasoning — 117 vids · 41.0h · 13 PYQs · 427 PQs

- **Series (Number and Letter Series) (Numerical Relations and Reasoning)**
  - *Basic Concepts and Terminologies*
      · Demo: Types of Series, Question Types, Pre-requisites (14m)
      · Demo: Tricks to Remember Alphabet to Number Mapping (15m)
      · Demo: Story for Reverse Alphabet to Number Mapping (11m)
      · PQ ×1
  - *Number Series*
      · All Possible Series that can be formed (11m)
      · Some Important Observations and Short Tricks (22m)
      · Series with combination (12m)
      · Find the next term (Important Questions) (9m)
      · Important Practice Questions (Part 2) (18m)
      · Brute Force Short Trick for Tough Questions (18m)
      · HOT (Higher Ordered Thinking) Questions (14m)
      · PYQ ×2
      · PQ ×35
  - *Letter or Alphabet Series*
      · Alphabet Series (Important Questions) (15m)
      · Important Practice Questions (Part 3) (11m)
      · Important Practice Questions (Part 4) (15m)
      · PYQ ×2
      · PQ ×18
  - *Alpha-Numeric Series*
      · PQ ×8
  - *Multiple Topics*
      · Find the missing term (Important Questions) (11m)
      · Find the odd one out (Important Questions) (15m)
      · Important Practice Questions (Part 1) (18m)
      · NUMBER AND LETTER SERIES (Revision & Practice Problems) (1.1h)
      · PYQ ×4
      · PQ ×62
- **Coding Decoding**
  - *Basic Concepts, Alphabet–Number Mapping and Base Conversions*
      · Demo: Pre-requisites and Basics Concepts (18m)
      · Demo: Trick for Alphabet to Number Mapping (11m)
      · Demo: Reverse Alphabet to Number Mapping (10m)
      · PYQ ×3
      · PQ ×5
  - *Word or Alphabet based Coding*
      · Type 1 Important Practice Questions (13m)
      · PQ ×18
  - *Number Based Coding*
      · Type 2 Important Practice Questions (6m)
      · PQ ×7
  - *Alphabet, Word, Number based Coding (Mixed Patterns)*
      · Type 3.1 Important Practice Questions (14m)
      · Type 3.2 Important Practice Questions (12m)
      · PQ ×3
  - *Symbols based Coding*
      · Type 4 Important Practice Questions (14m)
      · PQ ×9
  - *Language Translation Coding (Chinese Coding) (Sentence Based Coding)*
      · Type 5.1 Important Practice Questions (19m)
      · Type 5.2 Important Practice Questions (14m)
      · PQ ×1
  - *Renaming Based Coding (Object Substitution)*
      · Type 6.1 Important Practice Questions (19m)
      · Type 6.2 Important Practice Questions (11m)
      · Type 6.3 Important Practice Questions (11m)
      · PQ ×1
  - *Pair, Group, Relationship-Based and Miscellaneous Coding*
      · Some Important Miscellaneous Problems (13m)
      · PQ ×1
  - *Multiple Topics*
      · A Very HOT Question [MUST SOLVE] (27m)
      · Quick Revision & Practice Problems (1.3h)
      · PYQ ×3
      · PQ ×45
- **Non Verbal Reasoning (Spatial Aptitude) (Spatial Reasoning) (Visual Reasoning)**
  - *Image Analysis and Rotation Problems*
      · Demo: Image Analysis (15m)
      · PQ ×5
  - *Translation*
  - *Scaling*
  - *Mirror and Water Images*
      · Demo: Mirror Images (14m)
      · Demo: Water Images (13m)
      · PQ ×15
  - *Grouping, Assembling and Shape Construction*
      · Group of Images (14m)
      · Shape Construction (15m)
      · PQ ×5
  - *Paper Folding and Paper Cutting*
      · Paper Cutting (16m)
      · Paper Folding (12m)
      · PQ ×3
  - *Dot Situation Problems*
      · Dot Situation (15m)
  - *Series & Pattern Recognition (Patterns in 2D) (Symbol Series)*
      · Series (25m)
      · PQ ×12
  - *Patterns in 3D*
      · PQ ×1
  - *Classification (Odd-One-Out)*
      · Classification (17m)
      · PQ ×22
  - *Embedded and Hidden Figures*
      · Embedded Images (15m)
  - *Figure Matrix (Figure Analogy)*
      · Figure Matrix (16m)
      · PQ ×3
  - *Rule Detection (Logical Pattern Rules)*
      · Rule Detection (12m)
      · PQ ×1
  - *Pattern Completion & Figure Completion*
      · Pattern Completion (10m)
      · PQ ×6
  - *Multiple Topics*
      · Spatial Aptitude - Concepts, Short Tricks & Questions (33m)
      · Visual Reasoning (2m)
      · PQ ×73
- **Data Interpretation**
  - *Basic Concepts & Terminologies*
      · Demo: Pre-requisites & Basic Concepts (7m)
      · Demo: Types of Graphs (11m)
      · Demo: Tricks Ratio to Percentage Table (22m)
      · Ratio - Percentage Conversion (12m)
  - *Table Graph*
      · Table Graph (Part 1) (25m)
      · Table Graph (Part 2) (8m)
      · PYQ ×1
      · PQ ×2
  - *Bar Graph*
      · Bar Graph (8m)
      · PQ ×1
  - *Pie Chart (Pie Graph)*
      · Pie Chart (Pie Graph) (14m)
      · PQ ×3
  - *Line Graph*
      · Line Graph (Part 1) (9m)
      · Line Graph (Part 2) (7m)
      · PQ ×2
  - *2D-3D Plots and Maps*
  - *Caselet / Paragraph DI*
  - *Multiple Topics*
      · PYQ ×1
      · PQ ×8
- **Blood Relations**
  - *Multiple Topics*
      · Concepts, Short Tricks & Questions (1) (1.2h)
      · Concepts, Short Tricks & Questions (2) (2.0h)
  - *Basics and Family Tree*
      · PYQ ×1
      · PQ ×19
  - *Coded Blood Relation*
      · PQ ×6
  - *Indicating Blood Relation*
      · PQ ×8
      · PYQ ×1
      · PQ ×33
- **Syllogisms**
  - *Basic Syllogism*
      · Concepts, Short Tricks & Questions (Part 1) (1.0h)
      · Venn Diagram Concepts for Syllogism (9m)
      · PYQ ×1
      · PQ ×20
  - *Advance Syllogism*
      · Concepts, Short Tricks & Questions (Part 2) (1.6h)
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×1
      · PQ ×22
- **Deductive and Inductive Reasoning (Logical Deduction and Induction) (Prepositional Reasoning)**
  - *Statement and Conclusion*
      · Statement & Conclusion (Part 1) (32m)
      · Statement & Conclusion (Part 2) (22m)
      · PQ ×7
  - *Statement and Arguement*
      · Statement & Argument (26m)
      · PQ ×5
  - *Statement and Assumption*
      · Statement & Assumption (11m)
      · PQ ×6
  - *Statement and Course of Action*
      · Statement & Course of Action (10m)
      · PQ ×11
  - *Assertion and Reasoning*
  - *Inference*
      · PQ ×8
  - *Cause and Effect*
      · PQ ×4
  - *Multiple Topics*
      · PQ ×41
- **Selection Decision Table (Decision Making)**
  - *Basic Selection Decision Table (Decision Making)*
      · Introduction (6m)
      · Practice Questions (1) (21m)
      · Practice Questions (2) (16m)
      · Practice Questions (3) (18m)
      · Practice Questions (4) (20m)
      · Practice Questions (5) (18m)
      · Decision Making - Concepts, Short Tricks & Questions (18m)
      · PQ ×7
  - *Advance Selection Decision Table (Decision Making)*
      · PQ ×3
  - *Multiple Topics*
      · PQ ×10
- **Clock**
  - *Basic Concepts and Clock Mechanics*
      · Basic Concepts, Short Tricks & Questions (45m)
      · Important Practice Questions (36m)
      · PQ ×3
  - *Angle Between Hands*
  - *Mirror Image of Clock Time*
  - *Water Image of Clock Time*
  - *Miscellaneous Clock Problems*
      · PQ ×2
  - *Multiple Topics*
      · PQ ×5
- **Calendar**
  - *Basics of Calendar (Year, Month, Week, Day System)*
      · Weightage & Pre-Introduction (3m)
      · Basic Concepts & Short Tricks (9m)
      · Leap Year  Concepts & Tricks (7m)
      · Short Trick for Breaking Year into Pieces (6m)
      · Leap Year Calendar Repeats after 28 years (13m)
      · PQ ×3
  - *Finding Day on a Given Date*
      · Short Trick Find Day on a Particular Date (8m)
      · Question Find Day on a Particular Date (5m)
      · Short Trick Find Day on a Particular Date (8m)
      · Short Trick Find Day on a Particular Date (9m)
      · Formula Find Day on a Particular Date (10m)
      · Formula Find Day on a Particular Date (8m)
      · PQ ×4
  - *Date – Date Relationship (4 Categories Method)*
      · Category 1 & 2 Find Day on Particular Date (12m)
      · Category 3 Find Day on a Particular Date (13m)
      · Category 4 Find Day on a Particular Date (7m)
      · PQ ×1
  - *Month Replication and Same Calendar Problems*
      · Which 2 months in a year has same Calendar (15m)
      · Short Trick Same Calendar in 2 Years (7m)
      · Short Trick Same Calendar in 2 Years (7m)
      · PQ ×1
  - *Formulas and High - Yield Questions*
      · Practice Questions & Short Tricks (14m)
      · Practice Questions & Short Tricks (11m)
      · Practice Questions & Short Tricks (11m)
      · Important Practice Questions & Short Tricks (7m)
      · Important Practice Questions & Short Tricks (6m)
      · Important Practice Questions & Short Tricks (6m)
      · Important Practice Questions & Short Tricks (6m)
      · Quick Revision, Short Tricks & Questions (1.0h)
  - *Multiple Topics*
      · PQ ×9
- **Cubes & Dices**
  - *Basic Concepts & Properties*
      · PQ ×1
  - *Closed Dice*
      · Closed Dice Tricks & Questions (29m)
      · PQ ×2
  - *Cubes and Open Dice*
      · Cubes & Dice (Part 1) (11m)
      · Cubes & Dice (Part 2) (19m)
      · PQ ×1
  - *Painted & Cut Cube Problems, Rotation & Comparison of Dice*
      · Painted & Cut Cube Problems (42m)
      · Dice (31m)
      · PQ ×2
  - *Multiple Topics*
      · PQ ×6
- **Directions (Direction Test)**
  - *Basic Concepts, Terminologies and Formulas*
      · Concepts, Short Tricks & Questions (1) (1.0h)
      · Concepts, Short Tricks & Questions (2) (1.4h)
  - *Distance based Questions*
  - *Direction based Questions*
      · PQ ×8
  - *Distance and Direction Mixed Questions*
      · PQ ×9
  - *Shadow*
      · PQ ×1
  - *Multiple Topics*
      · PQ ×18
- **Analogy**
  - *Basic Concept of Analogy*
      · 1: Non Verbal Reasoning - Analogy (16m)
      · PYQ ×1
      · PQ ×44
  - *Number-Based Analogy*
      · PYQ ×1
      · PQ ×6
  - *Letter or Alphabet Analogy*
      · PQ ×17
  - *Symbol or Figure or Diagram-Based Analogy (Non-Verbal Analogy)*
      · PQ ×1
  - *Multiple Topics*
      · PQ ×1
      · PYQ ×2
      · PQ ×69
- **Seating Arrangements**
  - *Multiple Topics*
      · Concepts, Tricks & Questions (1) (1.3h)
      · Concepts, Tricks & Questions (2) (44m)
  - *Single Row Arrangement*
      · PQ ×2
  - *Double Row Arrangement*
      · PQ ×2
  - *Circular Arrangement*
      · PYQ ×1
      · PQ ×3
  - *Square or Rectangular or Polygonal Arrangement*
      · PQ ×4
  - *Floor or Level Based Arrangement (Vertical Seating)*
      · PQ ×1
      · PYQ ×1
      · PQ ×12
- **Analytical Reasoning (Counting Figures Reasoning)**
  - *Basic Concepts & Approach to Counting Figures*
      · PQ ×1
  - *Counting Squares*
      · Square Counting Tricks (25m)
      · PQ ×1
  - *Counting Rectangles*
      · Rectangle Counting Tricks (9m)
      · PQ ×1
  - *Counting Triangles*
      · Triangle Counting Tricks (1.3h)
      · PQ ×9
  - *Counting Straight Lines or Intersecting Lines*
      · Straight Lines Counting Tricks (12m)
      · PQ ×1
  - *Counting Cubes and other 3D Figures*
  - *Counting Other Figures (Polygons & Mixed Shapes)*
  - *Multiple Topics*
      · PQ ×1
      · PQ ×14
      · PYQ ×13
      · PQ ×427
      · Coal India - Unit Test - Logical Reasoning (45m)

### 12. Paper-1 | Quantitative Aptitude — 273 vids · 81.5h · 34 PYQs · 372 PQs

- **Ratio and Proportion (Ratios)**
  - *Basic Concepts & Properties of Ratio*
      · Demo: What is Ratio & Proportion, Definition & Examples (12m)
      · Demo: Properties of Ratios, Properties of Proportions (14m)
      · PQ ×5
  - *Types of Ratio*
      · Demo: Types of Ratios with Examples (15m)
      · Short Tricks to Combine Two or More Ratios (16m)
  - *Direct, Inverse & Joint Variation*
      · What is Variation, What is Direct & Indirect Variation (13m)
  - *Basic Concepts & Properties of Proportion*
      · Invertendo, Alternendo, Componendo & Dividendo Property (15m)
      · Addendo Property & Equivalent Ratio Property (16m)
      · PQ ×4
  - *Division of Quantity in a Given Ratio*
      · Short Trick to Divide a Given Number X in ratio of M N (16m)
      · Short Trick to bring given set of numbers in proportion (14m)
      · Short Trick to convert given ratio into required ratio (8m)
      · Finding ratio of 2 numbers from their sum & difference (3m)
      · PQ ×3
  - *Mean / Extreme / Continued Proportion*
      · PQ ×2
  - *Successive & Combined Ratio Problems*
      · Short Trick to Find A   C when A   B & B   C is given (6m)
      · Short Trick to Find A   B   C given some mA = nB = pC (5m)
      · Short Trick to find (mX + nY)   (pX + qY) given x   y (10m)
      · Short Trick to Find bigger ratio out of given 2 ratios (9m)
      · PYQ ×1
      · PQ ×2
  - *Multiple Topics*
      · Quick Revision and Practice Questions (1.1h)
      · PYQ ×1
      · PQ ×16
- **Mixture and Alligation**
  - *Basic Concepts and Weighted Average*
      · Demo: What is Covered in this Topic (10m)
      · Demo: Pre-requisite required to understand Mixture & Alligation (12m)
      · Demo: Concept of Weighted Average & its role in Alligations (14m)
  - *Alligation Rule (Core Concept + Two-Ingredient Mixture)*
      · What is Mixture & Alligation (12m)
      · Where to apply Alligation Rule (Applications) (6m)
      · TCS Previous Year Question on Alligation Rule (11m)
      · WIPRO Previous Year Question on Alligation Rule (10m)
      · BANK PO & AMCAT Previous Year Question on Alligation Rule (12m)
      · GATE Exam (Mechanical) Asked Question on Alligation Rule (13m)
      · COGNIZANT & ACCENTURE Asked Questions on Alligation Rule (9m)
      · PYQ ×1
      · PQ ×8
  - *Three-Ingredient Mixtures and Mixture of Mixtures*
      · SHORT TRICKS to solve problems on MIXTURE OF MIXTURE (11m)
      · SHORT TRICK To Apply Alligation Rule on 3 Ingredients (14m)
      · INFOSYS Previous Year Question on 3 Ingredients Mixture (13m)
      · TCS, INFOSYS & E-LITMUS Question on Mixture of Mixture (10m)
  - *Profit–Loss Based Alligation (Cost Price, Selling at CP, Fake Profit)*
      · Solving PROFIT & LOSS Questions Using Alligation Rule (15m)
      · Water mixed to a mixture & sold at CP to make profit (1) (11m)
      · Water mixed to a mixture & sold at CP to make profit (2) (10m)
      · Water mixed to a mixture & sold at CP to make profit (3) (6m)
      · Selling item in 2 parts with given profit% or loss% (1) (6m)
      · Selling item in 2 parts with given profit% or loss% (2) (10m)
      · Selling item in 2 parts with given profit% or loss% (3) (9m)
      · PQ ×1
  - *Concentration / Purity Adjustment Problems*
      · Alligation Rule For Diluting Milk With Water Problems (13m)
      · Adding an Ingredient to Increase Concentration Questions (11m)
      · SHORT TRICK -Adding Ingredient to Increase Concentration (7m)
      · PQ ×1
  - *Application-Based Problems (Population, Students, Males/Females, Distribution)*
      · Finding number of males &  females using alligation rule (9m)
  - *Challenging and Mixed Questions*
      · Mixtures & Alligations Challenging Questions (1) (10m)
      · Mixtures & Alligations Challenging Questions (2) (23m)
  - *Investment and Interest Rate Based Alligation (Simple Interest, Compound Interest)*
      · Solving SIMPLE INTEREST Questions using Alligation Rule (13m)
      · Short Tricks to solve investment interest problems (1) (8m)
      · Short Tricks to solve investment interest problems (2) (7m)
  - *Multiple Topics*
      · Mixture & Alligations (Quick revision & Practice Problems) (1.4h)
      · PYQ ×1
      · PQ ×10
- **Permutation and Combination**
  - *Basic Concepts & Counting Principles*
      · Demo: Permutation & Combination (Quick Revision & Practice Questions) (1.2h)
      · PQ ×1
  - *Permutations (with & without Repetition)*
      · Demo: Permutations with No Repetition (17m)
      · Demo: Permutations with Unlimited Repetitions (8m)
      · Permutations with Limited Repetitions (9m)
      · Tricks to Solve The Famous MISSISSIPPI Problem in P&C (13m)
      · Vowels & Consonants Type Questions in P&C (9m)
      · Tricks to Solve Questions on  Arrangement of Letters (9m)
      · Tricks to Solve Questions on  Arrangement of Digits  (1) (14m)
      · Tricks to Solve Questions on  Arrangement of Digits  (2) (6m)
      · PYQ ×1
      · PQ ×5
  - *Circular & Grouping Permutations*
      · Tricks to Solve Grouping Type Questions in P&C (12m)
      · Tricks for Problems on Choosing Items from Group of Items (14m)
      · Circular Arrangements (10m)
      · Circular Arrangements on Groups (10m)
      · Tricks to Solve  Necklace Based Problems (8m)
      · PQ ×1
  - *Combinations (with & without Repetition)*
      · Combinations with No Repetitions & Unlimited Repetitions (13m)
      · Solving Some Basic Questions on Permutation & Combination (14m)
      · An Important Property (Binomial Theorem) (6m)
      · Total Outcomes, MCQ Paper Solving, Unlimited Repetitions (10m)
      · PYQ ×1
      · PQ ×3
  - *Special Applied Problems*
      · Tricks to Solve Questions on  Binary Strings (10m)
      · Trick for Sum of all numbers formed from given digits (11m)
      · Finding Rank of a Word (Concept + Short Trick) (13m)
      · Question on Finding Rank of a Word Without Repetition (11m)
      · Short Trick to Find Rank of a Word With Repetitions (9m)
      · Short Trick to Find Number of Handshakes (10m)
      · Chocolate Picking Problem (6m)
      · Counting Sticks Approach (11m)
      · Short Tricks to Solve  Dice Sum Problem  (1) (10m)
      · Short Tricks to Solve  Dice Sum Problem  (2) (12m)
      · Conventional Method of Solving  Dice Sum Problem (7m)
      · Short Tricks for  Alphabet Selection Problem  in P&C (8m)
      · PQ ×1
  - *Advanced Counting Theorems*
      · Principle of Inclusion & Exclusion, Use of Venn Diagram (13m)
      · Number of Intersection Points & Parallelogram (7m)
      · Concept & Short Tricks of Derangement in P&C (11m)
      · Important Questions on Derangements (10m)
      · PQ ×9
  - *Multiple Topics*
      · PYQ ×2
      · PQ ×20
- **Number System**
  - *Basic Concepts & Classification of Numbers*
      · PQ ×2
  - *Factors, Multiples & Prime Factorization*
      · Demo: Short Tricks to Find Number & Product of Factors (11m)
      · Demo: Tricky Important Questions on Finding Product of Factors (10m)
      · Demo: Short Tricks to Find Number of Odd & Even Factors (18m)
      · Tricks To Find Sum of Factors & Sum of Odd & Even Factors (13m)
      · Finding those Factors of 'P' which are divisible by 'Q' (11m)
      · 86-7776 NVS 2019 (1m)
      · PQ ×6
  - *Concept of Remainders*
      · Concept of Reminders (Part 1) (13m)
      · Concept of Reminders (Part 2) (16m)
      · Concept of Reminders (Part 3) (22m)
      · Concept of Reminders (Part 4) (18m)
      · Short Trick for Reminders on Successive Divisions (11m)
      · PYQ ×1
      · PQ ×1
  - *Unit Digit & Last Digit Concepts*
      · Short Tricks to Find Unit Digit of an Expression (1) (15m)
      · Short Tricks to Find Unit Digit of an Expression (2) (19m)
      · PQ ×2
  - *Perfect Squares, Perfect Cubes, Power, Square Root and Patterns*
      · Interesting Facts About Perfect Squares & Perfect Cubes (12m)
      · Tricks to Find Factors that are Perfect Squares & Cubes (11m)
      · Question - Find Factors that are Perfect Squares & Cubes (9m)
      · Number Systems - HOT Questions (1) (13m)
      · Number Systems - HOT Questions (2) (6m)
      · PQ ×4
  - *Multiple Topics*
      · Number System (Quick Revision & Practice Questions) (1.4h)
      · PYQ ×1
  - *Simplification Based Problems*
      · PYQ ×1
      · PQ ×6
      · PYQ ×3
      · PQ ×21
- **HCF LCM**
  - *Finding HCF*
      · Demo: Tricks for HCF by Inspection, HCF by Prime Factorization (18m)
      · Demo: Trick to find HCF by Long Division Method (6m)
      · Demo: Short Trick to find HCF by minimum difference method (14m)
      · Short Trick to find HCF by using smallest element (10m)
      · An Important Property of HCF & LCM + Practice Question (13m)
      · How to find HCF Quickly with the help of given options (6m)
      · Short Trick to find HCF of Big Numbers (10m)
      · Short Trick to find HCF of more than 2 numbers (6m)
      · Short Trick to find HCF using Co-Prime Numbers Concept (13m)
      · PQ ×2
  - *HCF and LCM of Fractions and Decimals*
      · Short Tricks to calculate HCF of Decimals & Fractions (11m)
      · Short Trick to find LCM of decimal numbers (7m)
      · Short Trick to find LCM & HCF of fractions (9m)
      · PQ ×2
  - *Basic Concepts: Factors, Multiples, Prime & Composite Numbers*
      · Part 1 - Short Tricks to check Divisibility by 7 & 13 (12m)
      · Part 2 - Short Tricks to check Divisibility by 7 & 13 (15m)
      · Another Short Trick to find HCF of Big Numbers (5m)
  - *Finding LCM*
      · What is a multiple What is LCM  Find LCM by inspection (11m)
      · Short Trick to Find LCM in just 5 seconds (8m)
      · Short Trick to find LCM using Division method (8m)
      · Short Trick to find LCM using Prime Factorization (13m)
      · Short Trick to find LCM using Co-Prime Numbers Concept (9m)
      · Short Trick to find LCM of more than 2 numbers (8m)
      · Short Trick to find LCM of big numbers (4m)
      · Short Trick to find LCM of 2 numbers when HCF is given (6m)
      · PQ ×2
  - *Application and Word Problems Based on HCF and LCM*
      · PQ ×6
  - *Definition, Difference, Properties and Relationship Between HCF and LCM*
      · PQ ×1
  - *HCF and LCM of more than two numbers*
      · PQ ×2
  - *Multiple Topics*
      · HCF LCM (Quick Revision & Practice Problems) (1.2h)
      · PQ ×15
- **Speed Time and Distance**
  - *Basics, Prerequisites and Unit Conversions*
      · Demo: What is covered in this course (10m)
      · Demo: Pre-requisites required for Speed, Time & Distance (14m)
      · Demo: Definitions, Basic Formulas, Units and Inter-conversions (12m)
      · Trick to convert kilometer per hour to meter per second (8m)
      · PQ ×1
  - *Proportionality and Constant Variable Concepts*
      · What happens when Speed or Distance or Time is constant (13m)
      · PQ ×2
  - *Average Speed*
      · Concept & Short Tricks to calculate AVERAGE SPEED (1) (14m)
      · Concept & Short Tricks to calculate AVERAGE SPEED (2) (6m)
      · Concept & Short Tricks to calculate AVERAGE SPEED (3) (10m)
      · Average - Short Tricks to Find Average Speed (7m)
      · Important Practice Questions on AVERAGE SPEED (1) (9m)
      · Important Practice Questions on AVERAGE SPEED (2) (13m)
      · Important Practice Questions on AVERAGE SPEED (3) (9m)
      · PYQ ×1
      · PQ ×6
  - *Relative Speed, Meeting Point, Catch-Up and Chase Problems*
      · PQ ×4
  - *Train Problems*
      · Concept of Relative Speed Required for Problem on Trains (19m)
      · Case 1_ Train Crossing a stationary pole, signal or man (19m)
      · Case 2_ Train Crossing a Platform, Bridge or Tunnel (16m)
      · Case 3_ Two Trains Crossing One Other(Opposite Direction) (12m)
      · Case 4_ Two Trains Crossing One Other (Same Direction) (13m)
      · Conventions To Solve Problems on Train + Tricky Questions (11m)
      · Short Trick To Solve Problem on Stoppages (9m)
      · Important Question & Short Trick on Train Problems (1) (9m)
      · Important Question & Short Trick on Train Problems (2) (9m)
      · Important Question & Short Trick on Train Problems (3) (9m)
      · PQ ×6
  - *Boats and Streams*
      · Basic Concepts, Terminology & Formulas of Boats & Streams (12m)
      · Solving Basic Level Questions on Boats & Streams (12m)
      · Short Trick to Solve Round Trip Problem in Boats & Stream (14m)
      · Short Trick to Solve Comparison Problem in Boats & Stream (13m)
      · Important Questions on Boats & Streams with Short Tricks (13m)
      · 20.6 (1.1h)
      · PQ ×5
  - *Circular Track Problems*
  - *Complex and Mixed Journey Problems*
      · PQ ×1
  - *Multiple Topics*
      · Important Practice Questions on SPEED TIME & DISTANCE 1 (1.2h)
      · Important Practice Questions on SPEED TIME & DISTANCE 2 (1.2h)
      · Speed Time & Distance (Quick Revisions & Practice Questions) (1.6h)
      · PYQ ×1
      · PQ ×25
- **Average**
  - *Basic Concepts and Formulas*
      · Basic Concepts, Formulas & Questions (6m)
      · PQ ×6
  - *Average of Consecutive / Odd / Even / Natural Numbers*
      · Average of First N Odd, Even, Consecutive No (8m)
      · Average of N Consecutive Odd & Even Numbers (7m)
      · PQ ×3
  - *Average of Arithmetic Series, Squares, and Cubes*
      · Average of Arithmetic Series, Squares, Cubes (5m)
  - *Change in Average (When Members Join, Leave, or Replace)*
      · Change on Average when person join or leave (7m)
      · Change on Average when a person replaces (8m)
      · PQ ×3
  - *Effect on Average by Arithmetic Operations*
      · Effect on Average by Arithmetic Operations (6m)
      · PQ ×1
  - *Weighted Average, Combined / Mixture Average Problems*
      · Weighted Average - Concept & Short Tricks (9m)
      · PYQ ×1
      · PQ ×3
  - *Practical and Contextual Word Problems*
      · 8 (7m)
      · Cricket Based Problems on Average (Part 1) (8m)
      · Average - Cricket Based Problems on Average (Part 2) (10m)
  - *Multiple Topics*
      · Average (Quick Revision & Practice Problems) Part 1 (32m)
      · Average (Quick Revision & Practice Problems) Part 2 (1.2h)
  - *Error Correction Problems*
      · PYQ ×1
      · PQ ×16
- **Age Problems**
  - *Basic Concepts of Ages*
      · Problems on Age - Concepts, Short Tricks & Questions (1.4h)
      · PQ ×1
  - *Age Ratio–Based Problems*
      · PQ ×2
  - *Age Comparison and Multiple Condition Problems*
      · PQ ×4
  - *Age Difference, Sum and Product Based Problems*
      · PQ ×1
  - *Advanced Multi-Stage Age Problems (Past + Present + Future)*
      · PQ ×2
  - *Multiple Topics*
      · PQ ×10
- **Percentage**
  - *Basic Concepts, Terminologies & Properties*
      · What is Covered in this Course (12m)
      · Pre-requisite required to understand Percentages (14m)
      · Complete Percentage in One Shot (1.1h)
      · PQ ×1
  - *Conversion Between Fractions (Ratio) & Percentages*
      · Demo: Basics of Percentages, Percentage - Fraction Conversions (13m)
      · Important Property, Trick to find 10 & 1 percent of any number (10m)
      · Short Tricks to Remember Ratio to Percentage Table Part 1 (9m)
      · Short Tricks to Remember Ratio to Percentage Table Part 2 (11m)
      · Short Tricks to Remember Ratio to Percentage Table Part 3 (9m)
      · Short Tricks to Remember Ratio to Percentage Table Part 4 (8m)
      · Practice Problems on Ratio to Percentage Conversion (10m)
      · Practice Problems on Percentage to Ratio Conversion (8m)
      · Question on Ratio to Percentage Conversion (5m)
      · PYQ ×1
      · PQ ×2
  - *Finding Percentage*
      · Few Important Points for Percentages (7m)
      · The Three Confusing Questions of Percentages (9m)
      · PYQ ×1
      · PQ ×2
  - *Percentage Relationship Questions*
      · PQ ×1
  - *Successive Percentage Change*
      · PQ ×3
  - *Percentage Difference & Reverse Comparison*
      · PQ ×4
  - *Expenditure, Consumption, & Price Relationship*
      · PQ ×4
  - *Percentage in Population / Growth / Successive Years*
      · PQ ×2
  - *Multiple Topics*
      · Important Practice Questions on Percentages (Part 1) (53m)
      · Important Practice Questions on Percentages (Part 2) (46m)
      · PYQ ×2
      · PQ ×19
- **Profit and Loss**
  - *Basic Concepts, Formulas and Quick Transformations*
      · Basic Concepts (14m)
      · Short Tricks to Solve Questions Quickly (11m)
      · Short Tricks to Solve Questions Quickly (11m)
  - *Finding Profit, Loss, Cost Price, Selling Price, Profit Percent and Loss Percent*
      · Short Trick to Find Selling Price Quickly (9m)
      · Short Trick to Find Selling Price Quickly (12m)
      · Cost Price = Profit Percent (10m)
      · PQ ×11
  - *Multiple Items and Mixed Rate Problems*
      · Profit Loss Percent on Multiple Items (9m)
      · Profit Loss on Selling Multiple Items (7m)
      · PQ ×2
  - *Overall Profit and Loss (Combined Transactions)*
      · Find Profit & Loss Percent (10m)
      · Find Overall Profit and Loss (9m)
      · Find Overall Profit & Loss Percentage (7m)
      · PQ ×4
  - *Discount, Marked Price and Trader Tricks (Including False Weight)*
      · Practice Questions (8m)
      · Practice Questions (7m)
      · Practice Questions (11m)
      · Practice Questions (8m)
      · PYQ ×1
      · PQ ×9
  - *Multiple Topics*
      · Quick Revision & Practice Questions (1.2h)
      · PYQ ×1
      · PQ ×26
- **Time and Work**
  - *Basic Concepts of Work & Efficiency*
      · Important Concepts, Tricks & Questions (1.1h)
      · Basic Concepts (6m)
      · PQ ×1
  - *Individual Work and Combined Work Problems*
      · Short Tricks for Alone & Combined Work (13m)
      · PQ ×7
  - *Efficiency Ratio and Comparative Work Rate*
      · Tricks for Comparision Based Questions (11m)
      · PQ ×1
  - *Alternate Days & Remaining Work Problems*
      · Person joining or leaving in between (12m)
      · Efficiency & Alterate Days Problem (2) (6m)
      · PQ ×3
  - *Men–Women / Worker-Based Problems*
      · PQ ×1
  - *Work & Wages Distribution*
  - *Work–Hour–Man Relationship Problems*
      · PYQ ×1
      · PQ ×4
  - *Machine or Productivity-Based Work Problems*
  - *Multiple Topics*
      · Practice Questions (15m)
      · Practice Questions (11m)
      · Practice Questions (11m)
      · Practice Questions (12m)
      · PQ ×1
      · PYQ ×1
      · PQ ×18
- **Pipe and Cistern**
  - *Basic Concepts, Formulas and Terminology*
      · Pipes & Cisterns (1.2h)
  - *Single Pipe Problems*
  - *Multiple Pipes Together*
      · PQ ×6
  - *Pipes Opening or Closing at Different Times*
      · PQ ×1
  - *Alternate Day or Hour Problems*
  - *Leakage or Hole Problems*
      · PQ ×2
  - *Multiple Topics*
      · PQ ×9
- **Simple Interest and Compound Interest**
  - *Simple Interest - Basic Concepts, Formulas and Terminologies*
      · Terminology  Principal, Rate, Time, Interest, Amount (7m)
      · Simple Interest   Basic Concepts & Formulas (16m)
      · Simple Interest   Basic Level Questions (10m)
      · Simple Interest  Important Practice Questions (Set 1) (15m)
      · PQ ×7
  - *Simple Interest – Applications*
      · Tricks & Questions on money becoming multiple times on SI (13m)
      · Questions on Extra Amount Received on Extra Interest Rate (8m)
      · Short Trick for Questions on  Variable Rate of Interest (10m)
      · Short Trick for Questions on  Difference in SI (8m)
      · Short Trick for Questions on  Difference in Amount (12m)
      · Questions on  Principal Money Divided into Parts (12m)
      · Simple Interest  Important Practice Questions (Set 2) (11m)
      · PQ ×5
  - *Installments and Debt-Related Problems*
      · Short Trick to solve  Debt Related Problems (15m)
  - *Compound Interest – Core Concepts*
      · Compound Interest   An Introduction (8m)
      · Compound Interest   Formula & Comparison with SI (6m)
      · Short Trick to Find Compound Interest in just 10 Seconds (12m)
      · Compound Interest   Basics + Problem Solving (1) (29m)
      · Compound Interest   Basics + Problem Solving (2) (1.0h)
      · Compound Interest   Basics + Problem Solving (3) (1.1h)
      · PQ ×7
  - *Compound Interest – Advanced Patterns*
      · PQ ×1
  - *Mixed SI CI and Special Cases*
      · Simple and compound interest (Quick Revision & Practice Questions) (1.1h)
  - *Multiple Topics*
      · PQ ×20
- **Powers and Exponents (Surds and Indices)**
  - *Basic Concepts & Laws of Exponents (Indices)*
  - *Negative & Fractional Exponents*
  - *Simplification Using Laws of Exponents*
      · PQ ×4
  - *Laws of Surds & Simplification*
      · Surds and Indices Part 1 (17m)
      · Surds and Indices Part 2 (13m)
      · PQ ×1
  - *Rationalization of Surds*
      · Surds and Indices Part 3 (10m)
      · PYQ ×1
      · PQ ×1
  - *Comparing & Simplifying Complex Powers*
      · Surds and Indices Part 4 (3m)
  - *Multiple Topics*
      · UPDATED_surds and indices (1.1h)
      · PYQ ×1
      · PQ ×6
- **Mensuration and Geometry**
  - *Basic Concepts and Geometric Terminology*
      · Triangle & Circle, Basic Concepts & Formulas (55m)
      · PYQ ×1
      · PQ ×2
  - *2D Mensuration (Plane Figures)*
      · Practice Questions - Part 1 (44m)
      · Practice Questions - Part 2 (56m)
      · Practice Questions - Part 3 (1.1h)
      · PYQ ×1
      · PQ ×18
  - *3D Mensuration (Solid Figures)*
      · 3D Geometry Introduction (16m)
      · Surface Area, Volume and Capacity Are Different (17m)
      · 3D Geometry Important Question (5m)
      · PQ ×12
  - *Relation Between 2D & 3D Figures*
      · PYQ ×1
      · PQ ×1
  - *Multiple Topics*
      · PYQ ×3
      · PQ ×33
- **Probability**
  - *Basic Concepts and Terminology*
      · What is Sure Event, Impossible Event, Complementary Event (14m)
      · Short Trick to find total outcomes in an experiment (12m)
      · Mutually Exclusive Events & Exhaustive Events (17m)
      · Odds in Favour of an event & Odds Against An Event (11m)
      · Demo: What is Experiment, Event, Favorable & Total Outcome (15m)
      · PYQ ×2
      · PQ ×3
  - *Classical Problems (Cards, Dice, Coins, Digits, Number, Objects)*
      · Short Tricks to deal with cases of 'At least' & 'At most' (9m)
      · Tricks & Techniques to Solve Dice Sum Problems (16m)
      · Tricks & Techniques to Solve Playing Cards Problem (9m)
      · Finding Probability of 53 Sundays in a Leap Year (12m)
      · PYQ ×5
      · PQ ×16
  - *Probability Using Venn Diagrams & Set Theory*
      · Some Important Events (A AND B, A OR B, A BUT NOT B) (15m)
      · PYQ ×1
      · PQ ×4
  - *Conditional Probability*
      · PQ ×3
  - *Law of Total Probability*
  - *Bayes Theorem (Inverse Probability)*
      · PYQ ×1
  - *Probability Using Permutation & Combination Logic*
      · PQ ×7
  - *Continuous Probability Distribution, Random Variables & Expected Value*
      · PYQ ×3
      · PQ ×17
  - *Multiple Topics*
      · Quick Revision & Practice Questions - Part 1 (1.1h)
      · Quick Revision & Practice Questions - Part 2 (34m)
      · PYQ ×12
      · PQ ×50
- **Statistics**
  - *Introduction & Types of Data*
      · Basic Concepts (1.3h)
      · PQ ×2
  - *Mean, Median, and Mode for ungrouped data*
      · PQ ×7
  - *Mean, Median, and Mode for grouped data*
      · Advance Concepts (56m)
      · PYQ ×1
  - *Range, Mean Deviation, Variance, and Standard Deviation*
      · PYQ ×2
      · PQ ×9
  - *Multiple Topics*
      · PQ ×4
      · PYQ ×3
      · PQ ×22
- **Arithmetic**
  - *Basic Arithmetic*
      · Arithmetic - Part 1 (1.1h)
      · Arithmetic - Part 2 (27m)
      · PQ ×6
  - *Advance Arithmetic*
  - *Multiple Topics*
      · PQ ×6
- **Algebra**
  - *Basic Concepts & Fundamental Operations*
      · Simplification and Algebra (1.5h)
      · Introduction (15m)
      · Concept Building (11m)
      · PQ ×1
  - *Laws & Identities of Algebra*
      · Important Identities (19m)
      · How to Plot Equations on Graphs (26m)
      · PQ ×8
  - *Factorization & Simplification*
      · Some Example Questions (11m)
      · PQ ×2
  - *Linear Equations*
      · Linear Equation - Concepts, Short Tricks & Questions (21m)
      · Linear Equations Application Practice Question (33m)
      · PQ ×6
  - *Quadratic Equations*
      · Ways to Solve Quadractic Equations (12m)
      · PQ ×7
  - *Polynomials & Algebraic Expressions*
      · Types of polynomial and Binomial (21m)
      · How To Solve HCF in Polynomials (26m)
      · How To Solve LCM in Polynomials (13m)
      · PQ ×2
  - *Algebraic Fractions, Rational & Irrational Expressions*
      · PQ ×1
  - *Linear Inequalities & Modulus*
      · PYQ ×1
      · PQ ×2
  - *Simplification Based Problems*
      · Hacks To Solve Numeric Questions Using Algebraic Identities (30m)
      · PYQ ×1
  - *Multiple Topics*
      · Practice Questions on HCF & LCM Of Polynomials (15m)
      · PYQ ×2
      · PQ ×29
      · PYQ ×34
      · PQ ×371
      · Coal India - Unit Test - Quantitative Aptitude (45m)

### 13. Paper-1 | English — 52 vids · 24.6h · 2 PYQs · 527 PQs

- **Vocabulary**
  - *Word Meanings (Contextual Vocabulary)*
      · Demo: Part 1 (1.8h)
      · Demo: Part 2 (1.7h)
      · Demo: Part 3 (1.1h)
      · Part 4 (1.1h)
      · PQ ×24
  - *Synonyms & Antonyms*
      · Introduction - Synonyms & Antonyms (23m)
      · Building vocabulary the  smart way (18m)
      · Root Words, Prefixes, Suffixes (17m)
      · High Frequency  Synonyms (24m)
      · High Frequency  Antonyms (15m)
      · PART A - Commonly confused pairs (14m)
      · Word Relationships Vocabulary Networks (13m)
      · Question Solving  Strategies (10m)
      · 55 Synonyms&Antonyms NVS 2014 (2m)
      · PYQ ×1
      · PQ ×111
  - *Homophones / Homonyms / Confusing Words*
      · Module 1: Homophones, Homonyms, Confusing Words (24m)
      · Module 2: Homophones, Homonyms, Confusing Words (17m)
      · PQ ×3
  - *One-Word Substitutions*
      · Concepts, Tricks & Questions (53m)
      · Practice Questions (22m)
      · PQ ×23
  - *Idioms, Phrases, Pharasal Verbs and Collocations*
      · Idioms, Phrases and Collocations 1 (20m)
      · Idioms, Phrases and Collocations 2 (9m)
      · Idioms, Phrases and Collocations 3 (12m)
      · PQ ×45
  - *Root Words, Prefixes & Suffixes*
      · Part-1 Root Words, Prefixes, Suffixes (22m)
      · Part-2 Root Words, Prefixes, Suffixes (23m)
      · PQ ×1
  - *Foreign Origin Words (Commonly Used)*
      · Foreign Words (10m)
      · PQ ×1
  - *Spelling & Commonly Mis-spelt Words*
      · Concepts, Rules, Short Tricks & Questions (31m)
      · Spellings, Commonly Misspelt Words 1 (19m)
      · Spellings, Commonly Misspelt Words 2 (5m)
      · Spellings, Commonly Misspelt Words 3 (10m)
      · PQ ×24
  - *Multiple Topics*
      · PQ ×8
      · PYQ ×1
      · PQ ×240
- **Comprehension / Reading Comprehension / Unseen Passages (Critical Reasoning) (Paragraph Questions)**
  - *Basic Reading & Understanding (Literal Comprehension)*
      · Concepts, Tricks, Questions (14m)
      · Concepts, Rules & Tricks (29m)
      · Practice Questions (1) (43m)
      · Practice Questions (2) (21m)
      · Practice Questions (3) (56m)
      · Practice Questions (4) (27m)
      · Comprehension - UGC NET June 2025 (10m)
      · PQ ×45
  - *Vocabulary in Context*
      · PQ ×13
  - *Central Idea and Main Theme Identification*
      · PQ ×8
  - *Tone & Attitude Detection*
      · PQ ×6
  - *Inference-Based Questions, Assumption and Implication Recognition*
      · PYQ ×1
      · PQ ×14
  - *Data / Example Interpretation*
      · PQ ×1
  - *True / False / Cannot Say Type Questions*
      · PQ ×3
  - *Logical Structure & Flow Understanding (Cause-effect, comparision-contrast, problem-solution)*
      · PQ ×3
  - *Multiple Topics*
      · Critical Reasoning - Concepts, Short Tricks & Questions (1) (11m)
      · PQ ×3
      · PYQ ×1
      · PQ ×96
- **Sentence Re-arrangements (Para Jumbles) (Narrative Sequencing)**
  - *Basic Sentence Re-arrangement (Para Jumbles)  (Narrative Sequencing)*
      · Concepts, Rules, Short Tricks & Questions (1.2h)
      · PQ ×23
  - *Advance Sentence Re-arrangement (Para Jumbles)  (Narrative Sequencing)*
      · Practice Questions (22m)
      · PQ ×3
  - *Multiple Topics*
      · PQ ×26
- **Sentence Correction (Error Correction)**
  - *Basic Concepts, Terminologies and Rules*
      · Concepts, Rules, Tricks & Questions (1.2h)
      · Concept, Rules, Tricks, Questions (28m)
      · Practice Questions (39m)
      · Practice Questions (1) (12m)
      · Practice Questions (2) (15m)
  - *Subject–Verb Agreement Errors*
      · PQ ×12
  - *Tense & Verb Form Errors*
      · PQ ×9
  - *Pronoun & Reference Errors*
      · PQ ×1
  - *Preposition & Connector Errors*
      · PQ ×9
  - *Modifier Placement Errors*
      · PQ ×1
  - *Adjective vs Adverb Errors*
      · PQ ×2
  - *Parallelism / Comparison Errors*
      · PQ ×2
  - *Redundancy & Word Choice Errors*
      · PQ ×1
  - *Vocabulary Error*
  - *Sentence Improvement*
      · Concepts, Tricks & Questions (11m)
      · PQ ×4
  - *Logical Error*
      · PQ ×3
  - *Multiple Topics*
      · PQ ×5
      · PQ ×49
- **Sentence Completion (Fill in the blanks)**
  - *Basic Concepts, Terminologies and Rules*
      · Concepts, Rules & Short Tricks (27m)
      · Easy Questions (26m)
      · Tough Questions (22m)
      · Practice Questions (30m)
      · Practice Questions (46m)
      · PQ ×3
  - *Context Understanding (Meaning of the Sentence)*
      · PQ ×17
  - *Signal Words (Logic Clues)*
      · PQ ×3
  - *Parts of Speech Fit*
      · 123 Sentence Completion Context Understanding 7522 NVS 2019 (2m)
      · PQ ×13
  - *Vocabulary in Context (Tone/Emotion Fit)*
      · PQ ×23
  - *Idioms and Pharases Usage*
      · PQ ×10
  - *Verb Tense or Verb Form Based on Clues*
      · PQ ×13
  - *Multiple Topics*
      · PQ ×2
      · PQ ×84
- **Sentence Construction**
  - *Basics of Sentence Construction*
      · Concepts, Tricks & Questions (8m)
      · PQ ×4
  - *Parts of Speech Placement in Sentence Construction*
      · PQ ×1
  - *Sentence Sequencing and Coherence (Micro Sentence Construction)*
      · PQ ×2
  - *Constructing Grammatically Correct Sentences (Error-Free Writing)*
      · PQ ×10
  - *Advanced Sentence Construction (Context + Meaning Accuracy)*
  - *Multiple Topics*
      · PQ ×1
      · PQ ×18
- **Cloze Test (Cloze Passage)**
  - *Basics of Cloze Test and Understanding Context*
      · Cloze Test - Concepts, Rules, Short Tricks & Questions (12m)
      · Cloze Test - Practice Questions (29m)
      · PQ ×2
  - *Grammar-Based Blanks (Rule-Based Cloze Test)*
  - *Vocabulary-Based Blanks (Meaning-Based Cloze Test)*
      · PQ ×10
  - *Logical / Connective Cloze Test (Coherence & Linking)*
      · PQ ×2
  - *Mixed Cloze Test (Grammar + Vocab + Logic Combination)*
  - *Multiple Topics*
      · PQ ×14
      · PYQ ×2
      · PQ ×527
      · Coal India - Unit Test - English (45m)

### 14. Coal India Previous Year Paper — 0 vids · 6.0h · 0 PYQs · 0 PQs

      · Coal India pervious year 2020 (3.0h)
      · Coal India pervious year 2017 (3.0h)

### 15. Engineering Mathematics — 264 vids · 25.6h · 89 PYQs · 250 PQs

- **Set Theory**
  - *Sets, Representation of Sets and Hierarchy of numbers*
      · What is SET (6m)
      · Representation Of Set (3m)
      · Natural number, Whole number, Integer (3m)
      · Rational Number, Irrational Number, Complex Number (3m)
      · PQ ×1
  - *Finite, Infinite, Countable, and Uncountable Sets*
      · Finite, Infinite, Countable, Uncountable Set (4m)
      · PQ ×3
  - *Null, Universal, Subsets, Proper Subsets*
      · NullEmpty Set and Universal Set (5m)
      · SubSet and Proper SubSet Of a Set (5m)
      · Equality Of a Sets (3m)
      · PQ ×2
  - *Power Set and its Cardinality*
      · Power Set of a Set (4m)
      · Practice Question (5m)
      · 9.2 Practice Question (3m)
      · PYQ ×3
      · PQ ×2
  - *Set Operations – Union, Intersection, Set Difference, Symmetric Difference, and Complement*
      · Complement, Union and Intersection of Sets (5m)
      · Practice Question (5m)
      · Set Difference and Symmetric Difference (3m)
      · Laws of Set Theory (3m)
      · 12.5 Practice Question (3m)
      · 12.6 Practice Question (2m)
      · 12.7 Practice Question (3m)
      · 12.8 Practice Question (3m)
      · 12.24 Practice Question (2m)
      · PYQ ×4
      · PQ ×11
      · PYQ ×7
      · PQ ×19
- **Relations**
  - *Cartesian Product, Relation, Inverse & Complement*
      · Cartesian Product of Sets (4m)
      · What is a Relation (4m)
      · Complement of a Relation (3m)
      · Inverse of a Relation (2m)
      · PQ ×4
  - *Reflexive Irreflexive Relation – Count, and Properties*
      · Reflexive Relation (7m)
      · Irreflexive Relation (5m)
      · PYQ ×1
      · PQ ×2
  - *Symmetric Anti-Symmetric Asymmetric Relation and Properties*
      · Symmetric Relation (9m)
      · Anti-Symmetric Relation (8m)
      · Asymmetric Relation (7m)
      · PQ ×4
  - *Transitive Relation – Definition, Count, and Properties*
      · Transitive Relation (7m)
      · Transitive Closure (4m)
      · PQ ×3
  - *Equivalence Relation, Equivalence Classes, Partitions of a Set*
      · Equivalence Relation (1m)
      · PYQ ×3
      · PQ ×10
  - *Partial Order Relation – Properties, Partially Ordered Set (Poset), and Total Order Relation*
      · Partial Order Relation (1m)
      · PQ ×1
  - *Hasse Diagram, Greatest Element, Least Element, Upper Bound, Lower Bound*
      · Conversion of POSET to Hasse Diagram (9m)
      · Identify valid Hasse Diagram (7m)
      · Maximal & Minimal Element (6m)
      · Greatest & Least Element (6m)
      · Upper Bound & Lower Bound (7m)
      · Least Upper Bound & Greatest Lower Bound (7m)
      · PQ ×2
  - *Lattice – Definition, Formation, and Examples of Join and Meet Operations*
      · Lattice Part-1 (8m)
      · Lattce part-2 (6m)
      · PQ ×2
  - *Bounded, Unbounded, Distributive, Complemented Lattices and Boolean Algebr*
      · Unbounded,Bounded, Complement & Distributed Lattice (5m)
      · Practice Question Part-1 (8m)
      · Practice Question Part-2 (5m)
      · Practice Question (9m)
      · Practice Question (4m)
      · 24.5 Practice Question (2m)
      · 24.6 Practice Question (3m)
      · Gate 1988 (1m)
      · PQ ×2
      · PYQ ×4
      · PQ ×30
- **Functions**
  - *Definition of a Function – Domain, Co-domain, Range, and Count of Possible Functions*
      · What is Function (6m)
      · How Many Different Function are Possible (3m)
      · Gate 1998 (2m)
      · PYQ ×1
      · PQ ×5
  - *Composition of Functions – Definition, Properties, and Examples*
      · Compostion of Functions (5m)
      · PQ ×2
  - *One-to-One (Injective) Function – Definition, Count, and Properties*
      · One-To-One (Injective Function) (3m)
      · Number of Injective Functions are Possible (4m)
      · PQ ×1
  - *Onto (Surjective) Function – Definition, Count, and Properties*
      · Onto (Surjective Function) (3m)
      · Number of Onto (Surjective are Possible) (5m)
      · PQ ×3
  - *Bijective Function – Definition, Count, and Properties*
      · Bijective Function (3m)
      · Onto (Surjective Function) (3m)
      · Number of Onto (Surjective are Possible) (5m)
      · PYQ ×1
      · PQ ×2
  - *Inverse of a Function – Definition, Existence Conditions, and Examples*
      · Inverse of a Function (5m)
      · PQ ×1
      · PYQ ×2
      · PQ ×14
- **Graph Theory**
  - *Introduction to Graphs – Definitions, Terminology (Loops, Parallel Edges, Adjacent Vertices)*
      · Basic Terminology of Graph (6m)
      · PQ ×1
  - *Types of Graphs – Finite, Infinite, Null, Trivial, Complete*
      · Finite Graph (3m)
      · Null Graph Vs Trivial Graph (3m)
      · Complete Graph (5m)
      · PYQ ×1
      · PQ ×4
  - *Bipartite, Cycle, Regular, and Complement of a Graph*
      · Cycle, Wheel & Regular Graph (3m)
      · Complement Of a Graph (4m)
      · Bi-Partie Graph (4m)
      · PYQ ×2
      · PQ ×3
  - *Number of Graphs – Counting of Simple, Undirected, Unlabeled*
      · Number Of Simple Graph With n Vertices (5m)
      · Number Of Simple Graph  With n Vertices e Edges (3m)
      · Gate 1994 (2m)
      · Cycle, Wheel & Regular Graph (3m)
      · Complement Of a Graph (4m)
      · Bi-Partie Graph (4m)
      · PYQ ×4
      · PQ ×4
  - *Degree of Vertex – Isolated and Pendant Vertices, Handshaking Lemma, and Degree Sequence*
      · Degree of Vertex, Isolated & Pendant Vertex (4m)
      · Hand-Shaking Theorem Part-1 (5m)
      · 8.3 Practice Question (3m)
      · 8.4 Practice Question (1m)
      · 8.5 Practice Question (2m)
      · 8.7 Practice Question (2m)
      · PYQ ×2
      · PQ ×2
  - *Minimum and Maximum Degree – Relationships, Degree Constraints, and Havel-Hakimi Theorem*
      · Max, Min Degree (4m)
      · Degree Sequence Problem (8m)
      · 9.2 Practice Question (2m)
      · 13.1 Practice Question (2m)
      · An ordered −tuple d_2,\ldots,d_n)\) with \geq \geq \ldots \geq d_n\) (2m)
      · The degree sequence of simple graph is the sequence of (3m)
      · Graph satisfies The min-degree of is defined as Therefore, min-degree (3m)
  - *Graph Traversal – Walk, Path, Trail, Circuit, and Connected Graphs*
      · Walk , Trail & Path (21m)
      · Connected Graph (6m)
      · Practice Question (5m)
      · PYQ ×4
      · PQ ×3
  - *Euler and Hamiltonian Graphs – Definitions, Conditions, and Examples*
      · Euler Graph (6m)
      · Hamiltonian Graph (4m)
      · PYQ ×1
      · PQ ×5
  - *Planar Graphs – Kuratowski’s Theorems, Homorphism and examples*
      · Planner Graph (7m)
      · PQ ×5
  - *Euler Formula – Planar Graph Formula, Applications, and Derived Relations*
      · Euler Formula (4m)
      · Euler Formula and its Version (4m)
      · PYQ ×3
      · PQ ×3
  - *Graph Coloring – Vertex Coloring, Edge Coloring, Chromatic Number, and Coloring Theorems*
      · Graph Coloring (6m)
      · Practice Question (6m)
      · Important Conclusion of Graph Coloring (3m)
      · PYQ ×2
      · PQ ×7
  - *Trees – Definitions, Properties, Eccentricity, Diameter, Radius, and Center*
      · Tree (6m)
      · Eccentricity of Vertex (5m)
      · PYQ ×3
      · PQ ×4
  - *Spanning Tree and Spanning Forest – Definition, Construction, and Applications*
      · Spanning Tree (6m)
      · Spanning Forest (4m)
      · PYQ ×3
      · PQ ×2
  - *Cut Set and Connectivity – Edge Connectivity, Vertex Connectivity, and Cut Set Concepts*
      · Edges CutSet and Edges Connectivity (7m)
      · Vertex CutSet and Vertex Connectivity (4m)
      · Practice Question (4m)
      · PYQ ×2
      · PQ ×3
  - *Graph Isomorphism – Definition, Detection, and Problem Solving*
      · Isomorphism (4m)
      · Isomorphism ShortCut Trick (3m)
      · Practice Questions (7m)
      · Practice Question (4m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (2m)
      · Practice Question (4m)
      · PQ ×1
  - *Graph Matching – Maximal, Maximum, Perfect Matching, and Related Concepts*
      · Matching (9m)
      · PQ ×3
  - *Graph Covering – Line and Vertex Covering, Independent Set, and Minimal/Maximal Variants*
      · Minimum line covering (5m)
      · Maximum independent line set (4m)
      · Minimum vertex covering (3m)
      · Maximumj independent line set (3m)
      · PYQ ×1
      · PQ ×4
      · PYQ ×28
      · PQ ×54
- **Group Theory**
  - *Closure-Algebraic Structure, Associative-SemiGroup,  Identity-Monoid*
      · Basics of Group Theory (4m)
      · Closure Property and Algebraic Structure (5m)
      · Problems on Closure Property and Algebraic Structure (4m)
      · Associative Property and Semi-Groups (5m)
      · Problems on Associative Property and Semi-Groups (4m)
      · Identity Property and Monoid (4m)
      · Problems on Identity Property and Monoid (4m)
      · PYQ ×1
      · PQ ×1
  - *Inverse Property and  Group*
      · Inverse Property and Group (3m)
      · Questions on Inverse Property and Group (5m)
      · Properties of Group (3m)
      · PQ ×8
  - *Commutative Property and Abelian Groups*
      · Commutative Property and Abelian Group (3m)
      · 11.1 Practice Question (5m)
      · 11.2 Practice Question (2m)
      · 11.3 Practice Question (3m)
      · 11.4 Practice Question (4m)
      · 11.5 Practice Question (4m)
      · 11.6 Practice Question (2m)
      · Practice Question (3m)
      · 11.4 Practice Question (4m)
      · PYQ ×2
      · PQ ×6
  - *Classification of Finite and Infinite Groups*
      · Finite Group Practice Question (4m)
      · Finite Group & Order of group (4m)
      · Addition Modulo & Multiplication (5m)
      · Practice Questions (9m)
      · Practice Questions (5m)
      · 14.5 Practice Question (1m)
      · Practice Question (1m)
      · PQ ×1
  - *Subgroup Definition, Examples, and Verification Techniques*
      · SubGroup (4m)
      · 15.3 Practice Question (1m)
      · PQ ×1
  - *Determining the Order of Elements within Groups*
      · Order Of an Element (6m)
      · Practice Questions (5m)
      · Generating Element and Cyclic Group (4m)
      · Lagrange's Theorem (3m)
      · PQ ×1
      · PYQ ×3
      · PQ ×18
- **Propositional and Predicate Logic**
  - *Introduction to Propositions, Laws of Contradiction and Excluded Middle*
      · History Of Proposition (6m)
      · Definition Of Proposition (5m)
      · Understanding Argument (4m)
      · Law Of Contradiction (2m)
      · Law of Excluded Middle (1m)
      · PQ ×1
  - *Types of Propositions – Atomic and Compound*
      · Compound Proposition (2m)
      · PQ ×1
  - *Logical Operators – Negation, Conjunction, and Disjunction*
      · Conjuction Operation With Question (5m)
      · Disjunction Operation With Questions (3m)
      · PYQ ×1
      · PQ ×2
  - *Implication and Bi-Conditional Operators in Logic*
      · Implication Operation With Properties (7m)
      · Practice Questions (7m)
      · Practice Questions (7m)
      · Biconditional operator (2m)
      · PYQ ×1
      · PQ ×4
  - *Types of Logical Cases – Tautology, Contradiction, Contingency, Satisfiability, and Validity*
      · Type of cases (4m)
      · PYQ ×2
      · PQ ×3
  - *Introduction to First Order Predicate Logic*
      · First order Predicate Logic (8m)
      · PQ ×1
  - *Quantifiers – Universal and Existential*
      · Quantifiers (2m)
      · More on Quantifiers (6m)
      · Quantifier Negation (4m)
      · Ordering of Quantifiers (9m)
      · Existential Quantifier with Conjunction and Disjunction (5m)
      · Universal Quantifier with Conjunction and Disjunction (3m)
      · PYQ ×5
      · PQ ×7
  - *Practice Problems on Quantifiers and Predicate Logic*
      · Practice Questions (2m)
      · 19.1 Practice Questions (2m)
      · 19.3 Practice Questions (4m)
      · 19.4 Practice Questions (4m)
  - *Functional Completeness*
      · Functionality Complete Set (1m)
      · PYQ ×9
      · PQ ×19
- **Linear Algebra**
  - *Matrix and Vectors - Definition and Types*
      · Introduction to Matrix & Vectors (12m)
      · Dot Product of Vectors (4m)
      · Types of Matrices (18m)
      · Special Matrices : Orthogonal Matrix (6m)
      · Special Matrices : Idempotent Matrix (5m)
      · Special Matrices : Involutary Matrix (11m)
      · Special Matrices : Nilpotent Matrix (8m)
      · Equality of Matrices (2m)
      · PYQ ×2
      · PQ ×4
  - *Matrix Addition and Multiplication*
      · Matrix Addition & Multiplication (14m)
  - *Transpose of a Matrix*
      · Transpose of a Matrix (9m)
      · PYQ ×2
      · PQ ×1
  - *Elementary Row and Column Operations*
      · Elementary Row & Column Operations (5m)
  - *Determinant of a Matrix*
      · Determinant of a Matrix (12m)
      · Finding Determinant of Big Matrices (3m)
      · Properties of Determinants (6m)
      · Co-Factor Matrix (5m)
      · PYQ ×7
      · PQ ×8
  - *Adjoint and Inverse of a Matrix*
      · Adjoint of a Matrix (8m)
      · Properties of Adjoint, Inverse & Determinants (8m)
      · PQ ×2
  - *Rank of a Matrix*
      · Rank of a Matrix (19m)
      · Finding Rank using Gauss Elimination Method (8m)
      · Properties of Rank (6m)
      · Practice Question on Finding Rank (Q1) (5m)
      · Practice Question on Finding Rank (Q2) (4m)
      · PYQ ×1
      · PQ ×2
  - *System of Linear Equations*
      · System of Linear Equations (7m)
      · Solution Set (3m)
      · Under-determined & Over-determined System (6m)
      · Independence of System of Linear Equations (2m)
      · Consistent System of Equations (10m)
      · Elimination of Variables (Solving System of Linear Equation) (4m)
      · Echelon Form - Gauss Elimination Method (Solving Equations) (9m)
      · Diagonal Matrix- Gauss Elimination Method- Solving Equations (9m)
      · Shortcut Tricks for Solving System of Linear Equation (4m)
      · Cramer's Rule (Solving System of Linear Equation) (4m)
      · Matrix Solution (Solving System of Linear Equation) (4m)
      · Homogeneous System of Linear Equations (12m)
      · PYQ ×3
      · PQ ×2
  - *Trace of a Matrix*
      · Trace of a Matrix (17m)
      · PQ ×2
  - *Eigen Values and Eigen Vectors*
      · Eigen Values and Eigen Vectors (14m)
      · Properties of Eigen Values and Eigen Vectors (24m)
      · PQ ×10
  - *Diagonalization*
  - *LU Decomposition*
      · PQ ×2
  - *Multiple Topics*
      · PYQ ×2
      · PQ ×3
      · PYQ ×17
      · PQ ×36
- **Calculus**
  - *Limits*
      · Introduction to Limits (18m)
      · Important Properties of Limits (6m)
      · Indeterminate Forms (12m)
      · Non-Indeterminate Forms (6m)
      · Solving Limits : Substitution Method (8m)
      · Solving Limits: Tabular & Approximation Method (6m)
      · Solving Limits: Factorization Method (18m)
      · Solving Limits: Expansion Method (14m)
      · Solving Limits: L Hopital's Rule (6m)
      · Questions on L Hopital's Rule (Part 1) (23m)
      · Questions on L Hopital's Rule (Part 2) (11m)
      · Proof of L Hopital's Rule (5m)
      · Some Notable Special Limits (6m)
      · PQ ×7
  - *Continuity*
      · continuity (7m)
      · Continuity in intervals (5m)
      · Properties of Continuous Functions (1m)
      · Let's Solve Questions on Continuity (12m)
      · Types of Discontinuity (8m)
      · Gate CS 2013 - 1 Mark Question (3m)
      · Gate CS 2015 - Set 2 - 1 Mark Question (5m)
      · Gate CS 2014 - Set 1 - 2 Marks Question (6m)
      · PYQ ×2
      · PQ ×5
  - *Differentiability and Differentiation*
      · Differentiation Rules & Formulas (2m)
      · DIFFERENTIABILITY - Mathematical Definition (6m)
      · Differentiability - Geometric Definition (8m)
      · How to Geometrically identify Non-Differentiability? (5m)
      · GATE CS 2016 - Set 2 - 1 Mark Question (3m)
      · GATE CS 2014 - Set 1 - 2 Marks Question (2m)
      · Rolle’s Theorem (8m)
      · GATE CS 2014 – Set 1 – 1 Mark Question (7m)
      · Lagrange's Mean Value Theorem (6m)
      · Applications of Mean Value Theorem (8m)
      · Cauchy’s Extended Mean Value Theorem (6m)
      · PYQ ×1
      · PQ ×6
  - *Maxima and Minima*
      · Stationary Point & Critical Point (7m)
      · Maxima & Minima (13m)
      · Monotonic Functions (4m)
      · How to Mathematically find Maxima & Minima? (7m)
      · Finding Maxima & Minima (Practice Questions Set 1) (10m)
      · Finding Maxima & Minima (Practice Questions Set 2) (7m)
      · Finding Maxima & Minima (Practice Questions Set 3) (6m)
      · Finding Maxima & Minima (Practice Questions Set 4) (4m)
      · Finding Maxima & Minima (Practice Questions Set 5) (5m)
      · Finding Maxima & Minima (Practice Questions Set 6) (10m)
      · PYQ ×2
      · PQ ×2
  - *Integration*
      · Integration & Indefinite Integrals (6m)
      · Definite Integrals (10m)
      · Properties of Definite Integrals (10m)
      · All Formulas of Integration (1m)
      · Solving Integration: Substitution Method (16m)
      · Solving Integration: Partial Fractions Method (14m)
      · Complications in Partial Fractions Method (11m)
      · Solving Integration: Integration by Parts Method (10m)
      · GATE Question on Integration by Parts Method (7m)
      · GATE CS 2000 Question (7m)
      · GATE CS 2009 Question (4m)
      · GATE CS 2011 – 2 Marks Question (11m)
      · GATE CS 2014 – Set 3 Question (8m)
      · PYQ ×4
      · PQ ×7
  - *Multiple Topics*
      · PYQ ×3
      · PQ ×6
  - *Numerical Methods*
      · PYQ ×7
      · PQ ×23
      · PYQ ×19
      · PQ ×56
      · PYQ ×89
      · PQ ×246
      · Coal India - Unit Test - Engineering Mathematics (45m)

### 16. Coal India Mock Test — 0 vids · 9.0h · 0 PYQs · 0 PQs

      · 23 July - Coal India - Full Mock Test 1 (3.0h)
      · 27 July - Coal India - Full Mock Test 2 (3.0h)
      · 31 July - Coal India - Full Mock Test 3 (3.0h)

---

## IOCL P2 Test Series

`IOCL-ENGINEERSOFFICERS-GRADE-A-CS-PAPER-2-TEST-SERIES` · **0 videos / 0.0h** · 0 PYQs · 0 PQs · 1 subtopics · 23 tests · 1 notes

### 0. Test Schedule — 0 vids ·  · 0 PYQs · 0 PQs

- **About the Course**
  - *Study Plan & Test Schedule*

### 1. Technical Subject Unit Tests — 0 vids · 8.2h · 0 PYQs · 0 PQs

      · IOCL - Unit Test - Engineering Mathematics (45m)
      · IOCL - Unit Test - Computer Networks (45m)
      · IOCL - Unit Test - Programming & Data Structures (45m)
      · IOCL - Unit Test - Digital Logic (45m)
      · IOCL - Unit Test - Computer Architecture (45m)
      · IOCL - Unit Test - Operating Systems (45m)
      · IOCL - Unit Test - Database Management Systems (45m)
      · IOCL - Unit Test - Computer Networks (45m)
      · IOCL - Unit Test - Algorithms (45m)
      · IOCL - Unit Test - Theory of Computation (45m)
      · IOCL - Unit Test - Compiler Design (45m)

### 2. CS/IT Sectional Mock Tests — 0 vids · 7.5h · 0 PYQs · 0 PQs

      · IOCL - Mock Test - CS/IT Sectional — Test 1 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 2 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 3 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 4 (1.5h)
      · IOCL - Mock Test - CS/IT Sectional — Test 5 (1.5h)

### 3. Complete Paper Full Mock Test — 0 vids · 17.5h · 0 PYQs · 0 PQs

      · IOCL - Complete Paper Mock Tests — Test 1 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 2 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 3 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 4 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 5 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 6 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 7 (2.5h)

---

## IOCL P1 Test Series

`IOCL-ENGINEERSOFFICERS-GRADE-A-GENERAL-APTITUDE-PAPER-1-TEST-SERIES` · **0 videos / 0.0h** · 0 PYQs · 0 PQs · 0 subtopics · 15 tests · 0 notes

### 0. Unit Tests — 0 vids · 1.0h · 0 PYQs · 0 PQs

      · IOCL Unit Test - Verbal Ability (20m)
      · IOCL Unit Test - Logical Reasoning (20m)
      · IOCL Unit Test - Quantitative Aptitude (20m)

### 1. Full-Length Mock Tests — 0 vids · 5.0h · 0 PYQs · 0 PQs

      · IOCL Mock Test - 1 - General Aptitude (1.0h)
      · IOCL Mock Test - 2 - General Aptitude (1.0h)
      · IOCL Mock Test - 3 - General Aptitude (1.0h)
      · IOCL Mock Test - 4 - General Aptitude (1.0h)
      · IOCL Mock Test - 5 - General Aptitude (1.0h)

### 2. Complete Paper Full Mock Test — 0 vids · 17.5h · 0 PYQs · 0 PQs

      · IOCL - Complete Paper Mock Tests — Test 1 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 2 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 3 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 4 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 5 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 6 (2.5h)
      · IOCL - Complete Paper Mock Tests — Test 7 (2.5h)

---

