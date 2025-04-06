# Working with API Headers, Authorization Tokens, and Parameters

We are going to use - https://jsonplaceholder.typicode.com/ for our examples, it is a Free fake and reliable API.

### What Are Headers?

In API communication, **headers** are key-value pairs that provide metadata about the request or response like content type, authorization, and caching instructions, enabling the server to process the data and the client to interpret it correctly. 

- What kind of data you accept (`Accept`)
- What format you’re sending (`Content-Type`)
- Who you are (`User-Agent`, `Authorization`)

API headers are a crucial part of HTTP requests and responses, acting as a way to convey additional information beyond the actual data being transferred.

**Purpose:**

They provide metadata that helps the server understand the request and how to respond, and also allows the client to understand the response and how to handle it.

- **Examples of common headers:**
    - **Content-Type:** Specifies the format of the data being sent or received (e.g., `application/json`, `application/xml`).
    - **Authorization:** Contains authentication credentials, like API keys or tokens.
    - **Accept:** Indicates the format of the response the client is willing to receive.
    - **Cache-Control:** Provides instructions about caching behavior.
    - **User-Agent:** Identifies the client application making the request.

**Key-value pairs:**Headers are structured as key-value pairs, where the key is the header name (e.g., `Content-Type`) and the value is the associated information (e.g., `application/json`).

**Request vs. Response Headers:**

- **Request Headers:** Sent by the client to the server, providing information about the request.
- **Response Headers:** Sent by the server to the client, providing information about the response.

### Example:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "MyApp/1.0"
}

response = requests.get(url, headers=headers)
print(response.status_code)
```

---

## **Authorization and API Tokens**

### What Is an API Token?

API tokens are unique identifiers used for authentication and authorization, while authorization determines whether a user or application has permission to access specific resources after authentication

### How API Tokens Work

Here's what happens when a token is used:

1. A user or application trying to connect with the API provides the token to the API server to authenticate their identity and access.
2. The server reviews the token. If the token is valid, the API server grants the requested level of access. If the token is invalid or does not grant the necessary level of access, the API server rejects the request.

When using API tokens, the API provider can adjust or revoke access at any time. API tokens can even have built-in expiration dates, so they can't be reused forever.

Many APIs require an **authorization token** to prove your identity. This is often done via an `Authorization` header.

### Example (Bearer Token):

```python
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
response = requests.get("https://api.example.com/data", headers=headers)
```

### Common Auth Methods:

| Method | Header Example |
| --- | --- |
| Bearer Token | `Authorization: Bearer <token>` |
| Basic Auth | `Authorization: Basic <base64 user:pass>` |
| API Key | `Authorization: Apikey <key>` OR in params |

---

### 1. NASA Open APIs

NASA offers a collection of APIs providing access to various space and earth science data. [NASA Open APIs](https://api.nasa.gov/?utm_source=chatgpt.com)

**How to Get Started:**

- **Register:** Visit [api.nasa.gov](https://api.nasa.gov/) to sign up for a free API key.[NASA Open APIs](https://api.nasa.gov/?utm_source=chatgpt.com)
- **Explore APIs:** Browse the available APIs, such as Astronomy Picture of the Day (APOD) or Mars Rover Photos.
- **Example Request:**

```python
  import requests

  api_key = 'YOUR_NASA_API_KEY'
  url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

  response = requests.get(url)
  data = response.json()

  print(data['title'])
  print(data['url'])
```

### Astronomy Picture of the Day (APOD)

This API provides daily images or photographs of space along with descriptions. For instance, you can retrieve the APOD for a specific date:[Wikipedia+1Wikipédia, l'encyclopédie libre+1](https://en.wikipedia.org/wiki/Web_API?utm_source=chatgpt.com)

```python
import requests

api_key = 'YOUR_NASA_API_KEY'
date = '2025-03-06'  # Example date
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}'

response = requests.get(url)
data = response.json()

