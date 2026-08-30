import os
import sys
import socket
import webbrowser
from pathlib import Path

# Fix Windows console encoding if needed
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="PSU Markdown Print Studio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WORKSPACE_ROOT = Path(__file__).resolve().parent

def get_installed_printers():
    printers_list = []
    default_printer = "Default System Printer"
    try:
        import win32print
        raw_printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        printers_list = [p[2] for p in raw_printers]
        try:
            default_printer = win32print.GetDefaultPrinter()
        except Exception:
            pass
    except Exception:
        printers_list = ["Default Printer (Windows Generic)"]
    return {
        "printers": printers_list,
        "default_printer": default_printer
    }

@app.get("/api/system-info")
async def system_info():
    printer_data = get_installed_printers()
    return {
        "status": "online",
        "app": "PSU Markdown Print Studio",
        "workspace": str(WORKSPACE_ROOT),
        **printer_data
    }

@app.get("/api/workspace-files")
async def list_workspace_md_files():
    """List markdown files inside the workspace for quick 1-click loading."""
    md_files = []
    ignore_dirs = {'.git', 'node_modules', '.cursor', 'terminals', '__pycache__', '.pytest_cache'}
    
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('.')]
        for f in files:
            if f.endswith('.md') or f.endswith('.markdown'):
                full_path = Path(root) / f
                rel_path = full_path.relative_to(WORKSPACE_ROOT)
                size_kb = full_path.stat().st_size / 1024
                md_files.append({
                    "name": f,
                    "rel_path": str(rel_path).replace("\\", "/"),
                    "size_kb": round(size_kb, 1),
                    "dir": str(rel_path.parent).replace("\\", "/") if str(rel_path.parent) != "." else "Root"
                })
    
    md_files.sort(key=lambda x: (x["dir"], x["name"]))
    return {"files": md_files}

