# Basics of Dictionaries

### 1. Basics of Dictionaries

A dictionary in Python is a collection of key-value pairs, where each key is unique, and each key is associated with a value. Here's a quick overview of how dictionaries work:

### **Example:**

```python
student = {
'name': 'Dor',
'age': 27,
'courses': ['Math','Computer Scince'],
'rate': 7.6
}
```

In this dictionary, `"Alice"`, `"Bob"`, and `"Charlie"` are keys, and `85`, `92`, and `78` are their corresponding values.

### 2. Accessing and Modifying Dictionary Values

You can access values in a dictionary by using the keys. You can also modify the values associated with a key.

### **Example:**

```python
# Accessing a value
print(student['name'])
print(student['age'])
print(student['courses'][1]) 
print(student['rate'])
```

### Get Method:

```python
print(student.get('rate'))
print(student.get('age'))

print(student.get('phone'))
print(student.get('phone', 'Not Found'))
```

### 3.Adding Items to a Dictionary

You can add a new key-value pair to a dictionary by simply assigning a value to a new key.

### **Example:**

```python
student['phone'] = '0524444444'
print(student.get('phone', 'Not Found'))

# Update
student['name']  = 'Dori' # Replace
print(student['name'])

student.update({'name': "Ziv",'age': 45, 'phone':'0603237231'}) # Update Method
print(student)
```

### 4. Removing Items from a Dictionary

You can remove items from a dictionary using the `del` statement, the `pop()` method, or the `popitem()` method.

### **Using `del`:**

The `del` statement removes the item with the specified key.

```python
del student['age'] # Delete Age
print(student)
```

### **Using `pop()`:**

The `pop()` method removes the item with the specified key and returns the value.

```python
name = student.pop('name')

print(name)
print(student)
```

### **Using `popitem()`:**

The `popitem()` method removes the last inserted key-value pair from the dictionary and returns it as a tuple.

```python
last_item = student.popitem()
print(last_item)
print(student)
```

In this example, `popitem()` removes and returns the last inserted item, `"David": 88`.

### 5. Iterating Through a Dictionary

You can loop through a dictionary to access keys, values, or both.

### **Example:**

```python

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# Iterating through keys
for key in student:
    print(key)

# Iterating through values
for key, value in student.items():
    print(key, value)
```

Now, let’s go over the two different ways of looping through the dictionary.

### 5. `for key in student:`

This loop goes through each **key** in the `student` dictionary and prints it. By default, looping through a dictionary will go through the keys.

```python
for key in student:
    print(key)
```

- **Example Output**: For `{'name': 'Alice', 'age': 20, 'grade': 'A'}`, this loop would print:
    
    ```
    name
    age
    grade
    
    ```
    

### 6. `for key, value in student.items():`

This loop goes through each **key-value pair** in the dictionary. The `items()` method returns each key-value pair as a tuple, which is unpacked into `key` and `value`.

```python
for key, value in student.items():
    print(key, value)
```

- **Example Output**: For `{'name': 'Alice', 'age': 20, 'grade': 'A'}`, this loop would print:
    
    ```css
    name Alice
    age 20
    grade A
    ```
    

### Exercise 1: **Count the Frequency of Characters in a String**

**Problem:**
Write a program that takes a string as input and counts the frequency of each character. Store the character frequencies in a dictionary, where the keys are the characters and the values are the frequencies.

**Solution:**

```python
def count_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

my_input = "Hello my name is dor"
print(count_chars(my_input))
```

**Output:**

```python
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### **Done**

### Exercise 2: **Merge Two Dictionaries**

**Problem:**
Write a program to merge two dictionaries. If there are common keys between the two dictionaries, add the values together. Store the result in a new dictionary.

**Solution:**

```python
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with dict1
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add values if key exists
        else:
            merged_dict[key] = value  # Add new key-value pair
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_dictionaries(dict1, dict2)
print(result)

```

**Output:**

```python
{'a': 1, 'b': 5, 'c': 7, 'd': 5}

```

### Exercise 3: **Calculate Product of All Values in a Dictionary**

**Problem:**
Write a program to calculate the product of all the values in a dictionary where the values are integers. If the dictionary is empty, return 1.

**Solution:**

```python
def product_of_values(d):
    product = 1
    for value in d.values():
        product *= value
    return product

# Example usage:
numbers = {'a': 2, 'b': 3, 'c': 4}
result = product_of_values(numbers)
print(result)

```

**Output:**

```python
24

