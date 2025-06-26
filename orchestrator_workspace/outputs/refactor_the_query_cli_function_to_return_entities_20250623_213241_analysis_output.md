  ● IMPLEMENTATION_TEMPLATE

    # Role: Senior Software Engineer

    You are a senior software engineer with deep expertise in building production-ready features. You have:
    - 15+ years of experience in software development
    - Expertise in maintaining code quality and consistency
    - Strong focus on testing and documentation
    - Ability to implement complex features while following existing patterns perfectly

    ## Your Mission
    Implement the feature: Refactor the query CLI function to return entities against their route. so if its query docket {docket}, it returns the docket and all of its
    documents, comments, attachments, etc, with configurable switches.

    You must follow the patterns and conventions discovered during the analysis phase EXACTLY. No improvements or refactoring - pure feature implementation following
  existing
     patterns.

    ## Implementation Constraints
    - Follow existing patterns precisely
    - Minimize changes to existing code
    - Write comprehensive tests
    - Document all decisions
    - Handle errors consistently with the project
    - Maintain backward compatibility

    ## Phase 1: Pre-Implementation Setup
    - Review analysis findings
    - Set up development environment with AIRules
    - Verify Spark and Delta Lake are working
    - Create feature branch: `git checkout -b feature/unified-query-command`
    - Run existing tests to ensure baseline: `./tests/run_all_tests.sh`

    ## Phase 2: Implementation Planning
    [Detailed breakdown based on feature requirements]

    1. **Refactor existing query.py command**
       - Keep existing comment-specific functionality as legacy support
       - Extract common query patterns into reusable components
       - File: `airules/cli/commands/query.py`

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

  Remember: Your analysis will be the only guide for implementation. Make it comprehensive.

✻ Thinking…

  The user wants me to execute a deep analysis of the AIRules codebase to prepare for implementing a refactored query CLI function. I need to follow the analysis template
  methodically, examining the codebase and documenting my findings in detail.

  Let me start with Phase 1: Project Structure Deep Dive.

● I'll execute a comprehensive analysis of the AIRules codebase following the template. Let me start by exploring the project structure systematically.

● Task(Analyze CLI command organization)
  ⎿  Done (7 tool uses · 29.1k tokens · 1m 12.4s)

✻ Thinking…

  Good, I've got a comprehensive understanding of the CLI structure. Now let me move to analyzing the Delta Spark models and entity relationships.

● Task(Analyze Delta Spark models and relationships)
  ⎿  Done (12 tool uses · 54.4k tokens · 2m 1.9s)

✻ Thinking…

  Excellent, I now have a deep understanding of the entity models and relationships. Let me continue with analyzing the current query command implementation and how it
  works.

● Task(Analyze current query command implementation)
  ⎿  Done (11 tool uses · 31.8k tokens · 1m 39.0s)

✻ Thinking…

  Good, I have a thorough understanding of the current query implementation. Now let me analyze the display patterns from infrastructure commands to understand how results
  should be formatted in the new unified query.

● Task(Analyze display patterns and testing infrastructure)
  ⎿  Done (15 tool uses · 36.3k tokens · 1m 49.0s)

✻ Thinking…

  Now I have comprehensive information about the codebase. Let me compile a final analysis document that brings together all my findings into a complete deliverable.

● Task(Compile final comprehensive analysis)
  ⎿  Done (4 tool uses · 32.1k tokens · 4m 35.6s)

✻ Thinking…

  Now let me create the final comprehensive analysis document that brings together all my findings in a structured format.

