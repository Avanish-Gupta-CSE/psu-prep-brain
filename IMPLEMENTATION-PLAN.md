# PSU Prep Implementation Plan

Last updated: 22 Apr 2026

## Objective

Turn this workspace into a durable, GitHub-backed exam preparation system that:

1. lives in a private GitHub repository
2. keeps `.brain` as the single source of truth for progress and planning
3. separates shared CS/GATE-style preparation from exam-specific preparation
4. supports dedicated GitHub Copilot agents for shared-core, HPCL, IFFCO, and MSTC
5. stays synchronized through common tracking files instead of fragmenting into disconnected notes

## Current State

The workspace currently contains:

- `.brain/` with study tracking, exam tracking, syllabus, weak areas, motivation, and MSTC GD notes
- `.cursor/rules/psu-prep.mdc` with the original operating rules for the prep system
- `MSTC/` with MSTC source PDFs
- `Resume-Berkadia.tex` for career-history and interview prep

Current structural gaps:

- no GitHub remote configured yet or verified as usable
- no `.github/` Copilot customization layer
- no `Shared-Core/` directory for common subjects
- no `HPCL/` directory
- no `IFFCO/` directory
- no MSTC interview-specific working documents
- `.brain` is still mostly in March 2026 state and must be synchronized to 22 Apr 2026

## Non-Negotiable Design Rules

### 1. Shared Memory Rule

`.brain` remains the canonical memory system.

All exam-specific agents may read their own directories, but they must treat the following files as shared state:

- `.brain/Progress.md`
- `.brain/ExamTracker.md`
- `.brain/StudyPlan.md`
- `.brain/Syllabus.md`
- `.brain/WeakAreas.md`
- `.brain/MockTestLog.md`
- `.brain/Motivation.md`

### 2. Separation Rule

Keep common preparation separate from exam-specific overlays.

- `Shared-Core/` will contain reusable technical prep
- `HPCL/` will contain HPCL-only framing, deadlines, mock strategy, and selection-process notes
- `IFFCO/` will contain IFFCO-only role fit, technology gap closure, and interview/exam notes
- `MSTC/` will continue to hold source files and will gain interview-prep documents

### 3. Source Integrity Rule

Every exam folder should distinguish between:

- `Confirmed` facts from official advertisement, official website, admit-card notes, syllabus PDFs, or application portal
- `Inferred` pattern notes from previous-year trends, mock tests, forum reports, or overlap reasoning

Never mix official instructions and inferred patterns in the same section without labeling them.

### 4. Priority Rule

Until HPCL CBT on 3 May 2026:

- 70% effort: HPCL + Shared-Core
- 20% effort: IFFCO-specific stack gaps
- 10% effort: MSTC interview readiness

After HPCL:

- 60% effort: IFFCO
- 25% effort: Shared-Core retention
- 15% effort: MSTC interview readiness until MSTC results/interview movement happens

## Implementation Order

This order is deliberate. Each step reduces ambiguity for the next one.

### Phase 1: Repository Foundation

#### Task 1. Verify local git state

Goal:

- confirm whether the workspace is already a git repository
- check current branch
- check whether a remote exists
- inspect working tree status before any wider changes

Validation:

- `git rev-parse --is-inside-work-tree`
- `git status --short`
- `git remote -v`

#### Task 2. Create private GitHub repository

Repository name:

- `psu-prep-brain`

Requirements:

- private visibility
- set remote origin
- push the current branch
- ensure all current files are included, including `.brain`, MSTC PDFs, and resume

Validation:

- `gh repo view`
- `git remote -v`
- `git push -u origin <branch>` succeeds

### Phase 2: GitHub Copilot Foundation

Create the core `.github` customization structure:

- `.github/copilot-instructions.md`
- `.github/instructions/`
- `.github/prompts/`
- `.github/agents/`
- `AGENTS.md`

Purpose of each:

- `copilot-instructions.md`: repository-wide operating contract
- `.github/instructions/*.instructions.md`: path-specific behavior for `.brain`, `Shared-Core`, `HPCL`, `IFFCO`, `MSTC`
- `.github/prompts/*.prompt.md`: repeatable workflows such as daily planning, study session, mock review, interview drill, and sync-to-brain
- `.github/agents/*.agent.md`: dedicated prep agents for shared-core, HPCL, IFFCO, and MSTC
- `AGENTS.md`: shared sync contract that all agents follow when reading and writing workspace state

