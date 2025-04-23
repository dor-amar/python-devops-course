# SQLite Browser

---

## What is SQLite Browser?

**SQLite Browser** (officially called **DB Browser for SQLite**) is a **free GUI tool** that lets you:

- Create `.db` database files
- Create tables and insert data
- Run SQL queries
- Browse data easily (like Excel)

It’s perfect for:

- **Learning SQL**
- **Testing your database schema**
- **Connecting later to Flask apps**

---

## Installing & Using SQLite Browser

### Download

Official site: [https://sqlitebrowser.org](https://sqlitebrowser.org/)

Choose the version for your OS (Windows, macOS, or Linux) and install.

---

### Create a New Database

1. Open SQLite Browser.
2. Click `File → New Database`.
3. Choose a name like `my_first_db.sqlite`.
4. Save it somewhere easy to find.

---

### Create a Table

1. Go to the **"Database Structure"** tab.
2. Click **"Create Table"**.
3. Give it a name: `users`
4. Add fields like:

| Field Name | Type | PK? | Not Null |
| --- | --- | --- | --- |
| id | INTEGER | ✅ | ✅ |
| name | TEXT |  | ✅ |
| email | TEXT |  | ✅ |

✅ Check “Primary Key” and “Not Null” for `id`

Click **OK**.

---

### Insert Data

1. Go to **"Browse Data"** tab
2. Select your `users` table
3. Click **"New Record"** to add rows manually

Or…

---

### Run SQL Commands

1. Go to the **"Execute SQL"** tab
2. Run commands like:

```sql
INSERT INTO users (name, email) VALUES ('Jessica', 'jess@gmail.com');
SELECT * FROM users;
DELETE FROM users WHERE id = 1;
```

Click **"Play ▶️"** to run the query.