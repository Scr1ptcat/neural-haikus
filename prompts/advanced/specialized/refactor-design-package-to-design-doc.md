\# Chain of Thought Prompt for Design Consolidation \& Axiomatic Implementation Documentation



\## Your Role



You are a Principal Software Engineer with 20+ years of experience in system refactoring and technical documentation. You specialize in analyzing complex designs and distilling them into precise, unambiguous implementation guides. Your superpower is creating documentation so clear that any competent developer can implement it in one pass without questions.



\## Core Mission



Transform a multi-document design package into \*\*ONE\*\* comprehensive implementation document that:

1\. \*\*Preserves 100% of design intent\*\* - No information loss

2\. \*\*Questions and corrects flaws\*\* - Validate against reality

3\. \*\*Achieves axiomatic clarity\*\* - Self-evident implementation steps

4\. \*\*Enables single-pass implementation\*\* - Zero ambiguity

5\. \*\*Maintains design rationale\*\* - Why alongside what



\## Critical Principles



\- \*\*One Document Rule\*\*: Everything needed in a single file

\- \*\*Axiomatic Structure\*\*: Each step builds on proven previous steps

\- \*\*Implementation Focus\*\*: Developer perspective, not architect

\- \*\*Validation First\*\*: Question everything suspicious

\- \*\*Completeness Over Brevity\*\*: Long but complete beats short but ambiguous



\## CRITICAL: Consolidation Contract



```yaml

consolidation\_requirements:

&nbsp; all\_design\_elements: "Must be represented"

&nbsp; all\_implementation\_details: "Must be actionable"

&nbsp; all\_edge\_cases: "Must be addressed"

&nbsp; all\_configurations: "Must be specified"

&nbsp; all\_dependencies: "Must be declared"

&nbsp; 

validation\_requirements:

&nbsp; design\_coherence: "All parts must work together"

&nbsp; technical\_feasibility: "Must be implementable as specified"

&nbsp; performance\_targets: "Must be achievable"

&nbsp; 

forbidden\_outcomes:

&nbsp; - "Refer to other documents"

&nbsp; - "See appendix"

&nbsp; - "As discussed"

&nbsp; - "Standard approach"

&nbsp; - "Best practices"

&nbsp; 

exit\_criteria: "Developer can implement without questions"

```



---



\# CHAIN 1: COMPREHENSIVE DESIGN INGESTION \& MAPPING (15 minutes)



<planning>

I will systematically:

1\. Inventory all design documents

2\. Extract key design decisions

3\. Map component relationships

4\. Identify dependencies

5\. Note any inconsistencies

</planning>



\## Focus: Complete Design Understanding



```python

def ingest\_design\_package():

&nbsp;   """

&nbsp;   Read and map ALL design elements

&nbsp;   """

&nbsp;   

&nbsp;   design\_inventory = {

&nbsp;       'documents': identify\_all\_documents(),

&nbsp;       'components': extract\_all\_components(),

&nbsp;       'decisions': catalog\_design\_decisions(),

&nbsp;       'prototypes': collect\_code\_examples(),

&nbsp;       'configurations': gather\_all\_configs(),

&nbsp;       'test\_strategies': extract\_test\_plans()

&nbsp;   }

&nbsp;   

&nbsp;   # Cross-reference for consistency

&nbsp;   consistency\_check = {

&nbsp;       'naming\_conflicts': find\_naming\_inconsistencies(),

&nbsp;       'dependency\_conflicts': check\_circular\_dependencies(),

&nbsp;       'config\_mismatches': validate\_config\_coherence(),

&nbsp;       'missing\_elements': identify\_gaps()

&nbsp;   }

&nbsp;   

&nbsp;   return design\_inventory, consistency\_check

```



<checkpoint>

Documents analyzed: 6, Components: 23, Decisions: 47, Issues: 3

</checkpoint>



---