print(data['title'])
print(data['url'])
```

---

### News API

**Overview:** News API provides access to news articles from various sources worldwide. [News API](https://newsapi.org/register?utm_source=chatgpt.com)

**How to Get Started:**

- **Register:** Go to [newsapi.org/register](https://newsapi.org/register) to create a free account and obtain an API key.[News API](https://newsapi.org/register?utm_source=chatgpt.com)
- **Explore Endpoints:** Access top headlines, search for articles, or retrieve news sources.
- **Example Request:**

```python
import requests

api_key = 'YOUR_NEWS_API_KEY'
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

response = requests.get(url)
articles = response.json()['articles']

for article in articles[:5]:
    print(article['title'])

```

---

### Finnhub Stock API

**Overview:** Finnhub offers free APIs for real-time stock market data, company fundamentals, and economic information. [Finnhub+1API Ninjas+1](https://finnhub.io/register?utm_source=chatgpt.com)

**How to Get Started:**

- **Register:** Sign up at [finnhub.io/register](https://finnhub.io/register) to get your free API key.[Finnhub](https://finnhub.io/register?utm_source=chatgpt.com)
- **Explore Endpoints:** Access stock quotes, company news, and financial statements.
- **Example Request:**

```python
import requests

api_key = 'YOUR_FINNHUB_API_KEY'
url = f'https://finnhub.io/api/v1/quote?symbol=AAPL&token={api_key}'

response = requests.get(url)
quote = response.json()

print(f"Apple Stock Price: {quote['c']}")
```

---

**Tips for Working with APIs:**

- **Read the Documentation:** Each API has its own set of rules, endpoints, and rate limits. Familiarize yourself with the documentation to understand how to authenticate and make requests properly.
- **Secure Your API Key:** Never expose your API key in public repositories or share it openly. Treat it like a password.
- **Handle Errors Gracefully:** Implement error handling in your code to manage issues like network errors or exceeding rate limits.

---

### Bearer tokens are

**a secure method for authenticating and authorizing API requests, acting as a digital credential that grants access to protected resources when included in the Authorization header of an HTTP request**

.

**Here's a more detailed explanation:**

- **What they are:**Bearer tokens are strings of characters, often generated by a server after successful authentication, that represent a user or application's identity and permissions.
- **How they work:**
    - The client (e.g., a mobile app or web application) requests access to an API resource.
    - The server authenticates the client and, if successful, issues a bearer token.
    - The client stores the token securely and includes it in the `Authorization` header of subsequent requests to the API.
    - The server verifies the token and grants access to the requested resources if it's valid.
- **Security:**
    - Bearer tokens are more secure than API keys because they can be revoked and have expiration times.
    - They are typically transmitted over HTTPS to prevent eavesdropping.
- **Common usage:**
    - **OAuth 2.0:** Bearer tokens are a core part of the OAuth 2.0 protocol, used for delegated authorization and secure API access.
    - **JSON Web Tokens (JWT):** JWTs are a type of bearer token that can contain claims about the user or application, enabling more granular authorization.
- **Example:**
    - `Authorization: Bearer <token_value>`
    - Where `<token_value>` is the actual bearer token string.
- **Implementation:**
    - Developers need to implement the logic for obtaining and managing bearer tokens, as well as integrating them into their API requests.
    - Many frameworks and libraries provide tools for working with bearer tokens, simplifying the process.

### Log in and get a Bearer token

```python
import requests

# Send login credentials
login_url = "https://reqres.in/api/login"
payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

login_response = requests.post(login_url, json=payload)

# Get the token
if login_response.status_code == 200:
    token = login_response.json().get("token")
    print("Got token:", token)
else:
    print("Login failed:", login_response.text)
```

---

### Use the token in a Bearer header

Now that you have a token, you can use it to make another request (simulated auth in this case):

```python
# Use the token as a Bearer token
headers = {
    "Authorization": f"Bearer {token}"
}

