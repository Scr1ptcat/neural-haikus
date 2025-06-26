Feature: Integrate orchestrator.py into prompt-runner CLI
  Complexity: Medium-High
  Estimated Time: 16-20 hours broken down by phase
    - Analysis: 2-3 hours
    - Implementation: 10-12 hours
    - Testing: 3-4 hours
    - Documentation: 1-2 hours

  Key Risks:
  1. **Database Schema Conflicts**
     - Risk: Migration might conflict with existing schema
     - Mitigation: Careful review of models.py, test migrations on copy

  2. **Template Storage Strategy**
     - Risk: Large templates might not fit well in database
     - Mitigation: Consider TEXT columns or file storage fallback

  3. **Session State Management**
     - Risk: Complex state transitions between orchestration steps
     - Mitigation: Use state machine pattern, extensive testing

  4. **Integration with Workflow System**
     - Risk: Overlap/confusion with existing workflow functionality
     - Mitigation: Clear documentation, distinct use cases

  Key Files to Focus On:
  - prompt_tool/cli.py - Command registration point
  - prompt_tool/commands/workflow_cmds.py - Reference implementation
  - prompt_tool/db/models.py - Database schema
  - prompt_tool/core/config.py - Configuration management
  - prompt_tool/workflows/engine.py - Execution patterns
  - tests/commands/ - Testing patterns
  - orchestrator.py - Source functionality

  Similar Existing Features:
  - Workflow System: Multi-step prompt execution with state
  - Template System: Variable substitution in prompts
  - Batch Operations: Multiple execution handling
  - Project Management: Organizing related work

  Integration Points:
  - CLI Registration: Add to app.add_typer() calls in cli.py
  - Database Models: Extend models.py with new tables
  - Configuration: Add orchestration settings to config
  - Template Storage: Leverage Prompt model or create specialized storage
  - Execution Tracking: Link to ExecutionRecord for history
  - Project Association: Use existing Project relationships

  Testing Strategy:
  - Unit Tests: Test each orchestration component in isolation
  - Integration Tests: Test full planning → analysis → implementation flow
  - CLI Tests: Use Typer's test client for command testing
  - Database Tests: Use transactional fixtures for rollback
  - Mock Strategy: Mock LLM calls, test template processing
  - Coverage Target: Match project's existing coverage (likely 80%+)

  Performance Considerations:
  - Template Caching: Cache parsed templates in memory
  - Database Queries: Use eager loading for session relationships
  - File I/O: Minimize workspace file operations
  - Progress Feedback: Use Rich progress bars for long operations

  Security Considerations:
  - Input Validation: Sanitize feature requests and templates
  - File Paths: Validate workspace paths to prevent traversal
  - Template Injection: Ensure safe template rendering
  - Access Control: Respect project-level permissions

  Rollback Plan:
  1. Database: Alembic down migration ready
  2. Code: Feature branch allows clean revert
  3. Config: No breaking changes to existing config
  4. Data: Sessions table independent, safe to drop

  Implementation Order:
  1. Create database migration for new tables
  2. Implement core orchestration module
  3. Add command group with basic commands
  4. Integrate with existing systems (projects, templates)
  5. Add comprehensive tests
  6. Documentation and examples
  7. Performance optimization if needed

  Success Criteria:
  - All orchestrator.py functionality available via CLI
  - Seamless integration with existing project/workflow system
  - Rich-formatted output matching project style
  - Comprehensive test coverage
  - No breaking changes to existing functionality
  - Clear documentation for users