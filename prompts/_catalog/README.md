# Neural-Haikus Prompt Library

> A comprehensive collection of Chain of Thought (CoT) prompts for AI-assisted software development

## 🚀 Quick Start

This library contains 62 carefully crafted prompts organized by domain and purpose. Each prompt follows Chain of Thought methodology to ensure thorough analysis before implementation.

### Finding the Right Prompt

1. **Browse by task type** in the folders below
2. **Check the [CATALOG.md](./CATALOG.md)** for detailed descriptions
3. **Use variants**:
   - `-comprehensive` for production/complex tasks
   - `-light` for prototypes/simple tasks  
   - `optimized-` for research-enhanced versions

### Top 5 Most Used Prompts

1. 🔍 [Deep Solution Analysis](./analysis-and-problem-solving/deep-solution-analysis-comprehensive.md) - For complex debugging
2. 🏗️ [Design Comprehensive](./design-and-architecture/design-comprehensive.md) - For system design
3. 💻 [Implementation Comprehensive](./development-and-testing/development/implementation-comprehensive.md) - For feature development
4. 🧪 [Test Development](./development-and-testing/test-development/test-development.md) - For test creation
5. 📚 [Docs Consolidation](./cleanup-and-organization/documentation/docs-consolidation-v3.md) - For documentation

## 📁 Library Structure

```
prompts/
├── 📊 analysis-and-problem-solving/ (6 prompts)
│   └── Deep analysis, debugging, gap identification
├── 🧹 cleanup-and-organization/ (9 prompts)
│   ├── documentation/ - Documentation consolidation
│   ├── project-wide/ - Codebase cleanup
│   └── testing/ - Test organization
├── 🏛️ design-and-architecture/ (11 prompts)
│   └── System design, optimization, quality
├── 💻 development-and-testing/ (9 prompts)
│   ├── debugging/ - Debug strategies
│   ├── development/ - Implementation
│   └── test-development/ - Test creation
├── 🔬 research-based-variants/ (11 prompts)
│   └── Optimized versions using latest research
├── 🛠️ specialized/ (6 prompts)
│   └── Tool-specific (Claude CLI, TUI, etc.)
└── 📖 meta/ (3 prompts)
    └── Guides for creating prompts
```

## 🎯 How to Use These Prompts

### 1. With the Orchestrator
```bash
# Use a prompt as a template in the orchestrator workflow
python orchestrator.py plan "implement feature X using comprehensive design prompt"
```

### 2. Direct Copy-Paste
1. Open the prompt file
2. Replace placeholder variables:
   - `[PROJECT_NAME]` → Your project name
   - `[YEARS]` → Your experience level
   - `[DOMAIN_EXPERTISE]` → Your domain
3. Copy to your AI assistant (Claude, GPT-4, etc.)

### 3. As Templates
Many prompts include template versions with clear placeholders for customization.

## 🔍 Choosing the Right Variant

### Comprehensive vs Light
- **Comprehensive**: Full analysis, production code, complex features
- **Light**: Quick prototypes, simple features, time-constrained

### Original vs Optimized  
- **Original**: Battle-tested, maximum compatibility
- **Optimized**: Research-enhanced, better structure, clearer outputs

### Versioning (v2, v3)
- **Latest (v3)**: Most recent improvements
- **Previous versions**: For compatibility with existing workflows

## 📊 Prompt Categories Explained

### Analysis & Problem-Solving
Deep-dive investigation prompts for debugging, performance issues, and gap analysis. These prompts emphasize evidence gathering and root cause analysis.

### Cleanup & Organization  
Systematic approaches to refactoring, documentation consolidation, and test suite organization. Focus on maintaining functionality while improving structure.

### Design & Architecture
Comprehensive design prompts covering requirements analysis, system architecture, and quality reviews. Includes both upfront design and iterative improvement.

### Development & Testing
Implementation-focused prompts for feature development, debugging, and test creation. Emphasizes code quality and comprehensive testing.

### Research-Based Variants
Prompts optimized using prompt engineering research. These versions often have better structure, clearer instructions, and more predictable outputs.

### Specialized
Tool-specific prompts for technologies like Claude CLI, Python Textual TUI, and algorithm implementations.

### Meta
Guides and templates for creating your own high-quality prompts. Learn the principles behind effective Chain of Thought prompting.

## 🏷️ Prompt Selection Matrix

| Task Type | Time Available | Complexity | Recommended Prompt |
|-----------|---------------|------------|-------------------|
| Bug Fix | Limited | Simple | `targeted-solution.md` |
| Bug Fix | Adequate | Complex | `deep-solution-analysis-comprehensive.md` |
| New Feature | Limited | Simple | `implementation-light.md` |
| New Feature | Adequate | Complex | `design-comprehensive.md` + `implementation-comprehensive.md` |
| Refactoring | Any | Any | `project-cleanup-comprehensive.md` |
| Testing | Limited | Simple | `test-development.md` |
| Testing | Adequate | Complex | `test-implementation-code-first-v3.md` |

## 📈 Library Statistics

- **Total Prompts**: 62 (after removing 2 duplicates)
- **Average Token Usage**: 1,500-3,000 per prompt
- **Success Rate**: Highest with comprehensive variants
- **Most Optimized Category**: Research-based variants

## 🔧 Maintenance

### Recent Changes
- Removed 2 exact duplicates (see [MIGRATION_REPORT.md](./MIGRATION_REPORT.md))
- Added comprehensive catalog with metadata
- Enhanced documentation and navigation

### Contributing
When adding new prompts:
1. Place in the appropriate category folder
2. Use clear, descriptive filenames
3. Include purpose and use cases in the prompt
4. Update CATALOG.md with the new entry
5. Follow existing naming conventions

### Quality Standards
Each prompt should include:
- Clear purpose statement
- Placeholder variables for customization  
- Phase-based structure (understanding → implementation → validation)
- Expected outputs
- Success criteria

## 🔗 Quick Links

- 📚 **[Full Catalog](./CATALOG.md)** - Detailed index with descriptions
- 📋 **[Migration Report](./MIGRATION_REPORT.md)** - Recent reorganization details
- 🏠 **[Main Project README](../README.md)** - Neural-haikus overview
- 📖 **[CLAUDE.md](../CLAUDE.md)** - Project documentation for Claude Code

## 💡 Pro Tips

1. **Start with comprehensive versions** for important features
2. **Use optimized variants** with modern LLMs (GPT-4, Claude)
3. **Chain prompts together** - Design → Implementation → Testing
4. **Check the meta folder** to learn prompt engineering
5. **Save successful outputs** as new orchestrator templates

---

*This prompt library is part of the neural-haikus project - structuring AI-assisted development through Chain of Thought methodologies.*