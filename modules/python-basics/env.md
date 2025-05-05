# **Using Environment Variables in Python Applications**

---

## **What Are Environment Variables?**

Environment variables are **key-value pairs** stored in the system environment. They are **external to your codebase** and commonly used to:

- Store configuration
- Inject secrets (like API keys)
- Support multiple environments (dev, staging, prod)
- Improve security (no credentials in code)

### Example

```bash
export API_KEY="123abc456"
```

This key is now available to any application or script that runs in the same shell session.

---

## **Why Use Environment Variables?**

### ✅ **Advantages**

- **Security**: Keep secrets out of your code and Git history.
- **Flexibility**: Change settings without modifying code.
- **Portability**: Run the same code in different environments.
- **12-Factor App Compliant**: A best practice for modern app development.

---

## **Accessing Environment Variables in Python**

Python uses the built-in `os` module to access environment variables.

### Basic Usage

```python
import os

api_key = os.getenv("API_KEY")  # Returns None if not found
print("API Key:", api_key)

```

### With Default Fallback

```python
debug_mode = os.getenv("DEBUG", "False")  # Default to False
```

### Error if Missing

```python
database_url = os.environ["DATABASE_URL"]  # Raises KeyError if not found
```

---

## **Real-World Example: Secure Database Connection**

Imagine you have a Python app using Mongo. Instead of this:

```python
DATABASE_URL="mongodb+srv://doramar5555:AQqXIeuYSzDiYrqr@cluster0.ix22vtr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```

You should do this:

### 1. Set the environment variable:

```bash
export DATABASE_URL="mongodb+srv://doramar5555:AQqXIeuYSzDiYrqr@cluster0.ix22vtr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```

### 2. Access it in Python:

```python

from pymongo import MongoClient
import os

DATABASE_URL=os.getenv("DATABASE_URL")

def db_init():
    client = MongoClient(DATABASE_URL)
    db = client.student_bot
    collection = db.knowledge_base
    return collection

print(db_init())
```

---

## **Using `.env` Files with `python-dotenv`**

### Problem:

Environment variables in local development can get annoying.

### Solution: Use a `.env` file to store them.

**`.env`**

```
API_KEY=123abc456
DEBUG=True
```

### nstall the library:

```bash
pip install python-dotenv
```

### Load the variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Automatically reads .env and sets os.environ
print(os.getenv("ENVIRONMENT"))

```

---

## **Keeping `.env` Secure**

⚠️ **Important:** Add `.env` to your `.gitignore` so it's never pushed to GitHub.

**.gitignore**

```
.env
```

---

## **Multi-Environment Setup (Dev/Staging/Prod)**

You can have different `.env` files:

- `.env.development`
- `.env.staging`
- `.env.production`

Then in your script:

```python
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env.development")
```

---

### In your app:

```python
import os
print(os.getenv("API_KEY"))
```

## **Tips and Best Practices**

| Practice | Why |
| --- | --- |
| Use `os.getenv()` with defaults | Prevent crashes on missing vars |
| Keep `.env` in `.gitignore` | Protect secrets |
| Document required variables | Help collaborators |
| Avoid using `.env` in production | Use system-level vars or secret managers |
| Separate configs by environment | Clean and manageable setups |

---

## **Extra Example: Flask App Config**

```python
from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback-secret")

@app.route("/")
def hello():
    return "Secret Key: " + app.config["SECRET_KEY"]

if __name__ == "__main__":
    app.run(debug=True)
```

Use a `.env` like:

```
SECRET_KEY=my-super-secret-key
```

---

## **Bonus: Validating Env Vars**

You can write a utility to validate critical env vars on startup:

```python
required_vars = ["DATABASE_URL", "API_KEY"]
for var in required_vars:
    if not os.getenv(var):
        raise Exception(f"Missing required env var: {var}")
```

---

## References

- Python `os` docs: https://docs.python.org/3/library/os.html#os.getenv
- `python-dotenv`: https://saurabh-kumar.com/python-dotenv
- 12-Factor App: https://12factor.net/config
- GitHub Actions secrets: https://docs.github.com/en/actions/security-guides/encrypted-secrets