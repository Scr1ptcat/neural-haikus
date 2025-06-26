  1. Architecture Overview

  System Design Pattern

  The prompt-runner project follows a Modular Command-Line Architecture with these key patterns:
  - Command Pattern: Each functionality is encapsulated in separate command modules
  - Repository Pattern: Database operations abstracted through db_ops functions
  - Service Layer: Business logic separated in modules like workflows/, cache/, optimization/
  - Plugin Architecture: Commands are dynamically registered via Typer

  Component Organization

  prompt_tool/
  ├── cli.py                  # Main entry point, command registration
  ├── commands/               # CLI command implementations
  │   ├── project_cmds.py    # Project management
  │   ├── workflow_cmds.py   # Workflow execution (similar to orchestrator)
  │   └── [other_cmds].py    # Other command groups
  ├── core/                   # Core utilities
  │   ├── templating.py      # Template engine with variable substitution
  │   └── model_integration.py # LLM integration layer
  ├── db/                     # Database layer
  │   ├── models.py          # SQLAlchemy models
  │   └── db_utils.py        # Database operations
  └── workflows/              # Workflow engine (similar functionality)
      └── engine.py          # Step-by-step execution

  Data Flow

  1. CLI Command → Typer router → Command function
  2. Command Function → Validates input → Database operations
  3. Business Logic → Core modules → Model integration
  4. Output → Rich formatting → Console display

  Integration Patterns

  - Dependency Injection: Database sessions injected via context managers
  - Decorator Pattern: @with_db_session for automatic session handling
  - Template Method: Workflow execution follows defined steps

  2. Code Conventions Document

  Naming Standards

  - Files: snake_case.py (e.g., workflow_cmds.py, template_engine.py)
  - Command Groups: noun_cmds.py pattern (e.g., project_cmds.py)
  - Functions: snake_case with verb_noun pattern
  def create_workflow(name: str, ...)  # Good
  def list_sessions(project_id: int)   # Good
  - Classes: PascalCase
  class WorkflowEngine:
  class OrchestrationSession(Base):  # SQLAlchemy models
  - CLI Commands: Verb-noun with hyphens
  prompt-runner workflow create
  prompt-runner orchestrate list-sessions  # Proposed

  File Organization Patterns

  - Command modules: All commands in prompt_tool/commands/
  - One Typer app per command group: Each file exports app = typer.Typer(...)
  - Related functionality grouped: e.g., all workflow logic in workflows/

  Import/Export Conventions

  # Standard import order (enforced by isort)
  import os  # stdlib
  from pathlib import Path
  from typing import Optional, Dict

  import typer  # third-party
  from rich.console import Console
  from sqlalchemy.orm import Session

  from prompt_tool.db.models import Project  # local absolute imports
  from prompt_tool.core.templating import TemplateEngine

  Error Handling Patterns

  # Consistent error handling via utils
  try:
      # operation
  except Exception as e:
      handle_command_error("creating session", e)

  # Validation with early exit
  entity = validate_entity_exists(session, "Project", name, db_ops.get_project_by_name)

  Logging Approaches

  - Rich console for user-facing output: console.print("[green]✓[/green] Success")
  - Progress bars for long operations: with Progress() as progress:
  - Tables for structured data display

  3. Feature Integration Points

  Primary Integration Point: New Command Group

  Create prompt_tool/commands/orchestrate_cmds.py:
  app = typer.Typer(name="orchestrate", help="Feature planning and orchestration")

  Register in prompt_tool/cli.py:27-39:
  from prompt_tool.commands import orchestrate_cmds
  app.add_typer(orchestrate_cmds.app, name="orchestrate", help="Feature planning orchestration")

  Database Schema Extensions

  Add to prompt_tool/db/models.py after line 499:
  class OrchestrationSession(Base):
      __tablename__ = 'orchestration_sessions'

      id = Column(Integer, primary_key=True)
      session_id = Column(String(36), unique=True, nullable=False)
      project_id = Column(Integer, ForeignKey('projects.id'))
      feature_request = Column(Text, nullable=False)
      status = Column(String(20), default='planning')  # planning, analysis, implementation, completed

      # Template storage
      orchestrator_template = Column(Text)
      analysis_template = Column(Text)
      implementation_template = Column(Text)
      execution_notes = Column(Text)

      # Analysis results
      analysis_results = Column(Text)

      # Metadata
      complexity = Column(String(20))  # low, medium, high
      time_estimate = Column(String(50))
      created_at = Column(DateTime(timezone=True), server_default=func.now())
      updated_at = Column(DateTime(timezone=True), onupdate=func.now())

      # Relationships
      project = relationship("Project", backref="orchestration_sessions")
      executions = relationship("Execution", secondary="orchestration_executions")

  Module Structure

  Create prompt_tool/orchestration/:
  orchestration/
  ├── __init__.py
  ├── orchestrator.py         # Core logic from original script
  ├── session_manager.py      # Session lifecycle management
  ├── template_processor.py   # Template parsing and storage
  └── prompt_builder.py       # Prompt generation for each phase

  Integration with Existing Systems

  1. Leverage Workflow Engine: Use existing WorkflowEngine for multi-step execution
  2. Template System: Integrate with TemplateEngine for variable substitution
  3. Model Integration: Use ModelIntegration for LLM calls
  4. Project Association: Link sessions to projects like other entities

  Files to Modify

  1. prompt_tool/cli.py: Add command registration (line ~39)
  2. prompt_tool/db/models.py: Add new model (after line 499)
  3. alembic/versions/: Create new migration for schema

  Potential Conflicts

  - Workflow overlap: Clear distinction needed between workflows and orchestration
  - Template storage: Large templates may need TEXT columns or file fallback
  - Session naming: Avoid confusion with database sessions

  4. Testing Strategy

  Test Organization

  tests/
  ├── test_commands/
  │   └── test_orchestrate_cmds.py  # CLI command tests
  ├── test_orchestration/
  │   ├── test_orchestrator.py      # Core logic tests
  │   ├── test_session_manager.py   # Session management
  │   └── test_integration.py       # Full workflow tests
  └── conftest.py                   # Shared fixtures

  Testing Frameworks and Patterns

  - Framework: pytest with fixtures
  - CLI Testing: typer.testing.CliRunner
  - Mocking: unittest.mock for external dependencies
  - Database: Transactional fixtures with rollback

  Example Test Pattern

  class TestOrchestrateCommands:
      @pytest.fixture
      def runner(self):
          return CliRunner()

      @pytest.fixture
      def mock_session(self):
          with patch('prompt_tool.commands.orchestrate_cmds.db_manager') as mock:
              session = MagicMock()
              mock.session.return_value.__enter__.return_value = session
              yield session

      def test_plan_command(self, runner, mock_session):
          result = runner.invoke(app, ["plan", "add auth", "--project", "myapp"])
          assert result.exit_code == 0
          assert "Created session" in result.stdout

  Mock/Stub Approaches

  - Mock database sessions for unit tests
  - Mock LLM calls to avoid external dependencies
  - Use fixtures for test data setup

  Expected Coverage

  - Match project standard (likely 80%+)
  - Unit tests for all command functions
  - Integration tests for full orchestration flow
  - Edge case coverage for template parsing

  5. Implementation Readiness Checklist

  Prerequisites Confirmed ✓

  - Typer-based CLI architecture understood
  - SQLAlchemy model patterns identified
  - Command registration process clear
  - Testing patterns documented
  - Similar workflow system analyzed

  Patterns Identified ✓

  - Command module structure: app = typer.Typer() pattern
  - Error handling: handle_command_error() utility
  - Database operations: with db_manager.session() pattern
  - Output formatting: Rich console with colors/tables
  - File organization: Modular structure in commands/

  Integration Points Mapped ✓

  - CLI registration point: prompt_tool/cli.py:39
  - Database models location: prompt_tool/db/models.py
  - Command directory: prompt_tool/commands/
  - New module location: prompt_tool/orchestration/
  - Test directory structure planned

  Implementation Steps

  1. Database Migration
  alembic revision -m "Add orchestration tables"
  # Edit migration file
  alembic upgrade head
  2. Core Module Creation
    - Port orchestrator.py logic to prompt_tool/orchestration/
    - Adapt file storage to use database
    - Integrate with existing template system
  3. Command Implementation
    - Create orchestrate_cmds.py with commands: plan, analyze, implement, list-sessions
    - Follow workflow_cmds.py patterns for consistency
    - Use Rich for formatted output
  4. Testing
    - Unit tests for each component
    - Integration tests for full flow
    - CLI command tests

  Risks Documented

  1. Template Size: Large templates may exceed typical database column sizes
    - Mitigation: Use TEXT columns, consider file storage for very large templates
  2. State Management: Complex session states across multiple steps
    - Mitigation: Clear state machine, comprehensive status tracking
  3. User Experience: Confusion with existing workflow system
    - Mitigation: Clear documentation, distinct command names
  4. LLM Integration: Template extraction depends on LLM output format
    - Mitigation: Robust parsing with fallbacks, clear error messages

  Key Implementation Guidelines

  - Follow existing patterns exactly - no architectural changes
  - Use Rich for all output formatting
  - Integrate with project management system
  - Store templates in database for consistency
  - Provide clear progress indicators for long operations
  - Include comprehensive help text for all commands