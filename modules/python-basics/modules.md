# if **name** == "**main**"

In Python, the construct `if __name__ == "__main__":` is a common idiom used to make code both importable as a module and executable as a script.

Here's how it works:

1. **`__name__` variable**: Every Python module has a special built-in variable called `__name__`. When a module is run directly (for example, using `python myscript.py`), the `__name__` variable is set to `"__main__"`. If the module is imported into another module, `__name__` is set to the module's name.
2. **`if __name__ == "__main__":` block**: This line checks whether the script is being run directly (i.e., `__name__ == "__main__"`) or being imported as a module into another script. If it is run directly, the code inside this `if` block will be executed. If the script is imported, the code inside this block will not run.

### **Why Use `if __name__ == "__main__"`?**

- It lets you write code that can either:
    - **Run directly as a script**, or
    - **Be imported as a module** without running the main code.

### Example:

```python
# myscript.py

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

- **When run directly:** If you run `myscript.py` directly from the command line, the output will be `Hello, World!`.
    
    ```
    $ python myscript.py
    Hello, World!
    ```
    
- **When imported as a module:** If you import `myscript.py` into another script, the `main()` function won't run automatically. This allows you to reuse the functions defined in `myscript.py` without executing the script's main functionality.
    
    ```python
    # another_script.py
    
    import myscript
    
    # main() from myscript won't be executed automatically
    ```
    

### Why Use It?

- **Running as a Script:** If you run the file directly (like `python myfile.py`), the code inside this block will execute. This is useful for testing or running the script on its own.
- **Importing as a Module:** If you import the file into another script, the code inside this block **will not run**. This allows you to use functions or classes from the file without accidentally running the script's main code.

### Simple Example:

- **Direct Run:**
    
    ```python
    # myfile.py
    print("This always runs")
    
    if __name__ == "__main__":
        print("This runs only when the file is run directly")
    ```
    
    Output when running `python myfile.py`:
    
    ```csharp
    This always runs
    This runs only when the file is run directly
    ```
    
- **When Imported:**
    
    ```python
    # another_file.py
    import myfile
    ```
    
    Output:
    
    ```scss
    This always runs
    ```
    
    (Notice that "This runs only when the file is run directly" doesn't print because the file was imported, not run directly.)


### **What is a Module?**

A **module** in Python is a file that contains Python code — functions, variables, or classes — that can be reused in other Python programs. By creating your own module, you can:

- **Organize code**: Keep related functions and data together.
- **Promote reusability**: Write the code once and use it in multiple programs.
- **Simplify debugging**: Work on smaller chunks of code independently.

### **Import modules**

You can load a module with the **import** keyword.

In the example below we load the *os module*. This is short for operating system, so you can do system tasks.

```
import os
os.system("dir")
os.system("ls")
os.system("ls -l")
```

---

Using that module we call one of its functions named system (runs a command).

In this case it will simply list the files in the directory (dir command).

There are many many modules available for Python.

### **Get specific functions from a module**

To import a specific function in a module, you can use the line:

```
from moduleimport function
```

---

There's a module named *time* which has all kind of functionality for time: get the date, hour, minute, second and so on. That's quite a lot of functionality.

Lets say you want the program to wait 2 seconds. If you want, you can import a specific function instead of the whole module.

```
from time import sleep
sleep(2)
print("Hello, world!")  
```

---

### **Import all functions from a module.**

You can import all functions from a module, but this is not recommended.

The example below imports the whole time module (all functions), which you can then use.

```
from time
time.sleep(2)
print("Hello, world!")
```

---

### **List functions in module**

To see all functions in a module, start the Python interpreter and type

```
# List functions in module  
import os
print(dir(os))
```

---

### **Create a Python Module**

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

### **Create a Python Script to Import the Module**

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

### **Run the Script**

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

### **Using `from` to Import Specific Items**

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

### **Store Modules in a Folder**

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

**Example: Checking Module Search Paths**

```python
import sys
print(sys.path)

```

Think of it as a **toolbox** with reusable tools (functions and classes).

### Types of Modules:

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

### Create a file called `myutils.py`

```python
# myutils.py
def greet(name):
    return f"Hello, {name}!"

def square(x):
    return x * x
```

### Use it in another file

```python
# main.py
import myutils

print(myutils.greet("Noa"))
print(myutils.square(4))  # 16

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
## References

- [Python Official Docs – Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Built-in Modules List](https://docs.python.org/3/py-modindex.html)
- [pip documentation](https://pip.pypa.io/en/stable/)

---
## Navigation

[⬅️ Previous: Working with JSON Files in Python](json.md) | [Next: What is an API ? ➡️](api.md)
