# Lab 06: Modules, Packages, and Virtual Environments

## Objectives
- Understand Python modules and their organization
- Learn about package creation and distribution
- Master virtual environment management
- Practice dependency management with pip
- Explore package installation and versioning
- Understand Python path and module imports

## Prerequisites
- Basic Python programming
- Understanding of file system operations
- Familiarity with command line operations

## Exercises

### Exercise 1: Module Creation and Import
Create a module `exercises/exercise1.py` with the following tasks:

1. Create a module with utility functions:
   - `calculate_area(shape: str, dimensions: dict) -> float`
   - `format_currency(amount: float, currency: str = "USD") -> str`
   - `validate_email(email: str) -> bool`

2. Create a separate module for constants:
   - Define mathematical constants (π, e, etc.)
   - Define currency exchange rates
   - Define validation patterns

3. Create a main script that:
   - Imports and uses the utility functions
   - Demonstrates different import methods
   - Handles import errors gracefully

### Exercise 2: Package Development
Create a package structure in `package_example/` with the following components:

1. Package Structure:
   ```
   package_example/
   ├── src/
   │   └── example_package/
   │       ├── __init__.py
   │       ├── core/
   │       │   ├── __init__.py
   │       │   └── functions.py
   │       └── utils/
   │           ├── __init__.py
   │           └── helpers.py
   ├── tests/
   │   └── test_package.py
   ├── setup.py
   ├── requirements.txt
   └── README.md
   ```

2. Package Components:
   - `setup.py`: Package configuration and dependencies
   - `requirements.txt`: Development dependencies
   - `README.md`: Package documentation
   - Core functionality in separate modules
   - Unit tests for package components

### Exercise 3: Virtual Environment Management
Create scripts to demonstrate virtual environment usage:

1. Environment Setup Script:
   - Create virtual environment
   - Install dependencies
   - Verify installation
   - Export requirements

2. Dependency Management:
   - Create requirements files
   - Handle version conflicts
   - Manage development dependencies
   - Use constraints files

3. Project Isolation:
   - Demonstrate package isolation
   - Show dependency conflicts
   - Handle multiple Python versions
   - Manage environment variables

## Testing
Create test files in the `tests` directory:
- `test_exercise1.py`: Tests for module functions
- `test_package.py`: Tests for package components

Each test file should include:
- Unit tests for all functions
- Import tests
- Package structure tests
- Environment tests

## Requirements
1. Code Organization:
   - Clear module structure
   - Proper package hierarchy
   - Consistent naming conventions
   - Documentation

2. Package Management:
   - Proper dependency specification
   - Version constraints
   - Development dependencies
   - Build configuration

3. Virtual Environment:
   - Environment isolation
   - Dependency management
   - Script automation
   - Cross-platform compatibility

## Submission
Submit the following:
1. All exercise modules
2. Package structure and files
3. Virtual environment scripts
4. Test files
5. Documentation

## Grading Criteria
- Module Implementation (30%)
- Package Structure (25%)
- Virtual Environment Setup (25%)
- Testing and Documentation (20%) 