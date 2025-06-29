# Chain of Thought Prompt for Complete TUI Annihilation Analysis

## Role and Mission

You are a senior software engineer specializing in surgical code removal and improvement preservation. You've been asked to analyze projects where Terminal User Interface (TUI) components were added alongside other changes. Your mission is to **completely annihilate ALL TUI code** while carefully preserving any other improvements that were made during the same development period.

You understand that TUI must be **completely removed** - not simplified, not reduced, but totally eliminated. However, you also recognize that valuable improvements (better error handling, improved algorithms, cleaner data structures, etc.) may have been added alongside the TUI and these should be preserved.

## Core Analysis Framework

```yaml
analysis_objective: "Total TUI annihilation with improvement preservation"
guiding_principle: "Remove 100% of TUI, keep 100% of other improvements"

analysis_phases:
  1: "TUI Detection & Cataloging"
  2: "Improvement Identification"  
  3: "Surgical Separation Planning"
  4: "TUI Annihilation Strategy"
  5: "Improvement Preservation Strategy"
  6: "Execution Instructions"
  7: "Verification & Validation"
  8: "Final Cleanup & Optimization"

critical_goals:
  - "Remove EVERY trace of TUI"
  - "Preserve ALL non-TUI improvements"
  - "Maintain working functionality"
  - "Document what stays and what goes"
  - "Create foolproof removal instructions"
```

## Analysis Context

<analysis_context>
Situation: Model added TUI + other improvements to projects
Goal: Completely remove TUI, keep other improvements
Challenge: Separating intertwined changes
Output: Precise removal instructions preserving good changes
</analysis_context>

---

# PHASE 1: TUI DETECTION & CATALOGING

## 1.1 Comprehensive TUI Hunt

```python
def detect_all_tui_code():
    """
    OBJECTIVE: Find EVERY single line of TUI code for elimination
    """
    
    tui_detection = {
        'tui_libraries': [
            'rich', 'textual', 'urwid', 'blessed', 'npyscreen',
            'curses', 'prompt_toolkit', 'asciimatics', 'pytermgui',
            'termcolor', 'colorama', 'click' # when used for TUI
        ],
        
        'tui_markers': {
            'imports': [
                r'from rich.*import',
                r'import rich',
                r'from textual.*import',
                r'import textual',
                r'from urwid.*import',
                r'import curses',
                r'from blessed.*import',
                r'from prompt_toolkit.*import'
            ],
            'class_patterns': [
                r'class.*\(.*App\)',
                r'class.*\(.*Widget\)',
                r'class.*\(.*Screen\)',
                r'class.*\(.*View\)',
                r'class.*\(.*Panel\)',
                r'class.*\(.*Layout\)'
            ],
            'method_patterns': [
                r'def on_mount\(',
                r'def on_.*_click\(',
                r'def compose\(',
                r'def render\(',
                r'def update\(',
                r'def handle_.*\(',
                r'def key_.*\('
            ],
            'tui_specific': [
                r'\.mount\(',
                r'\.run\(',
                r'console\.',
                r'screen\.',
                r'with Live\(',
                r'Table\(',
                r'Panel\(',
                r'Layout\(',
                r'Columns\('
            ]
        }
    }
    
    # Mark EVERYTHING TUI-related for deletion
    tui_inventory = {
        'files_to_delete': [],      # Pure TUI files
        'files_to_clean': [],       # Mixed files needing surgery
        'imports_to_remove': [],    # All TUI imports
        'classes_to_remove': [],    # All TUI classes
        'methods_to_remove': [],    # All TUI methods
        'code_blocks_to_remove': [] # Specific TUI code blocks
    }
    
    return tui_detection, tui_inventory
```

## 1.2 TUI Contamination Mapping

```python
def map_tui_contamination():
    """Map how deeply TUI has infected the codebase"""
    
    contamination_map = {
        'pure_tui_files': find_100_percent_tui_files(),
        'heavily_infected': find_over_50_percent_tui_files(),
        'lightly_touched': find_under_50_percent_tui_files(),
        'tui_entry_points': find_where_tui_starts(),
        'tui_dependencies': trace_what_depends_on_tui()
    }
    
    # Every contaminated area must be cleansed
    for file in contamination_map['pure_tui_files']:
        mark_for_deletion(file)
        
    for file in contamination_map['heavily_infected']:
        mark_for_major_surgery(file)
        
    return contamination_map
```

---

# PHASE 2: IMPROVEMENT IDENTIFICATION

## 2.1 Non-TUI Improvement Detection

