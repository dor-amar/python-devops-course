
# Lecture Goals

- Understand **what environment variables are** and **why** we use them.
- Learn **where** to store environment variables safely.
- Use a **`.env` file** in a Flask app.
- **Read** variables using `python-dotenv`.
- **Connect** to a SQLite/PostgreSQL database using a connection string from `.env`.

---

# What Are Environment Variables?

✅ Environment variables are **key-value pairs** stored **outside your code**.

✅ They are used to:

- Store **sensitive information** (passwords, database URLs, API keys).
- Store **configurations** that might change (like debug mode, port number).

✅ Why?

- **Security**: Don't hardcode secrets into the codebase.
- **Flexibility**: You can change settings without changing code.
- **Best Practice**: Used in **production**, **development**, **CI/CD pipelines**, **Docker**, **cloud servers**.

---

# Where Do We Store Them?

There are two common places:

| Environment | Where stored? | Example |
| --- | --- | --- |
| Local | `.env` file in project root | `.env` |
| Production | Set directly on the server/cloud | AWS Secrets Manager, etc. |

---

# How Does a `.env` File Look?

Example `.env` file:

```
FLASK_ENV=development
DATABASE_URL=sqlite:///tasks.db
SECRET_KEY=mysecretkey
```

⚡ **Important rules:**

- Always name it `.env`
- Never upload `.env` to GitHub (add it to `.gitignore`!)

---

# How to Load `.env` in Flask

Install the `python-dotenv` library:

```bash
pip install python-dotenv
```

Inside your `app.py`:

```python
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

print("Database URL is:", os.getenv('DATABASE_URL'))
```

---

# Read and Print an Env Variable

1. `.env`:

```
MY_NAME=Dor
```

1. `app.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

print("Hello,", os.getenv('MY_NAME'))

```

**Output:**

```bash
Hello, Dor
```

---

# Database Connection String Example

Imagine your `.env` has:

```
DATABASE_URL=sqlite:///tasks.db
```

**OR for PostgreSQL:**

```
DATABASE_URL=postgresql://user:password@host:port/database
```

---

## How to Use the Connection String in Flask?

Example (`app.py`):

```python
import sqlite3
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
DB_PATH = os.getenv('DATABASE_URL')
print("DB will be created/accessed at:", DB_PATH)

def init_db():
    # This will create the DB and the tasks table if they don't exist
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        );
    ''')
    # Optional: Add one sample task
    count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    if count == 0:
        conn.execute("INSERT INTO tasks (title) VALUES ('Sample Task')")
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return {'tasks': [dict(row) for row in tasks]}

if __name__ == '__main__':
    init_db()  # ✅ Automatically creates the file and table
    app.run(debug=True)

```

---

# Best Practices

✅ Always use environment variables for anything sensitive.

✅ Always **load** them at the **top** of your app.

✅ Always **add `.env` to `.gitignore`**:

```bash
# .gitignore
.env
```

✅ In production (AWS, Heroku, Docker), set the variables directly in environment settings.

---

# Summary Slide

| Concept | Example |
| --- | --- |
| Sensitive Data Storage | `DATABASE_URL`, `SECRET_KEY` |
| File to Use Locally | `.env` |
| Python Library to Load | `python-dotenv` |
| How to Access in Code | `os.getenv('VARIABLE_NAME')` |