Validation:

- files exist in the expected locations
- VS Code Copilot customizations can discover the repository instructions and prompt/agent files

### Phase 3: Brain Synchronization

Update the March-stale state to 22 Apr 2026.

Files to update:

- `.brain/Progress.md`
- `.brain/ExamTracker.md`
- `.brain/StudyPlan.md`
- `.brain/Syllabus.md`
- `.brain/WeakAreas.md`

Expected outcome:

- HPCL becomes the active sprint
- IFFCO is added as a next-urgent exam track
- MSTC is marked as post-GD, waiting for result/interview, with interview-readiness continuing in the background
- shared-core topics reflect current focus rather than the old March phase-only state

Validation:

- `Progress.md` no longer claims Phase 1 MSTC GD is still active
- `ExamTracker.md` correctly reflects current urgency ordering
- `StudyPlan.md` aligns with actual remaining days before HPCL and roughly one month for IFFCO

### Phase 4: Shared-Core Layer

Create `Shared-Core/` for the reusable technical foundation.

Proposed structure:

```text
Shared-Core/
  README.md
  Overlap-Matrix.md
  Digital-Logic/
    README.md
  COA/
    README.md
  Programming-Concepts/
    README.md
  DSA/
    README.md
  Operating-Systems/
    README.md
  DBMS/
    README.md
  Computer-Networks/
    README.md
  Information-Security/
    README.md
  Emerging-Technologies/
    README.md
  Aptitude/
    README.md
```

What each subject README should contain:

- topic breakdown
- exam relevance mapping
- high-yield subtopics
- known weak areas
- likely question forms
- short revision order

Validation:

- overlap matrix clearly maps Shared-Core subjects to HPCL, IFFCO, and MSTC interview relevance

### Phase 5: HPCL Track

Create `HPCL/` as the main active exam directory.

Proposed structure:

```text
HPCL/
  README.md
  Official-Sources.md
  Selection-Process.md
  Syllabus-Breakdown.md
  Previous-Pattern-Notes.md
  Eleven-Day-Sprint.md
  Mock-Strategy.md
  Progress-Log.md
```

Confirmed official anchors already identified:

- HPCL job openings page
- official IS Officer syllabus link
- official selection methodology link
- official mock test link
- official detailed advertisement link

What the HPCL track must emphasize:

- official syllabus sections
- what belongs to shared-core vs HPCL-specific framing
- CBT strategy before 3 May 2026
- probable weighting and question-style notes clearly marked as inferred where not directly official

Validation:

- `Official-Sources.md` clearly lists URLs and what each source confirms
- `Syllabus-Breakdown.md` mirrors the official scope closely
- `Eleven-Day-Sprint.md` is day-addressable and realistic given work schedule

### Phase 6: IFFCO Track

Create `IFFCO/` as the second active exam directory.

Proposed structure:

```text
IFFCO/
  README.md
  Confirmed-Advertisement-Details.md
  Selection-Process-Assumptions.md
  Role-Fit-Against-Resume.md
  Oracle-PLSQL-Track.md
  DotNet-EntityFramework-Awareness.md
  Application-Servers-And-Web.md
  One-Month-Plan.md
  Mock-And-Interview-Log.md
```

Confirmed facts available from the user-provided image and live application page:

- role: Officer / Senior Officer (IT)
- number of posts: seven
- age: 21 to 27 years as on 1 Apr 2026 with category relaxations
- qualification: IT / Computer Science / AI bachelor degree
- experience: maximum up to 5 years post-qualification
- technical expectations include Oracle database, SQL, PL/SQL, entity framework core, C, C#, bootstrap, Node.js, React, Hindi and English
- application deadline visible in image: latest by 28 Apr 2026

What the IFFCO track must emphasize:

- user’s fit versus the role
- current strength overlap from MERN, databases, and enterprise work
- targeted gap closure for Oracle / PL-SQL and Microsoft stack awareness
- clear separation between confirmed ad facts and inferred exam/interview patterns

Validation:

