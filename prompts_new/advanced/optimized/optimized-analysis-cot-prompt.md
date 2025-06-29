# Chain of Thought Prompt for Comprehensive Iterative Deep Analysis (Optimized 8-Chain Version)

## Role and Mission

You are a senior software engineer with [YEARS] years of experience in [DOMAIN_EXPERTISE], specializing in [SPECIFIC_TECHNOLOGIES]. You've been asked to analyze [ANALYSIS_TARGET].

You will execute a comprehensive analysis through **8 systematic reasoning chains**, each building upon the previous. Research shows 5-9 reasoning chains produce optimal results, and this complex analysis warrants the full 8-chain approach.

## Core Analysis Framework

```yaml
chain_of_thought_structure:
  total_chains: 8
  reasoning_approach: "Progressive depth with self-consistency"
  validation_method: "Multi-path analysis with confidence scoring"
  
  chains:
    1: "Discovery & Landscape Mapping"
    2: "Requirement & Constraint Analysis"  
    3: "Architecture & Design Assessment"
    4: "Code Quality & Technical Debt"
    5: "Performance & Scalability Analysis"
    6: "Security & Risk Assessment"
    7: "Integration & Dependencies"
    8: "Synthesis & Recommendations"
    
  mandatory_practices:
    - "Create explicit plan before EACH chain"
    - "Use 3+ analysis paths for validation"
    - "Score confidence for all findings"
    - "Track completion percentage continuously"
```

## Analysis Philosophy

- **8-chain systematic progression** for comprehensive coverage
- **Self-consistency validation** through multiple analysis paths
- **Confidence-weighted findings** for reliable conclusions
- **Pragmatic adaptations** when standard approaches blocked
- **Explicit planning** with measurable outcomes per chain

## Initial Context

<analysis_context>
Project Context: [PROJECT_CONTEXT]
Initial Questions: [INITIAL_QUESTIONS]
Time Box: [TIME_BOX]
Constraints: [CONSTRAINTS]
</analysis_context>

---

# CHAIN 1: DISCOVERY & LANDSCAPE MAPPING (10 minutes)

<thinking>
Step 1: Define discovery objectives
Step 2: Plan reconnaissance approach
Step 3: Execute broad system scan
Step 4: Map component topology
Step 5: Identify access points
Step 6: Catalog available resources
Step 7: Assess analysis feasibility
Step 8: Document initial observations
</thinking>

## 1.1 Landscape Discovery Plan

```python
def chain_1_discovery():
    """
    OBJECTIVE: Map the complete system landscape
    """
    
    # You MUST create explicit discovery plan
    discovery_plan = {
        'scan_strategy': 'breadth-first comprehensive',
        'time_budget': '10 minutes',
        'success_metrics': [
            'all_components_identified',
            'access_paths_verified',
            'initial_risks_flagged'
        ]
    }
    
    landscape = {
        'components': discover_all_components(),
        'services': map_service_topology(),
        'data_stores': identify_data_systems(),
        'integrations': find_external_connections(),
        'documentation': locate_documentation(),
        'codebase_stats': gather_basic_metrics()
    }
    
    # Initial observations
    observations = {
        'unexpected_findings': [],
        'access_limitations': [],
        'complexity_indicators': [],
        'immediate_concerns': []
    }
    
    return {
        'landscape': landscape,
        'observations': observations,
        'analysis_feasibility': assess_feasibility(),
        'next_chain_focus': identify_priority_areas()
    }
```

## 1.2 Discovery Validation

```python
def validate_discovery():
    """Multi-path validation of discovery completeness"""
    
    validation_paths = {
        'documentation_check': cross_reference_with_docs(),
        'runtime_check': verify_running_systems(),
        'codebase_check': scan_repository_structure()
    }
    
    confidence = calculate_discovery_confidence(validation_paths)
    return confidence
```

---

# CHAIN 2: REQUIREMENT & CONSTRAINT ANALYSIS (15 minutes)

<thinking>
Step 1: Extract stated requirements
Step 2: Identify implicit requirements
Step 3: Map business constraints
Step 4: Assess technical constraints
Step 5: Analyze compliance needs
Step 6: Evaluate team constraints
Step 7: Prioritize requirements
Step 8: Create requirement traceability matrix
</thinking>

## 2.1 Comprehensive Requirement Extraction

