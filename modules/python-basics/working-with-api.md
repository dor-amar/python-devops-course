# Working with APIs in Python

![image.png](../../images/api3.png)

### **1. Introduction to APIs**

- **What is an API?**
    - API stands for Application Programming Interface. It’s a way for different software applications to communicate with each other.
    - APIs allow you to interact with external services and retrieve or send data.
- **Types of APIs**
    - **REST (Representational State Transfer)**: The most common type, typically uses HTTP requests (GET, POST, PUT, DELETE).
    - **SOAP (Simple Object Access Protocol)**: A protocol for exchanging structured information, less commonly used nowadays.
    - **GraphQL**: A query language for APIs, allows clients to request specific data.

### **2. Making HTTP Requests**

- **HTTP Methods**:
    - **GET**: Retrieve data from an API.
    - **POST**: Send data to an API (e.g., to create a new resource).
    - **PUT**: Update data on an API.
    - **DELETE**: Delete data on an API.
- **Using the `requests` Library**:
    - Python’s `requests` library makes it easy to send HTTP requests.
    
    ```python
    import requests
    ```
    

### **3. Basic GET Request**

- **Making a GET Request**:
    
    ```python
    response = requests.get('https://randomfox.ca/floof')
    print(response.status_code)  # Check the status code (e.g., 200 for success)
    print(response.json())  # Parse the response as JSON
    
    ```
    
- **Handling Query Parameters**:
    
    ```python
    params = {'key1': 'value1', 'key2': 'value2'}
    response = requests.get('https://randomfox.ca/floof', params=params)
    print(response.url)  # See the full URL with parameters
    
    ```
    

## 3. Practical Examples

### **Example 1: Fetching a Random Joke**

You can use the exact code and explanation from the PDF:

```python
import requests

url = 'https://official-joke-api.appspot.com/jokes/random'

response = requests.get(url)
joke = response.json()

print(joke['setup'], joke['punchline'])
```

**Explanation**:

- Walk your students through how this code uses the `requests.get()` method to make a GET request to a joke API and then parses the response using `.json()` to extract and print the joke.

**Output**:

- Example: "Why don't scientists trust atoms? Because they make up everything."

### **Example 3: GitHub API**

Finally, use the GitHub API example to show how to interact with a real-world API that many students may have heard of:

```python
import requests

url = "https://api.github.com/repos/microsoft/vscode/issues"
response = requests.get(url)
issues = response.json()

for issue in issues:
    print(issue['title'])
```

**Explanation**:

- Walk them through how this example fetches issues from the Visual Studio Code repository on GitHub and prints their titles.

### **Example: Checking the Status Code**

```python
import requests

# Define the URL for the API endpoint
url = "https://api.github.com/repos/python/cpython"

# Make a GET request to the API
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    print("Success! The request was successful.")
    data = response.json()
    print(f"Repository: {data['name']}")
    print(f"Description: {data['description']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

```

### **Explanation**:

1. **Import the requests library**: This library allows you to send HTTP requests in Python.
2. **Define the URL**: Here, we're using GitHub's API to get information about the official Python repository.
3. **Make a GET request**: The `requests.get(url)` function sends a GET request to the specified URL.
4. **Check the status code**:
    - If the status code is `200`, it means the request was successful. We then parse the JSON response and print some details about the repository.
    - If the status code is not `200`, we print a message indicating that the request failed and show the actual status code.

### **Running the Example**:

When you run the code, if the request is successful, you’ll see output like:

```
Success! The request was successful.
Repository: cpython
Description: The Python programming language

```

If the request fails for some reason (e.g., the URL is incorrect or the server is down), you’ll see something like:

```
Failed to retrieve data. Status code: 404
```

### **Teaching Points**:

- **Understanding Status Codes**: Emphasize that status codes are essential for understanding how the server responded to your request.
    - `200` means success.
    - `404` means the resource was not found.
    - `500` means there was a server error, etc.
- **Error Handling**: Teach students to always check the status code and handle errors appropriately, instead of assuming that the request was successful.

This simple example provides a clear and practical way to introduce working with status codes in API requests.

### **2. Working with a List of Jokes**

The API also offers an endpoint to retrieve multiple jokes at once. Here’s how to work with a list of jokes.

**Before Structuring the Data**

```python
import requests

# Define the URL for fetching ten jokes
url = "https://official-joke-api.appspot.com/jokes/ten"

# Make a GET request to the API
response = requests.get(url)

jokes = response.json()

print(jokes)
print(len(jokes))
```

**After Structuring the Data**

