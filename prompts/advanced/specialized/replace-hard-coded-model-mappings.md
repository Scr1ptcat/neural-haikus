# Transform Method Implementation and Analysis Prompt

## Task: Analyze Hard-coded Mappings, Add Transform Method, and Replace All Instances

You are implementing a specific refactoring pattern to centralize data transformation logic. This involves THREE phases that must be completed in order:

1. **PHASE 1: ANALYSIS** - Find ALL hard-coded field mappings for this model
2. **PHASE 2: IMPLEMENTATION** - Add transform method(s) to the model
3. **PHASE 3: REPLACEMENT** - Replace all found instances with transform calls

Complete ALL three phases. Do NOTHING else.

## PHASE 1: Deep Analysis

First, analyze the ENTIRE codebase to find ALL instances where this model's data is being manually mapped. Search for:

### Search Patterns:
1. **Direct dictionary creation** for this model:
   ```python
   # Look for patterns like:
   result = {
       "field_name": value,
       "another_field": another_value,
       # ... many fields matching the model schema
   }
   ```

2. **List building with append**:
   ```python
   # Look for patterns like:
   results = []
   for row in df.collect():
       results.append({
           "field": row.field,
           # ... field mapping
       })
   ```

3. **Manual Row/DataFrame field extraction**:
   ```python
   # Look for patterns like:
   data = {
       "id": row.id if hasattr(row, 'id') else row['id'],
       "name": row.asDict().get('name'),
       # ... etc
   }
   ```

4. **Write/upsert/save methods** calling the model with manually mapped data

### Where to Search:
- Pipeline files (`airules/pipelines/*.py`)
- CLI command files (`airules/cli/commands/*.py`)
- Test files that create test data
- Any file that imports this model class
- Files that reference the table name

### Analysis Scope:
- ONLY analyze for THIS specific model
- ONLY look for write/create/insert operations (not reads)
- ONLY report actual field mapping (not simple pass-through)
- Focus on production code (tests are lower priority)

### Analysis Output Format:
```yaml
hard_coded_mappings_found:
  - file: "path/to/file.py"
    line_range: "123-145"
    method: "method_name"
    pattern: "dict creation with 15 fields"
    fields_mapped: ["field1", "field2", "..."]
    
  - file: "another/file.py"
    line_range: "456-478"
    method: "another_method"
    pattern: "list append in for loop"
    fields_mapped: ["field1", "field2", "..."]
    
total_instances: 5
files_affected: 3
```

### Analysis Guidelines:

1. **Identify by Schema Fields**: Look for dictionaries containing fields that match the model's schema
2. **Check Imports**: Find files that import this model class
3. **Table Name References**: Search for the table name string
4. **Common Method Names**: Look for write*, save*, upsert*, insert*, create* methods
5. **DataFrame Operations**: Check for `.collect()` followed by dictionary creation
6. **Nested Field Access**: Watch for patterns like `data.get('nested', {}).get('field')`
7. **Loop Patterns**: Look for `for` loops that build lists of dicts matching the schema
8. **Dict Comprehensions**: Check for list/dict comprehensions creating model data

### Search Commands to Use:
- Search for the model class name
- Search for the table name
- Search for key field names from the schema
- Search for patterns like `append({` near model usage
- Search for `model.write` or `model.upsert` calls

### DO NOT Report:
- Simple field access without transformation
- Reading/querying operations
- Test data that uses completely different patterns
- Unrelated dictionary creation

### MUST Report:
- ANY location creating dicts that match the model schema
- Even if it "seems like initial data preparation"
- Even if it's "already in the right format"
- EVERY instance counts - no exceptions

## PHASE 2: Implementation

### Your ONLY responsibilities:
1. Add a `transform()` method to the model class
2. Add a `transform_batch()` method if the model processes multiple records
3. Make NO other changes to the model

## PHASE 3: Replacement

### Your ONLY responsibilities:
1. Replace ALL hard-coded field mappings found in Phase 1 with calls to transform
2. Simplify the calling code to use the model's transform methods
3. Make NO other changes

