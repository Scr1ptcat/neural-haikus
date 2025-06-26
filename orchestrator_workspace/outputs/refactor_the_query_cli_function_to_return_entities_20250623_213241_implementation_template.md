3. Locate integration points for the new feature
  4. Understand the testing philosophy and approach
  5. Document everything needed for successful implementation

  ## Phase 1: Project Structure Deep Dive
  [Specific areas to investigate based on the feature]
  - CLI command organization in `airules/cli/commands/`
  - Delta Spark models in `airules/delta_spark/models/`
  - Table registry and schema management in `airules/delta_spark/`
  - Current query command implementation in `airules/cli/commands/query.py`
  - Infrastructure commands in `airules/cli/commands/infrastructure.py` for display patterns

  ## Phase 2: Architecture Analysis
  [What architectural aspects to focus on]
  - Click framework patterns with AppContext passing
  - Delta Lake integration with AbstractDeltaModel base class
  - Entity relationships: Docket → Documents → Comments → Attachments
  - QueryBuilder and QueryResultsHandler patterns in current query command
  - DeltaTableRegistry for table management
  - Configuration system in `airules/config.py`
  - Spark session management in `airules/utils/spark_session.py`

  ## Phase 3: Code Standards Discovery
  [Specific patterns to document]
  - Command naming: verb-noun pattern (e.g., list-tables, show-config)
  - CLI decorator pattern: @click.command() with @pass_context
  - Error handling: try/except with click.echo for user messages
  - Progress bars: tqdm for long operations
  - Output formatting: support for table (default), json, csv
  - Class naming: PascalCase with descriptive suffixes (Handler, Builder, Manager)
  - Method naming: snake_case with clear action verbs
  - Import organization: standard library, third-party, local imports

  ## Phase 4: Feature-Specific Investigation
  [Targeted analysis for this feature]
  - Current query command limitations (only queries comments)
  - Entity model methods to leverage:
    - Docket.get_by_id(), Document.get_by_docket()
    - Comment.get_by_document(), Attachment.get_by_comment()
    - Comment.get_comments_with_attachments()
  - Display patterns from infrastructure commands:
    - Table formatting with headers and separators
    - JSON output with proper serialization
    - CSV export capabilities
  - Configurable switches pattern from existing commands (--format, --output-file)
  - Entity type detection from table names in DeltaTableRegistry

  ## Phase 5: Testing Infrastructure
  [Testing approach analysis]
  - Test organization in `tests/unit/` and `tests/integration/`
  - Mock patterns using unittest.mock
  - Test CLI commands with Click's CliRunner
  - Test data fixtures and sample docket IDs
  - Delta table testing with temporary tables
  - Coverage expectations from existing test suites

  ## Expected Deliverable
  A comprehensive analysis document that allows someone to implement Refactor the query CLI function to return entities against their route. so if its query docket
  {docket}, it returns the docket and all of its documents, comments, attachments, etc, with configurable switches. without needing to ask any questions about the codebase.

  Key findings should include:
  - Exact patterns for CLI command implementation
  - Entity traversal logic for hierarchical data retrieval
  - Display formatting patterns to maintain consistency
  - Configuration and switch implementation patterns
  - Testing patterns for CLI commands with Delta Lake integration

● Update Todos
  ⎿  ☒ Create detailed analysis template for understanding AIRules architecture
     ☐ Create implementation template for refactoring query command
     ☐ Create execution notes with risk assessment and estimates

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

  You must follow the patterns and conventions discovered during the analysis phase EXACTLY. No improvements or refactoring - pure feature implementation following existing
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

  2. **Create new unified query system**
     - New class: `UnifiedQueryBuilder` to handle all entity types
     - New class: `EntityTraverser` for hierarchical data retrieval
     - New class: `UnifiedResultsHandler` for consistent display
     - Location: Keep in `airules/cli/commands/query.py` to maintain structure