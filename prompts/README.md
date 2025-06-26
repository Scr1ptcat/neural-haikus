# Neural Haikus Prompt Library

A comprehensive collection of Chain of Thought (CoT) prompts for software development, organized by purpose and use case. These prompts follow a systematic, phase-based approach to ensure thorough analysis and high-quality implementation.

## 📁 Directory Structure

```
prompts/
├── cleanup-and-organization/      # Prompts for cleaning and organizing codebases
├── development-and-testing/       # Test creation and debugging prompts
├── design-and-architecture/       # System design and architecture prompts
├── analysis-and-problem-solving/  # Analysis and debugging prompts
├── specialized/                   # Domain-specific prompts
└── meta/                         # Guides and meta-documentation
```

## 🎯 Quick Start Guide

### Finding the Right Prompt

1. **Starting a new project?** → Check `design-and-architecture/`
2. **Cleaning up existing code?** → Browse `cleanup-and-organization/`
3. **Writing or fixing tests?** → Look in `development-and-testing/`
4. **Debugging issues?** → See `analysis-and-problem-solving/`
5. **Need guidance?** → Start with `meta/prompt-library-index.md`

## 📚 Prompt Categories

### 🧹 Cleanup and Organization

Prompts for cleaning, organizing, and refactoring codebases.

#### Project-Wide
- **[full-project-cleanup.md](cleanup-and-organization/project-wide/full-project-cleanup.md)** - Complete project cleanup including tests, docs, and dead code
- **[generic-cleanup-template.md](cleanup-and-organization/project-wide/generic-cleanup-template.md)** - Customizable template for any cleanup task

#### Documentation
- **[docs-consolidation.md](cleanup-and-organization/documentation/docs-consolidation.md)** - Consolidate scattered documentation
- **[docs-consolidation-template.md](cleanup-and-organization/documentation/docs-consolidation-template.md)** - Template version for custom doc cleanup
- **[docs-consolidation-howto.md](cleanup-and-organization/documentation/docs-consolidation-howto.md)** - Guide for using doc consolidation prompts

#### Testing
- **[test-directory-cleanup.md](cleanup-and-organization/testing/test-directory-cleanup.md)** - Organize and clean test directories
- **[test-data-cleanup.md](cleanup-and-organization/testing/test-data-cleanup.md)** - Clean and organize test data files

### 🛠️ Development and Testing

Prompts for test development and debugging tasks.

#### Test Development
- **[comprehensive-test-development.md](development-and-testing/test-development/comprehensive-test-development.md)** - Full test suite development (22KB)
- **[quick-test-development.md](development-and-testing/test-development/quick-test-development.md)** - Rapid test creation (8KB)
- **[improve-test-pass-rate.md](development-and-testing/test-development/improve-test-pass-rate.md)** - Fix failing tests systematically

#### Debugging
- **[tree-sitter-correction.md](development-and-testing/debugging/tree-sitter-correction.md)** - Debug tree-sitter implementations

### 🏗️ Design and Architecture

Prompts for system design and architectural decisions.

- **[design-phase-template.md](design-and-architecture/design-phase-template.md)** - Comprehensive design phase approach
- **[integration-phase.md](design-and-architecture/integration-phase.md)** - Code integration best practices
- **[quality-phase.md](design-and-architecture/quality-phase.md)** - Quality assurance phase
- **[optimization-template.md](design-and-architecture/optimization-template.md)** - Performance optimization

### 🔍 Analysis and Problem Solving

Prompts for analyzing code and solving complex problems.

- **[project-analysis-bug-resolution.md](analysis-and-problem-solving/project-analysis-bug-resolution.md)** - Systematic bug analysis and resolution
- **[project-analysis-bug-resolution-howto.md](analysis-and-problem-solving/project-analysis-bug-resolution-howto.md)** - Guide for bug resolution prompt
- **[deep-solution-analysis.md](analysis-and-problem-solving/deep-solution-analysis.md)** - Deep technical analysis
- **[vision-gap-analysis.md](analysis-and-problem-solving/vision-gap-analysis.md)** - Analyze gaps between vision and implementation
- **[vision-gap-analysis-howto.md](analysis-and-problem-solving/vision-gap-analysis-howto.md)** - Guide for vision gap analysis