### CRITICAL REPLACEMENT RULES:
- **EVERY instance of manual dict creation that matches the model schema MUST be replaced**
- Do NOT skip replacements because "it's creating the initial dict" - that's EXACTLY what should be replaced
- Do NOT claim replacements are "unnecessary" - ALL hard-coded mappings must go
- The ONLY exception: Keep minimal fields that are truly external (like IDs from outside the model's domain)

### What Constitutes a Replacement:
If you see code like this:
```python
result = {
    "field1": data.get("field1"),
    "field2": data.get("field2", default),
    "field3": calculate_something(data),
    # ... many fields
}
model.write_something([result])
```

It MUST be replaced. The model's transform should handle ALL field mapping, defaults, and calculations.

### What NOT to do:
- Do NOT create new files or classes
- Do NOT add dataclasses or type hints beyond what exists
- Do NOT refactor unrelated code
- Do NOT optimize or improve existing logic
- Do NOT add validation beyond simple field transformation
- Do NOT change method signatures of existing methods
- Do NOT add extensive documentation
- Do NOT implement complex business logic

### Pattern to Implement:

```python
# 1. Add to the model class:
def transform(self, data: Union[Dict, Row]) -> Dict:
    """Transform input data to match the model schema."""
    if isinstance(data, Row):
        data = data.asDict()
    
    # Extract any nested fields
    # Apply defaults
    # Build transformed dict
    transformed = {
        "field1": data.get("field1"),
        "field2": data.get("field2", "default_value"),
        # ... map all fields from schema
    }
    
    # Validate if validator exists
    if hasattr(self, 'validator'):
        self.validator.validate_record(transformed, self.schema)
    
    return transformed

def transform_batch(self, records: List[Union[Dict, Row]]) -> DataFrame:
    """Transform a batch of records into a DataFrame."""
    transformed = [self.transform(record) for record in records]
    return self.spark.createDataFrame(transformed, schema=self.schema)

# 2. Update write methods to use transform:
def write_something(self, records: List[Union[Dict, Row]]) -> DataFrame:
    if not records:
        return None
    
    # REPLACE manual mapping with:
    df = self.transform_batch(records)
    self.write_table(df)
    return df
```

### Model to Analyze:

**Model File:**
attachment_extracted_text.py

The analysis phase will find all locations with hard-coded mappings for this model.

### Transformation Rules:

1. **Field Mapping**: Copy the EXACT field mapping logic from ALL locations found
2. **Nested Objects**: Handle with `.get()` chains or dict access
3. **Defaults**: Use the same defaults as the hard-coded versions
4. **Derived Fields**: Include any calculated fields (e.g., token counts)
5. **Timestamps**: Preserve timestamp logic (datetime.now() for created_at, etc.)
6. **Consolidate Logic**: If different locations use different logic for the same field, use the most complete version

**CRITICAL**: The transform method must handle ALL variations found across the codebase. If location A maps field X one way and location B maps it differently, the transform must support both patterns.

**IMPORTANT**: When replacing hard-coded mappings, ensure the transform method contains ALL the logic from the original mapping. Don't lose any field transformations, calculations, or defaults in the transition.

### Output Requirements:

Structure your response in THREE clear sections:

## 1. ANALYSIS RESULTS

```yaml
hard_coded_mappings_found:
  - file: "exact/path/to/file.py"
    line_range: "XXX-YYY"
    method: "method_name"
    pattern: "description of pattern"
    fields_mapped: [list of field names found]
    
  # ... all instances found
  
summary:
  total_instances: N
  files_affected: N
  common_patterns: ["pattern1", "pattern2"]
```

## 2. TRANSFORM IMPLEMENTATION

Show ONLY the transform methods to add to the model:

```python
# ADD to class YourModel:
def transform(self, data: Union[Dict, Row]) -> Dict:
    """Transform input data to match the model schema."""
    if isinstance(data, Row):
        data = data.asDict()
    
    # Include ALL field mappings found in analysis
    return {
        # ... all fields
    }
    
def transform_batch(self, records: List[Union[Dict, Row]]) -> DataFrame:
    """Transform a batch of records into a DataFrame."""
    transformed = [self.transform(record) for record in records]
    return self.spark.createDataFrame(transformed, schema=self.schema)

# If any write methods need updating in the model:
def write_something(self, records: List[Union[Dict, Row]]) -> DataFrame:
    # Show the update needed
```

## 3. REPLACEMENTS

For EACH location found in the analysis:
```python
# FILE: path/to/file.py
# METHOD: method_name
# LINES: XXX-YYY

# REPLACE:
predictions = []
for row in df.collect():
    predictions.append({
        "field1": row.field1,
        "field2": row.field2,
        # ... many fields
    })
model.write_something(predictions)

# WITH:
model.write_something(df.collect())
```

### Example Transformation:

If the hard-coded mapping looks like:
```python
prompt_metadata = row.prompt_metadata if hasattr(row, 'prompt_metadata') else {}
result = {
    "prediction_id": row.prediction_id,
    "prompt_id": prompt_metadata.get("prompt_id"),
    "tokens_used": len(row.raw_response.split()) if row.raw_response else 0,
    "created_at": datetime.now()
}
```

The transform method should be:
```python
def transform(self, data: Union[Dict, Row]) -> Dict:
    """Transform input data to match the model schema."""
    if isinstance(data, Row):
        data = data.asDict()
    
    prompt_metadata = data.get('prompt_metadata', {})
    
    return {
        "prediction_id": data.get("prediction_id"),
        "prompt_id": prompt_metadata.get("prompt_id"),
        "tokens_used": len(data.get("raw_response", "").split()) if data.get("raw_response") else 0,
        "created_at": datetime.now()
    }
```

Remember: You are ONLY adding transform methods and replacing hard-coded mappings. Nothing else.

### FINAL CHECKLIST:
- [ ] Found ALL hard-coded mappings in Phase 1
- [ ] Created transform method that handles ALL found patterns
- [ ] Replaced EVERY SINGLE hard-coded mapping instance
- [ ] Did NOT skip any replacements as "unnecessary"
- [ ] Did NOT leave any manual field mapping in place

If you find yourself thinking "this replacement isn't necessary" - STOP. It IS necessary. The entire point is to centralize ALL field mapping logic in the model's transform method.

### Complete Example Output:

## 1. ANALYSIS RESULTS

```yaml
hard_coded_mappings_found:
  - file: "airules/pipelines/predictive_token_pipeline.py"
    line_range: "401-421"
    method: "_write_results"
    pattern: "list append with dict creation in for loop"
    fields_mapped: ["prediction_id", "docket_id", "comment_id", "predicted_topics", 
                    "prediction_confidence", "raw_response", "prompt_id", "prompt_version",
                    "prompt_type", "provider_name", "model_name", "tokens_used",
                    "prediction_timestamp", "error_message", "processing_duration_ms",
                    "http_status", "error_type", "retry_count"]
    
  - file: "airules/cli/commands/predictive_token.py"
    line_range: "418-437"
    method: "_save_to_delta_lake"
    pattern: "direct dict creation"
    fields_mapped: ["prediction_id", "docket_id", "comment_id", ...]
    
summary:
  total_instances: 2
  files_affected: 2
  common_patterns: ["nested prompt_metadata access", "datetime.now() for timestamps"]
```

## 2. TRANSFORM IMPLEMENTATION

```python
# ADD to class PredictiveTokens:
def transform(self, data: Union[Dict, Row]) -> Dict:
    """Transform input data to match the model schema."""
    if isinstance(data, Row):
        data = data.asDict()
    
    # Handle nested prompt metadata
    prompt_metadata = data.get('prompt_metadata', {})
    
    return {
        "prediction_id": data.get("prediction_id"),
        "docket_id": data.get("docket_id"),
        # ... all 18 fields based on analysis
    }

def transform_batch(self, records: List[Union[Dict, Row]]) -> DataFrame:
    """Transform a batch of records into a DataFrame."""
    transformed = [self.transform(record) for record in records]
    return self.spark.createDataFrame(transformed, schema=self.schema)
```

## 3. REPLACEMENTS

```python
# FILE: airules/pipelines/predictive_token_pipeline.py
# METHOD: _write_results
# LINES: 401-421

# REPLACE:
predictions = []
for row in df.collect():
    prompt_metadata = row.prompt_metadata if hasattr(row, 'prompt_metadata') else {}
    predictions.append({
        "prediction_id": row.prediction_id,
        # ... 17 more fields
    })
model.upsert_predictions(predictions)

# WITH:
model.upsert_predictions(df.collect())
```
