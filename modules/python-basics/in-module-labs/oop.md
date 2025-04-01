# Lab: Introduction to OOP

### Prerequisites:

- Python installed
- Basic understanding of variables and functions

---

## Objective:

By the end of this lab, you will:

- Create a class with attributes and methods
- Use the `__init__` method (constructor)
- Instantiate objects
- Access and modify attributes
- Work with object methods

---

## Task 1: Create the Class

### Goal:

Create a class called `Employee` with the following:

- Attributes: `name`, `position`, `salary`
- A method `describe()` that prints the employee’s details

---

## Task 2: Create an Object

### Goal:

Create an `Employee` object with:

- `name = "Alice"`
- `position = "Developer"`
- `salary = 80000`

Then call the `describe()` method to print the information.

---

## Task 3: Add a Method to Give a Raise

### Goal:

Add a method `give_raise(amount)` that increases the employee’s salary and prints the new salary.

Use it to give Alice a $5000 raise.

---

## Task 4: Modify the Position

### Goal:

Change the employee's position from `"Developer"` to `"Senior Developer"` and call `describe()` again.

---

## Bonus Task: Multiple Employees

### Goal:

Create a list of 3 `Employee` objects with different names, positions, and salaries.

Loop through the list and:

- Call `describe()` for each
- Give each one a $2000 raise using `give_raise()`