### 🎯 Specialized

Domain-specific and experimental prompts.

- **[pagerank-analysis.md](specialized/pagerank-analysis.md)** - PageRank algorithm implementation (30KB)
- **[claude-cli-prompts.md](specialized/claude-cli-prompts.md)** - Claude CLI specific prompts
- **[templar-prompt-v1.md](specialized/templar-prompt-v1.md)** - Templar system prompt
- **[o3-prompt-fit.md](specialized/o3-prompt-fit.md)** - O3 model optimization prompt

### 📖 Meta

Documentation and guides about the prompt system itself.

- **[prompt-library-index.md](meta/prompt-library-index.md)** - Master index of all prompts
- **[cotp-development-guide.md](meta/cotp-development-guide.md)** - How to develop Chain of Thought prompts
- **[quality-engineering-approach.md](meta/quality-engineering-approach.md)** - Quality engineering methodology

## 🚀 Usage Guidelines

### Basic Usage

1. **Choose the appropriate prompt** based on your task
2. **Copy the prompt content** to your LLM interface
3. **Replace placeholder variables** (marked with `[BRACKETS]`)
4. **Follow the phases** as outlined in the prompt
5. **Complete verification steps** before considering the task done

### Common Placeholders

- `[YEARS]` - Years of experience for the role
- `[DOMAIN_EXPERTISE]` - Specific domain knowledge
- `[PROJECT_NAME]` - Your project name
- `[SPECIFIC_TASK]` - The task to accomplish
- `[CODEBASE_PATH]` - Path to your codebase

### Best Practices

1. **Read the entire prompt first** - Understand all phases before starting
2. **Don't skip phases** - Each phase builds on the previous
3. **Verify at each step** - Use the built-in verification checkpoints
4. **Customize thoughtfully** - Adapt prompts to your specific needs
5. **Document changes** - Note any modifications you make

## 🔧 Prompt Characteristics

### Chain of Thought (CoT) Methodology

All prompts follow a systematic approach:
1. **Understanding Phase** - Deep analysis before action
2. **Planning Phase** - Strategic approach development
3. **Implementation Phase** - Systematic execution
4. **Verification Phase** - Quality checks and validation
5. **Documentation Phase** - Record decisions and learnings

### Quality Principles

- **Fix-first mentality** - Address root causes, not symptoms
- **Pattern recognition** - Follow existing codebase patterns
- **Comprehensive testing** - Every change includes tests
- **Clear documentation** - Explain the why, not just the what
- **No shortcuts** - Do it right the first time

## 📝 Contributing New Prompts

When adding new prompts:

1. **Follow the naming convention**: `[purpose]-[function]-[variant].md`
2. **Place in appropriate category** or create new one if needed
3. **Include clear role definition** at the start
4. **Use phase-based structure** for complex tasks
5. **Add verification steps** throughout
6. **Update this README** with the new prompt

## 🔄 Maintenance

- **Regular Reviews**: Audit prompts quarterly for relevance
- **Version Control**: Track significant changes in git
- **Duplicate Check**: Verify no functional duplicates exist
- **Effectiveness Tracking**: Note which prompts work best

## 📊 Prompt Statistics

- **Total Prompts**: 27
- **Categories**: 6 main categories
- **Largest Prompt**: pagerank-analysis.md (30KB)
- **Most Comprehensive**: comprehensive-test-development.md
- **Quick Solutions**: 5 "quick" or "template" variants

## 🎓 Learning Path

New to Chain of Thought prompts? Start here:

1. Read `meta/cotp-development-guide.md`
2. Review `meta/prompt-library-index.md`
3. Try `cleanup-and-organization/project-wide/generic-cleanup-template.md`
4. Study phase structure in `design-and-architecture/design-phase-template.md`
5. Practice with `analysis-and-problem-solving/project-analysis-bug-resolution.md`

---

*This prompt library is part of the Neural Haikus project - a sophisticated orchestration system for AI-assisted development workflows.*