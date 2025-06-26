# Orchestration UX Improvement Guide

## Context: Working with Manual LLM Interaction Constraints

Since the orchestration system requires manual copy/paste between the CLI and Claude.ai (or other LLM interfaces), we need creative solutions that work within these constraints while significantly improving the developer experience.

## Immediate UX Improvements (No External Dependencies)

### 1. Smart Session Management

#### Current Pain Point
```bash
# Users must type this repeatedly:
prompt-runner orchestrate analyze --session 20241225_143052_a1b2c3d4
```

#### Solution: Active Session Concept
```python
# Implementation in orchestrate_cmds.py
import os
from pathlib import Path

ACTIVE_SESSION_FILE = Path.home() / ".prompt-runner" / "active-session"

def set_active_session(session_id: str):
    """Set the active orchestration session."""
    ACTIVE_SESSION_FILE.parent.mkdir(exist_ok=True)
    ACTIVE_SESSION_FILE.write_text(session_id)

def get_active_session() -> Optional[str]:
    """Get the active orchestration session."""
    if ACTIVE_SESSION_FILE.exists():
        return ACTIVE_SESSION_FILE.read_text().strip()
    return None

# Modify all commands to use active session by default
def analyze(
    session_id: Optional[str] = typer.Option(None, "--session", "-s", help="Session ID (uses active if not specified)"),
    # ... other options
):
    if not session_id:
        session_id = get_active_session()
        if not session_id:
            console.print("[red]No active session. Use --session or set one with 'use-session'[/red]")
            raise typer.Exit(1)
```

#### New Commands
```bash
# Set active session
prompt-runner orchestrate use-session <session-id>

# Show current status
prompt-runner orchestrate status
# Output: Active session: abc123, Current phase: analysis, Next step: implement

# All subsequent commands use active session
prompt-runner orchestrate analyze    # No --session needed!
prompt-runner orchestrate implement  # Automatic
```

### 2. Intelligent Copy/Paste Helpers

#### Solution: Smart Output Formatting
```python
def format_for_copy(content: str, format_type: str = "markdown") -> str:
    """Format content for easy copying with visual markers."""
    
    # Add clear copy boundaries
    header = "┌─── COPY BELOW THIS LINE ───┐"
    footer = "└─── COPY ABOVE THIS LINE ───┘"
    
    # Add line numbers for large outputs
    if content.count('\n') > 50:
        lines = content.split('\n')
        numbered = [f"{i+1:4d} │ {line}" for i, line in enumerate(lines)]
        content = '\n'.join(numbered)
    
    # Add visual checksum for verification
    checksum = hashlib.md5(content.encode()).hexdigest()[:8]
    
    return f"""
{header}
{content}
{footer}
Checksum: {checksum} (verify after paste)
"""
```

#### Clipboard Integration (Cross-Platform)
```python
# Add to requirements.txt: pyperclip>=1.8.2

import pyperclip

def copy_to_clipboard(content: str) -> bool:
    """Copy content to system clipboard."""
    try:
        pyperclip.copy(content)
        return True
    except:
        return False

# Modify plan command
@app.command()
def plan(
    feature_request: str,
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy prompt to clipboard"),
    # ... other options
):
    # ... generate prompt
    
    if copy:
        if copy_to_clipboard(prompt):
            console.print("[green]✓[/green] Prompt copied to clipboard!")
        else:
            console.print("[yellow]![/yellow] Could not access clipboard, showing prompt instead")
```

### 3. Workflow Shortcuts

#### Solution: Combined Commands
```python
@app.command("flow")
def orchestration_flow(
    action: str = typer.Argument(..., help="Action: start, continue, or status"),
    feature: Optional[str] = typer.Option(None, "--feature", "-f", help="Feature description for start"),
    auto_copy: bool = typer.Option(True, "--auto-copy/--no-copy", help="Auto-copy prompts"),
):
    """Streamlined orchestration workflow."""
    
    if action == "start":
        # Create session and generate plan
        session_id = create_session(feature)
        set_active_session(session_id)
        prompt = generate_plan_prompt(session_id)
        
        if auto_copy and copy_to_clipboard(prompt):
            console.print(f"[green]✓[/green] Session created: {session_id}")
            console.print("[green]✓[/green] Planning prompt copied to clipboard!")
            console.print("\n[bold]Next:[/bold] Paste into Claude and run: [cyan]prompt-runner orchestrate flow continue[/cyan]")
        
    elif action == "continue":
        # Determine next phase and execute
        session_id = get_active_session()
        phase = get_current_phase(session_id)
        
        if phase == "planning":
            # Automatically read from clipboard or file
            content = pyperclip.paste() if auto_copy else read_interactive()
            process_orchestrator_output(session_id, content)
            # Generate next prompt
            next_prompt = generate_analysis_prompt(session_id)
            if auto_copy and copy_to_clipboard(next_prompt):
                console.print("[green]✓[/green] Analysis prompt copied to clipboard!")
```

