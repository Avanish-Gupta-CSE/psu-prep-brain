import fs from "node:fs";

const DEFAULT_PDF_PATH =
  "C:\\Users\\agupt1\\Downloads\\cdn.digialm.com__per_g01_pub_1258_touchstone_AssessmentQPHTMLMode1__1258O26309_1258O26309S2D3367_17878273890053807_1832901400109_1258O26309S2D3367E1.html.pdf";

const CORRECT_OPTION_COLOR = "#40c64b";

function normalizeColor(color) {
  if (!color) return null;
  if (Array.isArray(color)) return normalizeColor(color[0]);
  if (typeof color === "string") return color.trim().toLowerCase();
  return String(color).trim().toLowerCase();
}

function isTruthyString(s) {
  return typeof s === "string" && s.trim().length > 0;
}

function extractUnicode(value) {
  if (!value) return "";
  if (typeof value === "string") return value;
  if (Array.isArray(value)) return value.map(extractUnicode).join("");
  if (typeof value === "object") {
    if (typeof value.unicode === "string") return value.unicode;
  }
  return "";
}

function extractShowTextString(args) {
  // pdf.js operator args for showText/showSpacedText contain glyph objects with `unicode`.
  // Some PDFs encode spaces as \u0003 (ETX) in glyph.unicode.
  const raw = extractUnicode(args);
  return raw.replace(/\u0003/g, " ");
}

function parseSectionLine(text) {
  const m = text.match(/^Section\s*:\s*(.+)$/i);
  return m ? m[1].trim() : null;
}

function parseKeyValueLine(text, key) {
  // Example: "Chosen Option : B" or "Status : Answered"
  const re = new RegExp(`^${key}\\s*:\\s*(.+)$`, "i");
  const m = text.match(re);
  return m ? m[1].trim() : null;
}

function parseQNumber(text) {
  const m = text.match(/^Q\.(\d+)$/i);
  return m ? Number(m[1]) : null;
}

function parseOptionLetter(text) {
  const m = text.match(/^\s*([A-D])\.\s*/i);
  return m ? m[1].toUpperCase() : null;
}

function isSectionCaptureTerminator(text) {
  // Stop capturing section name when we hit page marker or a question marker.
  if (/^Q\.\d+$/i.test(text)) return true;
  if (/^--\s*\d+\s*of\s*\d+\s*--$/i.test(text)) return true;
  return false;
}

function joinSectionTokens(tokens) {
  let out = "";
  for (let i = 0; i < tokens.length; i += 1) {
    const t = String(tokens[i] ?? "").trim();
    if (!t) continue;

    const next = i + 1 < tokens.length ? String(tokens[i + 1] ?? "").trim() : "";

    if (!out) {
      out = t;
      continue;
    }

    // Handle split words like "A" + "wareness" => "Awareness"
    if (t.length === 1 && /^[A-Z]$/.test(t) && next && /^[a-z]/.test(next)) {
      out += ` ${t}${next}`;
      i += 1;
      continue;
    }

    // Handle continuation like "wareness" after "A" (if it slipped through)
    if (/^[a-z]/.test(t) && /[A-Za-z]$/.test(out)) {
      out += t;
      continue;
    }

    out += ` ${t}`;
  }
  return out.trim();
}

function asAttemptedChoice(chosen) {
  if (!isTruthyString(chosen)) return null;
  const v = chosen.trim().toUpperCase();
  if (v === "--" || v === "-" || v === "NA" || v === "N/A") return null;
  if (/^[A-D]$/.test(v)) return v;
  if (/^[1-4]$/.test(v)) return v;
  return null;
}

