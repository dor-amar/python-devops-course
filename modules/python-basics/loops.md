# **Loops in Python**

### **Lecture: Loops in Python**

---

### **What Are Loops?**

- **Definition**:
    
    Loops allow you to execute a block of code multiple times, making your programs more efficient for repetitive tasks.
    
- **Why Use Loops?**
    - To automate repetitive tasks like iterating through a list of items or repeatedly checking for a condition.
    - Example: Printing numbers from 1 to 100 without writing 100 lines of code.

---

### **Types of Loops in Python**

### **1. `for` Loops**

- **Purpose**:
    
    Iterate over a sequence (e.g., list, tuple, string) or a range of numbers.
    
- **Syntax**:
    
    ```python
    for item in sequence:
        # Code block to execute
    
    ```
    
- **Example: Iterating Through a List**:
    
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    
    ```
    
- **Example: Using `range()`**:
    
    ```python
    for i in range(5):  # i will take values 0, 1, 2, 3, 4
        print(i)
    
    ```
    
- **`range()` Explained**:
    - `range(start, stop, step)` generates numbers from `start` to `stop-1` with an optional step size.
    - Examples:
        
        ```python
        range(5)        # 0, 1, 2, 3, 4
        range(1, 6)     # 1, 2, 3, 4, 5
        range(1, 10, 2) # 1, 3, 5, 7, 9
        
        ```
        

---

### **2. `while` Loops**

- **Purpose**:
    
    Repeats a block of code as long as a condition is `True`.
    
- **Syntax**:
    
    ```python
    while condition:
        # Code block to execute
    
    ```
    
- **Example: Counting Down**:
    
    ```python
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
    
    ```
    
- **Important Note**:
    
    Always ensure the condition becomes `False` at some point to avoid infinite loops.
    

---

### **3. Loop Control Statements**

These statements alter the flow of a loop.

### **`break`**

- **Purpose**:
    
    Exits the loop prematurely.
    
- **Example**:
    
    ```python
    for i in range(10):
        if i == 5:
            break  # Exit the loop when i equals 5
        print(i)
    
    ```
    

### **`continue`**

- **Purpose**:
    
    Skips the rest of the code in the current iteration and moves to the next iteration.
    
- **Example**:
    
    ```python
    for i in range(10):
        if i % 2 == 0:
            continue  # Skip even numbers
        print(i)
    
    ```
    

### **`else` with Loops**

- **Purpose**:
    
    Executes a block of code after the loop completes **normally** (i.e., without encountering a `break`).
    
- **Example**:
    
    ```python
    for i in range(5):
        print(i)
    else:
        print("Loop completed successfully!")
    
    ```
    
    - If the loop is terminated by a `break`, the `else` block is **not** executed.

---

### **Examples**

### **1. Using `for` Loop with a List**

```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")

```

### **2. Summing Numbers with a `for` Loop**

```python
total = 0
for num in range(1, 11):  # Sum numbers 1 to 10
    total += num
print(f"Total: {total}")

```

### **3. Factorial Calculation with a `while` Loop**

```python
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"Factorial: {factorial}")

```

### **4. Finding Prime Numbers**

```python
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(f"{num} is a prime number")

```

---

### **Common Mistakes**

1. **Infinite Loops**:
    - Forgetting to update the loop condition can result in an infinite loop.
    - Example:
        
        ```python
        i = 0
        while i < 5:
            print(i)  # This will run forever because i is never incremented
        
        ```
        
2. **Misusing `break` and `continue`**:
    - Misplacing these statements can lead to unexpected behavior.
3. **Not Using `range()` Correctly**:
    - Forgetting the `step` parameter for specific patterns.
    - Example:
        
        ```python
        for i in range(1, 10):  # Prints 1 to 9, not including 10
            print(i)
        
        ```
        

---

### **Best Practices**

1. **Use Descriptive Variable Names**:
    - Instead of `i`, use meaningful names like `index` or `item`.
2. **Avoid Nested Loops If Possible**:
    - Nested loops can slow down your program. Use better logic or algorithms if feasible.
3. **Test Loop Conditions**:
    - Ensure the loop condition will eventually become `False`.
4. **Use `break` and `continue` Sparingly**:
    - Overusing them can make your code harder to read.

---

### **Real-World Applications of Loops**

1. **Processing Data**:
    - Iterating through files, rows in a database, or API responses.
2. **Automating Tasks**:
    - Automatically generating reports or emails.
3. **Simulations**:
    - Running simulations or repetitive calculations.

---

### **Practice Tasks**

### **Task 1: Print Multiplication Table**

Write a script to print the multiplication table of a given number (e.g., `5`).

### **Task 2: Reverse a String**

Ask the user for a string and print its reverse using a loop.

### **Task 3: Sum of Digits**

Write a script to calculate the sum of digits in an integer (e.g., `123` → `1+2+3=6`).

### **Task 4: Find the Maximum in a List**

Write a script to find the largest number in a list using a loop.

### **Task 5: Generate Fibonacci Series**

Print the Fibonacci series up to a given number (e.g., `10`).

---

### **Key Takeaways**

- Loops are essential for repetitive tasks.
- Use `for` loops for sequences and `while` loops for condition-based iterations.
- Loop control statements (`break`, `continue`, `else`) give you fine-grained control over the loop flow.
- Always test your loops to avoid infinite iterations.