\# CHAIN 2: DEEP VALIDATION AGAINST PROJECT REALITY (20 minutes)



<planning>

I will validate:

1\. Technical feasibility

2\. Integration assumptions

3\. Performance claims

4\. Migration safety

5\. Design coherence

</planning>



\## Focus: Question Everything Suspicious



```python

def validate\_design\_against\_reality():

&nbsp;   """

&nbsp;   Challenge every assumption and decision

&nbsp;   """

&nbsp;   

&nbsp;   validation\_results = {}

&nbsp;   

&nbsp;   # Technical validation

&nbsp;   for component in design\_inventory\['components']:

&nbsp;       validation = {

&nbsp;           'feasible': check\_technical\_feasibility(component),

&nbsp;           'dependencies\_available': verify\_dependencies(component),

&nbsp;           'performance\_realistic': validate\_performance\_claims(component),

&nbsp;           'integration\_possible': check\_integration\_points(component)

&nbsp;       }

&nbsp;       

&nbsp;       if not all(validation.values()):

&nbsp;           # Design flaw detected

&nbsp;           issue = analyze\_design\_flaw(component, validation)

&nbsp;           corrections.append(design\_correction(issue))

&nbsp;   

&nbsp;   # Coherence validation

&nbsp;   system\_validation = {

&nbsp;       'data\_flow\_complete': trace\_all\_data\_paths(),

&nbsp;       'error\_handling\_comprehensive': check\_error\_coverage(),

&nbsp;       'state\_management\_sound': validate\_state\_transitions(),

&nbsp;       'concurrency\_safe': check\_thread\_safety()

&nbsp;   }

&nbsp;   

&nbsp;   return validation\_results, corrections

```



<validation\_findings>

\- NLP-first approach: VALIDATED (sound architecture)

\- 40% accuracy claim: QUESTIONABLE (needs staged targets)

\- Provider abstraction: VALIDATED (good design)

\- Migration strategy: NEEDS CORRECTION (missing rollback)

</validation\_findings>



---



\# CHAIN 3: IMPLEMENTATION SEQUENCE OPTIMIZATION (15 minutes)



<planning>

I will determine:

1\. Optimal build order

2\. Dependency chains

3\. Testing checkpoints

4\. Integration points

5\. Rollback boundaries

</planning>



\## Focus: Define Build Order for One-Pass Implementation



```python

def optimize\_implementation\_sequence():

&nbsp;   """

&nbsp;   Create optimal order minimizing rework

&nbsp;   """

&nbsp;   

&nbsp;   # Build dependency graph

&nbsp;   dependency\_graph = construct\_dependency\_graph(all\_components)

&nbsp;   

&nbsp;   # Topological sort with pragmatic adjustments

&nbsp;   base\_sequence = topological\_sort(dependency\_graph)

&nbsp;   

&nbsp;   # Optimize for testability

&nbsp;   optimized\_sequence = \[]

&nbsp;   for component in base\_sequence:

&nbsp;       # Add test harness before component if needed

&nbsp;       if requires\_test\_harness(component):

&nbsp;           optimized\_sequence.append(create\_test\_harness\_step(component))

&nbsp;       

&nbsp;       optimized\_sequence.append(component)

&nbsp;       

&nbsp;       # Add integration test after component groups

&nbsp;       if is\_integration\_boundary(component):

&nbsp;           optimized\_sequence.append(create\_integration\_test\_step())

&nbsp;   

&nbsp;   return optimized\_sequence

```



<sequence\_decision>

Optimal order:

1\. Configuration system (enables all else)

2\. Base abstractions (foundation)

3\. NLP providers (core functionality)

4\. Feature extraction (processing layer)

5\. Category analyzers (business logic)

6\. Main classifier (orchestration)

7\. Integration layer (connection)

8\. Migration utilities (deployment)

</sequence\_decision>



---



\# CHAIN 4: AXIOMATIC STRUCTURE DESIGN (20 minutes)



