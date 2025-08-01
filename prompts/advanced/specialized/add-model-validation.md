# TypedDict and Validation Implementation Prompt

## Task: Add TypedDict and Validation to Existing Model

You are implementing a specific pattern for adding type hints and validation to an existing PySpark model. Follow these instructions EXACTLY and do NOTHING else.

### Your ONLY responsibilities:
1. Add a TypedDict class that matches the existing schema
2. Import and use the existing SchemaValidator 
3. Update the transform method to include validation
4. Make NO other changes

### What NOT to do:
- Do NOT create new files
- Do NOT refactor existing logic
- Do NOT add new features or methods
- Do NOT optimize or improve existing code
- Do NOT add logging beyond what exists
- Do NOT change the schema definition
- Do NOT add docstrings beyond the TypedDict description
- Do NOT implement new validation logic - use SchemaValidator as-is

### The Pattern to Implement:

```python
# 1. Add these imports at the top (after existing imports)
from typing import TypedDict, Optional, List  # only what's needed
from datetime import datetime  # only if schema has timestamps
from airules.delta_spark.models.schema_validator import SchemaValidator

# 2. Add TypedDict before the class (match schema EXACTLY)
class YourModelDict(TypedDict, total=False):
    """Type hints for your_model - matches YOUR_MODEL_SCHEMA"""
    # Copy field names and types from the schema
    # Required fields (from schema where nullable=False)
    # Optional fields (from schema where nullable=True)

# 3. In __init__, add validator
def __init__(self, spark: SparkSession, table_registry: DeltaTableRegistry):
    super().__init__(spark, "your_table_name", table_registry)
    self.validator = SchemaValidator()  # ADD THIS LINE ONLY

# 4. In transform method, add validation before return
def transform(self, data: Union[Dict, Row, YourModelDict]) -> Dict:
    # ... existing transformation logic ...
    
    # Add validation right before the return statement
    self.validator.validate_record(transformed, self.schema)
    return transformed
```

### Model to Update:

attachment_extracted_text.py

### Schema Reference:
The model uses `ATTACHMENT_EXTRACTED_TEXT_SCHEMA` from `model_schema.py`. Create the TypedDict to match this schema's field names and types exactly.

### Output Requirements:
1. Show ONLY the modified sections of the file
2. Use diff-style comments to indicate changes:
   - `# ADD:` for new lines
   - `# EXISTING:` for context lines (unchanged)
3. Do not show the entire file
4. Do not explain what you're doing
5. Just show the code changes

### Example Output Format:
```python
# EXISTING: from typing import Dict, Union
# ADD: from typing import Dict, Union, TypedDict, Optional, List
# ADD: from airules.delta_spark.models.schema_validator import SchemaValidator

# ADD: class YourModelDict(TypedDict, total=False):
# ADD:     """Type hints for your_model - matches YOUR_MODEL_SCHEMA"""
# ADD:     field1: str
# ADD:     field2: Optional[int]

class YourModel(AbstractDeltaModel):
    def __init__(self, spark: SparkSession, table_registry: DeltaTableRegistry):
        # EXISTING: super().__init__(spark, "your_table", table_registry)
        # ADD: self.validator = SchemaValidator()
```

Remember: You are ONLY adding TypedDict and validation. Nothing else.
