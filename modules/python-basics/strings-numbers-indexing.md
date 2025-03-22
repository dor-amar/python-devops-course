### **1. Introduction to Strings and Numbers**

- **Strings**: A sequence of characters enclosed in quotes.
    - Single quotes: `'Hello'`
    - Double quotes: `"World"`
- **Numbers**:
    - **Integers (`int`)**: Whole numbers, e.g., `10`, `3`.
    - **Floats (`float`)**: Numbers with a decimal point, e.g., `3.14`, `2.0`.

### **2. Working with Strings**

### **2.1 Creating Strings**

```python
greeting = "Hello, World!"
name = 'Alice'
```

You can also use triple quotes (`'''...'''` or `"""..."""`) for multi-line strings:

```python
long_text = """This is a multi-line
string that spans
multiple lines."""
```

### **2.2 String Concatenation**

- Combining two or more strings using the `+` operator.

```python
first_name = "Dor"
last_name = "Amar"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith
```

### **2.3 String Multiplication**

- Repeating a string multiple times using the  operator.

```python
echo = "Echo! " * 3
print(echo)  # Output: Echo! Echo! Echo!
```

### **2.4 Accessing Characters in a String (Indexing)**

- Access individual characters using indices. Indices start at 0.

```python
word = "Python"
print(word[0])  # Output: P
print(word[2])  # Output: t
```

### **2.5 Slicing Strings**

- Extracting a substring using `[start:end]`.

```python
text = "Hello, World!"
print(text[0:5])  # Output: Hello
print(text[7:12]) # Output: World
```

### **2.6 Common String Methods**

- **`upper()`**: Converts all characters to uppercase.
- **`lower()`**: Converts all characters to lowercase.
- **`strip()`**: Removes whitespace from the beginning and end.
- **`replace(old, new)`**: Replaces occurrences of `old` with `new`.

**Examples**:

```python
message = " Hello, World! "
print(message.upper())     # Output:  HELLO, WORLD!
print(message.lower())     # Output:  hello, world!
print(message.strip())     # Output:  Hello, World!
print(message.replace("World", "Python"))  # Output: Hello, Python!
```

### **String Formatting**

String formatting allows you to insert values into strings. Here are some popular methods:

### f-strings (Python 3.6+)

```python
name = "Dor"
age = 27
print(f"My name is {name} and I'm {age} years old.")
```

### **String Length**

To get the length of a string, use the `len()` function:

```python
text = "Hello, World!"
print(len(text))  # Output: 13
```

### **Check Substring Presence**

You can check if a substring is present in a string using the `in` keyword:

```python
text = "Hello, World!"
print("Hello" in text)   # Output: True
print("Python" in text)  # Output: False
```

### **3. Working with Numbers**

### **3.1 Basic Arithmetic Operations**

- Addition (`+`), Subtraction (), Multiplication (), Division (`/`), and Exponentiation (`*`).

**Examples**:

```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a ** b) # Output: 1000
```

### **3.2 Converting Between Types**

- **`int()`**: Converts a value to an integer.
- **`float()`**: Converts a value to a float.
- **`str()`**: Converts a value to a string.

**Examples**:

```python
num_str = "123"
num_int = int(num_str)
print(num_int)  # Output: 123

num_float = float(num_int)
print(num_float)  # Output: 123.0

num_to_str = str(num_float)
print(num_to_str)  # Output: "123.0"
```

[Math Functions](https://www.notion.so/Math-Functions-1326059138ae804cb3fef093dc836d8e?pvs=21) 

### **4. Indexing and Slicing**

### **4.1 Indexing Strings**

- Access individual characters using their position.

```python
phrase = "Hello"
print(phrase[0])  # Output: H
print(phrase[4])  # Output: o
```

### **String Slicing**

Slicing allows you to get a specific range of characters from a string. The syntax for slicing is:

```python
string[start:end]
```

- `start`: The index to start from (inclusive).
- `end`: The index to stop at (exclusive).

```python
text = "Hello, World!"

# Get characters from index 0 to 4
print(text[0:5])   # Output: Hello

# Get characters from index 7 to the end
print(text[7:])    # Output: World!

# Get characters from the beginning to index 4
print(text[:5])    # Output: Hello
```

### **4.3 Negative Indexing**

- Negative indices start from the end of the string.

```python
word = "Python"
print(word[-1])  # Output: n
print(word[-3])  # Output: h
```

### **Step in Slicing**

You can specify a step to select characters at a certain interval. The syntax is:

```python
string[start:end:step]
```

The `step` determines how many characters to skip. A step of `2` selects every second character.

```python
text = "Hello, World!"

# Get every second character
print(text[::2])  # Output: Hlo ol!

# Get every second character in reverse
print(text[::-2]) # Output: !drWolH
```

### **Reversing a String**

You can use slicing with a negative step to reverse the string.

```python
text = "Hello, World!"

# Reverse the string
print(text[::-1])  # Output: !dlroW ,olleH
```

### **5. Practical Exercises**

### **Exercise 1: Print First and Last Character**

- Write a program that stores a string and prints its first and last character.

**Example**:

```python
text = "Example"
print(text[0])   # Output: E
print(text[-1])  # Output: e
```

### **Exercise 2: String Slicing**

- Ask the user for a word and print a substring containing the first three characters.

**Example**:

```python
word = input("Enter a word: ")
print(word[:3])
```

### **Exercise 3: Basic Arithmetic with User Input**

- Ask the user for two numbers and print their sum, difference, product, and quotient.

**Example**:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

```

### **Exercise 4: String Manipulation**

- Ask the user for a sentence, convert it to uppercase, and print the length of the sentence.

**Example**:

```python
sentence = input("Enter a sentence: ")
print(sentence.upper())
print("Length:", len(sentence))

```

### **Exercise 5: Replace in a String**

- Create a string that contains a sentence. Replace one word in the sentence with another word and print the new sentence.

**Example**:

```python
sentence = "I love programming."
new_sentence = sentence.replace("programming", "Python")
print(new_sentence)  # Output: I love Python.
```