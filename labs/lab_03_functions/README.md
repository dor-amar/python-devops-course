# Lab 03: Functions and Modules

This lab introduces you to Python's function system and module organization. You'll learn how to create reusable functions, work with different types of arguments, and organize code into modules.

## Learning Objectives

By the end of this lab, you will be able to:
- Create and use functions with different types of arguments
- Work with default parameters and keyword arguments
- Use lambda functions and function decorators
- Create and import custom modules
- Understand function scope and closures
- Use built-in Python modules effectively

## Exercises

### Exercise 1: Advanced Function Arguments
Create a program that:
1. Implements a function with different argument types:
   - Positional arguments
   - Keyword arguments
   - Default parameters
   - Variable-length arguments (*args, **kwargs)
2. Demonstrates function overloading using default parameters
3. Uses lambda functions for simple operations

### Exercise 2: Function Decorators and Closures
Create a program that:
1. Implements a timing decorator to measure function execution time
2. Creates a memoization decorator for caching function results
3. Uses closures to create function factories
4. Demonstrates decorator chaining

### Exercise 3: Custom Module Development
Create a module that:
1. Implements a set of related functions for string manipulation
2. Uses proper module organization (__init__.py, etc.)
3. Includes docstrings and type hints
4. Provides both public and private functions
5. Includes unit tests for the module

## Requirements

- Python 3.8 or higher
- pytest (for running tests)
- time module (built-in)
- functools module (built-in)

## Getting Started

1. Navigate to the `exercises` directory
2. Create your Python files for each exercise
3. Run the tests to verify your solutions:
   ```bash
   python -m pytest tests/
   ```

## Tips

- Use type hints for better code documentation
- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Consider function reusability
- Use meaningful parameter names
- Handle edge cases in your functions

## Submission

Submit your completed exercise files in the `exercises` directory. Make sure all tests pass before submitting. 