● Comprehensive Analysis: AIRules Query Command Refactoring

  1. Architecture Overview

  System Architecture

  The AIRules system follows a layered architecture with clear separation of concerns:

  ┌─────────────────────────────────────────────────────────┐
  │                    CLI Layer                            │
  │  (airules/cli/__init__.py, commands/*.py)              │
  ├─────────────────────────────────────────────────────────┤
  │                 Business Logic Layer                    │
  │  (airules/analysis/*, airules/pipelines/*)             │
  ├─────────────────────────────────────────────────────────┤
  │                  Data Access Layer                      │
  │  (airules/delta_spark/models/*)                        │
  ├─────────────────────────────────────────────────────────┤
  │              Delta Lake / Spark Layer                   │
  │  (airules/delta_spark/base.py, utils/spark_session.py) │
  └─────────────────────────────────────────────────────────┘

  Component Organization

  - CLI Commands: /airules/cli/commands/ - Each command in separate file
  - Data Models: /airules/delta_spark/models/ - One model per entity
  - Configuration: /airules/config.py - Centralized config management
  - Table Registry: /airules/delta_spark/delta_table_registry.py - Table metadata
  - Utilities: /airules/utils/ - Shared utilities (logging, spark, config)

  Data Flow Pattern

  1. CLI command receives user input
  2. Command validates and creates AppContext
  3. AppContext provides Spark session and schema manager
  4. Data models query Delta tables using Spark SQL
  5. Results formatted and displayed based on output format

  2. Code Conventions Document

  Naming Standards

  - Commands: Verb-noun pattern (list-tables, show-config)
  - Classes: PascalCase with descriptive suffixes (QueryBuilder, ResultsHandler)
  - Methods: snake_case with action verbs (get_by_id, build_query)
  - Files: snake_case matching content (query.py, delta_operations.py)

  File Organization Pattern

  # Standard import order (from any command file)
  import sys
  import logging
  from typing import List, Optional, Dict
  from dataclasses import dataclass

  import click
  from pyspark.sql import DataFrame
  from tqdm import tqdm

  from airules.cli.common import AppContext, pass_context
  from airules.delta_spark.models import Comment
  from airules.utils.logging_utils import log_exception

  Command Structure Pattern

  @click.command()
  @click.argument("entity_id")
  @click.option("--format", type=click.Choice(["table", "json", "csv"]), default="table")
  @click.option("--limit", type=int, default=100, help="Maximum results")
  @pass_context
  def command_name(ctx: AppContext, entity_id: str, format: str, limit: int):
      """Command description for help text."""
      logger = logging.getLogger(__name__)

      try:
          # Initialize resources
          spark = ctx.get_spark()
          schema_manager = ctx.get_schema_manager()

          # Validate input
          if not entity_id:
              raise click.BadParameter("Entity ID required")

          # Execute logic
          # ...

          # Display results
          click.echo(f"✓ Operation completed successfully")

      except Exception as e:
          logger.error(f"Failed to execute: {str(e)}")
          if ctx.debug:
              log_exception(logger, e, "command_name")
          sys.exit(1)
      finally:
          ctx.cleanup()

  Error Handling Pattern

  # From airules/analysis/nlp/nlp_analyzer.py
  try:
      # Operation
      result = perform_operation()
  except ValueError as e:
      logger.error(f"Invalid value: {str(e)}")
      raise click.ClickException(str(e))
  except Exception as e:
      logger.error(f"Unexpected error: {str(e)}")
      if debug_mode:
          log_exception(logger, e, "operation_name")
      raise

  Delta Table Access Pattern

  # From airules/delta_spark/models/comments.py
  class Comment(AbstractDeltaModel):
      def get_by_docket(self, docket_id: str) -> DataFrame:
          """Get all comments for a docket."""
          table_name = self._get_qualified_table_name()
          query = f"""
          SELECT * FROM {table_name}
          WHERE docket_id = '{docket_id}'
          ORDER BY posted_date DESC
          """
          return self.spark.sql(query)

  3. Feature Integration Points

  Primary Integration Points

  1. CLI Command Registration (airules/cli/init.py:173)
  # Add after existing commands
  cli.add_command(query)  # Enhanced unified query
  2. Query Command Enhancement (airules/cli/commands/query.py)
    - Extend existing QueryFilter dataclass
    - Enhance QueryBuilder for multi-table support
    - Update QueryResultsHandler for hierarchical display
  3. Entity Model Integration
    - Use existing methods: Docket.get_by_id(), Document.get_by_docket()
    - Leverage Comment.get_comments_with_attachments() for joins
    - Utilize Attachment.get_all_by_docket() with include_comment_columns
  4. Table Registry Usage (airules/delta_spark/delta_table_registry.py:120)
  # Get table info for dynamic queries
  table_config = registry.get_table("comments")
  schema = table_config.schema
  5. Display Integration (Following infrastructure.py patterns)
  # Hierarchical display
  click.echo("DOCKET INFORMATION:")
  click.echo("-" * 50)
  click.echo(f"  📊 {docket_id}")
  click.echo(f"     Title: {title}")
  click.echo()
  click.echo("DOCUMENTS:")
  # ... continue hierarchy

  Configuration Points

  - Environment detection: ctx.environment (local/databricks)
  - Debug mode: ctx.debug for verbose output
  - Config overrides: ctx.config for custom settings

  4. Testing Strategy

  Test Organization

  tests/
  ├── unit/
  │   ├── test_unified_query.py      # New test file
  │   ├── test_query_builder.py      # Test query building
  │   └── test_entity_traverser.py   # Test traversal logic
  ├── integration/
  │   └── test_query_integration.py  # End-to-end tests
  └── fixtures/
      └── query_fixtures.py          # Test data

  Unit Testing Pattern

  # From existing test patterns
  import unittest
  from unittest.mock import Mock, patch
  from click.testing import CliRunner

  class TestUnifiedQuery(unittest.TestCase):
      def setUp(self):
          self.runner = CliRunner()
          self.mock_ctx = Mock(spec=AppContext)
          self.mock_spark = Mock()
          self.mock_ctx.get_spark.return_value = self.mock_spark

      def test_query_docket_basic(self):
          # Mock data
          mock_docket_df = Mock()
          mock_docket_df.collect.return_value = [Row(docket_id="EPA-123")]

          # Execute
          result = self.runner.invoke(
              query,
              ['docket:EPA-123'],
              obj=self.mock_ctx
          )

          # Assert
          assert result.exit_code == 0
          assert "EPA-123" in result.output

  Integration Testing Pattern

  @pytest.mark.integration
  def test_full_hierarchy_query(spark_session, temp_delta_path):
      """Test querying full entity hierarchy."""
      # Setup test data
      create_test_docket(spark_session, temp_delta_path)

      # Execute query
      result = query_entities(
          "docket:TEST-123",
          include_all=True,
          spark=spark_session
      )

      # Verify hierarchy
      assert len(result["documents"]) > 0
      assert len(result["comments"]) > 0
      assert len(result["attachments"]) > 0

  Mock Patterns

  - Mock Spark DataFrames: Return Mock() with .collect() method
  - Mock Schema Manager: Return table existence checks
  - Mock File I/O: Use StringIO for CSV exports
  - Mock Progress Bars: Disable in tests with disable=True

  5. Implementation Readiness Checklist

  Prerequisites Confirmed ✓

  - CLI command structure understood (Click framework)
  - Delta Lake model patterns documented
  - Entity relationships mapped
  - Display formatting patterns identified
  - Testing patterns analyzed

  Patterns Identified ✓

  - Command registration pattern in cli/init.py
  - AppContext usage for dependency injection
  - SQL query building with proper escaping
  - Multi-format output support (table/json/csv)
  - Error handling and logging conventions

  Integration Points Mapped ✓

  - Where to add new command: /airules/cli/commands/query.py
  - How to access entities: Through model classes in /airules/delta_spark/models/
  - Display formatting: Follow infrastructure.py patterns
  - Configuration: Use AppContext and config.py
  - Testing: Add to /tests/unit/ and /tests/integration/

  Risks Documented ✓

  - Performance with deep traversal (Mitigation: pagination, limits)
  - Memory usage with large results (Mitigation: streaming, batching)
  - Complex SQL generation (Mitigation: use existing patterns)
  - Backward compatibility (Mitigation: extend, don't replace)

  Implementation Approach ✓

  1. Phase 1: Extend QueryFilter for multi-entity support
  2. Phase 2: Create EntityTraverser using existing model methods
  3. Phase 3: Enhance QueryBuilder for dynamic joins
  4. Phase 4: Update ResultsHandler for hierarchical display
  5. Phase 5: Add comprehensive tests following existing patterns

  Key Takeaways

  The AIRules codebase is well-structured with clear patterns that make extending the query functionality straightforward:

  1. Use existing infrastructure: The models already have the methods needed
  2. Follow established patterns: Command structure, error handling, and display formats are consistent
  3. Leverage the type system: Delta tables have schemas that can guide implementation
  4. Test comprehensively: The existing test patterns show how to mock Spark operations effectively
  5. Maintain compatibility: Extend the existing query command rather than replacing it