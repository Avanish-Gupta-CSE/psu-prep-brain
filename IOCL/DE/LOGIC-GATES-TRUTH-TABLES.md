# Logic Gates — Truth Tables & Properties Matrix ★ REVISION SHEET (IOCL · Digital Logic)

> 🎯 **Target:** Recite all 6 gate truth tables in <10 sec + know exactly which algebraic laws each gate satisfies (idempotent · commutative · associative · distributive · identity).
> ⏱️ **Read time:** 8 min · **Print version:** `LOGIC-GATES-TRUTH-TABLES.pdf` (same folder — 2 pages, pin above desk).
> *See also:* `Notes/Shared-Core/DIGITAL-LOGIC.md` (concept base) — this sheet is the exam-ready extract.

---

## 1. Definition — gate & truth table

- **Logic gate** = a physical circuit that computes one Boolean function of its inputs.
- **Truth table** = the exhaustive input → output map (2ⁿ rows for n inputs). It is the *identity card* of a gate.
- **The six basic gates:**
  - Basic: **AND · OR · NOT**
  - Universal: **NAND · NOR** (each alone can build any gate)
  - Function-specific: **XOR** (parity/difference) · **XNOR** (equality)

---

## 2. Master Truth Table — all 6 gates (2-input)

| A | B | **AND** A·B | **OR** A+B | **NAND** (A·B)′ | **NOR** (A+B)′ | **XOR** A⊕B | **XNOR** A⊙B |
|:-:|:-:|:-----------:|:----------:|:---------------:|:--------------:|:-----------:|:------------:|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

**Fast recall (memorize the shape, not the rows):**

- **AND** — "sab chahiye": 1 **only** in bottom row (1,1)
- **OR** — "koi bhi chale": 0 **only** in top row (0,0)
- **NAND** = AND inverted → 0 **only** at (1,1)
- **NOR** = OR inverted → 1 **only** at (0,0)
- **XOR** — 1 in the **two middle rows** (inputs **differ**; odd count of 1s = parity gate)
- **XNOR** — 1 at **(0,0) and (1,1)** (inputs **same**; equality detector)

---

## 3. Properties Matrix ★ (the part you print)

| Property | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|---|---|---|---|---|
| **Idempotent**<br>X op X = X | ✅ X·X = X | ✅ X+X = X | ❌ X↑X = X′ | ❌ X↓X = X′ | ❌ X⊕X = **0** | ❌ X⊙X = **1** |
| **Commutative**<br>A op B = B op A | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Associative**<br>(A op B) op C = A op (B op C) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ ★trap |
| **Distributive** | ✅ over OR & XOR | ✅ over AND | ❌ | ❌ | ❌ over AND * | ❌ |
| **Identity element e**<br>X op e = X | e = **1** | e = **0** | none | none | e = **0** | e = **1** |
| **Constant (output independent of X)** | X·0 = 0 | X+1 = 1 | X↑0 = 1 | X↓1 = 0 | — | — |
| **Complement law**<br>X op X′ | X·X′ = 0 | X+X′ = 1 | X↑X′ = **1** | X↓X′ = **0** | X⊕X′ = **1** | X⊙X′ = **0** |
| **Universal gate?** | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |

*\* BUT note:* **AND distributes over XOR** → A·(B⊕C) = A·B ⊕ A·C ✅

**Summary to burn in:**

- **All 6 gates are commutative.**
- **Associative: AND · OR · XOR · XNOR** — mnemonic **A-O-X-X**. **NAND/NOR are NOT associative.**
- **Idempotent + distributive (both): only AND and OR** — they form Boolean algebra proper.
- **Universal: only NAND and NOR.**
- **XNOR IS associative** — classic trap MCQ.

---

## 4. Worked Examples (PYQ patterns)

**Example 1 — Build OR from NAND only:**
A + B = (A↑A) ↑ (B↑B). Verify A=0, B=1: (0↑0)=1 → (1↑1)=0 → 1↑0 = **1** ✓