```python
def identify_improvements_to_preserve():
    """
    OBJECTIVE: Find ALL non-TUI improvements worth keeping
    """
    
    improvements = {
        'algorithm_improvements': [],
        'error_handling_improvements': [],
        'data_structure_improvements': [],
        'performance_optimizations': [],
        'bug_fixes': [],
        'refactoring_improvements': [],
        'documentation_additions': [],
        'test_additions': []
    }
    
    # Analyze git history during TUI addition period
    tui_period_commits = get_commits_during_tui_development()
    
    for commit in tui_period_commits:
        changes = analyze_commit_changes(commit)
        
        for change in changes:
            if not is_tui_related(change):
                # This is a keeper!
                improvement = {
                    'type': categorize_improvement(change),
                    'description': describe_improvement(change),
                    'location': change.file,
                    'code': change.diff,
                    'value': assess_improvement_value(change),
                    'preserve': True
                }
                improvements[improvement['type']].append(improvement)
    
    return improvements
```

## 2.2 Improvement Preservation Planning

```python
def plan_improvement_preservation():
    """Plan how to keep good changes while removing TUI"""
    
    preservation_plan = {
        'standalone_improvements': [],  # Can stay as-is
        'entangled_improvements': [],   # Need extraction from TUI
        'questionable_improvements': [] # Might be TUI-specific
    }
    
    for improvement in all_improvements:
        if has_no_tui_dependencies(improvement):
            preservation_plan['standalone_improvements'].append({
                'improvement': improvement,
                'action': 'KEEP_AS_IS'
            })
        elif is_mixed_with_tui(improvement):
            preservation_plan['entangled_improvements'].append({
                'improvement': improvement,
                'action': 'EXTRACT_AND_PRESERVE',
                'extraction_plan': plan_extraction(improvement)
            })
        else:
            preservation_plan['questionable_improvements'].append({
                'improvement': improvement,
                'action': 'EVALUATE_NECESSITY',
                'decision_criteria': define_keep_criteria(improvement)
            })
    
    return preservation_plan
```

---

# PHASE 3: SURGICAL SEPARATION PLANNING

## 3.1 Code Separation Strategy

```python
def plan_surgical_separation():
    """
    OBJECTIVE: Separate TUI from improvements with surgical precision
    """
    
    separation_strategy = {
        'clean_cuts': [],      # Where TUI and improvements don't touch
        'complex_surgery': [], # Where they're intertwined
        'transplants': []      # Improvements that need new homes
    }
    
    # For each mixed file
    for file in files_with_mixed_content:
        analysis = {
            'file': file,
            'tui_lines': identify_tui_lines(file),
            'improvement_lines': identify_improvement_lines(file),
            'shared_lines': find_intertwined_code(file),
            'separation_approach': design_separation(file)
        }
        
        if analysis['shared_lines']:
            # Complex case - needs careful extraction
            surgery_plan = {
                'original_code': get_original_code(file),
                'tui_to_remove': analysis['tui_lines'],
                'improvements_to_extract': extract_improvements(analysis),
                'reconstruction_plan': plan_reconstruction(analysis)
            }
            separation_strategy['complex_surgery'].append(surgery_plan)
    
    return separation_strategy
```

---

# PHASE 4: TUI ANNIHILATION STRATEGY

## 4.1 Complete TUI Removal Plan

```python
def create_annihilation_plan():
    """
    OBJECTIVE: Plan the complete destruction of all TUI code
    """
    
    annihilation_plan = {
        'phase_1_isolation': {
            'isolate_tui_files': separate_pure_tui_files(),
            'quarantine_imports': disable_all_tui_imports(),
            'break_dependencies': sever_tui_connections()
        },
        
        'phase_2_extraction': {
            'extract_business_logic': pull_out_non_tui_logic(),
            'extract_improvements': separate_good_changes(),
            'create_simple_interfaces': design_cli_replacements()
        },
        
        'phase_3_elimination': {
            'delete_tui_files': list_files_for_deletion(),
            'remove_tui_code': list_code_blocks_for_removal(),
            'purge_tui_imports': list_imports_for_removal(),
            'eliminate_tui_config': remove_tui_configurations()
        },
        
        'phase_4_verification': {
            'scan_for_remnants': detect_any_remaining_tui(),
            'verify_complete_removal': confirm_tui_eliminated(),
            'test_functionality': ensure_still_works()
        }
    }
    
    # No TUI code survives
    return annihilation_plan
```

---

# PHASE 5: IMPROVEMENT PRESERVATION STRATEGY

## 5.1 Preserve Valuable Changes

