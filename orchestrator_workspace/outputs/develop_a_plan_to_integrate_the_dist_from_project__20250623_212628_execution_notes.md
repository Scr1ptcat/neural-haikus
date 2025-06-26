Feature: Integrate project-extractor dist package and ensure it stays updated
  Complexity: Medium
  Estimated Time: 12-16 hours broken down by phase
  - Analysis: 2 hours (completed)
  - Implementation: 8-10 hours
    - Package integration: 2 hours
    - Scanner updates: 2 hours
    - Auto-update mechanism: 3-4 hours
    - Error handling & edge cases: 1-2 hours
  - Testing: 3 hours
  - Documentation: 1 hour

  Key Risks:
  - Virtual environment conflicts between development/production
  Mitigation: Support both package and script modes with runtime switching
  - File watching performance impact
  Mitigation: Make auto-update optional via config
  - Build failures blocking scans
  Mitigation: Maintain fallback to last working version
  - Cross-platform compatibility (file watching)
  Mitigation: Use watchdog library with platform abstraction

  Key Files to Focus On:
  - templar/scanner.py (line 158 - _run_extractor method)
  - templar/config.py (line 34 - PROJECT_EXTRACTOR_PATH)
  - NEW: templar/utils/extractor_manager.py
  - NEW: templar/services/update_watcher.py
  - project-extractor/build.sh
  - project-extractor/setup.py

  Similar Existing Features:
  - Database migration checking (version comparison pattern)
  - Redis connection management (fallback pattern)
  - Config hot-reloading (file watching pattern)

  Integration Points:
  - Scanner subprocess execution
  - Configuration loading
  - CLI initialization (for update checks)
  - API startup (for background watcher)

  Testing Strategy:
  - Mock project-extractor package for unit tests
  - Use temporary virtualenv for integration tests
  - Test both modes (package/script) in CI/CD
  - Performance benchmarks for scan times

  Performance Considerations:
  - Package import faster than subprocess Python startup
  - File watching should use efficient OS-level notifications
  - Cache version checks to avoid repeated file reads
  - Rebuild only when source files change (not docs/tests)

  Security Considerations:
  - Validate wheel integrity after build
  - Restrict file watching to project-extractor directory
  - Log all automatic rebuilds for audit trail
  - Ensure no arbitrary code execution from watched files

  Rollback Plan:
  - Environment variable to disable package mode
  - Keep script execution path as permanent fallback
  - Version tracking allows rollback to previous wheel
  - Document manual override procedures