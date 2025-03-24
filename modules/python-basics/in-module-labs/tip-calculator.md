# Tip Calculator

### Objective

Build a **command-line Tip Calculator** that asks the user for:

- Total bill amount
- Tip percentage
- Number of people

Then it calculates:

- Total tip
- Total bill including tip
- Amount each person needs to pay

---

**You Will**

- Taking input using `input()`
- Type conversion (`float`, `int`)
- Basic math operations
- Rounding numbers
- Using formatted strings (`f""`)
- Defensive coding with exception handling

---

## 🛠️ Project Tasks

---

### Task 1: Get User Inputs

Ask the user:

- What was the total bill?
- What percentage tip would you like to give? (e.g., 10, 15, 20)
- How many people are splitting the bill?

```python
# Example inputs
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? ")
people = input("How many people to split the bill? ")
```

---

### Task 2: Convert and Calculate

- Convert inputs to numbers using `float()` or `int()`
- Calculate tip amount
- Calculate total amount
- Divide total by number of people
- Round to 2 decimal places

---

### Task 3: Output the Result

Use `print()` and `f""` to display the result clearly.

Example:

```
Each person should pay: $15.35
```

---

### Task 4: Handle Bad Input

If the user types something that isn’t a number (like "ten" instead of 10), catch the error and ask again.