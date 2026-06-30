/* global window, alert, confirm */

(() => {
  // Exam Modes Configuration
  const MODES = {
    realExam: {
      key: "realExam",
      label: "GET Computer Science Exam",
      badge: "GET EXAM",
      totalQuestions: 100,
      durationSec: 60 * 60, // 1 hour
      distribution: {
        technical: 80,
        quant: 5,
        reasoning: 5,
        gk: 5,
        english: 5,
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
      }
      for (let i = 0; i < count; i += 1) {
        picked.push(pool[randInt(pool.length)]);
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

    showScreen("results");
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
