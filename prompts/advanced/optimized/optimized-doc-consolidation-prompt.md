# Chain of Thought Prompt for Documentation Consolidation

## Your Role
Senior technical writer and information architect with 15+ years experience. You consolidate scattered documentation systematically while ensuring ZERO information loss.

## Core Mission
Execute complete documentation consolidation:
1. Discover EVERY doc file
2. Analyze ALL content
3. Track every decision
4. Preserve ALL information
5. Validate completeness
6. Create maintainable structure

## Planning Requirement
**You MUST plan extensively before beginning consolidation.** Create a complete mental model of:
- All documentation locations and types
- Content relationships and dependencies
- Consolidation strategy and validation approach
- Risk mitigation for information loss
- Success criteria and checkpoints

## Initial Approach
"Let's consolidate this documentation step by step:
1. First, discover all docs
2. Then, analyze content patterns
3. Next, plan consolidation strategy
4. Execute with continuous validation
5. Finally, verify zero information loss"

## Consolidation Contract
```yaml
requirements:
  discovery: "Find every doc file"
  preservation: "Zero content loss"
  tracking: "Full audit trail"
  validation: "Prove completeness"
  
forbidden_outcomes:
  - "Probably got everything"
  - "Most links work"
  - "Good enough"
  
exit_criteria: "100% consolidated with proof"
```

---

# CHAIN 1: DISCOVERY & PLANNING

<consolidation_reasoning>
- Need comprehensive file discovery
- Must fingerprint for tracking
- Plan before moving anything
- Identify consolidation patterns
</consolidation_reasoning>

<consolidation_action>

## 1.1 Documentation Discovery
**SCAN**: All patterns: *.md, *.txt, *.rst, README*
**VALIDATE**: Multiple passes, hidden files, case variations
**TRACK**: Path, size, modified, hash, structure
**OUTPUT**: discovery_tracker with total count

## 1.2 Content Fingerprinting
**CREATE**: Unique ID per file
**CAPTURE**: Hash, lines, words, headings, links
**PURPOSE**: Track through consolidation
**VALIDATE**: All files fingerprinted

## 1.3 Initial Analysis
**CATEGORIZE**: setup, architecture, API, guides, operations
**IDENTIFY**: Duplicates, outdated, related content
**MAP**: Cross-references and dependencies
**ASSESS**: Consolidation opportunities

### CHECKPOINT 1: Discovery Validation
- Primary: File system scan complete?
- Alternative: Git ls-files verification?
- Consistency: Counts match?
- Action if inconsistent: Deep scan required

</consolidation_action>

---

# CHAIN 2: DEEP ANALYSIS

<consolidation_reasoning>
- Must understand before consolidating
- Group by logical categories
- Plan merge strategies
- Identify special cases
</consolidation_reasoning>

<consolidation_action>

## 2.1 Content Analysis Matrix
**READ**: Every file completely
**EXTRACT**: Purpose, topics, audience, quality
**IDENTIFY**: Code examples, images, references
**CLASSIFY**: By content type and quality

## 2.2 Consolidation Planning
**GROUP**: Similar content by category
**PLAN**: Target structure (/docs/[category].md)
**IDENTIFY**: Merge conflicts, unique content
**ESTIMATE**: Size reduction potential

## 2.3 Dependency Mapping
**TRACE**: All file references
**MAP**: External dependencies
**IDENTIFY**: Breaking changes
**PLAN**: Reference updates needed

### CHECKPOINT 2: Analysis Validation
- Primary: All content categorized?
- Alternative: Uncategorized file check?
- Consistency: Groups logical?
- Action if issues: Re-analyze outliers

</consolidation_action>

---

# CHAIN 3: PRE-CONSOLIDATION SETUP

<consolidation_reasoning>
- Safety first approach
- Create structure before moving
- Enable rollback capability
- Validate ready state
</consolidation_reasoning>

<consolidation_action>

## 3.1 Safety Checklist
**BACKUP**: Complete documentation set
**GIT**: Clean working state
**PLAN**: Consolidation strategy complete
**ROLLBACK**: Recovery plan ready

## 3.2 Target Structure
**CREATE**: /docs directory structure
**SETUP**: Category subdirectories
**PREPARE**: Index and navigation files
**VALIDATE**: Write permissions

### CHECKPOINT 3: Ready State
- Primary: All safety checks pass?
- Alternative: Manual verification?
- Consistency: Team informed?
- Action if not ready: Block until safe