### 4. Better Error Recovery

#### Solution: Checkpoint System
```python
class OrchestrationCheckpoint:
    """Save and restore orchestration state."""
    
    def __init__(self, session_id: str):
        self.checkpoint_dir = Path.home() / ".prompt-runner" / "checkpoints" / session_id
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
    
    def save_phase_input(self, phase: str, content: str):
        """Save input for a phase to enable retry."""
        file_path = self.checkpoint_dir / f"{phase}_input.txt"
        file_path.write_text(content)
    
    def save_phase_output(self, phase: str, content: str):
        """Save output for a phase."""
        file_path = self.checkpoint_dir / f"{phase}_output.txt"
        file_path.write_text(content)
    
    def can_retry(self, phase: str) -> bool:
        """Check if we can retry a phase."""
        return (self.checkpoint_dir / f"{phase}_input.txt").exists()

# Add retry command
@app.command("retry")
def retry_phase(
    phase: Optional[str] = typer.Option(None, "--phase", "-p", help="Phase to retry (auto-detects if not specified)"),
):
    """Retry the last failed operation."""
    session_id = get_active_session()
    checkpoint = OrchestrationCheckpoint(session_id)
    
    if not phase:
        phase = detect_failed_phase(session_id)
    
    if checkpoint.can_retry(phase):
        content = checkpoint.load_phase_input(phase)
        # Retry the operation
        retry_operation(session_id, phase, content)
```

### 5. Visual Progress Tracking

#### Solution: Rich Status Display
```python
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.panel import Panel

@app.command("status")
def show_status(
    session_id: Optional[str] = typer.Option(None, "--session", "-s", help="Session ID (uses active if not specified)"),
    detailed: bool = typer.Option(False, "--detailed", "-d", help="Show detailed status"),
):
    """Show orchestration session status with visual progress."""
    
    if not session_id:
        session_id = get_active_session()
    
    # Create visual progress display
    table = Table(title=f"Session: {session_id}")
    table.add_column("Phase", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Duration", style="yellow")
    table.add_column("Actions", style="blue")
    
    phases = ["Planning", "Analysis", "Implementation", "Testing", "Cleaning"]
    current_phase_idx = get_current_phase_index(session_id)
    
    for idx, phase in enumerate(phases):
        if idx < current_phase_idx:
            status = "✓ Complete"
            duration = get_phase_duration(session_id, phase)
            action = ""
        elif idx == current_phase_idx:
            status = "▶ In Progress"
            duration = "..."
            action = get_next_command(session_id, phase)
        else:
            status = "◯ Pending"
            duration = "-"
            action = ""
        
        table.add_row(phase, status, duration, action)
    
    console.print(table)
    
    # Show progress bar
    progress = (current_phase_idx / len(phases)) * 100
    console.print(f"\nOverall Progress: [green]{'█' * int(progress/10)}{'░' * (10-int(progress/10))}[/green] {progress:.0f}%")
```

### 6. Template Validation and Auto-fix

#### Solution: Smart Template Processing
```python
def validate_and_fix_template(template: str, template_type: str) -> tuple[str, list[str]]:
    """Validate template and auto-fix common issues."""
    fixes = []
    
    # Auto-fix common LLM formatting issues
    if "```" in template and not template.strip().startswith("```"):
        # LLM sometimes adds markdown formatting
        template = re.sub(r'```\w*\n?', '', template)
        fixes.append("Removed markdown code blocks")
    
    # Fix indentation issues
    if template_type in ["implementation", "testing"]:
        lines = template.split('\n')
        if any(line.startswith('    ') for line in lines):
            # Normalize indentation
            template = textwrap.dedent(template)
            fixes.append("Normalized indentation")
    
    # Validate Jinja2 syntax
    env = Environment()
    try:
        env.parse(template)
    except TemplateSyntaxError as e:
        # Try to auto-fix common Jinja2 errors
        if "unexpected '}'" in str(e):
            template = template.replace('}}', '} }')
            fixes.append("Fixed Jinja2 bracket spacing")
    
    return template, fixes
