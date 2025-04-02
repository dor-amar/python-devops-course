# Working with JSON Files in Python

JavaScript Object Notation (JSON) is a data exchange format. While originally designed for JavaScript, these days many computer programs interact with the web and use JSON.

Interacting with the web is mostly done through APIs (Application Programmable Interface), in JSON format.

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

| JSON Data Type | Description |
| --- | --- |
| `object` | A collection of key-value pairs inside curly braces (`{}`) |
| `array` | A list of values wrapped in square brackets (`[]`) |
| `string` | Text wrapped in double quotes (`""`) |
| `number` | Integers or floating-point numbers |
| `boolean` | Either `true` or `false` without quotes |
| `null` | Represents a [null value](https://realpython.com/null-in-python/), written as `null` |

Just like in dictionaries and lists, you’re able to nest data in JSON objects and arrays. For example, you can include an object as the value of an object. Also, you’re free to use any other allowed value as an item in a JSON array.

---

## **Correct Way to Work With JSON Files**

Use this pattern:

```python
import json

with open("transactions.json") as f:
    data = json.load(f)  # parse the full structure once

for entry in data:
    print(entry["event"])
```

Now you're working with Python objects: `dict`s and `list`s, just like you would if you'd manually typed them in Python.

---

### **Convert Python Dictionaries to JSON**

```python
import json

data = {
    "name": "Jessica",
    "age": 30,
    "is_admin": True,
    "skills": ["python", "devops"]
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))
```

🧾 **Output**:

```json
{"name": "Alice", "age": 30, "is_admin": true, "skills": ["python", "devops"]}
```

After importing the `json` module, you can use [`.dumps()`](https://docs.python.org/3/library/json.html#json.dumps) to convert a Python dictionary to a **JSON-formatted string**, which represents a JSON object.

It’s important to understand that when you use `.dumps()`, you get a Python string in return. In other words, you don’t create any kind of JSON data type. The result is similar to what you’d get if you used Python’s built-in [`str()` function](https://realpython.com/python-strings/)

**Note:** When you convert a dictionary to JSON, the dictionary keys will always be strings in JSON.

```python
import json

data = {
    1: "one",
    2: "two",
    3: "three"
}

json_string = json.dumps(data)
print(json_string)
```

### Output:

```json
{"1": "one", "2": "two", "3": "three"}
```

Notice that the **integer keys** `1`, `2`, `3` are now **strings** `"1"`, `"2"`, `"3"` in the JSON output.

When you use `json.dumps()`, you can use [additional arguments](https://docs.python.org/3/library/json.html#json.dumps) to control the look of the resulting JSON-formatted string

- `indent` – adds line breaks and indentation (pretty print)
- `sort_keys` – sorts keys alphabetically
- `separators` – customizes the spacing between elements
- `ensure_ascii` – handles Unicode characters

## **Example Dictionary**

```python
import json

data = {
    "name": "Jessica",
    "age": 30,
    "admin": True,
    "skills": ["python", "devops"]
}
```

---

### `indent`: Pretty Print with Indentation

```python
print(json.dumps(data, indent=4))
```

### `sort_keys`: Sort Keys Alphabetically

```python
print(json.dumps(data, indent=2, sort_keys=True))
```

---

### `separators`: Remove Whitespace for Compact Output

```python
print(json.dumps(data, separators=(",", ":")))
```

---

### `ensure_ascii=False`: Keep Unicode Characters Readable

```python
emoji_data = {"message": "Hello 👋"}
print(json.dumps(emoji_data, ensure_ascii=False))
```

---

### **Write a JSON File With Python**

The JSON format can come in handy when you want to save data outside of your Python program. Instead of spinning up a database, you may decide to use a JSON file to store data for your workflows. Again, Python has got you covered.

The `json.dump()` function has two required arguments:

1. The object you want to write
2. The file you want to write into

### 🧪 **Example**

```python
import json

# Python dictionary
data = {
    "name": "Jessie",
    "age": 30,
    "is_admin": True,
    "skills": ["python", "devops"]
}

# Write it to a file
with open("user.json", "w") as f:
    json.dump(data, f)
```

This creates a file named `user.json` in the current directory with the dictionary saved in **JSON format**.

### Want It to Look Prettier?

Add `indent=4` to make the file human-readable:

```python
json.dump(data, f, indent=4)
```

| Action | Method |
| --- | --- |
| Dict → JSON string | `json.dumps(data)` |
| Dict → JSON file | `json.dump(data, file)` |

---

## **Reading JSON With Python**

In the former sections, you learned how to serialize Python data into JSON-formatted strings and JSON files. Now, you’ll see what happens when you load JSON data back into your Python program.

In parallel to `json.dumps()` and `json.dump()`, the `json` library provides two functions to deserialize JSON data into a Python object:

The **two main ways** to read JSON depending on the source:

| Use Case | Function |
| --- | --- |
| Reading JSON from a file | `json.load()` |
| Reading JSON from a string | `json.loads()` |
1. `json.loads()`: To deserialize a string, bytes, or [byte array](https://realpython.com/python-mutable-vs-immutable-types/#byte-arrays) instances
2. `json.load()`: To deserialize a text file or a binary file

As a rule of thumb, you work with `json.loads()` when your data is already present in your Python program. You use `json.load()` with external files that are saved on your disk.

### **Read JSON From a File**

If you have a file called `user.json` already.

You can read it like this:

```python
import json

with open("user.json", "r") as f:
    data = json.load(f)

print(data["name"])      # Alice
print(data["skills"])    # ['python', 'devops']
```

 `json.load()` converts the file content into a **Python dictionary**.

---

## **How to Open an External JSON File in Python**

> 🧠 An external JSON file simply means a .json file stored on your local disk or in a specific directory (not hardcoded into the script).
> 

---

### **Example JSON File: `config.json`**

Make sure you have a file named `config.json` in your project folder:

```json
{
    "app_name": "Inventory Tracker",
    "version": "1.0",
    "debug": true,
    "max_items": 100
}
```

---

### **Python Code to Open and Read It**

```python
import json

# Open the external JSON file
with open("config.json", "r") as f:
    config = json.load(f)

# Access values from the JSON
print("App Name:", config["app_name"])
print("Debug Mode:", config["debug"])

```

---

**Key Points**

- `open("config.json", "r")` opens the file in **read mode**
- `json.load(f)` parses the file into a **Python dictionary**
- You can now access values using standard Python syntax (`config["key"]`)

---

### What If the File Is in Another Folder?

```python
with open("configs/settings/config.json") as f:
    config = json.load(f)
```

Just provide the **correct path** relative to where your Python script is running.

---

### If the File Doesn’t Exist

Add error handling to avoid crashes:

```python
try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("File exists but contains invalid JSON.")
```

### 🧠 Summary

| Goal | Method |
| --- | --- |
| Open JSON file | `with open("file.json")` |
| Parse JSON to dict | `json.load(file_object)` |

---

### **Validate** JSON syntax

You can use the built-in `json` module and attempt to parse the data using `json.loads()` (for strings) or `json.load()` (for files).

If the JSON is **invalid**, Python will raise a `json.JSONDecodeError`.

## Validate JSON From a String

```python
import json

json_str = '{"name": "Alice", "age": 30}'  # ✅ Valid JSON

try:
    parsed = json.loads(json_str)
    print("✅ JSON is valid!")
except json.JSONDecodeError as e:
    print("❌ Invalid JSON:", e)
```

---

## Sources

- Python Docs: https://docs.python.org/3/library/json.html
- Real Python JSON tutorial: https://realpython.com/python-json/