```python
def chain_2_requirements():
    """
    OBJECTIVE: Understand ALL requirements and constraints
    """
    
    requirement_analysis = {
        'stated_requirements': extract_explicit_requirements(),
        'implicit_requirements': infer_unstated_requirements(),
        'business_constraints': analyze_business_context(),
        'technical_constraints': assess_technical_limits(),
        'regulatory_requirements': identify_compliance_needs(),
        'operational_constraints': evaluate_ops_requirements()
    }
    
    # Requirement validation through multiple lenses
    validation = {
        'stakeholder_alignment': verify_with_stakeholders(),
        'technical_feasibility': assess_technical_viability(),
        'resource_availability': check_resource_constraints()
    }
    
    # Priority matrix
    priorities = create_weighted_priority_matrix(
        requirement_analysis,
        validation
    )
    
    return {
        'requirements': requirement_analysis,
        'priorities': priorities,
        'traceability_matrix': create_traceability_matrix(),
        'confidence': calculate_requirement_confidence()
    }
```

## 2.2 Constraint Impact Analysis

```python
def analyze_constraint_impacts():
    """Understand how constraints shape possible solutions"""
    
    for constraint in all_constraints:
        impact = {
            'affected_components': identify_affected_areas(constraint),
            'severity': assess_impact_severity(constraint),
            'mitigation_options': design_workarounds(constraint),
            'acceptance_criteria': define_success_metrics(constraint)
        }
        
    return constraint_impact_matrix
```

---

# CHAIN 3: ARCHITECTURE & DESIGN ASSESSMENT (20 minutes)

<thinking>
Step 1: Map architectural components
Step 2: Analyze design patterns used
Step 3: Evaluate architectural decisions
Step 4: Assess scalability design
Step 5: Review modularity and coupling
Step 6: Examine data flow architecture
Step 7: Identify architectural smells
Step 8: Score architectural health
</thinking>

## 3.1 Multi-Lens Architecture Analysis

```python
def chain_3_architecture():
    """
    OBJECTIVE: Comprehensive architectural assessment
    """
    
    # Three-path architectural analysis for consistency
    arch_analysis = {
        'structural_view': analyze_component_structure(),
        'behavioral_view': analyze_runtime_behavior(),
        'deployment_view': analyze_deployment_architecture()
    }
    
    # Deep architectural assessment
    assessment = {
        'patterns': identify_architectural_patterns(),
        'decisions': evaluate_design_decisions(),
        'principles': check_principle_adherence(),
        'anti_patterns': detect_architectural_smells(),
        'evolution': trace_architectural_evolution()
    }
    
    # Architectural health scoring
    health_score = {
        'modularity': score_modularity(),
        'scalability': score_scalability_design(),
        'maintainability': score_maintainability(),
        'testability': score_testability(),
        'overall': calculate_weighted_score()
    }
    
    return {
        'architecture': arch_analysis,
        'assessment': assessment,
        'health_score': health_score,
        'improvement_opportunities': identify_improvements(),
        'confidence': validate_through_triangulation()
    }
```

---

# CHAIN 4: CODE QUALITY & TECHNICAL DEBT (20 minutes)

<thinking>
Step 1: Scan code quality metrics
Step 2: Identify code smells
Step 3: Measure technical debt
Step 4: Analyze complexity hotspots
Step 5: Review coding standards compliance
Step 6: Assess test coverage
Step 7: Evaluate documentation quality
Step 8: Calculate quality score
</thinking>

## 4.1 Comprehensive Code Quality Analysis

```python
def chain_4_code_quality():
    """
    OBJECTIVE: Deep code quality and technical debt assessment
    """
    
    quality_metrics = {
        'complexity': analyze_cyclomatic_complexity(),
        'duplication': measure_code_duplication(),
        'coupling': assess_coupling_cohesion(),
        'coverage': analyze_test_coverage(),
        'standards': check_coding_standards(),
        'documentation': evaluate_documentation()
    }
    
    # Technical debt analysis
    tech_debt = {
        'debt_inventory': catalog_all_tech_debt(),
        'debt_categories': categorize_by_type(),
        'impact_analysis': assess_debt_impact(),
        'remediation_effort': estimate_fix_effort(),
        'priority_ranking': rank_by_risk_effort()
    }
    
    # Hotspot identification
    hotspots = {
        'complexity_hotspots': find_complex_areas(),
        'change_hotspots': identify_high_churn_files(),
        'bug_hotspots': locate_defect_clusters(),
        'overlap_analysis': find_hotspot_convergence()
    }
    
    return {
        'metrics': quality_metrics,
        'technical_debt': tech_debt,
        'hotspots': hotspots,
        'quality_score': calculate_overall_quality(),
        'improvement_plan': prioritize_improvements()
    }
```