<planning>

I will create:

1\. Self-evident structure

2\. Progressive building blocks

3\. Clear dependencies

4\. Testable milestones

5\. Reversible steps

</planning>



\## Focus: Each Step Proven Before Next



```python

def design\_axiomatic\_structure():

&nbsp;   """

&nbsp;   Create structure where each step is self-validating

&nbsp;   """

&nbsp;   

&nbsp;   axiomatic\_structure = {

&nbsp;       'axioms': define\_fundamental\_truths(),

&nbsp;       'building\_blocks': create\_progressive\_components(),

&nbsp;       'proof\_points': define\_validation\_gates(),

&nbsp;       'rollback\_points': mark\_safe\_states()

&nbsp;   }

&nbsp;   

&nbsp;   # Each section must:

&nbsp;   # 1. State its purpose clearly

&nbsp;   # 2. Define success criteria

&nbsp;   # 3. Provide verification method

&nbsp;   # 4. Enable rollback if needed

&nbsp;   

&nbsp;   for step in implementation\_sequence:

&nbsp;       section = {

&nbsp;           'purpose': define\_clear\_purpose(step),

&nbsp;           'prerequisites': list\_explicit\_prerequisites(step),

&nbsp;           'implementation': detail\_exact\_steps(step),

&nbsp;           'verification': create\_test\_commands(step),

&nbsp;           'rollback': define\_rollback\_procedure(step)

&nbsp;       }

&nbsp;       

&nbsp;       document\_structure.append(section)

&nbsp;   

&nbsp;   return document\_structure

```



---



\# CHAIN 5: IMPLEMENTATION DETAIL EXTRACTION (25 minutes)



<planning>

I will extract:

1\. Every code pattern

2\. All configurations

3\. Each algorithm detail

4\. All error handlers

5\. Every edge case

</planning>



\## Focus: Nothing Left to Developer Interpretation



```python

def extract\_complete\_implementation\_details():

&nbsp;   """

&nbsp;   Pull EVERY implementation detail from all sources

&nbsp;   """

&nbsp;   

&nbsp;   implementation\_details = {}

&nbsp;   

&nbsp;   for component in all\_components:

&nbsp;       details = {

&nbsp;           'exact\_imports': list\_all\_required\_imports(component),

&nbsp;           'class\_structure': define\_complete\_class(component),

&nbsp;           'method\_signatures': specify\_all\_methods(component),

&nbsp;           'error\_handling': detail\_all\_error\_cases(component),

&nbsp;           'logging\_points': mark\_all\_log\_locations(component),

&nbsp;           'configuration': specify\_all\_settings(component),

&nbsp;           'test\_cases': define\_all\_tests(component)

&nbsp;       }

&nbsp;       

&nbsp;       # Extract from prototypes

&nbsp;       if has\_prototype(component):

&nbsp;           details\['reference\_implementation'] = extract\_prototype\_code(component)

&nbsp;           details\['proven\_patterns'] = identify\_working\_patterns(component)

&nbsp;       

&nbsp;       implementation\_details\[component] = details

&nbsp;   

&nbsp;   return implementation\_details

```



<detail\_checkpoint>

Methods specified: 67, Configs: 23, Error cases: 45, Tests: 89

</detail\_checkpoint>



---



\# CHAIN 6: EDGE CASE \& ERROR SCENARIO COMPLETION (20 minutes)



<planning>

I will ensure:

1\. All errors handled

2\. Edge cases covered

3\. Race conditions addressed

4\. Resource cleanup defined

5\. Failure recovery specified

</planning>



\## Focus: Defensive Programming Completeness



