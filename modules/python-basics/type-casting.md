# **Python Type Casting**

### **Python Type Casting**

---

### **What is Type Casting?**

Type casting in Python refers to converting one data type into another. It is used to ensure data compatibility and manipulate data effectively in your scripts.

---

### **Types of Type Casting in Python**

### **1. Explicit Type Casting**

This is when you manually convert a value from one type to another using Python's built-in functions.

### **2. Implicit Type Casting**

This is when Python automatically converts one type to another during an operation without explicit instructions.

---

### **Common Type Casting Functions**

| Function | Description | Example |
| --- | --- | --- |
| `int()` | Converts to an integer | `int("5")` → `5` |
| `float()` | Converts to a floating-point number | `float("5.5")` → `5.5` |
| `str()` | Converts to a string | `str(5)` → `"5"` |
| `list()` | Converts to a list | `list((1, 2, 3))` → `[1, 2, 3]` |
| `tuple()` | Converts to a tuple | `tuple([1, 2, 3])` → `(1, 2, 3)` |
| `set()` | Converts to a set | `set([1, 2, 2, 3])` → `{1, 2, 3}` |
| `bool()` | Converts to a Boolean (`True` or `False`) | `bool(0)` → `False` |

---

### **Examples of Type Casting**

### **1. Converting Strings to Integers and Floats**

```python
python
Copy code
# String to Integer
num = int("123")
print(num)  # Output: 123

# String to Float
num_float = float("123.45")
print(num_float)  # Output: 123.45

```

### **2. Converting Numbers to Strings**

```python
python
Copy code
# Integer to String
num_str = str(123)
print(num_str)  # Output: "123"

# Float to String
num_str_float = str(123.45)
print(num_str_float)  # Output: "123.45"

```

### **3. Converting Between Collections**

```python
python
Copy code
# Tuple to List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# List to Set (removes duplicates)
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3}

```

### **4. Converting to Boolean**

```python
python
Copy code
# Integer to Boolean
print(bool(0))    # Output: False
print(bool(10))   # Output: True

# String to Boolean
print(bool(""))   # Output: False
print(bool("Hi")) # Output: True

```

### **5. Implicit Type Casting**

```python
python
Copy code
# Python automatically converts int to float
num = 10
result = num + 3.5
print(result)  # Output: 13.5
print(type(result))  # Output: <class 'float'>

```

---

### **Use Cases for Type Casting**

1. **Combining Different Data Types:**
    - Example: Concatenating strings with integers.
        
        ```python
        age = 25
        message = "I am " + str(age) + " years old."
        print(message)
        
        ```
        
2. **Validating User Input:**
    - Convert string input from `input()` into numeric types for calculations.
        
        ```python
        user_input = input("Enter a number: ")
        number = int(user_input)
        print("Double the number:", number * 2)
        
        ```
        
3. **Handling API Data:**
    - Convert data returned from an API (often as strings) into appropriate types for processing.
4. **Removing Duplicates:**
    - Use `set()` to remove duplicates from a list.

---

### **Common Errors in Type Casting**

1. **Invalid Conversions:**
    - Trying to convert a non-numeric string to an integer:
        
        ```python
        int("abc")  # Raises ValueError
        
        ```
        
2. **Loss of Precision:**
    - Converting from float to int:
        
        ```python
        num = int(12.9)
        print(num)  # Output: 12 (decimal part is discarded)
        
        ```
        

---

### **Hands-On Exercises**

### **Exercise 1: String to Number**

1. Ask the user to enter two numbers as strings.
2. Convert them to integers and calculate their sum.

### **Exercise 2: Removing Duplicates**

1. Create a list with duplicate values.
2. Convert it into a set to remove duplicates.

### **Exercise 3: Data Conversion**

1. Take a tuple of strings (e.g., `("1", "2", "3")`) and convert it into a list of integers.

---

### **Best Practices**

1. Always validate inputs before converting types to avoid errors.
2. Use explicit type casting when the data type conversion isn't obvious.
3. Be cautious about precision loss when converting between numeric types.