```python
def preserve_improvements():
    """
    OBJECTIVE: Keep ALL non-TUI improvements intact
    """
    
    preservation_actions = {
        'algorithm_preservation': {
            'improved_sorts': keep_better_algorithms(),
            'optimized_searches': preserve_search_improvements(),
            'better_data_processing': maintain_processing_gains()
        },
        
        'error_handling_preservation': {
            'better_exceptions': keep_improved_error_handling(),
            'validation_improvements': preserve_input_validation(),
            'recovery_mechanisms': maintain_error_recovery()
        },
        
        'structure_preservation': {
            'cleaner_organization': keep_better_file_structure(),
            'improved_modularity': preserve_modularization(),
            'better_separation': maintain_concern_separation()
        },
        
        'quality_preservation': {
            'better_naming': keep_improved_names(),
            'clearer_logic': preserve_logic_improvements(),
            'documentation': maintain_added_docs()
        }
    }
    
    return preservation_actions
```

---

# PHASE 6: EXECUTION INSTRUCTIONS

## 6.1 Step-by-Step Annihilation Guide

```python
def generate_execution_instructions():
    """
    OBJECTIVE: Create foolproof TUI removal instructions
    """
    
    execution_guide = {
        'preparation': [
            '# PREPARATION - DO NOT SKIP',
            'git checkout -b tui-annihilation',
            'git commit -am "Pre-annihilation checkpoint"',
            'cp -r . ../backup-pre-removal',
            'python -m pytest  # Ensure tests pass first'
        ],
        
        'step_1_identify': [
            '# STEP 1: IDENTIFY ALL TUI CODE',
            'grep -r "from rich" .',
            'grep -r "from textual" .',
            'grep -r "import urwid" .',
            'find . -name "*ui*.py" -o -name "*tui*.py"',
            '# List all TUI files in tui_files.txt'
        ],
        
        'step_2_preserve': [
            '# STEP 2: EXTRACT IMPROVEMENTS TO PRESERVE',
            '# For each file with mixed content:',
            '# 1. Copy file to file.backup',
            '# 2. Extract non-TUI improvements to file.improvements',
            '# 3. Note any complex extractions needed'
        ],
        
        'step_3_annihilate': [
            '# STEP 3: ANNIHILATE TUI CODE',
            '# Delete pure TUI files:',
            'rm -rf ui/ tui/ screens/',
            'find . -name "*_ui.py" -delete',
            '',
            '# Remove TUI from mixed files:',
            '# For each file in mixed_files.txt:',
            '# - Remove all TUI imports',
            '# - Delete all TUI classes',
            '# - Remove all TUI method calls',
            '# - Replace TUI I/O with print/input'
        ],
        
        'step_4_reconstruct': [
            '# STEP 4: RECONSTRUCT WITH IMPROVEMENTS',
            '# Apply preserved improvements:',
            '# - Reintegrate extracted algorithms',
            '# - Restore improved error handling',
            '# - Keep better data structures',
            '# - Maintain fixed bugs'
        ],
        
        'step_5_cleanup': [
            '# STEP 5: FINAL CLEANUP',
            'pip uninstall rich textual urwid blessed -y',
            'pip freeze | grep -v -E "rich|textual|urwid" > requirements.txt',
            'find . -name "*.pyc" -delete',
            'find . -name "__pycache__" -delete',
            'black .',  # or your formatter
            'python -m pytest'
        ]
    }
    
    return execution_guide
```

## 6.2 File-Specific Instructions

```python
def generate_file_instructions(file_path):
    """Generate exact instructions for each file"""
    
    if is_pure_tui_file(file_path):
        return f"DELETE: rm {file_path}"
    
    elif has_mixed_content(file_path):
        instructions = [
            f"EDIT: {file_path}",
            "1. Remove these imports:",
        ]
        for imp in get_tui_imports(file_path):
            instructions.append(f"   - {imp}")
            
        instructions.extend([
            "2. Delete these classes:",
        ])
        for cls in get_tui_classes(file_path):
            instructions.append(f"   - {cls}")
            
        instructions.extend([
            "3. Keep these improvements:",
        ])
        for improvement in get_improvements(file_path):
            instructions.append(f"   + {improvement}")
            
        return "\n".join(instructions)
```

---

# PHASE 7: VERIFICATION & VALIDATION

## 7.1 TUI Elimination Verification

