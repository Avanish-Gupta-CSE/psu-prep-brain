#!/usr/bin/env python3
"""
Convert Azure Document Intelligence OCR output (raw.txt) into a structured
Markdown file (revision-ebook-glm.md) for the PSU prep brain repo.

Source format: JSON with ocr_result.content (line-by-line with <<P#-L#>> markers)
              plus ocr_result.raw_result with paragraphs, tables, sections, etc.
"""

import json
import re
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "raw.txt")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "revision-ebook-glm.md")

# Chapter definitions based on the INDEX page of the book
CHAPTERS = [
    (1, "Computer Organization and Architecture", 3, 10),
    (2, "Data Structures & Algorithm", 11, 27),
    (3, "Discrete Mathematics", 28, 35),
    (4, "Digital Logic", 36, 49),
    (5, "Database Management System", 50, 65),
    (6, "Theory of Computation", 66, 78),
    (7, "Compiler Design", 79, 85),
    (8, "Operating Systems", 86, 103),
    (9, "Computer Networks", 104, 119),
    (10, "Programming in C & C++", 120, 141),
    (11, "Web Technology", 142, 156),
    (12, "Software Engineering", 157, 180),
    (13, "Cloud Computing", 181, 192),
]

# Normalized chapter match strings for fuzzy matching
CHAPTER_PATTERNS = [
    (1, "computer organization and architecture"),
    (2, "data structure"),
    (3, "discrete mathematics"),
    (4, "digital logic"),
    (5, "database management"),
    (6, "theory of computation"),
    (7, "compiler design"),
    (8, "operating system"),
    (9, "computer network"),
    (10, "programming in c"),
    (11, "web technology"),
    (12, "software engineering"),
    (13, "cloud computing"),
]


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_chapter_for_page(page_num):
    for num, title, start, end in CHAPTERS:
        if start <= page_num <= end:
            return (num, title)
    return None


def is_chapter_title(content):
    """Check if content matches a chapter title. Returns (num, title) or None."""
    c = content.lower().strip()
    # Remove leading number prefix like "01.", "02.", etc.
    c_clean = re.sub(r'^\d+\.\s*', '', c).strip()
    for num, pattern in CHAPTER_PATTERNS:
        if pattern in c_clean or c_clean in pattern:
            return (num, CHAPTERS[num-1][1])
    return None


def format_table(table):
    """Convert an Azure DI table to Markdown."""
    rows = table.get("cells", [])
    if not rows:
        return ""
    
    row_count = table.get("rowCount", 0)
    col_count = table.get("columnCount", 0)
    
    grid = [["" for _ in range(col_count)] for _ in range(row_count)]
    for cell in rows:
        r = cell.get("rowIndex", 0)
        c = cell.get("columnIndex", 0)
        content = cell.get("content", "").strip().replace("\n", " ")
        if r < row_count and c < col_count:
            grid[r][c] = content
    
    lines = []
    for i, row in enumerate(grid):
        line = "| " + " | ".join(cell if cell else " " for cell in row) + " |"
        lines.append(line)
        if i == 0:
            sep = "| " + " | ".join("---" for _ in row) + " |"
            lines.append(sep)
    
    return "\n".join(lines)


def escape_md(text):
    """Escape markdown special chars in regular text (but preserve intentional formatting)."""
    # Don't escape # inside code-like patterns (e.g., #include)
    # Only escape # at start of lines that aren't intended as headings
    return text


