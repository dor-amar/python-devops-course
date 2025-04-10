# **Flask Lab: Building Your First Flask Application**

**Objective:**

- Understand basic routing and HTTP methods in Flask.
- Learn how to use templates to render dynamic HTML content.
- Handle form submissions using POST methods.

---

### **Setting Up Flask**

1. **Install Flask**
    
    Ensure that Flask is installed in your Python environment. Run the following command:
    
2. **Create the Flask Application:**
    - Create a new Python file called `app.py`.
3. **Import Flask and Initialize the App:**
At the top of `app.py`, write the following code:
    
    ```python
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    ```
    
4. **Define a Basic Route:**
Create a route that will render a simple "Hello, World!" message.
5. **Run the Flask Application:**
Add the following code at the bottom of your `app.py` to run the application:
    - This will start the Flask development server on `http://127.0.0.1:5000/`.
    - Navigate to `http://127.0.0.1:5000/` in your browser, and you should see the "Hello, World!" message.

---

### **Working with Templates**

1. **Create a Template Directory:**
Create a new directory called `templates` in your project folder. Flask looks for HTML files in the `templates` folder.
2. **Create a Template File:**
Inside the `templates` directory, create a new file called `index.html`.
3. **Define HTML Content in the Template:**
In `index.html`, write the following HTML:
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Lab</title>
    </head>
    <body>
        <h1>Welcome to Flask!</h1>
        <p>This is a basic template rendering example.</p>
    </body>
    </html>
    ```
    
4. **Render the Template in Flask:**
In your `app.py`, modify the `home` route to render the `index.html` template instead of returning a string.
5. **Run the Application Again:**
Restart the Flask app and visit `http://127.0.0.1:5000/` again. This time, it should render the HTML template.

---

### **Handling Form Submissions (POST Method)**

1. **Add a Form to the Template:**
Update `index.html` to include a simple form that takes a user's name.
    
    ```html
    <form method="POST" action="/greet">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
    ```
    
2. **Create a New Route to Handle the Form:**
In your `app.py`, define a new route that will handle form submissions using the POST method.
    
    ```python
    @app.route('/greet', methods=['POST'])
    def greet():
        name = request.form.get('name')
        return f'Hello, {name}!'
    ```
    
3. **Test the Form Submission:**
    - When you visit `http://127.0.0.1:5000/`, you should see a form.
    - Enter a name and submit the form. You should be greeted with "Hello, [name]!" on a new page.