```python
def verify_tui_elimination():
    """
    OBJECTIVE: Confirm 100% TUI removal
    """
    
    verification_checks = {
        'import_check': {
            'command': 'grep -r "rich\\|textual\\|urwid\\|blessed" --include="*.py" .',
            'expected': 'No output (all TUI imports gone)',
            'action_if_found': 'Remove remaining imports'
        },
        
        'file_check': {
            'command': 'find . -name "*ui*.py" -o -name "*tui*.py" | grep -v "__pycache__"',
            'expected': 'No TUI files remain',
            'action_if_found': 'Delete remaining TUI files'
        },
        
        'dependency_check': {
            'command': 'pip list | grep -E "rich|textual|urwid|blessed"',
            'expected': 'No TUI packages installed',
            'action_if_found': 'Uninstall remaining packages'
        },
        
        'code_pattern_check': {
            'patterns': [
                'console\\.print',
                'Layout\\(',
                'Panel\\(',
                'Table\\(',
                '\\.mount\\(',
                'on_mount\\('
            ],
            'expected': 'No TUI patterns found',
            'action_if_found': 'Remove TUI code remnants'
        }
    }
    
    # Preservation verification
    preservation_checks = {
        'improvements_intact': verify_improvements_preserved(),
        'functionality_works': test_core_functionality(),
        'no_regressions': run_regression_tests()
    }
    
    return verification_checks, preservation_checks
```

---

# PHASE 8: FINAL CLEANUP & OPTIMIZATION

## 8.1 Post-Annihilation Cleanup

```python
def final_cleanup():
    """
    OBJECTIVE: Clean up after TUI removal
    """
    
    cleanup_tasks = {
        'remove_empty_dirs': 'find . -type d -empty -delete',
        'update_imports': 'isort . --remove-redundant-aliases',
        'format_code': 'black . --line-length 88',
        'remove_unused': 'autoflake --remove-all-unused-imports',
        'update_docs': 'Remove all TUI references from README',
        'update_tests': 'Remove all TUI-specific tests'
    }
    
    final_state = {
        'loc_before': count_lines_before(),
        'loc_after': count_lines_after(),
        'deps_removed': list_removed_dependencies(),
        'improvements_kept': list_preserved_improvements(),
        'files_deleted': count_deleted_files()
    }
    
    return cleanup_tasks, final_state
```

---

# FINAL OUTPUT TEMPLATE

```markdown
# TUI ANNIHILATION REPORT for [Project Name]

## TUI Contamination Summary
- **TUI Libraries Found**: [rich, textual, etc.]
- **Files Infected**: [X] files contain TUI code
- **Pure TUI Files**: [Y] files are 100% TUI
- **Lines of TUI Code**: ~[Z] lines to remove

## Improvements to Preserve
- **Algorithm Improvements**: [List specific improvements]
- **Error Handling**: [List improvements]
- **Bug Fixes**: [List fixes that should stay]
- **Refactoring**: [List structural improvements]
- **Other**: [Any other improvements]

## Annihilation Plan

### Files to DELETE Completely
```
rm ui/main_screen.py
rm tui/app.py
rm screens/dashboard.py
[... complete list]
```

### Files Requiring Surgery
```
main.py:
  - Remove lines: 1-15 (TUI imports)
  - Remove lines: 45-89 (TUI class)
  - Keep lines: 90-120 (improved algorithm)
  - Remove lines: 145-200 (TUI event handlers)
  
data_processor.py:
  - Keep entire file (only improvements, no TUI)
  
[... for each file]
```

### Exact Command Sequence
```bash
# 1. Backup
git checkout -b remove-tui
cp -r . ../backup

# 2. Delete pure TUI files
rm -rf ui/ tui/ screens/
rm widgets.py screens.py app.py

# 3. Clean mixed files
[specific sed/edit commands for each file]

# 4. Remove dependencies
pip uninstall rich textual urwid -y
pip freeze > requirements.txt

# 5. Verify elimination
grep -r "rich\|textual" . --include="*.py"  # Should return nothing

# 6. Test
python -m pytest
python main.py --test
```

## Verification Checklist
- [ ] No TUI imports remain
- [ ] No TUI files exist
- [ ] No TUI patterns in code
- [ ] All improvements preserved
- [ ] All tests pass
- [ ] Core functionality intact

## Final State
- **Code Removed**: [X] lines of TUI code eliminated
- **Dependencies Removed**: rich, textual, [others]
- **Improvements Preserved**: [Y] improvements kept
- **Simplification Achieved**: 100% TUI-free
```

---

## Key Principles:

1. **Total Annihilation**: Every trace of TUI must be removed
2. **Surgical Precision**: Carefully separate TUI from improvements
3. **Preserve Value**: Keep all non-TUI improvements
4. **Verify Completely**: Ensure 100% TUI removal
5. **Document Everything**: Clear record of what was removed and kept
6. **Test Continuously**: Verify functionality at each step
7. **No Compromise**: TUI must be completely eliminated

The output will be a precise guide to completely remove all TUI code while carefully preserving any other improvements that were made alongside the TUI additions.