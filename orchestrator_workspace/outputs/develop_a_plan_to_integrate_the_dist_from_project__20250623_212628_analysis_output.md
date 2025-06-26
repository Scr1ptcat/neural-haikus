  1. Architecture Overview

  System Design Pattern: Service-Oriented Architecture with Clean Separation
  - Core Pattern: Monolithic application with service layer abstraction
  - Entry Points:
    - CLI (templar.py → templar/cli.py) using Click framework
    - REST API (api/main.py) using FastAPI with lifespan management
  - Data Flow:
  User Request → CLI/API → Service Layer → External Tools → Database
                              ↓                ↓
                         Scanner.py    project-extractor
                              ↓                ↓
                         subprocess ←──────────┘

  Component Organization:
  templar/
  ├── Core Services (scanner.py, config.py, database.py)
  ├── Service Layer (services/*.py) - Optional features
  ├── Models (models/*.py) - Data structures
  └── Utilities (health_check.py) - Cross-cutting concerns

  api/
  ├── Routes (routes/*.py) - Endpoint definitions
  ├── Dependencies (dependencies.py) - DI setup
  └── Utils (utils/*.py) - API helpers

  2. Code Conventions Document

  Naming Standards:
  - Files: snake_case.py (e.g., semantic_embedder.py)
  - Classes: PascalCase (e.g., RepositoryScanner, DatabaseManager)
  - Functions/Methods: snake_case (e.g., scan_repository, _run_extractor)
  - Constants: UPPER_SNAKE_CASE (e.g., MAX_FILE_SIZE, SCAN_INTERVAL_MINUTES)

  Import Organization (strict order):
  # 1. Standard library
  import os
  from pathlib import Path
  from typing import Dict, List, Optional

  # 2. Third-party
  import psycopg2
  from fastapi import FastAPI

  # 3. Local imports (relative)
  from .config import Config
  from ..services.cache_manager import CacheManager

  Error Handling Pattern:
  # Validation at initialization
  if not path.exists():
      raise FileNotFoundError(f"Path not found: {path}")

  # Operation-specific handling
  try:
      result = subprocess.run(cmd, check=True, capture_output=True)
  except subprocess.CalledProcessError as e:
      logger.error(f"Command failed: {e.stderr}")
      raise  # Re-raise for caller to handle

  Logging Approach:
  logger = logging.getLogger(__name__)  # At module level
  logger.info(f"Starting operation on {target}")
  logger.error(f"Failed to process {item}: {error}")
  logger.debug(f"Detailed info: {debug_data}")

  3. Feature Integration Points

  Primary Integration: templar/scanner.py
  - Line 158-180: _run_extractor() method - Replace subprocess command
  - Line 30-33: Initialization - Add dist path checking
  - Line 106, 118: Version hardcoding - Make dynamic

  Configuration Integration: templar/config.py
  - Line 34: Add PROJECT_EXTRACTOR_DIST_PATH configuration
  - Line 50+: Add new environment variables:
  PROJECT_EXTRACTOR_MODE = os.getenv('PROJECT_EXTRACTOR_MODE', 'auto')
  PROJECT_EXTRACTOR_AUTO_UPDATE = os.getenv('PROJECT_EXTRACTOR_AUTO_UPDATE', 'false')

  Health Check Integration: templar/health_check.py
  - Line 414-419: Update check_project_extractor() to check dist first

  New Service Creation: templar/services/extractor_manager.py
  class ExtractorManager:
      def __init__(self):
          self.source_path = Config.PROJECT_EXTRACTOR_PATH
          self.dist_path = Config.PROJECT_EXTRACTOR_DIST_PATH

      def get_command(self) -> List[str]:
          # Return appropriate command based on mode/availability

      def check_version(self) -> str:
          # Get current version from dist or source

      def needs_update(self) -> bool:
          # Compare source and dist versions

  4. Testing Strategy

  Test Organization:
  tests/
  ├── unit/
  │   ├── test_scanner.py         # Mock subprocess calls
  │   └── test_extractor_manager.py  # New tests
  ├── integration/
  │   └── test_dist_integration.py   # End-to-end dist tests
  └── conftest.py                    # Shared fixtures

  Mock Pattern for Subprocess (test_scanner.py example):
  @patch('subprocess.run')
  def test_dist_execution(self, mock_run):
      mock_run.return_value = MagicMock(
          stdout='{"version": "2.1.0", "files": []}',
          stderr='',
          returncode=0
      )
      # Test dist-based execution

  Fixture Pattern:
  @pytest.fixture
  def mock_extractor_dist(tmp_path):
      """Create mock project-extractor dist"""
      dist_path = tmp_path / "dist" / "project-extractor"
      dist_path.parent.mkdir()
      dist_path.write_text("#!/usr/bin/env python3\n...")
      dist_path.chmod(0o755)
      return dist_path

  5. Implementation Readiness Checklist

  ✅ Prerequisites Confirmed:
  - project-extractor has build.sh script
  - Dist creates wheel at dist/project_extractor-2.1.0-py3-none-any.whl
  - Scanner uses subprocess pattern amenable to modification
  - Configuration system supports new variables

  ✅ Patterns Identified:
  - Service layer pattern for optional features
  - Graceful degradation for missing dependencies
  - Environment-based configuration
  - Comprehensive error handling with logging
  - Mock-based testing for external commands

  ✅ Integration Points Mapped:
  - scanner.py:_run_extractor() - Primary modification
  - config.py - New configuration variables
  - health_check.py - Dist availability checking
  - New service: extractor_manager.py

  ⚠️ Risks Documented:
  1. No existing file watching pattern - Will need to introduce new dependency
  2. No automatic update mechanisms - All updates are manual
  3. Hard-coded version - Currently "2.0.0" everywhere
  4. Virtual environment isolation - Need to handle pip install in correct env

  🔧 Implementation Notes:
  1. Follow existing subprocess pattern exactly
  2. Add feature flag for gradual rollout
  3. Maintain backward compatibility with script mode
  4. Use existing logging and error patterns
  5. Create comprehensive tests following existing patterns
  6. Update health checks to validate dist

  File Modification List:
  1. templar/config.py - Add new configurations
  2. templar/scanner.py - Update execution logic
  3. templar/health_check.py - Add dist checking
  4. NEW: templar/services/extractor_manager.py - Version/path management
  5. NEW: tests/unit/test_extractor_manager.py - Unit tests
  6. NEW: tests/integration/test_dist_integration.py - Integration tests
  7. README.md - Update setup instructions
  8. .env.example - Add new environment variables