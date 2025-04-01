This project involves creating a Flask-based web application that integrates with **Discord** using its API and stores messages in an **SQLite database**.

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

## Setup Instructions

### Set up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate 
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### `requirements.txt` should include:

```
Flask
discord-webhook
```

> If you're missing the file, run this to generate it:
> 

```bash
pip freeze > requirements.txt
```

---

### Configure Discord Webhook

Edit `app.py` and set your actual Discord webhook:

```python
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/....'
```

---

### Run the Application

```bash
python app.py
```

Visit http://localhost:5000

---

## `index.html` (Example Template)

Place this file inside the `templates/` folder:

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Message Relay</title>
</head>
<body>
    <h1>Send a Message to Discord</h1>
    <form id="messageForm">
        <input type="text" name="text" placeholder="Your message" required>
        <button type="submit">Send</button>
    </form>
    <div id="response"></div>

    <script>
        document.getElementById('messageForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const response = await fetch('/input_text', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            document.getElementById('response').innerText = result.message;
        });
    </script>
</body>
</html>

```

---

## Test the Endpoints

### 1. `/input_text` – Submit a Message

```bash
curl -X POST -F "text=Hello from cURL!" http://localhost:5000/input_text
```

### 2. `/get_messages` – View Recent Messages

```bash
curl http://localhost:5000/get_messages
```

## **Snnipets to help you**

> You can use some examples we did in the class
> 

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
python
CopyEdit
def save_to_database(text):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (content, timestamp) VALUES (?, ?)', (text, datetime.now()))
    conn.commit()
    conn.close()

```