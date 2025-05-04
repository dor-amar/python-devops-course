# Python Generators and Yield Lab

## Introduction
This lab will help you practice using Python generators and the `yield` keyword. You'll work through exercises that demonstrate the power of generators for memory-efficient data processing.

## Learning Objectives
- Understand how generators work
- Implement memory-efficient data processing
- Create custom generators
- Work with infinite sequences
- Process large files efficiently

## Exercise 1: Fibonacci Generator
Create a generator function that yields the Fibonacci sequence. The function should:
- Accept an optional parameter for the maximum number of terms
- If no maximum is provided, generate an infinite sequence
- Each call should yield the next number in the sequence

```python
def fibonacci(max_terms=None):
    # Your code here
    pass
```

## Exercise 2: File Line Processor
Create a generator function that processes a large text file. The function should:
- Accept a file path and a search term
- Yield each line that contains the search term
- Process the file line by line (don't load the entire file into memory)
- Include the line number with each match

```python
def search_file(file_path, search_term):
    # Your code here
    pass
```

## Exercise 3: Batch Processor
Create a generator function that processes data in batches. The function should:
- Accept an iterable and a batch size
- Yield items in batches of the specified size
- Handle the last batch if it's smaller than the batch size

```python
def batch_generator(items, batch_size):
    # Your code here
    pass
```

## Exercise 4: Prime Number Generator
Create a generator function that yields prime numbers. The function should:
- Generate prime numbers starting from 2
- Include an optional parameter to limit the maximum prime number
- Use an efficient algorithm (e.g., Sieve of Eratosthenes)

```python
def prime_generator(max_prime=None):
    # Your code here
    pass
```

## Exercise 5: Data Transformer
Create a generator function that transforms data on the fly. The function should:
- Accept an iterable and a transformation function
- Apply the transformation to each item
- Yield the transformed items one at a time
- Handle any exceptions that might occur during transformation

```python
def transform_generator(items, transform_func):
    # Your code here
    pass
```

## Testing Your Solutions
For each exercise, test your generator with various inputs. Here are some test cases to consider:

### Exercise 1 Test Cases:
```python
# Test finite sequence
for num in fibonacci(5):
    print(num)  # Should print first 5 Fibonacci numbers

# Test infinite sequence (with break)
for num in fibonacci():
    if num > 100:
        break
    print(num)
```

### Exercise 2 Test Cases:
```python
# Create a test file
with open("test.txt", "w") as f:
    f.write("Line 1: Hello\nLine 2: World\nLine 3: Hello again")

# Test the generator
for line, number in search_file("test.txt", "Hello"):
    print(f"Found at line {number}: {line}")
```

### Exercise 3 Test Cases:
```python
items = range(10)
for batch in batch_generator(items, 3):
    print(batch)  # Should print [0,1,2], [3,4,5], [6,7,8], [9]
```

### Exercise 4 Test Cases:
```python
# Test first 10 primes
for prime in prime_generator(30):
    print(prime)

# Test infinite sequence (with break)
for prime in prime_generator():
    if prime > 100:
        break
    print(prime)
```

### Exercise 5 Test Cases:
```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
for transformed in transform_generator(numbers, square):
    print(transformed)  # Should print 1, 4, 9, 16, 25
```

## Tips
- Use `yield` to pause execution and return values
- Remember that generators maintain their state between calls
- Consider using `try/except` blocks for error handling
- Use `next()` to manually advance a generator
- Document your generator functions with docstrings

## Resources
- [Python Generator Documentation](https://docs.python.org/3/tutorial/classes.html#generators)
- [PEP 255 -- Simple Generators](https://www.python.org/dev/peps/pep-0255/)
- [Python Generators Tutorial](https://realpython.com/introduction-to-python-generators/)
