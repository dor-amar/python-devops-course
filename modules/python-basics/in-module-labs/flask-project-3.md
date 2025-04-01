# Flask Project

This project involves creating a Flask-based web application that integrates with **Discord** using its API and stores messages in an **SQLite database**. Let me break it down for clarity and address possible gaps or improvements.

**Discord Webhook:** 

[https://www.svix.com/resources/guides/how-to-make-webhook-discord/#:~:text=Click the arrow next to,icon and name your webhook](https://www.svix.com/resources/guides/how-to-make-webhook-discord/#:~:text=Click%20the%20arrow%20next%20to,icon%20and%20name%20your%20webhook).

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

https://stackoverflow.com/questions/62731561/discord-send-message-only-from-python-app-to-discord-channel-one-way-communic

---

## Key Objectives

1. **Text Submission (POST `/input_text`)**
    - Accept user input as a JSON payload.
    - Send this text to a **Discord server** via a webhook.
    - Store the message in an **SQLite3 database**.
2. **Discord Integration**
    - Utilize the Discord webhook to transmit messages.
3. **Message Retrieval (GET `/get_messages`)**
    - Retrieve messages submitted in the last **30 minutes** from the database.
4. **HTML Frontend**
    - Simple form to submit messages.

---

## Code Review and Explanation

### 1. **Flask Setup and SQLite3 Database**

The initial database setup creates a `messages` table if it does not exist:

```python
conn = sqlite3.connect('messages.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT, timestamp DATETIME)')
conn.commit()
```

**Issues:**

- The database connection `conn` and cursor are created globally, which is not thread-safe. A better practice is to create them within a function or request context.

**Solution:**
Wrap the database interaction in a helper function like this:

```python
def get_db_connection():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row
    return conn
```

---

### 2. **Endpoint 1 - Input Text**

Handles the input text submission.

```python
@app.route('/input_text', methods=['POST'])
def input_text():
    try:
        data = request.get_json()
        text = data['text']

        # Send text to Discord server
        send_to_discord(text)

        # Save text to SQLite database
        save_to_database(text)

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
```

**Potential Improvements:**

- Input validation for `text` should check if it's non-empty and a string.
- Return a proper error response if `data` is invalid.

**Updated Code:**

```python
if not text or not isinstance(text, str):
    return jsonify({"status": "error", "message": "Invalid input"}), 400
```

---

### 3. **Discord Integration**

Uses the `DiscordWebhook` library to send messages.

```python
def send_to_discord(text):
    webhook = DiscordWebhook(url=discord_webhook_url, content=text)
    webhook.execute()
```

**Notes:**

- Make sure to replace `YOUR_DISCORD_WEBHOOK_URL` with a valid Discord webhook URL.
- The library `discord_webhook` must be installed using `pip install discord-webhook`.

---

### 4. **Saving to SQLite Database**

The function to save text includes a timestamp:

```python
def save_to_database(text):
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now()
    cursor.execute('INSERT INTO messages (content, timestamp) VALUES (?, ?)', (text, timestamp))
    conn.commit()
    conn.close()
```

---

### 5. **Endpoint 3 - Message Retrieval**

Retrieves messages from the database within the last 30 minutes.

```python
@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        cutoff_time = datetime.now() - timedelta(minutes=30)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT content, timestamp FROM messages WHERE timestamp > ?', (cutoff_time,))
        messages = cursor.fetchall()
        conn.close()

        # Debugging: print fetched messages
        print("Retrieved messages:", messages)

        return jsonify({"status": "success", "messages": [{"content": row['content'], "timestamp": row['timestamp']} for row in messages]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

```

---

## Final Folder Structure

```bash
flask-discord-project/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # HTML form for text submission
├── messages.db            # SQLite3 database
└── requirements.txt       # Required libraries
```

**requirements.txt**

```makefile
Flask
discord-webhook
```

---

## Running the Application

1. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
2. Run the Flask app:
    
    ```bash
    python app.py
    ```
    
3. Access the endpoints:
    - **Text Submission:** `POST /input_text`
        
        ```json
        {"text": "Hello Discord!"}
        ```
        
    - **Message Retrieval:** `GET /get_messages`
    - **HTML Form:** Visit `http://127.0.0.1:5000/`