@app.get("/api/read-file")
async def read_workspace_file(path: str):
    """Read a specific markdown file from the workspace."""
    target_path = (WORKSPACE_ROOT / path).resolve()
    if not str(target_path).startswith(str(WORKSPACE_ROOT)):
        raise HTTPException(status_code=403, detail="Access denied")
    if not target_path.exists() or not target_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        content = target_path.read_text(encoding='utf-8')
        return {
            "name": target_path.name,
            "path": path,
            "content": content,
            "size_kb": round(target_path.stat().st_size / 1024, 1)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload-md")
async def upload_markdown(file: UploadFile = File(...)):
    """Accept drag-and-dropped markdown file."""
    try:
        content_bytes = await file.read()
        try:
            content = content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            content = content_bytes.decode("latin-1")
        
        return {
            "name": file.filename,
            "size_kb": round(len(content_bytes) / 1024, 1),
            "content": content
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read file: {str(e)}")

# Frontend HTML
INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PSU Markdown Print Studio (Brother Printer Ready)</title>
  
  <!-- Modern Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap" rel="stylesheet">
  
  <!-- Highlight.js for Syntax Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  
  <!-- Marked.js for GFM Markdown Rendering -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    :root {
      --bg-color: #0f172a;
      --card-bg: #1e293b;
      --border-color: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --accent: #10b981;
      --paper-width: 210mm;
      --paper-min-height: 297mm;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-color);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Screen UI Header */
    .app-header {
      background-color: var(--card-bg);
      border-bottom: 1px solid var(--border-color);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      background: linear-gradient(135deg, #3b82f6, #8b5cf6);
      width: 38px;
      height: 38px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 700;
    }

    .brand-title {
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .printer-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.75rem;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 4px 10px;
      border-radius: 9999px;
      font-weight: 500;
      margin-left: 10px;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 18px;
      font-size: 0.875rem;
      font-weight: 600;
      border-radius: 8px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .btn-primary {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.4);
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
      transform: translateY(-1px);
    }

    .btn-secondary {
      background-color: #334155;
      color: #f1f5f9;
      border-color: #475569;
    }

    .btn-secondary:hover {
      background-color: #475569;
    }

    /* Main Workspace Layout */
    .app-main {
      display: grid;
      grid-template-columns: 330px 1fr;
      flex: 1;
      height: calc(100vh - 64px);
      overflow: hidden;
    }

    /* Sidebar Controls */
    .sidebar {
      background-color: #131d2f;
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }

    .sidebar-section {
      padding: 16px;
      border-bottom: 1px solid var(--border-color);
    }

    .sidebar-title {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Drop Zone */
    .drop-zone {
      border: 2px dashed #475569;
      border-radius: 12px;
      padding: 24px 16px;
      text-align: center;
      background: rgba(30, 41, 59, 0.5);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .drop-zone:hover, .drop-zone.dragover {
      border-color: var(--primary);
      background: rgba(59, 130, 246, 0.12);
      transform: scale(1.01);
    }

    .drop-icon {
      color: var(--primary);
      margin-bottom: 8px;
    }

    .drop-text {
      font-size: 0.875rem;
      font-weight: 600;
      margin-bottom: 4px;
    }

    .drop-subtext {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    /* Settings Controls */
    .control-group {
      margin-bottom: 14px;
    }

    .control-label {
      display: block;
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 6px;
      font-weight: 500;
    }

    .select-input {
      width: 100%;
      background: #1e293b;
      border: 1px solid #475569;
      color: white;
      padding: 8px 10px;
      border-radius: 6px;
      font-size: 0.85rem;
      outline: none;
      font-family: inherit;
    }

    .select-input:focus {
      border-color: var(--primary);
    }

    .toggle-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      font-size: 0.85rem;
    }

    .toggle-row input[type="checkbox"] {
      width: 16px;
      height: 16px;
      accent-color: var(--primary);
      cursor: pointer;
    }

    /* Workspace Quick File Picker */
    .file-list {
      max-height: 250px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .file-item {
      padding: 8px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
      color: #cbd5e1;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.15s ease;
      background: rgba(30, 41, 59, 0.3);
      border: 1px solid transparent;
    }

    .file-item:hover {
      background: #1e293b;
      border-color: #475569;
      color: white;
    }

    /* Preview Canvas Container */
    .preview-container {
      background-color: #0b1120;
      padding: 30px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }

    .preview-toolbar {
      width: 100%;
      max-width: var(--paper-width);
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    /* Print Paper Sheet (A4 Simulation) */
    .paper-sheet {
      width: var(--paper-width);
      min-height: var(--paper-min-height);
      background: white;
      color: #1e293b;
      padding: 18mm 16mm;
      box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.6), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
      border-radius: 2px;
      position: relative;
      transition: font-size 0.2s ease, padding 0.2s ease;
    }

    /* Markdown Body Styling */
    .markdown-body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      color: #1e293b;
    }

    .markdown-body.serif-font {
      font-family: 'Merriweather', Georgia, serif;
      line-height: 1.7;
    }

    .markdown-body.mono-font {
      font-family: 'Fira Code', Consolas, monospace;
    }

    /* Font Size Presets */
    .font-compact { font-size: 9.5pt; }
    .font-compact h1 { font-size: 16pt; margin-top: 14pt; margin-bottom: 6pt; }
    .font-compact h2 { font-size: 13pt; margin-top: 12pt; margin-bottom: 5pt; }
    .font-compact h3 { font-size: 11pt; margin-top: 10pt; margin-bottom: 4pt; }
    .font-compact pre, .font-compact code { font-size: 8.5pt; }

    .font-standard { font-size: 10.5pt; }
    .font-standard h1 { font-size: 19pt; margin-top: 18pt; margin-bottom: 8pt; }
    .font-standard h2 { font-size: 15pt; margin-top: 14pt; margin-bottom: 6pt; }
    .font-standard h3 { font-size: 12.5pt; margin-top: 12pt; margin-bottom: 5pt; }
    .font-standard pre, .font-standard code { font-size: 9pt; }

    .font-large { font-size: 12pt; }
    .font-large h1 { font-size: 22pt; margin-top: 20pt; margin-bottom: 10pt; }
    .font-large h2 { font-size: 17pt; margin-top: 16pt; margin-bottom: 8pt; }
    .font-large h3 { font-size: 14pt; margin-top: 14pt; margin-bottom: 6pt; }
    .font-large pre, .font-large code { font-size: 10pt; }

    /* Margins */
    .margin-narrow { padding: 12mm 10mm; }
    .margin-standard { padding: 18mm 16mm; }
    .margin-wide { padding: 25mm 22mm; }

    /* Two Columns Layout */
    .two-column-layout {
      column-count: 2;
      column-gap: 8mm;
      column-rule: 1px solid #e2e8f0;
    }
    .two-column-layout h1, 
    .two-column-layout .document-header {
      column-span: all;
    }

    /* Elements */
    .markdown-body h1, .markdown-body h2, .markdown-body h3, 
    .markdown-body h4, .markdown-body h5, .markdown-body h6 {
      font-weight: 700;
      color: #0f172a;
      page-break-after: avoid;
      break-after: avoid;
    }

    .markdown-body h1 {
      border-bottom: 2px solid #0f172a;
      padding-bottom: 4px;
    }

    .markdown-body h2 {
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 3px;
    }

    .markdown-body p {
      margin-bottom: 8pt;
    }

    .markdown-body ul, .markdown-body ol {
      margin-bottom: 8pt;
      padding-left: 20pt;
    }

    .markdown-body li {
      margin-bottom: 3pt;
    }

    /* Tables */
    .markdown-body table {
      width: 100%;
      border-collapse: collapse;
      margin: 10pt 0;
      font-size: 0.9em;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .markdown-body th, .markdown-body td {
      border: 1px solid #94a3b8;
      padding: 5pt 7pt;
      text-align: left;
      vertical-align: top;
    }

    .markdown-body th {
      background-color: #f1f5f9;
      font-weight: 600;
      color: #0f172a;
    }

    .markdown-body tr:nth-child(even) {
      background-color: #f8fafc;
    }

    /* Code Blocks */
    .markdown-body pre {
      background-color: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 8pt 10pt;
      margin: 8pt 0;
      overflow-x: auto;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .markdown-body code {
      font-family: 'Fira Code', Consolas, Monaco, monospace;
      background-color: #f1f5f9;
      border: 1px solid #e2e8f0;
      padding: 1pt 3pt;
      border-radius: 3px;
      color: #b91c1c;
      font-size: 0.9em;
    }

    .markdown-body pre code {
      background: none;
      border: none;
      padding: 0;
      color: inherit;
    }

    .markdown-body blockquote {
      border-left: 4px solid #3b82f6;
      background-color: #f8fafc;
      padding: 6pt 10pt;
      margin: 8pt 0;
      color: #334155;
      font-style: italic;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .markdown-body hr {
      border: 0;
      border-top: 1px solid #cbd5e1;
      margin: 12pt 0;
    }

    /* Page Break Helper */
    .page-break {
      page-break-before: always;
      break-before: page;
      height: 0;
      margin: 0;
      border: none;
    }

    /* Document Header on Paper */
    .document-header {
      border-bottom: 2px solid #0f172a;
      padding-bottom: 8pt;
      margin-bottom: 14pt;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }

    .doc-meta-title {
      font-size: 1.3em;
      font-weight: 800;
      color: #0f172a;
    }

    .doc-meta-subtitle {
      font-size: 0.8em;
      color: #64748b;
    }

    /* PRINT STYLESHEET (OPTIMIZED FOR BROTHER & A4 LASER PRINTERS) */
    @media print {
      @page {
        size: A4 portrait;
        margin: 12mm 10mm 12mm 10mm;
      }

      body {
        background: white !important;
        color: black !important;
        margin: 0 !important;
        padding: 0 !important;
      }

      .app-header,
      .sidebar,
      .preview-toolbar,
      .no-print {
        display: none !important;
      }

      .app-main {
        display: block !important;
        height: auto !important;
        overflow: visible !important;
      }

      .preview-container {
        padding: 0 !important;
        background: transparent !important;
        overflow: visible !important;
      }

      .paper-sheet {
        width: 100% !important;
        min-height: auto !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        background: transparent !important;
      }

      .markdown-body {
        color: #000000 !important;
      }

      .markdown-body th {
        background-color: #f1f1f1 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .markdown-body code {
        color: #000 !important;
        background-color: #f5f5f5 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .markdown-body pre {
        background-color: #f9f9f9 !important;
        border-color: #999 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }

      .markdown-body a {
        color: #000 !important;
        text-decoration: underline !important;
      }

      .page-break {
        page-break-before: always !important;
        break-before: page !important;
      }

      .avoid-break {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Navigation Bar -->
  <header class="app-header no-print">
    <div class="brand-section">
      <div class="brand-icon">
        <i data-lucide="printer"></i>
      </div>
      <div>
        <div class="brand-title">PSU Markdown Print Studio</div>
      </div>
      <div id="printer-status" class="printer-badge">
        <i data-lucide="check-circle" style="width: 12px; height: 12px;"></i>
        <span id="printer-name">Detecting Printer...</span>
      </div>
    </div>

    <div class="header-actions">
      <button class="btn btn-secondary" onclick="openFilePicker()">
        <i data-lucide="folder-open" style="width: 16px; height: 16px;"></i>
        Open .md
      </button>
      <input type="file" id="file-input" accept=".md,.markdown,.txt" style="display: none;" onchange="handleFileSelect(event)">
      
      <button class="btn btn-secondary" onclick="resetToSample()">
        <i data-lucide="refresh-cw" style="width: 16px; height: 16px;"></i>
        Sample Note
      </button>

      <button class="btn btn-primary" onclick="triggerPrint()">
        <i data-lucide="printer" style="width: 18px; height: 18px;"></i>
        Print to Brother Printer (Ctrl+P)
      </button>
    </div>
  </header>

  <!-- Main Split Layout -->
  <main class="app-main">
    
    <!-- Left Sidebar: Controls & File Explorer -->
    <aside class="sidebar no-print">
      
      <!-- Drag and Drop Box -->
      <div class="sidebar-section">
        <div class="sidebar-title">
          <i data-lucide="upload-cloud" style="width: 14px; height: 14px;"></i>
          Drop Markdown File
        </div>
        <div id="drop-zone" class="drop-zone" onclick="openFilePicker()">
          <div class="drop-icon">
            <i data-lucide="file-text" style="width: 32px; height: 32px; margin: 0 auto;"></i>
          </div>
          <div class="drop-text">Drag & Drop *.md file here</div>
          <div class="drop-subtext">or click to browse from PC</div>
        </div>
      </div>

      <!-- Print & Page Format Controls -->
      <div class="sidebar-section">
        <div class="sidebar-title">
          <i data-lucide="sliders" style="width: 14px; height: 14px;"></i>
          Print Layout Options
        </div>

        <div class="control-group">
          <label class="control-label">Font Size</label>
          <select id="fontSizeSelect" class="select-input" onchange="applySettings()">
            <option value="font-compact">Compact (9.5pt) — High Density / Cheat Sheet</option>
            <option value="font-standard" selected>Standard (10.5pt) — Balanced</option>
            <option value="font-large">Large (12pt) — High Legibility</option>
          </select>
        </div>

        <div class="control-group">
          <label class="control-label">Typography Style</label>
          <select id="fontFamilySelect" class="select-input" onchange="applySettings()">
            <option value="sans-font" selected>Clean Inter Sans (Modern / Tech)</option>
            <option value="serif-font">Merriweather Serif (Book / Formal)</option>
            <option value="mono-font">Fira Code (Code Heavy / Specs)</option>
          </select>
        </div>

        <div class="control-group">
          <label class="control-label">Page Margins</label>
          <select id="marginSelect" class="select-input" onchange="applySettings()">
            <option value="margin-narrow">Narrow (10mm) — Max Page Use</option>
            <option value="margin-standard" selected>Standard (16mm) — Balanced A4</option>
            <option value="margin-wide">Wide (22mm) — Formal Margin</option>
          </select>
        </div>

        <div class="toggle-row">
          <span>2-Column Layout (Cheat Sheet)</span>
          <input type="checkbox" id="twoColumnToggle" onchange="applySettings()">
        </div>

        <div class="toggle-row">
          <span>Include Header Banner</span>
          <input type="checkbox" id="headerToggle" checked onchange="applySettings()">
        </div>
      </div>

      <!-- Quick Workspace Explorer -->
      <div class="sidebar-section" style="flex: 1; display: flex; flex-direction: column;">
        <div class="sidebar-title">
          <i data-lucide="files" style="width: 14px; height: 14px;"></i>
          Workspace Markdown Notes
        </div>
        <div id="workspace-files" class="file-list">
          <div style="font-size: 0.8rem; color: #64748b; padding: 10px; text-align: center;">
            Scanning notes...
          </div>
        </div>
      </div>

    </aside>

    <!-- Right Canvas: Paper Preview Simulation -->
    <section class="preview-container">
      <div class="preview-toolbar no-print">
        <div>
          <strong id="active-filename" style="color: #f1f5f9;">01-KEYS-AND-CONSTRAINTS.md</strong>
          <span id="active-filesize" style="margin-left: 8px; color: #64748b;">(12.4 KB)</span>
        </div>
        <div style="font-size: 0.8rem; color: #94a3b8;">
          Formatted A4 Print Preview
        </div>
      </div>

      <!-- A4 Sheet Element -->
      <div id="paper" class="paper-sheet font-standard margin-standard">
        
        <!-- Document Header Banner -->
        <div id="doc-header" class="document-header">
          <div>
            <div id="doc-title-text" class="doc-meta-title">DBMS: Keys & Constraints</div>
            <div id="doc-subtitle-text" class="doc-meta-subtitle">PSU Revision Core Notes &bull; Avanish Gupta</div>
          </div>
          <div id="doc-date" class="doc-meta-subtitle" style="text-align: right;">
            Print Date: <span id="current-date-span"></span>
          </div>
        </div>

        <!-- Rendered Markdown Body -->
        <div id="markdown-content" class="markdown-body">
          <!-- Markdown will render here -->
        </div>

      </div>
    </section>

  </main>

  <script>
    lucide.createIcons();

    let rawMarkdown = "";
    let currentFileName = "Sample_Note.md";

    const SAMPLE_MARKDOWN = `# Database Management Systems: Keys, Constraints & ACID

## 1. Relational Keys Overview

A **key** is an attribute or set of attributes that uniquely identifies any tuple in a relation.

| Key Type | Definition | Key Characteristics | Can be NULL? |
| :--- | :--- | :--- | :---: |
| **Super Key (SK)** | Any superset of Candidate Key | Uniquely identifies rows | Partial |
| **Candidate Key (CK)** | Minimal Super Key | No redundant attribute | **NO** |
| **Primary Key (PK)** | Selected candidate key | Chosen for entity integrity | **NO (Strict)** |
| **Alternate Key (AK)** | Candidate keys not chosen as PK | Backup candidate key | **NO** |
| **Foreign Key (FK)** | References PK of another table | Maintains referential integrity | **YES** |

---

## 2. Integrity Constraints

\`\`\`sql
-- SQL Table definition with strict integrity constraints
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100) NOT NULL,
    DeptID INT,
    Salary DECIMAL(10,2) CHECK (Salary >= 25000),
    Email VARCHAR(150) UNIQUE,
    CONSTRAINT fk_department FOREIGN KEY (DeptID) 
        REFERENCES Department(DeptID) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE
);
\`\`\`

### Key Constraint Rules:
- [x] **Domain Constraint:** Value must belong to valid predefined data type.
- [x] **Entity Integrity Constraint:** Primary Key cannot accept NULL values.
- [x] **Referential Integrity Constraint:** Foreign Key value must match an existing PK or be NULL.

---

## 3. ACID Properties in Transaction Processing

> **Atomicity:** All operations succeed, or all fail (All or Nothing). Managed by Recovery Manager (Undo/Redo Log).  
> **Consistency:** Database remains in a valid state before and after execution.  
> **Isolation:** Intermediate states are invisible to concurrent transactions. Managed by Concurrency Control.  
> **Durability:** Committed changes persist even across system crashes.

\`\`\`text
T1: Read(A) -> A := A - 500 -> Write(A) -> Read(B) -> B := B + 500 -> Write(B) -> Commit
\`\`\`
`;

    // Configure Marked
    marked.setOptions({
      gfm: true,
      breaks: true,
      highlight: function(code, lang) {
        if (lang && hljs.getLanguage(lang)) {
          try {
            return hljs.highlight(code, { language: lang }).value;
          } catch (e) {}
        }
        return hljs.highlightAuto(code).value;
      }
    });

    // On Load
    window.addEventListener('DOMContentLoaded', () => {
      document.getElementById('current-date-span').textContent = new Date().toLocaleDateString('en-US', {
        year: 'numeric', month: 'short', day: 'numeric'
      });
      fetchSystemInfo();
      fetchWorkspaceFiles();
      loadMarkdownContent(SAMPLE_MARKDOWN, "01-KEYS-AND-CONSTRAINTS.md");
      setupDragAndDrop();
    });

    async function fetchSystemInfo() {
      try {
        const res = await fetch('/api/system-info');
        const data = await res.json();
        const printerEl = document.getElementById('printer-name');
        if (data.default_printer) {
          printerEl.textContent = `Printer: ${data.default_printer}`;
        } else {
          printerEl.textContent = 'Brother / System Printer Ready';
        }
      } catch (e) {
        document.getElementById('printer-name').textContent = 'Default Printer Ready';
      }
    }

    async function fetchWorkspaceFiles() {
      try {
        const res = await fetch('/api/workspace-files');
        const data = await res.json();
        const container = document.getElementById('workspace-files');
        container.innerHTML = '';
        
        if (!data.files || data.files.length === 0) {
          container.innerHTML = '<div style="font-size:0.8rem;color:#64748b;padding:8px;">No .md files found</div>';
          return;
        }

        data.files.forEach(f => {
          const item = document.createElement('div');
          item.className = 'file-item';
          item.innerHTML = `
            <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${f.rel_path}">
              ${f.name}
            </span>
            <span style="font-size: 0.7rem; color: #64748b;">${f.size_kb}K</span>
          `;
          item.onclick = () => loadWorkspaceFile(f.rel_path, f.name);
          container.appendChild(item);
        });
      } catch (e) {
        console.error('Failed to load workspace files', e);
      }
    }

    async function loadWorkspaceFile(relPath, name) {
      try {
        const res = await fetch(`/api/read-file?path=${encodeURIComponent(relPath)}`);
        const data = await res.json();
        loadMarkdownContent(data.content, name);
      } catch (e) {
        alert('Failed to read file from workspace: ' + e.message);
      }
    }

    function loadMarkdownContent(mdText, filename) {
      rawMarkdown = mdText;
      currentFileName = filename || "Document.md";
      
      document.getElementById('active-filename').textContent = currentFileName;
      const sizeKB = (new Blob([mdText]).size / 1024).toFixed(1);
      document.getElementById('active-filesize').textContent = `(${sizeKB} KB)`;

      // Extract First H1 for document title
      const titleMatch = mdText.match(/^#\s+(.+)$/m);
      if (titleMatch) {
        document.getElementById('doc-title-text').textContent = titleMatch[1];
      } else {
        document.getElementById('doc-title-text').textContent = currentFileName.replace(/\.[^/.]+$/, "");
      }

      // Convert pagebreak tags
      let parsed = mdText
        .replace(/<!--\s*pagebreak\s*-->/gi, '<div class="page-break"></div>')
        .replace(/\\pagebreak/g, '<div class="page-break"></div>');

      const html = marked.parse(parsed);
      document.getElementById('markdown-content').innerHTML = html;

      // Wrap tables & code blocks in avoid-break class
      document.querySelectorAll('#markdown-content table').forEach(t => t.classList.add('avoid-break'));
      document.querySelectorAll('#markdown-content pre').forEach(p => p.classList.add('avoid-break'));
      document.querySelectorAll('#markdown-content blockquote').forEach(b => b.classList.add('avoid-break'));

      lucide.createIcons();
    }

    function setupDragAndDrop() {
      const dropZone = document.getElementById('drop-zone');

      ['dragenter', 'dragover'].forEach(name => {
        window.addEventListener(name, (e) => {
          e.preventDefault();
          e.stopPropagation();
          dropZone.classList.add('dragover');
        });
      });

      ['dragleave', 'drop'].forEach(name => {
        window.addEventListener(name, (e) => {
          e.preventDefault();
          e.stopPropagation();
          dropZone.classList.remove('dragover');
        });
      });

      window.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length > 0) {
          handleFile(files[0]);
        }
      });
    }

    function openFilePicker() {
      document.getElementById('file-input').click();
    }

    function handleFileSelect(e) {
      if (e.target.files.length > 0) {
        handleFile(e.target.files[0]);
      }
    }

    function handleFile(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        loadMarkdownContent(e.target.result, file.name);
      };
      reader.readAsText(file);
    }

    function resetToSample() {
      loadMarkdownContent(SAMPLE_MARKDOWN, "DBMS_Keys_And_Constraints.md");
    }

    function applySettings() {
      const paper = document.getElementById('paper');
      const content = document.getElementById('markdown-content');
      
      // Font Size
      paper.classList.remove('font-compact', 'font-standard', 'font-large');
      paper.classList.add(document.getElementById('fontSizeSelect').value);

      // Margins
      paper.classList.remove('margin-narrow', 'margin-standard', 'margin-wide');
      paper.classList.add(document.getElementById('marginSelect').value);

      // Font Family
      content.classList.remove('sans-font', 'serif-font', 'mono-font');
      content.classList.add(document.getElementById('fontFamilySelect').value);

      // Two Column Layout
      if (document.getElementById('twoColumnToggle').checked) {
        content.classList.add('two-column-layout');
      } else {
        content.classList.remove('two-column-layout');
      }

      // Header Banner
      const header = document.getElementById('doc-header');
      header.style.display = document.getElementById('headerToggle').checked ? 'flex' : 'none';
    }

    function triggerPrint() {
      window.print();
    }

    // Keyboard shortcut Ctrl+P
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
        e.preventDefault();
        triggerPrint();
      }
    });
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_index():
    return HTMLResponse(content=INDEX_HTML)

def is_port_free(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(('127.0.0.1', port)) != 0

def find_first_free_port(preferred_ports=[8888, 5500, 7860, 9000, 9999, 8000]):
    for port in preferred_ports:
        if is_port_free(port):
            return port
    for p in range(8001, 8999):
        if is_port_free(p):
            return p
    return 8888

def run_server(port: int = None):
    if port is None:
        port = find_first_free_port()
    
    print("==================================================")
    print(f"PSU Markdown Print Studio starting on http://localhost:{port}")
    print("Connects to Brother / System Printer with A4 auto-formatting")
    print("==================================================")
    
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass
        
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="info")

if __name__ == "__main__":
    p = None
    if len(sys.argv) > 1:
        try:
            p = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port=p)
