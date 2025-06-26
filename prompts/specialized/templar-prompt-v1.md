Okay, your instructions are to create a new program named 'templar' that analyzes, monitors, and reports on multiple repositories being developed.

Here is the long term vision:

=================================
Templar: The Unified Platform Guardian
Templar will evolve into a comprehensive platform orchestration and protection system that ensures reliability, consistency, and intelligence across your entire development and data ecosystem.
Core Capabilities
🏗️ Development Environment Orchestration

Provides container-based development environments with Docker-like simplicity, eliminating "works on my machine" issues forever
Automatically scales complex data stacks, synchronizes configurations, and anonymizes sensitive data for safe local development
Tracks code and data lineage across all projects and tools, providing complete visibility into your system's interconnections

🔍 Comprehensive Observability Suite

Distributed Tracing & APM: Full visibility into request flows and performance bottlenecks across your entire system
Intelligent Error Tracking: Captures production errors with complete context, stack traces, and session replay capabilities
Centralized Logging: Unified log aggregation using modern stacks (ELK/Loki+Grafana) with powerful search and analysis
Real-time Metrics: OpenTelemetry-based instrumentation tracking pipeline durations, throughput, error rates, and system health
Unified Status Dashboard: Single pane of glass showing system health, recent failures, performance trends, and operational metrics

🛡️ Advanced Quality Assurance

AI-Powered Fuzz Testing: Automated security and stability testing using intelligent input generation
Mutation Testing: Validates test suite quality by systematically introducing bugs and ensuring detection
Data Quality Validation: Great Expectations integration for continuous data pipeline validation and monitoring
Standardized LLM Workflow Logging: Built-in templates for consistent observability in AI/ML pipelines

🤖 Intelligent Operations & Self-Healing

Knowledge Base of Failure Patterns: Automatically catalogs errors, resolutions, and patterns over time
Automated Remediation: AI-driven system that recognizes known issues and applies proven fixes without human intervention
Predictive Maintenance: Learns from historical patterns to prevent issues before they occur
Smart Runbooks: Transforms traditional runbooks into automated, context-aware response systems

Templar stands as the vigilant guardian of your platform - watching, protecting, and intelligently responding to keep your systems running smoothly.
====================================

For now. Your instructions are to:

1.) There is a localhost postgresdb named 'templardb'. I have created user 'templar_process_user' with password 'qM133cXPX&i#n!f8YQOum'. Create the schema there using the account I provide. Please create the reader and writer users you suggest, as well.
2.) Develop the initial Python script to use the project_extractor tool to scan each directory, then write to the tables in the database. Please ensure this succeeds.
3.) Develop a unit test library that tests this functionality extensively. Store the scripts in a tests/ subdirectory from the root level of the project. The master script should be run_tests.sh and run_tests.py.
4.) Run the tests to ensure they succeed.
5.) Create a readme for this and cleanup any old/unused files.

CREATE ROLE templar_process_user
  WITH LOGIN
       PASSWORD 'qM133cXPX&i#n!f8YQOum'











-- 1. Create the login role (with optional replication privilege)
CREATE ROLE templar_process_user
  WITH LOGIN
       PASSWORD 'qM133cXPX&i#n!f8YQOum'
       NOSUPERUSER      -- restricts to this DB only
       NOCREATEROLE     -- cannot create other roles
       NOCREATEDB       -- cannot create other databases
       /* add REPLICATION here if you need streaming replicas: REPLICATION */
  ;

-- 2. Allow connection to the target database
GRANT CONNECT ON DATABASE "templardb" TO templar_process_user;
GRANT TEMPORARY ON DATABASE "templardb" TO templar_process_user;

-- 3. Switch into the target database
\c "templardb"

-- 4. For every user schema, grant full rights on existing objects and set up defaults
DO $$
DECLARE
  _schema text;
BEGIN
  FOR _schema IN
    SELECT nspname
      FROM pg_namespace
     WHERE nspname NOT LIKE 'pg_%'
       AND nspname <> 'information_schema'
  LOOP
    -- allow use and creation inside each schema
    EXECUTE format('GRANT USAGE, CREATE ON SCHEMA %I TO templar_process_user;', _schema);

    -- grant all rights on all existing tables, sequences, functions
    EXECUTE format('GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA %I TO templar_process_user;', _schema);
    EXECUTE format('GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA %I TO templar_process_user;', _schema);
    EXECUTE format('GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA %I TO templar_process_user;', _schema);

    -- ensure any future objects also grant full rights
    EXECUTE format(
      'ALTER DEFAULT PRIVILEGES IN SCHEMA %I
         GRANT ALL PRIVILEGES
           ON TABLES, SEQUENCES, FUNCTIONS
           TO templar_process_user;',
      _schema
    );
  END LOOP;
END
$$;

-- 5. (Optional) Make templar_process_user the OWNER of the database itself
--    so it can ALTER DATABASE-level settings.
ALTER DATABASE "templardb" OWNER TO templar_process_user;








