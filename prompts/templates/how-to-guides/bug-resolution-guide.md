# Example: How to Use the Generic Template

## Original Scenario
"There is a new file in cli.commands named test_nlp.py. In test_nlp, there is a method test_nlp_enhancements() that tries to create its own spark session. It should be inheriting the spark session from the AppContext. Reference data_sync.py as an existing part of the code-base that works."

## Template Mapping

### Placeholders to Replace:
- `[YEARS]` → "10+"
- `[DOMAIN_EXPERTISE]` → "distributed systems and data processing"
- `[SPECIFIC_TECHNOLOGIES]` → "Apache Spark and NLP applications"
- `[BUG_SUMMARY]` → "a critical Spark session management bug"
- `[TARGET_FILE]` → "test_nlp.py"
- `[TARGET_LOCATION]` → "/cli/commands/"
- `[REFERENCE_FILE]` → "data_sync.py"
- `[PROBLEM_PATTERN]` → "creating its own Spark session"
- `[CORRECT_PATTERN]` → "inheriting the Spark session from AppContext"
- `[ANALYSIS_FOCUS]` → "Analyze and rationalize divergent NLP method implementations"

### Technology-Specific Replacements:
- `[Primary Technology]` → "Spark"
- `[Central Component]` → "AppContext"
- `[language]` → "python"

## How to Use This Template

### Step 1: Identify Your Scenario
Break down your bug/task into:
1. **The Problem**: What's broken or needs fixing?
2. **The Anti-Pattern**: What's being done wrong?
3. **The Correct Pattern**: What should be done instead?
4. **Reference Implementation**: Where can we see it done correctly?
5. **Secondary Analysis**: Any additional investigation needed?

### Step 2: Map to Template Placeholders
Create a mapping table like above to ensure consistency throughout the prompt.

### Step 3: Customize Technical Details
- Adjust the expertise section to match the required technologies
- Update verification checkpoints for your specific domain
- Modify test examples to match your testing framework
- Add domain-specific anti-patterns to avoid

### Step 4: Adjust Depth as Needed
- For simpler bugs: Reduce the analysis phases
- For complex systems: Add more component analysis sections
- For multiple bugs: Duplicate Phase 2 for each issue

## Template Variations

### Variation 1: New Feature Development
Replace bug-fixing focus with:
- Requirements analysis phase
- Design pattern selection
- Implementation planning
- Feature testing strategy

### Variation 2: Performance Optimization
Adjust to include:
- Performance baseline measurement
- Bottleneck identification
- Optimization strategies
- Benchmark validation

### Variation 3: Security Audit
Modify to cover:
- Vulnerability assessment
- Security pattern analysis
- Remediation planning
- Security testing

## Tips for Effective Use

1. **Be Specific**: The more specific your placeholders, the better the guidance
2. **Include Examples**: Add code examples in the correct language
3. **Maintain Standards**: Keep testing and documentation standards consistent
4. **Adjust Expertise**: Match the role expertise to the problem domain
5. **Scale Appropriately**: Simple bugs don't need all phases

## Common Customizations

### For Frontend Bugs:
- Change testing focus to component/E2E testing
- Add UI/UX considerations
- Include browser compatibility checks

### For Database Issues:
- Add schema analysis phase
- Include query optimization steps
- Focus on data integrity testing

### For API Problems:
- Include endpoint analysis
- Add contract testing
- Focus on backwards compatibility

### For Infrastructure Issues:
- Add configuration analysis
- Include deployment verification
- Focus on monitoring/logging
