# Orchestration Database Schema Enhancement Proposal

## Overview

This document outlines specific database schema enhancements to enable comprehensive analytics and workflow optimization for the prompt-runner orchestration system.

## Current Schema Analysis

### Existing OrchestrationSession Table
```python
class OrchestrationSession(Base):
    __tablename__ = 'orchestration_sessions'
    
    # Current fields
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    feature_request = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)
    orchestrator_prompt = Column(Text)
    orchestrator_output = Column(Text)
    
    # Template storage (good foundation)
    planning_template = Column(Text)
    analysis_template = Column(Text)
    implementation_template = Column(Text)
    testing_template = Column(Text)
    cleaning_template = Column(Text)
    
    # Results storage
    analysis_results = Column(Text)
    implementation_results = Column(Text)
    testing_results = Column(Text)
    cleaning_results = Column(Text)
    
    # Minimal metadata
    metadata = Column(JSON)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))
```

## Proposed Schema Enhancements

### 1. Enhanced OrchestrationSession Table

```sql
-- Add analytics columns to existing table
ALTER TABLE orchestration_sessions ADD COLUMN session_version INTEGER DEFAULT 1;
ALTER TABLE orchestration_sessions ADD COLUMN user_identifier VARCHAR(255);
ALTER TABLE orchestration_sessions ADD COLUMN session_type VARCHAR(50) DEFAULT 'manual';  -- manual, automated, hybrid

-- Phase timing columns
ALTER TABLE orchestration_sessions ADD COLUMN planning_started_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN planning_completed_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN analysis_started_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN analysis_completed_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN implementation_started_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN implementation_completed_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN testing_started_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN testing_completed_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN cleaning_started_at TIMESTAMP WITH TIME ZONE;
ALTER TABLE orchestration_sessions ADD COLUMN cleaning_completed_at TIMESTAMP WITH TIME ZONE;

-- Success tracking
ALTER TABLE orchestration_sessions ADD COLUMN planning_success BOOLEAN;
ALTER TABLE orchestration_sessions ADD COLUMN analysis_success BOOLEAN;
ALTER TABLE orchestration_sessions ADD COLUMN implementation_success BOOLEAN;
ALTER TABLE orchestration_sessions ADD COLUMN testing_success BOOLEAN;
ALTER TABLE orchestration_sessions ADD COLUMN cleaning_success BOOLEAN;
ALTER TABLE orchestration_sessions ADD COLUMN overall_success BOOLEAN;

-- Efficiency metrics
ALTER TABLE orchestration_sessions ADD COLUMN total_duration_seconds FLOAT;
ALTER TABLE orchestration_sessions ADD COLUMN active_duration_seconds FLOAT;  -- Excluding idle time
ALTER TABLE orchestration_sessions ADD COLUMN retry_count INTEGER DEFAULT 0;
ALTER TABLE orchestration_sessions ADD COLUMN manual_interventions INTEGER DEFAULT 0;

-- Developer experience
ALTER TABLE orchestration_sessions ADD COLUMN developer_rating INTEGER CHECK (developer_rating >= 1 AND developer_rating <= 5);
ALTER TABLE orchestration_sessions ADD COLUMN developer_feedback TEXT;
ALTER TABLE orchestration_sessions ADD COLUMN would_recommend BOOLEAN;
ALTER TABLE orchestration_sessions ADD COLUMN time_saved_hours FLOAT;

-- Feature complexity (enhanced)
ALTER TABLE orchestration_sessions ADD COLUMN complexity_score FLOAT;  -- Calculated complexity
ALTER TABLE orchestration_sessions ADD COLUMN estimated_hours FLOAT;
ALTER TABLE orchestration_sessions ADD COLUMN actual_hours FLOAT;
ALTER TABLE orchestration_sessions ADD COLUMN accuracy_score FLOAT;  -- How close estimate was to actual

-- Add indexes for performance
CREATE INDEX idx_orchestration_sessions_user ON orchestration_sessions(user_identifier);
CREATE INDEX idx_orchestration_sessions_status ON orchestration_sessions(status);
CREATE INDEX idx_orchestration_sessions_created ON orchestration_sessions(created_at);
CREATE INDEX idx_orchestration_sessions_success ON orchestration_sessions(overall_success);
```

### 2. New Table: OrchestrationPhaseMetrics