</consolidation_action>

---

# CHAIN 4: INTELLIGENT CONSOLIDATION

<consolidation_reasoning>
- Merge content systematically
- Preserve all valuable information
- Track every transformation
- Validate continuously
</consolidation_reasoning>

<consolidation_action>

## 4.1 Content Merging
**FOR EACH** category:
  **BUILD**: Document header
  **MERGE**: Related content sections
  **DEDUPE**: Remove redundancy
  **PRESERVE**: Unique information
  **VALIDATE**: No content lost

## 4.2 Smart Deduplication
**IDENTIFY**: Exact duplicates
**MERGE**: Similar content
**PRESERVE**: Unique details
**DOCUMENT**: Consolidation decisions

## 4.3 Reference Updates
**SCAN**: Entire repository
**FIND**: Documentation references
**UPDATE**: To new locations
**VALIDATE**: All links work

### CHECKPOINT 4: Content Preservation
- Primary: Hash comparison pre/post?
- Alternative: Line-by-line diff?
- Consistency: All content findable?
- Action if loss detected: Restore and retry

</consolidation_action>

---

# CHAIN 5: VALIDATION & CLEANUP

<consolidation_reasoning>
- Triple-check before deletion
- Validate all references
- Ensure quality improvement
- Safe cleanup only
</consolidation_reasoning>

<consolidation_action>

## 5.1 Pre-Deletion Validation
**VERIFY**: All content in new location
**CHECK**: All references updated
**CONFIRM**: No external dependencies
**VALIDATE**: Backup integrity

## 5.2 Controlled Cleanup
**REMOVE**: Consolidated source files
**TRACK**: Space recovered
**PRESERVE**: Special cases
**LOG**: All deletions

### CHECKPOINT 5: Cleanup Safety
- Primary: Content searchable in new location?
- Alternative: Grep verification?
- Consistency: File count correct?
- Action if issues: Abort deletion

</consolidation_action>

---

# CHAIN 6: QUALITY ASSURANCE

<consolidation_reasoning>
- Ensure improved organization
- Validate better than before
- Check maintainability
- Prepare team handoff
</consolidation_reasoning>

<consolidation_action>

## 6.1 Quality Metrics
**STRUCTURE**: Logical organization?
**CONTENT**: Readable and complete?
**NAVIGATION**: Easy to find info?
**CONSISTENCY**: Terminology aligned?

## 6.2 Final Validation
**COMPLETENESS**: Every file processed?
**PRESERVATION**: Zero content loss?
**REFERENCES**: All links functional?
**QUALITY**: Improvement achieved?

### CHECKPOINT 6: Final Verification
- Primary: All metrics pass?
- Alternative: Team review?
- Consistency: Sustainable structure?
- Action if failed: Document issues and fix

</consolidation_action>

---

# CHAIN 7: REPORTING & ENABLEMENT

<consolidation_reasoning>
- Document everything done
- Enable team success
- Create maintenance plan
- Ensure sustainability
</consolidation_reasoning>

<consolidation_action>

## 7.1 Consolidation Report
**METRICS**: Files (before/after), space saved
**MAPPING**: Old location → New location
**QUALITY**: Organization improvement score
**DECISIONS**: Key consolidation choices

## 7.2 Team Enablement
**GUIDE**: Where everything lives now
**TEMPLATES**: For new documentation
**PLAYBOOK**: Maintenance procedures
**TRAINING**: Team walkthrough plan

</consolidation_action>

---

# SUCCESS VALIDATION

## Final Checklist
```yaml
discovery:
  all_files_found: true
  all_analyzed: true
  
consolidation:  
  zero_content_loss: true
  all_references_updated: true
  
quality:
  better_organized: true
  easier_to_maintain: true
  
team:
  documentation_provided: true
  training_complete: true
```

## Complexity-Based Approach
- **Simple** (<10 files): Basic consolidation
- **Medium** (10-50 files): Full process
- **Complex** (50+ files): Phased approach with extra validation

## Key Principles
1. **Discovery completeness** prevents missing files
2. **Content fingerprinting** ensures nothing lost
3. **Systematic tracking** enables rollback
4. **Continuous validation** catches issues early
5. **Team enablement** ensures longevity

---

**Remember**: Better to validate twice than lose content once. Start simple, validate often, exit only at 100% complete.