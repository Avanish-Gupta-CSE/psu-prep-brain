# IFFCO CBT Portal Practice Simulator (Practice Only)

This is a **practice-only** simulator designed to perfectly replicate the user experience, layout, and features of the official IFFCO CBT (Computer-Based Test) portal. It is built to help you build muscle memory, manage time pressure, and practice navigation under realistic exam conditions.

It is **not** intended for use during any real assessment/exam.

---

## Key Features (Portal-Accurate)

- **Dashboard Screen**: Replicates the official "My Examinations" dashboard, showing the mandatory Practice Exam and the actual GET Computer Science Exam.
- **System Check Screen**: Simulates the pre-exam device check, requesting webcam access to verify your camera, browser, full-screen mode, clock, and server connectivity. Includes a graceful animated fallback if camera access is denied.
- **Split-Pane CBT Layout**:
  - **Left Pane**: Displays the active question category, question prompt, radio options, and navigation buttons.
  - **Right Sidebar**: Shows your live webcam proctoring feed ("MONITORED IN THE ACTUAL EXAM") and the **NAVIGATOR** box.
- **Backtracking & Direct Jump**: Supports going back to previous questions using the `< Previous` button, or jumping directly to any question by clicking its numbered circle in the **NAVIGATOR** grid.
- **Flag for Review**: Allows flagging questions for later review, which turns their navigator circle orange.
- **Clear Answer**: Allows clearing your selected option for the current question.
- **Theme Toggle**: Supports toggling between the official light theme (default) and a dark theme via the moon/sun icon in the header.

---

## Supported Modes

1. **GET Computer Science Exam (Confirmed Real Pattern)**:
   - **100 questions / 60 minutes (1 hour)**
   - Distribution: `100 technical`
2. **Practice Exam (Mandatory Practice Mode)**:
   - **10 questions / 10 minutes**
   - Distribution: `10 GK/Mixed`
3. **Mode A (Rumored Old Pattern)**:
   - **150 questions / 45 minutes**
   - Distribution: `100 technical + 10 quant + 10 reasoning + 10 GK + 10 IFFCO + 10 English`
4. **Mode B (Coaching Pattern)**:
   - **120 questions / 120 minutes**
   - Distribution: `80 technical + 10 quant + 10 reasoning + 10 GK + 10 English`

---

## Keyboard Shortcuts

The simulator supports comprehensive keyboard shortcuts to maximize your speed and minimize trackpad usage:

- `1` `2` `3` `4`: Select option A, B, C, or D
- `Space` or `F`: Toggle Flag for Review
- `C`: Clear Selected Answer
- `←` or `P`: Previous Question
- `→` or `N` or `Enter`: Next Question

---

## Run Locally

### Option 1 (Simplest)
Open `index.html` directly in your browser.

### Option 2 (Recommended)
Serve the folder with a local server to avoid browser file/camera security restrictions:

```powershell
cd "c:\Users\agupt1\Projects\Personal\psu-prep-brain\IFFCO\simulator"
python -m http.server 5173
```

Then open `http://localhost:5173` in Google Chrome.

---

## Question Bank

Questions live in `question-bank.js` as a simple array of objects:

```js
{
  id: "tech_dbms_001",
  tag: "technical", // technical | quant | reasoning | english | gk | iffco
  prompt: "Which normal form removes partial dependency?",
  options: ["1NF", "2NF", "3NF", "BCNF"],
  answerIndex: 1
}
```

You can add more questions by following the same schema. If a test mode requests more questions for a category than what is available in the bank, the simulator will automatically sample with replacement and print a warning in the console.