```

### 7. Batch Operations

#### Solution: Multi-Phase Commands
```python
@app.command("batch")
def batch_operations(
    operations: str = typer.Argument(..., help="Comma-separated operations: analyze,implement,test"),
    pause: bool = typer.Option(True, "--pause/--no-pause", help="Pause between operations"),
):
    """Execute multiple orchestration phases in sequence."""
    
    session_id = get_active_session()
    ops = [op.strip() for op in operations.split(',')]
    
    for i, op in enumerate(ops):
        console.print(f"\n[bold]Phase {i+1}/{len(ops)}: {op.title()}[/bold]")
        
        # Generate prompt for this phase
        prompt = generate_phase_prompt(session_id, op)
        
        if copy_to_clipboard(prompt):
            console.print(f"[green]✓[/green] {op.title()} prompt copied to clipboard!")
        
        if pause and i < len(ops) - 1:
            console.print("\n[yellow]Ready for next phase?[/yellow]")
            if not typer.confirm("Continue to next phase?"):
                break
        
        # Wait for user to complete LLM interaction
        console.print(f"\n[dim]Complete the {op} phase with Claude, then:[/dim]")
        console.print(f"[cyan]prompt-runner orchestrate save-{op} --paste[/cyan]")
        
        # Show progress
        show_mini_progress(i+1, len(ops))
```

## Advanced UX Patterns

### 1. Smart File Handling
```python
# Auto-detect orchestration output files
def auto_detect_files() -> list[Path]:
    """Detect recently created orchestration-related files."""
    download_dir = Path.home() / "Downloads"
    pattern = r"(orchestrat|planning|analysis|implement|test|clean).*\.(txt|md)"
    
    recent_files = []
    for file in download_dir.glob("*"):
        if re.match(pattern, file.name, re.IGNORECASE):
            if file.stat().st_mtime > time.time() - 300:  # Last 5 minutes
                recent_files.append(file)
    
    return recent_files

# Add to process command
if not file and not content:
    # Check for recent files
    recent = auto_detect_files()
    if recent:
        console.print("[yellow]Found recent files:[/yellow]")
        for i, f in enumerate(recent):
            console.print(f"{i+1}. {f.name}")
        
        choice = typer.prompt("Select file number (or 0 to skip)", type=int)
        if choice > 0 and choice <= len(recent):
            file = recent[choice-1]
```

### 2. Workflow Templates
```python
# Predefined workflow patterns
WORKFLOW_TEMPLATES = {
    "crud": {
        "name": "CRUD Operations",
        "phases": ["analyze", "implement", "test"],
        "templates": {
            "analysis": "crud_analysis_template.j2",
            "implementation": "crud_implementation_template.j2",
            "testing": "crud_testing_template.j2"
        }
    },
    "api": {
        "name": "API Endpoint",
        "phases": ["analyze", "implement", "test", "document"],
        "templates": {...}
    }
}

@app.command("workflow")
def use_workflow(
    workflow_type: str = typer.Argument(..., help="Workflow type: crud, api, refactor, etc."),
    feature: str = typer.Option(..., "--feature", "-f", help="Feature description"),
):
    """Use a predefined workflow template."""
    template = WORKFLOW_TEMPLATES.get(workflow_type)
    if not template:
        show_available_workflows()
        raise typer.Exit(1)
    
    # Create session with workflow template
    session_id = create_workflow_session(feature, template)
    set_active_session(session_id)
    
    console.print(f"[green]✓[/green] Started {template['name']} workflow")
    console.print(f"Session: [cyan]{session_id}[/cyan]")
    console.print(f"Phases: {' → '.join(template['phases'])}")
```

### 3. Intelligent Prompts
```python
def enhance_prompt_with_context(prompt: str, session_id: str) -> str:
    """Add relevant context to prompts based on session history."""
    
    # Get session context
    ctx = get_session_context(session_id)
    
    # Add relevant information
    enhancements = []
    
    if ctx.get('previous_errors'):
        enhancements.append(f"Note: Previous attempt had errors: {ctx['previous_errors']}")
    
    if ctx.get('tech_stack'):
        enhancements.append(f"Tech Stack: {', '.join(ctx['tech_stack'])}")
    
    if ctx.get('constraints'):
        enhancements.append(f"Constraints: {ctx['constraints']}")
    
    if enhancements:
        prompt += "\n\n## Additional Context\n" + "\n".join(f"- {e}" for e in enhancements)
    
    return prompt
```

## Implementation Priority

1. **Week 1**: Active sessions, smart copy/paste, status command
2. **Week 2**: Workflow shortcuts, checkpoint system, batch operations  
3. **Week 3**: Template validation, file auto-detection, progress tracking
4. **Week 4**: Workflow templates, context enhancement, advanced patterns

These improvements work within the manual LLM interaction constraint while dramatically improving the developer experience.