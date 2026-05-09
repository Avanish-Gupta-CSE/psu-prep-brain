$ErrorActionPreference = "Stop"

function Write-Json([hashtable]$obj) {
  $json = ($obj | ConvertTo-Json -Compress)
  [Console]::Out.WriteLine($json)
}

try {
  # Read hook payload (not required for behavior, but useful for future debugging).
  $raw = [Console]::In.ReadToEnd()
  if ($raw -and $raw.Trim().Length -gt 0) {
    try { $null = $raw | ConvertFrom-Json } catch { }
  }

  $git = Get-Command git -ErrorAction SilentlyContinue
  if (-not $git) {
    Write-Json @{}
    exit 0
  }

  # Only act when there are changes under .brain/ or MSTC/
  $changed = & git status --porcelain=v1 -- .brain MSTC 2>$null
  if (-not $changed -or $changed.Count -eq 0) {
    Write-Json @{}
    exit 0
  }

  & git add -A -- .brain MSTC | Out-Null

  # If nothing ended up staged, exit quietly.
  $staged = & git diff --cached --name-only -- .brain MSTC 2>$null
  if (-not $staged -or $staged.Count -eq 0) {
    Write-Json @{}
    exit 0
  }

  $today = Get-Date -Format "yyyy-MM-dd"
  $msg = "brain: sync MSTC notes ($today)"

  & git commit -m $msg | Out-Null

  # Push only when on main; otherwise attempt a fast-forward update to origin/main.
  $branch = (& git rev-parse --abbrev-ref HEAD).Trim()
  if ($branch -eq "main") {
    & git push origin main | Out-Null
  }
  else {
    & git fetch origin main 2>$null | Out-Null
    & git push origin HEAD:main 2>$null | Out-Null
  }

  Write-Json @{}
  exit 0
}
catch {
  # Fail open: never block session end due to sync issues.
  try { Write-Json @{} } catch { }
  exit 0
}
