My Thought Process for Enhancement
Let me explain how I refactored your prompt and why each change makes it more effective:
1. Structured Phases Instead of Vague Instructions
Original Problem: "Please perform a deep analysis of this project and learn it" is too vague.
My Enhancement: Created Phase 1 with specific discovery actions:

Concrete steps (list directories, read README, identify stack)
Verification checkpoints to ensure understanding
Focus on relevant components for the bug

Why: Models perform better with specific, actionable steps rather than abstract goals.
2. Progressive Understanding with Checkpoints
Original Problem: Jumped directly from "learn it" to "fix bug" with no verification.
My Enhancement: Added verification checkpoints after each section:

"Can I explain what this project does?"
"Can I trace how a Spark session is properly obtained?"

Why: Ensures the model actually understands before proceeding, preventing incorrect fixes based on misunderstanding.
3. Reference Pattern Analysis
Original Problem: Mentioned data_sync.py but didn't specify what to learn from it.
My Enhancement: Created detailed steps for studying the reference:

Document HOW it obtains Spark session
Note the specific pattern used
Identify setup/teardown procedures

Why: Explicitly studying the correct pattern prevents the model from guessing at the solution.
4. Incorporated Testing Standards
Original Problem: No mention of testing approach or standards.
My Enhancement:

Added testing infrastructure assessment
Required tests in proper subdirectories
Mandated using run_tests only
Included "fix-first" mentality

Why: Maintains consistency with the testing standards we established earlier.
5. Systematic Bug Analysis
Original Problem: "tries to create its own spark session" doesn't explain why this is wrong.
My Enhancement:

Document the anti-pattern explicitly
Explain WHY it's problematic
Show correct vs incorrect code examples

Why: Understanding the "why" leads to better fixes and prevents similar issues.
6. Structured NLP Analysis
Original Problem: "analyze why they are different" is open-ended.
My Enhancement: Created a comparison matrix approach:

List all variants systematically
Document specific differences
Create decision framework for consolidation

Why: Structured analysis leads to actionable recommendations rather than just observations.
7. Clear Success Criteria
Original Problem: No definition of "done."
My Enhancement: Added comprehensive checklist covering:

Bug fix completion
NLP analysis completion
Code quality standards

Why: Clear success criteria ensure thorough completion and nothing is missed.
8. Anti-Pattern Warnings
Throughout the prompt: Added explicit warnings against:

Creating debugging scripts
Direct SparkSession creation
Skipping failing tests

Why: Proactively prevents common mistakes based on our established standards.
Key Principles I Applied:

Specificity Over Abstraction - Every instruction is concrete and actionable
Verification Before Progress - Checkpoints ensure understanding
Pattern Learning - Study working examples before implementing
Standards Enforcement - Testing and architecture standards woven throughout
Documentation Focus - Every change must be documented
Fix-First Mentality - Problems are fixed, not worked around

This refactored prompt guides the model through a systematic journey from understanding to implementation, ensuring both the bug is properly fixed and the codebase is improved through proper analysis and documentation.
