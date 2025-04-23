# SQLite3

https://www.sqlite.org/

https://docs.python.org/3/library/sqlite3.html

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/8d9f99b4-0243-4f6a-ad70-ee35c09a9f83/693e38d6-d84f-44a7-a257-f18ed4599089/image.png)

### What is SQLite3?

**SQLite3** is a lightweight, self-contained, serverless, and highly reliable database engine that is built into Python. Unlike other database management systems (e.g., MySQL, PostgreSQL), SQLite does not require a separate server process. Instead, it stores data in a simple file on disk, making it ideal for small-scale applications, testing, and development.

### When to Use SQLite3:

- Prototyping and development.
- Small-scale applications.
- Testing before deploying to a larger database system.
- Applications where a lightweight and simple database solution is sufficient (e.g., mobile apps, desktop software).

### What is SQLite3?

**SQLite3** is a lightweight, self-contained, serverless, and highly reliable database engine that is built into Python. Unlike other database management systems (e.g., MySQL, PostgreSQL), SQLite does not require a separate server process. Instead, it stores data in a simple file on disk, making it ideal for small-scale applications, testing, and development.

---

### Key Features of SQLite3:

1. **Serverless**:
    - No need for a server to manage the database. It works directly with the file system.
2. **Lightweight**:
    - The entire database is stored in a single file, and the library itself is very small.
3. **Zero Configuration**:
    - No setup or configuration is needed. You can start using it right away.
4. **Portable**:
    - Since the database is stored in a single file, it can be easily shared and moved between systems.
5. **Built-in with Python**:
    - SQLite3 comes bundled with Python's standard library, so you don’t need to install any additional packages to use it.

---

### When to Use SQLite3:

- Prototyping and development.
- Small-scale applications.
- Testing before deploying to a larger database system.
- Applications where a lightweight and simple database solution is sufficient (e.g., mobile apps, desktop software).

---

### Basic SQLite3 Operations in Python:

Here's a step-by-step guide to using SQLite3 with Python:

### 1. **Connect to a Database**

If the database file does not exist, it will be created automatically.

```python
import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("example.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

```

---

### 2. **Create a Table**

Define a table structure.

```python
# SQL command to create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

```

---

### 3. **Insert Data**

Add records to the table.

```python
# Insert a single record
cursor.execute("""
INSERT INTO Users (name, age, email)
VALUES ('Alice', 25, 'alice@example.com')
""")

# Insert multiple records
users = [
    ('Bob', 30, 'bob@example.com'),
    ('Charlie', 35, 'charlie@example.com')
]
cursor.executemany("""
INSERT INTO Users (name, age, email)
VALUES (?, ?, ?)
""", users)

# Commit changes to save them
connection.commit()

```

---

### 4. **Retrieve Data**

Query and fetch records from the table.

```python
# Fetch all records
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fetch specific records
cursor.execute("SELECT name, email FROM Users WHERE age > 30")
rows = cursor.fetchall()
for row in rows:
    print(row)

```

---

### 5. **Update Data**

Modify existing records.

```python
# Update a user's age
cursor.execute("""
UPDATE Users
SET age = 28
WHERE name = 'Alice'
""")
connection.commit()

```

---

### 6. **Delete Data**

Remove records from the table.

```python
# Delete a user
cursor.execute("""
DELETE FROM Users
WHERE name = 'Bob'
""")
connection.commit()

```

---

### 7. **Close the Connection**

Always close the database connection when done.

```python
connection.close()

```

---

### Full Example:

```python
import sqlite3

# Connect to the database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

# Insert data
users = [
    ('Alice', 25, 'alice@example.com'),
    ('Bob', 30, 'bob@example.com'),
    ('Charlie', 35, 'charlie@example.com')
]
cursor.executemany("INSERT INTO Users (name, age, email) VALUES (?, ?, ?)", users)

# Retrieve and print data
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()

```

---

### Benefits of SQLite3:

- Easy to use.
- No need for external dependencies or setup.
- Perfect for small-scale projects or when starting with database programming.

### **What is a Cursor?**

- In SQLite3, a cursor is an object that allows you to interact with the database. It acts as a pointer to the database connection and is used to execute SQL commands and fetch results.
- The cursor is created by calling the `cursor()` method on a database connection object.

### **Executing SQL Commands**

**Executing SQL Queries:**

- The `execute()` method is used to run SQL commands. It can be used for various operations like creating tables, inserting data, updating records, and more.

### **Committing Changes**

**Why Commit is Important:**

- After making changes to the database, such as inserting, updating, or deleting data, those changes are not saved until you commit them.
- The `commit()` method is called on the connection object to save all changes made since the last commit.

**Fetching Query Results:**

- After executing a SELECT query, you can use methods like `fetchall()`, `fetchone()`, or `fetchmany()` to retrieve the results.

### **SQLite3 Class**

### **1. Introduction to SQLite3**

- Explain what SQLite is: a self-contained, serverless, and zero-configuration database engine.
- Highlight its use cases, especially in small to medium-sized applications and as a development database.

### **2. Setting Up SQLite3**

- SQLite3 comes bundled with Python, so no installation is required.
- Import the `sqlite3` module:
    
    ```python
    import sqlite3
    ```
    

### **3. Connecting to a Database**

- Explain how to connect to an SQLite database:
    
    ```python
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    ```
    
    - If the database `example.db` doesn’t exist, SQLite will create it.

### **4. Creating a Table**

