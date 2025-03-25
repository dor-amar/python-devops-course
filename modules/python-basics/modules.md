### **What is a Module?**

A **module** in Python is a file that contains Python code — functions, variables, or classes — that can be reused in other Python programs. By creating your own module, you can:

- **Organize code**: Keep related functions and data together.
- **Promote reusability**: Write the code once and use it in multiple programs.
- **Simplify debugging**: Work on smaller chunks of code independently.

### **Step 1: Create a Python Module**

A module is simply a Python file containing functions, variables, or classes. Save the file with a `.py` extension.

**Example: `mymodule.py`**

```python
# mymodule.py

def greet(name):
    """Function to greet someone."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

PI = 3.14159

```

---

### **Step 2: Create a Python Script to Import the Module**

Now, create another Python file to import and use the module.

**Example: `main.py`**

```python
# main.py

# Import the custom module
import mymodule

# Use the functions and variables from the module
print(mymodule.greet("Dor"))
print("Sum:", mymodule.add_numbers(5, 7))
print("Value of PI:", mymodule.PI)

```

---

### **Step 3: Run the Script**

1. Save both files (`mymodule.py` and `main.py`) in the same directory.
2. Run `main.py` using the Python interpreter:
    
    ```bash
    python main.py
    ```
    

**Output:**

```yaml
Hello, Dor!
Sum: 12
Value of PI: 3.14159
```

---

### **Step 4: Using `from` to Import Specific Items**

You can import specific functions or variables directly from the module.

**Example: `main.py`**

```python
# Import specific functions and variables
from mymodule import greet, add_numbers, PI

# Use the imported items
print(greet("Jessica"))
print("Sum:", add_numbers(10, 20))
print("Value of PI:", PI)

```

---

### **Step 5: Store Modules in a Folder**

You can organize modules in a folder and treat it as a package.

**Folder Structure:**

```css
my_package/
    __init__.py
    mymodule.py
main.py

```

**Example: `main.py`**

```python
# Import the module from the package
from my_package import mymodule

print(mymodule.greet("Class"))
print("Sum:", mymodule.add_numbers(8, 4))

```

---

### **Bonus: Tips for Your Class**

1. **Explain the Purpose of Modules**: To reuse code and keep the project organized.
2. **Practice Hands-On**: Ask students to create their own modules, e.g., a `math_tools.py` with custom math functions.
3. **Explain Module Search Path**: Python looks for modules in the current directory and paths defined in `sys.path`.

**Example: Checking Module Search Paths**

```python
import sys
print(sys.path)

```

## Modules

## What is a Module?

A **module** is a file that contains Python code — functions, variables, or classes — that you can **reuse** in other Python programs.

🧠 Think of it as a **toolbox** with reusable tools (functions and classes).

### 📦 Types of Modules:

- **Built-in modules** – Come with Python (e.g., `math`, `random`, `os`)
- **External modules** – Installed via `pip` (e.g., `requests`, `pandas`)
- **User-defined modules** – Code you write in separate `.py` files

---

## Importing Modules

### ✅ Basic `import`

```python
import math
print(math.sqrt(16))  # 4.0
```

### ✅ `from ... import`

```python
from math import sqrt
print(sqrt(25))  # 5.0
```

### ✅ Using `as` (aliasing)

```python
import math as m
print(m.pi)  # 3.141592653...
```

---

## Creating Your Own Module

### Step 1: Create a file called `myutils.py`

```python
# myutils.py
def greet(name):
    return f"Hello, {name}!"

def square(x):
    return x * x
```

### Step 2: Use it in another file

```python
# main.py
import myutils

print(myutils.greet("Noa"))
print(myutils.square(4))  # 16

```

---

## 🔍 4. The `__name__ == "__main__"` Trick

Use this to write code that only runs when the module is executed directly, not when imported:

```python
# myutils.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Test"))  # Only runs if you run myutils.py directly
```

---

## External Modules

Install external modules with `pip`:

```bash
pip install requests
```

Then use it in Python:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

---

## Useful Built-in Modules

| Module | Use Case |
| --- | --- |
| `math` | Mathematical operations |
| `random` | Random numbers and choices |
| `os` | Interact with the operating system |
| `datetime` | Work with dates and times |
| `sys` | System-level operations |
| `json` | Handle JSON data |

---

## Examples & Practice

### Example 1: `random.choice()`

```python
import random

options = ['rock', 'paper', 'scissors']
print(random.choice(options))
```

### Example 2: Use `os` to get the current directory

```python
import os
print(os.getcwd())
```

---

## Summary

✅ Modules help organize and reuse code

✅ Use `import` to access functions from other files

✅ You can use built-in, external, or custom modules

✅ Use `__name__ == "__main__"` to control execution logic

---

## 📝 Homework / Practice

1. Create a module called `math_utils.py` with functions:
    - `add(a, b)`
    - `multiply(a, b)`
2. Import and use it in another script.
3. Install an external module (`pyfiglet`) and print styled text.

---

## References

- [Python Official Docs – Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Built-in Modules List](https://docs.python.org/3/py-modindex.html)
- [pip documentation](https://pip.pypa.io/en/stable/)