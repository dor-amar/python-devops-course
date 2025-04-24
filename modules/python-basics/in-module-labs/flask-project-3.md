This project involves creating a Flask-based web application that integrates with **Discord** using its API and stores messages in an **SQLite database**.

This task is more challenging than what we’ve done so far — and that’s the point!

It’s designed to push you a bit further. Don’t worry if you get stuck — feel free to use the internet, documentation, or AI tools to help you solve problems along the way.

📝 When you submit your project, please include a file called reflection.md where you:

Describe what the project was about

Explain what you were asked to do

Reflect on the challenges you faced and how you solved them


**Discord Webhook:** 

[https://www.svix.com/resources/guides/how-to-make-webhook-discord/#:~:text=Click the arrow next to,icon and name your webhook](https://www.svix.com/resources/guides/how-to-make-webhook-discord/#:~:text=Click%20the%20arrow%20next%20to,icon%20and%20name%20your%20webhook).

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

https://stackoverflow.com/questions/62731561/discord-send-message-only-from-python-app-to-discord-channel-one-way-communic

### Project Goal:

You’re going to build a small **Flask web app** that allows users to:

- ✍️ Submit a message (via form or JSON)
- 📤 Send that message to a **Discord channel** via **webhook**
- 🗃️ Store that message in a **SQLite3 database**
- 🔁 Retrieve the latest messages from the last 30 minutes
- 🖥️ And... there’s a basic **HTML interface** included!

---

## What You’ll Learn

✅ Flask basics (routes, POST/GET, HTML templates)

✅ How to use SQLite3 in Flask

✅ Send data to Discord using Webhooks

✅ Work with JSON and APIs

✅ Return JSON from your own Flask app

---

## 💡 Project Overview: **"Message Relay"**

A simple Flask web app that:

1. Accepts text messages via a web form.
2. Sends the message to a Discord channel via a Webhook.
3. Saves the message to an SQLite database.
4. Provides an API to retrieve messages from the past 30 minutes.

---

## 🗂️ Project Structure

```
message-relay/
├── app.py
├── templates/
│   └── index.html
├── messages.db        # Auto-created on first run
├── requirements.txt
└── README.md
```

---
📝 Here's a suggested to-do list to guide your development — but you're not limited to it.

Feel free to freestyle and build the app however you like - **there is not a one write answer to solve this project** for example - using .env, adding a ui or other functionalities.


# To-Do List 
## 1️⃣ Setup

- [ ]  Create project folder and virtual environment
- [ ]  Install: `Flask`, `discord-webhook`
- [ ]  Add your Discord Webhook URL to `app.py`

---

## 2️⃣ Build the App

- [ ]  Create `app.py` with a basic Flask setup
- [ ]  Create `/` route to serve an HTML form
- [ ]  Create `/input_text` route to:
    - [ ]  Get message input
    - [ ]  Send it to Discord via webhook
    - [ ]  Save it in SQLite (`messages.db`)

---

## 3️⃣ Database

- [ ]  Create `messages` table: `id`, `content`, `timestamp`
- [ ]  Write a function to save messages
- [ ]  Write a `/get_messages` route to return messages from the last 30 minutes (as JSON)

---

## 4️⃣ Frontend

- [ ]  Create `index.html` with a form to submit messages
- [ ]  Use JavaScript to send the form via fetch and show the response

---

## 5️⃣ Final Steps

- [ ]  Test with cURL and browser
- [ ]  Create `reflection.md` — explain what you built and how you solved issues

### **End Goal**

Build a Flask web app that lets users send messages to a Discord channel **and** stores those messages in a local SQLite database, with an option to view recent ones.

---

### **Project Flow Diagram**

```
[User] ──▶ [Flask Web App]
             │
             ├──▶ [Send to Discord (Webhook)]
             │
             ├──▶ [Save to SQLite Database]
             │
             └──▶ [Return Confirmation + Show Recent Messages]

```

## **Snnipets to help you**
<details><summary>Click here for some hints</summary> 

### ✅ The Database

```python
def get_db_connection():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row
    return conn

```

- This creates a safe, per-request SQLite connection.
- The table `messages` has 3 fields: id, content, and timestamp.

### ✅ Sending to Discord

```python
from discord_webhook import DiscordWebhook

def send_to_discord(text):
    webhook = DiscordWebhook(url=YOUR_DISCORD_WEBHOOK_URL, content=text)
    webhook.execute()

```

⚠️ Replace `YOUR_DISCORD_WEBHOOK_URL` with your own webhook URL.

### ✅ Saving to SQLite

```python
def save_to_database(text):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (content, timestamp) VALUES (?, ?)', (text, datetime.now()))
    conn.commit()
    conn.close()
```
</details>