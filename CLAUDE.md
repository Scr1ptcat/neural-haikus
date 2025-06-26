# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Neural-haikus is a prompt engineering framework and orchestration system designed to structure AI-assisted development workflows through Chain of Thought (CoT) prompting methodologies. It provides reusable templates and an automated workflow system for feature planning and implementation.

## Key Commands

### Orchestrator Commands
```bash
# Basic workflow commands
python orchestrator.py plan "feature description"              # Start planning a new feature
python orchestrator.py analyze --session-file <path>          # Run analysis phase
python orchestrator.py implement --session-file <path>        # Execute implementation

# Batch processing
python orchestrator.py batch --file features.txt              # Process multiple features

# Session management
python orchestrator.py list                                   # List all sessions
python orchestrator.py status --session-file <path>           # Check session progress

# Flags
--save-to-file                                               # Save prompts to files instead of terminal
--verbose                                                    # Enable verbose logging
```

## Architecture Overview

### Orchestrator Workflow (6 phases)
1. **Plan** - Generate orchestrator prompts from feature descriptions
2. **Process Orchestrator** - Extract and save templates from LLM output
3. **Analyze** - Perform deep codebase analysis using templates
4. **Process Analysis** - Save analysis results to outputs directory
5. **Implement** - Execute implementation based on analysis
6. **Complete** - Finalize session with documentation

### Directory Structure
```
neural-haikus/
├── orchestrator.py              # Main orchestration engine
├── orchestrator_workspace/      
│   ├── outputs/                # Generated analysis and implementation files
│   ├── sessions/               # JSON session state files
│   └── templates/              # Extracted templates from sessions
├── Generic Templates/          # Reusable Chain of Thought prompt templates
│   ├── DESIGN_PHASE_PROMPT_TEMPLATE.txt
│   ├── Generic_COTP_Project_Analysis_Bug_Resolution.txt
│   └── [Various specialized templates]
└── [Phase-specific templates and documentation]
```

### Session Management
- Sessions tracked with unique IDs: `{timestamp}_{sanitized_feature_name}`
- Session states: planned → templates_ready → analyzing → analysis_complete → implementing → complete
- Session data stored as JSON in `orchestrator_workspace/sessions/`
- Outputs saved to `orchestrator_workspace/outputs/{session_id}/`

### Template System
Templates use Chain of Thought methodology with:
- Placeholder variables: `[YEARS]`, `[DOMAIN_EXPERTISE]`, `[PROJECT_NAME]`, etc.
- Multi-phase approaches (understanding → analysis → implementation → validation)
- Built-in quality checks and anti-patterns
- Documentation requirements

## Development Guidelines

### Working with Templates
1. Always replace placeholder variables when using templates
2. Follow the established Chain of Thought patterns
3. Templates emphasize understanding before implementation
4. Each template includes verification steps - complete them all

### Orchestrator Best Practices
1. Start new features with `plan` command
2. Save important prompts with `--save-to-file` flag
3. Review generated templates before proceeding to analysis
4. Complete each phase before moving to the next
5. Session files preserve state - you can resume interrupted workflows

### Key Principles (from templates)
- **Deep Understanding First**: Analyze thoroughly before implementing
- **Follow Existing Patterns**: Identify and adhere to codebase conventions
- **Comprehensive Testing**: Every implementation must include tests
- **Proper Documentation**: Document decisions and implementation details
- **No Shortcuts**: Fix root causes, not symptoms

## Current Features and Roadmap

### Active Features
- Multi-phase orchestration workflow
- Session state management
- Template extraction and storage
- Batch processing capabilities

### Planned Enhancements (from features.txt)
- Database integration for session/template storage
- Template versioning and customization
- A/B testing for prompt effectiveness
- Integration with prompt-runner tool
- Browser extension for easier copying
- Analytics and metrics tracking

## Important Notes

1. **No External Dependencies**: The orchestrator.py runs with standard Python - no requirements.txt needed
2. **Template-Driven**: All workflows are driven by the prompt templates - customize them for your needs
3. **Session Persistence**: Sessions are saved automatically - you can always resume where you left off
4. **Manual Integration**: Currently requires manual copying of prompts to LLM interfaces (automation planned)

## Common Workflows

### Adding a New Feature
1. Create feature description in features.txt or pass directly to plan command
2. Run: `python orchestrator.py plan "feature description" --save-to-file`
3. Review generated orchestrator prompt
4. Copy prompt to LLM, get response, save as template
5. Run: `python orchestrator.py analyze --session-file <path>`
6. Review analysis output
7. Run: `python orchestrator.py implement --session-file <path>`

### Using Generic Templates
1. Browse `Generic Templates/` for relevant template
2. Copy template content
3. Replace all placeholder variables
4. Follow the template's phase structure
5. Complete all verification steps

### Debugging Sessions
- Check session status: `python orchestrator.py status --session-file <path>`
- Review session JSON in `orchestrator_workspace/sessions/`
- Check outputs in `orchestrator_workspace/outputs/{session_id}/`
- Use `--verbose` flag for detailed logging