function computeSectionAggregates(questions, { negativePerWrong }) {
  const perSection = new Map();

  function ensure(sec) {
    if (!perSection.has(sec)) {
      perSection.set(sec, {
        section: sec,
        total: 0,
        attempted: 0,
        correct: 0,
        wrong: 0,
        unattempted: 0,
        rawMarks: 0,
      });
    }
    return perSection.get(sec);
  }

  for (const q of questions) {
    const sec = q.section ?? "Unknown";
    const agg = ensure(sec);
    agg.total += 1;

    const attempted = q.attemptedChoice !== null;
    const correct = attempted && q.correctChoice && q.attemptedChoice === q.correctChoice;
    const wrong = attempted && q.correctChoice && q.attemptedChoice !== q.correctChoice;

    if (attempted) agg.attempted += 1;
    else agg.unattempted += 1;

    if (correct) agg.correct += 1;
    else if (wrong) agg.wrong += 1;

    // Assumption: +1 for correct, 0 for unattempted; optional negative marking for wrong.
    let marks = 0;
    if (correct) marks += 1;
    if (wrong) marks -= negativePerWrong;
    agg.rawMarks += marks;
  }

  const rows = [...perSection.values()].sort((a, b) => a.section.localeCompare(b.section));
  const total = rows.reduce(
    (acc, r) => {
      acc.total += r.total;
      acc.attempted += r.attempted;
      acc.correct += r.correct;
      acc.wrong += r.wrong;
      acc.unattempted += r.unattempted;
      acc.rawMarks += r.rawMarks;
      return acc;
    },
    { section: "TOTAL", total: 0, attempted: 0, correct: 0, wrong: 0, unattempted: 0, rawMarks: 0 },
  );

  return { rows, total };
}

function padRight(s, n) {
  const str = String(s);
  return str.length >= n ? str : str + " ".repeat(n - str.length);
}

function fmtMarks(x) {
  // Keep .25 style if negative marking applies
  if (Number.isInteger(x)) return String(x);
  return x.toFixed(2).replace(/0+$/, "").replace(/\.$/, "");
}

function printTable(rows, totalRow) {
  const secWidth = Math.max(18, ...rows.map((r) => r.section.length), totalRow.section.length) + 2;
  const header =
    padRight("SECTION", secWidth) +
    padRight("TOT", 6) +
    padRight("ATT", 6) +
    padRight("COR", 6) +
    padRight("WRONG", 8) +
    padRight("UNATT", 8) +
    "MARKS";

  console.log(header);
  console.log("-".repeat(header.length));
  for (const r of rows) {
    console.log(
      padRight(r.section, secWidth) +
        padRight(r.total, 6) +
        padRight(r.attempted, 6) +
        padRight(r.correct, 6) +
        padRight(r.wrong, 8) +
        padRight(r.unattempted, 8) +
        fmtMarks(r.rawMarks),
    );
  }
  console.log("-".repeat(header.length));
  console.log(
    padRight(totalRow.section, secWidth) +
      padRight(totalRow.total, 6) +
      padRight(totalRow.attempted, 6) +
      padRight(totalRow.correct, 6) +
      padRight(totalRow.wrong, 8) +
      padRight(totalRow.unattempted, 8) +
      fmtMarks(totalRow.rawMarks),
  );
}

