# Example: Using the Documentation Consolidation Template

## Scenario Examples

### Example 1: Python Project with Scattered Docs
**Situation**: A Python project has README files in every directory, random .txt notes, and some .rst files.

**Template Configuration**:
- `[PROJECT_NAME]` → "DataPipeline"
- `[FILE_EXTENSIONS]` → ".md, .txt, .rst"
- `[EXCLUDE_DIRS]` → "__pycache__, .pytest_cache"
- `[DOC_CATEGORIES]` → Add "Testing Guide, Docker Setup, Data Schemas"
- `[TARGET_STRUCTURE]` → Add "testing.md, docker.md, schemas.md"
- `[SPECIAL_FILES]` → "LICENSE, CHANGELOG.md, CONTRIBUTING.md"
- `[SIZE_LIMIT]` → "150KB"

### Example 2: JavaScript/React Project
**Situation**: Frontend project with component-level READMEs and scattered documentation.

**Template Configuration**:
- `[PROJECT_NAME]` → "E-Commerce UI"
- `[FILE_EXTENSIONS]` → ".md, .mdx"
- `[EXCLUDE_DIRS]` → "build, coverage, .next"
- `[DOC_CATEGORIES]` → Add "Component Library, Styling Guide, State Management"
- `[TARGET_STRUCTURE]` → Add "components.md, styling.md, state-management.md"
- `[SPECIAL_FILES]` → "LICENSE, CODE_OF_CONDUCT.md"
- `[SIZE_LIMIT]` → "200KB"

### Example 3: Microservices Architecture
**Situation**: Multiple services each with their own documentation.

**Template Configuration**:
- `[PROJECT_NAME]` → "OrderSystem"
- `[FILE_EXTENSIONS]` → ".md, .txt, .adoc"
- `[EXCLUDE_DIRS]` → "target, out"
- `[DOC_CATEGORIES]` → Add "Service Catalog, Integration Patterns, Security Policies"
- `[TARGET_STRUCTURE]` → 
  ```
  /docs/
  ├── README.md
  ├── services/
  │   ├── catalog.md
  │   └── integration-patterns.md
  ├── setup.md
  ├── architecture.md
  └── security.md
  ```
- `[SPECIAL_FILES]` → "LICENSE, SECURITY.md"
- `[SIZE_LIMIT]` → "100KB"

## Customization Guidelines

### 1. Adjusting for Project Size

#### Small Projects (< 10 docs)
- Simplify Phase 1 - quick inventory is sufficient
- Merge more aggressively - aim for 3-5 final documents
- Skip the formal report - a simple summary suffices

#### Large Projects (> 100 docs)
- Extend Phase 1 - add automated scanning tools
- Consider more categories to prevent huge files
- Add a migration timeline for gradual consolidation
- Include team assignments for different sections

### 2. Domain-Specific Adaptations

#### For Data Science Projects
Add categories:
- "Data Dictionaries"
- "Model Documentation"
- "Experiment Logs"
- "Notebook Guides"

#### For API-First Projects
Add categories:
- "OpenAPI Specs"
- "Webhook Documentation"
- "Rate Limiting Guides"
- "SDK Documentation"

#### For Enterprise Projects
Add categories:
- "Compliance Documentation"
- "Audit Trails"
- "SLA Documentation"
- "Disaster Recovery"

### 3. Team Size Considerations

#### Solo Developer
- Simplify the process - focus on organization
- Skip team communication steps
- Emphasize future maintainability

#### Large Team (10+)
- Add review stages between phases
- Include stakeholder approval steps
- Create migration training materials
- Plan phased rollout

### 4. Version Control Strategies

#### For Active Projects
```bash
# Create a backup branch before consolidation
git checkout -b pre-consolidation-backup
git checkout main
git checkout -b doc-consolidation

# After consolidation
git commit -m "docs: Consolidate all documentation into /docs directory

- Merged X files into Y consolidated documents
- Removed redundant documentation
- Updated all internal links
- See /docs/consolidation-report.md for details"
```

#### For Legacy Projects
- Consider keeping historical documentation in an archive folder
- Document the "as-of" date for consolidated content
- Preserve important historical context

## Special Situations

### Handling Generated Documentation
If your project has auto-generated docs (e.g., from JSDoc, Sphinx):
1. Keep generation sources in original locations
2. Output generated docs to `/docs/generated/`
3. Reference generated docs from hand-written docs
4. Add generation commands to documentation

### Multi-Language Projects
For projects with multiple programming languages:
1. Consider language-specific subdirectories
2. Or integrate by function rather than language
3. Maintain consistent style across languages

### Documentation in Code
For projects with significant inline documentation:
1. Don't duplicate - reference from /docs
2. Create extraction scripts if needed
3. Link between code docs and /docs

## Quick Start Checklist

1. **Copy the template**
2. **Replace all placeholders** with your project specifics
3. **Review and adjust phases** based on project size
4. **Add any domain-specific categories**
5. **Set realistic size limits**
6. **Plan your timeline**
7. **Communicate with your team**
8. **Execute systematically**

## Red Flags to Watch For

- 🚩 Resistance to delete old files → Create archive branch
- 🚩 Too many categories → Consolidate more aggressively  
- 🚩 Files larger than limit → Split strategically
- 🚩 Broken external links → Create redirect mapping
- 🚩 Missing documentation → Note for future creation

## Success Metrics

Track these to measure consolidation success:
- Time to find information (before vs after)
- Documentation update frequency
- New contributor onboarding time
- Number of "where is X documented?" questions
- Documentation-related issues/PRs

## Final Tips

1. **Take breaks** - Reading all docs is mentally taxing
2. **Use tools** - grep, find, ack for searching
3. **Version control** - Commit frequently during consolidation
4. **Get feedback** - Show draft structure to team early
5. **Be ruthless** - If it's outdated or redundant, remove it
6. **Think ahead** - Design for future growth
