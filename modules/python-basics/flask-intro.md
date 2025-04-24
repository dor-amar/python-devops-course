# Flask Introduction

![image.png](/images/flask.png)
[What is Flask ?](https://pythonbasics.org/what-is-flask-python/)
[Flask Docs](https://flask.palletsprojects.com/en/stable/)
### Introduction to Flask in Python

**Objective**: By the end of this lecture, students should understand the basics of Flask, how to set up a simple web server, and create basic routes to handle different URLs.

---

### **What is Flask?**

- **Flask** is a lightweight web framework written in Python. It’s designed to be simple and easy to use, making it a popular choice for beginners and developers who want to build web applications quickly.
- **Key Features**:
    - **Lightweight**: Flask doesn’t include a lot of built-in features by default, allowing you to add only what you need.
    - **Modular**: You can easily extend Flask with various libraries and extensions to add features like database support, form handling, authentication, etc.
    - **Flexible**: Flask gives you the freedom to structure your code however you like, making it ideal for small to medium-sized projects.

---

### **Setting Up Flask**

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

## 🧠 Remember ?

```python
if __name__ == "__main__":
    app.run(debug=True)
```

This tells Python:

> “Only run the Flask server if this file is being run directly, not imported.”
> 

---
[⬅️ Previous: Abstraction & Encapsulation](abstraction-encapsulation.md) | [Next: Flask - Hello World ➡️](flask-hello-world.md)
