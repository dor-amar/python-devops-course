## Folder Structure

```
mongo_app/
│
├── .env                # stores sensitive config like connection string
├── main.py             # your Python app
└── requirements.txt    # dependencies
```

---

## Install Required Packages

```bash
pip install pymongo python-dotenv
```

Then save them:

```bash
echo "pymongo\npython-dotenv" > requirements.txt
```

---

## Create `.env` File

**`.env`**

```
MONGO_URI=mongodb://localhost:27017/
# or use Atlas URI:
# MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority
```

> 💡 Never commit this file to GitHub! Add .env to your .gitignore.
> 

---

## Python Code (`main.py`)

```python
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load .env variables
load_dotenv()

# Get the MongoDB URI from environment
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Access database and collection
db = client["test_db"]
collection = db["users"]

# Insert a sample user
collection.insert_one({"name": "Alice", "email": "alice@example.com"})

# Fetch and print all users
print("All users in the collection:")
for user in collection.find():
    print(user)

```

---

## 5️⃣ Add `.env` to `.gitignore`

**`.gitignore`**

```
.env
__pycache__/
venv/
```

---

## Why Use `.env`?

- Keeps **credentials out of your code**
- Easy to change between **local/dev/prod**
- Works with platforms like **Docker**

---

## Output Example

```
All users in the collection:
{'_id': ObjectId('...'), 'name': 'Alice', 'email': 'alice@example.com'}
```