## What is an If Statement?

The **if statement** is used to run a block of code only if a specific condition is true. It helps make your code "decision-based," allowing it to act differently depending on the values you give it.

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

**Syntax:**

```python
if condition:
    # code to execute if condition is true
```

### Basic If Statement Example

```python
age = 18

if age >= 18:
    print("You are eligible to Drink.")
```

In this example:

- The condition `age >= 18` is checked. If it’s `True`, the message "You are eligible to drink." is printed.
- If the condition is `False`, the code inside the `if` statement will be skipped.

### Using `else`

The `else` part of an if statement allows you to specify code that runs when the condition is `False`.

**Example:**

```python
age = 16

if age >= 18:
    print("You are eligible to Drink.")
else:
    print("You are not eligible to Drink.")
```

In this example:

- If `age` is 18 or older, it prints "You are eligible to vote."
- Otherwise, it prints "You are not eligible to vote."

### Using `elif` (Else If)

The `elif` statement allows you to check multiple conditions in sequence. Python will evaluate each condition in order and run the first block of code with a `True` condition.

**Example:**

```python
grade = 85

if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
else:
    print("You need to improve.")
```

In this example:

- Python checks each condition in order. If `grade` is 85, it prints "You got a B." and skips the rest of the conditions.

### Python Nested if Statement
Example: Movie Theater Admission

Let’s say we want to write a program that checks if a person can watch a movie based on their **age** and if they have a **ticket**.

1. **If the person is 18 or older**, they are old enough to watch the movie.
2. **If the person has a ticket**, they can enter.
3. If they don’t have a ticket, they can’t enter, even if they’re old enough.
4. If they’re younger than 18, they can’t watch the movie.

**Code Example:**

```python
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 18:
    if has_ticket == "yes":
        print("You can watch the movie.")
    else:
        print("You need a ticket to watch the movie.")
else:
    print("You are too young to watch the movie.")

```

### Explanation:

1. **First Condition**: The program checks if the person’s age is 18 or older.
    - If **True**, it proceeds to the next condition (nested `if`).
    - If **False**, it prints "You are too young to watch the movie."
2. **Nested Condition**: If the person is old enough (age >= 18), the program then checks if they have a ticket.
    - If they have a ticket (`has_ticket == "yes"`), it prints "You can watch the movie."
    - If they don’t have a ticket, it prints "You need a ticket to watch the movie."

### Example Output

### Case 1: Age is 20, has a ticket

```bash
Enter your age: 20
Do you have a ticket? (yes/no): yes
Output: You can watch the movie.

```

### Case 2: Age is 20, no ticket

```vbnet
Enter your age: 20
Do you have a ticket? (yes/no): no
Output: You need a ticket to watch the movie.

```

### Case 3: Age is 15

```bash
Enter your age: 15
Do you have a ticket? (yes/no): yes
Output: You are too young to watch the movie.

```

### Key Points

- **Nested if** statements allow us to check conditions in layers.
- Use nested if statements when the second condition depends on the first one being `True`.
- This example first checks if the person is old enough and then checks if they have a ticket, providing specific responses based on the results.

This approach helps make code more readable and organized, especially when dealing with complex decisions.

---

## Python Logical Operators

### 1. **`and` Operator**

The `and` operator requires **both conditions to be `True`** for the whole expression to be `True`.

**Example: Checking Age and Membership**

```python
age = 20
is_member = True

if age >= 18 and is_member:
    print("You can access the VIP section.")
else:
    print("Access denied.")
```

- In this example, both `age >= 18` and `is_member` must be `True` for the message "You can access the VIP section." to print.
- If either condition is `False`, it will print "Access denied."

**Explanation of Output**:

- If `age` is 20 and `is_member` is `True`, output will be: `You can access the VIP section.`
- If `age` is 16 or `is_member` is `False`, output will be: `Access denied.`

---

### 2. **`or` Operator**

The `or` operator requires **at least one condition to be `True`** for the whole expression to be `True`.

**Example: Weekend Check**

```python
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("You can relax, it's a day off!")
else:
    print("It's a workday.")
```

- In this example, the message "You can relax, it's a day off!" will print if either `day` is `"Saturday"` or `"Sunday"`, or if `is_holiday` is `True`.
- If none of these conditions is `True`, it will print "It's a workday."

**Explanation of Output**:

- If `day` is `"Saturday"` and `is_holiday` is `False`, output will be: `You can relax, it's a day off!`
- If `day` is `"Monday"` and `is_holiday` is `False`, output will be: `It's a workday.`

---

### 3. **`not` Operator**

The `not` operator **reverses the result** of a condition. If the condition is `True`, `not` makes it `False`, and vice versa.

**Example: Checking if User is NOT Logged In**

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue.")
else:
    print("Welcome back!")
```

- Here, `not is_logged_in` will be `True` if `is_logged_in` is `False`.
- So, the message "Please log in to continue." will print if the user is not logged in.

**Explanation of Output**:

- If `is_logged_in` is `False`, output will be: `Please log in to continue.`
- If `is_logged_in` is `True`, output will be: `Welcome back!`

---

### Summary

- **if**: Checks a condition and executes code if it’s `True`.
- **else**: Executes code if the `if` condition is `False`.
- **elif**: Allows you to check multiple conditions in order.
- **and/or**: Combine multiple conditions.
- **Nested if**: Place an if statement inside another if statement for more specific conditions.

---

### Combining Logical Operators

You can combine `and`, `or`, and `not` in a single condition to check multiple criteria.

**Example: Access Control**

```python
age = 20
has_id = True
is_guest = False

if (age >= 18 and has_id) or is_guest:
    print("Access granted.")
else:
    print("Access denied.")
```

- This will grant access if either the person is 18 or older **and** has an ID, **or** if they are a guest.
- If none of these conditions is met, it will print "Access denied."

**Explanation of Output**:

- If `age` is 20, `has_id` is `True`, and `is_guest` is `False`, output will be: `Access granted.`
- If `age` is 16, `has_id` is `False`, and `is_guest` is `False`, output will be: `Access denied.`

---

### Exercises for Practice

1. **Check if a Number is Positive, Negative, or Zero**
    
    ```python
    number = int(input("Enter a number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
    ```
    
2. **Simple Grading System**
    
    ```python
    score = int(input("Enter your score: "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")
    ```

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
## Navigation

[⬅️ Previous: function with two arguments](functions.md) | [Next: **Loops in Python** ➡️](loops.md)