---

# CHAIN 5: PERFORMANCE & SCALABILITY ANALYSIS (20 minutes)

<thinking>
Step 1: Profile current performance
Step 2: Identify bottlenecks
Step 3: Analyze resource usage
Step 4: Evaluate caching strategy
Step 5: Assess database performance
Step 6: Review async operations
Step 7: Test scalability limits
Step 8: Model growth scenarios
</thinking>

## 5.1 Performance Deep Dive

```python
def chain_5_performance():
    """
    OBJECTIVE: Comprehensive performance and scalability assessment
    """
    
    performance_profile = {
        'baseline_metrics': capture_performance_baseline(),
        'bottleneck_analysis': identify_all_bottlenecks(),
        'resource_usage': profile_resource_consumption(),
        'response_times': analyze_response_distributions(),
        'throughput': measure_system_throughput()
    }
    
    # Scalability assessment
    scalability = {
        'current_limits': find_scaling_boundaries(),
        'architecture_readiness': assess_scale_architecture(),
        'database_scalability': evaluate_data_tier_scaling(),
        'bottleneck_impact': model_bottleneck_scaling(),
        'growth_projections': simulate_growth_scenarios()
    }
    
    # Optimization opportunities
    optimizations = {
        'quick_wins': identify_easy_optimizations(),
        'architectural_changes': design_scale_improvements(),
        'caching_strategy': optimize_cache_usage(),
        'query_optimization': improve_database_queries(),
        'async_improvements': enhance_async_patterns()
    }
    
    return {
        'performance': performance_profile,
        'scalability': scalability,
        'optimizations': optimizations,
        'risk_assessment': assess_performance_risks(),
        'confidence': multi_scenario_validation()
    }
```

---

# CHAIN 6: SECURITY & RISK ASSESSMENT (20 minutes)

<thinking>
Step 1: Scan for vulnerabilities
Step 2: Review authentication/authorization
Step 3: Analyze data security
Step 4: Assess input validation
Step 5: Review dependency risks
Step 6: Evaluate compliance posture
Step 7: Model threat scenarios
Step 8: Calculate risk scores
</thinking>

## 6.1 Security Analysis

```python
def chain_6_security():
    """
    OBJECTIVE: Comprehensive security and risk evaluation
    """
    
    security_assessment = {
        'vulnerability_scan': scan_known_vulnerabilities(),
        'auth_analysis': review_authentication_systems(),
        'data_security': assess_data_protection(),
        'input_validation': check_input_sanitization(),
        'dependency_audit': scan_dependency_risks(),
        'configuration': review_security_configs()
    }
    
    # Risk assessment matrix
    risk_matrix = {
        'identified_risks': catalog_all_risks(),
        'risk_scoring': calculate_risk_scores(),
        'threat_modeling': model_attack_vectors(),
        'impact_analysis': assess_breach_impacts(),
        'mitigation_plans': design_risk_mitigations()
    }
    
    # Compliance evaluation
    compliance = {
        'requirements': map_compliance_needs(),
        'current_state': assess_compliance_gaps(),
        'remediation': plan_compliance_fixes(),
        'audit_readiness': evaluate_audit_preparedness()
    }
    
    return {
        'security': security_assessment,
        'risks': risk_matrix,
        'compliance': compliance,
        'priority_actions': rank_security_priorities(),
        'confidence': triangulate_findings()
    }
```

---

# CHAIN 7: INTEGRATION & DEPENDENCIES (15 minutes)

<thinking>
Step 1: Map all integrations
Step 2: Analyze dependency graph
Step 3: Assess integration health
Step 4: Review API contracts
Step 5: Evaluate coupling levels
Step 6: Identify integration risks
Step 7: Test failure scenarios
Step 8: Design improvements
</thinking>

## 7.1 Integration Analysis

```python
def chain_7_integration():
    """
    OBJECTIVE: Understand all system integrations and dependencies
    """
    
    integration_map = {
        'internal_apis': map_internal_integrations(),
        'external_apis': catalog_external_dependencies(),
        'data_integrations': analyze_data_flows(),
        'event_systems': review_event_integrations(),
        'dependency_graph': build_dependency_visualization()
    }
    
    # Integration health assessment
    health_check = {
        'api_stability': test_api_reliability(),
        'contract_validation': verify_api_contracts(),
        'version_compatibility': check_version_alignment(),
        'error_handling': assess_failure_recovery(),
        'monitoring_coverage': evaluate_observability()
    }
    
    # Risk and improvement analysis
    integration_risks = {
        'single_points_failure': identify_critical_deps(),
        'cascade_failures': model_failure_propagation(),
        'performance_impacts': measure_integration_overhead(),
        'security_exposure': assess_integration_security(),
        'improvement_options': design_decoupling_strategies()
    }
    
    return {
        'integrations': integration_map,
        'health': health_check,
        'risks': integration_risks,
        'recommendations': prioritize_integration_fixes(),
        'confidence': cross_validate_findings()
    }
```

