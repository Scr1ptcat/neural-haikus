#!/usr/bin/env python3
"""
Template Orchestrator - Automated Feature Planning System

This script manages the workflow of:
1. Taking a feature request
2. Generating filled analysis/implementation templates
3. Executing those templates to implement features

Usage:
    python orchestrator.py plan "add user authentication"
    python orchestrator.py analyze --session-file sessions/auth_20240115_103000.json
    python orchestrator.py implement --session-file sessions/auth_20240115_103000.json
"""

import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
import subprocess
import textwrap
from typing import Dict, Any, Optional, List
import re

# Version
__version__ = "1.2.0"

# Optional color support
try:
    # ANSI color codes for better terminal output
    class Colors:
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        END = '\033[0m'
    
    # Disable colors if not in a terminal
    if not sys.stdout.isatty():
        Colors.BLUE = Colors.GREEN = Colors.YELLOW = Colors.RED = Colors.BOLD = Colors.END = ''
except:
    # Fallback if terminal doesn't support colors
    class Colors:
        BLUE = GREEN = YELLOW = RED = BOLD = END = ''

class TemplateOrchestrator:
    def __init__(self, base_dir: str = "orchestrator_workspace"):
        """Initialize the orchestrator with workspace directory."""
        self.base_dir = Path(base_dir)
        self.sessions_dir = self.base_dir / "sessions"
        self.outputs_dir = self.base_dir / "outputs"
        self.templates_dir = self.base_dir / "templates"
        
        # Create directories
        for dir_path in [self.sessions_dir, self.outputs_dir, self.templates_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
            
        # Detect Python executable
        self.python_cmd = self._detect_python()
            
        # Store templates
        self._store_templates()
    
    def _detect_python(self) -> str:
        """Detect the appropriate Python command for this system."""
        # Try python3 first, then python
        for cmd in ['python3', 'python']:
            try:
                result = subprocess.run([cmd, '--version'], 
                                     capture_output=True, 
                                     text=True, 
                                     timeout=5)
                if result.returncode == 0:
                    return cmd
            except (subprocess.SubprocessError, FileNotFoundError):
                continue
        
        # Default to python3 if nothing works
        return 'python3'
    
    def _store_templates(self):
        """Store the template content for use in prompts."""
        
        # Orchestrator Prompt - Fixed format string issues
        self.orchestrator_prompt = """# Role: Senior Technical Architect & Project Planner

You are a senior technical architect with 20+ years of experience in software development, system design, and project planning. You excel at:
- Rapidly understanding codebases and their patterns
- Breaking down vague requirements into concrete technical specifications  
- Creating detailed implementation plans that junior developers can follow
- Anticipating integration challenges and edge cases
- Estimating effort accurately based on project complexity

## Your Current Task

You've been asked to prepare comprehensive work sessions for implementing a new feature. You need to:
1. Quickly analyze the current project to understand its architecture
2. Interpret the feature request into detailed technical requirements
3. Create filled templates that another developer (or AI) can execute without additional context

## Project Analysis Phase

Take 30-60 seconds to scan the project:

```bash
# Quick discovery commands to understand the project
find . -name "package.json" -o -name "requirements.txt" -o -name "go.mod" -o -name "Gemfile" | head -5
find . -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.go" | grep -E "(main|app|index|server)" | head -10
ls -la
tree -d -L 2 -I 'node_modules|__pycache__|.git'
# Use {python_cmd} for Python files
find . -name "*.py" -exec grep -l "class\\|def\\|@app" {{}} \\; | head -10
```

## Feature Request: {feature_request}

## Required Output

You must provide THREE comprehensive sections. Please format them EXACTLY as shown:

### 1. ANALYSIS_TEMPLATE

```
# Role: Senior Software Analyst

You are a senior software analyst with expertise in code archaeology and pattern recognition. Your mission is to perform a deep analysis of this codebase to understand every aspect that will impact the implementation of: {feature_request}

## Analysis Objectives
1. Map the complete architecture and understand design decisions
2. Identify all patterns, conventions, and standards
3. Locate integration points for the new feature
4. Understand the testing philosophy and approach
5. Document everything needed for successful implementation

## Phase 1: Project Structure Deep Dive
[Specific areas to investigate based on the feature]
- Directory organization and what belongs where
- File naming conventions and patterns
- Module organization and dependencies
- Build and deployment structure

## Phase 2: Architecture Analysis
[What architectural aspects to focus on]
- Design patterns in use (MVC, microservices, etc.)
- State management approach
- Data flow patterns
- External service integrations
- Middleware/plugin architecture

## Phase 3: Code Standards Discovery
[Specific patterns to document]
- Naming conventions for files, functions, variables, classes
- Code organization within files
- Import/export patterns
- Error handling approaches
- Logging standards
- Comment and documentation style

## Phase 4: Feature-Specific Investigation
[Targeted analysis for this feature]
- Similar existing features to use as reference
- Specific integration points needed
- Data models that will be affected
- API endpoints or interfaces to modify/create
- Security considerations

## Phase 5: Testing Infrastructure
[Testing approach analysis]
- Test file organization
- Testing frameworks and patterns
- Mock/stub approaches
- Test data management
- Coverage expectations

## Expected Deliverable
A comprehensive analysis document that allows someone to implement {feature_request} without needing to ask any questions about the codebase.
```

### 2. IMPLEMENTATION_TEMPLATE

```
# Role: Senior Software Engineer

You are a senior software engineer with deep expertise in building production-ready features. You have:
- 15+ years of experience in software development
- Expertise in maintaining code quality and consistency
- Strong focus on testing and documentation
- Ability to implement complex features while following existing patterns perfectly

## Your Mission
Implement the feature: {feature_request}

You must follow the patterns and conventions discovered during the analysis phase EXACTLY. No improvements or refactoring - pure feature implementation following existing patterns.

## Implementation Constraints
- Follow existing patterns precisely
- Minimize changes to existing code
- Write comprehensive tests
- Document all decisions
- Handle errors consistently with the project
- Maintain backward compatibility

## Phase 1: Pre-Implementation Setup
- Review analysis findings
- Set up development environment
- Verify all dependencies
- Create feature branch (if using git)

## Phase 2: Implementation Planning
[Detailed breakdown based on feature requirements]
- Component breakdown with rationale
- File creation/modification list
- Integration points and approach
- Data model changes (if any)
- API changes (if any)

## Phase 3: Core Implementation
[Step-by-step implementation guide]
1. Data Layer (if applicable)
   - Schema changes
   - Migrations
   - Model updates
   
2. Business Logic
   - Core feature logic
   - Validation rules
   - Business constraints
   - Error handling
   
3. Interface Layer
   - API endpoints
   - UI components
   - CLI commands
   - External interfaces

4. Integration
   - Connect all components
   - Update existing flows
   - Maintain compatibility

## Phase 4: Testing Implementation
[Comprehensive testing requirements]
- Unit tests for all new functions/methods
- Integration tests for component interactions
- End-to-end tests for user flows
- Edge case testing
- Error scenario testing
- Performance testing (if applicable)

## Phase 5: Documentation and Polish
- Code documentation (inline comments, docstrings)
- API documentation updates
- User documentation (if applicable)
- Configuration documentation
- Migration guide (if breaking changes)

## Expected Deliverable
Complete, working implementation of {feature_request} that:
- Follows all existing patterns
- Includes comprehensive tests
- Is properly documented
- Handles all edge cases
- Integrates seamlessly with existing code
```

### 3. EXECUTION_NOTES

```
Feature: {feature_request}
Complexity: [Low/Medium/High based on analysis]
Estimated Time: [X-Y hours broken down by phase]
  - Analysis: [X hours]
  - Implementation: [Y hours]
  - Testing: [Z hours]
  - Documentation: [W hours]

Key Risks:
[Identified risks with mitigation strategies]

Key Files to Focus On:
[List of critical files for this feature]

Similar Existing Features:
[Reference implementations to follow]

Integration Points:
[Where this feature touches existing code]

Testing Strategy:
[Specific testing approach for this feature]

Performance Considerations:
[Any performance impacts to consider]

Security Considerations:
[Security aspects to address]

Rollback Plan:
[How to rollback if issues arise]
```

## Important Notes

1. Be extremely specific in your templates - someone should be able to execute them without any project knowledge
2. Include actual file paths, function names, and patterns you observe
3. Don't make assumptions - base everything on what you can see in the project
4. If something is unclear, make a reasonable inference and document it
5. Always err on the side of being too detailed rather than too vague

Remember: The goal is to reduce the implementation time from hours of exploration to minutes of execution."""
    
    def _print_colored(self, message: str, color: str = Colors.END) -> None:
        """Print a colored message."""
        print(f"{color}{message}{Colors.END}")
    
    def _print_success(self, message: str) -> None:
        """Print a success message in green."""
        self._print_colored(f"✅ {message}", Colors.GREEN)
    
    def _print_error(self, message: str) -> None:
        """Print an error message in red."""
        self._print_colored(f"❌ {message}", Colors.RED)
    
    def _print_info(self, message: str) -> None:
        """Print an info message in blue."""
        self._print_colored(f"ℹ️  {message}", Colors.BLUE)
    
    def _print_warning(self, message: str) -> None:
        """Print a warning message in yellow."""
        self._print_colored(f"⚠️  {message}", Colors.YELLOW)
    
    def _validate_session_file(self, session_file: str) -> bool:
        """Validate that a session file exists and is valid JSON."""
        session_path = Path(session_file)
        if not session_path.exists():
            self._print_error(f"Session file not found: {session_file}")
            return False
        
        try:
            with open(session_path, 'r') as f:
                json.load(f)
            return True
        except json.JSONDecodeError:
            self._print_error(f"Invalid JSON in session file: {session_file}")
            return False

    def plan_feature(self, feature_request: str, save_to_file: bool = False) -> Dict[str, Any]:
        """
        Step 1: Take a feature request and generate the orchestrator prompt.
        By default, outputs to terminal. Use save_to_file=True to save to file.
        """
        self._print_info(f"Planning feature: {feature_request[:100]}{'...' if len(feature_request) > 100 else ''}")
        
        # Create session data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_id = f"{self._sanitize_filename(feature_request)}_{timestamp}"
        
        session_data = {
            "id": session_id,
            "feature_request": feature_request,
            "timestamp": timestamp,
            "status": "planned",
            "project_type": None,  # Will be filled by orchestrator
            "files": {
                "orchestrator_prompt": None,
                "analysis_template": None,
                "implementation_template": None,
                "execution_notes": None
            }
        }
        
        # Generate orchestrator prompt - using named placeholders
        prompt = self.orchestrator_prompt.format(
            python_cmd=self.python_cmd,
            feature_request=feature_request
        )
        
        # Save session
        session_file = self.sessions_dir / f"{session_id}.json"
        session_data["files"]["orchestrator_prompt"] = prompt
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        self._print_success(f"Created session: {session_id}")
        self._print_info(f"Session file: {session_file}")
        
        if save_to_file:
            # Save to file
            prompt_file = self.outputs_dir / f"{session_id}_orchestrator_prompt.md"
            with open(prompt_file, 'w') as f:
                f.write(prompt)
            self._print_success(f"Orchestrator prompt saved to: {prompt_file}")
        else:
            # Output to terminal (default)
            print("\n" + "="*80)
            self._print_colored("ORCHESTRATOR PROMPT - Copy everything below:", Colors.BOLD)
            print("="*80 + "\n")
            print(prompt)
            print("\n" + "="*80)
        
        self._print_colored("\nNEXT STEPS:", Colors.BOLD)
        print("1. Copy the orchestrator prompt above and feed to your LLM")
        print("2. Save the LLM's output")
        print(f"3. Run: {Colors.YELLOW}python orchestrator.py process-orchestrator --session-file {session_file}{Colors.END}")
        print("="*60 + "\n")
        
        return session_data
    
    def batch_plan_features(self, features_file: str, save_to_file: bool = False) -> List[Dict[str, Any]]:
        """
        Plan multiple features from a file.
        File format: One feature per line, or separated by '---' for multi-line features.
        """
        self._print_info(f"Processing batch features from: {features_file}")
        
        if not Path(features_file).exists():
            self._print_error(f"Features file not found: {features_file}")
            return []
        
        try:
            with open(features_file, 'r') as f:
                content = f.read()
        except Exception as e:
            self._print_error(f"Error reading features file: {e}")
            return []
        
        # Check if using separator format or line format
        if '---' in content:
            # Multi-line features separated by ---
            features = [f.strip() for f in content.split('---') if f.strip()]
        else:
            # One feature per line
            features = [line.strip() for line in content.splitlines() if line.strip()]
        
        self._print_info(f"Found {len(features)} features to plan")
        
        sessions = []
        for i, feature in enumerate(features, 1):
            print(f"\n[{i}/{len(features)}] ", end="")
            session = self.plan_feature(feature, save_to_file=save_to_file)
            sessions.append(session)
            
            # Brief pause between features if outputting to terminal
            if not save_to_file and i < len(features):
                print(f"\n{Colors.YELLOW}Press Enter to continue to next feature...{Colors.END}")
                input()
        
        self._print_success(f"Batch planning complete! Created {len(sessions)} sessions.")
        return sessions
    
    def get_interactive_feature(self) -> str:
        """Get feature description interactively, supporting multi-line input."""
        self._print_colored("📝 Enter your feature description (multi-line supported)", Colors.BLUE)
        print("Type 'END' on a new line when finished:\n")
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        
        return '\n'.join(lines)
    
    def process_orchestrator_output(self, session_file: str, orchestrator_output: str) -> Dict[str, Any]:
        """
        Step 2: Process the orchestrator output to extract filled templates.
        """
        self._print_info("Processing orchestrator output...")
        
        if not self._validate_session_file(session_file):
            return {}
        
        # Load session
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        # Parse orchestrator output to extract the three sections
        sections = self._parse_orchestrator_output(orchestrator_output)
        
        if not all(k in sections for k in ['analysis', 'implementation', 'notes']):
            self._print_error("Could not parse all sections from orchestrator output")
            print("Expected sections: ANALYSIS_TEMPLATE, IMPLEMENTATION_TEMPLATE, EXECUTION_NOTES")
            print("\nTroubleshooting:")
            print("- Ensure the AI output includes all three numbered sections")
            print("- Sections should be labeled: 1. ANALYSIS_TEMPLATE, 2. IMPLEMENTATION_TEMPLATE, 3. EXECUTION_NOTES")
            print("- Content can be in code blocks or plain text")
            
            # Show what was found
            print(f"\nSections found: {list(sections.keys())}")
            
            # Try to provide helpful debugging info
            if not sections:
                print("\nNo sections were parsed. Check the output format.")
            else:
                for section, content in sections.items():
                    print(f"\n{section}: {len(content)} characters")
            
            return session_data
        
        # Update session data
        session_data["files"]["analysis_template"] = sections['analysis']
        session_data["files"]["implementation_template"] = sections['implementation']
        session_data["files"]["execution_notes"] = sections['notes']
        session_data["status"] = "templates_ready"
        
        # Extract metadata from execution notes
        if "Estimated Time:" in sections['notes'] or "Time:" in sections['notes']:
            time_match = re.search(r'(?:Estimated )?Time:\s*(\d+(?:-\d+)?)\s*hours?', sections['notes'], re.IGNORECASE)
            if time_match:
                session_data["time_estimate"] = time_match.group(1)
        
        if "Complexity:" in sections['notes']:
            complexity_match = re.search(r'Complexity:\s*(\w+)', sections['notes'], re.IGNORECASE)
            if complexity_match:
                session_data["complexity"] = complexity_match.group(1)
        
        # Save updated session
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        # Save individual template files
        session_id = session_data["id"]
        
        analysis_file = self.outputs_dir / f"{session_id}_analysis_template.md"
        with open(analysis_file, 'w') as f:
            f.write(sections['analysis'])
        
        implementation_file = self.outputs_dir / f"{session_id}_implementation_template.md"
        with open(implementation_file, 'w') as f:
            f.write(sections['implementation'])
        
        notes_file = self.outputs_dir / f"{session_id}_execution_notes.md"
        with open(notes_file, 'w') as f:
            f.write(sections['notes'])
        
        self._print_success("Templates extracted and saved")
        self._print_info(f"Analysis template: {analysis_file}")
        self._print_info(f"Implementation template: {implementation_file}")
        self._print_info(f"Execution notes: {notes_file}")
        
        self._print_colored("\nNEXT STEPS:", Colors.BOLD)
        print(f"1. Run analysis: {Colors.YELLOW}python orchestrator.py analyze --session-file {session_file}{Colors.END}")
        print("="*60 + "\n")
        
        return session_data
    
    def run_analysis(self, session_file: str, save_to_file: bool = False) -> str:
        """
        Step 3: Generate prompt for running the analysis template.
        By default, outputs to terminal. Use save_to_file=True to save to file.
        """
        self._print_info("Preparing analysis phase...")
        
        if not self._validate_session_file(session_file):
            return ""
        
        # Load session
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        if not session_data["files"]["analysis_template"]:
            self._print_error("No analysis template found. Run process-orchestrator first.")
            return ""
        
        # Create analysis prompt with comprehensive role
        analysis_prompt = f"""# Role: Senior Software Analyst & Code Archaeologist

You are a senior software analyst with 15+ years of experience in:
- Reverse engineering complex codebases
- Identifying architectural patterns and design decisions
- Understanding implicit conventions and standards
- Mapping component relationships and data flows
- Recognizing testing strategies and quality standards

## Your Current Mission

You are executing a deep analysis of this codebase to prepare for implementing: {session_data['feature_request']}

Your analysis must be so thorough and detailed that another developer could implement this feature without looking at the code themselves. Think of yourself as creating a comprehensive map of unfamiliar territory.

## Analysis Execution Instructions

You are now in the project directory. Follow the analysis template below methodically. For each phase:
1. Execute the suggested investigation steps
2. Document your findings in detail
3. Note specific examples and file locations
4. Identify patterns and conventions
5. Flag any concerns or complexity

## Analysis Template to Execute:

{session_data['files']['analysis_template']}

## Expected Analysis Output

Your deliverable should include:

### 1. Architecture Overview
- System design pattern (MVC, microservices, etc.)
- Component organization and responsibilities
- Data flow diagrams (described textually)
- Integration patterns

### 2. Code Conventions Document
- Naming standards (with examples)
- File organization patterns
- Import/export conventions
- Error handling patterns
- Logging approaches

### 3. Feature Integration Points
- Exactly where this feature will integrate
- Which files will need modification
- What patterns to follow for integration
- Potential conflicts or challenges

### 4. Testing Strategy
- How similar features are tested
- Test file organization
- Mocking/stubbing patterns
- Expected test coverage

### 5. Implementation Readiness Checklist
- Prerequisites confirmed
- Patterns identified
- Integration points mapped
- Risks documented

## Critical Reminders

1. **Be Specific**: Don't say "uses MVC pattern" - show exactly how with file examples
2. **Document Locations**: Always include file paths and line numbers when relevant
3. **Show Examples**: Include code snippets that demonstrate patterns
4. **Think Integration**: Focus on how the new feature will fit into existing code
5. **Anticipate Issues**: Flag any potential problems or complexity

Remember: Your analysis will be the only guide for implementation. Make it comprehensive."""
        
        if save_to_file:
            # Save analysis prompt
            session_id = session_data["id"]
            analysis_prompt_file = self.outputs_dir / f"{session_id}_analysis_prompt.md"
            with open(analysis_prompt_file, 'w') as f:
                f.write(analysis_prompt)
            self._print_success(f"Analysis prompt saved to: {analysis_prompt_file}")
        else:
            # Output to terminal (default)
            print("\n" + "="*80)
            self._print_colored("ANALYSIS PROMPT - Copy everything below:", Colors.BOLD)
            print("="*80 + "\n")
            print(analysis_prompt)
            print("\n" + "="*80)
        
        # Update session status
        session_data["status"] = "analyzing"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        self._print_colored("\nNEXT STEPS:", Colors.BOLD)
        print("1. Copy the analysis prompt above and feed to your LLM (while in the project directory)")
        print("2. Save the analysis output")
        print(f"3. Run: {Colors.YELLOW}python orchestrator.py process-analysis --session-file {session_file}{Colors.END}")
        print("="*60 + "\n")
        
        return analysis_prompt
    
    def process_analysis_output(self, session_file: str, analysis_output: str) -> Dict[str, Any]:
        """
        Step 4: Process the analysis output and prepare for implementation.
        """
        self._print_info("Processing analysis output...")
        
        if not self._validate_session_file(session_file):
            return {}
        
        # Load session
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        # Save analysis output
        session_data["files"]["analysis_output"] = analysis_output
        session_data["status"] = "analysis_complete"
        
        # Save to file
        session_id = session_data["id"]
        analysis_output_file = self.outputs_dir / f"{session_id}_analysis_output.md"
        with open(analysis_output_file, 'w') as f:
            f.write(analysis_output)
        
        # Update session
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        self._print_success("Analysis output saved")
        self._print_info(f"Analysis results: {analysis_output_file}")
        
        self._print_colored("\nNEXT STEPS:", Colors.BOLD)
        print(f"1. Run implementation: {Colors.YELLOW}python orchestrator.py implement --session-file {session_file}{Colors.END}")
        print("="*60 + "\n")
        
        return session_data
    
    def run_implementation(self, session_file: str, save_to_file: bool = False) -> str:
        """
        Step 5: Generate prompt for running the implementation template.
        By default, outputs to terminal. Use save_to_file=True to save to file.
        """
        self._print_info("Preparing implementation phase...")
        
        if not self._validate_session_file(session_file):
            return ""
        
        # Load session
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        if not session_data["files"]["implementation_template"]:
            self._print_error("No implementation template found.")
            return ""
        
        if not session_data["files"]["analysis_output"]:
            self._print_error("No analysis output found. Run analysis first.")
            return ""
        
        # Create implementation prompt with comprehensive role
        implementation_prompt = f"""# Role: Senior Software Engineer & Feature Implementation Specialist

You are a senior software engineer with deep expertise in:
- Building production-ready features with zero defects
- Following existing patterns with absolute precision
- Writing comprehensive test suites
- Creating self-documenting code
- Handling edge cases and error scenarios
- Integrating features seamlessly into existing systems

## Your Current Mission

You are implementing the feature: {session_data['feature_request']}

You must deliver a complete, production-ready implementation that looks like it was written by the original team. Your code should be indistinguishable from the existing codebase in terms of style, patterns, and quality.

## Critical Implementation Rules

1. **Pattern Conformity is Law**: Follow existing patterns EXACTLY - no improvements or personal preferences
2. **Minimal Disruption**: Touch only what's necessary for the feature
3. **Test Everything**: Every new function/method needs tests
4. **Document Decisions**: Explain WHY, not just WHAT
5. **Handle All Cases**: Think about edge cases, errors, and exceptional scenarios

## Analysis Context

The following analysis provides your complete understanding of the codebase:

{session_data['files']['analysis_output']}

## Implementation Template to Execute:

{session_data['files']['implementation_template']}

## Expected Implementation Deliverables

### 1. Code Changes Documentation
For each file created or modified:
```
File: [path/to/file]
Type: [Created/Modified]
Purpose: [Why this change is needed]
Changes: [Specific modifications made]
```

### 2. Actual Implementation Code
Show the complete code for:
- All new files (entire file content)
- All modifications (before/after for context)
- Configuration changes
- Database migrations (if applicable)

### 3. Test Implementation
Provide comprehensive tests:
- Unit tests for every new function/method
- Integration tests for feature flows
- Edge case tests
- Error scenario tests
Include the actual test code, not just descriptions

### 4. Verification Steps
Document how to verify the implementation:
- How to run the feature
- Expected behavior
- How to run tests
- Performance considerations

### 5. Integration Confirmation
Confirm that:
- All existing tests still pass
- No existing functionality is broken
- Performance is acceptable
- Security is maintained

## Implementation Quality Checklist

Before considering your implementation complete, verify:

- [ ] Follows all patterns identified in analysis
- [ ] All new code has corresponding tests
- [ ] Error handling matches project standards
- [ ] Logging follows project conventions
- [ ] Documentation is complete
- [ ] No TODO or FIXME comments remain
- [ ] Code is ready for production

## Common Implementation Pitfalls to Avoid

1. **Don't Refactor**: Even if you see better ways, stick to existing patterns
2. **Don't Skip Tests**: Every code path needs test coverage
3. **Don't Assume**: If something is unclear, document your interpretation
4. **Don't Over-Engineer**: Implement exactly what's needed, no more
5. **Don't Break Compatibility**: Ensure backward compatibility

Remember: Your implementation should be so clean and well-integrated that it looks like it was always part of the codebase. The analysis has given you the map - now follow it precisely."""
        
        if save_to_file:
            # Save implementation prompt
            session_id = session_data["id"]
            impl_prompt_file = self.outputs_dir / f"{session_id}_implementation_prompt.md"
            with open(impl_prompt_file, 'w') as f:
                f.write(implementation_prompt)
            self._print_success(f"Implementation prompt saved to: {impl_prompt_file}")
        else:
            # Output to terminal (default)
            print("\n" + "="*80)
            self._print_colored("IMPLEMENTATION PROMPT - Copy everything below:", Colors.BOLD)
            print("="*80 + "\n")
            print(implementation_prompt)
            print("\n" + "="*80)
        
        # Update session status
        session_data["status"] = "implementing"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        self._print_colored("\nNEXT STEPS:", Colors.BOLD)
        print("1. Copy the implementation prompt above and feed to your LLM (while in the project directory)")
        print("2. Let it implement the feature following all patterns")
        print(f"3. Run: {Colors.YELLOW}python orchestrator.py complete --session-file {session_file}{Colors.END}")
        print("="*60 + "\n")
        
        return implementation_prompt
    
    def complete_session(self, session_file: str, implementation_output: str) -> None:
        """
        Step 6: Mark session as complete and save final output.
        """
        self._print_info("Completing session...")
        
        if not self._validate_session_file(session_file):
            return
        
        # Load session
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        # Save implementation output
        session_id = session_data["id"]
        impl_output_file = self.outputs_dir / f"{session_id}_implementation_output.md"
        with open(impl_output_file, 'w') as f:
            f.write(implementation_output)
        
        session_data["files"]["implementation_output"] = implementation_output
        session_data["status"] = "complete"
        session_data["completed_at"] = datetime.now().isoformat()
        
        # Update session
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        # Generate summary
        self._generate_summary(session_data)
        
        self._print_success("Feature implementation complete!")
        self._print_info(f"All outputs in: {self.outputs_dir}")
        print(f"\n{Colors.BOLD}Session Summary:{Colors.END}")
        print(f"- Feature: {session_data['feature_request'][:80]}...")
        print(f"- Time Estimate: {session_data.get('time_estimate', 'Unknown')}")
        print(f"- Complexity: {session_data.get('complexity', 'Unknown')}")
        print(f"- Status: {Colors.GREEN}{session_data['status']}{Colors.END}")
    
    def show_status(self, session_file: str) -> None:
        """Show the current status of a session with detailed information."""
        if not self._validate_session_file(session_file):
            return
        
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        print(f"\n{Colors.BOLD}Session Status:{Colors.END}")
        print(f"ID: {session_data['id']}")
        print(f"Feature: {session_data['feature_request'][:100]}...")
        print(f"Status: {self._get_status_colored(session_data['status'])}")
        print(f"Created: {session_data['timestamp']}")
        
        if session_data.get('completed_at'):
            print(f"Completed: {session_data['completed_at']}")
        
        if session_data.get('time_estimate'):
            print(f"Time Estimate: {session_data['time_estimate']} hours")
        
        if session_data.get('complexity'):
            print(f"Complexity: {session_data['complexity']}")
        
        print(f"\n{Colors.BOLD}Files:{Colors.END}")
        for file_type, content in session_data['files'].items():
            if content:
                print(f"✅ {file_type}")
            else:
                print(f"⏳ {file_type}")
        
        # Show next steps based on status
        print(f"\n{Colors.BOLD}Next Steps:{Colors.END}")
        next_steps = {
            "planned": f"Run: {Colors.YELLOW}python orchestrator.py process-orchestrator --session-file {session_file}{Colors.END}",
            "templates_ready": f"Run: {Colors.YELLOW}python orchestrator.py analyze --session-file {session_file}{Colors.END}",
            "analyzing": "Feed the analysis prompt to your LLM and save the output",
            "analysis_complete": f"Run: {Colors.YELLOW}python orchestrator.py implement --session-file {session_file}{Colors.END}",
            "implementing": "Feed the implementation prompt to your LLM and save the output",
            "complete": "Review the implementation and test your feature!"
        }
        
        print(next_steps.get(session_data['status'], "Unknown status"))
    
    def _get_status_colored(self, status: str) -> str:
        """Return status with appropriate color."""
        status_colors = {
            "planned": Colors.BLUE,
            "templates_ready": Colors.BLUE,
            "analyzing": Colors.YELLOW,
            "analysis_complete": Colors.YELLOW,
            "implementing": Colors.YELLOW,
            "complete": Colors.GREEN
        }
        color = status_colors.get(status, Colors.END)
        return f"{color}{status}{Colors.END}"
    
    def list_sessions(self) -> None:
        """List all sessions and their status."""
        print(f"\n{Colors.BOLD}All Sessions:{Colors.END}\n")
        
        sessions = list(self.sessions_dir.glob("*.json"))
        if not sessions:
            print("No sessions found.")
            return
        
        # Group by status
        by_status = {}
        for session_file in sorted(sessions, reverse=True):
            try:
                with open(session_file, 'r') as f:
                    data = json.load(f)
                
                status = data.get('status', 'unknown')
                if status not in by_status:
                    by_status[status] = []
                by_status[status].append((session_file, data))
            except:
                continue
        
        # Display grouped by status
        status_order = ["complete", "implementing", "analysis_complete", "analyzing", "templates_ready", "planned"]
        for status in status_order:
            if status in by_status:
                print(f"{Colors.BOLD}{status.upper()}{Colors.END}")
                for session_file, data in by_status[status]:
                    status_emoji = {
                        "planned": "📝",
                        "templates_ready": "📋",
                        "analyzing": "🔍",
                        "analysis_complete": "📊",
                        "implementing": "🔨",
                        "complete": "✅"
                    }.get(data["status"], "❓")
                    
                    print(f"\n{status_emoji} {data['id']}")
                    print(f"   Feature: {data['feature_request'][:60]}...")
                    print(f"   Created: {data['timestamp']}")
                    if data.get('time_estimate'):
                        print(f"   Estimate: {data['time_estimate']} hours")
                    print(f"   File: {session_file}")
                print()
    
    def _parse_orchestrator_output(self, output: str) -> Dict[str, str]:
        """Parse the three sections from orchestrator output with flexible matching."""
        sections = {}
        
        # Normalize the output - handle various markdown formats
        output = output.replace('\r\n', '\n')
        
        # Try to extract each section with multiple patterns
        # Look for numbered sections with various formats
        
        # Pattern groups for each section
        section_patterns = {
            'analysis': [
                # With code blocks
                r'(?:###?\s*)?1\.\s*ANALYSIS_TEMPLATE[^\n]*\n+```[^\n]*\n(.*?)\n```',
                # Without code blocks
                r'(?:###?\s*)?1\.\s*ANALYSIS_TEMPLATE[^\n]*\n+(.*?)(?=\n(?:###?\s*)?2\.|$)',
                # Case insensitive
                r'(?i)(?:###?\s*)?1\.\s*analysis[_\s]?template[^\n]*\n+```[^\n]*\n(.*?)\n```',
                r'(?i)(?:###?\s*)?1\.\s*analysis[_\s]?template[^\n]*\n+(.*?)(?=\n(?:###?\s*)?2\.|$)',
            ],
            'implementation': [
                # With code blocks
                r'(?:###?\s*)?2\.\s*IMPLEMENTATION_TEMPLATE[^\n]*\n+```[^\n]*\n(.*?)\n```',
                # Without code blocks
                r'(?:###?\s*)?2\.\s*IMPLEMENTATION_TEMPLATE[^\n]*\n+(.*?)(?=\n(?:###?\s*)?3\.|$)',
                # Case insensitive
                r'(?i)(?:###?\s*)?2\.\s*implementation[_\s]?template[^\n]*\n+```[^\n]*\n(.*?)\n```',
                r'(?i)(?:###?\s*)?2\.\s*implementation[_\s]?template[^\n]*\n+(.*?)(?=\n(?:###?\s*)?3\.|$)',
            ],
            'notes': [
                # With code blocks
                r'(?:###?\s*)?3\.\s*EXECUTION_NOTES[^\n]*\n+```[^\n]*\n(.*?)\n```',
                # Without code blocks
                r'(?:###?\s*)?3\.\s*EXECUTION_NOTES[^\n]*\n+(.*?)$',
                # Case insensitive
                r'(?i)(?:###?\s*)?3\.\s*execution[_\s]?notes[^\n]*\n+```[^\n]*\n(.*?)\n```',
                r'(?i)(?:###?\s*)?3\.\s*execution[_\s]?notes[^\n]*\n+(.*?)$',
            ]
        }
        
        # Try each pattern for each section
        for section_name, patterns in section_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, output, re.DOTALL)
                if match:
                    content = match.group(1).strip()
                    sections[section_name] = content
                    break
        
        # If we couldn't find all sections, try a more lenient approach
        if len(sections) < 3:
            # Look for any numbered sections
            numbered_sections = re.findall(
                r'(?:###?\s*)?(\d)\.\s*([A-Z_]+)[^\n]*\n+((?:```[^\n]*\n)?.*?)(?=\n(?:###?\s*)?\d\.|$)',
                output,
                re.DOTALL | re.IGNORECASE
            )
            
            for num, title, content in numbered_sections:
                # Clean up content
                content = content.strip()
                if content.startswith('```'):
                    # Extract from code block
                    code_match = re.match(r'```[^\n]*\n(.*?)\n```', content, re.DOTALL)
                    if code_match:
                        content = code_match.group(1).strip()
                
                # Map to our expected sections
                if '1' in num and 'analysis' not in sections:
                    sections['analysis'] = content
                elif '2' in num and 'implementation' not in sections:
                    sections['implementation'] = content
                elif '3' in num and 'notes' not in sections:
                    sections['notes'] = content
        
        return sections
    
    def _sanitize_filename(self, text: str) -> str:
        """Convert feature request to safe filename."""
        # Remove special characters and replace spaces
        safe = re.sub(r'[^\w\s-]', '', text.lower())
        safe = re.sub(r'[-\s]+', '_', safe)
        return safe[:50]  # Limit length
    
    def _generate_summary(self, session_data: Dict[str, Any]) -> None:
        """Generate a summary report for the completed session."""
        session_id = session_data["id"]
        summary_file = self.outputs_dir / f"{session_id}_summary.md"
        
        summary = f"""# Feature Implementation Summary

## Feature: {session_data['feature_request']}
**Session ID**: {session_id}
**Status**: {session_data['status']}
**Created**: {session_data['timestamp']}
**Completed**: {session_data.get('completed_at', 'N/A')}

## Estimates
- **Time**: {session_data.get('time_estimate', 'Unknown')} hours
- **Complexity**: {session_data.get('complexity', 'Unknown')}

## Process Timeline
1. ✅ Planning - Created orchestrator prompt
2. ✅ Template Generation - Filled analysis and implementation templates  
3. ✅ Analysis - Understood project patterns
4. ✅ Implementation - Built the feature

## Output Files
- Orchestrator Prompt: `{session_id}_orchestrator_prompt.md`
- Analysis Template: `{session_id}_analysis_template.md`
- Implementation Template: `{session_id}_implementation_template.md`
- Execution Notes: `{session_id}_execution_notes.md`
- Analysis Output: `{session_id}_analysis_output.md`
- Implementation Output: `{session_id}_implementation_output.md`

## Next Steps
1. Review the implementation output
2. Test the feature
3. Commit the changes
"""
        
        with open(summary_file, 'w') as f:
            f.write(summary)
        
        self._print_info(f"Summary report: {summary_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Template Orchestrator - Automated Feature Planning System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(f"""
        Examples:
            # Start a new feature (outputs prompt to terminal by default)
            {Colors.YELLOW}python orchestrator.py plan "add user authentication"{Colors.END}
            
            # For complex multi-line features, use interactive mode
            {Colors.YELLOW}python orchestrator.py plan --interactive{Colors.END}
            
            # Read feature from file
            {Colors.YELLOW}python orchestrator.py plan --file feature.txt{Colors.END}
            
            # Plan multiple features at once
            {Colors.YELLOW}python orchestrator.py batch --file features.txt{Colors.END}
            
            # Save prompt to file instead
            {Colors.YELLOW}python orchestrator.py plan "add user authentication" --save-to-file{Colors.END}
            
            # Process orchestrator output
            {Colors.YELLOW}python orchestrator.py process-orchestrator --session-file sessions/auth_20240115.json --input output.txt{Colors.END}
            
            # Check session status
            {Colors.YELLOW}python orchestrator.py status --session-file sessions/auth_20240115.json{Colors.END}
            
            # Run analysis (outputs to terminal by default)
            {Colors.YELLOW}python orchestrator.py analyze --session-file sessions/auth_20240115.json{Colors.END}
            
            # Run implementation  
            {Colors.YELLOW}python orchestrator.py implement --session-file sessions/auth_20240115.json{Colors.END}
            
            # List all sessions
            {Colors.YELLOW}python orchestrator.py list{Colors.END}
        """)
    )
    
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Plan command
    plan_parser = subparsers.add_parser('plan', help='Plan a new feature')
    plan_parser.add_argument('feature', nargs='?', help='Feature description (optional if using --file or --interactive)')
    plan_parser.add_argument('--save-to-file', action='store_true', 
                           help='Save prompt to file instead of displaying in terminal')
    plan_parser.add_argument('--file', '-f', help='Read feature description from file')
    plan_parser.add_argument('--interactive', '-i', action='store_true',
                           help='Enter feature description interactively (for complex multi-line features)')
    
    # Batch command for multiple features
    batch_parser = subparsers.add_parser('batch', help='Plan multiple features at once')
    batch_parser.add_argument('--file', '-f', required=True, help='File containing feature list (one per line or separated by ---)')
    batch_parser.add_argument('--save-to-file', action='store_true',
                            help='Save all prompts to files instead of displaying')
    
    # Process orchestrator output
    process_orch_parser = subparsers.add_parser('process-orchestrator', help='Process orchestrator output')
    process_orch_parser.add_argument('--session-file', required=True, help='Session file path')
    process_orch_parser.add_argument('--input', help='Input file with orchestrator output (or stdin)')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show session status')
    status_parser.add_argument('--session-file', required=True, help='Session file path')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Run analysis phase')
    analyze_parser.add_argument('--session-file', required=True, help='Session file path')
    analyze_parser.add_argument('--save-to-file', action='store_true',
                              help='Save prompt to file instead of displaying in terminal')
    
    # Process analysis output
    process_analysis_parser = subparsers.add_parser('process-analysis', help='Process analysis output')
    process_analysis_parser.add_argument('--session-file', required=True, help='Session file path')
    process_analysis_parser.add_argument('--input', help='Input file with analysis output (or stdin)')
    
    # Implement command
    implement_parser = subparsers.add_parser('implement', help='Run implementation phase')
    implement_parser.add_argument('--session-file', required=True, help='Session file path')
    implement_parser.add_argument('--save-to-file', action='store_true',
                                help='Save prompt to file instead of displaying in terminal')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Complete the session')
    complete_parser.add_argument('--session-file', required=True, help='Session file path')
    complete_parser.add_argument('--input', help='Input file with implementation output (or stdin)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all sessions')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    orchestrator = TemplateOrchestrator()
    
    try:
        if args.command == 'plan':
            # Handle different input methods
            if args.file:
                # Read from file
                with open(args.file, 'r') as f:
                    feature_request = f.read().strip()
            elif args.interactive:
                # Get interactively
                feature_request = orchestrator.get_interactive_feature()
            elif args.feature:
                # Use command line argument
                feature_request = args.feature
            else:
                # No feature provided
                orchestrator._print_error("Please provide a feature description via command line, --file, or --interactive")
                return
            
            orchestrator.plan_feature(feature_request, save_to_file=args.save_to_file)
        
        elif args.command == 'batch':
            orchestrator.batch_plan_features(args.file, save_to_file=args.save_to_file)
        
        elif args.command == 'process-orchestrator':
            if args.input:
                with open(args.input, 'r') as f:
                    output = f.read()
            else:
                print("Paste the orchestrator output (Ctrl+D when done):")
                output = sys.stdin.read()
            orchestrator.process_orchestrator_output(args.session_file, output)
        
        elif args.command == 'status':
            orchestrator.show_status(args.session_file)
        
        elif args.command == 'analyze':
            orchestrator.run_analysis(args.session_file, save_to_file=args.save_to_file)
        
        elif args.command == 'process-analysis':
            if args.input:
                with open(args.input, 'r') as f:
                    output = f.read()
            else:
                print("Paste the analysis output (Ctrl+D when done):")
                output = sys.stdin.read()
            orchestrator.process_analysis_output(args.session_file, output)
        
        elif args.command == 'implement':
            orchestrator.run_implementation(args.session_file, save_to_file=args.save_to_file)
        
        elif args.command == 'complete':
            if args.input:
                with open(args.input, 'r') as f:
                    output = f.read()
            else:
                print("Paste the implementation output (Ctrl+D when done):")
                output = sys.stdin.read()
            orchestrator.complete_session(args.session_file, output)
        
        elif args.command == 'list':
            orchestrator.list_sessions()
    
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Operation cancelled by user.{Colors.END}")
        sys.exit(0)
    except Exception as e:
        orchestrator._print_error(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
