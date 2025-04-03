# Build a Python Utility Module for File Analysis

You will create a **reusable Python module** that analyzes `.txt` files and provides useful statistics, such as:

- Word count
- Line count
- Character count
- Most common word
- Frequency of each word

They will then **import and use** this module in a separate script to analyze any file of their choice.

---

## Folder Structure

```
project/
├── file_utils.py     # Custom module with file analysis logic
└── analyzer.py       # Script that uses the module
```

---

## Learning Outcomes

By completing this lab, You will:

- Create and structure an advanced Python module
- Use `collections.Counter`, `with open()`, and file reading techniques
- Handle exceptions (file not found, empty file, etc.)
- Use `__name__ == "__main__"` to test modules
- Build code that could be used in real-world automation or CLI tools

---

## Instructions

---

### Task 1: Create the Module – `file_utils.py`

Create functions:

1. `get_word_count(file_path)`
2. `get_line_count(file_path)`
3. `get_char_count(file_path)`
4. `get_most_common_word(file_path)`
5. `get_word_frequencies(file_path)` → returns a dictionary

Add `__name__ == "__main__"` to run tests on a sample file (`sample.txt`).

Example:

```python
if __name__ == "__main__":
    print(get_word_count("sample.txt"))
```

Use `collections.Counter` for counting words.

---

### Task 2: Build `analyzer.py`

Write a CLI-style script that:

1. Prompts the user to enter the file path.
2. Uses the `file_utils` module to:
    - Display total words, lines, characters
    - Show the top 5 most frequent words
3. Displays an error message if the file doesn’t exist.

---

### Task 3 Export Results

Allow the user to choose if they want to export the results to `results.txt`.

---

## Sample Code Snippets

### `file_utils.py`