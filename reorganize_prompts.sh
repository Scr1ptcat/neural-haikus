#!/bin/bash
# Prompt Collection Reorganization Script
# Generated from PROMPT_ORGANIZATION_REPORT.md
# 
# This script will reorganize all prompts according to the new structure.
# Review carefully before executing!

set -e  # Exit on error

echo "=== Prompt Collection Reorganization Script ==="
echo "This script will reorganize your prompt collection."
echo "Please review the changes in PROMPT_ORGANIZATION_REPORT.md first."
echo ""
read -p "Do you want to proceed? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Reorganization cancelled."
    exit 0
fi

echo ""
echo "Creating new directory structure..."

# Create main directories
mkdir -p prompts/{cleanup-and-organization,development-and-testing,design-and-architecture,analysis-and-problem-solving,specialized,meta}

# Create subdirectories
mkdir -p prompts/cleanup-and-organization/{project-wide,documentation,testing}
mkdir -p prompts/development-and-testing/{test-development,debugging}

echo "Moving and renaming files..."

# Cleanup and Organization
echo "  - Processing cleanup and organization prompts..."
mv "Clean Project Chain Of Thought Prompt" "prompts/cleanup-and-organization/project-wide/full-project-cleanup.md" 2>/dev/null || echo "    ! Could not move 'Clean Project Chain Of Thought Prompt'"
mv "Generic Templates/Clean_Generic_Chain_of_Thought_Prompt.txt" "prompts/cleanup-and-organization/project-wide/generic-cleanup-template.md" 2>/dev/null || echo "    ! Could not move generic cleanup template"
mv "Clean_Docs_Chain_Of_Thought_Prompt.txt" "prompts/cleanup-and-organization/documentation/docs-consolidation.md" 2>/dev/null || echo "    ! Could not move docs cleanup"
mv "Generic Templates/Doc_Consolidation" "prompts/cleanup-and-organization/documentation/docs-consolidation-template.md" 2>/dev/null || echo "    ! Could not move doc consolidation"
mv "Generic Templates/Doc_Consolidation_How_To" "prompts/cleanup-and-organization/documentation/docs-consolidation-howto.md" 2>/dev/null || echo "    ! Could not move doc consolidation howto"
mv "Clean_Test_Dir_Chain_Of_Thought_Prompt.txt" "prompts/cleanup-and-organization/testing/test-directory-cleanup.md" 2>/dev/null || echo "    ! Could not move test dir cleanup"
mv "Generic Templates/Clean-Test-Data.txt" "prompts/cleanup-and-organization/testing/test-data-cleanup.md" 2>/dev/null || echo "    ! Could not move test data cleanup"

# Development and Testing
echo "  - Processing development and testing prompts..."
mv "Generic Templates/Test_Development" "prompts/development-and-testing/test-development/comprehensive-test-development.md" 2>/dev/null || echo "    ! Could not move test development"
mv "Test-Development-CoTP.txt" "prompts/development-and-testing/test-development/quick-test-development.md" 2>/dev/null || echo "    ! Could not move quick test development"
mv "Improve_Test_Pass_Rate_CoTP.txt" "prompts/development-and-testing/test-development/improve-test-pass-rate.md" 2>/dev/null || echo "    ! Could not move test pass rate"
mv "Tree Sitter Correction Prompt" "prompts/development-and-testing/debugging/tree-sitter-correction.md" 2>/dev/null || echo "    ! Could not move tree sitter"

# Design and Architecture
echo "  - Processing design and architecture prompts..."
if [ -f "DESIGN PHASE" ]; then
    echo "    - Removing duplicate DESIGN PHASE file..."
    rm "DESIGN PHASE"
fi
mv "Generic Templates/DESIGN_PHASE_PROMPT_TEMPLATE.txt" "prompts/design-and-architecture/design-phase-template.md" 2>/dev/null || echo "    ! Could not move design phase template"
mv "INTEGRATE PHASE" "prompts/design-and-architecture/integration-phase.md" 2>/dev/null || echo "    ! Could not move integrate phase"
mv "QUAlITY PHASE" "prompts/design-and-architecture/quality-phase.md" 2>/dev/null || echo "    ! Could not move quality phase"
mv "OPTIMIZATION_PROMPT_TEMPLATE.txt" "prompts/design-and-architecture/optimization-template.md" 2>/dev/null || echo "    ! Could not move optimization template"

# Analysis and Problem Solving
echo "  - Processing analysis and problem-solving prompts..."
mv "Generic Templates/Generic_COTP_Project_Analysis_Bug_Resolution.txt" "prompts/analysis-and-problem-solving/project-analysis-bug-resolution.md" 2>/dev/null || echo "    ! Could not move project analysis"
mv "Generic Templates/How_To_Use_Project_Analysis_Bug_Resolution.txt" "prompts/analysis-and-problem-solving/project-analysis-bug-resolution-howto.md" 2>/dev/null || echo "    ! Could not move project analysis howto"
mv "Generic Templates/Deep_Solution_Analysis.txt" "prompts/analysis-and-problem-solving/deep-solution-analysis.md" 2>/dev/null || echo "    ! Could not move deep solution analysis"
mv "Generic Templates/Vision_Gap_Analysis.txt" "prompts/analysis-and-problem-solving/vision-gap-analysis.md" 2>/dev/null || echo "    ! Could not move vision gap analysis"
mv "Generic Templates/Vision_Gap_Analysis_How_To" "prompts/analysis-and-problem-solving/vision-gap-analysis-howto.md" 2>/dev/null || echo "    ! Could not move vision gap howto"

# Specialized
echo "  - Processing specialized prompts..."
mv "PageRank_Prompt" "prompts/specialized/pagerank-analysis.md" 2>/dev/null || echo "    ! Could not move pagerank"
mv "Claude CLI Prompts" "prompts/specialized/claude-cli-prompts.md" 2>/dev/null || echo "    ! Could not move claude cli"
mv "templar_prompt_v1" "prompts/specialized/templar-prompt-v1.md" 2>/dev/null || echo "    ! Could not move templar"
mv "Generic Templates/Generic_o3_prompt_fit" "prompts/specialized/o3-prompt-fit.md" 2>/dev/null || echo "    ! Could not move o3 prompt"

# Meta
echo "  - Processing meta prompts..."
mv "Chain Of Thought Prompt Library" "prompts/meta/prompt-library-index.md" 2>/dev/null || echo "    ! Could not move prompt library"
mv "COTP-Development-Explanation.txt" "prompts/meta/cotp-development-guide.md" 2>/dev/null || echo "    ! Could not move COTP explanation"
mv "Quality Chain Of Thought Prompt" "prompts/meta/quality-engineering-approach.md" 2>/dev/null || echo "    ! Could not move quality engineering"

# Clean up empty Generic Templates directory
echo ""
echo "Cleaning up..."
if [ -d "Generic Templates" ] && [ -z "$(ls -A 'Generic Templates')" ]; then
    echo "  - Removing empty Generic Templates directory..."
    rmdir "Generic Templates"
fi

echo ""
echo "=== Reorganization Complete ==="
echo ""
echo "Next steps:"
echo "1. Review the new structure in the prompts/ directory"
echo "2. Check for any files that couldn't be moved (marked with !)"
echo "3. Review PROMPT_ORGANIZATION_REPORT.md for full details"
echo "4. Consider creating README files for each category"
echo ""
echo "To undo these changes, you'll need to manually move files back or restore from version control."