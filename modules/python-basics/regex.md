### What is Regex?

**Regular Expressions** are patterns used to match sequences of characters in strings.

Think of it like a **search-and-replace** tool on steroids. Instead of literal search, you define a pattern, and Python will look for matches.

---

### When Should You Use Regex?

Use **regex** when you need to:

- Validate inputs (emails, phone numbers, passwords)
- Search for complex patterns in text
- Extract parts of strings (e.g., domain names, hashtags)
- Replace patterns in strings (e.g., remove HTML tags)
- Parse logs, config files, or structured text formats (e.g., CSV-like but messy)

---

### The `re` Module in Python

Python’s built-in `re` module provides regex support.

```python
import re
```

---

### Simple Matching

### Example 1: Match a word in a sentence

```python
import re

text = "Hello, my name is Dor."
match = re.search("name", text)

if match:
    print("Found:", match.group())  # Output: Found: name
```

- `re.search()` scans the `text` for the **first location** where the **pattern** `"name"` appears.
- In this case, `"name"` is found at index 11 in the sentence.

We are searching the text for the word `"name"` using regex. If it exists, you print it. The function `re.search()` returns a match object if found, or `None` otherwise.

### Matching Multiple Occurrences

If you want to **find all matches** of a pattern (e.g., the word `"name"` appears more than once), you should use `re.findall()` instead of `re.search()`.

---

### Example:

```python
import re

text = "My name is Dor. What's your name? Name is important."
matches = re.findall(r"\bname\b", text, flags=re.IGNORECASE)

print(matches)
```

### Explanation:

- `re.findall()` returns **all matches** of the pattern as a list.
- `\bname\b` ensures you match the **whole word** `name` only.
- `flags=re.IGNORECASE` makes it **case-insensitive**, so it matches `"name"` and `"Name"`.

### Output:

```python
['name', 'name', 'Name']
```

### Simple Explanation of `\b` (Word Boundary):

`\b` is like saying:

**"Only match this word if it stands alone, or is clearly the start or end of a word."**

---

## **Common Regex Functions and Patterns**

| Function | Description |
| --- | --- |
| `re.search()` | Search for the **first match** |
| `re.findall()` | Return **all matches** as a list |
| `re.match()` | Match only at the **beginning of the string** |
| `re.sub()` | Replace parts of the string |
| `re.compile()` | Compile a regex for repeated use |

| Pattern | Matches |
| --- | --- |
| `.` | Any character except newline |
| `\d` | Digit (0–9) |
| `\w` | Word character (a-z, A-Z, 0–9, _) |
| `\s` | Whitespace |
| `\D` | Non-digit |
| `\W` | Non-word character |
| `\S` | Non-whitespace |
| `^` | Start of string |
| `$` | End of string |
| `[]` | Any one of the characters inside |
| ` | ` |
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | Exactly n times |
| `{n,m}` | Between n and m times |
| `()` | Group |

---

### Extract Digits from a String

```python
text = "Order #1234 from 2023"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['1234', '2023']
```

### Breaking down `\d+`:

- `\d` → Matches any **digit** (same as `[0-9]`)
- `+` → Means "**one or more**" of the preceding token

So together, `\d+` means:

> “Match a group of one or more digits.”
> 

---

### Find All Lines Containing the Word "error" in a Text File

This example shows how to read a `.txt` file and find all lines that contain the word **"error"** (case-insensitive), which is common in log parsing and DevOps.

---

### Example Code

```python
import re

with open("logfile.txt", "r") as file:
    lines = file.readlines()

error_lines = []

for line in lines:
    if re.search(r"\berror\b", line, re.IGNORECASE):
        error_lines.append(line.strip())

# Print all error lines
for err in error_lines:
    print(err)
```

---

### What This Does:

- `open("logfile.txt", "r")`: Opens the file for reading.
- `re.search(r"\berror\b", line, re.IGNORECASE)`:
    - Matches the word `"error"` only as a **whole word** (because of `\b`).
    - Ignores case, so it matches `"Error"`, `"ERROR"`, `"error"`, etc.
- `.strip()`: Removes newline characters and spaces.

---

### **Find All Capitalized Words**

```python
import re

text = "Alice and Bob went to New York."
caps = re.findall(r"\b[A-Z][a-z]*\b", text)

print(caps)  # ['Alice', 'Bob', 'New', 'York']
```

- `\b` → word boundary
- `[A-Z]` → first letter is uppercase
- `[a-z]*` → followed by 0 or more lowercase letters

---

## Validate Email

```python
email = "hello@domain.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email")
```

### 1. `email = "hello@domain.com"`

- This is the string we want to validate — an email address.

### 2. `pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"`

Let’s break down this regex:

| Part | Meaning |
| --- | --- |
| `^` | Start of the string |
| `[\w\.-]+` | One or more word characters (`a-z`, `A-Z`, `0-9`, `_`) or dot `.` or hyphen `-` — for the **username** part |
| `@` | The "@" symbol — required in every email |
| `[\w\.-]+` | One or more valid domain name characters |
| `\.` | A literal dot (.) separating domain and extension |
| `\w+` | One or more word characters — for the domain extension (e.g., `com`, `org`) |
| `$` | End of the string |

### 3. `re.match(pattern, email)`

- Tries to match the regex pattern **starting from the beginning** of the email string.

### 4. `if re.match(...)`

- If the match is successful (i.e., valid format), print `"Valid email"`.

---

### Extract Domain Names from URLs

```python
urls = ["https://www.google.com", "http://openai.com"]
pattern = r"https?://([\w\.]+)"

domains = [re.search(pattern, url).group(1) for url in urls]
print(domains)  # ['www.google.com', 'openai.com']
```

---

### When Do We Usually Use Regex?

We use **regex** when we need to **search, extract, validate, or replace** text based on a **pattern**, not just a fixed value.

Here are the most common real-life scenarios:

---

### **Input Validation**

- Check if an email, phone number, username, or password is valid.

```python
re.match(r"^\d{10}$", phone_number)  # Exactly 10 digits
```

---

### **Text Extraction**

- Get all emails, URLs, hashtags, numbers, etc., from a large text or webpage.

```python
re.findall(r"https?://\S+", text)  # Finds all URLs
```

---

### **Log or File Parsing**

- Search logs for errors, warnings, IP addresses, or user actions.

```python
re.search(r"\bERROR\b", line)
```

---

### **Search and Replace**

- Clean up text, remove HTML tags, format data.

```python
re.sub(r"<.*?>", "", html)  # Remove all HTML tags
```

---

### **Natural Language or Text Analysis**

- Tokenize words, extract keywords, analyze sentence structure.

```python
re.findall(r"\b\w+\b", paragraph)
```

---

### 🔧 Summary:

> Use regex whenever you need smart, pattern-based text processing that string functions (split, replace, find) can't handle easily.
> 

**My personal take is that regex can be generated by tools or AI as long as we understand it !**