```python

def complete\_error\_handling():

&nbsp;   """

&nbsp;   Ensure EVERY possible failure is handled

&nbsp;   """

&nbsp;   

&nbsp;   error\_scenarios = {}

&nbsp;   

&nbsp;   for component in all\_components:

&nbsp;       # Identify all failure modes

&nbsp;       failures = {

&nbsp;           'input\_validation': define\_invalid\_inputs(component),

&nbsp;           'resource\_failures': identify\_resource\_issues(component),

&nbsp;           'integration\_failures': find\_integration\_errors(component),

&nbsp;           'concurrency\_issues': detect\_race\_conditions(component),

&nbsp;           'performance\_degradation': model\_slowdowns(component)

&nbsp;       }

&nbsp;       

&nbsp;       # Define handling for each

&nbsp;       for failure\_type, scenarios in failures.items():

&nbsp;           for scenario in scenarios:

&nbsp;               handling = {

&nbsp;                   'detection': how\_to\_detect(scenario),

&nbsp;                   'immediate\_response': define\_response(scenario),

&nbsp;                   'logging': specify\_log\_format(scenario),

&nbsp;                   'recovery': design\_recovery(scenario),

&nbsp;                   'monitoring': define\_alerts(scenario)

&nbsp;               }

&nbsp;               

&nbsp;               error\_scenarios\[f"{component}\_{scenario}"] = handling

&nbsp;   

&nbsp;   return error\_scenarios

```



---



\# CHAIN 7: CONFIGURATION \& DEPLOYMENT SPECIFICATION (15 minutes)



<planning>

I will specify:

1\. All configurations

2\. Environment variables

3\. Deployment steps

4\. Migration procedures

5\. Rollback plans

</planning>



\## Focus: Zero Ambiguity Deployment



```python

def specify\_deployment\_completely():

&nbsp;   """

&nbsp;   Every deployment detail explicitly defined

&nbsp;   """

&nbsp;   

&nbsp;   deployment\_specification = {

&nbsp;       'prerequisites': list\_all\_prerequisites(),

&nbsp;       'environment\_setup': define\_all\_environments(),

&nbsp;       'configuration\_files': provide\_all\_configs(),

&nbsp;       'deployment\_sequence': order\_deployment\_steps(),

&nbsp;       'verification\_steps': create\_smoke\_tests(),

&nbsp;       'rollback\_procedure': detail\_rollback\_steps()

&nbsp;   }

&nbsp;   

&nbsp;   # Migration specific

&nbsp;   migration\_details = {

&nbsp;       'data\_migration': step\_by\_step\_data\_migration(),

&nbsp;       'cutover\_procedure': define\_exact\_cutover(),

&nbsp;       'parallel\_run': specify\_parallel\_testing(),

&nbsp;       'performance\_validation': define\_benchmarks(),

&nbsp;       'fallback\_triggers': when\_to\_rollback()

&nbsp;   }

&nbsp;   

&nbsp;   return deployment\_specification, migration\_details

```



---



\# CHAIN 8: FINAL CONSOLIDATION \& SINGLE DOCUMENT GENERATION (30 minutes)



<planning>

I will consolidate:

1\. All validated designs

2\. Implementation sequence

3\. Complete details

4\. Error handling

5\. Deployment steps

Into ONE document with ZERO external references

</planning>



\## Focus: Create THE Implementation Document



```python

def generate\_single\_implementation\_document():

&nbsp;   """

&nbsp;   Consolidate EVERYTHING into one implementable document

&nbsp;   """

&nbsp;   

&nbsp;   document\_sections = \[

&nbsp;       create\_executive\_summary(),

&nbsp;       define\_prerequisites\_section(),

&nbsp;       detail\_implementation\_sequence(),

&nbsp;       provide\_component\_specifications(),

&nbsp;       include\_complete\_configurations(),

&nbsp;       specify\_testing\_procedures(),

&nbsp;       define\_deployment\_process(),

&nbsp;       add\_verification\_checklists()

&nbsp;   ]

&nbsp;   

&nbsp;   # Ensure completeness

&nbsp;   completeness\_check = {

&nbsp;       'all\_components\_documented': verify\_component\_coverage(),

&nbsp;       'all\_configs\_included': check\_configuration\_completeness(),

&nbsp;       'all\_tests\_defined': validate\_test\_coverage(),

&nbsp;       'no\_external\_references': scan\_for\_external\_refs(),

&nbsp;       'implementation\_order\_clear': verify\_sequence\_clarity()

&nbsp;   }

&nbsp;   

&nbsp;   if not all(completeness\_check.values()):

&nbsp;       missing = identify\_missing\_elements(completeness\_check)

&nbsp;       raise IncompleteDocumentation(f"Missing: {missing}")

&nbsp;   

&nbsp;   return consolidated\_document

```



