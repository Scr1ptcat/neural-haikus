Please perform a deep analysis of this project to understand it, then once you have learned the project at a deep level  - fill out this chain of thought prompt template to have a model analyze the following questions with respect to this project:

Your output should be this template filled out and fitted for a model to perform the analysis:

# Generic Template for Iterative Deep Solution Analysis

## Template Instructions
Replace the following placeholders:
- `[YEARS]` - Years of experience (e.g., "10+")
- `[DOMAIN_EXPERTISE]` - Relevant technical domains (e.g., "distributed systems and NLP")
- `[SPECIFIC_TECHNOLOGIES]` - Key technologies (e.g., "Python, TensorFlow, SpaCy")
- `[ANALYSIS_TARGET]` - What you're analyzing (e.g., "two NLP pipeline implementations")
- `[INITIAL_QUESTIONS]` - Starting questions (they will evolve)
- `[PROJECT_CONTEXT]` - What you know about the project (may be wrong)
- `[TIME_BOX]` - How much time you have (affects depth)

---

# Chain of Thought Prompt for Iterative Deep Analysis

## Role and Mission
You are a senior software engineer with [YEARS] years of experience in [DOMAIN_EXPERTISE], specializing in [SPECIFIC_TECHNOLOGIES]. You've been asked to analyze [ANALYSIS_TARGET]. 

But here's the thing: You know that initial questions are often wrong, documentation lies, and real understanding comes from iterative discovery. Your approach will adapt based on what you actually find.

## Your Analysis Philosophy
- **Quick probes before deep dives** - Don't waste time analyzing the wrong things
- **Questions evolve with understanding** - Initial questions are just starting points
- **Reality over documentation** - Code tells the truth, docs tell stories
- **Time-boxed exploration** - Perfect understanding is impossible, good enough is achievable
- **Document the journey** - The path to understanding is as valuable as the destination

## Initial Context (Subject to Change)
"I've been told: [PROJECT_CONTEXT]

Initial questions I've been asked to answer:
[INITIAL_QUESTIONS]

But I know these might change as I learn more. Let me start exploring."

---

## Phase 1: Reality Probe (First 15 minutes)

### 1.1 Quick Reconnaissance
"Before any deep analysis, let me see what I'm actually dealing with."

```bash
# First, does this project even exist as described?
ls -la
# Finding: "Oh, there are 5 different pipeline folders, not 2"

# How big is this thing?
find . -name "*.py" | wc -l
# Finding: "2,847 Python files... this is bigger than expected"

# Is it actively maintained?
git log --oneline -10
# Finding: "Last commit: 'WIP - do not use' ... 8 months ago"

# Quick code quality check
grep -r "TODO\|FIXME\|HACK" . | wc -l
# Finding: "847 TODOs... this might be rough"
```

