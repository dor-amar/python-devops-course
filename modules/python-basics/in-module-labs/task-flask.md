# Build a Task Manager App

Build a simple **Task Manager App** where users can:

- View all tasks
- Add a new task
- Mark a task as completed

**Skills practiced:**

- Flask routes (GET and POST)
- Forms in HTML
- SQLite3 basic operations (CREATE, INSERT, UPDATE, SELECT)

---

# 📝 Project Structure:

```
task_manager/
├── app.py
├── templates/
│   ├── index.html
│   └── add_task.html
└── tasks.db
```

---

# Set up the Database

Create a database `tasks.db` with a `tasks` table

**Table fields:**

- `id` → unique task ID (Primary Key)
- `title` → short task title
- `description` → optional details
- `completed` → 0 (not done) / 1 (done)

---

# Build the Flask Application

### app.py

```python
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Init DB
def init_db():
   # Connect to your db here 
# Connect to the database
def get_db_connection():
   # Connect to your db here 

# Route: Home - List all tasks
@app.route('/')
def index():
   # Show all tasks - Hint - fetchall()

# Route: Add new task
@app.route('/add', methods=('GET', 'POST'))
def add():
   # Add a new task, write to the DB

# Route: Mark task as completed
@app.route('/complete/<int:id>')
def complete(id):
   # Update the specific task if done or not

if __name__ == '__main__':
    app.run(debug=True)

```

---

# HTML Templates

### templates/index.html

```html
<!doctype html>
<html>
<head>
    <title>Task Manager</title>
</head>
<body>
    <h1>Task Manager</h1>
    <a href="/add">➕ Add New Task</a>
    <ul>
        {% for task in tasks %}
            <li>
                {% if task.completed %}
                    ✅ <s>{{ task.title }}</s> - {{ task.description }}
                {% else %}
                    {{ task.title }} - {{ task.description }}
                    <a href="/complete/{{ task.id }}">[Mark as Completed]</a>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

### templates/add_task.html

```html
<!doctype html>
<html>
<head>
    <title>Add Task</title>
</head>
<body>
    <h1>Add a New Task</h1>
    <form method="post">
        <label>Title:</label><br>
        <input type="text" name="title" required><br><br>

        <label>Description:</label><br>
        <textarea name="description" rows="4" cols="50"></textarea><br><br>

        <button type="submit">Add Task</button>
    </form>
    <br>
    <a href="/">🔙 Back to Task List</a>
</body>
</html>
```

---

# Bonus Challenges

- Allow deleting tasks (`DELETE FROM tasks WHERE id = ?`)
- Separate tasks into "Completed" and "Pending" sections
- Add a "Clear all completed tasks" button
- Add a task due date
- Style the app nicely using basic CSS

---