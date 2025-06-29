# Neural-Haikus Remaining Commits Script
# Handles the files not included in the first batch

Write-Host "Handling Remaining Commits" -ForegroundColor Cyan
Write-Host "==========================" -ForegroundColor Cyan
Write-Host ""

# Check what remains
Write-Host "Checking remaining changes..." -ForegroundColor Yellow
git status --short
Write-Host ""

# Function to confirm
function Confirm-Commit {
    $response = Read-Host "Proceed? (y/n)"
    if ($response -ne "y") {
        Write-Host "Cancelled." -ForegroundColor Red
        exit 1
    }
}

# Commit 10: Commit scripts
Write-Host "Commit 10: Commit helper scripts" -ForegroundColor Green
git add commit_*.ps1 commit_*.sh
git status --short
Confirm-Commit
git commit -m "chore: Add commit helper scripts for organizing changes"

# Commit 11: prompts_new if it exists
if (Test-Path "prompts_new") {
    Write-Host ""
    Write-Host "Commit 11: New prompts structure (temporary)" -ForegroundColor Green
    git add prompts_new/
    git status --short
    Confirm-Commit
    git commit -m "temp: Add new prompts structure for migration"
}

# Commit 12: Any remaining prompt files
Write-Host ""
Write-Host "Commit 12: Remaining prompt updates" -ForegroundColor Green
$promptFiles = git status --porcelain | Where-Object { $_ -match "prompts/" } | ForEach-Object { $_.Substring(3) }
if ($promptFiles) {
    foreach ($file in $promptFiles) {
        git add $file
    }
    git status --short
    Confirm-Commit
    git commit -m "chore: Update remaining prompt files"
}

# Commit 13: Migration artifacts
Write-Host ""
Write-Host "Commit 13: Migration artifacts" -ForegroundColor Green
git add reorganize_prompts.py reorganization_map.json 2>$null
git add migration_plan.txt 2>$null
git status --short
if (git status --porcelain) {
    Confirm-Commit
    git commit -m "chore: Add prompt reorganization scripts and mappings"
}

# Final check
Write-Host ""
Write-Host "Final Status:" -ForegroundColor Green
git status

Write-Host ""
Write-Host "Summary of all commits:" -ForegroundColor Cyan
git log --oneline -15