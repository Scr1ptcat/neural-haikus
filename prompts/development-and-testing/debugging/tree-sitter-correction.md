Context
The tree-sitter implementation appears complete but is failing at runtime with import errors. This prompt guides you through systematic debugging and completion of the feature until all tests pass and the feature works correctly.
Error Analysis
Current error:
Error: Required analysis modules not found: cannot import name 'EnhancedComplexityAnalyzer' from 'analysis.tree_sitter'
Debugging and Completion Process
Phase 1: Diagnose the Current State

Verify File Structure
bash# List all files in the tree_sitter module
find analysis/tree_sitter -type f -name "*.py" | sort

# Expected structure:
analysis/
└── tree_sitter/
    ├── __init__.py
    ├── base_analyzer.py
    ├── enhanced_complexity.py  # This seems to be missing
    ├── language_analyzer.py
    └── ...

Check Import Statements

Open analysis/tree_sitter/__init__.py
Verify what is being exported
Check if EnhancedComplexityAnalyzer is defined and exported
Trace where this class should be defined


Identify the Caller

Find where EnhancedComplexityAnalyzer is being imported
Check the expected interface
Understand what the calling code expects



Phase 2: Fix Implementation Issues

Create Missing Components
If EnhancedComplexityAnalyzer doesn't exist, create it:
python# analysis/tree_sitter/enhanced_complexity.py
"""Enhanced complexity analyzer using tree-sitter."""

from typing import Dict, Any, Optional
import logging
from .base_analyzer import TreeSitterAnalyzer

