### What is a Function?

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we can put it into a function and call that function whenever we need it.

**Example:**
Think of a function like a coffee machine. Every time you press the button, the machine makes coffee. Similarly, every time you call a function, it runs the code inside it and returns a result.

### Why Use Functions?

1. **Reusability**: Write the code once, use it multiple times.
2. **Organization**: Break down large problems into smaller, manageable parts.
3. **Avoiding Repetition**: Reduces duplicate code, making it easier to maintain.
4. **Easier to Debug**: Errors are easier to locate and fix when code is divided into functions.

---

### Defining a Function

To define a function in Python, use the `def` keyword, followed by the function name, parentheses, and a colon. Any code inside the function is indented.

**Syntax:**

```python
def function_name():
    # code to execute
    return
```

**Example:**

```python
def greet():
    print("Hello, welcome to the class!")
```

To **call** the function, simply write the function's name followed by parentheses.

```python
greet()  # Output: Hello, welcome to the class!
```

![image.png](../../images/image%20(1).png)

---

### Functions with Parameters

Functions can accept **parameters** (or inputs) to work with specific data.

**Example:**

```python
# function with two arguments 
def add_numbers(num1, num2): 
  sum = num1 + num2 
  print('Sum: ', sum) 

# function call with two values 
add_numbers(5, 4)
```

In this example, `name` is a parameter. When we call `greet("Alice")`, `"Alice"` is passed as the value of `name`.

![image.png](../../images/image%20(2).png)

---

### Return Values

Functions can return a result using the `return` keyword. This allows the function to produce a result that can be used later.

**Example:**

```python
 # function definition 
def find_square(num): 
  result = num * num 
  return result 
# function call 
square = find_square(3) 
print('Square:',square) 
# Output: Square: 9
```

In this example, the function `add` returns the sum of `a` and `b`. We store this result in the variable `result`.

![image.png](../../images/image%20(3).png)

---

### Example: Add Two Numbers

```python
# function that adds two numbers 
def add_numbers(num1, num2): 
  sum = num1 + num2 
  return sum 
# calling function with two values 
result = add_numbers(5, 4) 
print('Sum: ', result) 
# Output: Sum: 9
```

### Exercises for Practice

1. **Create a Function to Calculate Area of a Rectangle**
    
    ```python
    def area_rectangle(length, width):
        return length * width
    ```
    
2. **Create a Function to Check if a Number is Even or Odd**
    
    ```python
    def is_even(number):
        return number % 2 == 0
    ```
    
3. **Create a Function to Convert Celsius to Fahrenheit**
    
    ```python
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    ```
    

---

### Benefit of using Functions

1. Code Reusable - We can use the same function multiple times in our program which
makes our code reusable. For example,

```python
# function definition 
def get_square(num): 
  return num * num 
for i in [1,2,3]: 
# function call 
  result = get_square(i) 
  print('Square of',i, '=',result)
```