# Let's try to access a protected resource (simulated)
user_url = "https://reqres.in/api/users/2"
response = requests.get(user_url, headers=headers)

print(response.status_code)
print(response.json())
```

---

### Explanation

- `Authorization: Bearer <token>`  this is how most modern APIs expect you to send access tokens.
- `requests.get(..., headers=headers)` this adds the token to your request.
- This simulates the same flow you’d follow with APIs like GitHub, Stripe, Twitter, or NASA.

---

## What is a JWT Token?

A **JWT (JSON Web Token)** is a compact and secure way to transmit information between two parties usually the **client (you)** and the **server** that can be **verified and trusted**.

It's mostly used for **authentication**.

### **The Benefits of using JWT:**

JWTs contain JSON objects that are encoded and signed, ensuring integrity and authenticity without relying on stateful sessions on the server.

Some of the key benefits that make JWTs useful are:

- Compact size from URL-safe JSON encoding for space efficiency
- Self-contained with all necessary user information to avoid excessive database queries
- Digital signatures for tamper-proof security and authenticity verification
- Stateless nature to improve scalability by removing server-side sessions
- Universal interoperability with JSON parsers available in most languages
- Extensible via custom data fields without breaking existing frameworks

### **How Does JWT Work?**

JSON Web Tokens (JWTs) play a key role in authentication by providing a secure and efficient way to verify the identity of users. The process typically involves the following steps:

1. **User Authentication:** Users sign in using their username and password or through external providers like Google or Facebook. The authentication server validates the credentials and issues a JSON Web Token (JWT) certifying the user's identity.
2. **JWT Generation:** The identity provider (IdP) generates a JWT, signing it with either a secret salt or a private key. This JWT encapsulates essential user information, such as user ID, roles, and expiration time.
3. **JWT Usage:** The user's client securely stores the JWT obtained during authentication. When accessing protected resources, the client includes the JWT in the HTTP Authorization header.
4. **Token Verification:** The resource server decodes and verifies the authenticity of the JWT using the provided secret salt or public key. This process ensures the integrity and origin of the token.

### DummyJSON

DummyJSON provides a free fake REST API with JWT authentication endpoints, allowing you to practice login and token-based authentication.[DummyJSON+1Reddit+1](https://dummyjson.com/docs/auth?utm_source=chatgpt.com)

<aside>
<img src="notion://custom_emoji/8d9f99b4-0243-4f6a-ad70-ee35c09a9f83/1bc60591-38ae-808a-9be5-007a551fc05e" alt="notion://custom_emoji/8d9f99b4-0243-4f6a-ad70-ee35c09a9f83/1bc60591-38ae-808a-9be5-007a551fc05e" width="40px" />

You can use any user's credentials from [dummyjson.com/users](https://dummyjson.com/users). Tokens are returned in the response and set as cookies.

</aside>

### Using JWT with DummyJSON API

```python
import requests

# Login to get JWT token
login_url = "https://dummyjson.com/auth/login"
credentials = {
    "username": "emilys",  # test account provided by DummyJSON
    "password": "emilyspass"
}

response = requests.post(login_url, json=credentials)

if response.status_code == 200:
    auth_data = response.json()
    print("Response JSON:", response.json())  # <— this will help debug
    token = auth_data['accessToken']
    print("✅ Logged in successfully.")
    print("JWT Token:", token)

    # Use the token to access protected route
    protected_url = "https://dummyjson.com/auth/users"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    protected_response = requests.get(protected_url, headers=headers)

    if protected_response.status_code == 200:
        users = protected_response.json()
        print("✅ Accessed protected data:")
        for user in users['users'][:5]:  # print only the first 5 users
            print(f"- {user['firstName']} {user['lastName']}")
    else:
        print(" Failed to access protected route.")
else:
    print("Login failed:", response.status_code, response.text)

```