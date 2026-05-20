$inputPath = "c:\Users\agupt1\Projects\Personal\psu-prep-brain\MSTC\Quick Revision Ebook\raw.txt"
$outputPath = "c:\Users\agupt1\Projects\Personal\psu-prep-brain\MSTC\Quick Revision Ebook\revision-ebook-minimax.md"

$content = Get-Content $inputPath -Raw

# Replace page markers with line breaks
$content = $content -replace '<<P\d+-L\d+>>', [char]10

# Clean up extra whitespace
$content = $content -replace '\s+', ' '

# Fix common OCR artifacts
$content = $content -replace 'Â\xa0', ' '
$content = $content -replace 'Â¢', '-'
$content = $content -replace 'Â®', '(R)'
$content = $content -replace 'Â©', '(C)'
$content = $content -replace 'Â§', '§'
$content = $content -replace 'Â¶', '¶'
$content = $content -replace 'â€¢', '•'
$content = $content -replace 'â‰¥', '≥'
$content = $content -replace 'â‰¤', '≤'
$content = $content -replace 'â‰', '≈'
$content = $content -replace 'â€"', '"'
$content = $content -replace 'â€"', '"'
$content = $content -replace 'â€"', "'"
$content = $content -replace 'â€"', "'"
$content = $content -replace 'Î±', 'α'
$content = $content -replace 'Î²', 'β'
$content = $content -replace 'Î³', 'γ'

# Remove any remaining [data:...] artifacts
$content = $content -replace '\[data:[^\]]*\]', ''

# Ensure blank lines around section headers (lines ending with numbers like 3-10)
$content = $content -replace '(\d+-\d+)\s+([A-Z])', "`$1`n`$2"

# Save
$content | Out-File -FilePath $outputPath -Encoding UTF8

Write-Host "Conversion complete. Output: $outputPath"