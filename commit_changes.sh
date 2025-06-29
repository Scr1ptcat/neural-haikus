#!/bin/bash
# Neural-Haikus Project Commit Script
# This script organizes all changes into logical, focused commits
# Review each commit before proceeding

set -e  # Exit on error

echo "🚀 Neural-Haikus Commit Script"
echo "==============================="
echo "This script will create focused commits for all changes."
echo "Please review each commit message before proceeding."
echo ""

# Function to pause and ask for confirmation
confirm() {
    read -p "➡️  Proceed with this commit? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Commit cancelled. Exiting..."
        exit 1
    fi
}

# Commit 1: CLAUDE.md improvements
echo "📝 Commit 1: Update CLAUDE.md with prompt library documentation"
echo "Files: CLAUDE.md"
git add CLAUDE.md
git status --short
confirm
git commit -m "docs: Update CLAUDE.md with comprehensive prompt library info

- Added detailed orchestrator commands including resume and process utilities
- Documented new prompt library structure with 27+ templates
- Added prompt library categories and usage guidelines
- Updated directory structure to reflect reorganized prompts
- Added batch processing and session management instructions

 "

# Commit 2: Prompt library reorganization
echo ""
echo "📚 Commit 2: Reorganize prompt library with improved structure"
echo "Files: prompts/* (new structure)"
git add prompts/
git status --short
confirm
git commit -m "refactor: Reorganize prompt library for better discoverability

- Created quick-start folder with top 5 most-used prompts
- Organized prompts by SDLC phase (planning→design→implementation→testing→debugging→maintenance)
- Added complexity-based navigation (simple/standard/comprehensive)
- Separated advanced prompts (optimized/specialized)
- Centralized documentation in _catalog directory
- Created comprehensive INDEX.md for navigation
- Removed 1 duplicate file: quality-comprehensive (copy).md

Structure now provides multiple access paths and better scalability.

 "

# Commit 3: Prompt library documentation
echo ""
echo "📖 Commit 3: Add comprehensive prompt library documentation"
echo "Files: prompts/_catalog/*, prompts/INDEX.md, PROMPT_MIGRATION_COMPLETE.md"
git add PROMPT_MIGRATION_COMPLETE.md
git status --short
confirm
git commit -m "docs: Add prompt library catalog and migration documentation

- Created CATALOG.md with detailed index of all 62 prompts
- Added migration report documenting reorganization
- Created search-index.json for programmatic access
- Added INDEX.md for easy navigation
- Documented migration process and benefits

Provides comprehensive documentation for the reorganized prompt library.

 "

# Commit 4: Orchestrator improvements
echo ""
echo "📊 Commit 4: Update orchestrator.py"
echo "Files: orchestrator.py"
git add orchestrator.py
git status --short
confirm
git commit -m "feat: Update orchestrator.py

- Updated orchestrator script (specific changes need review)
- Maintains compatibility with new prompt structure

 "

# Commit 5: Project documentation updates
echo ""
echo "📄 Commit 5: Update project documentation"
echo "Files: README.md, features.txt, ORCHESTRATION_*.md, REORGANIZATION_COMPLETE.md"
git add README.md features.txt ORCHESTRATION_*.md PROMPT_ORGANIZATION_REPORT.md REORGANIZATION_COMPLETE.md
git status --short
confirm
git commit -m "docs: Update project documentation files

- Updated README.md
- Modified features.txt with latest feature requests
- Updated orchestration analysis reports
- Added prompt organization report
- Updated reorganization completion status

Ensures all project documentation is current.

 "

# Commit 6: Orchestrator workspace outputs
echo ""
echo "🔧 Commit 6: Update orchestrator workspace outputs"
echo "Files: orchestrator_workspace/outputs/*"
git add orchestrator_workspace/outputs/
git status --short
confirm
git commit -m "chore: Update orchestrator workspace outputs

- Updated analysis outputs and templates
- Modified execution notes and implementation templates
- Updated summaries for completed sessions

Reflects latest orchestrator workflow executions.

 "

# Commit 7: Orchestrator sessions
echo ""
echo "💾 Commit 7: Update orchestrator session files"
echo "Files: orchestrator_workspace/sessions/*"
git add orchestrator_workspace/sessions/
git status --short
confirm
git commit -m "chore: Update orchestrator session states

- Updated session JSON files with latest states
- Modified session tracking data

Maintains session continuity for orchestrator workflows.

 "



# Commit 9: Backup and migration artifacts
echo ""
echo "🗄️ Commit 9: Add prompt library backup"
echo "Files: prompts_backup/"
echo "Note: You may want to skip this commit if backup is temporary"
read -p "➡️  Include backup directory in commit? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git add prompts_backup/
    git status --short
    git commit -m "backup: Add original prompt library structure

- Preserved original prompt organization before migration
- Can be removed after confirming new structure works well

 "
else
    echo "⏭️  Skipping backup directory"
fi

# Final check
echo ""
echo "✅ All commits prepared!"
echo ""
git status
echo ""
echo "🎉 Done! All changes have been organized into focused commits."
echo ""
echo "Next steps:"
echo "1. Review the commit history: git log --oneline"
echo "2. Push to remote: git push origin main"
echo "3. Remove prompts_backup/ if no longer needed"
echo "4. Clean up any temporary files"