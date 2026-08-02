/* global window, alert, confirm */

(() => {
  // Exam Modes Configuration
  const MODES = {
    cbt1Exam: {
      key: "cbt1Exam",
      label: "IFFCO GET CBT 1 — Full 100 Verified Questions Mock",
      badge: "100% CBT 1 RECALL",
      totalQuestions: 100,
      durationSec: 60 * 60, // 1 hour
      distribution: {
        cbt1: 100,
      },
    },
    cbt1_part1: {
      key: "cbt1_part1",
      label: "IFFCO CBT 1 — Part 1 (Q1 – Q10: DBMS, Security & OS)",
      badge: "PART 1 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60, // 6 minutes
      cbt1Range: [0, 10],
    },
    cbt1_part2: {
      key: "cbt1_part2",
      label: "IFFCO CBT 1 — Part 2 (Q11 – Q20: Compiler, DSA & ACID)",
      badge: "PART 2 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [10, 20],
    },
    cbt1_part3: {
      key: "cbt1_part3",
      label: "IFFCO CBT 1 — Part 3 (Q21 – Q30: OS Scheduling, Algo & TOC)",
      badge: "PART 3 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [20, 30],
    },
    cbt1_part4: {
      key: "cbt1_part4",
      label: "IFFCO CBT 1 — Part 4 (Q31 – Q40: Cache, Indexing & Concurrency)",
      badge: "PART 4 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [30, 40],
    },
    cbt1_part5: {
      key: "cbt1_part5",
      label: "IFFCO CBT 1 — Part 5 (Q41 – Q50: Data Structures & Parsing)",
      badge: "PART 5 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [40, 50],
    },
    cbt1_part6: {
      key: "cbt1_part6",
      label: "IFFCO CBT 1 — Part 6 (Q51 – Q60: SDLC, IR, B+ Trees & Networks)",
      badge: "PART 6 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [50, 60],
    },
    cbt1_part7: {
      key: "cbt1_part7",
      label: "IFFCO CBT 1 — Part 7 (Q61 – Q70: ML, System Design & Architecture)",
      badge: "PART 7 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [60, 70],
    },
    cbt1_part8: {
      key: "cbt1_part8",
      label: "IFFCO CBT 1 — Part 8 (Q71 – Q80: DBMS Triggers, Locks & REST)",
      badge: "PART 8 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [70, 80],
    },
    cbt1_part9: {
      key: "cbt1_part9",
      label: "IFFCO CBT 1 — Part 9 (Q81 – Q90: Complexity, SJF & Consistent Hashing)",
      badge: "PART 9 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [80, 90],
    },
    cbt1_part10: {
      key: "cbt1_part10",
      label: "IFFCO CBT 1 — Part 10 (Q91 – Q100: Idempotency, Cloud & Distributed Systems)",
      badge: "PART 10 (10 Qs)",
      totalQuestions: 10,
      durationSec: 6 * 60,
      cbt1Range: [90, 100],
    },
    realExam: {
      key: "realExam",
      label: "GET Computer Science Exam (Mixed Technical)",
      badge: "GET EXAM",
      totalQuestions: 100,
      durationSec: 60 * 60, // 1 hour
      distribution: {
        cbt1: 70,
        technical: 30,
      },
    },
    practiceExam: {
      key: "practiceExam",
      label: "Mock Exam — General Knowledge",
      badge: "PRACTICE",
      totalQuestions: 10,
      durationSec: 10 * 60, // 10 minutes
      distribution: {
        gk: 10,
      },
    },
    modeA: {
      key: "modeA",
      label: "Mode A (Rumored Old Pattern)",
      badge: "RUMORED",
      totalQuestions: 150,
      durationSec: 45 * 60, // 45 minutes
      distribution: {
        technical: 100,
        quant: 10,
        reasoning: 10,
        gk: 10,
        iffco: 10,
        english: 10,
      },
    },
    modeB: {
      key: "modeB",
      label: "Mode B (Coaching Pattern)",
      badge: "COACHING",
      totalQuestions: 120,
      durationSec: 120 * 60, // 2 hours
      distribution: {
        technical: 80,
        quant: 10,
        reasoning: 10,
        gk: 10,
        english: 10,
      },
    },
  };

  const questionBank = Array.isArray(window.IffcoQuestionBank) ? window.IffcoQuestionBank : [];

  // DOM Elements
  const bodyEl = document.body;
  const screens = {
    dashboard: document.getElementById("screen-dashboard"),
    systemCheck: document.getElementById("screen-system-check"),
    test: document.getElementById("screen-test"),
    results: document.getElementById("screen-results"),
  };

  // Header Elements
  const portalHeader = document.getElementById("portal-header");
  const portalBrandText = document.getElementById("portal-brand-text");
  const navLinks = document.getElementById("nav-links");
  const userProfileWidget = document.getElementById("user-profile-widget");
  const themeToggleBtn = document.getElementById("theme-toggle-btn");
  const logoutBtn = document.getElementById("logout-btn");
  const portalFooter = document.getElementById("portal-footer");

  // Dashboard Screen Buttons
  const startPracticeBtn = document.getElementById("start-practice-btn");
  const startActualBtn = document.getElementById("start-actual-btn");
  const startCbt1Btn = document.getElementById("start-cbt1-btn");

  // System Check Screen Elements
  const systemCheckVideo = document.getElementById("system-check-video");
  const systemCheckVideoPlaceholder = document.getElementById("system-check-video-placeholder");
  const cameraDeviceName = document.getElementById("camera-device-name");
  const cameraBadge = document.getElementById("camera-badge");
  const cameraStatusDesc = document.getElementById("camera-status-desc");
  const runAgainBtn = document.getElementById("run-again-btn");
  const proceedBtn = document.getElementById("proceed-btn");

  // CBT Exam Screen Elements
  const examBadge = document.getElementById("exam-badge");
  const examTitleText = document.getElementById("exam-title-text");
  const progressIndicator = document.getElementById("progress-indicator");
  const attemptedIndicator = document.getElementById("attempted-indicator");
  const timeLeftEl = document.getElementById("timeLeft");
  const questionCategory = document.getElementById("question-category");
  const flagBtn = document.getElementById("flag-btn");
  const flagBtnText = document.getElementById("flag-btn-text");
  const promptEl = document.getElementById("prompt");
  const optionsEl = document.getElementById("options");
  const prevBtn = document.getElementById("prev-btn");
  const clearBtn = document.getElementById("clear-btn");
  const nextBtn = document.getElementById("next-btn");

  // Sidebar Elements
  const proctorVideo = document.getElementById("proctor-video");
  const proctorVideoPlaceholder = document.getElementById("proctor-video-placeholder");
  const navProgressText = document.getElementById("nav-progress-text");
  const navAttemptedText = document.getElementById("nav-attempted-text");
  const navigatorGrid = document.getElementById("navigator-grid");
  const submitExamBtn = document.getElementById("submit-exam-btn");

  // Results Screen Elements
  const scoreEl = document.getElementById("score");
  const attemptedEl = document.getElementById("attempted");
  const accuracyEl = document.getElementById("accuracy");
  const avgSecFinalEl = document.getElementById("avgSecFinal");
  const breakdownEl = document.getElementById("breakdown");
  const reviewListEl = document.getElementById("review-list");
  const downloadPdfBtns = document.querySelectorAll(".download-pdf-btn");
  const restartBtn = document.getElementById("restart-btn");

  // State Variables
  let activeMode = MODES.realExam;
  let questions = [];
  let responses = []; // Array of { selectedIndex: null|number, flagged: boolean, timeMs: number }
  let currentIndex = 0;
  let startedAtMs = 0;
  let questionStartedAtMs = 0;
  let timerId = null;
  let webcamStream = null;

  // Theme Toggle Logic
  function initTheme() {
    const isDark = localStorage.getItem("theme") === "dark";
    bodyEl.classList.toggle("dark-theme", isDark);
    bodyEl.classList.toggle("light-theme", !isDark);
    updateThemeIcons(isDark);
  }

  function toggleTheme() {
    const isDark = bodyEl.classList.toggle("dark-theme");
    bodyEl.classList.toggle("light-theme", !isDark);
    localStorage.setItem("theme", isDark ? "dark" : "light");
    updateThemeIcons(isDark);
  }

  function updateThemeIcons(isDark) {
    const moonIcon = themeToggleBtn.querySelector(".moon-icon");
    const sunIcon = themeToggleBtn.querySelector(".sun-icon");
    if (isDark) {
      moonIcon.classList.add("hidden");
      sunIcon.classList.remove("hidden");
    } else {
      moonIcon.classList.remove("hidden");
      sunIcon.classList.add("hidden");
    }
  }

  themeToggleBtn.addEventListener("click", toggleTheme);

  // Screen Navigation Helpers
  function showScreen(screenId) {
    Object.keys(screens).forEach((key) => {
      if (key === screenId) {
        screens[key].classList.remove("hidden");
      } else {
        screens[key].classList.add("hidden");
      }
    });

    // Adjust Header styles based on the screen
    if (screenId === "test") {
      portalHeader.style.padding = "10px 20px";
      portalBrandText.textContent = "IFFCO CBT Portal";
      navLinks.classList.add("hidden");
      userProfileWidget.classList.add("hidden");
      logoutBtn.classList.add("hidden");
      portalFooter.classList.add("hidden");
    } else {
      portalHeader.style.padding = "14px 28px";
      portalBrandText.textContent = "Exam Portal";
      navLinks.classList.remove("hidden");
      userProfileWidget.classList.remove("hidden");
      logoutBtn.classList.remove("hidden");
      portalFooter.classList.remove("hidden");
    }
  }

  // Webcam Handling
  async function requestWebcam() {
    try {
      // Stop existing stream if any
      stopWebcam();

      cameraBadge.textContent = "CHECKING";
      cameraBadge.className = "badge badge-danger"; // red while checking
      cameraStatusDesc.textContent = "Requesting camera access...";

      webcamStream = await navigator.mediaDevices.getUserMedia({
        video: { width: 640, height: 480 },
        audio: false,
      });

      // Point system check video to stream
      systemCheckVideo.srcObject = webcamStream;
      systemCheckVideo.classList.remove("hidden");
      systemCheckVideoPlaceholder.classList.add("hidden");

      cameraBadge.textContent = "OK";
      cameraBadge.className = "badge badge-success";
      cameraStatusDesc.textContent = "Camera active & verified";

      // Get device name if available
      const videoTracks = webcamStream.getVideoTracks();
      if (videoTracks.length > 0) {
        cameraDeviceName.textContent = videoTracks[0].label || "Integrated Webcam";
      }
    } catch (err) {
      console.warn("Webcam access failed:", err);
      systemCheckVideo.classList.add("hidden");
      systemCheckVideoPlaceholder.classList.remove("hidden");
      
      const placeholderSpan = systemCheckVideoPlaceholder.querySelector("span");
      if (placeholderSpan) {
        placeholderSpan.textContent = "Camera Access Denied (Proceeding anyway)";
      }

      cameraBadge.textContent = "FAILED";
      cameraBadge.className = "badge badge-danger";
      cameraStatusDesc.textContent = "Using fallback mock avatar";
      cameraDeviceName.textContent = "No camera detected";
    }
  }

  function stopWebcam() {
    if (webcamStream) {
      webcamStream.getTracks().forEach((track) => track.stop());
      webcamStream = null;
    }
    systemCheckVideo.srcObject = null;
    proctorVideo.srcObject = null;
  }

  // Question Picker Logic
  function randInt(maxExclusive) {
    return Math.floor(Math.random() * maxExclusive);
  }

  function shuffleInPlace(arr) {
    for (let i = arr.length - 1; i > 0; i -= 1) {
      const j = randInt(i + 1);
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function pickQuestionsForMode(mode) {
    if (mode.cbt1Range) {
      const cbt1Pool = questionBank.filter((q) => q && q.tag === "cbt1");
      const [start, end] = mode.cbt1Range;
      const picked = cbt1Pool.slice(start, end);
      return { picked: [...picked], warnings: [] };
    }

    const dist = mode.distribution;
    const byTag = new Map();

    for (const q of questionBank) {
      if (!q || typeof q !== "object") continue;
      const tag = q.tag;
      if (typeof tag !== "string") continue;
      if (!byTag.has(tag)) byTag.set(tag, []);
      byTag.get(tag).push(q);
    }

    const picked = [];
    const warnings = [];

    for (const [tag, count] of Object.entries(dist)) {
      if (count <= 0) continue;
      const pool = byTag.get(tag) || [];
      if (pool.length === 0) {
        throw new Error(`No questions found for tag '${tag}' in question-bank.js`);
      }
      if (pool.length < count) {
        warnings.push(`Tag '${tag}' has only ${pool.length} questions; sampling with replacement to reach ${count}.`);
        for (let i = 0; i < count; i += 1) {
          picked.push(pool[randInt(pool.length)]);
        }
      } else {
        const poolCopy = shuffleInPlace([...pool]);
        for (let i = 0; i < count; i += 1) {
          picked.push(poolCopy[i]);
        }
      }
    }

    shuffleInPlace(picked);
    return { picked, warnings };
  }

  // Exam Navigation & Rendering
  function renderQuestion() {
    const q = questions[currentIndex];
    if (!q) return;

    questionStartedAtMs = Date.now();

    // Update Progress Indicators
    progressIndicator.textContent = `Q ${currentIndex + 1} / ${questions.length}`;
    navProgressText.textContent = `${String(currentIndex + 1).padStart(2, "0")} / ${questions.length}`;

    const attemptedCount = responses.filter((r) => r.selectedIndex !== null).length;
    attemptedIndicator.textContent = `${attemptedCount} Attempted`;
    navAttemptedText.textContent = `${attemptedCount} attempted`;

    // Update Category Pill
    questionCategory.textContent = (q.tag || "TECHNICAL").toUpperCase();

    // Update Flag Button State
    const resp = responses[currentIndex];
    if (resp.flagged) {
      flagBtn.classList.add("flagged");
      flagBtnText.textContent = "Flagged for Review";
    } else {
      flagBtn.classList.remove("flagged");
      flagBtnText.textContent = "Flag for Review";
    }

    // Render Prompt
    promptEl.textContent = `${currentIndex + 1}. ${q.prompt || ""}`;

    // Render Options
    optionsEl.innerHTML = "";
    const letters = ["A", "B", "C", "D"];
    const opts = Array.isArray(q.options) ? q.options : [];

    for (let i = 0; i < 4; i += 1) {
      const text = opts[i] ?? "";
      
      const wrapper = document.createElement("div");
      wrapper.className = "option-wrapper";

      const input = document.createElement("input");
      input.type = "radio";
      input.name = "exam-option";
      input.id = `opt-${i}`;
      input.className = "option-radio-input";
      input.value = i;
      if (resp.selectedIndex === i) {
        input.checked = true;
      }

      const label = document.createElement("label");
      label.className = "option-label";
      label.setAttribute("for", `opt-${i}`);

      const circle = document.createElement("div");
      circle.className = "option-circle";

      const textSpan = document.createElement("span");
      textSpan.className = "option-text";
      textSpan.textContent = `${letters[i]}. ${text}`;

      label.appendChild(circle);
      label.appendChild(textSpan);
      wrapper.appendChild(input);
      wrapper.appendChild(label);

      // Event listener for selection
      input.addEventListener("change", () => {
        selectOption(i);
      });

      optionsEl.appendChild(wrapper);
    }

    // Update Navigator Grid Selection
    updateNavigatorGridUI();

    // Disable/Enable Previous Button
    prevBtn.disabled = currentIndex === 0;
  }

  function updateNavigatorGridUI() {
    const circles = navigatorGrid.querySelectorAll(".circle-btn");
    circles.forEach((btn, idx) => {
      const resp = responses[idx];
      btn.className = "circle-btn"; // reset

      if (idx === currentIndex) {
        btn.classList.add("current");
      }
      if (resp.selectedIndex !== null) {
        btn.classList.add("answered");
      }
      if (resp.flagged) {
        btn.classList.add("flagged");
      }
    });
  }

  function renderNavigatorGrid() {
    navigatorGrid.innerHTML = "";
    questions.forEach((_, idx) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "circle-btn";
      btn.textContent = idx + 1;
      btn.addEventListener("click", () => {
        saveCurrentQuestionTime();
        currentIndex = idx;
        renderQuestion();
      });
      navigatorGrid.appendChild(btn);
    });
  }

  function saveCurrentQuestionTime() {
    if (questionStartedAtMs > 0) {
      const spent = Date.now() - questionStartedAtMs;
      responses[currentIndex].timeMs += spent;
      questionStartedAtMs = Date.now();
    }
  }

  function selectOption(idx) {
    responses[currentIndex].selectedIndex = idx;
    saveCurrentQuestionTime();
    updateNavigatorGridUI();

    // Update Attempted Indicators immediately
    const attemptedCount = responses.filter((r) => r.selectedIndex !== null).length;
    attemptedIndicator.textContent = `${attemptedCount} Attempted`;
    navAttemptedText.textContent = `${attemptedCount} attempted`;
  }

  function clearAnswer() {
    responses[currentIndex].selectedIndex = null;
    saveCurrentQuestionTime();
    
    // Uncheck radio buttons
    const checkedRadio = optionsEl.querySelector('input[name="exam-option"]:checked');
    if (checkedRadio) checkedRadio.checked = false;

    updateNavigatorGridUI();

    // Update Attempted Indicators immediately
    const attemptedCount = responses.filter((r) => r.selectedIndex !== null).length;
    attemptedIndicator.textContent = `${attemptedCount} Attempted`;
    navAttemptedText.textContent = `${attemptedCount} attempted`;
  }

  function toggleFlag() {
    const resp = responses[currentIndex];
    resp.flagged = !resp.flagged;
    saveCurrentQuestionTime();

    if (resp.flagged) {
      flagBtn.classList.add("flagged");
      flagBtnText.textContent = "Flagged for Review";
    } else {
      flagBtn.classList.remove("flagged");
      flagBtnText.textContent = "Flag for Review";
    }

    updateNavigatorGridUI();
  }

  function prevQuestion() {
    if (currentIndex > 0) {
      saveCurrentQuestionTime();
      currentIndex -= 1;
      renderQuestion();
    }
  }

  function nextQuestion() {
    saveCurrentQuestionTime();
    if (currentIndex < questions.length - 1) {
      currentIndex += 1;
      renderQuestion();
    } else {
      // On the last question, Next can trigger a friendly submit confirmation
      if (confirm("You are on the last question. Would you like to submit your exam?")) {
        submitExam();
      }
    }
  }

  // Timer Logic
  function formatTime(sec) {
    const s = Math.max(0, Math.floor(sec));
    const mm = String(Math.floor(s / 60)).padStart(2, "0");
    const ss = String(s % 60).padStart(2, "0");
    return `${mm}:${ss}`;
  }

  function updateTimer() {
    const elapsedMs = Date.now() - startedAtMs;
    const remainingSec = activeMode.durationSec - elapsedMs / 1000;
    timeLeftEl.textContent = formatTime(remainingSec);

    if (remainingSec <= 0) {
      alert("Time is up! Your exam will be submitted automatically.");
      submitExam({ timedOut: true });
    }
  }

  // Submit and Results
  function submitExam({ timedOut = false } = {}) {
    if (!timedOut) {
      const unattempted = responses.filter((r) => r.selectedIndex === null).length;
      let msg = "Are you sure you want to submit your exam?";
      if (unattempted > 0) {
        msg += ` You have ${unattempted} unanswered questions remaining.`;
      }
      if (!confirm(msg)) return;
    }

    saveCurrentQuestionTime();

    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }

    stopWebcam();

    // Calculate Results
    const totalQ = questions.length;
    const attempted = responses.filter((r) => r.selectedIndex !== null).length;
    const correct = responses.filter((r, idx) => r.selectedIndex !== null && r.selectedIndex === questions[idx].answerIndex).length;
    const elapsedSec = (Date.now() - startedAtMs) / 1000;
    const avgSec = attempted > 0 ? elapsedSec / attempted : 0;
    const acc = attempted > 0 ? (correct / attempted) * 100 : 0;

    scoreEl.textContent = `${correct} / ${totalQ}`;
    attemptedEl.textContent = `${attempted} / ${totalQ}`;
    accuracyEl.textContent = `${acc.toFixed(1)}%`;
    avgSecFinalEl.textContent = avgSec.toFixed(1);

    // Breakdown by Tag
    const byTag = new Map();
    responses.forEach((r, idx) => {
      const q = questions[idx];
      const tag = q.tag || "technical";
      if (!byTag.has(tag)) {
        byTag.set(tag, { total: 0, attempted: 0, correct: 0, timeMs: 0 });
      }
      const s = byTag.get(tag);
      s.total += 1;
      if (r.selectedIndex !== null) s.attempted += 1;
      if (r.selectedIndex !== null && r.selectedIndex === q.answerIndex) s.correct += 1;
      s.timeMs += r.timeMs;
    });

    breakdownEl.innerHTML = "";
    const sortedTags = Array.from(byTag.entries()).sort((a, b) => a[0].localeCompare(b[0]));
    
    sortedTags.forEach(([tag, s]) => {
      const row = document.createElement("div");
      row.className = "bdRow";

      const k = document.createElement("div");
      k.className = "bdKey";
      k.textContent = tag;

      const v1 = document.createElement("div");
      v1.className = "bdVal";
      v1.textContent = `Correct: ${s.correct}/${s.total}`;

      const v2 = document.createElement("div");
      v2.className = "bdVal";
      v2.textContent = `Attempted: ${s.attempted}/${s.total}`;

      const v3 = document.createElement("div");
      v3.className = "bdVal";
      v3.textContent = `Avg sec/Q: ${(s.total > 0 ? s.timeMs / 1000 / s.total : 0).toFixed(1)}s`;

      row.appendChild(k);
      row.appendChild(v1);
      row.appendChild(v2);
      row.appendChild(v3);
      breakdownEl.appendChild(row);
    });

    // Render Detailed Question Review List
    if (reviewListEl) {
      reviewListEl.innerHTML = "";
      const letters = ["A", "B", "C", "D"];

      questions.forEach((q, idx) => {
        const resp = responses[idx] || { selectedIndex: null };
        const selected = resp.selectedIndex;
        const correct = q.answerIndex;
        const isCorrect = selected !== null && selected === correct;
        const isAttempted = selected !== null;

        const card = document.createElement("div");
        card.className = `review-card ${isCorrect ? "card-correct" : isAttempted ? "card-incorrect" : "card-unattempted"}`;

        const header = document.createElement("div");
        header.className = "review-card-header";

        const qNum = document.createElement("span");
        qNum.className = "review-q-num";
        qNum.textContent = `Question ${idx + 1}`;

        const statusBadge = document.createElement("span");
        if (isCorrect) {
          statusBadge.className = "badge badge-success";
          statusBadge.textContent = "✓ CORRECT";
        } else if (isAttempted) {
          statusBadge.className = "badge badge-danger";
          statusBadge.textContent = "✗ INCORRECT";
        } else {
          statusBadge.className = "badge badge-warning";
          statusBadge.textContent = "⚠️ UNATTEMPTED";
        }

        header.appendChild(qNum);
        header.appendChild(statusBadge);

        const prompt = document.createElement("p");
        prompt.className = "review-q-prompt";
        prompt.textContent = q.prompt;

        const optsContainer = document.createElement("div");
        optsContainer.className = "review-options";

        (q.options || []).forEach((optText, optIdx) => {
          const optRow = document.createElement("div");
          let rowClass = "review-opt";

          const isUserChoice = selected === optIdx;
          const isRightAnswer = correct === optIdx;

          if (isRightAnswer && isUserChoice) {
            rowClass += " opt-correct-choice";
          } else if (isRightAnswer) {
            rowClass += " opt-correct";
          } else if (isUserChoice) {
            rowClass += " opt-incorrect";
          }

          optRow.className = rowClass;

          const leftBox = document.createElement("div");
          leftBox.className = "review-opt-left";

          const letterSpan = document.createElement("span");
          letterSpan.className = "review-opt-letter";
          letterSpan.textContent = `${letters[optIdx]}.`;

          const textSpan = document.createElement("span");
          textSpan.className = "review-opt-text";
          textSpan.textContent = optText;

          leftBox.appendChild(letterSpan);
          leftBox.appendChild(textSpan);

          optRow.appendChild(leftBox);

          if (isRightAnswer && isUserChoice) {
            const badgeSpan = document.createElement("span");
            badgeSpan.className = "review-opt-tag tag-success";
            badgeSpan.textContent = "✓ Your Answer (Correct)";
            optRow.appendChild(badgeSpan);
          } else if (isRightAnswer) {
            const badgeSpan = document.createElement("span");
            badgeSpan.className = "review-opt-tag tag-correct";
            badgeSpan.textContent = "✓ Correct Answer";
            optRow.appendChild(badgeSpan);
          } else if (isUserChoice) {
            const badgeSpan = document.createElement("span");
            badgeSpan.className = "review-opt-tag tag-danger";
            badgeSpan.textContent = "✗ Your Choice";
            optRow.appendChild(badgeSpan);
          }

          optsContainer.appendChild(optRow);
        });

        card.appendChild(header);
        card.appendChild(prompt);
        card.appendChild(optsContainer);
        reviewListEl.appendChild(card);
      });
    }

    showScreen("results");
  }

  // Generate and Download PDF Report Function
  function downloadPdfReport() {
    const printWindow = window.open("", "_blank");
    if (!printWindow) {
      alert("Pop-up blocked! Please allow pop-ups for localhost to download your PDF test report.");
      return;
    }

    const testTitle = activeMode ? (activeMode.label || "IFFCO GET Practice Test") : "IFFCO GET Practice Test";
    const dateStr = new Date().toLocaleString("en-IN", {
      dateStyle: "medium",
      timeStyle: "short",
    });

    const totalQ = questions.length;
    const attempted = responses.filter((r) => r.selectedIndex !== null).length;
    const correct = responses.filter((r, idx) => r.selectedIndex !== null && r.selectedIndex === questions[idx].answerIndex).length;
    const incorrect = attempted - correct;
    const unattempted = totalQ - attempted;
    const accuracy = attempted > 0 ? ((correct / attempted) * 100).toFixed(1) : "0.0";

    const letters = ["A", "B", "C", "D"];

    let qHtml = "";
    questions.forEach((q, idx) => {
      const resp = responses[idx] || { selectedIndex: null };
      const selected = resp.selectedIndex;
      const correctIdx = q.answerIndex;
      const isCorrect = selected !== null && selected === correctIdx;
      const isAttempted = selected !== null;

      let statusBadge = "";
      let borderColor = "#e5e7eb";
      let bgBadgeColor = "#f3f4f6";
      let textBadgeColor = "#374151";

      if (isCorrect) {
        statusBadge = "✓ CORRECT";
        borderColor = "#10b981";
        bgBadgeColor = "#d1fae5";
        textBadgeColor = "#065f46";
      } else if (isAttempted) {
        statusBadge = "✗ INCORRECT";
        borderColor = "#ef4444";
        bgBadgeColor = "#fee2e2";
        textBadgeColor = "#991b1b";
      } else {
        statusBadge = "⚠️ UNATTEMPTED";
        borderColor = "#f59e0b";
        bgBadgeColor = "#fef3c7";
        textBadgeColor = "#92400e";
      }

      let optionsHtml = "";
      (q.options || []).forEach((optText, optIdx) => {
        const isUserChoice = selected === optIdx;
        const isRightAnswer = correctIdx === optIdx;

        let optStyle = "padding: 8px 12px; margin-bottom: 6px; border-radius: 6px; font-size: 13px; display: flex; align-items: center; justify-content: space-between;";
        let tagHtml = "";

        if (isRightAnswer && isUserChoice) {
          optStyle += " background-color: #d1fae5; border: 1.5px solid #10b981; font-weight: 600; color: #065f46;";
          tagHtml = '<span style="font-size: 11px; font-weight: 700; color: #065f46;">✓ Your Answer (Correct)</span>';
        } else if (isRightAnswer) {
          optStyle += " background-color: #ecfdf5; border: 1.5px solid #a7f3d0; font-weight: 600; color: #047857;";
          tagHtml = '<span style="font-size: 11px; font-weight: 700; color: #047857;">✓ Correct Answer</span>';
        } else if (isUserChoice) {
          optStyle += " background-color: #fee2e2; border: 1.5px solid #fca5a5; color: #991b1b;";
          tagHtml = '<span style="font-size: 11px; font-weight: 700; color: #991b1b;">✗ Your Choice</span>';
        } else {
          optStyle += " background-color: #f9fafb; border: 1px solid #f3f4f6; color: #4b5563;";
        }

        optionsHtml += `
          <div style="${optStyle}">
            <span><strong>${letters[optIdx]}.</strong> ${optText}</span>
            ${tagHtml}
          </div>
        `;
      });

      qHtml += `
        <div style="border: 1px solid ${borderColor}; border-left: 5px solid ${borderColor}; border-radius: 8px; padding: 14px; margin-bottom: 14px; page-break-inside: avoid; background-color: #ffffff;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 700; font-size: 14px; color: #111827;">Q${idx + 1}. ${q.prompt}</span>
            <span style="font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; background-color: ${bgBadgeColor}; color: ${textBadgeColor}; text-transform: uppercase;">${statusBadge}</span>
          </div>
          <div style="margin-top: 8px;">
            ${optionsHtml}
          </div>
        </div>
      `;
    });

    const docHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="utf-8">
        <title>IFFCO_CBT_Report_${testTitle.replace(/[^a-zA-Z0-9]/g, "_")}</title>
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #111827; margin: 0; padding: 24px; background-color: #ffffff; }
          .header { border-bottom: 2px solid #10b981; padding-bottom: 12px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: flex-end; }
          .title { font-size: 20px; font-weight: 800; color: #115e59; margin: 0; }
          .subtitle { font-size: 13px; color: #4b5563; margin-top: 4px; }
          .candidate-info { text-align: right; font-size: 12px; color: #4b5563; }
          .candidate-name { font-weight: 700; font-size: 14px; color: #111827; }
          .summary-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 24px; background: #f3f4f6; padding: 14px; border-radius: 8px; }
          .stat-box { text-align: center; }
          .stat-label { font-size: 11px; text-transform: uppercase; color: #6b7280; font-weight: 600; display: block; }
          .stat-val { font-size: 18px; font-weight: 800; color: #111827; margin-top: 2px; }
          .stat-val.green { color: #059669; }
          .stat-val.red { color: #dc2626; }
          .stat-val.yellow { color: #d97706; }
          @media print {
            body { padding: 0; background-color: #ffffff; }
            .no-print { display: none !important; }
          }
        </style>
      </head>
      <body>
        <div class="no-print" style="margin-bottom: 20px; text-align: right;">
          <button onclick="window.print()" style="background-color: #10b981; color: white; border: none; padding: 10px 22px; font-weight: 700; border-radius: 6px; cursor: pointer; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            🖨️ Save as PDF / Print
          </button>
        </div>

        <div class="header">
          <div>
            <h1 class="title">IFFCO GET CBT Practice Test Report</h1>
            <div class="subtitle"><strong>Exam Mode:</strong> ${testTitle}</div>
          </div>
          <div class="candidate-info">
            <div class="candidate-name">AVANISH KUMAR GUPTA</div>
            <div>Date: ${dateStr}</div>
          </div>
        </div>

        <div class="summary-grid">
          <div class="stat-box">
            <span class="stat-label">Score</span>
            <span class="stat-val green">${correct} / ${totalQ}</span>
          </div>
          <div class="stat-box">
            <span class="stat-label">Accuracy</span>
            <span class="stat-val green">${accuracy}%</span>
          </div>
          <div class="stat-box">
            <span class="stat-label">Attempted</span>
            <span class="stat-val">${attempted} / ${totalQ}</span>
          </div>
          <div class="stat-box">
            <span class="stat-label">Incorrect</span>
            <span class="stat-val red">${incorrect}</span>
          </div>
          <div class="stat-box">
            <span class="stat-label">Unattempted</span>
            <span class="stat-val yellow">${unattempted}</span>
          </div>
        </div>

        <h3 style="font-size: 16px; margin-bottom: 14px; border-bottom: 1px solid #e5e7eb; padding-bottom: 6px; color: #111827;">Detailed Question Analysis & Answers</h3>

        ${qHtml}

        <script>
          window.onload = function() {
            setTimeout(function() {
              window.print();
            }, 300);
          };
        </script>
      </body>
      </html>
    `;

    printWindow.document.open();
    printWindow.document.write(docHtml);
    printWindow.document.close();
  }

  // Reset and Boot
  function reset() {
    stopWebcam();
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }
    questions = [];
    responses = [];
    currentIndex = 0;
    startedAtMs = 0;
    questionStartedAtMs = 0;

    timeLeftEl.textContent = "--:--";
    progressIndicator.textContent = "Q -- / --";
    attemptedIndicator.textContent = "-- Attempted";
    promptEl.textContent = "";
    optionsEl.innerHTML = "";
    navigatorGrid.innerHTML = "";
    breakdownEl.innerHTML = "";

    showScreen("dashboard");
  }

  // Event Listeners for Dashboard
  document.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-mode]");
    if (btn) {
      const modeKey = btn.getAttribute("data-mode");
      if (MODES[modeKey]) {
        activeMode = MODES[modeKey];
        showScreen("systemCheck");
        requestWebcam();
      }
    }
  });

  if (startCbt1Btn) {
    startCbt1Btn.addEventListener("click", () => {
      activeMode = MODES.cbt1Exam;
      showScreen("systemCheck");
      requestWebcam();
    });
  }

  startPracticeBtn.addEventListener("click", () => {
    activeMode = MODES.practiceExam;
    showScreen("systemCheck");
    requestWebcam();
  });

  startActualBtn.addEventListener("click", () => {
    activeMode = MODES.realExam;
    showScreen("systemCheck");
    requestWebcam();
  });

  runAgainBtn.addEventListener("click", () => {
    requestWebcam();
  });

  proceedBtn.addEventListener("click", () => {
    // Pick questions and prepare responses
    try {
      const { picked, warnings } = pickQuestionsForMode(activeMode);
      if (warnings.length > 0) {
        warnings.forEach((w) => console.warn(w));
      }

      questions = picked;
      responses = questions.map(() => ({
        selectedIndex: null,
        flagged: false,
        timeMs: 0,
      }));

      currentIndex = 0;
      startedAtMs = Date.now();
      questionStartedAtMs = startedAtMs;

      // Setup proctor video if webcam is active
      if (webcamStream) {
        proctorVideo.srcObject = webcamStream;
        proctorVideo.classList.remove("hidden");
        proctorVideoPlaceholder.classList.add("hidden");
      } else {
        proctorVideo.classList.add("hidden");
        proctorVideoPlaceholder.classList.remove("hidden");
      }

      // Render Exam UI
      examBadge.textContent = activeMode.badge;
      examTitleText.textContent = activeMode.label;
      renderNavigatorGrid();
      renderQuestion();

      showScreen("test");

      // Start Countdown Timer
      if (timerId) clearInterval(timerId);
      timerId = setInterval(updateTimer, 200);
      updateTimer();

    } catch (e) {
      console.error(e);
      alert(e instanceof Error ? e.message : String(e));
    }
  });

  // Event Listeners for Exam Controls
  downloadPdfBtns.forEach((btn) => {
    btn.addEventListener("click", downloadPdfReport);
  });
  prevBtn.addEventListener("click", prevQuestion);
  nextBtn.addEventListener("click", nextQuestion);
  clearBtn.addEventListener("click", clearAnswer);
  flagBtn.addEventListener("click", toggleFlag);
  submitExamBtn.addEventListener("click", () => submitExam());
  restartBtn.addEventListener("click", reset);
  logoutBtn.addEventListener("click", reset);

  // Keyboard Shortcuts
  window.addEventListener("keydown", (ev) => {
    // Only capture shortcuts when test screen is visible
    if (screens.test.classList.contains("hidden")) return;

    const key = ev.key;
    
    // Options 1-4 selection
    if (key === "1" || key === "2" || key === "3" || key === "4") {
      ev.preventDefault();
      const optIdx = Number(key) - 1;
      
      // Select the radio button in UI
      const radio = document.getElementById(`opt-${optIdx}`);
      if (radio) {
        radio.checked = true;
        selectOption(optIdx);
      }
      return;
    }

    // Flag for Review (Space or F)
    if (key === " " || key.toLowerCase() === "f") {
      ev.preventDefault();
      toggleFlag();
      return;
    }

    // Clear Answer (C)
    if (key.toLowerCase() === "c") {
      ev.preventDefault();
      clearAnswer();
      return;
    }

    // Previous Question (ArrowLeft or P)
    if (key === "ArrowLeft" || key.toLowerCase() === "p") {
      ev.preventDefault();
      prevQuestion();
      return;
    }

    // Next Question (ArrowRight, N, or Enter)
    if (key === "ArrowRight" || key.toLowerCase() === "n" || key === "Enter") {
      ev.preventDefault();
      nextQuestion();
    }
  });

  // Initialize
  initTheme();
  showScreen("dashboard");
})();
