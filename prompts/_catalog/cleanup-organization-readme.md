# Cleanup and Organization Prompts

This category contains prompts for cleaning, organizing, and refactoring codebases. These prompts emphasize systematic approaches to technical debt reduction and code organization.

## 📁 Subcategories

### Project-Wide
Comprehensive cleanup prompts that address entire codebases.

- **full-project-cleanup.md** - Complete project overhaul including tests, documentation, and dead code removal
- **generic-cleanup-template.md** - Customizable template for any cleanup task (18KB - most comprehensive)

### Documentation
Focused on organizing and consolidating documentation.

- **docs-consolidation.md** - Consolidate scattered documentation into organized structure
- **docs-consolidation-template.md** - Generic template for documentation cleanup
- **docs-consolidation-howto.md** - Step-by-step guide for using documentation prompts

### Testing
Specialized prompts for test organization and cleanup.

- **test-directory-cleanup.md** - Organize chaotic test directories into logical structure
- **test-data-cleanup.md** - Clean and organize test data, fixtures, and mocks

## 🎯 When to Use These Prompts

Use cleanup prompts when:
- Starting work on a legacy codebase
- Preparing for a major refactor
- Standardizing project structure
- Reducing technical debt
- Onboarding new team members
- Before adding new features to messy code

## 🔑 Key Principles

All cleanup prompts follow these principles:
1. **Understand before changing** - Map the current state thoroughly
2. **Preserve functionality** - Never break working code
3. **Incremental progress** - Make reversible changes
4. **Document decisions** - Explain why changes were made
5. **Test continuously** - Verify nothing breaks

## 💡 Tips for Effective Use

1. **Start with project-wide analysis** before diving into specifics
2. **Run tests frequently** during cleanup
3. **Commit often** with clear messages
4. **Use version control** to track progress
5. **Consider team conventions** before standardizing

## 📊 Prompt Comparison

| Prompt | Scope | Complexity | Time Estimate |
|--------|-------|------------|---------------|
| full-project-cleanup | Entire codebase | High | Days-Weeks |
| generic-cleanup-template | Customizable | Variable | Hours-Days |
| docs-consolidation | Documentation only | Medium | Hours |
| test-directory-cleanup | Test files only | Medium | Hours |
| test-data-cleanup | Test data/fixtures | Low-Medium | Hours |

## 🔄 Recommended Workflow

1. Start with `generic-cleanup-template.md` to assess the situation
2. Use `full-project-cleanup.md` for comprehensive overhaul
3. Apply specialized prompts for focused areas:
   - `docs-consolidation.md` for documentation
   - `test-directory-cleanup.md` for test organization
4. Iterate until codebase meets standards

## ⚡ Quick Wins

For immediate impact, prioritize:
1. Removing dead code
2. Consolidating duplicate files
3. Standardizing naming conventions
4. Organizing imports
5. Cleaning up test data

These prompts are designed to transform chaotic codebases into well-organized, maintainable projects.