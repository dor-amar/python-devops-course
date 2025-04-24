# Flask Routing, Templates, and Forms Lab

## Objective
Build a simple Flask web application that demonstrates routing, templates, and form handling. You'll create a user registration system that:
1. Shows a welcome page
2. Has a registration form
3. Displays a success page after registration
4. Uses templates for consistent styling

## Requirements
- Python 3.8+
- Flask
- Basic understanding of HTML

## Setup
1. Create a new directory for your project:
```bash
mkdir flask-lab
cd flask-lab
```

2. Set up a virtual environment and install Flask:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask
```

## Project Structure
Create the following structure:
```
flask-lab/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   └── success.html
└── static/
    └── style.css
```

## Tasks

### 1. Create Base Template (base.html)
Create a base template that other templates will extend. It should include:
- A navigation bar with links to Home and Register
- A consistent layout
- A block for content

### 2. Create Home Page (index.html)
- Extend the base template
- Show a welcome message
- Include a link to the registration page

### 3. Create Registration Form (register.html)
- Extend the base template
- Create a form with fields for:
  - Username
  - Email
  - Password
  - Confirm Password
- Add basic validation (all fields required, passwords must match)

### 4. Create Success Page (success.html)
- Extend the base template
- Show a success message with the registered username
- Include a link to return home

### 5. Implement Flask Routes (app.py)
Create routes for:
- Home page ('/')
- Registration page ('/register')
- Form submission ('/register', methods=['POST'])
- Success page ('/success/<username>')

### 6. Add Basic Styling (style.css)
- Style the navigation bar
- Style the forms
- Add some basic colors and spacing

## Hints
1. Use `url_for()` for generating URLs in templates
2. Use `request.form` to access form data
3. Use `redirect()` and `url_for()` for redirecting after form submission
4. Use `flash()` messages for form validation feedback

## Bonus Tasks
1. Add form validation with error messages
2. Add a login form and route
3. Store user data in a simple dictionary (for now)
4. Add a user profile page
5. Style the application with Bootstrap

## Submission
Submit your completed project with:
1. All Python files
2. All template files
3. CSS file
4. A brief README explaining how to run the application

## Example Code Structure

### app.py
```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Temporary storage for users
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Basic validation
        if not all([username, email, password, confirm_password]):
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))
            
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))
            
        # Store user (in memory for now)
        users[username] = {
            'email': email,
            'password': password
        }
        
        return redirect(url_for('success', username=username))
        
    return render_template('register.html')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
```

### templates/base.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %} - Flask Lab</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Home</a>
        <a href="{{ url_for('register') }}">Register</a>
    </nav>
    
    <div class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### templates/register.html
```html
{% extends "base.html" %}

{% block title %}Register{% endblock %}

{% block content %}
    <h1>Register</h1>
    <form method="POST" action="{{ url_for('register') }}">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div>
            <label for="confirm_password">Confirm Password:</label>
            <input type="password" id="confirm_password" name="confirm_password" required>
        </div>
        <button type="submit">Register</button>
    </form>
{% endblock %}
```

## Evaluation Criteria
1. Correct implementation of routes and templates
2. Proper form handling and validation
3. Clean and organized code structure
4. Basic styling and user interface
5. Error handling and user feedback
6. Code comments and documentation

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [HTML Forms Guide](https://developer.mozilla.org/en-US/docs/Learn/Forms) 