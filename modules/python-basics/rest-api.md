# Building a REST API with Flask

## Overview

In this lecture, you'll learn how to create a RESTful API using **Flask**. A REST API lets your backend expose data to clients (web, mobile, CLI) over HTTP using standard request methods like `GET`, `POST`, `PUT`, and `DELETE`.

You’ll also learn:

- How to return proper JSON responses
- How to read query parameters and JSON payloads
- How to simulate a basic data layer using files

---

## What is a REST API?

A REST API is a backend system that responds to HTTP requests using:

- **GET** – Retrieve data
- **POST** – Create or update data
- **PUT** – Add new data
- **DELETE** – Remove data

Flask is a lightweight web framework that allows you to easily build RESTful endpoints using `@app.route()` decorators.

---

## Project 1: Return JSON from Flask

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'name': 'alice',
        'email': 'alice@outlook.com'
    })

app.run(debug=True)
```

### Why `jsonify`?

- `jsonify` automatically sets the correct response **Content-Type** to `application/json`.
- If you return a raw string like `json.dumps(...)`, Flask will treat it as `text/html` by default.

You can confirm this by opening Chrome Dev Tools → Network → Headers.

---

## How to Handle Different HTTP Methods

You can define which HTTP method a route handles using:

```python
@app.route('/endpoint', methods=['GET', 'POST', 'PUT', 'DELETE'])

```

By default, all routes handle **GET** only unless you specify otherwise.

---

## Project 2: Basic CRUD API Using a JSON File

We'll use a file (`/tmp/data.txt`) to store our data as a JSON list of records.

Each record will look like:

```json
{ "name": "alice", "email": "alice@example.com" }
```

---

### `GET` – Query a record by name

```python
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

```

**URL Example:**

```
GET http://localhost:5000/?name=alice
```

---

### `PUT` – Create a new record

```python

@app.route('/', methods=['PUT'])
def create_record():
    record = request.get_json()
    try:
        with open('/tmp/data.txt', 'r') as f:
            data = f.read()
            records = json.loads(data) if data else []
    except FileNotFoundError:
        records = []

    records.append(record)

    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))

    return jsonify(record)

```

---

### `POST` – Update an existing record

```python
@app.route('/', methods=['POST'])
def update_record():
    record = request.get_json()
    updated = False
    with open('/tmp/data.txt', 'r') as f:
        records = json.loads(f.read())

    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
            updated = True

    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))

    return jsonify(record if updated else {'error': 'record not found'})

```

---

### `DELETE` – Delete a record by name

```python
@app.route('/', methods=['DELETE'])
def delete_record():
    record = request.get_json()
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        records = json.loads(f.read())

    for r in records:
        if r['name'] != record['name']:
            new_records.append(r)

    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))

    return jsonify({'message': 'record deleted'})

```

---

## Bonus Tips

✅ **Use `request.get_json()`** instead of `json.loads(request.data)` — it's cleaner and safer

✅ Always validate user input (this example skips it for simplicity)

✅ Don’t use file storage in production — use a database like SQLite or PostgreSQL

✅ Use [Postman](https://www.postman.com/) or `curl` to test these endpoints

---

## 🌐 Hosting

To put this API online:

- Use [PythonAnywhere](https://www.pythonanywhere.com/) for quick deployment
- Or try [Render](https://render.com/), [Fly.io](https://fly.io/), or [Railway](https://railway.app/)

---

## 🧪 Practice Tasks for Students

1. Add a `GET /all` endpoint that returns all records
2. Add basic error handling for:
    - Missing `email`
    - Invalid JSON
3. Implement `PATCH` to only update part of a record (e.g., change email without touching name)
4. Add an `id` field instead of using `name` for identification