```python
import requests

# Define the URL for fetching ten jokes
url = "https://official-joke-api.appspot.com/jokes/ten"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    jokes = response.json()
    for joke in jokes:
        print(f"{joke['setup']} - {joke['punchline']}\n")
else:
    print(f"Failed to retrieve jokes. Status code: {response.status_code}")
```

### **1. Basic Error Handling with Status Codes**

We already touched on checking the status code of a response. Let’s expand on this to include different types of status codes and appropriate actions.

```python
import requests

# Define the URL for the random joke endpoint
url = "https://official-joke-api.appspot.com/jokes/random"

try:
    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        joke = response.json()
        print(f"{joke['setup']} - {joke['punchline']}")
    elif response.status_code == 404:
        print("The resource was not found (404).")
    elif response.status_code == 500:
        print("Server error (500). Try again later.")
    else:
        print(f"An unexpected error occurred. Status code: {response.status_code}")
```

# API Exampls

# Preparing Your Python Environment for APIs

To work with an API in Python, we'll need a tool for making requests. The most common library for this purpose is the [**requests** library](https://requests.readthedocs.io/en/latest/). Since `requests` isn't included in the standard Python library, we'll need to install it before we can use it.

If you use `pip` to manage your Python packages, you can install the `requests` library with the following command:

```bash
pip install requests
```

If you're using conda, use this command instead:

```bash
conda install requests
```

Once installed, import the library into your script to start making API requests:

```python
import requests
```

# Making Your First API Request in Python

Now that we’ve set up the `requests` library, let’s make our first API request. We’ll start with a simple GET request and take a closer look at the status codes that come with the server's response.

APIs use different request types, but GET is by far the most common when we just need to retrieve data. Since we’re focusing on pulling information, we’ll stick to GET requests for now.

*A typical API request involves sending a query to the server and receiving a response.*

