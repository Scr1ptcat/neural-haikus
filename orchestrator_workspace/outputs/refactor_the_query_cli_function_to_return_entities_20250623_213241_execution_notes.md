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

  3. **Add configurable switches**
     - `--include-documents`: Include documents when querying docket
     - `--include-comments`: Include comments (implies --include-documents)
     - `--include-attachments`: Include attachments (implies --include-comments)
     - `--depth`: Control traversal depth (0=entity only, -1=all levels)
     - `--format`: Existing pattern for output format
     - `--output-file`: Existing pattern for file export

  4. **Entity route detection**
     - Parse input to detect entity type: "docket:ID", "document:ID", "comment:ID", "attachment:ID"
     - Fall back to auto-detection by trying each entity type
     - Use DeltaTableRegistry to validate entity types

  ## Phase 3: Core Implementation
  [Step-by-step implementation guide]

  1. **Refactor QueryFilter for multi-entity support**
     ```python
     @dataclass
     class UnifiedQueryFilter:
         entity_type: str  # 'docket', 'document', 'comment', 'attachment'
         entity_id: str
         include_documents: bool = False
         include_comments: bool = False
         include_attachments: bool = False
         depth: int = 0
         # ... other existing filters

  2. Implement EntityTraverser class
  class EntityTraverser:
      def __init__(self, ctx: AppContext):
          self.ctx = ctx
          self.schema_manager = ctx.get_schema_manager()

      def traverse_hierarchy(self, entity_type: str, entity_id: str,
                           filter: UnifiedQueryFilter) -> Dict[str, List]:
          """Traverse entity hierarchy based on filter settings"""
          # Implementation following existing get_by_* patterns
  3. Extend QueryBuilder for multi-entity SQL
  class UnifiedQueryBuilder(QueryBuilder):
      def build_entity_query(self, entity_type: str, filter: UnifiedQueryFilter) -> str:
          """Build SQL query for any entity type"""
          # Use DeltaTableRegistry to get table info
          # Follow existing SQL patterns
  4. Create UnifiedResultsHandler
  class UnifiedResultsHandler(QueryResultsHandler):
      def display_hierarchical_results(self, results: Dict[str, List],
                                     format: str, output_file: Optional[str]):
          """Display results maintaining hierarchy"""
          # Follow infrastructure.py display patterns
  5. Update query command
  @click.command()
  @click.argument('entity_spec')  # Format: "docket:EPA-HQ-OAR-2023-0072" or just ID
  @click.option('--include-documents', is_flag=True, help='Include documents')
  @click.option('--include-comments', is_flag=True, help='Include comments (implies documents)')
  @click.option('--include-attachments', is_flag=True, help='Include attachments (implies comments)')
  @click.option('--depth', type=int, default=0, help='Traversal depth (-1 for all)')
  @click.option('--format', type=click.Choice(['table', 'json', 'csv']), default='table')
  @click.option('--output-file', help='Export results to file')
  @pass_context
  def query(ctx, entity_spec, include_documents, include_comments,
           include_attachments, depth, format, output_file):
      """Query entities with hierarchical traversal"""
      # Implementation following existing patterns

  Phase 4: Testing Implementation

  [Comprehensive testing requirements]

  1. Unit tests for new components
    - File: tests/unit/test_unified_query.py
    - Test UnifiedQueryFilter validation
    - Test EntityTraverser with mocked Delta models
    - Test UnifiedQueryBuilder SQL generation
    - Test entity type detection logic
  2. Integration tests
    - File: tests/integration/test_query_command.py
    - Test full hierarchy traversal
    - Test each entity type as entry point
    - Test depth control and include flags
    - Test output formats
  3. CLI tests
    - Update tests/test_cli.sh with new query examples
    - Test backward compatibility with existing query syntax
    - Test error handling for invalid entities
  4. Performance tests
    - Test with large datasets using test docket
    - Verify memory usage with deep traversal
    - Test query optimization

  Phase 5: Documentation and Polish

  - Update docstrings following existing patterns
  - Add examples to query command help text
  - Update CLAUDE.md with new query syntax examples
  - Create migration notes for users of old query command
  - Update README.md if it exists

  Expected Deliverable

  Complete, working implementation of Refactor the query CLI function to return entities against their route. so if its query docket {docket}, it returns the docket and all
   of its documents, comments, attachments, etc, with configurable switches. that:
  - Maintains full backward compatibility
  - Follows all existing Click and Delta Lake patterns
  - Provides intuitive entity traversal with configurable depth
  - Handles all edge cases (missing entities, permissions, etc.)
  - Includes comprehensive test coverage
  - Integrates seamlessly with existing CLI structure

● Update Todos
  ⎿  ☒ Create detailed analysis template for understanding AIRules architecture
     ☒ Create implementation template for refactoring query command
     ☐ Create execution notes with risk assessment and estimates

● EXECUTION_NOTES

  Feature: Refactor the query CLI function to return entities against their route. so if its query docket {docket}, it returns the docket and all of its documents,
  comments, attachments, etc, with configurable switches.
  Complexity: Medium-High
  Estimated Time: 16-20 hours broken down by phase
    - Analysis: 2-3 hours
    - Implementation: 8-10 hours
    - Testing: 4-5 hours
    - Documentation: 2 hours

  Key Risks:
  1. **Performance Impact** (Medium Risk)
     - Deep traversal of large dockets could be slow
     - Mitigation: Implement lazy loading, pagination options, and depth limits

  2. **Backward Compatibility** (Low Risk)
     - Existing query command usage must continue working
     - Mitigation: Keep existing functionality, add new features as extensions

  3. **Memory Usage** (Medium Risk)
     - Loading full hierarchy could exhaust memory
     - Mitigation: Stream results, implement batch processing

  4. **Delta Lake Query Complexity** (Low Risk)
     - Complex joins across multiple tables
     - Mitigation: Use existing model methods, optimize with z-ordering

  Key Files to Focus On:
  - `airules/cli/commands/query.py` - Main implementation file
  - `airules/delta_spark/models/*.py` - Entity models to understand relationships
  - `airules/delta_spark/table_registry.py` - Table configurations
  - `airules/cli/commands/infrastructure.py` - Display patterns reference
  - `tests/unit/test_query_command.py` - Existing test patterns

  Similar Existing Features:
  - `list-tables` command - Shows hierarchical grouping and formatting
  - `stats` command - Shows detailed entity information
  - Current `query` command - Base implementation to extend
  - `get_comments_with_attachments()` - Example of joined data retrieval

  Integration Points:
  - AppContext for accessing schema manager and Spark session
  - DeltaTableRegistry for entity type validation
  - Entity models (Docket, Document, Comment, Attachment) for data access
  - Click decorators and context passing
  - Output formatting utilities

  Testing Strategy:
  - Unit test each new component in isolation
  - Integration test with test docket EPA-HQ-OAR-2023-0072
  - Use CliRunner for CLI testing
  - Mock Spark/Delta operations for fast unit tests
  - Test all combinations of include flags and depth settings
  - Verify output formats (table, JSON, CSV)

  Performance Considerations:
  - Use Spark's lazy evaluation where possible
  - Implement result pagination for large datasets
  - Consider caching for repeated queries
  - Use Delta Lake's data skipping for query optimization
  - Monitor memory usage during deep traversal

  Security Considerations:
  - Validate entity IDs to prevent injection
  - Respect existing access controls (if any)
  - Sanitize output for CSV/JSON export
  - Log access for audit purposes

  Rollback Plan:
  1. Keep existing query command functional during development
  2. Use feature flag or separate command name initially
  3. Git branch protection until feature is stable
  4. Comprehensive test suite before merging
  5. Document rollback procedure in deployment notes
  6. Keep old command available as `query-legacy` if needed

  Additional Notes:
  - Consider adding --limit flag for result pagination
  - Future enhancement: parallel fetching for better performance
  - Consider progress bars for long-running queries
  - May want to add --summary flag for counts only
  - Could add --export-format for different file formats