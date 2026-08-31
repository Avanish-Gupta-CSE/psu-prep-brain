# Context gathering for project references

| Metadata | Value |
| :--- | :--- |
| **Chat ID** | `7a49e142-7255-4739-b68b-adbcd46e223b` |
| **Created At** | `2026-05-20 06:41:47` |
| **Last Updated At** | `2026-05-20 06:41:56` |
| **Files Touched / Summary** | Read Progress.md, NextSteps.md, copilot-instructions.md |
| **Model** | `gemini-3.1-pro` |

---

## 👤 User Message #1

Can you get the context based on @.brain @.cursor @MSTC @CN @DBMS @DSA 
@.github/copilot-instructions.md 

and then come back to me after getting this with your findings

---

## 🤖 Assistant Response

I have successfully gathered the context from the requested directories and files. Here is a summary of my findings regarding your PSU preparation workspace:

### 1. Repository Structure & Operating Rules (`.github/copilot-instructions.md` & `.cursor`)
*   **System Architecture:** The workspace is a personal exam-preparation system for PSU roles. It uses `.brain/` as the persistent memory layer and specific folders like `MSTC/`, `CN/`, `DBMS/`, and `DSA/` for subject and exam-specific materials.
*   **Note Creation Standards:** 
    *   Every study note must include a target and read time.
    *   **Mnemonics are mandatory** for lists of 4+ items, with a strong preference for "Hinglish" (Hindi + English).
    *   **Interview Scripts:** Major topics require a 20s or 40s conversational script ending with a concrete example.
    *   **Diagrams:** Use Mermaid for flowcharts/hierarchies, ASCII art for memory layouts, and Markdown tables for comparisons.
*   **Cursor Configs:** The `.cursor` directory contains your `hooks.json`, a `brain-sync.ps1` script, and the older `psu-prep.mdc` rule file which forms the basis for the Copilot instructions.

### 2. Current State & Progress (`.brain`)
*   **Immediate Situation:** According to `.brain/NextSteps.md` and `.brain/Progress.md`, you are currently in **Phase 2: MSTC MT (Systems) Final Interview Sprint**.
*   **Critical Deadline:** Your MSTC interview is scheduled for **21 May 2026 at 9:00 A.M.** in New Delhi.
*   **Current Focus:** The priority is strictly "MSTC only". You are focusing on the **"Core-4 basics"** (DBMS, OS, Computer Networks, DSA) and running daily **7-minute lightning technical drills**, as recent intel suggests the technical panels might be very short.
*   **Logistics:** You have travel planned for 19 May, with 20 May reserved as a revision and logistics day.

### 3. MSTC Interview Prep (`MSTC`)
*   **Planning & Tracking:** Contains your master plan (`MASTER-PLAN-2026-05-15-to-21.md`), daily plans, and a `MOCK-INTERVIEW-TRACKER.md` to log weak answers from your mock sessions.
*   **Question Banks:** Highly structured into `TECHNICAL-QUESTION-BANK.md`, `HR-QUESTION-BANK.md`, and `BEHAVIORAL-QUESTION-BANK.md`.
*   **Company Research:** Includes deep dives into MSTC's vision, mission, objectives (with mnemonics), and domain-based questions.
*   **Quick Revision:** Contains a `Quick Revision Ebook` folder with scripts and markdown files to help you compress theory into fast-recall answers.

### 4. Core Technical Subjects (`CN`, `DBMS`, `DSA`)
These folders contain your reusable "Shared-Core" notes, structured for quick revision:
*   **`CN` (Computer Networks):** Notes on Data Communication, OSI Model, and Network Topologies.
*   **`DBMS` (Database Management Systems):** Comprehensive notes covering 12 key areas including Keys, Normalization, Joins, SQL Traps, ACID properties, and Functional Dependencies.
*   **`DSA` (Data Structures & Algorithms):** 5 core modules covering Arrays, Linked Lists/Stacks/Queues, Trees/Graphs, Heaps/Hashing, and Sorting/Complexity.

**Next Steps:**
Based on your `.brain/NextSteps.md`, your immediate goals are to finish the OS notes, run 2 timed mixed mocks, and focus on your repair lists before your travel day. 

How would you like to proceed? We can run a 7-minute lightning drill, review a specific topic from the Core-4, or work on your 40s interview scripts!

---