def convert():
    data = load_data(INPUT_FILE)
    ocr = data.get("ocr_result", {})
    rr = ocr.get("raw_result", {})
    paragraphs = rr.get("paragraphs", [])
    tables = rr.get("tables", [])

    # Build table offset ranges to skip paragraphs that are inside tables
    table_offsets = set()
    for t in tables:
        for span in t.get("spans", []):
            offset = span.get("offset", 0)
            length = span.get("length", 0)
            for o in range(offset, offset + length):
                table_offsets.add(o)

    # Build a set of paragraph content offsets that fall inside tables
    table_para_indices = set()
    for i, p in enumerate(paragraphs):
        for span in p.get("spans", []):
            offset = span.get("offset", 0)
            length = span.get("length", 0)
            # Check if any part of this paragraph overlaps with a table
            for o in range(offset, offset + length):
                if o in table_offsets:
                    table_para_indices.add(i)
                    break

    # Also identify paragraph offsets for inline table insertion
    # Map: offset -> (table_index, table_object)
    table_start_offsets = {}
    for idx, t in enumerate(tables):
        spans = t.get("spans", [])
        if spans:
            first_offset = spans[0].get("offset", 0)
            table_start_offsets[first_offset] = (idx, t)

    current_chapter_num = 0
    output = []

    # ── Title Page ──
    output.append("# Computer Science & Engineering / Information Technology")
    output.append("")
    output.append("## CAPSULE — Quick Revision")
    output.append("")
    output.append("> Key Notes, Terms, Definitions and Formulae")
    output.append("")
    output.append("**Useful for:** UGC-NET/JRF, GATE, IES, PSU, UPPSC AE, Polytechnic Lecturer, "
                   "LT Grade, NIELIT, ISRO, UPPCL AE, UPRVUNL AE, UJVNL AE, KVS, NVS PGT, DSSSB, "
                   "PTCUL, ASSAM PSC, APPSC, BPSC, CGPSC, Gujarat SC, HPPSC, UPSC, MPPSC, Rajasthan "
                   "Basic Computer Teacher, J&KPSC, Kerala PSC, Karnataka PSC, KPCL AE, ISRO "
                   "Scientist/Engineer, OPSC, RPSC, TNPSC, Punjab PSC, Maharashtra PSC, BHEL ET, "
                   "TANGEDCO AE, Telangana PSC, JUVNL AEE, CIL MT, RRB SSC, SJVNL ET, TSGENCO AE, "
                   "VIZAG STEEL MT, Tamil Nadu TRB Polytechnic Lecturer")
    output.append("")
    output.append("---")
    output.append("")

    # ── Table of Contents ──
    output.append("## 📖 Table of Contents")
    output.append("")
    for num, title, start, end in CHAPTERS:
        output.append(f"{num}. **{title}** (pp. {start}–{end})")
    output.append("")
    output.append("---")
    output.append("")

    # ── Process Paragraphs ──
    i = 0
    last_table_inserted = -1
    while i < len(paragraphs):
        p = paragraphs[i]
        role = p.get("role")
        content = p.get("content", "").strip()
        br = p.get("boundingRegions", [])
        page = br[0].get("pageNumber", 0) if br else 0

        # Skip front matter (pages 1-2: title + index)
        if page <= 2:
            i += 1
            continue

        # Skip page numbers, footers, and YCT watermarks
        if role in ("pageNumber", "pageFooter"):
            i += 1
            continue
        if content == "YCT":
            i += 1
            continue

        # Skip paragraphs that are inside tables (we handle tables separately)
        if i in table_para_indices:
            i += 1
            continue

        # ── Chapter titles (role=title) ──
        if role == "title":
            # Handle split chapter titles like "08." + "OPERATING SYSTEM"
            combined = content
            if i + 1 < len(paragraphs) and paragraphs[i+1].get("role") == "title":
                next_content = paragraphs[i+1].get("content", "").strip()
                combined = f"{content} {next_content}".strip()
            
            match = is_chapter_title(combined)
            if not match:
                # Also try just the content itself
                match = is_chapter_title(content)
            
            if match:
                ch_num, ch_title = match
                current_chapter_num = ch_num
                output.append("")
                output.append(f"# {ch_num:02d}. {ch_title}")
                output.append("")
                # If we combined two paragraphs, skip the next one
                if combined != content:
                    i += 2
                else:
                    i += 1
            else:
                # Sub-title within a chapter
                heading_text = content.rstrip("-").rstrip()
                if heading_text:
                    output.append("")
                    output.append(f"### {heading_text}")
                    output.append("")
                i += 1
            continue

        # ── Section headings ──
        if role == "sectionHeading":
            heading_text = content.rstrip("-").rstrip()
            if heading_text:
                output.append("")
                output.append(f"#### {heading_text}")
                output.append("")
            i += 1
            continue

        # ── Page headers ──
        if role == "pageHeader":
            # Only include meaningful headers
            if content and not content.isdigit() and content != "YCT" and len(content) > 3:
                output.append(f"##### {content}")
                output.append("")
            i += 1
            continue

        # ── Regular content ──
        if content:
            # Skip standalone small numbers (page numbers)
            if content.isdigit() and len(content) <= 3:
                i += 1
                continue

            # Escape accidental markdown headings from code (#include, etc.)
            if content.startswith("#") and not content.startswith("# "):
                # This is likely code (#include, etc.) — wrap in backticks
                output.append(f"`{content}`")
                output.append("")
                i += 1
                continue

            # Format bullet points
            if content.startswith("·") or content.startswith("•"):
                content = "- " + content[1:].strip()
            elif content.startswith(".") and len(content) > 1 and content[1] == " ":
                content = "- " + content[2:].strip()

            output.append(content)
            output.append("")

        i += 1

    # ── Tables Section ──
    output.append("")
    output.append("---")
    output.append("")
    output.append("# 📊 Tables Reference")
    output.append("")

    for idx, table in enumerate(tables):
        # Skip the index table (first table)
        if idx == 0:
            continue

        md_table = format_table(table)
        if md_table:
            br = table.get("boundingRegions", [])
            page = br[0].get("pageNumber", 0) if br else 0
            if page <= 2:
                continue

            chapter_info = get_chapter_for_page(page)
            chapter_label = f"Ch {chapter_info[0]}: {chapter_info[1]}" if chapter_info else f"Page {page}"

            cells = table.get("cells", [])
            header_cells = [c for c in cells if c.get("kind") == "columnHeader"]
            if header_cells:
                titles = [c.get("content", "").strip()
                          for c in sorted(header_cells, key=lambda c: (c.get("rowIndex", 0), c.get("columnIndex", 0)))]
                title = " / ".join(t for t in titles if t)
            else:
                # Try first row as header
                first_row_cells = [c for c in cells if c.get("rowIndex") == 0]
                if first_row_cells:
                    titles = [c.get("content", "").strip()
                              for c in sorted(first_row_cells, key=lambda c: c.get("columnIndex", 0))]
                    title = " / ".join(t for t in titles if t)
                else:
                    title = f"Table {idx}"

            output.append(f"### {title}")
            output.append(f"*{chapter_label}*")
            output.append("")
            output.append(md_table)
            output.append("")

    # Write output
    final_text = "\n".join(output)
    # Clean up excess blank lines (max 2 consecutive)
    final_text = re.sub(r'\n{4,}', '\n\n\n', final_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_text)

    print(f"Written {len(final_text)} chars to {OUTPUT_FILE}")
    print(f"Total paragraphs processed: {len(paragraphs)}")
    print(f"Total tables: {len(tables)}")


if __name__ == "__main__":
    convert()