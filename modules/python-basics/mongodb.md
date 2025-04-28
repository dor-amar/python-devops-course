# MongoDB with Python

https://www.mongodb.com/resources/products/fundamentals/basics

https://cloud.mongodb.com/

---

# Class Goal:

By the end of this class, students will:

- Understand **what NoSQL** is (vs. SQL)
- Set up **MongoDB** locally
- Connect to MongoDB **using Python** (`pymongo`)
- Perform basic **CRUD operations** (Create, Read, Update, Delete)
- Understand **collections** and **documents**

---

# Quick Theory — SQL vs NoSQL

| SQL (Relational) | NoSQL (MongoDB) |
| --- | --- |
| Tables | Collections |
| Rows | Documents |
| Columns with fixed schema | Flexible structure (no fixed schema) |
| Relationships (Foreign Keys) | Embedded data inside documents |
| Example: PostgreSQL, MySQL | Example: MongoDB, DynamoDB |

**MongoDB stores data as JSON-like documents!**

---

# Install MongoDB Locally

```bash
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

MongoDB server runs **locally** on:

```
mongodb://localhost:27017
```

---

# Install pymongo (Python MongoDB Driver)

```bash
pip install pymongo
```

---

# Important MongoDB Concepts

| Concept | Meaning |
| --- | --- |
| Database | Group of collections (like a schema) |
| Collection | Group of documents (like a table) |
| Document | JSON-like object (data) |
| `_id` | Unique ID automatically created |
| No Schema | Each document can be different |

✅ MongoDB = very flexible!

---

# Basic Connection Example

Simple Python script to **connect to MongoDB**:

```python
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create/use a database
db = client['labdb']

# Create/use a collection
products = db['products']

print("Connected to MongoDB!")
```

**In MongoDB Atlas**, **databases and collections** are **only created** when you **actually insert data into them**.

**Just connecting or accessing** them from Python **does not create** them.

MongoDB is "lazy" — it **only saves** what is actually written.

## Code Explanation:

```python
from pymongo import MongoClient
```

**What this does:**

- Imports the `MongoClient` class from the `pymongo` library.
- `MongoClient` is the main tool we use to **connect** to a MongoDB server from Python.

---

```python
# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
```

**What this does:**

- Creates a **connection** to a **MongoDB server** running on your own computer (**localhost**) at the default MongoDB port **27017**.
- Now, `client` represents the connection to the MongoDB server.
- If MongoDB is running somewhere else (like on the cloud), you'd change this URL.

---

```python
# Create/use a database
db = client['labdb']
```

**What this does:**

- Accesses a **database** called `labdb`.
- If `labdb` already exists → it **connects** to it.
- If `labdb` does NOT exist → MongoDB will **create it automatically** when you first save data.

(MongoDB is very flexible — it doesn't force you to create databases manually.)

---

```python
# Create/use a collection
products = db['products']
```

**What this does:**

- Accesses a **collection** inside the database called `products`.
- Again:
    - If `products` exists → it **connects** to it.
    - If `products` does NOT exist → MongoDB will **create it automatically** when you insert the first document.

📝 In MongoDB:

- A **collection** is like a **table** in SQL.
- A **document** is like a **row** in SQL.

---

```python
print("Connected to MongoDB!")
```

✅ **What this does:**

- Just prints a success message to show everything is working and connected.

---

# Basic CRUD Operations

✅ **Insert a document**

```python
product = {"name": "Laptop", "price": 1200.99}
products.insert_one(product)
```

✅ **Find documents**

```python
for prod in products.find():
    print(prod)
```

✅ **Find with a filter**

```python
laptops = products.find({"name": "Laptop"})
for laptop in laptops:
    print(laptop)
```

✅ **Update a document**

```python
products.update_one({"name": "Laptop"}, {"$set": {"price": 999.99}})
```

✅ **Delete a document**

```python
products.delete_one({"name": "Laptop"})
```

---

# Example Full Script (lab.py)

```python
from pymongo import MongoClient

# Connect
client = MongoClient('mongodb://localhost:27017/')
db = client['labdb']
products = db['products']

# Insert
products.insert_one({"name": "Keyboard", "price": 49.99})

# Find
for prod in products.find():
    print(prod)

# Update
products.update_one({"name": "Keyboard"}, {"$set": {"price": 39.99}})

# Delete
products.delete_one({"name": "Keyboard"})
```

---

- In MongoDB, **everything you store is a document**.
- A document is just a **JSON** (or technically BSON = "Binary JSON").
- In Python, it’s simply a **Python dictionary**.

✅ You insert, query, update, and delete **entire documents** that look like nested JSON.

# How to Insert a Saved JSON File into MongoDB Using Python

---

# Save Your JSON File

Example:

Suppose you have a file called `products.json` in your project folder:

**products.json**:

```json
[
    {
        "name": "Laptop",
        "brand": "Dell",
        "specs": {
            "cpu": "Intel i7",
            "ram": "16GB",
            "storage": "512GB SSD"
        },
        "price": 1200.99,
        "available": true,
        "tags": ["electronics", "computer", "work"],
        "rating": 4.5
    },
    {
        "name": "Smartphone",
        "brand": "Samsung",
        "specs": {
            "cpu": "Snapdragon 888",
            "ram": "8GB",
            "storage": "128GB"
        },
        "price": 899.99,
        "available": true,
        "tags": ["electronics", "mobile"],
        "rating": 4.7
    }
]
```

Notice: it's an **array of objects** → so we will insert **multiple documents**.

---

# Python Code to Load and Insert JSON

```python
from pymongo import MongoClient
import json

MONGODB_URI = "mongodb+srv://doramar5555:cy58wmYeqxNxb7gj@cluster0.ix22vtr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Connect to local MongoDB
client = MongoClient(MONGODB_URI)

# Choose database and collection
db = client['labdb']
products = db['products']

# Load JSON file
with open('products.json') as file:
    data = json.load(file)  # Load JSON as Python list

# Insert into MongoDB
if isinstance(data, list):
    products.insert_many(data)  # Insert multiple documents
else:
    products.insert_one(data)   # Insert single document

print("Data inserted successfully!")
```

What happens:

- Python reads your `products.json` file.
- Loads it into a **Python list** (`data`).
- Inserts all documents into the MongoDB collection.

---

# 🧠 Important Notes:

- If your JSON file is a **list of objects** → use `insert_many`.
- If your JSON file is **one single object** → use `insert_one`.
- You must **make sure the JSON file is valid** (no syntax errors).
- Always **use `json.load()`**, not `json.loads()`, because you load from a **file** not a **string**.