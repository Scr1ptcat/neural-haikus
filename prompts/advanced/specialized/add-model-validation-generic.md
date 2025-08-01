Task: Scan All Models and Add Missing TypedDict/Validation
You are implementing a systematic scan to find all model files that lack TypedDict and validation, then adding this pattern to each one. Complete BOTH phases and do NOTHING else.
PHASE 1: Analysis - Find Models Without Validation
Scan ALL model files in:

airules/delta_spark/models/
All subdirectories (analysis/, reg_gov/, etc.)

Identify models that are missing ANY of:

Import of SchemaValidator
self.validator = SchemaValidator() in __init__
TypedDict definition for the model
self.validator.validate_record() call in transform method

Analysis Output Format:
yamlmodels_missing_validation:
  - file: "airules/delta_spark/models/analysis/example_model.py"
    class_name: "ExampleModel"
    table_name: "example_table"
    schema_constant: "EXAMPLE_MODEL_SCHEMA"
    missing_components:
      - "SchemaValidator import"
      - "self.validator initialization"
      - "TypedDict definition"
      - "validate_record call"
    
  - file: "airules/delta_spark/models/reg_gov/another_model.py"
    class_name: "AnotherModel"
    table_name: "another_table"
    schema_constant: "ANOTHER_MODEL_SCHEMA"
    missing_components:
      - "TypedDict definition"
      - "validate_record call"

summary:
  total_models_scanned: N
  models_missing_validation: N
  models_already_complete: N
Files to SKIP:

Abstract base classes (abstract_*.py)
Schema definition files (model_schema.py)
Utility files (schema_validator.py)
init.py files
Test files

PHASE 2: Implementation - Add Missing Components
For EACH model identified in Phase 1, add ONLY the missing components.
Your ONLY responsibilities:

Add TypedDict class if missing
Import SchemaValidator if missing
Add self.validator = SchemaValidator() if missing
Add validation call in transform method if missing
Make NO other changes

What NOT to do:

Do NOT create new files
Do NOT refactor existing logic
Do NOT add new features or methods
Do NOT optimize or improve existing code
Do NOT change method signatures
Do NOT add extensive documentation
Do NOT modify models that already have validation

The Pattern to Implement:
python# 1. Add these imports at the top (ONLY if missing)
from typing import TypedDict, Optional, List  # only what's needed
from datetime import datetime  # only if schema has timestamps
from airules.delta_spark.models.schema_validator import SchemaValidator

# 2. Add TypedDict before the class (ONLY if missing)
class YourModelDict(TypedDict, total=False):
    """Type hints for your_model - matches YOUR_MODEL_SCHEMA"""
    # Fields based on the schema

# 3. In __init__, add validator (ONLY if missing)
def __init__(self, spark: SparkSession, table_registry: DeltaTableRegistry):
    super().__init__(spark, "your_table_name", table_registry)
    self.validator = SchemaValidator()  # ADD THIS LINE ONLY IF MISSING

# 4. In transform method, add validation (ONLY if missing)
def transform(self, data: Union[Dict, Row, YourModelDict]) -> Dict:
    # ... existing transformation logic ...
    
    # Add validation right before the return statement
    self.validator.validate_record(transformed, self.schema)
    return transformed
Output Requirements:
1. ANALYSIS RESULTS
Show the complete scan results in YAML format as specified above.
2. IMPLEMENTATIONS
For EACH model that needs updates:
python# FILE: path/to/model.py
# MODEL: ModelClassName
# MISSING: [list of missing components]

# Show ONLY the changes needed:
# EXISTING: from typing import Dict, Union
# ADD: from typing import Dict, Union, TypedDict, Optional
# ADD: from airules.delta_spark.models.schema_validator import SchemaValidator

# ADD: class ModelNameDict(TypedDict, total=False):
# ADD:     """Type hints for model_name - matches MODEL_NAME_SCHEMA"""
# ADD:     field1: str
# ADD:     field2: Optional[int]

class ModelName(AbstractDeltaModel):
    def __init__(self, spark: SparkSession, table_registry: DeltaTableRegistry):
        # EXISTING: super().__init__(spark, "table_name", table_registry)
        # ADD: self.validator = SchemaValidator()
        
    def transform(self, data: Union[Dict, Row, ModelNameDict]) -> Dict:
        # EXISTING: ... transformation logic ...
        # EXISTING: return transformed_data
        # CHANGE TO:
        #     self.validator.validate_record(transformed_data, self.schema)
        #     return transformed_data
Search Strategy:

Find all .py files in models directory
Look for classes inheriting from AbstractDeltaModel
Check for presence of validation components
Skip files in the exclusion list

Example Search Patterns:

Missing import: File doesn't contain "from.*schema_validator import SchemaValidator"
Missing validator init: init doesn't contain "self.validator = SchemaValidator"
Missing TypedDict: No "class.*Dict.*TypedDict" before model class
Missing validation: transform method doesn't contain "validator.validate_record"

Remember: You are ONLY adding missing validation components. Do not modify models that already have complete validation.Chat controls Opus 4Powerful, large model for complex challenges Learn moreArtifacts
