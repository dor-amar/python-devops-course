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

```python
# Example solution
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

## Exercise 2: Using Lambda with map()
Use lambda functions with `map()` to:

1. Convert a list of temperatures from Celsius to Fahrenheit
2. Capitalize all strings in a list
3. Calculate the length of each string in a list

```python
# Example solution
temperatures_c = [0, 10, 20, 30, 40]
temperatures_f = list(map(lambda c: (c * 9/5) + 32, temperatures_c))
print(temperatures_f)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
```

## Exercise 3: Using Lambda with filter()
Use lambda functions with `filter()` to:

1. Filter out even numbers from a list
2. Filter out strings that start with a vowel
3. Filter out negative numbers from a list

```python
# Example solution
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
```

## Exercise 4: Using Lambda with sorted()
Use lambda functions with `sorted()` to:

1. Sort a list of tuples by the second element
2. Sort a list of strings by their length
3. Sort a list of dictionaries by a specific key

```python
# Example solution
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
print(sorted_students)
```

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

