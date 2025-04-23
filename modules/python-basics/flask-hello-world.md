# Flask - Hello World

# **Flask Tutorial: Hello World**

Welcome! In this tutorial you will learn how to create your first **Web App** with Python [Flask](http://flask.pocoo.org/).

## **Setup Project**

Python projects live in [virtual environments](https://pythonbasics.org/virtualenv/). Each project lives in a different virtual environment. This prevents package conflicts. *Python packages should not be installed system wide*.

Consider this:

- Project A needs Flask version 0.2
- Project B needs Flask version 0.3
- Project C needs Flask version 0.1

There is no way that system wide package installation would work, as there would be package conflicts.

### **Create Virtual Environment**

Open a terminal (see below how to open one quickly). Then install python3-venv.

On Ubuntu Linux you can run this command:

```
sudo apt-get install python3-venv
```

---

First create a project directory with the command

```
$ mkdir flaskexample
cd flaskexample
```

---

Then you can create a new virtual environment with the command:

```
$ python3 -m venv venv
```

---

### **Activate Virtual Environment**

The virtual environment has been created, but it’s not yet active.

Activate the virtual environment on Linux, use the command:

```
source venv/bin/activate
```

---

## **Install Flask**

The first step is to install Flask. Python comes with a package manager named `pip`. It uses the the official Python package repository named PyPI.

To install a Python package, you need to open a terminal. This varies per operating system.

You can install a Python package with the command:

```
pip install <package-name>

```

---

In this case you want to type the command:

```
pip install flask

```

---

Then verify it’s installed correctly. Type the command

```
(venv) ➜  flaskexample python3
```

---

The output should be:

```
>>> import flask
>>>

```

---

If you see the output below, it means flask is not installed in the virtual enviroment.

```
Python 3.7.3 (default, Aug 20 2019, 17:04:43)
[GCC 8.3.0] on linux
Type"help","copyright","credits" or"license"for more information.
>>> import flask
Traceback (most recent call last):
  File"<stdin>", line 1,in <module>
ModuleNotFoundError: No module named'flask'
>>>

```

---

## **Hello World**

Great! Now that everything is installed you can create your first Flask App.

Use the line below to import Flask in Python.

```
from flaskimport Flask
```

---

Create app, that hosts the application

```
app = Flask(__name__)
```

---

Then you need a *route* that calls a Python function. A route maps what you type in the browser (the url) to a Python function.

```
@app.route('/')
defindex():
```

---

The function should return something to the web browser,

```
return'Web App with Python Flask!'
```

---

Almost done, the server needs to be started. This starts the web app at port 81.

```
app.run(host='0.0.0.0', port=81)
```

---

Enter the url [*http://localhost:81/*](http://localhost:81/) in your web browser.

Code summary:

---
## Navigation

[⬅️ Previous: Flask Introduction](flask-intro.md) | [Next: Flask Route Template Form ➡️](flask-route-template-form.md)
