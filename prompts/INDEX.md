# Neural Haikus Prompt Library Index

## Directory Structure

### Quick Start (`/quick-start/`)
Top 5 most commonly used prompts for rapid access:
- `debug-issue.md` - Deep solution analysis for debugging
- `design-system.md` - Lightweight system design
- `implement-feature.md` - Lightweight feature implementation
- `write-tests.md` - Quick test development
- `consolidate-docs.md` - Documentation consolidation

### By Phase (`/by-phase/`)
Prompts organized by development lifecycle phase:

#### 1. Planning
- Vision gap analysis and project planning prompts

#### 2. Design
- **System Design**: Comprehensive and lightweight design approaches
- **Architecture**: Integration planning and optimization templates

#### 3. Implementation
- **Feature Development**: Comprehensive and lightweight implementation
- **Integration**: Code-first optimization and integration strategies

#### 4. Testing
- **Test Creation**: Various test development approaches (quick, standard, comprehensive)
- **Test Execution**: Improving test pass rates
- **Test Planning**: Strategic test planning prompts

#### 5. Debugging
- **Deep Analysis**: Bug resolution and solution analysis
- **Quick Fixes**: Targeted fixes like tree-sitter corrections

#### 6. Maintenance
- **Documentation**: Consolidation strategies
- **Optimization**: Quality reviews and code optimization
- **Refactoring**: Project cleanup and test refactoring

### By Complexity (`/by-complexity/`)
Same prompts organized by complexity level:
- **Simple**: Quick, lightweight approaches
- **Standard**: Balanced complexity for typical tasks
- **Comprehensive**: Thorough, detailed approaches

### Advanced (`/advanced/`)
- **Optimized**: Research-based Chain of Thought optimized prompts
- **Specialized**: Domain-specific prompts (Claude CLI, TUI validation, etc.)
- **Experimental**: Cutting-edge prompt techniques

### Templates (`/templates/`)
- **How-to Guides**: Step-by-step instructions for common tasks
- **Reusable Templates**: Generic templates for customization
- **Prompt Engineering**: Meta-prompts for creating new prompts

### Catalog (`/_catalog/`)
Documentation and meta-information:
- Migration reports and plans
- README files from original categories
- Meta documentation on CoT development
- Search index and reorganization maps

### Archive (`/_archive/`)
Legacy prompts preserved for reference

## Usage Guidelines

1. **Start with Quick Start**: For common tasks, check `/quick-start/` first
2. **Choose by Phase**: If you know what development phase you're in, browse `/by-phase/`
3. **Select Complexity**: Pick simple/standard/comprehensive based on your needs
4. **Explore Advanced**: For optimized or specialized use cases
5. **Customize Templates**: Use `/templates/` as starting points for custom prompts

## Key Features

- **Chain of Thought (CoT)** methodology throughout
- **Placeholder variables** for easy customization
- **Multi-phase approaches** with built-in verification
- **Quality checks** and anti-pattern detection
- **Documentation requirements** built into prompts

## Integration with Orchestrator

These prompts are designed to work with the neural-haikus orchestrator:
```bash
python orchestrator.py plan "feature description"
```

The orchestrator can extract and use these templates automatically in its workflow phases.