**Initial Reality Check:**
- Expectation: [What I was told]
- Reality: [What I'm seeing]
- Implication: [How this changes my approach]

### 1.2 Adjust Analysis Scope
"Based on what I'm seeing, I need to adjust my approach."

```python
def revise_analysis_plan():
    """
    My initial understanding was wrong. Adapting...
    """
    original_plan = {
        "analyze": "[ANALYSIS_TARGET]",
        "timeframe": "[TIME_BOX]",
        "depth": "comprehensive"
    }
    
    # Reality check
    actual_situation = {
        "complexity": "higher than expected",
        "code_quality": "concerning",
        "documentation": "minimal",
        "active_development": "abandoned?"
    }
    
    # Revised approach
    revised_plan = {
        "analyze": "core functionality only",
        "timeframe": "need more time or reduce scope",
        "depth": "good enough to answer key questions",
        "new_concerns": ["Is this code even in use?"]
    }
    
    return revised_plan
```

### 1.3 Find the Real Entry Points
"Documentation says one thing, but where does execution actually start?"

```python
# Look for actual usage
grep -r "import pipeline" --include="*.py" | grep -v test
# Finding: "Only imported in deprecated_runner.py"

# Search for main functions
grep -r "if __name__ == '__main__'" --include="*.py"
# Finding: "47 entry points! Which ones matter?"

# Check for tests to understand usage
find . -name "*test*.py" -o -name "test_*" | head
# Finding: "Tests are all skipped with 'TODO: fix after refactor'"
```

**Evolving Understanding:**
- "The 'two pipelines' are actually five different attempts"
- "Nobody seems to be using pipeline_v2.py"
- "The real pipeline might be in 'experimental/new_approach/'"

---

## Phase 2: Iterative Understanding Loops

### 2.1 First Loop: Follow the Execution
"Let me trace through actual execution to understand what really happens."

```python
def trace_execution_path():
    """
    Starting from what seems to be the entry point...
    """
    # Start simple - try to run it
    try:
        from pipeline_v1 import Pipeline
        p = Pipeline()
        # Finding: "ImportError: no module named 'legacy_processor'"
        # Need to understand dependencies first
    except ImportError as e:
        print(f"Can't even import: {e}")
        # New question: What environment does this need?
    
    # Check for setup instructions
    # Finding: "README says 'ask Bob for setup' - Bob left 2 years ago"
    
    # Look for configuration
    # Finding: "Hardcoded paths to /data/prod/... - this is production code?"
```

**New Questions Emerging:**
1. Is this analysis of production code safe?
2. Do I need special permissions/data to understand this?
3. Should I be looking at a different version?

### 2.2 Second Loop: Narrow Focus
"I can't understand everything. What's most important for the original questions?"

```python
def identify_core_differences():
    """
    Forget comprehensive analysis. What are the KEY differences?
    """
    # Quick diff to see scale of differences
    # Finding: "90% of code is identical between versions"
    
    # Focus on the 10% that's different
    core_differences = {
        "algorithm": "v1 uses nltk, v2 uses spacy",
        "data_flow": "v1 is synchronous, v2 attempts async",
        "error_handling": "v1 has none, v2 has... creative solutions"
    }
    
    # New realization: "These aren't versions, they're competing approaches!"
    # This changes everything about how I analyze them
```

### 2.3 Third Loop: Practical Impact
"Given time constraints, what actually matters?"

```python
def focus_on_what_matters():
    """
    I have [TIME_BOX] left. What will actually help?
    """
    critical_questions = {
        "performance": "Quick benchmark instead of deep analysis",
        "correctness": "Check output differences on sample data",
        "maintainability": "Count WTFs per minute while reading",
        "usage": "Find out if anyone actually uses this"
    }
    
    # Pick battles based on what I've learned
    if production_impact == "high":
        focus = "correctness and performance"
    elif team_confusion == "high":
        focus = "clear documentation of differences"
    else:
        focus = "recommendation to deprecate both"
```

---

## Phase 3: Adaptive Deep Dives

### 3.1 Targeted Investigation
"Based on my loops, I now know where to dig deeper."

```python
def deep_dive_where_needed():
    """
    Only diving deep into areas that matter
    """
    # Discovered v1 has a critical performance issue
    # Let me understand just that part
    
    def analyze_v1_bottleneck():
        # Finding: "It's loading a 2GB model for every request!"
        # This explains the performance complaints
        
        # New question: Does v2 fix this?
        # Finding: "V2 caches the model but... incorrectly"
        # Both are broken in different ways!
    
    # Document the specific issue, not everything
    findings = {
        "v1_issue": "Reloads model per request (2GB memory spike)",
        "v2_issue": "Caches model but memory leak (OOM after 100 requests)",
        "recommendation": "Neither is production-ready"
    }
```

### 3.2 Comparison Where Possible
"Some things can't be cleanly compared. Document the mess."

```python
def compare_what_is_comparable():
    """
    Initial plan was a clean comparison table.
    Reality is messier.
    """
    comparison_attempts = {
        "architecture": {
            "v1": "Classic pipeline pattern",
            "v2": "Started as pipeline, evolved into spaghetti",
            "comparable": False,
            "note": "V2 has organic growth problems"
        },
        "performance": {
            "v1": "Slow but predictable (30s/doc)",
            "v2": "Fast then crashes (2s/doc for 100 docs, then OOM)",
            "comparable": "Sort of",
            "note": "Different failure modes"
        },
        "accuracy": {
            "v1": "No tests to verify",
            "v2": "Tests exist but test wrong things",
            "comparable": False,
            "note": "Would need to create test suite"
        }
    }
    
    # Honest conclusion: "These solve different problems poorly"
```

### 3.3 Uncover Hidden Context
"Why do these implementations exist? The code holds clues."

```python
def archaeological_investigation():
    """
    Understanding the 'why' through code archaeology
    """
    # Git blame reveals story
    # Finding: "v1 was intern project, v2 was panic fix for demo"
    
    # Comments tell tales
    # Finding: "# TODO: Fix this properly after demo (2019-03-15)"
    # It's been 5 years...
    
    # Import patterns show evolution
    # Finding: "v2 imports from v1 but overrides half the methods"
    # This isn't a rewrite, it's a monkey patch!
    
    historical_context = {
        "v1": "Intern's learning project that made it to prod",
        "v2": "Emergency 'fix' that became permanent",
        "v3_attempt": "Found abandoned v3 folder - sensible approach",
        "recommendation": "Maybe look at v3 instead?"
    }
```

---

## Phase 4: Synthesis with Reality

### 4.1 Answer Original Questions (If Still Relevant)
"Let me address the original questions with what I've learned."

```markdown
## Original Questions vs Reality

### Q1: [Original question 1]
**Initial assumption**: Two clean implementations to compare
**Reality**: Multiple partial implementations, none production-ready
**Actual answer**: Both have fundamental issues, comparison is moot

### Q2: [Original question 2]
**What I found instead**: The real question should be "Why do we have 5 competing implementations?"
**Answer**: Technical debt from rushed deployments

### Q3: [Original question 3]
**Cannot answer because**: Would need production data access
**What I can say**: Based on code structure, neither scales well
```

### 4.2 Provide What's Actually Useful
"Forget the original analysis request. Here's what you need to know."

```python
def pragmatic_findings():
    """
    What actually matters given what I've discovered
    """
    useful_insights = {
        "immediate_concern": {
            "issue": "Both pipelines have production risks",
            "evidence": "Memory leaks, no error handling",
            "recommendation": "Don't increase traffic to either"
        },
        "practical_path": {
            "option_1": "Fix v2's memory leak (2-3 days)",
            "option_2": "Resurrect abandoned v3 (1-2 weeks)",
            "option_3": "Use external service (immediate)"
        },
        "knowledge_gaps": {
            "need_to_know": "Is this even the right problem to solve?",
            "who_to_ask": "Original requirements lost, check with Product"
        }
    }
    
    return useful_insights
```

### 4.3 Document the Journey
"The path to these findings is as important as the findings."

```markdown
## Analysis Journey Log

### Started with:
- Assumption: Two pipelines to compare
- Time allocated: [TIME_BOX]
- Questions: [INITIAL_QUESTIONS]

### Discovered:
1. **Hour 1**: Not 2 but 5+ implementations
2. **Hour 2**: Production code mixed with experiments
3. **Hour 3**: Both "versions" have critical issues
4. **Hour 4**: Found better abandoned approach (v3)

### Pivoted to:
- Understanding why multiple versions exist
- Identifying production risks
- Finding pragmatic path forward

### Key Insights:
- Technical: Both implementations are fundamentally flawed
- Historical: Rush decisions led to technical debt
- Organizational: No clear ownership or strategy
- Practical: External service might be best option
```

---

## Phase 5: Actionable Output

### 5.1 Recommendations Based on Reality
"Here's what should actually happen based on my analysis."

```python
def realistic_recommendations():
    """
    Not what was asked for, but what's needed
    """
    return {
        "immediate": [
            "Add monitoring to catch memory leaks",
            "Document which pipeline is actually in use",
            "Alert team about production risks"
        ],
        "short_term": [
            "Evaluate external NLP services",
            "Create actual test suite",
            "Document business requirements"
        ],
        "long_term": [
            "Consolidate to single solution",
            "Address technical debt properly",
            "Establish ownership"
        ],
        "questions_for_stakeholders": [
            "What are the actual requirements?",
            "Is custom solution necessary?",
            "Who owns this component?"
        ]
    }
```

### 5.2 What I Couldn't Analyze
"Honest about limitations and unknowns."

```markdown
## Analysis Limitations

### Couldn't analyze:
- Performance under real load (no access to prod data)
- Actual accuracy (no ground truth data)
- Business value (requirements unclear)

### Assumptions I had to make:
- Current code structure reflects current usage
- Git history is reasonably complete
- Comments reflect actual intentions

### What would improve analysis:
- Access to production metrics
- Conversation with original developers
- Clear business requirements
- More time for deeper investigation
```

---

## Success Criteria (Realistic Version)

Analysis is successful when:
- [ ] Key risks are identified (even if not asked about)
- [ ] Practical path forward is clear
- [ ] Stakeholders understand the real situation
- [ ] Time box was respected
- [ ] Findings are actionable (not just interesting)

## Anti-Patterns Avoided

- ❌ **Analysis Paralysis**: Trying to understand everything
- ❌ **Clean Room Analysis**: Ignoring the messy reality
- ❌ **Academic Exercise**: Providing theoretical comparisons
- ❌ **Scope Creep**: Analyzing more than time allows
- ❌ **False Precision**: Detailed analysis of wrong things

## Final Reflection

"I was asked to analyze [ANALYSIS_TARGET]. What I found was [different reality]. The original questions [were/weren't] the right ones. What actually matters is [key insight].

My analysis journey took me from [starting point] to [ending point], discovering [key surprises] along the way. The most valuable finding isn't the technical comparison but [actual insight about the situation].

Time spent: [actual time] vs [TIME_BOX] planned. The deviation was worth it because [reason] / should have stopped earlier because [reason]."

---

**Remember**: Good analysis adapts to what it finds. Great analysis knows when to stop digging and start providing value. The goal isn't complete understanding - it's actionable insight within constraints.
