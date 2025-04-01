# Lab: API

## **Lab: Mastering API Integration with Python**

### Objectives

- Understand the fundamentals of RESTful APIs.
- Perform GET and POST requests using Python's `requests` library.
- Process and store JSON responses.

---

## Part 1: Introduction to APIs and HTTP Requests

Use - https://jsonplaceholder.typicode.com/

### Task: Simple GET

**Goal:** Send a `GET` request to `/posts` and print the title of the first 5 posts.

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

for post in posts[:5]:
    print(f"Post {post['id']}: {post['title']}")
```

**Now You:** 

### Task: Fetch One Post by ID

**Goal:**

Ask the user to enter a post ID. Fetch the post from the API and print the post’s title and body.

**API Endpoint:**

```
https://jsonplaceholder.typicode.com/posts/{id}
```

### Task: Jokes API

Learn the basics of APIs and how to make HTTP requests using Python.

**Steps:**

1. **Understand APIs:** Read about what APIs are and how they function.[Python Tutorials – Real Python](https://realpython.com/python-api/?utm_source=chatgpt.com)
2. **Install Requests Library:** Ensure you have the `requests` library installed:
    
    ```bash
    pip install requests
    ```
    

3. **Make a Simple GET Request:** Use the `requests` library to fetch data from a public API.

**Example: Fetching a Random Joke**

```python
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
if response.status_code == 200:
    joke = response.json()
    print(f"{joke['setup']} - {joke['punchline']}")
else:
    print("Failed to retrieve a joke.")
```

**Expected Output:**

```
Why don't scientists trust atoms? - Because they make up everything.
```

### Task: Create a New Post (POST)

**Goal:** Send a `POST` request to create a fake post.

```python
data = {
    "title": "My New Post",
    "body": "Learning APIs with Python is fun!",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

if response.status_code == 201:
    new_post = response.json()
    print(f"Post created with ID: {new_post['id']}")
else:
    print("Error creating post.")
```

- What is response.json() does ?

---

## Get Comments for a Post

**Goal:**

Ask the user for a post ID. Fetch and display all comments related to that post.

**API Endpoint:**

```
https://jsonplaceholder.typicode.com/posts/{id}/comments
```

---

## List All Users and Their Emails

**Goal:**

Make a request to the `/users` endpoint. Print out the name and email address of each user.

**API Endpoint:**

```
https://jsonplaceholder.typicode.com/users
```

---

## Filter Posts by User

**Goal:**

Ask the user to enter a user ID. Then, fetch and display all post titles written by that user.

**API Endpoint with query parameter:**

```
https://jsonplaceholder.typicode.com/posts?userId={userId}

```

## Error Handling

### Goal:

Make a request to a post ID from JSONPlaceholder. If the post doesn't exist (e.g., ID 0 or 9999), catch the error and print a message like "Post not found."

### Instructions:

1. Ask the user to input a post ID.
2. Make a `GET` request to `/posts/{id}`.
3. Check if the response status code is 200.
4. If not, print a user-friendly error message.

### Solution:

```python
import requests

post_id = input("Enter a post ID: ")
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    print(f"Title: {post['title']}\nBody: {post['body']}")
else:
    print("Post not found. Please try a valid post ID.")
```

---

## Error Handling

### Goal:

Try to fetch comments from the `/comments` endpoint with a post ID. Implement proper error handling:

- If the response fails or takes too long, print an error message.
- Use `try-except` to catch exceptions like timeouts or connection errors.

### Instructions:

1. Ask the user to enter a post ID.
2. Send a GET request to `/posts/{id}/comments`.
3. Use `try` and `except` to:
    - Catch `requests.exceptions.Timeout`
    - Catch `requests.exceptions.ConnectionError`
4. Print the number of comments if successful.
5. Print a helpful message if an error occurs.