![](https://www.dataquest.io/wp-content/uploads/2019/09/api-request.svg)

When we make an API request, the response we get back from the server includes a **status code** that tells us if the request was successful or if something went wrong.

Let’s try making a GET request to an API endpoint that doesn’t exist, just to see what an error status code looks like. Here’s how we do it using the [`requests.get()` function](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request):

```python
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)
```

```
404
```

The `404` status code probably looks familiar—it’s what a server returns when it can’t find the resource we’re asking for. In this example, we intentionally requested `this-api-doesnt-exist`, which (as expected) doesn’t exist. This helps us understand what an error response looks like in practice.

# Understanding Common API Status Codes

Every API request to a web server returns a status code indicating the outcome of the request. Here are some common codes relevant to GET requests:

- `200`: Everything went okay, and the result has been returned (if any).
- `301`: The server is redirecting you to a different endpoint. This can happen when a company switches domain names or changes an endpoint name.
- `400`: The server thinks you made a bad request. This happens when you send incorrect data or make other client-side errors.
- `401`: The server thinks you're not authenticated. Many APIs require login credentials, so this happens when the correct credentials are not sent.
- `403`: The resource you're trying to access is forbidden. You don’t have the right permissions to see it.
- `404`: The resource you tried to access wasn’t found on the server.
- `503`: The server is not ready to handle the request.

Status codes starting with `4` indicate client-side errors, while codes beginning with `5` point to server-side issues. The first digit of the status code helps you quickly identify if a request was successful (`2xx`) or if there was an error (`4xx` or `5xx`). [Read more about status codes here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to deepen your understanding.

Now that you understand the basics of API requests and status codes, you're ready to start making your own requests and handling the responses!

In the next section, we'll look at some more practical examples of working with real-world APIs in Python.

# How to Read API Documentation (and Why It Matters)

### Consulting Documentation for Successful API Requests

When working with APIs, especially in the context of AI and data science, reviewing the documentation is essential for making effective requests. Documentation from providers like OpenAI, Google Cloud AI, or IBM Watson outlines how to use their services efficiently.

### Key Elements of API Documentation

Most API documentation includes details on available endpoints, required parameters, authentication methods, and expected response formats. For instance, the OpenAI API documentation provides comprehensive guidance on using their language models, such as GPT-4, for tasks like natural language processing.

### Exploring the Open Notify API

Here, we’ll work with the [Open Notify](http://open-notify.org/) API, which provides data about the International Space Station. This API is ideal for beginners due to its straightforward design and lack of authentication requirements.

### Understanding API Endpoints

APIs often offer multiple endpoints for different types of data. We’ll start with the [http://api.open-notify.org/astros.json](http://open-notify.org/Open-Notify-API/People-In-Space/) endpoint, which returns information about astronauts currently in space. According to the documentation, this API requires no inputs, making it simple to use.

### Making a GET Request to the API

> We are now Using : http://api.open-notify.org/
> 

Let’s make a GET request to this endpoint using the `requests` library:

```python
response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)
```

```
200
```

The `200` status code indicates that our request was successful. The API response is in JSON format. To view the data, we’ll use the [`response.json()` method](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content):

```python
print(response.json())
```

### The Importance of API Documentation

Thoroughly understanding API documentation is key to leveraging the capabilities of APIs for AI and data science. By carefully reviewing the guidelines, you can ensure you’re fully prepared to make the most of these tools.

---

# Working with JSON in Python API Requests

> We are now Using : https://jsonplaceholder.typicode.com/
> 

## Receiving JSON Responses from an API

### Example: GET + `.json()`

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

data = response.json()  # Converts response to Python dict

print(data["title"])
```

📌 `.json()` takes the raw response (string) and parses it into a Python dictionary or list.

## Sending JSON in POST Requests

We are now Using: https://reqres.in/

Most APIs expect `application/json` in the request body for POST/PUT.

### Full Example

```python
import requests

# JSON data we want to send
payload = {
    "name": "Dor",
    "job": "DevOps Engineer"
}

# Sending the POST request with the payload
response = requests.post("https://reqres.in/api/users", json=payload)

# Check status and parse the JSON response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

```

---

### 🧾 Expected Output

```
Status Code: 201
Response JSON: {
    'name': 'Dor',
    'job': 'DevOps Engineer',
    'id': '762',
    'createdAt': '2025-04-06T10:00:00.000Z'
}
```

---

### Notes:

- `201` status means **Created** – the resource was accepted.
- The `id` and `createdAt` fields are automatically added by the API.
- This API is fully public and safe for testing.

---

### Basic GET Request

```python
import requests

response = requests.get("https://reqres.in/api/users/2")
print(response.status_code)  # 200 means success
print(response.json())       # prints the data we got
```

👉 *What it does:*

This sends a simple request to an API and prints out the result. It’s like visiting a webpage and seeing what's there — but in code!

---

### Extracting Specific Data from JSON

```python
import requests

response = requests.get("https://reqres.in/api/users/2")
data = response.json()

print(data['data']['first_name'])  # shows the user's first name
```

👉 *What it does:*

We dig into the JSON response to print just the first name. Think of it like opening a drawer (data), then picking a folder (`'data'`), then reading a field inside it (`'first_name'`).

---

### What Happens When It Fails?

```python
import requests
    # wrap with if based on status code:    
response = requests.get("https://reqres.in/api/unknown/999")  # fake ID -Not exist
if response.status_code == 200:
    print(response.json())             # Will print error message
else:
    print(response.status_code)

```

👉 *What it does:*

Shows what happens when the data isn’t found (404 error). This is how we learn to handle mistakes.

---

### Using Try-Except to Handle Errors

```python
import requests

try:
    response = requests.get("https://reqres.in/api/unknown/999")
    data = response.json()
    print(data)
except Exception as e:
    print("Something went wrong:", e)
```

👉 *What it does:*

Wraps the code in a safe block. If something breaks, Python prints a friendly error instead of crashing.

---

### Loop Through List of Users

```python
import requests

response = requests.get("https://reqres.in/api/users?page=2")
data = response.json()

for user in data['data']:
    print(user['first_name'], user['email'])

# this is a request to the users endpoint with a query parameter page set to 2
# the endpoint is https://reqres.in/api/users
# the query parameter page is used to paginate the results
# the default page size is 6
# so this request will return the second page of users
```

👉 *What it does:*

We loop over a list of users and print names and emails. A very real-world task when working with APIs!

---

# Using an API with Query Parameters

The `http://api.open-notify.org/astros.json` endpoint we used earlier does not require parameters. We simply send a GET request, and the API returns data about the number of people currently in space.

However, many APIs require parameters to customize their behavior. This is especially common in APIs for AI and data science, where query parameters allow us to access specific subsets of data, configure AI models, or refine the results we receive.

### How Query Parameters Work

Query parameters are a way to filter and customize the data returned by an API. For example, you might use a `filter_by` parameter to retrieve data for a specific region or topic. This approach ensures you only receive the information you need, avoiding unnecessary data transfer.

To make this concept more relatable, imagine you're ordering a burger at a restaurant. You might ask for extra cheese, no pickles, and sweet potato fries instead of regular fries. These specific instructions are like query parameters—they customize your order to fit your preferences.

![](https://s3.amazonaws.com/dq-content/889/1.1a-m889.svg)

### Exploring the World Bank's Development Indicators API

We are now Using : https://datatopics.worldbank.org/world-development-indicators/

For this example, we'll use the [World Bank's Development Indicators](https://datatopics.worldbank.org/world-development-indicators/), a database with global development data for over 200 countries. To streamline access, we’ve built a dedicated server (`https://api-server.dataquest.io/economic_data`) that simplifies querying this resource in our examples.

### Using Query Parameters to Filter Data

Optional query parameters let us extract a subset of data from an API instead of retrieving everything. For instance, to filter data for countries in Sub-Saharan Africa, we could use the following URL:

```python
https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa
```

This parameterized request targets only the relevant region. The World Bank API also offers endpoints for additional queries, including `/countries`, `/indicators`, `/country_series`, `/series_time`, and more.

### Making Parameterized API Requests in Python

Here’s an example of making a GET request without query parameters:

```python
import requests

try:
    response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa")
    data = response.json()  
    print(data)
except Exception as e:
    print(e)

```

Here’s a breakdown of the query string:

- `?`: Indicates the start of the query string, separating it from the base URL.
- `filter_by`: Specifies the type of filtering to apply.
- `region`: Defines the field in the database to filter (in this case, the geographical region).
- `=`: Assigns the value to the specified field (`Sub-Saharan Africa`).
- `%20`: Represents a space in the URL, as spaces cannot be included directly.

The `data` variable now holds information about countries in Sub-Saharan Africa. Using query parameters like this allows us to efficiently tailor API requests to meet specific needs.

This code basically:

1. **Sends a request** to a website (an API).
2. The request asks for **economic data about countries** in a specific region — **Sub-Saharan Africa**.
3. It gets the response in **JSON format** (like a dictionary in Python).
4. It then **prints that data**.
5. If anything goes wrong (like connection issues or invalid response), it prints an **error message** instead of crashing.

## Understand the Structure of the Data

First, print and inspect the data:

```python
print(data)
```

Let’s say the data looks like this (simplified):

```python
[
  {"country": "Kenya", "region": "Sub-Saharan Africa", "gdp": 1000, "population": 54000000},
  {"country": "Nigeria", "region": "Sub-Saharan Africa", "gdp": 4500, "population": 200000000},
  ...
]
```

That’s a **list of dictionaries** — one dictionary per country.

---

## Loop Through the Data and Extract Fields

This request give us a long string, we need to parse it and make it a list of dictionaries, this str is in the right syntax, but it is still a string which means we cant iterate or make dict functions. 

```python
import requests
import json

try:
    response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa")
    raw_data = response.json()
    print(type(raw_data))
    if isinstance(raw_data, str):
        data = json.loads(raw_data)
        print(type(data))
        print(type(data[0]))
    else:
        data = raw_data

    for country in data:
        print(country['short_name'], "-", country['income_group'])

except Exception as e:
    print("Error:", e)

# the problem is that the data is not a list of dictionaries, but a string
# the solution is to use the json.loads() function to convert the string to a list of dictionaries
# the json.loads() function is a function that converts a JSON string to a Python object
# the json.loads() function is a function that converts a JSON string to a Python object
# the json.loads() function is a function that converts a JSON string to a Python object

#show me all the keys of a dictionary so i know what to iterate over in a preety way     
print(data[0].keys())  

# iterate on all the countries and see thier income group
for country in data:
    print(country['short_name'], "-", country['income_group']) 
    
#show me all the countries name that have a income group of low income - no list comprehension
lower_middle_income_countries = []
for country in data:
    if country['income_group'] == 'Lower middle income':
        lower_middle_income_countries.append(country['short_name'])
print(lower_middle_income_countries)

#show me all the countries name that have a income group of upper middle income - no list comprehension
upper_middle_income_countries = []
for country in data:
    if country['income_group'] == 'Upper middle income':
        upper_middle_income_countries.append(country['short_name'])
print(upper_middle_income_countries)    

# save lower middle income countries full dictionary to a json file - not only names - also all data
with open('lower_middle_income_countries.json', 'w') as f:
    for country in data:
        if country['income_group'] == 'Lower middle income':
            json.dump(country, f, indent=4) 
```

This script sends a request to an API to get economic data about Sub-Saharan African countries. Sometimes the response is a string instead of a usable Python object, so we check its type. If it’s a string, we convert it into a list of dictionaries using `json.loads()`. Once we have the data, we can loop through it and print specific fields — like the country’s short name and income group. We also print the dictionary keys to see what data is available. Then, we filter countries by their income group (e.g., "Lower middle income" or "Upper middle income") and store their names in a list. Finally, we show how to save the full data (not just names) for the "Lower middle income" countries into a JSON file. This helps students learn how to handle JSON data, explore it, filter it, and store it properly.