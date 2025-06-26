Feature: Orchestration Template System Enhancement
  Complexity: Medium-High
  Estimated Time: 16-20 hours total
  - Analysis: 2-3 hours (understanding dual orchestration systems)
  - Implementation: 10-12 hours
    - Database changes: 2 hours
    - Model updates: 2 hours
    - Template manager: 3 hours
    - Integration: 3 hours
    - CLI commands: 2 hours
  - Testing: 3-4 hours
  - Documentation: 1 hour

  Key Risks:
  1. Backward Compatibility: Existing orchestration sessions must continue working
    - Mitigation: Keep text fields, add new fields as optional
    - Provide migration utility for existing sessions
  2. Dual System Complexity: Two orchestration systems to maintain
    - Mitigation: Focus on integrated system first
    - Add optional database support to standalone orchestrator
  3. Template Discovery: Finding the right template for each use case
    - Mitigation: Implement template hierarchy (global -> project -> custom)
    - Add template metadata for categorization

  Key Files to Focus On:
  - prompt_tool/db/models.py (OrchestrationSession, Prompt models)
  - prompt_tool/orchestration/orchestrator.py (main orchestration logic)
  - prompt_tool/core/templating.py (template engine)
  - orchestrator.py (standalone system)
  - alembic/versions/ (for new migration)
  - prompt_tool/commands/orchestration.py (CLI commands)

  Similar Existing Features:
  - Prompt templates: Already implemented with is_template flag
  - Version control: PromptVersion model provides pattern
  - A/B testing: Existing infrastructure in prompt_tool/ab_testing/
  - Category system: Special categories like orchestration

  Integration Points:
  - OrchestrationSession model: Add prompt references
  - Prompt creation flow: Extend for orchestration templates
  - Template engine: Already supports Jinja2 rendering
  - CLI structure: Add to existing orchestration commands

  Testing Strategy:
  - Unit test each component (models, manager, CLI)
  - Integration test the full workflow
  - Test migration with existing data
  - Performance test template loading at scale
  - Test A/B testing integration

  Performance Considerations:
  - Eager load prompt relationships to avoid N+1 queries
  - Cache compiled templates in memory
  - Index prompt lookups by type and project
  - Consider Redis caching for frequently used templates

  Security Considerations:
  - Validate template content before storage
  - Sanitize variables in template rendering
  - Restrict template modification permissions
  - Audit template changes through versions

  Rollback Plan:
  1. Keep existing text fields functional
  2. Add feature flag for new template system
  3. Provide data export before migration
  4. Test rollback procedure: alembic downgrade -1
  5. Document manual rollback steps