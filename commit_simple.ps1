# Neural-Haikus Project Commit Script (Simple Version)
# This script creates focused commits using single-line messages

Write-Host "🚀 Neural-Haikus Commit Script (Simple Version)" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Creating focused commits with single-line messages.`n"

# Function to confirm
function Confirm-Commit {
    $response = Read-Host "Proceed? (y/n)"
    if ($response -ne 'y') {
        Write-Host "Cancelled." -ForegroundColor Red
        exit 1
    }
}

# Commit 1
Write-Host "`n📝 Commit 1: CLAUDE.md" -ForegroundColor Green
git add CLAUDE.md
git status --short
Confirm-Commit
git commit -m "docs: Update CLAUDE.md with comprehensive prompt library documentation and orchestrator commands"

# Commit 2
Write-Host "`n📚 Commit 2: Prompt library reorganization" -ForegroundColor Green
git add prompts/
git status --short
Confirm-Commit
git commit -m "refactor: Reorganize prompt library with phase-based structure and quick-start folder"

# Commit 3
Write-Host "`n📖 Commit 3: Prompt documentation" -ForegroundColor Green
git add PROMPT_MIGRATION_COMPLETE.md
git status --short
Confirm-Commit
git commit -m "docs: Add prompt library catalog, migration report, and search index"

# Commit 4
Write-Host "`n📊 Commit 4: Orchestrator" -ForegroundColor Green
git add orchestrator.py
git status --short
Confirm-Commit
git commit -m "feat: Update orchestrator.py for compatibility with new prompt structure"

# Commit 5
Write-Host "`n📄 Commit 5: Project docs" -ForegroundColor Green
git add README.md features.txt ORCHESTRATION_*.md PROMPT_ORGANIZATION_REPORT.md REORGANIZATION_COMPLETE.md
git status --short
Confirm-Commit
git commit -m "docs: Update project documentation including README and analysis reports"

# Commit 6
Write-Host "`n🔧 Commit 6: Workspace outputs" -ForegroundColor Green
git add orchestrator_workspace/outputs/
git status --short
Confirm-Commit
git commit -m "chore: Update orchestrator workspace outputs and templates"

# Commit 7
Write-Host "`n💾 Commit 7: Sessions" -ForegroundColor Green
git add orchestrator_workspace/sessions/
git status --short
Confirm-Commit
git commit -m "chore: Update orchestrator session state files"

# Commit 8
Write-Host "`n🤖 Commit 8: Claude integration" -ForegroundColor Green
git add .claude/
git status --short
Confirm-Commit
git commit -m "feat: Add Claude Code integration directory"

# Commit 9 (optional)
Write-Host "`n🗄️ Commit 9: Backup (optional)" -ForegroundColor Green
$backup = Read-Host "Include prompts_backup? (y/n)"
if ($backup -eq 'y') {
    git add prompts_backup/
    git status --short
    git commit -m "backup: Add original prompt library structure for reference"
}

Write-Host "`n✅ Done!" -ForegroundColor Green
git status
Write-Host "`nNext: git log --oneline" -ForegroundColor Yellow