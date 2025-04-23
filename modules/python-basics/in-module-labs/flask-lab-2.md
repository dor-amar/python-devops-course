# Build & Test Your Own Flask Task API
## Goal

- Build a Flask API with `GET`, `POST`, and `DELETE` methods.
- Use another Python script to **interact** with the API (create, read, delete tasks).

---

## Build the Flask API

### File: `app.py`

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Add a new task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled"),
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201

# Delete a task by ID
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": f"Task {task_id} deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

```

### Start your server:

```bash
python app.py
```

By default, it runs on `http://127.0.0.1:5000`

---

## Test the API with Python

### `client.py`

```python
import requests

API = "http://127.0.0.1:5000"

# Your Code Here ! 
# Test you app
```

---

## To-Dos:

1. Run `app.py` and keep the server running.
2. Run `client.py` to interact with the API.
3. Modify the client to:
    - Add multiple tasks
    - Try deleting a non-existent task
    - Add a `/complete/<id>` route to mark a task as done

---

## Hints for Extensions:

- Add `PUT` method to update a task’s title or status.
- Add validation (e.g., reject empty titles).
- Save tasks to a file or database instead of memory.

---

## Answers (Expected Outputs)

Example output after running `client.py`:

```bash
Task created: {'id': 1, 'title': 'Learn Flask API', 'done': False}
All tasks: [{'id': 1, 'title': 'Learn Flask API', 'done': False}]
Delete response: {'message': 'Task 1 deleted'}

```