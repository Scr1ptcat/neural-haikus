  I've successfully implemented the orchestration template system enhancement for prompt-runner. Here's what was accomplished:

  1. Database Migration (✓ Completed)

  - Created migration 23f95d91cb56_add_orchestration_template_system.py
  - Added columns for prompt references and rendered templates
  - Maintained backward compatibility with existing text fields
  - Successfully applied migration to database

  2. Model Updates (✓ Completed)

  - Updated OrchestrationSession model with:
    - orchestrator_prompt_id, analysis_prompt_id, implementation_prompt_id
    - rendered_orchestrator, rendered_analysis, rendered_implementation
    - template_type for categorization
    - Relationships to Prompt model

  3. OrchestrationTemplateManager (✓ Completed)

  - Created comprehensive template management system
  - Stores templates as Prompt objects with is_template=True
  - Uses special __orchestration__ category
  - Supports CRUD operations, versioning, and rendering
  - Includes default templates for all phases

  4. Orchestrator Updates (✓ Completed)

  - Added use_templates parameter for backward compatibility
  - Integrated template system for all phases (planning, analysis, implementation)
  - Caches template managers per project
  - Falls back to traditional prompts when templates unavailable

  5. CLI Commands (✓ Completed)

  Added comprehensive template management commands:
  - prompt-runner orchestrate template list - List templates
  - prompt-runner orchestrate template show - Show template details
  - prompt-runner orchestrate template add - Add new template
  - prompt-runner orchestrate template update - Update existing template
  - prompt-runner orchestrate template test - Test template rendering

  6. Testing (✓ Completed)

  - Created test_template_manager.py with comprehensive unit tests
  - Created test_template_integration.py for integration testing
  - Updated existing tests for backward compatibility
  - Achieved high test coverage

  7. Standalone Orchestrator Enhancement (✓ Completed)

  - Added --use-db flag to use database templates
  - Added --project parameter for database mode
  - Maintains full backward compatibility
  - Properly manages database connections

  Verification Steps

  1. Run the migration:
  alembic upgrade head
  2. Test template creation:
  prompt-runner orchestrate template add my_template --project myproject --type orchestrator --file template.jinja2
  3. Use templates in orchestration:
  prompt-runner orchestrate plan "Add new feature" --project myproject
  4. Use standalone orchestrator with database:
  python orchestrator.py --use-db --project myproject plan "Add new feature"
  5. Run tests:
  pytest tests/test_orchestration/test_template_manager.py
  pytest tests/test_orchestration/test_template_integration.py

  Key Features Delivered

  1. Backward Compatibility: Existing sessions continue to work with text fields
  2. Template Versioning: Full version history through PromptVersion
  3. A/B Testing Ready: Templates can be used with existing A/B testing infrastructure
  4. Project Scoping: Templates are scoped to projects
  5. Customization: Support for custom templates per project or feature type
  6. Dual System Support: Both file-based and database-based orchestration work seamlessly

  The implementation follows all existing patterns precisely, maintains backward compatibility, and provides a robust foundation for orchestration template management.