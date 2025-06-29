# Neural-Haikus Project Commit Script
# Simple version with standard quotes

Write-Host "Neural-Haikus Commit Script" -ForegroundColor Cyan
Write-Host "===========================" -ForegroundColor Cyan
Write-Host "Creating focused commits."
Write-Host ""

# Function to confirm
function Confirm-Commit {
    $response = Read-Host "Proceed? (y/n)"
    if ($response -ne "y") {
        Write-Host "Cancelled." -ForegroundColor Red
        exit 1
    }
}

# Commit 1
Write-Host ""
Write-Host "Commit 1: CLAUDE.md" -ForegroundColor Green
git add CLAUDE.md
git status --short
Confirm-Commit
git commit -m "docs: Update CLAUDE.md with comprehensive prompt library documentation and orchestrator commands"

# Commit 2
Write-Host ""
Write-Host "Commit 2: Prompt library reorganization" -ForegroundColor Green
git add prompts/
git status --short
Confirm-Commit
git commit -m "refactor: Reorganize prompt library with phase-based structure and quick-start folder"

# Commit 3
Write-Host ""
Write-Host "Commit 3: Prompt documentation" -ForegroundColor Green
git add PROMPT_MIGRATION_COMPLETE.md
git status --short
Confirm-Commit
git commit -m "docs: Add prompt library catalog, migration report, and search index"

# Commit 4
Write-Host ""
Write-Host "Commit 4: Orchestrator" -ForegroundColor Green
git add orchestrator.py
git status --short
Confirm-Commit
git commit -m "feat: Update orchestrator.py for compatibility with new prompt structure"

# Commit 5
Write-Host ""
Write-Host "Commit 5: Project docs" -ForegroundColor Green
git add README.md features.txt ORCHESTRATION_*.md PROMPT_ORGANIZATION_REPORT.md REORGANIZATION_COMPLETE.md
git status --short
Confirm-Commit
git commit -m "docs: Update project documentation including README and analysis reports"

# Commit 6
Write-Host ""
Write-Host "Commit 6: Workspace outputs" -ForegroundColor Green
git add orchestrator_workspace/outputs/
git status --short
Confirm-Commit
git commit -m "chore: Update orchestrator workspace outputs and templates"

# Commit 7
Write-Host ""
Write-Host "Commit 7: Sessions" -ForegroundColor Green
git add orchestrator_workspace/sessions/
git status --short
Confirm-Commit
git commit -m "chore: Update orchestrator session state files"

# Commit 8
Write-Host ""
Write-Host "Commit 8: Claude integration" -ForegroundColor Green
git add .claude/
git status --short
Confirm-Commit
git commit -m "feat: Add Claude Code integration directory"

# Commit 9 (optional)
Write-Host ""
Write-Host "Commit 9: Backup (optional)" -ForegroundColor Green
$backup = Read-Host "Include prompts_backup? (y/n)"
if ($backup -eq "y") {
    git add prompts_backup/
    git status --short
    git commit -m "backup: Add original prompt library structure for reference"
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Green
git status
Write-Host ""
Write-Host "Next: git log --oneline" -ForegroundColor Yellow