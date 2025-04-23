# Basic File Operations

File operations are a fundamental part of working with data in Python. They allow you to read from and write to files, enabling you to store data persistently or process data from external sources. Python provides built-in functions to handle file operations easily.

### **Common Use Cases for File Operations**

- **Data Storage:** Saving program data, such as configuration settings or user information, for later use.
- **Logging:** Writing logs or errors to a file to keep track of events during program execution.
- **Configuration Files:** Loading configurations from files to change how the program behaves without modifying the code.
- **Data Processing:** Reading large datasets from files, processing them, and possibly saving processed results.
- **Reports Generation:** Creating report files (e.g., CSV, text) for exporting processed data or analysis results.

### Basic File Operations in Python

1. **Opening a File**
2. **Reading from a File**
3. **Writing to a File**
4. **Closing a File**
5. **Using `with` Statement for Files**
6. **File Modes**
7. **Working with Different File Types**

### 1. Opening a File

Before you can read from or write to a file, you need to open it using the `open()` function. The `open()` function requires at least one argument: the name of the file. It can also take a second optional argument that specifies the mode (e.g., read, write).

**Syntax:**

```python
file_object = open('filename', 'mode')
```

**Example:**

```python
file = open('example.txt', 'r')  # Open a file named 'example.txt' in read mode
```

### 2. Reading from a File

Once a file is opened in read mode, you can read its contents using various methods:

- **`read()`**: Reads the entire file.
- **`readline()`**: Reads one line from the file.
- **`readlines()`**: Reads all lines from the file into a list.

**Example:**

```python
file = open('file.txt', 'r')
print(file.read())

# First 4 
print(file.read(4))

# Read first line 
print(file.readline())

# What happened if duplicated ? 
print(file.readline())
print(file.readline())

# Iterate
for line in file:
    print(line)

# Close Stream 
file.close()

# Try open a file that i dont have 
try:
    file = open('dor.txt','r')
    print(file.read())
except:
    print("No such file")
finally:
    file.close()
```

### 3. Writing to a File

You can write to a file by opening it in write mode (`'w'`) or append mode (`'a'`). If the file does not exist, it will be created. If it exists and is opened in write mode, the content will be overwritten.

- **`write()`**: Writes a string to the file.

**Example:**

```python
file = open("file.txt","a")
file.write("Last Line !")
file.close()

file = open("file.txt","r")
print(file.read())
file.close()

f = open("file.txt",'w')
f.write("Override")
f.close()

file = open("file.txt","r")
print(file.read())
file.close()
```

### 4. Creating New Files (2 ways)

```python
file = open("new_file.txt", "w")
file.close()

# Create file but returnes error if the file exists

import os 
if not os.path.exists("dor.txt"):
    f = open("dor.txt","x")
    f.close()
```

### 4. Delete a file

```python
import os 
if os.path.exists("dor.txt"):
    os.remove("dor.txt")
else: 
    print("File not exist")
```

### 5. Using `with` Statement for Files

A better way to handle files in Python is by using the `with` statement. This automatically takes care of closing the file, even if an error occurs during file operations.

**Example:**

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to explicitly close the file

```

### 6. File Modes

The second argument to `open()` is the mode. Here are some common file modes:

- **`'r'`**: Read mode (default). Opens the file for reading.
- **`'w'`**: Write mode. Opens the file for writing (overwrites the file if it exists).
- **`'a'`**: Append mode. Opens the file for appending (writes to the end of the file).
- **`'b'`**: Binary mode. Used with other modes (e.g., `'rb'`, `'wb'`) to open the file in binary format.
- **`'x'`**: Exclusive creation mode. Fails if the file already exists.
- **`'+'`**: Read and write mode (e.g., `'r+'`, `'w+'`).

## **Exercises for Class**

### Exercise 1: Creating and Writing to a File

**Objective:** Learn how to create a new file and write content to it.

1. Write a Python script that creates a new text file named `my_first_file.txt`.
2. Write the following text into the file: `"Hello, World! This is my first file operation in Python."`
3. Close the file after writing.

**Bonus:** Modify the script to append the text `"Adding more content to my file."` to the existing file without overwriting the original content

```python
# Step 1: Create a new file and open it for writing
with open('my_first_file.txt', 'w') as file:
    # Step 2: Write the text into the file
    file.write("Hello, World! This is my first file operation in Python.")

