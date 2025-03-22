### **Lecture: Conditional Statements in Python**

---

### **What Are Conditional Statements?**

- **Definition**:
    
    Conditional statements are used in programming to execute specific blocks of code based on certain conditions.
    
    They enable **decision-making** in your programs.
    
- **Why Use Them?**
    - To make your program dynamic and responsive to user input or specific scenarios.
    - For example, you might want your script to execute different actions based on the user's age or the value of a variable.

---

### **Key Components of Conditional Statements**

### **1. `if` Statement**

- **Purpose**:
    
    Executes a block of code only if a specified condition evaluates to `True`.
    
- **Syntax**:
    
    ```python
    if condition:
        # Code to execute if condition is True
    
    ```
    
- **Example**:
    
    ```python
    age = 20
    if age >= 18:
        print("You are an adult!")
    
    ```
    

---

### **2. `if-else` Statement**

- **Purpose**:
    
    Provides an alternative block of code if the condition is `False`.
    
- **Syntax**:
    
    ```python
    if condition:
        # Code if condition is True
    else:
        # Code if condition is False
    
    ```
    
- **Example**:
    
    ```python
    age = 15
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are not an adult.")
    
    ```
    

---

### **3. `if-elif-else` Statement**

- **Purpose**:
    
    Adds multiple conditions to check in sequence. The first condition that evaluates to `True` executes, and the rest are skipped.
    
- **Syntax**:
    
    ```python
    if condition1:
        # Code for condition1
    elif condition2:
        # Code for condition2
    else:
        # Code if all conditions are False
    
    ```
    
- **Example**:
    
    ```python
    age = 70
    if age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
    
    ```
    

---

### **Comparison Operators**

Used to compare two values. They return `True` or `False`.

| **Operator** | **Description** | **Example** |
| --- | --- | --- |
| `==` | Equal to | `5 == 5` → `True` |
| `!=` | Not equal to | `5 != 3` → `True` |
| `>` | Greater than | `5 > 3` → `True` |
| `<` | Less than | `5 < 3` → `False` |
| `>=` | Greater than or equal | `5 >= 5` → `True` |
| `<=` | Less than or equal | `5 <= 4` → `False` |

---

### **Logical Operators**

Used to combine conditional statements.

| **Operator** | **Description** | **Example** |
| --- | --- | --- |
| `and` | Returns `True` if both conditions are `True`. | `(5 > 3) and (4 < 6)` → `True` |
| `or` | Returns `True` if at least one condition is `True`. | `(5 > 3) or (4 > 6)` → `True` |
| `not` | Reverses the result of the condition. | `not(5 > 3)` → `False` |

---

### **Combining Conditions**

- **Example 1**: Using `and`
    
    ```python
    age = 25
    income = 50000
    if age > 18 and income > 30000:
        print("You are eligible for the loan.")
    
    ```
    
- **Example 2**: Using `or`
    
    ```python
    age = 16
    if age < 18 or age > 65:
        print("You are not eligible for a driving license.")
    
    ```
    
- **Example 3**: Using `not`
    
    ```python
    logged_in = False
    if not logged_in:
        print("Please log in to continue.")
    
    ```
    

---

### **Practical Examples**

### **1. User Input and Decision Making**

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

```

### **2. Nested `if` Statements**

- **Definition**: An `if` statement inside another `if` statement.
- **Example**:
    
    ```python
    age = 25
    country = "USA"
    
    if age >= 18:
        if country == "USA":
            print("You can vote in the USA.")
        else:
            print("You may not be eligible to vote in the USA.")
    else:
        print("You are not old enough to vote.")
    
    ```
    

### **3. Multiple Conditions**

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

```

---

### **Common Mistakes to Avoid**

1. **Misusing Indentation**:
    - Python requires proper indentation for blocks of code.
    - Example:
        
        ```python
        if True:
        print("This will cause an error!")  # IndentationError
        
        ```
        
2. **Using `=` Instead of `==`**:
    - `=` is for assignment, while `==` is for comparison.
    - Incorrect:
        
        ```python
        if x = 5:  # SyntaxError
            print("x is 5")
        
        ```
        
    - Correct:
        
        ```python
        if x == 5:
            print("x is 5")
        
        ```
        
3. **Overusing Nested `if` Statements**:
    - Too many nested conditions can make your code hard to read.
    - Use logical operators to simplify:
        
        ```python
        if age >= 18 and country == "USA":
            print("You can vote.")
        
        ```
        

---

### **Best Practices**

1. **Use Comments**:
    - Explain complex conditions with comments.
2. **Simplify Conditions**:
    - Combine conditions with logical operators instead of nesting.
3. **Test Edge Cases**:
    - Ensure your program behaves correctly for boundary values.
4. **Follow PEP 8 Guidelines**:
    - Keep your code clean and well-structured.

---

### **Hands-On Practice**

1. Write a program that asks the user for their age and outputs:
    - "Child" if age is less than 13.
    - "Teenager" if age is between 13 and 19.
    - "Adult" if age is 20 or above.
2. Create a script that:
    - Asks the user for their exam score.
    - Prints "Pass" if the score is 50 or above and "Fail" otherwise.
3. Write a program to check if a number is:
    - Positive and even.
    - Negative.
    - Zero.

---

### **Real-World Application**

### **Scenario**: E-Commerce Discount System

- **Problem**: Calculate discounts based on customer membership type and total cart value.
- **Example Code**:
    
    ```python
    membership = "Gold"
    cart_value = 150
    
    if membership == "Gold" and cart_value > 100:
        print("You get a 20% discount!")
    elif membership == "Silver" and cart_value > 100:
        print("You get a 10% discount!")
    else:
        print("No discount available.")
    
    ```
    

---

### **Key Takeaways**

1. Conditional statements allow your program to make decisions.
2. Use `if`, `elif`, and `else` to handle multiple scenarios.
3. Logical and comparison operators make your conditions more flexible.
4. Avoid nesting too deeply; use logical operators instead.