async function main() {
  const pdfPath = process.argv[2] ?? DEFAULT_PDF_PATH;
  const negativePerWrong = Number.isFinite(Number(process.argv[3])) ? Number(process.argv[3]) : 0;

  const pdfjs = await import("pdfjs-dist/legacy/build/pdf.mjs");
  const { OPS } = pdfjs;

  const data = new Uint8Array(fs.readFileSync(pdfPath));
  const doc = await pdfjs.getDocument({ data }).promise;

  let currentSection = "Unknown";
  let hasSeenAnySection = false;
  /** @type {string[] | null} */
  let sectionTokens = null;
  let pendingChosen = false;
  let pendingStatus = false;

  /** @type {null | { qNum: number, section: string, chosenRaw: string | null, attemptedChoice: string | null, correctChoice: string | null, status: string | null }} */
  let currentQ = null;
  /** @type {Array<ReturnType<typeof structuredClone>>} */
  const questions = [];

  function finalizeCurrentQuestion() {
    if (!currentQ) return;
    questions.push({ ...currentQ });
    currentQ = null;
  }

  function finalizeSectionCaptureIfAny() {
    if (!sectionTokens) return;
    const sec = joinSectionTokens(sectionTokens);
    if (sec) {
      currentSection = sec;
      if (!hasSeenAnySection) {
        hasSeenAnySection = true;
        if (currentQ && (currentQ.section ?? "Unknown") === "Unknown") {
          currentQ.section = currentSection;
        }
      }
    }
    sectionTokens = null;
  }

  function onTextToken(textRaw, fillColorRaw) {
    const text = String(textRaw ?? "").replace(/\s+/g, " ").trim();
    if (!text) return;

    const fillColor = normalizeColor(fillColorRaw);

    // Section capture (may be split across multiple tokens)
    if (sectionTokens) {
      if (isSectionCaptureTerminator(text)) {
        finalizeSectionCaptureIfAny();
        // fall through and process this token normally
      } else {
        sectionTokens.push(text);
        return;
      }
    }

    const sectionInline = parseSectionLine(text);
    if (sectionInline !== null) {
      sectionTokens = [sectionInline];
      return;
    }
    if (/^Section\s*:$/i.test(text) || /^Section$/i.test(text) || /^Section\s*:?$/i.test(text)) {
      sectionTokens = [];
      return;
    }

    // Question start
    const qNum = parseQNumber(text);
    if (qNum !== null) {
      finalizeCurrentQuestion();
      currentQ = {
        qNum,
        section: currentSection,
        chosenRaw: null,
        attemptedChoice: null,
        correctChoice: null,
        status: null,
      };
      pendingChosen = false;
      pendingStatus = false;
      return;
    }

    if (!currentQ) {
      return;
    }

    // Status
    const statusInline = parseKeyValueLine(text, "Status");
    if (statusInline) {
      currentQ.status = statusInline;
      pendingStatus = false;
    } else if (/^Status\s*:?$/i.test(text)) {
      pendingStatus = true;
    } else if (pendingStatus) {
      currentQ.status = text;
      pendingStatus = false;
    }

    // Chosen option
    const chosenInline = parseKeyValueLine(text, "Chosen Option");
    if (chosenInline) {
      currentQ.chosenRaw = chosenInline;
      currentQ.attemptedChoice = asAttemptedChoice(chosenInline);
      pendingChosen = false;
    } else if (/^Chosen Option\s*:?$/i.test(text) || /^Chosen Option$/i.test(text)) {
      pendingChosen = true;
    } else if (pendingChosen) {
      currentQ.chosenRaw = text;
      currentQ.attemptedChoice = asAttemptedChoice(text);
      pendingChosen = false;
    }

    // Correct option (green option letter)
    const optLetter = parseOptionLetter(text);
    if (optLetter && fillColor === CORRECT_OPTION_COLOR) {
      currentQ.correctChoice = optLetter;
    }
  }

  for (let pageNum = 1; pageNum <= doc.numPages; pageNum += 1) {
    const page = await doc.getPage(pageNum);
    const op = await page.getOperatorList();

    let fillColor = null;

    for (let i = 0; i < op.fnArray.length; i += 1) {
      const fn = op.fnArray[i];
      const args = op.argsArray[i];

      if (fn === OPS.setFillRGBColor || fn === OPS.setFillGray || fn === OPS.setFillCMYKColor) {
        fillColor = args?.[0] ?? null;
        continue;
      }

      if (fn === OPS.showText || fn === OPS.showSpacedText) {
        const tokenText = extractShowTextString(args);
        onTextToken(tokenText, fillColor);
      }
    }
  }

  // If the document ended while still capturing a section name, finalize it.
  finalizeSectionCaptureIfAny();

  finalizeCurrentQuestion();

  // Filter out malformed entries (just in case)
  const usable = questions.filter((q) => Number.isFinite(q.qNum));

  // Print a summary
  console.log(`PDF: ${pdfPath}`);
  console.log(`Pages: ${doc.numPages}`);
  console.log(`Questions parsed: ${usable.length}`);
  console.log(`Correct-option color: ${CORRECT_OPTION_COLOR}`);
  console.log(`Negative marking per wrong: ${negativePerWrong}`);
  const unknownSectionQs = usable.filter((q) => (q.section ?? "Unknown") === "Unknown");
  if (unknownSectionQs.length > 0) {
    console.log(
      `Unknown section questions: ${unknownSectionQs
        .slice(0, 25)
        .map((q) => `Q.${q.qNum}`)
        .join(", ")}${unknownSectionQs.length > 25 ? ", ..." : ""}`,
    );
  }
  console.log("");

  const { rows, total } = computeSectionAggregates(usable, { negativePerWrong });
  printTable(rows, total);

  // Diagnostics: missing correct choice or chosen option
  const missingCorrect = usable.filter((q) => !q.correctChoice);
  const missingChosen = usable.filter((q) => q.chosenRaw === null);

  console.log("");
  console.log(`Diagnostics: missing correctChoice = ${missingCorrect.length}, missing chosenRaw = ${missingChosen.length}`);
  if (missingCorrect.length > 0) {
    console.log(
      "First few missing correctChoice: " +
        missingCorrect
          .slice(0, 10)
          .map((q) => `Q.${q.qNum}(${q.section})`)
          .join(", "),
    );
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

