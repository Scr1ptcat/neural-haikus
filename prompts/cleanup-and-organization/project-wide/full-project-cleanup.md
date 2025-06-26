Please perform a comprehensive cleanup and reorganization of this project following these phases:
KEY OBJECTIVE: Don't just reorganize files - actively consolidate, merge, and rewrite content to eliminate redundancy and improve quality. This is especially important for documentation.
Phase 1: Initial Analysis
First, analyze the entire project structure:

List all directories and their purposes
Identify the project type (Python, JavaScript, etc.) and framework if applicable
Note the current location of tests, documentation, and build artifacts
Create a mental map of the project's intended structure

Phase 2: Test Consolidation

Identify all test files across the project:

Look for files matching patterns: *test*.py, *test*.js, test_*.py, *.test.js, *.spec.js, etc.
Check for test directories scattered throughout (e.g., __tests__, spec, etc.)
Note any test configuration files (pytest.ini, jest.config.js, etc.)


Create organized test structure:

Create a tests/ directory if it doesn't exist
Design a logical subdirectory structure within tests/ that mirrors the source code organization
Create tests/run_tests.sh or tests/run_tests.py as appropriate for the project type


Migrate tests:

Move test files to appropriate locations in tests/
Update import paths in test files as needed
Ensure test configuration files are properly located
Verify no test files remain scattered in the source directories



Phase 3: Documentation Consolidation and Rewriting
CRITICAL: This phase requires active content consolidation, not just file movement. You must read, analyze, merge, and rewrite documentation to eliminate redundancy.

Analyze all documentation:

Find all .md, .txt, .rst, and other documentation files
Exclude essential root-level files (README.md, LICENSE, CONTRIBUTING.md, CHANGELOG.md)
Create a content map: List what each document covers and identify overlaps
Note redundant information across multiple files
Identify outdated or contradictory information


Plan consolidated structure:

Create a docs/ directory if it doesn't exist
Design logical categories: docs/api/, docs/guides/, docs/architecture/, etc.
Plan merged documents: Instead of one-to-one moves, plan how to combine related content


Consolidate and rewrite documentation:

DO NOT simply move files - actively merge and rewrite content
For each topic area:

Gather all related documentation fragments
Combine into a single, coherent document
Remove redundancy while preserving all unique information
Update outdated information
Ensure consistent formatting and style


Example consolidations:

Multiple README files → Single comprehensive guide
Scattered API notes → Unified API documentation
Various setup instructions → One setup guide
Multiple "how-to" files → Organized tutorials section




Create new unified documents:

Write new consolidated files in docs/ with descriptive names
Create docs/README.md as a comprehensive index
Add cross-references between related documents
Delete the original scattered files only after content is preserved



Example Consolidation:
Before:

/src/api/auth_notes.txt (3 paragraphs about authentication)
/backend/README_AUTH.md (setup instructions)
/old_docs/authentication_flow.md (outdated flow diagram)
/temp/auth_todo.txt (implementation notes)

After:

/docs/api/authentication.md - Complete authentication guide combining all unique content, updated flow diagrams, clear setup instructions, and implementation details in a single, well-organized document

Phase 4: Dead and Temporary File Cleanup

Identify dead code:

Find unreferenced Python/JavaScript/etc. files
Locate obsolete configuration files
Identify deprecated modules or packages
Find empty or near-empty files that serve no purpose


Identify temporary files:

Build artifacts: dist/, build/, *.egg-info/, target/
Cache directories: __pycache__/, .cache/, .pytest_cache/
Editor files: *.swp, *~, .DS_Store, Thumbs.db
Compiled files: *.pyc, *.pyo, *.class, *.o
Dependencies: node_modules/ (if not needed), venv/, env/
Coverage reports: coverage/, .coverage, htmlcov/
Log files: *.log, logs/ (unless needed for debugging)


Safe removal process:

Double-check each file/directory before deletion
Preserve any .gitignore entries for temporary files
Do not delete: .git/, .gitignore, active virtual environments, or config files currently in use



Phase 5: Final Steps and Reporting

Update project files:

Update .gitignore to include any new temporary file patterns
Update README.md with new project structure if needed
Create or update docs/project-structure.md documenting the organization


Generate cleanup report:
=== PROJECT CLEANUP REPORT ===

TESTS CONSOLIDATED:
- Moved X test files to tests/
- Created test runner script: [path]
- Updated import paths in Y files

DOCUMENTATION ORGANIZED:
- Consolidated X documentation files into Y unified documents
- Merged content from: [list original files] → [new consolidated file]
- Created documentation index at docs/README.md
- Removed Z redundant paragraphs/sections
- Updated N outdated instructions

FILES REMOVED:
Dead code:
- [list of removed dead code files]

Temporary files:
- Removed X __pycache__ directories
- Removed Y compiled files
- Removed Z build artifacts
- [other categories]

TOTAL FILES REMOVED: X
TOTAL SPACE FREED: Y MB

RECOMMENDATIONS:
- [Any further cleanup suggestions]
- [Maintenance tips]


Important Guidelines:

Consolidation means rewriting: Do not just move documentation files - actively merge, deduplicate, and improve content
Never delete without verification: If unsure whether a file is needed, ask for confirmation
Preserve git history: Use git mv for moves when possible
Test after changes: Ensure tests still run after reorganization
Document changes: Keep notes of all significant moves and deletions
Respect project conventions: If the project has established patterns, follow them
Quality over quantity: Better to have 5 well-written, comprehensive docs than 20 scattered fragments

Please proceed with this cleanup systematically, phase by phase, and provide updates as you complete each phase.
