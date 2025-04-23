# Python Fundamentals - Data Types & Syntax

## **1. What Are Data Types?**

- Every value in Python has a **type**.
- Data types tell Python how to **store**, **manipulate**, and **interpret** the value.
- Python is **dynamically typed**, meaning you don’t need to declare data types explicitly:
    
    ```python
    x = 5        # Python knows it's an int
    name = "Dor" # Python knows it's a str
    ```
    

🔗 Reference: [Programiz – Python Variables and Data Types](https://www.programiz.com/python-programming/variables-datatypes)

---

## **2. Core Data Types in Python**

| Type | Python Syntax | Example | Use Case |
| --- | --- | --- | --- |
| Integer | `int` | `x = 10` | Disk size, port numbers |
| Float | `float` | `temp = 36.6` | CPU load, time durations |
| String | `str` | `name = "Dor"` | Logs, file paths, configs |
| Boolean | `bool` | `is_valid = True` | Script success/failure |

---

## **3. Integer (`int`)**

- Whole numbers (positive or negative), no decimals.

```python
cores = 4
memory_gb = 16
print("Cores:", cores)
```

### 🧮 Integer Operations:

```python
a = 10
b = 3

print(a + b)  # ➕ Addition → 13
print(a - b)  # ➖ Subtraction → 7
print(a * b)  # ✖️ Multiplication → 30
print(a / b)  # ➗ Division → 3.33 (returns float)
print(a // b) # Floor Division → 3
print(a % b)  # Modulus (remainder) → 1
```

---

## **4. Float (`float`)**

- Numbers with a **decimal point**.

```python
cpu_load = 2.58
temperature = 36.6
```

### 🧮 Float Operations:

```python
x = 5.5
y = 2.0

print(x + y)  # 7.5
print(x / y)  # 2.75
print(x % y)  # 1.5

```

ℹ️ **Note**: Floats are commonly used in DevOps for **load averages, uptimes, network latency**, etc.

---

## 🧵 **5. String (`str`)**

- A sequence of characters. You can use single (`'`) or double (`"`) quotes.

```python
user = "devops_user"
welcome = f"Welcome {user}!"
print(welcome)
```

### 🔧 Common String Operations:

```python
message = "Good Luck DevOps Course !!!"

print(message.upper())   # GOOD LUCK DEVOPS COURSE !!!
print(message.lower())   # good luck devops course !!!
print(message.split())   # ['Good', 'Luck', 'DevOps', 'Course', '!!!']
print(len(message))      # Count characters
```

DevOps Tip: Strings are critical when dealing with **file paths, log entries, shell commands, and config files**.

---

## **6. Boolean (`bool`)**

- Only two values: `True` or `False`
- Used in **conditional logic**, **checks**, and **automations**.

```python
is_up = True
is_reachable = False

if is_up:
    print("Server is running.")
else:
    print("Server is down.")
```

### 🔁 Boolean Logic Operators:

| Operation | Symbol | Example | Result |
| --- | --- | --- | --- |
| AND | `and` | `True and False` | `False` |
| OR | `or` | `True or False` | `True` |
| NOT | `not` | `not True` | `False` |

🧪 Real-World Example:

```python
cpu_usage = 75
disk_usage = 95

if cpu_usage < 80 and disk_usage < 90:
    print("System is healthy")
else:
    print("Warning: High resource usage")
```

---

## 🧑‍💻 Bonus: `type()` and `isinstance()`

- You can check the type of any variable using:

```python
x = "hello"
print(type(x))           # <class 'str'>
print(isinstance(x, str))# True
```

---
## Navigation

[⬅️ Previous: Introduction to Python](intro-to-python.md) | [Next: Variable Declaration and Assignment in Python ➡️](variables.md)
