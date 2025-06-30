# Development and Testing Prompts

This category contains prompts for test development, test improvement, and debugging tasks. These prompts emphasize comprehensive test coverage and systematic debugging approaches.

## 📁 Subcategories

### Test Development
Prompts for creating and improving test suites.

- **comprehensive-test-development.md** (22KB) - Full test architecture development with single entry point design
- **quick-test-development.md** (8KB) - Rapid test creation for immediate coverage
- **improve-test-pass-rate.md** - Systematic approach to fixing failing tests

### Debugging
Specialized debugging and correction prompts.

- **tree-sitter-correction.md** - Debug and fix tree-sitter parser implementations

## 🎯 When to Use These Prompts

### Test Development Prompts
- **comprehensive-test-development.md** when:
  - Building test suite from scratch
  - Refactoring test architecture
  - Implementing test best practices
  - Need single entry point design

- **quick-test-development.md** when:
  - Need tests quickly
  - Working on small features
  - Time-constrained situations
  - Prototype validation

- **improve-test-pass-rate.md** when:
  - Tests are failing
  - CI/CD pipeline is red
  - Refactoring broke tests
  - Upgrading dependencies

### Debugging Prompts
- **tree-sitter-correction.md** when:
  - Implementing parsers
  - Working with ASTs
  - Tree-sitter specific issues

## 🔑 Key Principles

All development and testing prompts follow:
1. **Test-first thinking** - Consider tests before implementation
2. **Single entry point** - One main test runner
3. **Clear assertions** - Explicit, readable test expectations
4. **Isolated tests** - No interdependencies
5. **Fast feedback** - Quick test execution

## 💡 Testing Best Practices

These prompts emphasize:
- **Descriptive test names** that explain what and why
- **Arrange-Act-Assert** pattern
- **Test data builders** for maintainability
- **Mocking at boundaries** only
- **Integration over unit** tests when practical

## 📊 Prompt Comparison

| Prompt | Use Case | Output | Complexity |
|--------|----------|--------|------------|
| comprehensive-test-development | Full test suite | Complete architecture | High |
| quick-test-development | Rapid coverage | Basic tests | Low |
| improve-test-pass-rate | Fix failures | Working tests | Medium |
| tree-sitter-correction | Parser debugging | Fixed implementation | High |

## 🔄 Recommended Workflow

1. **New Project**: Start with `comprehensive-test-development.md`
2. **Existing Project**: Use `quick-test-development.md` for immediate coverage
3. **Failing Tests**: Apply `improve-test-pass-rate.md`
4. **Specific Issues**: Use specialized debugging prompts

## 🚀 Test Architecture Features

The comprehensive prompt creates:
- Single `run_tests.py` entry point
- Automatic test discovery
- Configurable test execution
- Clean test organization
- Shared fixtures/utilities
- Performance benchmarks
- Coverage reporting

## ⚡ Quick Testing Tips

1. **Start simple** - Basic tests are better than no tests
2. **Test behaviors** - Not implementation details
3. **Use descriptive names** - Tests document the code
4. **Keep tests fast** - Slow tests won't be run
5. **Test edge cases** - Happy path isn't enough

These prompts help create maintainable, comprehensive test suites that give confidence in code changes.