# Example Package

A Python package demonstrating proper package structure, module organization, and virtual environment management.

## Features

- Data processing and analysis
- Input validation and sanitization
- Output formatting
- Comprehensive test suite
- Type hints and documentation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/example_package.git
   cd example_package
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package:
   ```bash
   pip install -e .
   ```

## Development Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the setup script:
   ```bash
   ./setup_env.sh
   ```

## Usage

```python
from example_package.core.functions import process_data, analyze_data
from example_package.utils.helpers import format_output, validate_input

# Process data
data = {"key": "value"}
processed = process_data(data)

# Analyze data
analysis = analyze_data(processed)

# Format output
formatted = format_output(analysis, format_type="pretty")

# Validate input
schema = {"name": str, "age": int}
is_valid = validate_input({"name": "John", "age": 30}, schema)
```

## Testing

Run the test suite:
```bash
pytest
```

## Code Style

Check code style:
```bash
black .
isort .
```

## Type Checking

Run type checks:
```bash
mypy .
```

## Documentation

Check documentation:
```bash
pydocstyle .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 