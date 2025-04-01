# Flask Introduction

![image.png](/images/flask.png)
[What is Flask ?](https://pythonbasics.org/what-is-flask-python/)
### Introduction to Flask in Python

**Objective**: By the end of this lecture, students should understand the basics of Flask, how to set up a simple web server, and create basic routes to handle different URLs.

---

### 1. **What is Flask?**

- **Flask** is a lightweight web framework written in Python. It’s designed to be simple and easy to use, making it a popular choice for beginners and developers who want to build web applications quickly.
- **Key Features**:
    - **Lightweight**: Flask doesn’t include a lot of built-in features by default, allowing you to add only what you need.
    - **Modular**: You can easily extend Flask with various libraries and extensions to add features like database support, form handling, authentication, etc.
    - **Flexible**: Flask gives you the freedom to structure your code however you like, making it ideal for small to medium-sized projects.

---

### 2. **Setting Up Flask**

- **Installation**:
Before we start, you need to install Flask. You can do this using pip:
    
    ```
    pip install flask
    ```
    
- **Creating Your First Flask App**:
Let’s create a very basic Flask application.
    1. **Create a new Python file** (e.g., `app.py`).
    2. **Write the following code**:
    
    ```python
    from flask import Flask
    
    # Create a Flask application object
    app = Flask(__name__)
    
    # Define a route for the root URL "/"
    @app.route('/')
    def home():
        return "Hello, Flask!"
    
    # Run the application
    if __name__ == '__main__':
        app.run(debug=True)
    
    ```
    
    - **Explanation**:
        - **`from flask import Flask`**: Imports the Flask class from the Flask package.
        - **`app = Flask(__name__)`**: Creates a new instance of the Flask class, which will be our WSGI application.
        - **`@app.route('/')`**: This is a route decorator. It tells Flask that the following function should be run when someone accesses the root URL (`/`).
        - **`def home():`**: The function that will be run when the root URL is accessed. It returns a simple string that will be displayed in the browser.
        - **`app.run(debug=True)`**: Starts the Flask web server. The `debug=True` argument allows Flask to automatically reload the server when you make changes to your code and gives you detailed error messages.
- **Running the Application**:
    1. Save the file as `app.py`.
    2. Open your terminal and navigate to the directory where `app.py` is located.
    3. Run the following command:
        
        ```
        python app.py
        
        ```
        
    4. You should see output similar to this:
        
        ```csharp
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        ```
        
    5. Open your web browser and go to `http://127.0.0.1:5000/`. You should see `Hello, Flask!` displayed.

---

### 3. **Understanding Routes and Views**

- **What is a Route?**:
    - A route in Flask is a URL pattern that the application recognizes and responds to. Each route is associated with a specific function (called a view function) that is executed when the route is accessed.
- **Creating More Routes**:
Let’s add more routes to our Flask app:
    
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return "Hello, Flask!"
    
    @app.route('/about')
    def about():
        return "This is the About page."
    
    @app.route('/contact')
    def contact():
        return "This is the Contact page."
    
    if __name__ == '__main__':
        app.run(debug=True)
    ```
    
    - **Explanation**:
        - **`@app.route('/about')`**: This route handles requests to the `/about` URL.
        - **`@app.route('/contact')`**: This route handles requests to the `/contact` URL.
        - Now, when you navigate to `http://127.0.0.1:5000/about` or `http://127.0.0.1:5000/contact`, the corresponding messages will be displayed.

---

### 4. **Returning HTML from Routes**

- **Returning Simple HTML**:
Instead of just returning plain text, you can return HTML content from your routes:
    
    ```python
    @app.route('/')
    def home():
        return "<h1>Welcome to My Flask App</h1><p>This is the home page.</p>"
    
    @app.route('/about')
    def about():
        return "<h1>About Us</h1><p>This is the about page.</p>"
    
    ```
    
    - **Explanation**:
        - The `return` statements now include HTML tags like `<h1>` and `<p>`, which will be rendered by the browser.
- **Using Templates**:
For more complex HTML, it's better to use templates (stored in separate HTML files). Flask automatically looks for templates in a folder called `templates`.
    
    **Example**:
    
    1. **Create a `templates` directory** in the same directory as `app.py`.
    2. **Create an `index.html` file** inside the `templates` directory:
        
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Welcome to My Flask App</h1>
            <p>This is the home page.</p>
        </body>
        </html>
        ```
        
    3. **Modify `app.py` to use the template**:
        
        ```python
        from flask import Flask, render_template
        
        app = Flask(__name__)
        
        @app.route('/')
        def home():
            return render_template('index.html')
        
        if __name__ == '__main__':
            app.run(debug=True)
        ```
        
    - **Explanation**:
        - **`render_template('index.html')`**: This tells Flask to render the `index.html` template when the `/` route is accessed.
        - Flask will look in the `templates` folder for a file named `index.html` and return its content.

---

### 5. **Flask Debug Mode**

- **What is Debug Mode?**
    - Running the Flask app with `debug=True` enables Flask’s built-in debugger and auto-reloading.
    - The debugger provides detailed error messages and tracebacks if something goes wrong.
    - Auto-reloading means the server automatically restarts when you make changes to your code, so you don’t need to stop and restart it manually.
- **Security Note**:
    - Debug mode should never be used in production because it can expose sensitive information. It's meant for development only.

---

### 6. **Recap and Next Steps**

- **Recap**:
    - We introduced Flask and set up a basic web server.
    - We created routes to handle different URLs.
    - We learned how to return both plain text and HTML from routes.
    - We briefly touched on using templates to manage HTML more effectively.