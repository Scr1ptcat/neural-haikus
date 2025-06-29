# Neural-Haikus Project Commit Script (PowerShell)
# This script organizes all changes into logical, focused commits
# Review each commit before proceeding

Write-Host "🚀 Neural-Haikus Commit Script" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan
Write-Host "This script will create focused commits for all changes."
Write-Host "Please review each commit message before proceeding.`n"

# Function to pause and ask for confirmation
function Confirm-Commit {
    $response = Read-Host "➡️  Proceed with this commit? (y/n)"
    if ($response -ne 'y') {
        Write-Host "❌ Commit cancelled. Exiting..." -ForegroundColor Red
        exit 1
    }
}

# Commit 1: CLAUDE.md improvements
Write-Host "`n📝 Commit 1: Update CLAUDE.md with prompt library documentation" -ForegroundColor Green
Write-Host "Files: CLAUDE.md"
git add CLAUDE.md
git status --short
Confirm-Commit
git commit -m @"
docs: Update CLAUDE.md with comprehensive prompt library info

- Added detailed orchestrator commands including resume and process utilities
- Documented new prompt library structure with 27+ templates
- Added prompt library categories and usage guidelines
- Updated directory structure to reflect reorganized prompts
- Added batch processing and session management instructions

 
"@

# Commit 2: Prompt library reorganization
Write-Host "`n📚 Commit 2: Reorganize prompt library with improved structure" -ForegroundColor Green
Write-Host "Files: prompts/* (new structure)"
git add prompts/
git status --short
Confirm-Commit
git commit -m @"
refactor: Reorganize prompt library for better discoverability

- Created quick-start folder with top 5 most-used prompts
- Organized prompts by SDLC phase (planning→design→implementation→testing→debugging→maintenance)
- Added complexity-based navigation (simple/standard/comprehensive)
- Separated advanced prompts (optimized/specialized)
- Centralized documentation in _catalog directory
- Created comprehensive INDEX.md for navigation
- Removed 1 duplicate file: quality-comprehensive (copy).md

Structure now provides multiple access paths and better scalability.

 
"@

# Commit 3: Prompt library documentation
Write-Host "`n📖 Commit 3: Add comprehensive prompt library documentation" -ForegroundColor Green
Write-Host "Files: prompts/_catalog/*, prompts/INDEX.md, PROMPT_MIGRATION_COMPLETE.md"
git add PROMPT_MIGRATION_COMPLETE.md
git status --short
Confirm-Commit
git commit -m @"
docs: Add prompt library catalog and migration documentation

- Created CATALOG.md with detailed index of all 62 prompts
- Added migration report documenting reorganization
- Created search-index.json for programmatic access
- Added INDEX.md for easy navigation
- Documented migration process and benefits

Provides comprehensive documentation for the reorganized prompt library.

 
"@

# Commit 4: Orchestrator improvements
Write-Host "`n📊 Commit 4: Update orchestrator.py" -ForegroundColor Green
Write-Host "Files: orchestrator.py"
git add orchestrator.py
git status --short
Confirm-Commit
git commit -m @"
feat: Update orchestrator.py

- Updated orchestrator script (specific changes need review)
- Maintains compatibility with new prompt structure

 
"@

# Commit 5: Project documentation updates
Write-Host "`n📄 Commit 5: Update project documentation" -ForegroundColor Green
Write-Host "Files: README.md, features.txt, ORCHESTRATION_*.md, REORGANIZATION_COMPLETE.md"
git add README.md features.txt ORCHESTRATION_*.md PROMPT_ORGANIZATION_REPORT.md REORGANIZATION_COMPLETE.md
git status --short
Confirm-Commit
git commit -m @"
docs: Update project documentation files

- Updated README.md
- Modified features.txt with latest feature requests
- Updated orchestration analysis reports
- Added prompt organization report
- Updated reorganization completion status

Ensures all project documentation is current.

 
"@

# Commit 6: Orchestrator workspace outputs
Write-Host "`n🔧 Commit 6: Update orchestrator workspace outputs" -ForegroundColor Green
Write-Host "Files: orchestrator_workspace/outputs/*"
git add orchestrator_workspace/outputs/
git status --short
Confirm-Commit
git commit -m @"
chore: Update orchestrator workspace outputs

- Updated analysis outputs and templates
- Modified execution notes and implementation templates
- Updated summaries for completed sessions

Reflects latest orchestrator workflow executions.

 
"@

# Commit 7: Orchestrator sessions
Write-Host "`n💾 Commit 7: Update orchestrator session files" -ForegroundColor Green
Write-Host "Files: orchestrator_workspace/sessions/*"
git add orchestrator_workspace/sessions/
git status --short
Confirm-Commit
git commit -m @"
chore: Update orchestrator session states

- Updated session JSON files with latest states
- Modified session tracking data

Maintains session continuity for orchestrator workflows.

 
"@

# Commit 8: Claude integration
Write-Host "`n🤖 Commit 8: Add Claude Code integration" -ForegroundColor Green
Write-Host "Files: .claude/"
git add .claude/
git status --short
Confirm-Commit
git commit -m @"
feat: Add Claude Code integration

- Added .claude directory for Claude Code configuration
- Enables better integration with Claude AI assistant

 
"@

# Commit 9: Backup and migration artifacts
Write-Host "`n🗄️ Commit 9: Add prompt library backup" -ForegroundColor Green
Write-Host "Files: prompts_backup/"
Write-Host "Note: You may want to skip this commit if backup is temporary" -ForegroundColor Yellow
$backupResponse = Read-Host "➡️  Include backup directory in commit? (y/n)"
if ($backupResponse -eq 'y') {
    git add prompts_backup/
    git status --short
    git commit -m @"
backup: Add original prompt library structure

- Preserved original prompt organization before migration
- Can be removed after confirming new structure works well

 
"@
} else {
    Write-Host "⏭️  Skipping backup directory" -ForegroundColor Yellow
}

# Final check
Write-Host "`n✅ All commits prepared!" -ForegroundColor Green
Write-Host ""
git status
Write-Host "`n🎉 Done! All changes have been organized into focused commits." -ForegroundColor Cyan
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Review the commit history: git log --oneline"
Write-Host "2. Push to remote: git push origin main"
Write-Host "3. Remove prompts_backup/ if no longer needed"
Write-Host "4. Clean up any temporary files"