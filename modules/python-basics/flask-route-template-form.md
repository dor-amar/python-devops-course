# Flask Routing, Templates, and Forms

**Goal:** Build real pages, handle user input, understand how forms work

---

## Warm-Up: Quick Flask Setup

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

# Routing

Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit a page.

Use the [**`route()`**](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route) decorator to bind a function to a URL.

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

You can do more! You can make parts of the URL dynamic and attach multiple rules to a function.

### `@app.route('/')`

- This **decorator** tells Flask:
    
    > "When someone goes to the homepage (/), run the index() function."
    > 
- `/` is the **root URL** → like `http://localhost:5000/`

- **What is a Decorator in Python?**
    
    A **decorator** is a **function that wraps another function** to modify its behavior — without changing the original function's code.
    
    It’s like putting a **filter or addon** on a function.
    
    ## Basic Structure:
    
    ```python
    def my_decorator(func):
        def wrapper():
            print("Before the function runs")
            func()
            print("After the function runs")
        return wrapper
    ```
    
    Then you apply it like this:
    
    ```python
    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()
    ```
    
    ### What happens under the hood?
    
    ```python
    say_hello = my_decorator(say_hello)
    ```
    
    So now, when you run `say_hello()`, it actually runs the `wrapper()` inside `my_decorator`.
    

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

# Variable Rules

You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a **converter** to specify the type of the argument like `<converter:variable_name>`.

- `escape()` is used to **protect your app from code injection**.

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

Converter types:

| `string` | (default) accepts any text without a slash |
| --- | --- |
| `int` | accepts positive integers |
| `float` | accepts positive floating point values |
| `path` | like `string` but also accepts slashes |
| `uuid` | accepts UUID strings |

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

## HTTP Methods

Web applications use different HTTP methods when accessing URLs. You should familiarize yourself with the HTTP methods as you work with Flask. By default, a route only answers to `GET` requests. You can use the `methods` argument of the [**`route()`**](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.route) decorator to handle different HTTP methods.

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

The example above keeps all methods for the route within one function, which can be useful if each part uses some common data.

You can also separate views for different methods into different functions. Flask provides a shortcut for decorating such routes with [**`get()`**](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.get), [**`post()`**](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.post), etc. for each common HTTP method.

```python
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
```

If `GET` is present, Flask automatically adds support for the `HEAD` method and handles `HEAD` requests according to the [HTTP RFC](https://www.ietf.org/rfc/rfc2068.txt). Likewise, `OPTIONS` is automatically implemented for you.

---

## Query Strings

A **query string** is the part **after the `?` in a URL**.

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
- It **looks like a Python dictionary**
- But you **can’t modify it**
- You use `.get()`, `.keys()`, `.values()` just like a dict

---

### Rendering Templates

Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the [Jinja2](https://palletsprojects.com/p/jinja/) template engine for you automatically.

Templates can be used to generate any type of text file. For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, and anything else.

For a reference to HTML, CSS, and other web APIs, use the [MDN Web Docs](https://developer.mozilla.org/).

To render a template you can use the [**`render_template()`**](https://flask.palletsprojects.com/en/stable/api/#flask.render_template) method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:

Folder structure:

```
/flask/
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
from flask import Flask, request, render_template

# Step 1: Create the app
app = Flask(__name__)

# Step 2: Route to display the form
@app.route("/form")
def show_form():
    return render_template("form.html")

# Step 3: Route to handle the form submission
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("username", "Guest")
    return render_template("greet.html", name=name)

# Step 4: Run the app
if __name__ == "__main__":
    app.run(debug=True)
```

Create `templates/greet.html`:

```html
<h1>Hello, {{ name }}!</h1>
```

---

## HTML Forms + Flask

### HTML (templates/form.html)

```html
<form method="POST" action="/submit">
  <input type="text" name="username" placeholder="Enter your name" />
  <input type="submit" value="Submit" />
</form>
```

- `method="POST"` → means we are **sending** data.
- `action="/submit"` → the form will send the data to the `/submit` route.

---

## Flask Backend

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return f"Hello, {username}!"
```

---

## `request.form` vs `request.args`

| Source | Use | Access With | Example |
| --- | --- | --- | --- |
| `POST` form | Data from form submission | `request.form['field']` | login form |
| `GET` query | Data in URL | `request.args['field']` | search?q=flask |

```python
# GET example
@app.route("/search")
def search():
    term = request.args.get("q")  # /search?q=hello
    return f"You searched for: {term}"
```

---

## POST vs GET (Key Differences)

| Feature | GET | POST |
| --- | --- | --- |
| Data in URL? | ✅ Yes (visible) | ❌ No (hidden) |
| Use for | Searching, filtering | Submitting forms (login, register) |
| Secure? | Less secure | More secure |

---

## Redirecting Users

Instead of returning a response directly, we can **redirect** them to another route.

```python
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def form():
    return '''
        <form method="POST" action="/submit">
            <input type="text" name="username" placeholder="Enter your name" />
            <input type="submit" value="Submit" />
        </form>
    '''

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return redirect(url_for("greet", name=username))

@app.route("/greet/<name>")
def greet(name):
    return f"Welcome, {name}!"

if __name__ == "__main__":
    app.run(debug=True)

```

---

## Flash Messages (show feedback)

### Enable session usage:

```python
from flask import Flask, flash, get_flashed_messages, session
app.secret_key = 'mysecret'
```

### Flash in route:

```python
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    flash(f"User {username} has been registered!")
    return redirect(url_for("index"))

```

### Show message in template:

```html
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for msg in messages %}
      <p>{{ msg }}</p>
    {% endfor %}
  {% endif %}
{% endwith %}
```

---

## Real-World Use Cases

- **Login forms** → POST data to backend
- **Search bars** → GET query parameters
- **Form validation** → Show flash errors
- **Redirects after success** → Avoid re-submitting on refresh