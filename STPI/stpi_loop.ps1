# STPI Daily Prep Loop Script
# This script runs in the background and outputs a tick every 24 hours to trigger daily goals and questions.

Write-Output "STPI Daily Prep Loop started successfully."

while ($true) {
    Start-Sleep -Seconds 86400
    Write-Output 'AGENT_LOOP_TICK_STPI_PREP {"prompt":"Deliver the daily STPI study goal and mock interview question"}'
}