```sql
CREATE TABLE orchestration_phase_metrics (
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES orchestration_sessions(id) ON DELETE CASCADE,
    phase VARCHAR(50) NOT NULL,  -- planning, analysis, implementation, testing, cleaning
    phase_index INTEGER NOT NULL,  -- Order in workflow
    
    -- Timing
    started_at TIMESTAMP WITH TIME ZONE NOT NULL,
    completed_at TIMESTAMP WITH TIME ZONE,
    duration_seconds FLOAT,
    idle_time_seconds FLOAT,  -- Time between phase completion and next phase start
    
    -- LLM interaction
    prompt_tokens INTEGER,
    completion_tokens INTEGER,
    total_tokens INTEGER,
    model_used VARCHAR(100),
    temperature FLOAT,
    
    -- Quality metrics
    output_length INTEGER,
    template_extraction_success BOOLEAN,
    validation_errors INTEGER DEFAULT 0,
    validation_warnings INTEGER DEFAULT 0,
    
    -- User interaction
    copy_paste_method VARCHAR(50),  -- manual, clipboard, file
    input_method VARCHAR(50),  -- interactive, file, api
    user_edits BOOLEAN DEFAULT FALSE,
    edit_count INTEGER DEFAULT 0,
    
    -- Error tracking
    error_occurred BOOLEAN DEFAULT FALSE,
    error_type VARCHAR(100),
    error_message TEXT,
    error_recovered BOOLEAN DEFAULT FALSE,
    
    -- Metadata
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT unique_session_phase UNIQUE (session_id, phase)
);

CREATE INDEX idx_phase_metrics_session ON orchestration_phase_metrics(session_id);
CREATE INDEX idx_phase_metrics_phase ON orchestration_phase_metrics(phase);
CREATE INDEX idx_phase_metrics_duration ON orchestration_phase_metrics(duration_seconds);
```

### 3. New Table: OrchestrationEvents

```sql
CREATE TABLE orchestration_events (
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES orchestration_sessions(id) ON DELETE CASCADE,
    event_type VARCHAR(100) NOT NULL,  -- command_executed, error_occurred, user_action, etc.
    event_category VARCHAR(50) NOT NULL,  -- cli, user, system, error
    phase VARCHAR(50),
    
    -- Event details
    command VARCHAR(255),
    parameters JSONB,
    result VARCHAR(50),  -- success, failure, cancelled
    
    -- Timing
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    duration_ms INTEGER,
    
    -- Context
    user_identifier VARCHAR(255),
    session_version INTEGER,
    error_details TEXT,
    
    -- Metadata
    metadata JSONB
);

CREATE INDEX idx_events_session ON orchestration_events(session_id);
CREATE INDEX idx_events_type ON orchestration_events(event_type);
CREATE INDEX idx_events_timestamp ON orchestration_events(timestamp);
CREATE INDEX idx_events_user ON orchestration_events(user_identifier);
```

### 4. New Table: OrchestrationCodeMetrics

```sql
CREATE TABLE orchestration_code_metrics (
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES orchestration_sessions(id) ON DELETE CASCADE,
    
    -- File metrics
    files_created INTEGER DEFAULT 0,
    files_modified INTEGER DEFAULT 0,
    files_deleted INTEGER DEFAULT 0,
    total_files INTEGER DEFAULT 0,
    
    -- Code volume
    lines_added INTEGER DEFAULT 0,
    lines_modified INTEGER DEFAULT 0,
    lines_deleted INTEGER DEFAULT 0,
    total_lines INTEGER DEFAULT 0,
    
    -- Language breakdown
    languages JSONB,  -- {"python": 500, "javascript": 200, "yaml": 50}
    primary_language VARCHAR(50),
    
    -- Quality metrics
    test_files_created INTEGER DEFAULT 0,
    test_cases_added INTEGER DEFAULT 0,
    test_coverage_before FLOAT,
    test_coverage_after FLOAT,
    test_coverage_delta FLOAT,
    
    -- Complexity metrics
    cyclomatic_complexity_avg FLOAT,
    cognitive_complexity_avg FLOAT,
    maintainability_index FLOAT,
    technical_debt_minutes INTEGER,
    
    -- Documentation
    docs_created INTEGER DEFAULT 0,
    docs_updated INTEGER DEFAULT 0,
    comment_lines_added INTEGER DEFAULT 0,
    documentation_score FLOAT,
    
    -- Version control
    git_commits INTEGER DEFAULT 0,
    git_branch VARCHAR(255),
    git_commit_hashes TEXT[],
    pr_created BOOLEAN DEFAULT FALSE,
    pr_number INTEGER,
    pr_url VARCHAR(500),
    
    -- Performance impact
    build_time_before_seconds FLOAT,
    build_time_after_seconds FLOAT,
    bundle_size_before_kb INTEGER,
    bundle_size_after_kb INTEGER,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_code_metrics_session ON orchestration_code_metrics(session_id);
CREATE INDEX idx_code_metrics_language ON orchestration_code_metrics(primary_language);
```

### 5. New Table: OrchestrationTemplateMetrics

