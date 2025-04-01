# Setting Up Flask with SQLite
### Step 1: Install Flask

**Objective**: Install Flask in your Python environment so that you can start building web applications.

**Instructions**:

1. Open your terminal (Command Prompt, PowerShell, or terminal on Mac/Linux).
2. Run the following command to install Flask:
    
    ```bash
    pip install flask
    ```
    

**Explanation**:

- **pip** is the package installer for Python. It allows you to install packages like Flask, which is a lightweight web framework for building web applications.

### Step 2: Create a Basic Flask Application

**Objective**: Set up a basic Flask application that can respond to HTTP requests.

**Instructions**:

1. Create a new file named `app.py` in your project directory.
2. Add the following code to `app.py`:
    
    ```python
    from flask import Flask
    
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Route to display the homepage
    @app.route('/')
    def home():
        return "Hello, Flask!"
    
    if __name__ == '__main__':
        app.run(debug=True)
    
    ```
    

**Explanation**:

- `from flask import Flask`: This imports the Flask class from the Flask package.
- `app = Flask(__name__)`: This line creates an instance of the Flask class. The `__name__` variable helps Flask determine the root path of the application.
- `@app.route('/')`: This is a route decorator. It maps the URL `/` to the `home` function.
- `def home():`: This function defines the view for the homepage. It returns a simple string "Hello, Flask!".
- `app.run(debug=True)`: This starts the Flask development server. The `debug=True` argument enables debug mode, which provides detailed error messages and auto-reloads the server when you make changes.

### Step 3: Run the Flask Application

**Objective**: Run the Flask application and access it via your web browser.

**Instructions**:

1. In the terminal, navigate to the directory where `app.py` is located.
2. Run the following command:
    
    ```bash
    python app.py
    
    ```
    
3. Open your web browser and go to `http://127.0.0.1:5000/`.

**Explanation**:

- Running `python app.py` starts the Flask server on `localhost` at port `5000`.
- When you visit `http://127.0.0.1:5000/`, Flask responds to the GET request with the message "Hello, Flask!".

### Step 4: Set Up a SQLite Database

**Objective**: Create and initialize a SQLite database that will store user information.

**Instructions**:

1. In `app.py`, add the following code to set up a database connection and initialize the database:
    
    ```python
    import sqlite3
    
    # Function to get a database connection
    def get_db_connection():
        conn = sqlite3.connect('mydatabase.db')
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        return conn
    
    # Function to initialize the database
    def init_db():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    ```
    
2. After defining this code, ensure to call `init_db()` at the beginning of the script to create the database when the app starts:
    
    ```python
    if __name__ == '__main__':
        init_db()
        app.run(debug=True)
    
    ```
    

**Explanation**:

- `sqlite3.connect('mydatabase.db')`: Connects to a SQLite database file named `mydatabase.db`. If the file does not exist, SQLite creates it.
- `conn.row_factory = sqlite3.Row`: This setting allows you to access database rows as dictionaries, making it easier to work with the data by column name.
- `cursor.execute('CREATE TABLE IF NOT EXISTS users...')`: This SQL command creates a table named `users` with three columns: `id`, `name`, and `email`. The `id` is an auto-incremented primary key.

### Step 5: Display User Data

**Objective**: Create a route that fetches and displays user data from the SQLite database.

**Instructions**:

1. Add a route to display the list of users:
    
    ```python
    from flask import render_template
    
    @app.route('/users')
    def users():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        conn.close()
        return render_template('users.html', users=rows)
    
    ```
    
2. Create a folder named `templates` in your project directory.
3. Inside the `templates` folder, create a file named `users.html` and add the following content:
    
    ```html
    htmlCopy code
    <!DOCTYPE html>
    <html>
    <head>
        <title>User List</title>
        
    </head>
    <body>
        <h1>User List</h1>
        <ul>
        {% for user in users %}
            <li>{{ user['name'] }} - {{ user['email'] }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    
    ```
    

**Explanation**:

- `render_template('users.html', users=rows)`: This renders the `users.html` template and passes the list of users to it.
- `users.html`: This is an HTML file that displays the user data. The `{% for user in users %}` loop iterates over the list of users and displays each user's name and email.

### Step 6: Add New Users

**Objective**: Create a route to add new users to the database via an HTML form.

**Instructions**:

1. Add the following route to handle form submissions:
    
    ```python
    @app.route('/add_user', methods=['GET', 'POST'])
    def add_user():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            conn.commit()
            conn.close()
            return redirect('/users')
        return '''
            <form method="post">
                Name: <input type="text" name="name"><br>
                Email: <input type="text" name="email"><br>
                <input type="submit" value="Add User">
            </form>
        '''
    ```
    

**Explanation**:

- This route handles both GET and POST requests. If the request is GET, it displays the form. If it's POST, it processes the form data and inserts it into the database.
- `cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))`: This SQL command inserts the new user into the `users` table.

### Step 7: Test the Application

**Objective**: Run the application and test the functionality.

**Instructions**:

1. Ensure that the Flask app is running (as explained in Step 3).
2. Visit `http://127.0.0.1:5000/users` to see the list of users.
3. Go to `http://127.0.0.1:5000/add_user` to add a new user. After submission, you should be redirected back to the users list.

**Explanation**:

- This final step verifies that the application works as intended. You should be able to view, add, and list users.

### Final Code

```python
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row 
    print("Connected to DB")
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE,
                   email TEXT UNIQUE
                   )
                   ''')
    conn.commit()
    conn.close()
    print("Init DB")

@app.route('/')
def home():
    return "Hello This is my API"

@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return render_template('users.html',users=rows)

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        return redirect('/users')
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Add User">
        </form>
    '''

if __name__ == '__main__':
    # פעולות הכנה להרים את האפליקציה

    get_db_connection() # Check Connection to DB
    init_db() # Create table

    # להתחיל את האפליקציה
    app.run(port=8080, debug=True)

```