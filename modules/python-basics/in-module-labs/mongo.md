# LAB: Insert Provided JSON File into MongoDB and Perform Queries
---

# Lab Goal

You will:

- **Load** a provided JSON file (`users.json`).
- **Insert** the data into a MongoDB `users` collection.
- **Search** and **filter** the users based on given queries.

---

# Files Provided

**users.json:**

```json
[
    {
        "username": "dor",
        "email": "dor@example.com",
        "age": 27,
        "skills": ["python", "devops", "mongodb"]
    },
    {
        "username": "jessie",
        "email": "jessie@example.com",
        "age": 26,
        "skills": ["html", "css", "javascript", "design"]
    },
    {
        "username": "eilon",
        "email": "eilon@example.com",
        "age": 29,
        "skills": ["aws", "terraform", "python"]
    },
    {
        "username": "yonatan",
        "email": "yonatan@example.com",
        "age": 31,
        "skills": ["java", "spring", "docker"]
    }
]

```

✅ 4 users, with nested lists inside (`skills`).

---

# Instructions

---

## Setup

1. Save the provided `users.json` file in your project folder.
2. Make sure your Python environment has:
    - `pymongo`
    - `python-dotenv`
    - `json`
    installed.

```bash
pip install pymongo python-dotenv
```

---

## Step 2: Write a Python Script

Create a script `insert_users.py` that:

- **Connects** to your MongoDB Atlas cluster.
- **Loads** the `users.json` file.
- **Inserts** the users into a MongoDB collection called `users` inside a database called `labdb`.

💡 **Hints for them:**

- Use `open()` and `json.load()` to read the file.
- Use `insert_many()` if the data is a list.
- Use `.env` to keep the MongoDB connection string **safe**.

---

## Perform the Following Queries

After inserting the users:

✅ 1. **Find and print all users who have "python" in their skills.**

✅ 2. **Find and print all users who are older than 27 years old.**

✅ 3. **Find and print the user whose username is "jessie".**

✅ 4. **Update "dor"’s email address to `dor@newdomain.com`.**

✅ 5. **Delete the user whose username is "yonatan".**

---

# Lab Checklist

| Task | Complete? |
| --- | --- |
| Load JSON file from disk |  |
| Insert data into MongoDB |  |
| Find users by skill |  |
| Find users by age |  |
| Find user by username |  |
| Update user email |  |
| Delete a user |  |