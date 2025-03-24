# Password Generator

### Objective

Build a **Password Generator** that creates strong passwords using random characters: letters, numbers, and symbols. Let the user choose the password length and character types.

---

## You Will

- Using the `random` and `string` modules
- Generating random characters and shuffling lists
- Building a command-line interface with `input()`
- Validating user input
- Joining lists into strings
- Writing modular and clean Python code

---

## 🛠️ Project Tasks

---

### 🔹 Task 1: Import Required Modules

Use Python's built-in modules:

```python
import random
import string

```

---

### 🔹 Task 2: Ask the User

Prompt the user for:

- Desired password length
- Include letters? (y/n)
- Include digits? (y/n)
- Include symbols? (y/n)

---

### 🔹 Task 3: Build Character Pool

Use the `string` module to add characters:

- `string.ascii_letters` → a-z + A-Z
- `string.digits` → 0-9
- `string.punctuation` → special characters

Build the character pool based on the user's input.

---

### 🔹 Task 4: Generate and Shuffle

- Use `random.choices()` to generate a list of characters
- Shuffle the password using `random.shuffle()`
- Join the list into a final password string

---

### 🔹 Task 5: Handle Errors

Add validation:

- If the user doesn’t choose any character type, show an error.
- If password length is less than or equal to 0, ask again.