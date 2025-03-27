# Dictionary ↔ JSON

## **Exercise:**

### Objective:

- Convert a Python dictionary to a JSON string.
- Save it to a file.
- Load it back from the file.
- Verify the data at every step.

---

### ✅ Step-by-step Instructions

### 1. Create a Python dictionary:

```python
person = {
    "name": "Dor",
    "age": 30,
    "skills": ["Python", "DevOps", "AWS"],
    "active": True
}

print("Original dictionary:", person)
print("Type:", type(person))
```

---

### 2. Convert the dictionary to a JSON string using `json.dumps()` and print it:

```python
import json

person_json = json.dumps(person)
print("\nJSON string:", person_json)
print("Type:", type(person_json))
```

---

### 3. Save the JSON string to a file using `json.dump()`:

```python
with open("person.json", "w") as f:
    json.dump(person, f)
print("\nSaved to person.json")
```

---

### 4. Load the JSON back from the file using `json.load()`:

```python
with open("person.json", "r") as f:
    loaded_person = json.load(f)

print("\nLoaded from file:", loaded_person)
print("Type:", type(loaded_person))
```

---

### 5. Compare the original dictionary with the one you loaded:

```python
print("\nIs the loaded data same as the original?", person == loaded_person)
```