- Demonstrate how to create a table using SQL commands in Python:
    
    ```python
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    ```
    
    - `CREATE TABLE IF NOT EXISTS`: Ensures that the table is only created if it doesn’t already exist.
    - `PRIMARY KEY AUTOINCREMENT`: Automatically assigns a unique ID to each record.

### **5. Inserting Data**

- Show how to insert data into the table:
    
    ```python
    pythonCopy code
    cursor.execute('''
    INSERT INTO users (username, email)
    VALUES ('JohnDoe', 'johndoe@example.com')
    ''')
    ```
    
    - Use placeholders for data to prevent SQL injection attacks:
        
        ```python
        pythonCopy code
        cursor.execute('''
        INSERT INTO users (username, email)
        VALUES (?, ?)
        ''', ('JaneDoe', 'janedoe@example.com'))
        ```
        
    - Commit the transaction to save changes:
        
        ```python
        conn.commit()
        ```
        

### **6. Querying Data**

- Demonstrate how to retrieve data from the database:
    
    ```python
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    ```
    
    - `fetchall()`: Retrieves all rows from the result set.
    - Explain other methods like `fetchone()` and `fetchmany()`.

### **7. Updating Data**

- Show how to update existing records:
    
    ```python
    cursor.execute('''
    UPDATE users
    SET email = ?
    WHERE username = ?
    ''', ('john.newemail@example.com', 'JohnDoe'))
    
    ```
    
    - Explain the importance of the `WHERE` clause to target specific records.

### **8. Deleting Data**

- Demonstrate how to delete records:
    
    ```python
    cursor.execute('''
    DELETE FROM users WHERE username = ?
    ''', ('JaneDoe',))
    ```
    
    - Again, emphasize the `WHERE` clause to prevent deleting all records.

### **9. Closing the Connection**

- Explain why it’s important to close the database connection when done:
    
    ```python
    conn.close()
    ```
    

### **Full Example Code**

Here is the complete example code that you can use for the class:

```python
import sqlite3

# 1. Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 2. Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# 3. Insert data into the table
cursor.execute('''
INSERT INTO users (username, email)
VALUES (?, ?)
''', ('JohnDoe', 'johndoe@example.com'))

cursor.execute('''
INSERT INTO users (username, email)
VALUES (?, ?)
''', ('JaneDoe', 'janedoe@example.com'))

# 4. Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print('All Users:')
for row in rows:
    print(row)

# 5. Update data
cursor.execute('''
UPDATE users
SET email = ?
WHERE username = ?
''', ('john.newemail@example.com', 'JohnDoe'))
conn.commit()

# 6. Query data again to see the update
cursor.execute('SELECT * FROM users WHERE username = ?', ('JohnDoe',))
row = cursor.fetchone()
print('\nUpdated User:')
print(row)

# 7. Delete data
cursor.execute('''
DELETE FROM users WHERE username = ?
''', ('JaneDoe',))
conn.commit()

# 8. Query data again to see the deletion
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print('\nRemaining Users:')
for row in rows:
    print(row)

# 9. Close the connection
conn.close()

```

### **Contact Management System**

**Scenario:** Imagine you’re building a small contact management system where users can add, update, view, and delete contacts.

**Database Structure:**

- Table: `contacts`
    - `id`: Integer (Primary Key)
    - `name`: Text
    - `phone`: Text
    - `email`: Text
    - `address`: Text

**Example Code:**

```python
import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create the contacts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)
''')

# Insert a new contact
cursor.execute('''
INSERT INTO contacts (name, phone, email, address)
VALUES (?, ?, ?, ?)
''', ('Dor amar', '123-456-7890', 'dor@example.com', '123 Maple Street'))

# Query all contacts
cursor.execute('SELECT * FROM contacts')
contacts = cursor.fetchall()

print('Contact List:')
for contact in contacts:
    print(contact)

# Update a contact's phone number
cursor.execute('''
UPDATE contacts
SET phone = ?
WHERE name = ?
''', ('987-654-3210', 'Alice Smith'))
conn.commit()

# Delete a contact
cursor.execute('''
DELETE FROM contacts WHERE name = ?
''', ('Alice Smith',))
conn.commit()

# View remaining contacts
cursor.execute('SELECT * FROM contacts')
contacts = cursor.fetchall()
print('Updated Contact List:')
for contact in contacts:
    print(contact)

# Close the connection
conn.close()

```

### **To-Do List Application**

**Scenario:** A simple to-do list app where users can add tasks, mark them as completed, or delete them once finished.

**Database Structure:**

- Table: `tasks`
    - `id`: Integer (Primary Key)
    - `task`: Text
    - `status`: Text (e.g., "Pending", "Completed")

**Example Code:**

```python
import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create the tasks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT NOT NULL
)
''')

# Insert a new task
cursor.execute('''
INSERT INTO tasks (task, status)
VALUES (?, ?)
''', ('Buy groceries', 'Pending'))

# Mark a task as completed
cursor.execute('''
UPDATE tasks
SET status = ?
WHERE task = ?
''', ('Completed', 'Buy groceries'))
conn.commit()

# Query all tasks
cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()

print('To-Do List:')
for task in tasks:
    print(task)

# Delete a completed task
cursor.execute('''
DELETE FROM tasks WHERE status = ?
''', ('Completed',))
conn.commit()

# View remaining tasks
cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()
print('Remaining Tasks:')
for task in tasks:
    print(task)

# Close the connection
conn.close()

```

---
## Navigation

[⬅️ Previous: Database + SQL](db-sql.md) | [Next: Setting Up Flask with SQLite ➡️](flask-sqlite3.md)