- `Role-Fit-Against-Resume.md` directly maps experience from `Resume-Berkadia.tex`
- `One-Month-Plan.md` is consistent with the application window and expected follow-up stages

### Phase 7: MSTC Interview Continuation

Extend MSTC from GD prep into interview prep.

Proposed additions under `MSTC/`:

```text
MSTC/
  README.md
  Interview-Prep.md
  HR-Question-Bank.md
  Behavioral-Leadership-Questions.md
  Career-Story-Bank.md
  Mock-Interview-Tracker.md
```

What this track must emphasize:

- PSU-appropriate HR responses
- behavioral questions in STAR format
- Amazon leadership-type questions adapted into general leadership/ownership/problem-solving language
- career-story translation from `Resume-Berkadia.tex`
- why PSU, why MSTC, why transition from private sector, and project-based impact stories

Validation:

- stories are grounded in actual resume experience and not generic interview filler
- `Career-Story-Bank.md` is reusable across MSTC and IFFCO interviews

### Phase 8: Dedicated Copilot Agents

Create four specialized GitHub Copilot agents.

Planned agent files:

- `.github/agents/gate-core.agent.md`
- `.github/agents/hpcl.agent.md`
- `.github/agents/iffco.agent.md`
- `.github/agents/mstc.agent.md`

Agent responsibilities:

- `gate-core`: maintain shared technical core and overlap mapping
- `hpcl`: manage HPCL sprint execution and update shared-core progress where applicable
- `iffco`: manage IFFCO-specific stack-gap closure and interview fit
- `mstc`: maintain interview readiness and resume-based answer bank

All agents must follow the same sync rules:

1. read `.brain/Progress.md` and `.brain/ExamTracker.md` first
2. respect the active exam priority
3. reuse shared-core instead of duplicating notes
4. write progress back to `.brain` when study is performed

Validation:

- each agent file explicitly states shared reads, owned scope, and write-back rules

### Phase 9: Reusable Prompt Files

Planned prompt files:

- `.github/prompts/daily-plan.prompt.md`
- `.github/prompts/study-session.prompt.md`
- `.github/prompts/mock-review.prompt.md`
- `.github/prompts/interview-drill.prompt.md`
- `.github/prompts/sync-brain.prompt.md`

Purpose:

- standardize repeatable interactions
- reduce friction when switching between agents
- make it easy to restart progress after interruptions

Validation:

- each prompt refers to the relevant shared and exam-specific files

### Phase 10: Final Validation

Final pass checklist:

1. repository exists on GitHub and is private
2. remote is configured correctly
3. current branch is pushed successfully
4. `.github` structure exists and is readable
5. shared-core exists
6. HPCL exists
7. IFFCO exists
8. MSTC interview documents exist
9. `.brain` reflects April 2026 reality
10. agents and prompts are discoverable and internally consistent

## Confirmed External Facts Already Gathered

### HPCL

Confirmed from HPCL job openings page:

- `Recruitment of Officers 2026` entry exists
- CBT scheduled for 3 May 2026
- official links are exposed for:
  - detailed advertisement
  - mock test
  - IS Officers syllabus
  - selection methodology

### IFFCO

Confirmed from user-provided image and application page:

- post is Officer / Senior Officer (IT)
- seven posts
- age 21 to 27 years as on 1 Apr 2026 with relaxations
- maximum up to 5 years post-qualification experience
- role expects Oracle database, SQL, PL/SQL, entity framework core, C, C#, bootstrap, Node.js, React
- application deadline shown as 28 Apr 2026

## Working Time Constraints

From the established profile:

- weekdays: about 6:00 to 7:30 AM and 9:00 to 11:00 PM
- work hours: 11 AM to 8 PM
- weekends: 4 to 6 hours realistic

This means implementation plans and study plans must remain realistic and time-bounded.

## Operating Principle For Execution

Implementation will proceed in narrow validated slices.

The next live execution order should be:

1. verify git state and remote/auth
2. create the private GitHub repo and push
3. add `.github` foundation files
4. sync `.brain`
5. add `Shared-Core/`
6. add `HPCL/`
7. add `IFFCO/`
8. add MSTC interview docs
9. add agents and prompts
10. validate the full workspace

## Immediate Next Task

The next task to execute after this plan file is:

`Verify git state, remote configuration, and GitHub CLI authentication.`