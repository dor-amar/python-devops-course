# JSON

# Working with JSON Files in Python

## Objective:

By the end of this class, you will:

- Understand what JSON is
- Learn how to parse JSON strings
- Learn how to read and write JSON files using Python
- Understand practical use cases (e.g., configs, APIs)

---

## What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data-interchange format that's:

- Easy to read and write for humans
- Easy to parse and generate by machines

It's commonly used to:

- Exchange data between a client and a server (APIs)
- Store configuration files
- Save structured data (like lists, dictionaries)

### 🧾 Example of a JSON object:

```json
{
  "name": "Dor",
  "age": 30,
  "is_teacher": true,
  "skills": ["Python", "DevOps", "Linux"]
}
```

It looks just like a Python dictionary — and that's the key idea!

---

## Python’s `json` Module

Python comes with a built-in `json` module to work with JSON data.

### 1. **Parsing JSON Strings**

Convert a JSON string into a Python dictionary:

```python
import json

data = '{"name": "Dor", "age": 30}'
parsed = json.loads(data)
print(parsed["name"])  # Output: Dor
```

### 2. **Converting Python to JSON String**

```python
person = {
  "name": "Dor",
  "skills": ["Python", "Docker"],
  "is_teacher": True
}

json_string = json.dumps(person)
print(json_string)
```

### Note:

- `dumps()` = Python ➜ JSON string
- `loads()` = JSON string ➜ Python

---

## Reading and Writing JSON Files

### 3. **Writing a Python object to a JSON file:**

```python
data = {
  "course": "DevOps",
  "duration": "10 months"
}

with open("data.json", "w") as file:
    json.dump(data, file)
```

### 4. **Reading from a JSON file:**

```python
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["course"])  # Output: DevOps

```

### Note:

- `dump()` = Python ➜ File (JSON)
- `load()` = File (JSON) ➜ Python

---

## Formatting Options in `json.dumps()`

```python
print(json.dumps(data, indent=2))
```

Optional parameters:

- `indent=2` – pretty prints JSON
- `sort_keys=True` – sorts dictionary keys

---

## Real-Life Use Cases

- **Config files**: Store app settings (like DB URLs, secrets)
- **APIs**: Sending and receiving JSON data
- **Storing Data**: Save user info or logs in structured format

---

## Mini Exercise (In-Class)

```python
# 1. Create a dictionary with your name, age, and 2 hobbies
# 2. Write it to a file called "student.json"
# 3. Read the file and print your hobbies
```

---

## 📚 Sources

- Python Docs: https://docs.python.org/3/library/json.html
- Real Python JSON tutorial: https://realpython.com/python-json/