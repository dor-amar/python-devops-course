# Lambda Functions

### **Introduction to Lambda Functions**

- **Explanation**:
    - Introduce the concept of anonymous functions and explain that lambda functions are small, unnamed functions defined using the `lambda` keyword.
    - Mention that lambda functions are often used for short, simple operations where defining a full function might be overkill.

### What is a Lambda Function in Python?

A **lambda function** in Python is a way to write a small, quick function in just one line of code. It’s like a “mini function” that you can create without giving it a name.

### What is an Anonymous Function?

An **anonymous function** is a function without a name. Instead of using the `def` keyword to define a regular function and give it a name, an anonymous function is created on the spot, usually for a short-term task.

In Python, anonymous functions are created using the **`lambda` keyword**, which is why they’re also called **lambda functions**.

### Why Use Lambda Functions?

- They are great for small, simple tasks.
- You don’t need to write a full `def` function if you only need it once.
- Perfect for short functions where naming the function isn't necessary.
- **Syntax**:
    
    ```python
    lambda arguments: expression
    ```
    

### **Limitations of Lambda Functions**

- **Single Expression Only**:
    - Lambda functions can only contain one expression. They cannot have multiple statements or complex logic like loops or conditionals.
- **Reduced Readability**:
    - Overusing lambda functions can make the code harder to read, especially for more complex operations.
- **No Documentation or Annotations**:
    - Lambda functions don’t support docstrings, which means you cannot add documentation directly to them. Also, they don’t support type annotations.

### **Best Practices**

- **Use for Simple Operations**:
    - Lambda functions should be used for short, simple operations. If the logic is complex, it’s better to use a regular function for clarity and readability.
- **Avoid Overusing**:
    - While lambda functions are powerful, overusing them can lead to code that is difficult to understand. Use them judiciously.
- **Use in Functional Programming**:
    - Lambda functions are particularly useful in functional programming paradigms, where functions are passed as arguments to other functions.

### **2. Basic Examples of Lambda Functions**

- **Example 1: Simple Addition**
    
    ```python
    add = lambda x, y: x + y
    print(add(2, 3))  # Output: 5
    
    ```
    
- **Example 2: Square of a Number**
    
    ```python
    square = lambda x: x * 2
    print(square(4))  # Output: 8
    
    ```
    

### **3. Using Lambda Functions with String Manipulation**

- **Example 3: Convert a String to Uppercase**
    
    ```python
    to_upper = lambda s: s.upper()
    print(to_upper("hello"))  # Output: "HELLO"
    
    ```
    
- **Example 4: Check if a String Starts with a Specific Letter**
    
    ```python
    starts_with_h = lambda s: s.startswith('H')
    print(starts_with_h("Hello"))  # Output: True
    print(starts_with_h("hello"))  # Output: False
    
    ```
    

### **4. Using Lambda Functions with `map()` and `filter()`**

- **Example 5: Using `map()` with Lambda to Apply a Function to Each Element**
    
    ```python
    words = ["apple", "banana", "cherry"]
    uppercase_words = list(map(lambda s: s.upper(), words))
    print(uppercase_words)  # Output: ['APPLE', 'BANANA', 'CHERRY']
    
    ```
    
- **Example 6: Using `filter()` with Lambda to Filter a List**
    
    ```python
    words = ["apple", "banana", "cherry", "avocado"]
    words_starting_with_a = list(filter(lambda s: s.startswith('a'), words))
    print(words_starting_with_a)  # Output: ['apple', 'avocado']
    
    ```
    

### **5. Practical Exercises**

- **Exercise 1**: Write a lambda function to check if a string is a palindrome (same forwards and backwards).
    
    ```python
    is_palindrome = lambda s: s == s[::-1]
    print(is_palindrome("radar"))  # Output: True
    print(is_palindrome("python"))  # Output: False
    
    ```
    
- **Exercise 2**: Use `map()` with a lambda function to add the prefix "Dr." to each name in a list.
    
    ```python
    names = ["Alice", "Bob", "Charlie"]
    doctors = list(map(lambda name: "Dr. " + name, names))
    print(doctors)  # Output: ['Dr. Alice', 'Dr. Bob', 'Dr. Charlie']
    
    ```
    
- **Exercise 3**: Use `filter()` with a lambda function to filter out all strings from a list that have fewer than 5 characters.
    
    ```python
    words = ["apple", "bat", "banana", "dog", "elephant"]
    long_words = list(filter(lambda s: len(s) >= 5, words))
    print(long_words)  # Output: ['apple', 'banana', 'elephant']
    
    ```