---



\# CHAIN 9: IMPLEMENTATION VALIDATION \& DEVELOPER TESTING (15 minutes)



<planning>

I will validate:

1\. Document completeness

2\. Implementation clarity

3\. No ambiguities

4\. Testable steps

5\. Success criteria

</planning>



\## Focus: Ensure Single-Pass Implementation



```python

def validate\_implementation\_document():

&nbsp;   """

&nbsp;   Verify developer can implement without questions

&nbsp;   """

&nbsp;   

&nbsp;   validation\_tests = {

&nbsp;       'clarity\_test': check\_each\_step\_is\_clear(),

&nbsp;       'completeness\_test': verify\_no\_missing\_info(),

&nbsp;       'sequence\_test': validate\_build\_order(),

&nbsp;       'testability\_test': ensure\_each\_step\_testable(),

&nbsp;       'rollback\_test': verify\_rollback\_possible()

&nbsp;   }

&nbsp;   

&nbsp;   # Simulate developer reading

&nbsp;   developer\_questions = simulate\_implementation\_reading()

&nbsp;   

&nbsp;   if developer\_questions:

&nbsp;       for question in developer\_questions:

&nbsp;           answer = find\_answer\_in\_document(question)

&nbsp;           if not answer:

&nbsp;               # Must add this information

&nbsp;               add\_clarification\_to\_document(question)

&nbsp;   

&nbsp;   final\_validation = {

&nbsp;       'can\_implement': True,

&nbsp;       'estimated\_time': calculate\_implementation\_time(),

&nbsp;       'risk\_points': identify\_risky\_sections(),

&nbsp;       'success\_probability': assess\_success\_likelihood()

&nbsp;   }

&nbsp;   

&nbsp;   return final\_validation

```



<final\_checkpoint>

✓ All components documented

✓ No external references  

✓ Every step testable

✓ Complete error handling

✓ Deployment fully specified

✓ Zero ambiguity remains

</final\_checkpoint>



---



\## Document Structure Template



```markdown

\# Semantic Category Classifier Refactoring: Complete Implementation Guide



\## Executive Summary

\[Purpose, approach, expected outcomes - 1 page max]



\## Prerequisites \& Setup

\[Everything needed before starting]



\## Implementation Sequence



\### Phase 1: Foundation Components

1\. Configuration System

&nbsp;  - Purpose: \[Why this first]

&nbsp;  - Implementation: \[Exact code]

&nbsp;  - Verification: \[How to test]

&nbsp;  - Rollback: \[How to undo]



2\. Base Abstractions

&nbsp;  \[Complete specification...]



\### Phase 2: Core Components

\[Continue pattern...]



\## Complete Component Specifications

\[Every class, method, configuration]



\## Error Handling Specifications

\[Every error case and response]



\## Testing Specifications

\[Every test with expected results]



\## Deployment Procedure

\[Step-by-step with verification]



\## Verification Checklists

\[How to confirm success]

```



---



\## Success Criteria



The final document enables a developer to:

1\. Start implementing immediately

2\. Complete without asking questions

3\. Test each component as built

4\. Deploy with confidence

5\. Rollback if needed



\*\*Remember\*\*: One document, complete information, axiomatic structure, zero ambiguity.

