#Flask Routing, Templates, and Forms

**Goal:** Build real pages, handle user input, understand how forms work

---

## 🔧 Warm-Up: Quick Flask Setup (Recap)

Create a folder:

```bash
mkdir flask-routing-lecture
cd flask-routing-lecture
```

Set up a virtualenv (💡pro tip: always isolate your Python projects):

```bash
python3 -m venv venv
source venv/bin/activate 
pip install flask
```

Create `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
```

Run it:

```bash
flask run
```

> Use FLASK_ENV=development to auto-reload and show better errors:
> 

```bash
export FLASK_ENV=development  # or set FLASK_DEBUG=1 on Windows
```

---

## Multiple Routes

Add a few more pages:

```python
@app.route("/about")
def about():
    return "This is the About page."

@app.route("/contact")
def contact():
    return "Contact us at contact@example.com"
```

Run the app and visit:

- http://127.0.0.1:5000/about
- http://127.0.0.1:5000/contact

---

## URL Parameters

Use dynamic URLs with `<variable>` in your route.

```python
@app.route("/user/<username>")
def greet_user(username):
    return f"Hello, {username}!"
```

Visit:

```
http://127.0.0.1:5000/user/Dor
```

> 💡 You can also specify types:
> 

```python
@app.route("/order/<int:order_id>")
def show_order(order_id):
    return f"Order #{order_id}"

```

---

## Query Strings

Go to:

```
http://127.0.0.1:5000/search?term=flask

```

Handle it in a route:

```python
from flask import request

@app.route("/search")
def search():
    term = request.args.get("term", "nothing")
    return f"You searched for: {term}"
```

> request.args is like a dict. But it’s immutable. You can't change it.
> 

---

## HTML Templates with Jinja2

Folder structure:

```
/flask-routing-lecture/
│
├── app.py
└── templates/
    ├── home.html
    ├── about.html
    └── greet.html

```

Create `templates/home.html`:

```html
<!DOCTYPE html>
<html>
  <head><title>Home</title></head>
  <body>
    <h1>Welcome to the Homepage!</h1>
    <a href="/about">Go to About</a>
  </body>
</html>
```

Update `app.py`:

```python
from flask import render_template

@app.route("/home")
def home_page():
    return render_template("home.html")
```

---

## Jinja2 Mini-Guide (Used in Templates)

```html
<!-- Insert variable -->
<p>Hello, {{ name }}!</p>

<!-- If condition -->
{% if logged_in %}
  <p>Welcome back!</p>
{% else %}
  <p>Please log in.</p>
{% endif %}

<!-- Loop -->
<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

> 🥚 Easter Egg #3: Jinja2 autoescapes by default — protects you from XSS.
> 
> 
> But you can manually mark something as safe: `{{ html_code | safe }}`
> 

---

## Forms + POST Methods

Create a form page: `templates/form.html`

```html
<form method="POST" action="/greet">
  <label>Your Name:</label>
  <input type="text" name="username">
  <button type="submit">Submit</button>
</form>
```

Update `app.py`:

```python
from flask import request

@app.route("/form")
def show_form():
    return render_template("form.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("username", "Guest")
    return render_template("greet.html", name=name)

```

Create `templates/greet.html`:

```html
<h1>Hello, {{ name }}!</h1>
```

---
## Navigation

[⬅️ Previous: Flask - Hello World](flask-hello-world.md) | [Next: Database + SQL ➡️](db-sql.md)
