# Data Types

### 1. **Introduction to Data Types**

- Definition: Data types define the type of data a variable can hold, such as numbers, text, etc.
- Importance: Understanding data types is fundamental to writing efficient and error-free code.

### 2. **Basic Data Types in Python**

- **Integer (`int`) מספר**
- **Float (`float`) מספר עשרוני**
- **String (`str`) מחרוזת**
- **Boolean (`bool`) בולאני**

https://www.programiz.com/python-programming/variables-datatypes

### 1. **Integer (`int`)**

- **Description**: Whole numbers, positive or negative, without a decimal point.

**Example**:

```python
age = 27
year = 2024
print("Age:", age)   # Output: Age: 25
print("Year:", year) # Output: Year: 2023
```

**Operations**:

```python
a = 10
b = 5
print(a + b)  # Addition: Output: 15
print(a - b)  # Subtraction: Output: 5
print(a * b)  # Multiplication: Output: 50
print(a / b)  # Division: Output: 2.0
print(a // b) # Floor Division: Output: 2
print(a % b)  # Modulus: Output: 0
```

### 2. **Float (`float`)**

- **Description**: Numbers with a decimal point.

**Example**:

```python
temperature = 36.6
pi = 3.14159
print("Temperature:", temperature) # Output: Temperature: 36.6
print("Pi:", pi)                   # Output: Pi: 3.14159
```

**Operations** (similar to integers, but with decimals):

```python
x = 5.5
y = 2.0
print(x + y)  # Output: 7.5
print(x - y)  # Output: 3.5
print(x * y)  # Output: 11.0
print(x / y)  # Output: 2.75
print(x // y) # Output: 2.0
print(x % y)  # Output: 1.5
```

### 3. **String (`str`)**

- **Description**: Sequence of characters, enclosed in single or double quotes.

**Example**:

```python
name = "Dor"
greeting = 'Hello'

print(name)
print(greeting)
print(greeting + ", " + name + "!")
```

**String Operations**:

```python
message = "Good Luck Devops Course !!!"
print(message.upper())
print(message.lower())
print(message.split())
print(len(message))
```

### 4. **Boolean (`bool`)**

- **Description**: Represents True or False.

**Example**:

```python
is_student = True
is_teacher = False
print(is_student) # Output: True
print(is_teacher) # Output: False
```

**Boolean Operations**:

```python
a = 10
b = 5
print(a > b)  # Output: True
print(a == b) # Output: False
print(a < b)  # Output: False
print(a != b) # Output: True
```

### **Exercise 1: Store and Print a String**

Create a variable to store your favorite fruit and print it.

**Example**:

```python
# Store favorite fruit
favorite_fruit = "apple"

# Print favorite fruit
print(favorite_fruit)
```

### **Exercise 2: Store and Print an Integer**

Create a variable to store your age and print it.

**Example**:

```python
# Store age
age = 25

# Print age
print(age)
```

### **Exercise 3: Store and Print a Float**

Create a variable to store a number with a decimal point (like the price of something) and print it.

**Example**:

```python
# Store price
price = 19.99

# Print price
print(price)
```

### **Exercise 4: Store and Print a Boolean**

Create a variable that indicates whether you like chocolate (True or False) and print it.

**Example**:

```python
# Store preference
likes_chocolate = True

# Print preference
print(likes_chocolate)
```

### **Exercise 5: Combine and Print Different Data Types**

Store a string, an integer, and a float in variables, then print them all together.

**Example**:

```python
# Store data
name = "Alice"
age = 30
height = 5.5

# Print the data
print(name)
print(age)
print(height)
```