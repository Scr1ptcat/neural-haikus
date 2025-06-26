  Executive Summary

  The prompt-runner project requires enhancements to its orchestration system to:
  1. Fix the database migration issue (already resolved)
  2. Store orchestration prompts as special templates in the database
  3. Enable customization per project or feature type
  4. Support versioning and A/B testing of orchestration strategies
  5. Integrate the existing prompt template system
  6. Enhance orchestrator.py to use database templates

  This analysis provides a complete architectural understanding and implementation blueprint.

  1. Architecture Overview

  System Design Pattern

  The project follows a Layered Architecture with clear separation of concerns:

  ┌─────────────────────────────────────────────┐
  │         CLI Layer (Typer)                   │
  ├─────────────────────────────────────────────┤
  │     Command Modules (commands/*.py)         │
  ├─────────────────────────────────────────────┤
  │        Core Business Logic                  │
  │  (orchestration/, core/, ab_testing/)      │
  ├─────────────────────────────────────────────┤
  │      Database Access Layer                  │
  │      (db/models.py, db/db_utils.py)       │
  ├─────────────────────────────────────────────┤
  │     PostgreSQL Database (via SQLAlchemy)   │
  └─────────────────────────────────────────────┘

  Dual Orchestration Systems

  1. Standalone Orchestrator (/orchestrator.py):
  - File-based session management
  - No database dependencies
  - Stores sessions as JSON in orchestrator_workspace/sessions/
  - Version 1.2.0, 1,358 lines
  - Key classes: TemplateOrchestrator, TemplateExtractor

  2. Integrated Orchestrator (prompt_tool/orchestration/):
  - Database-integrated via SQLAlchemy
  - Uses OrchestrationSession model
  - Linked to projects and executions
  - Key modules:
    - orchestrator.py: Core logic (224 lines)
    - session_manager.py: Session CRUD (148 lines)
    - template_processor.py: Template parsing (183 lines)
    - prompt_builder.py: Prompt generation (419 lines)

  Data Flow

  1. User invokes CLI command → prompt_tool/cli.py
  2. Command handler in commands/orchestrate_cmds.py
  3. Business logic in orchestration/orchestrator.py
  4. Database operations via db/db_utils.py
  5. Models defined in db/models.py

  2. Code Conventions Document

  Naming Standards

  Files:
  - Snake_case: orchestrate_cmds.py, template_processor.py
  - Suffix with purpose: *_cmds.py for commands, *_manager.py for managers

  Classes:
  - PascalCase: OrchestrationSession, TemplateEngine
  - Descriptive names: VariantSelector, ExperimentManager

  Functions/Methods:
  - Snake_case: create_planning_session(), extract_variables()
  - Action verbs: validate_template(), render(), process_output()

  Variables:
  - Snake_case: session_id, template_vars
  - Boolean prefix with is/has: is_template, has_errors

  File Organization Patterns

  # Standard module structure
  """Module docstring describing purpose."""

  # Standard library imports
  import os
  from typing import Dict, List, Optional

  # Third-party imports
  from sqlalchemy.orm import Session
  import typer

  # Local imports
  from prompt_tool.db.models import Model
  from prompt_tool.core.utils import helper_function

  # Module code...

  Error Handling Patterns

  # Custom exception usage
  try:
      result = orchestrator.create_planning_session(project_id, feature)
  except ValueError as e:
      console.print(f"[red]Error:[/red] {str(e)}")
      raise typer.Exit(1)

  # Session management with context managers
  with db_manager.session() as session:
      # Database operations
      session.commit()  # Auto-rollback on exception

  Logging Approach

  - Uses Python standard logging module
  - Log levels: DEBUG, INFO, WARNING, ERROR
  - Format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

  3. Feature Integration Points

  Exact Integration Locations

  1. Database Schema Changes
  - File: Create new migration in alembic/versions/
  - Pattern: Follow 99f52dfdd753_add_orchestration_tables.py
  - Add columns to orchestration_sessions table:
  orchestrator_prompt_id = Column(Integer, ForeignKey('prompts.id'))
  analysis_prompt_id = Column(Integer, ForeignKey('prompts.id'))
  implementation_prompt_id = Column(Integer, ForeignKey('prompts.id'))

  2. Model Updates
  - File: prompt_tool/db/models.py:520-559 (OrchestrationSession)
  - Add relationships:
  orchestrator_prompt = relationship("Prompt", foreign_keys=[orchestrator_prompt_id])
  analysis_prompt = relationship("Prompt", foreign_keys=[analysis_prompt_id])
  implementation_prompt = relationship("Prompt", foreign_keys=[implementation_prompt_id])

  3. Template Manager Creation
  - New file: prompt_tool/orchestration/template_manager.py
  - Pattern: Follow ab_testing/experiment_manager.py structure
  - Key methods: create_orchestration_template(), get_default_templates()

  4. CLI Command Updates
  - File: prompt_tool/commands/orchestrate_cmds.py
  - Add new commands at line 200+:
  @app.command()
  def template_list(project: str = typer.Option(...)):
      """List orchestration templates."""

  5. Integration with Existing Template System
  - Use TemplateEngine from prompt_tool/core/templating.py
  - Store templates as Prompt objects with is_template=True
  - Use special category __orchestration__ for organization

  Pattern Conformity Requirements

  Database Operations:
  # Always use db_manager context manager
  with db_manager.session() as session:
      # Use db_ops helpers
      prompt, created = db_ops.get_or_create(
          session, Prompt,
          project_id=project_id,
          name=template_name,
          defaults={"is_template": True}
      )

  CLI Command Structure:
  @app.command()
  def command_name(
      required_arg: str = typer.Argument(..., help="Description"),
      optional_arg: str = typer.Option(None, "--option", "-o", help="Description")
  ):
      """Command description."""
      try:
          with db_manager.session() as session:
              # Implementation
              print_success("Success message")
      except Exception as e:
          handle_command_error(e)

  4. Testing Strategy

  Test Organization

  tests/
  ├── test_orchestration/
  │   ├── test_orchestrator.py         # Unit tests for orchestrator
  │   ├── test_session_manager.py      # Session management tests
  │   ├── test_template_processor.py   # Template processing tests
  │   └── test_integration.py          # End-to-end tests
  ├── conftest.py                      # Global fixtures
  └── fixtures/                        # Test data files

  Testing Patterns

  Unit Test Structure:
  class TestOrchestrationTemplateManager:
      @pytest.fixture
      def manager(self, mock_db_session):
          return OrchestrationTemplateManager(mock_db_session)

      def test_create_template(self, manager):
          # Arrange
          template_content = "Test template {{ variable }}"

          # Act
          result = manager.create_orchestration_template(
              "test", template_content, "analysis"
          )

          # Assert
          assert result.is_template is True
          assert result.name == "orchestration_analysis_test"

  Mock Patterns:
  # Mock database session
  mock_session = MagicMock()
  mock_session.query.return_value.filter_by.return_value.first.return_value = None

  # Mock external services
  with patch('prompt_tool.core.templating.TemplateEngine') as mock_engine:
      mock_engine.render.return_value = "Rendered content"

  Expected Coverage

  - Unit tests: 90%+ coverage for new code
  - Integration tests: Key workflows covered
  - Edge cases: Template validation, missing templates, circular references

  5. Implementation Readiness Checklist

  Prerequisites Confirmed ✓

  - Database migration system working (Alembic)
  - Orchestration tables exist in database
  - Template system (TemplateEngine) functional
  - Prompt versioning system operational
  - A/B testing infrastructure available

  Patterns Identified ✓

  - Database operation patterns via db_utils.DatabaseManager
  - CLI command structure with Typer
  - Model relationships with SQLAlchemy
  - Testing patterns with pytest
  - Error handling conventions

  Integration Points Mapped ✓

  - OrchestrationSession model at line 520
  - Prompt model with template support at line 53
  - TemplateEngine for rendering at core/templating.py
  - CLI commands in commands/orchestrate_cmds.py
  - Database utilities in db/db_utils.py

  Risks Documented ✓

  1. Backward Compatibility Risk
  - Current sessions store templates as text
  - Solution: Keep text fields, add optional prompt references
  - Migration script to convert existing sessions

  2. Template Discovery Complexity
  - Need hierarchy: global → project → feature-type specific
  - Solution: Implement template resolver with precedence rules

  3. Performance Concerns
  - N+1 queries when loading templates
  - Solution: Eager loading with joinedload() in queries

  Implementation Complexity Analysis

  Database Changes: Low complexity (2 hours)
  - Standard migration pattern exists
  - Clear field additions

  Model Updates: Medium complexity (2 hours)
  - Relationships need careful foreign key setup
  - Backward compatibility consideration

  Template Manager: Medium complexity (3 hours)
  - New component but follows existing patterns
  - Integration with TemplateEngine

  CLI Integration: Low complexity (2 hours)
  - Standard command patterns to follow
  - Clear examples in existing commands

  Testing: Medium complexity (3-4 hours)
  - Need comprehensive test coverage
  - Mock complex interactions

  Implementation Blueprint

  File Modifications Required

  1. New Migration (create file):
  alembic/versions/xxx_orchestration_template_system.py
  2. Model Updates (modify):
  prompt_tool/db/models.py:520-559
  3. New Template Manager (create file):
  prompt_tool/orchestration/template_manager.py
  4. Update Orchestrator (modify):
  prompt_tool/orchestration/orchestrator.py:22-85
  5. CLI Commands (modify):
  prompt_tool/commands/orchestrate_cmds.py:200+
  6. Tests (create files):
  tests/test_orchestration/test_template_manager.py
  tests/test_orchestration/test_template_integration.py