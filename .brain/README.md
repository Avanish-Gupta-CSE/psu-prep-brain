# PSU Prep Brain-Complex

This directory is the persistent memory system for Avanish Gupta's PSU/Government exam preparation. It maintains context across Cursor chat sessions so that every new conversation picks up exactly where the last one left off.

## How This System Works

### For Cursor AI (Instructions)

**At the start of every new conversation:**
1. Read `.brain/NextSteps.md` -- get the current resume point and immediate next actions
2. Read `.brain/Progress.md` -- understand current phase, last session, and recent work
3. Read `.brain/ExamTracker.md` -- know which exams are upcoming and their priority
4. Check the current date against exam dates to auto-determine the active study phase

**During the conversation:**
- Follow the "Active Interleaving" teaching method:
  1. Give a compressed, bulleted summary of the concept (high-yield only)
  2. Provide code snippets / SQL queries for dry-running or bug-finding
  3. Immediately generate 3-5 GATE-level MCQs with negative marking simulation
  4. Wait for the student's answers before revealing solutions
  5. Give direct, technical feedback on wrong answers -- explain exactly where logic failed
- Never teach basic syntax -- the student is a working professional with 1.5+ years of industry experience
- Focus on edge cases that examiners love to test
- Track which topics were covered and update WeakAreas if the student struggles

**At the end of every conversation:**
- Update `.brain/NextSteps.md` if the immediate resume point or next actions changed
- Update `.brain/Progress.md` with: date, topics covered, questions attempted, accuracy, next goals
- Update `.brain/WeakAreas.md` if new weak areas were identified
- Update `.brain/MockTestLog.md` if any mock/practice scores were discussed
- Increment the streak counter if study happened today

### File Map

| File | Purpose | Update Frequency |
|------|---------|-----------------|
| `README.md` | This file -- system overview | Rarely |
| `NextSteps.md` | Canonical handoff and immediate next actions | Every session that changes priorities |
| `Profile.md` | Student profile, eligibility, constraints | On life changes |
| `Progress.md` | Session log, streak, current phase | Every session |
| `ExamTracker.md` | All exams: dates, status, patterns | When exam info changes |
| `StudyPlan.md` | Phase-based study schedule | When phases shift |
| `Syllabus.md` | Master topic list with completion % | After topic completion |
| `WeakAreas.md` | Topics needing extra focus | When weaknesses found |
| `MockTestLog.md` | Mock/PYQ scores and analysis | After every mock |
| `Motivation.md` | Streaks, milestones, recovery log | Every session |
| `QuickReference.md` | Formulae, shortcuts, exam-day tips | As topics are studied |

### Teaching Philosophy

The student failed GATE 2026 (CS: 21, DA: 28), failed BEL MT and BDL MT CBTs, and is recovering from a 1-1.5 month motivation slump. The approach must be:

- **Phase-locked**: Focus only on the next upcoming exam, not everything at once
- **High-yield**: Teach only what examiners test, skip low-probability topics
- **Active**: Questions first, theory second -- the student learns by doing
- **Direct**: No sugar-coating, no excessive encouragement -- just clear technical feedback
- **Progress-visible**: Always reference completion %, streaks, and upcoming milestones
