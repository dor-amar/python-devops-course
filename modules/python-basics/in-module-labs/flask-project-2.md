# **Flask + SQLite To-Do App with NGINX**

> Building our first app !
> 

---

## What You’ll Build

A simple but real To-Do app that lets users:

- ✅ Add tasks (title + optional due date)
- 🕐 Mark as done/undone
- 🗑️ Delete tasks
- 🔍 Filter tasks
- 🗄️ Store everything in an SQLite3 database
- 🌐 Deploy with NGINX as a reverse proxy (bonus)

---

## Project Structure

```bash
doitnow/
├── app.py                 ← Flask app
├── todo.db                ← SQLite3 database
├── templates/
│   ├── layout.html        ← Page layout
│   └── index.html         ← To-do list page
├── static/
│   └── style.css          ← Optional styling
├── requirements.txt
└── nginx/
    └── default.conf       ← Reverse proxy config (Week 2)
```

---

## Build the App (Flask + SQLite3)

- [ ]  Create a new virtual environment
- [ ]  Install Flask (`pip install flask`)
- [ ]  Initialize an SQLite DB named `todo.db`

SQL schema:

```sql
CREATE TABLE tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  due_date TEXT,
  is_done INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

📌 **Hint**: Use `sqlite3 todo.db` from terminal to test your schema.

---

### Flask Routes

- [ ]  `/` – Show all tasks
- [ ]  `/add` – Form to add new task
- [ ]  `/complete/<id>` – Mark task as done
- [ ]  `/delete/<id>` – Delete task

📌 **Tip**: Use `request.form.get()` to collect form input

📌 **Security Tip**: Always validate form input

---

## HTML Templates

📄 These are **starter files** provided in the `/templates/` folder.

### `layout.html`

```html
<!doctype html>
<html>
  <head>
    <title>To-Do</title>
  </head>
  <body>
    <h1>📝 Your To-Do App</h1>
    {% block content %}{% endblock %}
  </body>
</html>
```

---

### 📂 `index.html`

```html
{% extends 'layout.html' %}

{% block content %}
<form method="POST" action="/add">
  <input type="text" name="title" placeholder="Task title">
  <input type="date" name="due_date">
  <button type="submit">Add</button>
</form>

<ul>
  {% for task in tasks %}
    <li>
      {% if task[3] == 1 %}<s>{% endif %}
      {{ task[1] }} - due: {{ task[2] }}
      {% if task[3] == 1 %}</s>{% endif %}
      [<a href="/complete/{{ task[0] }}">✓</a>]
      [<a href="/delete/{{ task[0] }}">x</a>]
    </li>
  {% endfor %}
</ul>
{% endblock %}

```

---

- Use the templates above as-is (they work!)
- You can **generate HTML with AI** — just ask ChatGPT
    
    *“Generate an HTML form to add a task with a title and due date”*
    

---

## Deploy with NGINX

- [ ]  Install NGINX locally (or use a Linux VM)
- [ ]  Reverse proxy `localhost:80` → `localhost:5000`

Sample `nginx/default.conf`:

```
# Add your nginx configuration here
```

---

## 🧪 BONUS CHALLENGES

- [ ]  Add filtering: `/completed`, `/pending`
- [ ]  Add a "pin" or "priority" field
- [ ]  Add an "edit task" route + form
- [ ]  Add confirmation messages (using `flask.flash`)
- [ ]  Style it with Bootstrap (CDN)

---

## Submission Guidelines

You must submit:

- ✅ `app.py` with working routes
- ✅ Templates in `templates/`
- ✅ Screenshots or GitHub repo
- ✅ NGINX config