```sql
CREATE TABLE orchestration_template_metrics (
    id SERIAL PRIMARY KEY,
    template_type VARCHAR(50) NOT NULL,  -- planning, analysis, implementation, testing, cleaning
    template_hash VARCHAR(64) NOT NULL,  -- SHA-256 hash of template content
    
    -- Usage statistics
    usage_count INTEGER DEFAULT 0,
    success_count INTEGER DEFAULT 0,
    failure_count INTEGER DEFAULT 0,
    success_rate FLOAT GENERATED ALWAYS AS (
        CASE WHEN usage_count > 0 
        THEN success_count::FLOAT / usage_count::FLOAT 
        ELSE 0 END
    ) STORED,
    
    -- Performance metrics
    avg_completion_time_seconds FLOAT,
    avg_tokens_used INTEGER,
    avg_user_edits INTEGER,
    
    -- Quality metrics
    avg_developer_rating FLOAT,
    avg_code_quality_score FLOAT,
    avg_test_coverage_achieved FLOAT,
    
    -- Feature correlation
    feature_categories JSONB,  -- {"api": 20, "ui": 15, "database": 10}
    complexity_distribution JSONB,  -- {"simple": 30, "medium": 20, "complex": 5}
    
    -- Evolution tracking
    first_used_at TIMESTAMP WITH TIME ZONE,
    last_used_at TIMESTAMP WITH TIME ZONE,
    deprecated_at TIMESTAMP WITH TIME ZONE,
    replacement_template_hash VARCHAR(64),
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_template_metrics_type ON orchestration_template_metrics(template_type);
CREATE INDEX idx_template_metrics_hash ON orchestration_template_metrics(template_hash);
CREATE INDEX idx_template_metrics_success ON orchestration_template_metrics(success_rate);
```

## Analytics Views

### 1. Developer Productivity View

```sql
CREATE VIEW v_developer_productivity AS
SELECT 
    user_identifier,
    COUNT(DISTINCT id) as total_sessions,
    COUNT(DISTINCT CASE WHEN overall_success THEN id END) as successful_sessions,
    AVG(total_duration_seconds / 3600.0) as avg_duration_hours,
    AVG(time_saved_hours) as avg_time_saved_hours,
    AVG(developer_rating) as avg_satisfaction,
    SUM(CASE WHEN would_recommend THEN 1 ELSE 0 END)::FLOAT / 
        NULLIF(COUNT(CASE WHEN would_recommend IS NOT NULL THEN 1 END), 0) as recommendation_rate,
    MAX(created_at) as last_active
FROM orchestration_sessions
WHERE user_identifier IS NOT NULL
GROUP BY user_identifier;
```

### 2. Phase Performance View

```sql
CREATE VIEW v_phase_performance AS
SELECT 
    phase,
    COUNT(*) as execution_count,
    AVG(duration_seconds) as avg_duration_seconds,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_seconds) as median_duration_seconds,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY duration_seconds) as p95_duration_seconds,
    AVG(CASE WHEN error_occurred THEN 0 ELSE 1 END) as success_rate,
    AVG(total_tokens) as avg_tokens_used,
    SUM(validation_errors) as total_validation_errors
FROM orchestration_phase_metrics
GROUP BY phase;
```

### 3. Feature Complexity Analysis View

```sql
CREATE VIEW v_feature_complexity_analysis AS
SELECT 
    CASE 
        WHEN complexity_score < 3 THEN 'Simple'
        WHEN complexity_score < 7 THEN 'Medium'
        ELSE 'Complex'
    END as complexity_category,
    COUNT(*) as feature_count,
    AVG(total_duration_seconds / 3600.0) as avg_duration_hours,
    AVG(actual_hours) as avg_actual_hours,
    AVG(CASE WHEN overall_success THEN 1 ELSE 0 END) as success_rate,
    AVG(retry_count) as avg_retries,
    AVG(manual_interventions) as avg_interventions
FROM orchestration_sessions
WHERE complexity_score IS NOT NULL
GROUP BY complexity_category;
```

## Migration Strategy

### Phase 1: Non-Breaking Additions (Week 1)
1. Add new columns with defaults to orchestration_sessions
2. Create new tables without foreign key constraints
3. Deploy tracking code to start collecting metrics

### Phase 2: Data Population (Week 2)
1. Backfill historical data where possible
2. Add foreign key constraints
3. Create indexes for performance

### Phase 3: Analytics Implementation (Week 3)
1. Create views and materialized views
2. Build analytics dashboard
3. Implement reporting endpoints

### Phase 4: Optimization (Week 4)
1. Analyze query patterns
2. Add additional indexes as needed
3. Implement data archival strategy

## Benefits

1. **Comprehensive Analytics**: Track every aspect of the orchestration workflow
2. **Performance Optimization**: Identify bottlenecks and optimize phases
3. **Quality Improvement**: Correlate actions with code quality outcomes
4. **Developer Experience**: Measure and improve satisfaction
5. **Data-Driven Decisions**: Make improvements based on actual usage patterns
6. **Template Evolution**: Track template effectiveness and iterate
7. **Predictive Capabilities**: Build models to estimate effort and success probability

This schema enhancement transforms the orchestration system from a simple workflow tool into an intelligent, self-improving platform.