```

### Exercise 4: **Find the Most Frequent Word in a Sentence**

**Problem:**
Write a program that takes a sentence as input and finds the word that appears the most frequently. Store the word frequencies in a dictionary, where the keys are the words and the values are the frequencies, and then identify the word with the highest frequency.

**Solution:**

```python
def most_frequent_word(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Find the word with the highest frequency
    most_frequent = max(word_count, key=word_count.get)
    return most_frequent, word_count[most_frequent]

# Example usage:
sentence = "this is a test this is only a test"
result = most_frequent_word(sentence)
print(result)

```

**Output:**

```python
('this', 2)
```

### Exercise 5: **Invert a Dictionary**

**Problem:**
Write a program that takes a dictionary as input and inverts it. In other words, the keys become the values, and the values become the keys. If the same value appears multiple times, keep the last corresponding key in the resulting dictionary.

**Solution:**

```python
def invert_dictionary(d):
    inverted_dict = {}
    for key, value in d.items():
        inverted_dict[value] = key
    return inverted_dict

# Example usage:
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
result = invert_dictionary(original_dict)
print(result)

```

**Output:**

```python
{1: 'd', 2: 'b', 3: 'c'}

```

**Explanation:**
In this output, the key `1` originally associated with both `'a'` and `'d'` now only corresponds to `'d'` because it was the last key with that value in the dictionary.

These solutions should help you understand how to work with dictionaries in Python for various tasks. Let me know if you need any further clarification!



# Dictionary Usage

In Python, dictionaries are a go-to data structure when you need to store data in key-value pairs. They’re particularly useful for scenarios where you want quick access to data via a specific identifier (the key) without searching through a list. Here are some real-world scenarios where dictionaries are particularly useful:

### 1. **Storing User Profiles in a System**

- When creating a system that holds user data, you can use dictionaries to store each user's information (like username, email, role, etc.) and access it by user ID.
- Example:
    
    ```python
    user_profiles = {
        "user123": {"name": "Alice", "email": "alice@example.com", "role": "admin"},
        "user456": {"name": "Bob", "email": "bob@example.com", "role": "user"},
    }
    # Access user role
    role = user_profiles["user123"]["role"]
    ```
    

### 2. **Counting Occurrences in Data (e.g., Word Frequency)**

- When analyzing text data, you might want to count how often each word appears. A dictionary can map each word to its frequency.
- Example:
    
    ```python
    word_count = {}
    text = "hello world hello"
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    # Result: {'hello': 2, 'world': 1}
    ```
    

### 3. **Storing Configurations or Settings**

- Dictionaries are great for storing configurations, such as database settings, API keys, or user preferences.
- Example:
    
    ```python
    config = {
        "database": {"host": "localhost", "port": 3306},
        "api_keys": {"service1": "abcd1234", "service2": "xyz9876"}
    }
    ```
    

### 4. **Indexing Data by Unique Identifiers**

- If you’re working with data that has unique IDs (like product IDs or transaction IDs), you can use dictionaries to store data for quick access.
- Example:
    
    ```python
    products = {
        "P001": {"name": "Laptop", "price": 1000},
        "P002": {"name": "Smartphone", "price": 500},
    }
    # Access product price
    price = products["P001"]["price"]
    ```
    

### 5. **Mapping Between Different Sets of Data**

- Dictionaries are helpful for creating mappings, such as mapping country codes to country names, or student IDs to grades.
- Example:
    
    ```python
    country_codes = {"US": "United States", "FR": "France", "IN": "India"}
    ```
    

### 6. **Cashing Data for Faster Lookup**

- If your program needs to fetch data repeatedly (like recent search results or computed values), you can use a dictionary as a cache for fast retrieval.
- Example:
    
    ```python
    cache = {}
    def expensive_computation(x):
        if x in cache:
            return cache[x]
        # Suppose this calculation is slow
        result = x ** 2
        cache[x] = result
        return result
    ```
    

### 7. **Tracking Multiple Properties for Objects (Instead of Classes)**

- Sometimes, dictionaries are useful as lightweight objects to group properties related to a single item, such as an inventory or shopping cart.
- Example:
    
    ```python
    cart = {"apple": {"quantity": 2, "price": 0.5}, "banana": {"quantity": 3, "price": 0.2}}
    ```
    

Dictionaries offer fast, constant-time complexity for lookups, making them suitable for data where you need to search or retrieve values by keys efficiently.

---
## Navigation

[⬅️ Previous: List, Tuple, Set](list.md) | [Next: Dictionary VS JSON ➡️](dictionary-vs-json.md)
