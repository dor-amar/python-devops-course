# Add a Search Feature to the Flask API
## Goal

You’ll build your own Flask-based API to manage tasks, and then use another Python script to send API calls to it.

Finally, you’ll extend the API yourself by implementing a **search feature**.

---

## 🗂️ Project Structure

```
/task_api_project/
├── api.py            # Your Flask API server
└── client.py         # A Python script that talks to the API
```

---

## Part 1: Starter Code (Given)

### 🔧 `api.py` (Flask API)

You already have:

- `GET /tasks` → Get all tasks
- `POST /tasks` → Add a new task
- `/` → Welcome route

Tasks are stored in an in-memory Python list (`tasks = []`).

---

### 🔧 `client.py` (You will build or receive this)

Will send requests to your Flask server using the `requests` library.

---

## Part 2: Your Task – Add a Search Feature

### Objective

Add a new **search endpoint** to your Flask API that supports this:

```
GET /tasks/search?keyword=something
```

### Requirements

1. Add a new route in `api.py`:
    
    ```python
    @app.route("/tasks/search")
    def search_tasks():
        ...
    ```
    
2. Extract the `keyword` from the query string (use `request.args.get()`)
3. Filter all tasks where `keyword` is in the title (case-insensitive)
4. Return the filtered list as JSON

---

### 🧪 Example

### Tasks list:

```json
[
  { "id": 1, "title": "Learn Flask" },
  { "id": 2, "title": "Buy groceries" },
  { "id": 3, "title": "Learn Python" }
]
```

### URL:

```
GET /tasks/search?keyword=learn
```

### Should return:

```json
[
  { "id": 1, "title": "Learn Flask" },
  { "id": 3, "title": "Learn Python" }
]

```

---

## Bonus Challenge (Optional)

Update `client.py` so the user can:

- Add a task
- View all tasks
- Search tasks by keyword

Use `input()` to ask the user what they want to do.

---

## How to Run

Install Flask:

```bash
pip install flask

```

Run the server:

```bash
python3 api.py

```

In another terminal, run the client:

```bash
python client.py
```

---

## Submission

- Completed `api.py` with the search route implemented
- Optional: `client.py` with CLI interface