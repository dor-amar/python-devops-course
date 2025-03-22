# Lab 04: Object-Oriented Programming

This lab introduces you to Python's object-oriented programming features. You'll learn how to create classes, work with objects, implement inheritance, and use other OOP concepts.

## Learning Objectives

By the end of this lab, you will be able to:
- Create and use classes and objects
- Implement inheritance and polymorphism
- Work with class methods and static methods
- Use properties and descriptors
- Understand encapsulation and abstraction
- Implement operator overloading
- Use class decorators and metaclasses

## Exercises

### Exercise 1: Basic Classes and Objects
Create a program that:
1. Implements a class hierarchy for a library system:
   - Base class for library items (books, DVDs, etc.)
   - Derived classes for specific item types
   - Methods for checking out, returning, and managing items
2. Uses properties for data validation
3. Implements string representation methods
4. Uses class methods and static methods

### Exercise 2: Inheritance and Polymorphism
Create a program that:
1. Implements a shape hierarchy:
   - Abstract base class for shapes
   - Concrete classes for different shapes (circle, rectangle, etc.)
   - Methods for calculating area and perimeter
2. Uses abstract methods and properties
3. Implements operator overloading for shape operations
4. Demonstrates polymorphic behavior

### Exercise 3: Advanced OOP Concepts
Create a program that:
1. Implements a custom descriptor for data validation
2. Uses class decorators for method registration
3. Creates a metaclass for automatic method registration
4. Implements a singleton pattern
5. Uses composition and aggregation

## Requirements

- Python 3.8 or higher
- pytest (for running tests)
- abc module (built-in)
- dataclasses module (built-in)

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
- Consider encapsulation principles
- Use meaningful class and method names
- Handle edge cases in your methods
- Consider using dataclasses where appropriate

## Submission

Submit your completed exercise files in the `exercises` directory. Make sure all tests pass before submitting. 