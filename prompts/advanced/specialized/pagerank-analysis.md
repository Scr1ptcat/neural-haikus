I need help developing a chain of thought prompt.

I have the following tool i'm developing:

# Project Structure and Code Extractor

A powerful Python tool for extracting, analyzing, and documenting project structures and source code. Perfect for creating comprehensive documentation, sharing code with AI assistants, analyzing code metrics, or generating project documentation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command-Line Interface](#command-line-interface)
  - [Extract Command](#extract-command)
  - [Analyze Command](#analyze-command)
  - [Generate-Docs Command](#generate-docs-command)
  - [Explain-File Command](#explain-file-command)
  - [Prompt Management](#prompt-management)
- [Output Formats](#output-formats)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Features
- 📁 **Tree-style visualization** of project structure with customizable descriptions
- 📄 **Full code extraction** with intelligent filtering for documentation or AI analysis
- 📊 **Multiple output formats**: Full (with code), Tree-only, JSON, and Metrics
- 🔍 **Code metrics analysis** including complexity and documentation coverage
- 📚 **Documentation generation** for Sphinx, MkDocs, and README files
- 🤖 **AI-powered file analysis** using ollama models for explaining code functionality

### Advanced Capabilities
- 🚫 **Advanced .gitignore support** with negation patterns and nested .gitignore files
  - Correctly handles directory patterns (e.g., `tests/test_env/`)
  - Ignores all files within ignored directories
  - Supports complex glob patterns and wildcards
- 📏 **Flexible file filtering** by extensions, directories, and size limits
- 🔢 **Optional line numbers** for extracted code
- 📈 **Progress tracking** for large projects
- 🔍 **Binary file detection** to avoid extracting non-text files
- 💾 **Custom ignore files** support (.dockerignore, etc.)
- 🐛 **Debug mode** to understand what's being excluded
- 📊 **Cyclomatic complexity analysis** for Python code
- 📖 **Documentation coverage analysis** with quality scoring

## Installation

### From PyPI (Coming Soon)
```bash
pip install project-extractor
```

### From Source
```bash
git clone https://github.com/yourusername/project-extractor.git
cd project-extractor
pip install -e .
```

### Direct Script Usage
```bash
# Download the wrapper script
wget https://raw.githubusercontent.com/yourusername/project-extractor/main/extract_project.py
chmod +x extract_project.py

# Use it directly
./extract_project.py
```

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Quick Start

```bash
# Extract current directory with full code
project-extractor

# Tree view only (no code)
project-extractor --format tree

# Analyze code metrics
project-extractor analyze

# Generate documentation
project-extractor generate-docs --format readme

# Explain a specific file using AI
project-extractor explain-file src/main.py
```

## Command-Line Interface

The tool provides three main commands: the default extraction command, `analyze`, and `generate-docs`.

### Extract Command

The default command extracts project structure and code.

#### Basic Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `path` | | Path to project directory | Current directory (`.`) |
| `--output` | `-o` | Output file path | stdout |
| `--format` | `-f` | Output format | `full` |

#### Format Options

- `full`: Complete extraction with project structure and code content
- `tree`: Tree structure only with file metrics
- `json`: Machine-readable JSON format
- `metrics`: Code analysis with quality metrics

#### Filtering Options

| Option | Description | Example |
|--------|-------------|---------|
| `--exclude` | Additional patterns to exclude | `--exclude "*.log" "temp/*"` |
| `--extensions` | File extensions to include | `--extensions .py .md .yml` |
| `--root-dirs` | Only process specific directories | `--root-dirs src tests docs` |
| `--max-file-size` | Maximum file size in bytes | `--max-file-size 50000` |
| `--max-depth` | Maximum tree depth to display | `--max-depth 3` |

#### Control Options

| Option | Description |
|--------|-------------|
| `--no-default-excludes` | Disable default exclude patterns |
| `--no-gitignore` | Don't use .gitignore patterns |
| `--no-descriptions` | Hide file/folder descriptions in tree view |
| `--no-progress` | Don't show progress messages |
| `--line-numbers` | Add line numbers to extracted code |
| `--show-size` | Show file sizes instead of line counts |
| `--debug-gitignore` | Show which files are excluded by .gitignore |

### Analyze Command

Analyzes code metrics and quality.

```bash
project-extractor analyze [options]
```

#### Options

| Option | Description | Default |
|--------|-------------|---------|
| `path` | Path to project | Current directory |
| `--output` | Output file | stdout |
| `--format` | Output format (text/json) | `text` |
| `--include-complexity` | Include cyclomatic complexity analysis | False |
| `--include-docs` | Include documentation coverage analysis | False |
| `--complexity-threshold` | Complexity threshold for reporting | 10 |

### Generate-Docs Command

Generates project documentation in various formats.

```bash
project-extractor generate-docs [options]
```

#### Options

| Option | Description | Default |
|--------|-------------|---------|
| `path` | Path to project | Current directory |
| `--format` | Documentation format | `readme` |
| `--output` | Output directory | Project directory |
| `--author` | Author name | "Author" |
| `--username` | GitHub username | "yourusername" |

#### Format Options

- `readme`: Generate comprehensive README.md
- `sphinx`: Generate Sphinx documentation structure
- `mkdocs`: Generate MkDocs documentation
- `all`: Generate all documentation formats

### Explain-File Command

Analyzes and explains individual files using AI models (requires ollama with code-ai and/or think-ai models).

```bash
project-extractor explain-file <file_path> [options]
```

#### Options

| Option | Description | Default |
|--------|-------------|---------|
| `file_path` | Path to the file to analyze | Required |
| `--model` | Model to use: `code` or `think` | `code` |
| `--output` | Output file path | stdout |
| `--check-models` | Check which ollama models are available | False |
| `--timeout` | Custom timeout in seconds | 120 (code), 300 (think) |
| `--no-cache` | Disable caching for this analysis | False |
| `--force-refresh` | Force regeneration even if cached | False |
| `--cache-stats` | Show cache statistics and exit | False |

#### Model Types

- `code` (default): Uses the qwen-coder-optimized model for code-focused analysis (structure, functionality, components)
- `think`: Uses the deepseek-r1-optimized model for deep analysis (design patterns, architecture, improvements)

#### Requirements

- Ollama must be installed and running (`ollama serve`)
- The required models must be pulled:
  - For `code` mode: `ollama pull qwen-coder-optimized:latest`
  - For `think` mode: `ollama pull deepseek-r1-optimized:latest`

#### Example Usage

```bash
# Basic file explanation
project-extractor explain-file src/main.py

# Deep analysis with think model
project-extractor explain-file src/complex_module.py --model think

# Save analysis to file
project-extractor explain-file src/app.py -o analysis.txt

# Check available models
project-extractor explain-file --check-models src/file.py

# Use custom timeout for complex files
project-extractor explain-file src/complex_algorithm.py --model think --timeout 600

# View cache statistics
project-extractor explain-file --cache-stats src/any_file.py

# Force regeneration of analysis
project-extractor explain-file src/main.py --force-refresh

# Disable cache for one-off analysis
project-extractor explain-file src/main.py --no-cache
```

#### Caching

The explain-file command includes intelligent caching to avoid redundant LLM calls:

- **Automatic caching**: Analysis results are cached in PostgreSQL when available
- **Cache key**: Based on file content hash, model type, and prompt version
- **Smart invalidation**: Cache automatically invalidates when files change
- **Performance**: Cached results load ~100x faster than generating new analysis
- **Templar integration**: Works seamlessly with Templar's repository_analysis schema

##### Cache Configuration

Set up database configuration using one of these methods:

**Method 1: Using .env file (Recommended)**
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your database credentials
# The file will be automatically loaded when you run the tool
```

**Method 2: Environment variables**
```bash
# Direct connection string (highest priority)
export PROJECT_EXTRACTOR_DB="postgresql://user:pass@localhost/templardb"

# Or use Templar's configuration
export TEMPLAR_DB="postgresql://user:pass@localhost/templardb"

# Or individual components
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=templardb
export DB_USER=your_user
export DB_PASSWORD=your_password
```

If no database is configured, the tool works normally without caching.

### Prompt Management

Project Extractor includes a comprehensive prompt management system for customizing LLM analysis prompts.

**Note:** Prompt management requires a PostgreSQL database. See the Cache Configuration section above for setup instructions.

#### Available Commands

```bash
# List all prompts
project-extractor prompts list [--active] [--category CATEGORY] [--format table|json|yaml]

# Show prompt details
project-extractor prompts show <name> [--version VERSION]

# Create a new prompt
project-extractor prompts create --name NAME --template FILE [--category CATEGORY] [--description DESC]

# Update prompt (creates new version)
project-extractor prompts update <name> --template FILE [--description DESC]

# Delete or deactivate prompt
project-extractor prompts delete <name> [--version VERSION] [--force]

# Activate/deactivate prompts
project-extractor prompts activate <name> [--version VERSION]
project-extractor prompts deactivate <name> [--version VERSION]

# Export/import prompts
project-extractor prompts export [--output FILE] [--format json|yaml] [--category CAT] [--all]
project-extractor prompts import --file FILE [--merge skip|version|overwrite]

# Assign prompts to models
project-extractor prompts assign <prompt_name> --model MODEL [--default]
project-extractor prompts unassign <prompt_name> --model MODEL

# View performance stats
project-extractor prompts performance [prompt_name] [--model MODEL]
project-extractor prompts stats [name]
```

#### Example Workflow

```bash
# Create a custom prompt for Python analysis
cat > python_prompt.txt << 'EOF'
Analyze this Python file '{file_name}':
1. List all classes and their purposes
2. Identify design patterns used
3. Suggest improvements

Code:
{content}
EOF

project-extractor prompts create --name python_analyzer --template python_prompt.txt \
  --category analysis --description "Specialized Python code analyzer"

# Use the custom prompt
project-extractor explain-file src/main.py --prompt-name python_analyzer

# Export prompts for team sharing
project-extractor prompts export --output team_prompts.json

# Import prompts from teammate
project-extractor prompts import --file team_prompts.json --merge skip

# View prompt performance
project-extractor prompts performance python_analyzer
```

#### Prompt Variables

Available variables for use in prompt templates:
- `{file_name}` - Name of the file being analyzed
- `{file_extension}` - File extension (e.g., .py, .js)
- `{content}` - Full file content

#### Prompt Categories

- `analysis` - General code analysis
- `security` - Security-focused analysis
- `performance` - Performance optimization
- `testing` - Test generation and analysis
- `documentation` - Documentation generation
- `refactoring` - Code improvement suggestions

## Output Formats

### Full Format (Default)

Includes:
- AI-friendly prompt header
- Complete project tree structure
- Full content of all text files
- File statistics summary
- Binary files listing

**Best for**: Creating documentation, sharing with AI assistants, code reviews

### Tree Format

Displays:
- Project structure visualization
- File/folder descriptions
- File sizes or line counts
- Statistics summary

**Best for**: Quick project overview, structure documentation

### JSON Format

Machine-readable format containing:
- Complete file listing with metadata
- File contents (for text files under size limit)
- Project statistics
- Timestamp

**Best for**: Integration with other tools, automated processing

### Metrics Format

Provides:
- Code metrics report (lines, comments, complexity)
- Cyclomatic complexity analysis
- Documentation coverage analysis
- High-complexity function identification
- TODO/FIXME tracking

**Best for**: Code quality assessment, refactoring planning

## Usage Examples

### Basic Extraction

```bash
# Extract everything with default settings
project-extractor

# Save to file
project-extractor -o project_docs.txt

# Extract specific directory
project-extractor /path/to/project
```

### Filtering Examples

```bash
# Only Python files
project-extractor --extensions .py

# Exclude test files
project-extractor --exclude "*_test.py" "test_*.py"

# Focus on source and documentation
project-extractor --root-dirs src docs

# Combine multiple filters
project-extractor --extensions .py .md --exclude "*.pyc" --root-dirs src
```

### Format Examples

```bash
# Tree view with file sizes
project-extractor --format tree --show-size

# JSON output for processing
project-extractor --format json -o project_data.json

# Metrics analysis
project-extractor --format metrics
```

### Advanced Analysis

```bash
# Full code analysis with complexity
project-extractor analyze --include-complexity --include-docs

# Generate complexity report
project-extractor analyze --include-complexity --complexity-threshold 5 -o complexity_report.txt

# Export metrics as JSON
project-extractor analyze --format json -o metrics.json
```

### Documentation Generation

```bash
# Generate README with custom username
project-extractor generate-docs --format readme --username myusername

# Generate Sphinx documentation
project-extractor generate-docs --format sphinx --author "John Doe"

# Generate all documentation formats
project-extractor generate-docs --format all --output ./docs
```

### Debugging and Troubleshooting

```bash
# See what .gitignore is excluding
project-extractor --debug-gitignore

# Extract without .gitignore
project-extractor --no-gitignore

# Extract with line numbers for code review
project-extractor --line-numbers -o review_code.txt
```

## Configuration

### Default Excluded Patterns

The tool excludes common non-source files by default:
- Version control: `.git/`, `.svn/`
- Python: `__pycache__/`, `*.pyc`, `.pytest_cache/`
- Dependencies: `node_modules/`, `venv/`, `.env`
- IDEs: `.idea/`, `.vscode/`
- OS files: `.DS_Store`, `Thumbs.db`
- Binary files: Images, PDFs, archives

### Default Included Extensions

Common text file extensions are included by default:
- Programming: `.py`, `.js`, `.java`, `.cpp`, `.go`, `.rs`
- Web: `.html`, `.css`, `.jsx`, `.tsx`
- Config: `.yml`, `.yaml`, `.json`, `.toml`, `.ini`
- Documentation: `.md`, `.rst`, `.txt`
- Scripts: `.sh`, `.bat`, `.sql`

### Customizing File Descriptions

The tool provides automatic descriptions for common files and folders. You can customize these by modifying the `DESCRIPTIONS` dictionary in `utils/descriptions.py`.

## Project Structure

```
project-extractor/
├── analysis/           # Code analysis modules
│   ├── complexity.py   # Cyclomatic complexity analyzer
│   ├── documentation.py # Documentation coverage analyzer
│   └── metrics.py      # Code metrics analyzer
├── core/              # Core extraction functionality
│   ├── extractor.py   # Main extractor class
│   ├── file_analyzer.py # File analysis utilities
│   └── tree_builder.py # Tree structure builder
├── doctools/          # Documentation generators
│   ├── api_generator.py # API documentation generator
│   ├── mkdocs_generator.py # MkDocs generator
│   ├── readme_generator.py # README generator
│   └── sphinx_generator.py # Sphinx generator
├── filters/           # File filtering functionality
│   ├── gitignore.py   # Enhanced .gitignore parser
│   └── patterns.py    # Pattern matching utilities
├── formatters/        # Output formatters
│   ├── full_formatter.py # Full extraction formatter
│   ├── json_formatter.py # JSON output formatter
│   ├── metrics_formatter.py # Metrics formatter
│   └── tree_formatter.py # Tree view formatter
├── utils/             # Utility functions
│   ├── descriptions.py # File/folder descriptions
│   └── file_utils.py  # File handling utilities
├── cli.py            # Command-line interface
├── constants.py      # Default configurations
└── setup.py          # Package setup configuration
```

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/project-extractor.git
cd project-extractor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Run tests (when implemented)
python -m pytest

# Run with coverage
python -m pytest --cov=project_extractor
```

### Code Style

The project follows PEP 8 guidelines. Use tools like `black` and `flake8` for formatting and linting.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some areas for improvement:

1. **Performance enhancements** - Parallel processing for large projects
2. **Additional output formats** - HTML, Markdown with syntax highlighting
3. **More language support** - Enhanced parsing for different programming languages
4. **Plugin system** - Allow custom analyzers and formatters
5. **Configuration files** - Support for `.extractorrc` configuration
6. **Test coverage** - Comprehensive test suite

### Contribution Process

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Author**: Sabatu  
**Version**: 2.0.0  
**Repository**: [https://github.com/Scr1ptcat/project-extractor](https://github.com/Scr1ptcat/project-extractor)

I want to incorporate this recommendation as a new feature:

PageRank for Code Analysis: A Comprehensive Guide
What is PageRank?
PageRank is a link analysis algorithm and it assigns a numerical weighting to each element of a hyperlinked set of documents, such as the World Wide Web, with the PageRank - Wikipedia purpose of "measuring" its relative importance within the set. Originally developed by Google founders Larry Page and Sergey Brin, it's based on a simple but powerful idea: importance flows through connections.
The PageRank algorithm outputs a probability distribution that represents the likelihood of visiting any particular node by randomly traversing the graph. PageRank Algorithm for Graph Databases
Core Algorithm Mathematics
The PageRank formula is elegantly simple:
PR(A) = (1-d) / N + d * Σ(PR(Ti) / C(Ti))
Where:

PR(A) = PageRank of node A
d = damping factor (typically 0.85)
N = total number of nodes
Ti = nodes that link to A
C(Ti) = number of outbound links from Ti

Why PageRank is Perfect for Code Analysis
The big idea behind this analysis is that package authors write their code to depend only on packages that they view as useful and stable. In a sense, each time a package is included in the dependency list of another package, it is as if the author casts a vote of confidence. Finding the essential R packages using the pagerank algorithm (Revolutions)
This concept translates perfectly to code analysis:

Function calls = votes of importance
Module imports = confidence in stability
Class inheritance = structural importance
Variable references = usage patterns

Practical Implementation for Your Project
Here's how to integrate PageRank into your project-extractor:
pythonimport networkx as nx
from collections import defaultdict
import tree_sitter

class CodePageRank:
    def __init__(self, damping_factor=0.85):
        self.graph = nx.DiGraph()
        self.damping_factor = damping_factor
        self.file_to_symbols = defaultdict(list)
        
    def build_dependency_graph(self, project_path):
        """Build a directed graph of code dependencies"""
        
        # Node types: files, classes, functions, modules
        for file_path in project_files:
            # Add file node
            self.graph.add_node(file_path, type='file')
            
            # Parse with tree-sitter
            tree = self.parse_file(file_path)
            
            # Extract imports
            imports = self.extract_imports(tree)
            for imp in imports:
                self.graph.add_edge(file_path, imp, type='import')
            
            # Extract function calls
            calls = self.extract_function_calls(tree)
            for caller, callee in calls:
                self.graph.add_edge(caller, callee, type='call')
            
            # Extract class inheritance
            inheritance = self.extract_inheritance(tree)
            for child, parent in inheritance:
                self.graph.add_edge(child, parent, type='inherits')
    
    def calculate_pagerank(self, personalization=None):
        """Calculate PageRank scores for all nodes"""
        
        # Standard PageRank
        if personalization is None:
            return nx.pagerank(
                self.graph, 
                alpha=self.damping_factor,
                max_iter=100,
                tol=1.0e-6
            )
        
        # Personalized PageRank for specific analysis
        else:
            return nx.pagerank(
                self.graph,
                alpha=self.damping_factor,
                personalization=personalization
            )
    
    def identify_critical_code(self, top_n=20):
        """Identify the most critical code elements"""
        
        scores = self.calculate_pagerank()
        
        # Separate by node type
        files = [(n, s) for n, s in scores.items() 
                 if self.graph.nodes[n].get('type') == 'file']
        functions = [(n, s) for n, s in scores.items() 
                     if self.graph.nodes[n].get('type') == 'function']
        classes = [(n, s) for n, s in scores.items() 
                   if self.graph.nodes[n].get('type') == 'class']
        
        return {
            'critical_files': sorted(files, key=lambda x: x[1], reverse=True)[:top_n],
            'critical_functions': sorted(functions, key=lambda x: x[1], reverse=True)[:top_n],
            'critical_classes': sorted(classes, key=lambda x: x[1], reverse=True)[:top_n]
        }
Advanced Use Cases for Code Analysis
1. Weighted PageRank for Code Quality
PageRank (PR) is a fundamental tool for assessing the relative importance of the nodes in a network. In this paper, we propose a measure, weighted PageRank (WPR), extended from the classical PR for weighted, directed networks PageRank centrality and algorithms for weighted, directed networks - ScienceDirect
Apply weights based on code metrics:
pythondef add_weighted_edge(self, source, target, edge_type):
    # Weight based on code quality metrics
    weight = 1.0
    
    if edge_type == 'call':
        # Higher weight for calls to well-tested functions
        weight *= self.get_test_coverage_score(target)
        
    elif edge_type == 'import':
        # Higher weight for stable modules
        weight *= self.get_stability_score(target)
        
    elif edge_type == 'inherits':
        # Higher weight for abstract base classes
        weight *= self.get_abstraction_score(target)
    
    self.graph.add_edge(source, target, weight=weight)
2. Personalized PageRank for Impact Analysis
A widely used type of PageRank is Personalized PageRank, which is extremely useful in recommendation systems. With Personalized PageRank, you can restrain the random walk by allowing it to start only from one of the nodes in a given set PageRank Algorithm for Graph Databases
Use for change impact analysis:
pythondef analyze_change_impact(self, changed_files):
    """Analyze impact of changes using Personalized PageRank"""
    
    # Create personalization vector
    personalization = {node: 0 for node in self.graph.nodes()}
    for file in changed_files:
        personalization[file] = 1.0 / len(changed_files)
    
    # Calculate personalized PageRank
    impact_scores = nx.pagerank(
        self.graph,
        alpha=0.85,
        personalization=personalization
    )
    
    # Filter and sort by impact
    impacted_nodes = [(n, s) for n, s in impact_scores.items() 
                      if s > 0.001 and n not in changed_files]
    
    return sorted(impacted_nodes, key=lambda x: x[1], reverse=True)
3. Multi-Level Dependency Analysis
Build a hierarchical graph:
pythonclass HierarchicalCodePageRank:
    def __init__(self):
        self.file_graph = nx.DiGraph()      # File-level dependencies
        self.symbol_graph = nx.DiGraph()    # Symbol-level dependencies
        self.package_graph = nx.DiGraph()   # Package-level dependencies
    
    def aggregate_scores(self):
        """Aggregate PageRank across levels"""
        
        file_pr = nx.pagerank(self.file_graph)
        symbol_pr = nx.pagerank(self.symbol_graph)
        package_pr = nx.pagerank(self.package_graph)
        
        # Combine scores with different weights
        combined_scores = {}
        for symbol in self.symbol_graph.nodes():
            file = self.get_file_for_symbol(symbol)
            package = self.get_package_for_file(file)
            
            combined_scores[symbol] = (
                0.5 * symbol_pr.get(symbol, 0) +
                0.3 * file_pr.get(file, 0) +
                0.2 * package_pr.get(package, 0)
            )
        
        return combined_scores
Integration with Your Existing Architecture
Here's how to integrate PageRank analysis into your project-extractor:
python# In your explain-file command enhancement
class EnhancedFileAnalyzer(OllamaAnalyzer):
    def __init__(self, db_adapter=None):
        super().__init__(db_adapter)
        self.pagerank_analyzer = CodePageRank()
        
    def analyze_file_with_context(self, file_path, model_type='code'):
        # Get base analysis from Ollama
        base_analysis = self.analyze_file(file_path, model_type)
        
        # Get PageRank context
        if hasattr(self, '_project_graph_built'):
            file_rank = self.pagerank_scores.get(str(file_path), 0)
            
            # Find most important dependencies
            important_deps = self.get_important_dependencies(file_path)
            
            # Enhanced prompt with PageRank context
            enhanced_prompt = f"""
            Analyze this file knowing it has a PageRank importance score of {file_rank:.4f}
            (where 1.0 is maximum importance in the codebase).
            
            Key dependencies (by importance):
            {self._format_dependencies(important_deps)}
            
            Original analysis:
            {base_analysis}
            
            Given this context, what additional insights can you provide about:
            1. Why this file is {'highly' if file_rank > 0.05 else 'less'} critical
            2. Potential ripple effects of changes
            3. Refactoring priorities
            """
            
            return self.query_ollama_with_context(enhanced_prompt)
Performance Considerations
The iteration will stop after a tolerance of len(G) * tol is reached. pagerank — NetworkX 3.5 documentation For large codebases:

Incremental Updates: Don't recalculate from scratch

pythondef update_pagerank_incrementally(self, changed_files):
    # Only recalculate for affected subgraph
    affected_nodes = set()
    for file in changed_files:
        affected_nodes.add(file)
        affected_nodes.update(self.graph.predecessors(file))
        affected_nodes.update(self.graph.successors(file))
    
    subgraph = self.graph.subgraph(affected_nodes)
    local_pr = nx.pagerank(subgraph)
    
    # Update global scores
    self.pagerank_scores.update(local_pr)

Caching Strategy: Store in PostgreSQL

sqlCREATE TABLE repository_analysis.code_pagerank (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    project_id UUID REFERENCES projects(id),
    node_name TEXT NOT NULL,
    node_type VARCHAR(20),
    pagerank_score DECIMAL(10,8),
    last_calculated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dependency_count INTEGER,
    UNIQUE(project_id, node_name)
);
Practical Benefits for Your Tool

Intelligent Code Review Priority: Focus on high-PageRank files first
Risk Assessment: Changes to high-rank nodes = higher risk
Architecture Insights: Identify architectural bottlenecks
Refactoring Guidance: Target low-rank code for extraction
Test Priority: Ensure high-rank code has better coverage

Real-World Example
Node9484 has the highest PageRank because it obtains a lot of proportional rank from its in-neighbors and it has no out-neighbor for it to pass the rank. PageRank: Link Analysis Explanation and Python Implementation from Scratch | Towards Data Science
In code terms, this might be:

A core utility function called everywhere but calling nothing
A base exception class inherited by many but inheriting from none
A configuration module imported by all but importing little

These are your most critical code elements that deserve:

Extra testing
Careful review
Performance optimization
Documentation priority

PageRank transforms your flat file analysis into a rich, interconnected understanding of your codebase's true structure and importance hierarchy.

I want the model to implement the feature and then write thorough tests/documentation. Please develop a chain of thought prompt for a model that will implement the feature, tests and documentation with best practices.