class EnhancedComplexityAnalyzer:
    """Analyze code complexity using tree-sitter parsing."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.analyzers = {}  # Cache for language analyzers
    
    def analyze_file(self, file_path: str) -> Dict[str, Any]:
        """Analyze complexity of a single file."""
        # TODO: Implement actual analysis
        pass

Update init.py
Ensure proper exports:
python# analysis/tree_sitter/__init__.py
from .enhanced_complexity import EnhancedComplexityAnalyzer
from .base_analyzer import TreeSitterAnalyzer

__all__ = ['EnhancedComplexityAnalyzer', 'TreeSitterAnalyzer']

Fix Import Dependencies

Check if tree-sitter is installed: pip list | grep tree-sitter
Install if missing: pip install tree-sitter tree-sitter-languages
Handle optional imports gracefully



Phase 3: Implement Core Functionality

Complete the Implementation
python# Key methods to implement:

def detect_language(self, file_path: str) -> Optional[str]:
    """Detect programming language from file extension."""
    # Map extensions to languages
    
def get_parser(self, language: str):
    """Get or create parser for the language."""
    # Load language library dynamically
    
def analyze_complexity(self, file_path: str) -> Dict[str, Any]:
    """Main analysis entry point."""
    # 1. Read file
    # 2. Detect language
    # 3. Parse with tree-sitter
    # 4. Calculate metrics
    # 5. Return results

Integration Points
Update the main analyze command to use tree-sitter:
python# In the file that imports EnhancedComplexityAnalyzer
try:
    from analysis.tree_sitter import EnhancedComplexityAnalyzer
    TREE_SITTER_AVAILABLE = True
except ImportError as e:
    TREE_SITTER_AVAILABLE = False
    # Log the specific error for debugging


Phase 4: Testing and Validation

Create Minimal Test Case
python# test_minimal.py
"""Minimal test to verify imports work."""

def test_imports():
    """Test that all imports work."""
    try:
        from analysis.tree_sitter import EnhancedComplexityAnalyzer
        analyzer = EnhancedComplexityAnalyzer()
        print("✓ Import successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

if __name__ == "__main__":
    test_imports()

Run Progressive Tests
bash# Test 1: Python imports
python3 -c "from analysis.tree_sitter import EnhancedComplexityAnalyzer"

# Test 2: Basic instantiation
python3 test_minimal.py

# Test 3: CLI without tree-sitter
python3 extract_project.py analyze

# Test 4: CLI with tree-sitter
python3 extract_project.py analyze --use-tree-sitter

Create Integration Test
python# test_integration.py
import tempfile
import os

def test_analyze_simple_file():
    """Test analyzing a simple Python file."""
    # Create test file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write('''
def hello():
    if True:
        return "world"
''')
        test_file = f.name
    
    try:
        # Run analysis
        from analysis.tree_sitter import EnhancedComplexityAnalyzer
        analyzer = EnhancedComplexityAnalyzer()
        result = analyzer.analyze_file(test_file)
        
        # Verify results
        assert result is not None
        print(f"✓ Analysis complete: {result}")
    finally:
        os.unlink(test_file)


Phase 5: Debugging Workflow

When Tests Fail
For each failure:
a. Read the exact error message
b. Identify the failing line of code
c. Add debug logging before the failure
d. Check assumptions (file exists? module imported?)
e. Fix the specific issue
f. Re-run the test
g. Repeat until test passes

Common Issues and Fixes

ImportError: Module not in Python path → Check file location and init.py
AttributeError: Method missing → Implement the method or fix the name
ModuleNotFoundError: Dependency missing → Install with pip
TypeError: Wrong arguments → Check method signatures
FileNotFoundError: Path issues → Use absolute paths for testing



Phase 6: Verification Checklist

Complete Implementation Checklist

 All required files exist in correct locations
 All imports work without errors
 Tree-sitter is properly installed
 Language parsers are installed
 Basic functionality works
 CLI integration works
 Tests pass locally
 Error handling is robust
 Documentation is updated


End-to-End Validation
bash# Clean test
rm -rf __pycache__ analysis/__pycache__ analysis/*/__pycache__

# Run full test suite
python3 -m pytest tests/test_tree_sitter.py -v

# Test on real project
python3 extract_project.py analyze --use-tree-sitter /path/to/test/project


Phase 7: Final Implementation

Complete Missing Features
Based on test results, implement any missing functionality:

Actual tree-sitter parsing
Complexity calculation
Language detection
Error recovery
Performance optimization


Polish and Document

Add helpful error messages
Include usage examples
Document limitations
Add performance metrics



Debugging Commands Toolbox
bash# Check Python path
python3 -c "import sys; print('\n'.join(sys.path))"

# Verify module structure
python3 -c "import analysis.tree_sitter; print(dir(analysis.tree_sitter))"

# Test specific import
python3 -c "from analysis.tree_sitter import EnhancedComplexityAnalyzer"

# Check installed packages
pip list | grep -E "(tree-sitter|project-extractor)"

# Run with debug output
PYTHONPATH=. python3 extract_project.py analyze --use-tree-sitter --debug

# Check for syntax errors
python3 -m py_compile analysis/tree_sitter/*.py
Implementation Strategy

Start with the error: Fix the immediate import issue first
Build incrementally: Get basic imports working before adding features
Test continuously: Run tests after each change
Use print debugging: Add print statements to understand flow
Commit working states: Save progress when something works
Document failures: Keep notes on what didn't work and why

Success Criteria
The implementation is complete when:

python3 extract_project.py analyze --use-tree-sitter runs without errors
It produces meaningful output different from non-tree-sitter analysis
All tests in the test suite pass
The feature gracefully degrades when tree-sitter is not available
Performance is equal to or better than the regex-based approach

Begin Debugging
Start with Phase 1 and work through each phase systematically. Do not skip steps or assume something works without testing it. Each phase builds on the previous one, so ensure each phase is complete before moving on.
Remember: Claims of completion mean nothing without actual working code. Test everything, assume nothing, and verify each step works before proceeding.

Follow this protocol: 

Purpose
This protocol ensures that implementation claims are backed by actual working code. Follow this protocol after ANY implementation to verify functionality.
Validation Rules
Rule 1: No Implementation is Complete Without Proof
Never claim an implementation is complete without showing:

The exact commands you ran
The actual output (not hypothetical)
Evidence of successful execution

Rule 2: Test Every Integration Point
For each feature, test:

Import Test: Can the module be imported?
Unit Test: Does the module work in isolation?
Integration Test: Does it work with the existing system?
CLI Test: Does the command-line interface work?
Error Test: Does it handle errors gracefully?

Validation Steps
Step 1: Show File Creation
bash# Prove files exist
ls -la analysis/tree_sitter/
cat analysis/tree_sitter/__init__.py | head -20
cat analysis/tree_sitter/enhanced_complexity.py | head -30
Step 2: Python Import Test
bash# Test direct import
python3 -c "from analysis.tree_sitter import EnhancedComplexityAnalyzer; print('Import successful')"

# Test module contents
python3 -c "import analysis.tree_sitter; print(dir(analysis.tree_sitter))"
Step 3: Unit Test
python# Create and run minimal_test.py
cat > minimal_test.py << 'EOF'
from analysis.tree_sitter import EnhancedComplexityAnalyzer

try:
    analyzer = EnhancedComplexityAnalyzer()
    result = analyzer.analyze_file(__file__)
    print(f"SUCCESS: Analysis returned: {result}")
except Exception as e:
    print(f"FAILED: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
EOF

python3 minimal_test.py
Step 4: CLI Integration Test
bash# Test original functionality still works
python3 extract_project.py analyze 2>&1 | head -20

# Test new functionality
python3 extract_project.py analyze --use-tree-sitter 2>&1 | head -20

# If error, show exact error
python3 extract_project.py analyze --use-tree-sitter --debug 2>&1
Step 5: Error Handling Test
bash# Test with missing dependencies
python3 -c "import sys; sys.modules['tree_sitter'] = None; from analysis.tree_sitter import EnhancedComplexityAnalyzer"

# Test with invalid input
python3 -c "
from analysis.tree_sitter import EnhancedComplexityAnalyzer
analyzer = EnhancedComplexityAnalyzer()
result = analyzer.analyze_file('nonexistent.py')
print(result)
"
Output Requirements
For Each Test, Show:

Command executed (exact command, not paraphrased)
Full output (including errors)
Exit status: echo $? after each command
Interpretation: What the output means

Example Format:
TEST: Import Module
$ python3 -c "from analysis.tree_sitter import EnhancedComplexityAnalyzer"
[No output - success]
$ echo $?
0
✓ Import successful - module can be loaded

TEST: CLI Integration
$ python3 extract_project.py analyze --use-tree-sitter
[Actual output here, not placeholder]
$ echo $?
0
✓ CLI accepts --use-tree-sitter flag and executes
Common Pitfalls to Avoid

Don't assume file creation = working code

Files might have syntax errors
Imports might be wrong
Integration might be broken


Don't show hypothetical output

Always run the actual commands
Copy-paste real output
Include error messages


Don't skip error cases

Test what happens when things go wrong
Ensure graceful degradation
Verify error messages are helpful


Don't claim "tests pass" without showing them

Run each test
Show the output
Explain any failures



Debugging Protocol
When a test fails:

Show the exact error
bashpython3 extract_project.py analyze --use-tree-sitter 2>&1

Identify the error location
bash# Find the failing line
python3 -c "import traceback; traceback.print_exc()"

Check the specific issue
bash# Is it import error?
python3 -c "import analysis.tree_sitter"

# Is it attribute error?
python3 -c "from analysis.tree_sitter import EnhancedComplexityAnalyzer; print(dir(EnhancedComplexityAnalyzer))"

# Is it file not found?
ls -la analysis/tree_sitter/

Fix and retest

Make the specific fix
Run the same test again
Show it now works



Final Checklist
Before declaring implementation complete:

 All files created and shown to exist
 Import test passes with output shown
 Unit test executes with output shown
 CLI works without new flag (backward compatibility)
 CLI works with new flag
 Error handling demonstrated
 At least one real file analyzed successfully
 No "hypothetical" outputs - all real command results

The Golden Rule
If you haven't shown the actual command and its actual output, it didn't happen.
Sample Validation Report
VALIDATION REPORT: Tree-sitter Integration

1. FILES CREATED:
$ ls -la analysis/tree_sitter/
total 24
drwxr-xr-x 2 user user 4096 Nov 15 10:00 .
drwxr-xr-x 3 user user 4096 Nov 15 10:00 ..
-rw-r--r-- 1 user user  245 Nov 15 10:00 __init__.py
-rw-r--r-- 1 user user 3421 Nov 15 10:00 enhanced_complexity.py
✓ All required files present

2. IMPORT TEST:
$ python3 -c "from analysis.tree_sitter import EnhancedComplexityAnalyzer; print('Success')"
Success
✓ Module imports correctly

3. FUNCTIONALITY TEST:
$ python3 test_minimal.py
Testing basic functionality...
Analysis result: {'file': 'test.py', 'complexity': 1, 'tree_sitter_used': True}
✓ Basic analysis works

4. CLI TEST:
$ python3 extract_project.py analyze --use-tree-sitter
Analyzing project...
Using tree-sitter for enhanced analysis
[... actual output ...]
✓ CLI integration successful

5. ERROR HANDLING:
$ python3 extract_project.py analyze --use-tree-sitter nonexistent/
Error: Directory not found: nonexistent/
✓ Graceful error handling

CONCLUSION: Implementation verified and working
Remember: Trust, but verify. Always verify.
