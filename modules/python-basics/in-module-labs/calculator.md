# Calculator

### Objective

Build a simple and interactive command-line calculator that performs **basic arithmetic operations**: addition, subtraction, multiplication, and division.

---

## You Will

- How to use `input()` and `float()` for user input
- Conditional statements (`if`, `elif`, `else`)
- Defining and calling functions
- Error handling (`ZeroDivisionError`, `ValueError`)
- Creating clean, modular code

---

## 🛠️ Project Tasks

---

### Task 1: Show Operation Menu

Print options for the user to choose:

```
Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide

```

---

### Task 2: Get User Input

Ask the user to:

- Choose an operation (1-4)
- Enter two numbers

Use `input()` and `float()` to convert the numbers.

---

### Task 3: Perform Operation

Use conditional statements to perform the selected operation.

Example:

```python
if operation == '1':
    result = num1 + num2

```

---

### Task 4: Handle Division by Zero

If the user selects division and the second number is 0, show a friendly error message.

---

### Task 5: Use Functions

Define a function for each operation:

```python
def add(a, b):
    return a + b

```

---

### Task 6: Loop Until Exit

Wrap the whole program in a `while` loop. Ask the user if they want to perform another calculation.