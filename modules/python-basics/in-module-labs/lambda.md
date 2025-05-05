# Python Lambda Functions Lab

## Introduction
Lambda functions in Python are small, anonymous functions that can be created on the fly. They are useful for creating quick, one-time-use functions without formally defining them using `def`.

## Learning Objectives
- Understand the syntax and use cases of lambda functions
- Learn how to use lambda functions with built-in functions like `map()`, `filter()`, and `sorted()`
- Practice creating and using lambda functions in different scenarios

## Basic Syntax
```python
lambda arguments: expression
```

## Exercise 1: Basic Lambda Functions
Create lambda functions for the following operations:

1. A function that squares a number
2. A function that adds two numbers
3. A function that checks if a number is even


## Exercise 2: Using Lambda with map()
### In Python, map() is a built-in function used to apply another function to every item in an iterable (like a list). https://www.geeksforgeeks.org/python-map-function/
Use lambda functions with `map()` to:

1. Convert a list of temperatures from Celsius to Fahrenheit
2. Capitalize all strings in a list
3. Calculate the length of each string in a list


## Exercise 3: Using Lambda with filter()
### filter() is used to filter items from an iterable based on a condition. It keeps only the items for which the function returns True. https://www.w3schools.com/python/ref_func_filter.asp
Use lambda functions with `filter()` to:

1. Filter out even numbers from a list
2. Filter out strings that start with a vowel
3. Filter out negative numbers from a list


## Exercise 4: Using Lambda with sorted()
### sorted() is a built-in function that returns a new sorted list from the items of any iterable (like lists, tuples, or dictionaries), without changing the original. https://www.w3schools.com/python/ref_func_sorted.asp
Use lambda functions with `sorted()` to:

1. Sort a list of tuples by the second element
2. Sort a list of strings by their length
3. Sort a list of dictionaries by a specific key



## Challenge Exercise
Create a lambda function that:
1. Takes a list of dictionaries containing employee information
2. Returns a new list with only the names of employees who have a salary above a certain threshold
3. The output should be sorted alphabetically

```python
employees = [
    {'name': 'John', 'salary': 50000},
    {'name': 'Alice', 'salary': 75000},
    {'name': 'Bob', 'salary': 60000},
    {'name': 'Charlie', 'salary': 45000}
]

# Your solution here
```

## Best Practices
1. Use lambda functions for simple operations
2. Keep lambda functions short and readable
3. Use regular functions for complex operations
4. Document your code when using lambda functions in complex expressions

## Additional Resources
- [Python Lambda Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