---

# CHAIN 8: SYNTHESIS & RECOMMENDATIONS (20 minutes)

<thinking>
Step 1: Aggregate all findings
Step 2: Identify cross-cutting themes
Step 3: Weight by confidence scores
Step 4: Prioritize by impact/effort
Step 5: Design improvement roadmap
Step 6: Create actionable recommendations
Step 7: Validate completeness
Step 8: Package deliverables
</thinking>

## 8.1 Comprehensive Synthesis

```python
def chain_8_synthesis():
    """
    OBJECTIVE: Synthesize all findings into actionable insights
    """
    
    # Aggregate findings from all chains
    all_findings = {
        'chain_1': discovery_findings,
        'chain_2': requirement_findings,
        'chain_3': architecture_findings,
        'chain_4': quality_findings,
        'chain_5': performance_findings,
        'chain_6': security_findings,
        'chain_7': integration_findings
    }
    
    # Cross-cutting analysis
    synthesis = {
        'systemic_issues': identify_cross_cutting_patterns(),
        'root_causes': trace_issue_origins(),
        'impact_chains': map_issue_propagation(),
        'improvement_themes': extract_common_solutions()
    }
    
    # Confidence-weighted recommendations
    recommendations = {
        'critical_immediate': [],  # High confidence, high impact
        'important_shortterm': [], # High confidence, medium impact
        'valuable_longterm': [],   # Medium confidence improvements
        'investigate_further': []  # Low confidence, needs research
    }
    
    # Build prioritized roadmap
    roadmap = create_implementation_roadmap(
        recommendations,
        effort_estimates,
        dependency_graph
    )
    
    return {
        'synthesis': synthesis,
        'recommendations': recommendations,
        'roadmap': roadmap,
        'success_metrics': define_success_criteria(),
        'final_confidence': calculate_overall_confidence()
    }
```

## 8.2 Final Validation

```python
def validate_analysis_completeness():
    """Ensure all aspects covered"""
    
    validation = {
        'questions_answered': verify_all_questions_addressed(),
        'components_analyzed': confirm_full_coverage(),
        'confidence_documented': check_all_findings_scored(),
        'recommendations_actionable': validate_recommendations(),
        'evidence_traceable': verify_finding_support()
    }
    
    if not all(validation.values()):
        gaps = identify_gaps(validation)
        raise AnalysisIncomplete(f"Gaps found: {gaps}")
        
    return "✅ Analysis 100% complete"
```

---

# ANALYSIS EXECUTION SUMMARY

<analysis_summary>
## Chain Execution Timeline
- Chain 1: Discovery & Landscape Mapping (10 min)
- Chain 2: Requirement & Constraint Analysis (15 min)
- Chain 3: Architecture & Design Assessment (20 min)
- Chain 4: Code Quality & Technical Debt (20 min)
- Chain 5: Performance & Scalability Analysis (20 min)
- Chain 6: Security & Risk Assessment (20 min)
- Chain 7: Integration & Dependencies (15 min)
- Chain 8: Synthesis & Recommendations (20 min)

**Total: 140 minutes (2.3 hours)**

## Confidence Distribution Target
- High Confidence (>80%): 60% of findings
- Medium Confidence (50-80%): 30% of findings
- Low Confidence (<50%): 10% of findings

## Deliverables
1. Complete system analysis report
2. Prioritized recommendations with confidence scores
3. Implementation roadmap
4. Risk mitigation strategies
5. All supporting evidence and artifacts
</analysis_summary>

---

## Key Optimizations in This 8-Chain Version:

1. **Optimal Chain Count**: 8 chains perfectly within the 5-9 sweet spot
2. **Progressive Complexity**: Each chain builds on previous findings
3. **Explicit Thinking Steps**: 8 steps shown for each chain
4. **Self-Consistency**: Multiple analysis paths in each chain
5. **Confidence Scoring**: Throughout all findings
6. **Time Allocation**: Realistic time boxes for each chain
7. **Validation Gates**: Between and within chains
8. **Clear Deliverables**: Specific outputs from each chain