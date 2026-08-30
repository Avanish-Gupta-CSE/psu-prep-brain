@echo off
title PSU Markdown Print Studio (Brother Printer Ready)
echo =======================================================
echo   Starting PSU Markdown Print Studio on http://localhost:8888
echo   Drag and drop any *.md file to preview and print
echo =======================================================
python "%~dp0md_print_server.py" 8888
pause
