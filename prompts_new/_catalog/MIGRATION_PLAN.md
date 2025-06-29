# Prompt Migration Plan

## Current Structure Analysis

### Existing Categories:
1. **analysis-and-problem-solving/** (6 files)
   - deep-solution-analysis-comprehensive.md
   - deep-solution-analysis.md
   - project-analysis-bug-resolution-howto.md
   - project-analysis-bug-resolution.md
   - vision-gap-analysis-howto.md
   - vision-gap-analysis.md

2. **cleanup-and-organization/** (9 files)
   - documentation/ (4 files)
   - project-wide/ (2 files)
   - testing/ (2 files)
   - README.md

3. **design-and-architecture/** (11 files)
   - Various design, optimization, quality, and integration prompts

4. **development-and-testing/** (8 files)
   - debugging/ (1 file)
   - development/ (2 files)
   - test-development/ (5 files)
   - README.md

5. **meta/** (3 files)
   - Documentation about the prompt system itself

6. **research-based-variants/** (11 files)
   - All optimized/enhanced versions based on research

7. **specialized/** (6 files)
   - Domain-specific prompts

8. **Root level files** (3 files)
   - CATALOG.md
   - MIGRATION_REPORT.md
   - README.md

## Migration Mappings

### Phase 1: Research-based-variants → advanced/optimized/
- chain-of-thought-prompt-research.md → advanced/optimized/chain-of-thought-research.md
- click-cli-cot-enhanced.md → advanced/optimized/click-cli-enhanced.md
- optimized-analysis-cot-prompt.md → advanced/optimized/analysis-cot.md
- optimized-cot-cleaning-prompt.md → advanced/optimized/cleanup-cot.md
- optimized-cot-test-prompt.md → advanced/optimized/test-development-cot.md
- optimized-design-prompt.md → advanced/optimized/design.md
- optimized-doc-consolidation-prompt.md → advanced/optimized/documentation-consolidation.md
- optimized-implementation-prompt.md → advanced/optimized/implementation.md
- optimized-integration-prompt.md → advanced/optimized/integration.md
- optimized-quality-review-prompt.md → advanced/optimized/quality-review.md
- optimized-textual-prompt.md → advanced/optimized/textual-enhancement.md

### Phase 2: Specialized → advanced/specialized/
- TUI-Validation.md → advanced/specialized/tui-validation.md
- claude-cli-prompts.md → advanced/specialized/claude-cli.md
- o3-prompt-fit.md → advanced/specialized/o3-prompt-fit.md
- pagerank-analysis.md → advanced/specialized/pagerank-analysis.md
- prompt-library-organizer.md → advanced/specialized/prompt-library-organizer.md
- templar-prompt-v1.md → advanced/specialized/templar-v1.md

### Phase 3: By Phase Organization

#### 1-planning/
- vision-gap-analysis.md → by-phase/1-planning/vision-gap-analysis.md
- vision-gap-analysis-howto.md → templates/how-to-guides/vision-gap-analysis-guide.md

#### 2-design/
- design-comprehensive.md → by-phase/2-design/system-design/comprehensive-design.md
- design-light.md → by-phase/2-design/system-design/lightweight-design.md
- optimization-template.md → by-phase/2-design/architecture/optimization-template.md
- integration-phase.md → by-phase/2-design/architecture/integration-planning.md

#### 3-implementation/
- implementation-comprehensive.md → by-phase/3-implementation/feature-development/comprehensive-implementation.md
- implementation-light.md → by-phase/3-implementation/feature-development/lightweight-implementation.md
- optimization-integration-comprehensive.md → by-phase/3-implementation/integration/comprehensive-optimization-integration.md
- optimization-integration.md → by-phase/3-implementation/integration/standard-optimization-integration.md
- optimization-integration-comprehensive-code-first-v3.md → by-phase/3-implementation/integration/code-first-optimization-v3.md

#### 4-testing/
- test-development.md → by-phase/4-testing/test-creation/standard-test-development.md
- test-development-comprehensive.md → by-phase/4-testing/test-creation/comprehensive-test-development.md
- test-development-comprehensive-code-first-v3.md → by-phase/4-testing/test-creation/code-first-test-development-v3.md
- quick-test-development.md → by-phase/4-testing/test-creation/quick-test-development.md
- improve-test-pass-rate.md → by-phase/4-testing/test-execution/improve-test-pass-rate.md

#### 5-debugging/
- project-analysis-bug-resolution.md → by-phase/5-debugging/deep-analysis/bug-resolution-analysis.md
- project-analysis-bug-resolution-howto.md → templates/how-to-guides/bug-resolution-guide.md
- deep-solution-analysis.md → by-phase/5-debugging/deep-analysis/solution-analysis.md
- deep-solution-analysis-comprehensive.md → by-phase/5-debugging/deep-analysis/comprehensive-solution-analysis.md
- tree-sitter-correction.md → by-phase/5-debugging/quick-fixes/tree-sitter-correction.md

#### 6-maintenance/
- docs-consolidation.md → by-phase/6-maintenance/documentation/consolidation-standard.md
- docs-consolidation-v3.md → by-phase/6-maintenance/documentation/consolidation-v3.md
- docs-consolidation-template.md → templates/reusable-templates/documentation-consolidation.md
- docs-consolidation-howto.md → templates/how-to-guides/documentation-consolidation-guide.md
- full-project-cleanup-v3.md → by-phase/6-maintenance/refactoring/full-project-cleanup-v3.md
- generic-cleanup-template.md → templates/reusable-templates/generic-cleanup.md
- test-data-cleanup.md → by-phase/6-maintenance/refactoring/test-data-cleanup.md
- test-directory-cleanup.md → by-phase/6-maintenance/refactoring/test-directory-cleanup.md
- quality-comprehensive.md → by-phase/6-maintenance/optimization/quality-review-comprehensive.md
- quality-phase.md → by-phase/6-maintenance/optimization/quality-review-standard.md
- quality-comprehensive-code-first-v3.md → by-phase/6-maintenance/optimization/quality-review-code-first-v3.md

### Phase 4: By Complexity Organization
- Comprehensive versions → by-complexity/comprehensive/
- Light/Quick versions → by-complexity/simple/
- Standard versions → by-complexity/standard/

### Phase 5: Documentation Files → _catalog/
- CATALOG.md → _catalog/CATALOG.md
- README.md → _catalog/README.md
- MIGRATION_REPORT.md → _catalog/MIGRATION_REPORT.md
- cleanup-and-organization/README.md → _catalog/cleanup-organization-readme.md
- development-and-testing/README.md → _catalog/development-testing-readme.md
- meta/*.md → _catalog/meta/

### Phase 6: Archive Old Structure
- Move entire old structure to _archive/legacy-v1/ after migration complete

## Execution Steps

1. Create migration script to automate copying
2. Copy files according to mappings above
3. Verify all files copied correctly
4. Update any internal references/links
5. Create new index/catalog files
6. Archive old structure
7. Generate comprehensive migration report