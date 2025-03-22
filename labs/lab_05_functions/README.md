# Lab 05: Functions, Arguments, and Return Values

## Objectives
- Understand function definition and invocation
- Master different types of arguments (positional, keyword, default, *args, **kwargs)
- Learn about function return values and multiple returns
- Practice function documentation and type hints
- Explore lambda functions and closures
- Understand function decorators

## Prerequisites
- Basic Python syntax
- Understanding of variables and data types
- Familiarity with control structures

## Exercises

### Exercise 1: Basic Functions and Arguments
Create a module `exercises/exercise1.py` with the following functions:

1. `calculate_bmi(weight: float, height: float) -> float`:
   - Calculate BMI using weight (kg) and height (m)
   - Return the calculated BMI
   - Include type hints and docstring

2. `greet(name: str, greeting: str = "Hello") -> str`:
   - Return a greeting message
   - Use default argument for greeting
   - Include type hints and docstring

3. `sum_numbers(*numbers: float) -> float`:
   - Accept variable number of arguments
   - Return sum of all numbers
   - Include type hints and docstring

4. `create_person(name: str, age: int, **kwargs) -> dict`:
   - Create a person dictionary with required and optional fields
   - Accept additional fields as keyword arguments
   - Include type hints and docstring

### Exercise 2: Advanced Function Features
Create a module `exercises/exercise2.py` with the following functions:

1. `fibonacci(n: int) -> list[int]`:
   - Generate Fibonacci sequence up to n terms
   - Use recursion
   - Include type hints and docstring

2. `counter() -> callable`:
   - Create a closure that maintains a count
   - Return a function that increments and returns the count
   - Include type hints and docstring

3. `validate_input(func: callable) -> callable`:
   - Create a decorator that validates function arguments
   - Check if arguments are positive numbers
   - Include type hints and docstring

4. `process_data(data: list[dict]) -> tuple[list, list]`:
   - Process a list of dictionaries
   - Return two lists: valid and invalid entries
   - Include type hints and docstring

### Exercise 3: Practical Applications
Create a module `exercises/exercise3.py` with the following functions:

1. `calculate_statistics(numbers: list[float]) -> dict[str, float]`:
   - Calculate mean, median, and mode
   - Return results as a dictionary
   - Include type hints and docstring

2. `filter_and_transform(data: list[dict]) -> list[dict]`:
   - Filter data based on conditions
   - Transform filtered data
   - Include type hints and docstring

3. `create_calculator() -> dict[str, callable]`:
   - Return a dictionary of mathematical operations
   - Include basic arithmetic operations
   - Use lambda functions
   - Include type hints and docstring

4. `async_process_data(data: list) -> list`:
   - Process data asynchronously
   - Use async/await syntax
   - Include type hints and docstring

## Testing
Create test files in the `tests` directory for each exercise:
- `test_exercise1.py`
- `test_exercise2.py`
- `test_exercise3.py`

Each test file should include:
- Unit tests for all functions
- Edge cases and error conditions
- Type checking tests
- Documentation tests

## Requirements
1. All functions must include:
   - Type hints
   - Docstrings (Google style)
   - Error handling
   - Input validation

2. Code must follow:
   - PEP 8 style guide
   - Type checking with mypy
   - Documentation with pydocstyle

3. Tests must cover:
   - Happy path scenarios
   - Edge cases
   - Error conditions
   - Type checking

## Submission
Submit the following files:
1. All exercise modules
2. All test files
3. Any additional documentation

## Grading Criteria
- Function implementation (40%)
- Type hints and documentation (20%)
- Test coverage (30%)
- Code style (10%) 