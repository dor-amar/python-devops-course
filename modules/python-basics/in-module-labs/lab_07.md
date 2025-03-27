# Lab: Exception Handling in Python

## Exception Handling in Python

### Objectives

By the end of this lab, You will:

- Understand what exceptions are and why they occur.
- Learn how to use `try`, `except`, `else`, and `finally`.
- Create custom exception classes.
- Handle multiple exceptions.
- Practice debugging and protecting code from crashing.

---

## Introduction

**What is an Exception?**

An exception is an error that occurs during the execution of a program. If not handled, it will stop the program.

Examples:

```python
print(10 / 0)  # ZeroDivisionError
int("abc")     # ValueError
```

Python provides a way to handle these errors using `try-except` blocks so the program can continue to run.

---

## 🛠️ Tasks

---

### 🔹 Task 1: Basic Try-Except

**Step 1.1**: Create a program that asks the user to enter a number and divides 100 by that number.

Expected issues:

- Division by 0
- Invalid input (e.g., strings)

**Your Code:**

```python
# TODO: Wrap this in try-except
number = int(input("Enter a number to divide 100: "))
result = 100 / number
print(f"Result: {result}")
```

---

### Task 2: Handling Multiple Exceptions

**Step 2.1**: Expand your code to catch both `ValueError` and `ZeroDivisionError` and print appropriate messages.

```python
# Expected Output:
# ValueError -> "Please enter a valid number."
# ZeroDivisionError -> "You can't divide by zero!"
```

---

### Task 3: Using `else` and `finally`

**Step 3.1**: Add `else` and `finally` blocks to your code.

- `else`: runs only if no exception occurs.
- `finally`: runs no matter what.

---

### Task 4: Custom Exception

**Step 4.1**: Write a function that raises a custom exception if a username is shorter than 3 characters.

```python
class UsernameTooShort(Exception):
    pass

def register(username):
    # Raise UsernameTooShort if username is too short
    pass
```

---

### Task 5: Raising Exceptions

**Step 5.1**: Create a function that checks age. If age is under 18, raise a `ValueError` with the message `"You must be at least 18."`

```python
def check_age(age):
    # raise ValueError if age < 18
    pass
```

Use a `try-except` block to catch it when calling the function.

---

## ✅ Summary

You learned:

- How to prevent your Python program from crashing.
- `try`, `except`, `else`, `finally`
- Raising and creating exceptions
- Writing defensive and user-friendly code