# The file is automatically closed when the 'with' block is exited

# Bonus: Appending text to the existing file
with open('my_first_file.txt', 'a') as file:
    file.write("\nAdding more content to my file.")

```

### Exercise 2: Reading from a File

**Objective:** Practice reading the contents of a file.

1. Using the file `my_first_file.txt` created in Exercise 1, write a Python script that opens the file and reads its contents.
2. Print the contents of the file to the console.
3. Close the file after reading.

**Bonus:** Modify the script to read and print the file line by line instead of all at once.

```python
# Step 1: Open the file for reading
with open('my_first_file.txt', 'r') as file:
    # Step 2: Read the contents of the file
    content = file.read()

    # Step 3: Print the contents to the console
    print(content)

# The file is automatically closed when the 'with' block is exited

# Bonus: Reading and printing the file line by line
with open('my_first_file.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes extra newline characters

```

### Exercise 4: Counting Words in a File

**Objective:** Learn how to read a file and perform simple text processing.

1. Write a Python script that opens the file `my_first_file.txt` (or any text file of your choice) and reads its contents.
2. Count the number of words in the file. A word is defined as any sequence of characters separated by spaces.
3. Print the word count to the console.

**Bonus:** Modify the script to also count the number of lines in the file.

```python
# Step 1: Open the file for reading
with open('my_first_file.txt', 'r') as file:
    # Step 2: Read the contents of the file
    content = file.read()

    # Step 3: Split the content into words
    words = content.split()

    # Step 4: Count the number of words
    word_count = len(words)

    # Step 5: Print the word count
    print(f"Word count: {word_count}")

# Bonus: Count the number of lines
with open('my_first_file.txt', 'r') as file:
    line_count = len(file.readlines())
    print(f"Line count: {line_count}")

```

### Exercise 5: Searching for a Word in a File

**Solution:**

```python
# Step 1: Ask the user for a word to search
search_word = input("Enter the word to search for: ")

# Step 2: Open the file for reading
with open('my_first_file.txt', 'r') as file:
    # Step 3: Read the contents of the file
    content = file.read()

    # Step 4: Count the occurrences of the word
    word_count = content.count(search_word)

    # Step 5: Print the number of occurrences
    print(f"The word '{search_word}' appears {word_count} times in the file.")

# Bonus: Case-insensitive search
with open('my_first_file.txt', 'r') as file:
    content = file.read().lower()
    search_word_lower = search_word.lower()
    word_count = content.count(search_word_lower)
    print(f"The word '{search_word}' (case-insensitive) appears {word_count} times in the file.")

```

### 7. Working with Different File Types

### **Text Files**

Text files are the most common type of file, where data is stored as plain text.

**Example:**

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Print each line without the newline character

```

### **Binary Files**

Binary files contain data in binary format (e.g., images, executables). You can open and manipulate them using the `'b'` mode.

**Example:**

```python
with open('image.png', 'rb') as file:
    data = file.read()
    print(data[:10])  # Print the first 10 bytes of the image file

```

### Example: Working with Files

Let's walk through a real-world example of working with files. Suppose you have a text file called `students.txt` that contains a list of student names, one per line. You want to read this file, count the number of students, and then write this count to a new file called `count.txt`.

**students.txt:**

```
Alice
Bob
Charlie
David
```

**Python Script:**

```python
# Step 1: Read the file and count the number of lines (students)
with open('students.txt', 'r') as file:
    students = file.readlines()
    student_count = len(students)

# Step 2: Write the student count to a new file
with open('count.txt', 'w') as file:
    file.write(f"Number of students: {student_count}\n")

```

**Output in `count.txt`:**

```jsx
Number of students: 4

```

### Final Thoughts on File Operations

- **Always close files**: Either explicitly using `close()` or by using the `with` statement.
- **Be mindful of file modes**: Using the wrong mode can lead to unexpected data loss (e.g., using `'w'` instead of `'a'`).
- **Handle exceptions**: When working with files, especially in production code, it's good practice to handle exceptions (e.g., file not found).

---
## Navigation

[⬅️ Previous: Exception Handling in Python](exception-handling.md) | [Next: Working with JSON Files in Python ➡️](json.md)
