# Lab: File Operations in Python

### Objectives

By the end of this lab, students will:

- Understand how to open, read, write, and append to files.
- Use context managers (`with` statement) for file handling.
- Handle file-related exceptions (like `FileNotFoundError`).
- Work with text files line by line.
- Perform basic file manipulation (read from one file and write to another).

---

## Introduction

Python makes it easy to work with files using built-in functions.

### File Modes:

- `'r'` – Read (default), error if file doesn’t exist.
- `'w'` – Write, creates or truncates the file.
- `'a'` – Append to the end of file.
- `'r+'` – Read and write.

Using `with open(...)` ensures that the file is closed properly even if an error occurs.

---

## Tasks

---

### 🔹 Task 1: Write to a File

Create a file named `notes.txt` and write the text `"Python is great for DevOps!"`.

```python
# Your code here
```

---

### 🔹 Task 2: Read the File

Read the contents of `notes.txt` and print them.

```python
# Your code here
```

---

### 🔹 Task 3: Append to the File

Append the line `"File operations are simple in Python."` to `notes.txt`.

---

### 🔹 Task 4: Read Line by Line

Open `notes.txt` and read it line by line using a loop. Print each line with its line number.

**Expected Output:**

```
Line 1: Python is great for DevOps!
Line 2: File operations are simple in Python.
```

---

### 🔹 Task 5: Handle File Not Found

Try to read from a file called `missing.txt` which doesn't exist. Catch the `FileNotFoundError` and print a friendly error message.

---

### 🔹 Task 6: Copy File Content

Read content from `notes.txt` and write it to a new file called `backup.txt`.

---

### 🔹 Bonus Task: Count Words

Count how many words are in `notes.txt`.

---

## ✅ Summary

You learned:

- How to use `open()` and `with` for file handling.
- File modes: read, write, append.
- Reading files in full or line by line.
- Handling exceptions for file access.
- Writing safer and cleaner code for file operations.