**Example 2 — Build AND from NOR only:**
A · B = (A↓A) ↓ (B↓B). Verify A=1, B=0: (1↓1)=0 → (0↓0)=1 → 0↓1 = **0** ✓

**Example 3 — XOR associativity in a full adder:**
Sum = A ⊕ B ⊕ Cin — bracket order never changes the result; hardware chains XORs. Carry = AB + Cin(A⊕B).

**Example 4 — Trap check:**
X ⊕ X = **0** (not X!) · X ⊙ X = **1** · X ⊕ 0 = X · X ⊕ 1 = X′ (XOR = programmable inverter).

---

## 5. Mnemonics (Hinglish)

- **Gate outputs:** "**A**nd **S**ab **C**hahiye · **O**r **K**oi **B**hi **C**hale · **X**OR **A**lag-**A**lag · **X**NOR **E**k **J**aise"
- **Associative gates:** "**A-O-X-X**" → "**A**ur / **O**r / **X**or / **X**nor — **A**ssociative inko aata hai" (NAND/NOR fail)
- **Idempotent:** "**A**ur **O**r hi **A**pne-**A**ap hain (X·X=X) — baaki sab bigadte hain"
- **Universal:** "**N**AND **N**OR — **N**aya gate **N**ikalo (koi bhi)"

---

## 6. Quick Cheat Sheet

- **Universal recipes:** NOT = A↑A = A↓A · OR-from-NAND = (A↑A)↑(B↑B) · AND-from-NAND = (A↑B)↑(A↑B) · AND-from-NOR = (A↓A)↓(B↓B) · OR-from-NOR = (A↓B)↓(A↓B)
- **De Morgan:** (A·B)′ = A′ + B′ · (A+B)′ = A′·B′ — NAND/NOR are the dual pair
- **XOR magic:** X⊕0 = X · X⊕1 = X′ · X⊕X = 0 · X⊕X′ = 1 · n-chain XOR = **parity** (odd # of 1s → 1) · self-inverse: A⊕B⊕B = A
- **XNOR:** equality detector · n-chain XNOR = 1 for an **even** number of 1s (incl. zero)
- **MCQ favourites:** NAND/NOR commute but are **not** associative/distributive · XNOR **is** associative · only AND/OR are idempotent

---

## 7. 40-Second Script (interview / viva)

"There are six basic logic gates. AND gives 1 only when all inputs are 1; OR gives 1 when at least one input is 1. NAND and NOR are their inverses — and both are universal, meaning each alone can implement any Boolean function. XOR gives 1 when inputs differ — it's the parity gate; XNOR gives 1 when inputs are equal — the equality detector. On properties: all six gates are commutative; AND, OR, XOR and XNOR are associative — NAND and NOR are not; and only AND and OR are idempotent, because for example X XOR X equals 0, not X. De Morgan ties NAND and NOR together: complement of AB is A′+B′. For example, in a full adder the sum A⊕B⊕Cin uses XOR's associativity, and the carry uses AND and OR."

---

## 8. Follow-up Questions

**Q1. Is XNOR associative?**
A: **Yes** — (A⊙B)⊙C = A⊙B⊙C = 1 when an even number of 1s. Classic trap: most assume only AND/OR/XOR are associative.

**Q2. Why are NAND/NOR called universal?**
A: Each can implement NOT (A↑A), then AND and OR — hence any Boolean function (sum-of-products + De Morgan). {NAND} or {NOR} alone = functionally complete.

**Q3. Which gates are associative but NOT idempotent?**
A: XOR and XNOR — chains (A⊕B)⊕C work fine, but X⊕X = 0 breaks idempotence.

**Q4. What is the identity element of XOR? And why "programmable inverter"?**
A: e = 0 (X⊕0 = X). XOR with 1 flips the bit (X⊕1 = X′) — so a control input can invert or pass any signal.
