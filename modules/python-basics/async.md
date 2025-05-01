# Async Programming 

---

## **Objective**

By the end of this lecture, you  will:

- Understand the difference between synchronous and asynchronous code
- Be able to use `async/await`, `asyncio`, and `aiohttp`
- Build scalable, non-blocking Python programs
- Apply async code to real DevOps tasks such as monitoring, API polling, and log collection

---

## **What Is Asynchronous Programming?**

### Definition:

Asynchronous programming allows you to **run multiple tasks concurrently** without waiting for one to finish before starting another.

> Think of it like cooking multiple dishes: you boil pasta while simultaneously chopping vegetables. With sync code, you’d wait for the water to boil first.
> 

![image.png](attachment:d585912a-4a6e-49bb-8546-71051e3ec9c6:image.png)

For example, instead of waiting for an [HTTP request](https://blog.ragnarson.com/2013/09/03/life-of-an-http-request.html) to finish before continuing execution, with Python async coroutines you can submit the request and do other work that’s waiting in a queue while waiting for the HTTP request to finish.

---

## **The Synchronous Problem**

```python
import time

def fetch_site():
    print("Fetching site...")
    time.sleep(3)
    print("Done.")

fetch_site()
fetch_site()
```

**Output:**

```
Fetching site...
(wait 3 seconds)
Done.
Fetching site...
(wait 3 seconds)
Done.
```

This takes **6 seconds total**. You wait for each operation to complete **before starting the next**.

---

## **Introducing `async` and `await`**

`await` is a **keyword** in Python used to **pause** a coroutine until another coroutine completes.

It only works **inside an `async def` function**.

Let’s make it non-blocking using `asyncio`:

```python
import asyncio

async def fetch_site():
    print("Fetching site...")
    await asyncio.sleep(3)
    print("Done.")

async def main():
    await asyncio.gather(
        fetch_site(),
        fetch_site()
    )

asyncio.run(main())
```

✅ **Output:**

```
Fetching site...
Fetching site...
(wait 3 seconds)
Done.
Done.
```

> Only 3 seconds total! Tasks run concurrently.
> 

---

## **Important Concepts**

### `async def`

Defines an asynchronous function (aka coroutine). Must be awaited.

### `await`

Waits for a coroutine result **without blocking** other coroutines.

### `asyncio.run(main())`

Starts the event loop.

### `asyncio.gather(*tasks)`

Runs multiple coroutines concurrently and waits for all to finish.

---

## **Async HTTP Requests with `aiohttp`**

### Install:

```bash
pip install aiohttp
```

### Example:

```python
import aiohttp
import asyncio

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/get",
    "https://httpbin.org/uuid"
]

async def fetch(url, session):
    async with session.get(url) as response:
        data = await response.json()
        print(f"Fetched from {url}")
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())
```

---

## **Running Background Tasks**

Use `asyncio.create_task()` to start a task in the background:

```python
async def background_logger():
    while True:
        print("[LOG] System running...")
        await asyncio.sleep(5)

async def main():
    task = asyncio.create_task(background_logger())
    await asyncio.sleep(12)  # Let logger run in background

asyncio.run(main())
```

---

## **Best Practices**

| Tip | Description |
| --- | --- |
| ✅ Use `asyncio.run()` | Don’t manually create event loops |
| ✅ Use `aiohttp` not `requests` | Requests is blocking |
| ✅ Handle exceptions | Wrap calls with `try/except` |
| ❌ Avoid mixing sync & async | Especially with I/O |

---

## When Not to Use `async`

- **CPU-bound tasks** (use `concurrent.futures.ProcessPoolExecutor` or multiprocessing instead)
- Synchronous libraries (e.g., `requests`, `boto3` without async wrapper)
- Very simple scripts where concurrency offers no benefit

## What Is `async` About?

> Async is not about making your code faster. It’s about making it more efficient in situations where your program waits for something — especially I/O-bound operations.
> 

I/O-bound means:

- Waiting for a response from a **web API**
- Waiting for a **file to read or write**
- Waiting for a **database query**
- Waiting for a **network socket**

When you use `time.sleep(3)`, Python *literally pauses* and does nothing for 3 seconds. But if you use `await asyncio.sleep(3)`, it tells Python:

> "This task is idle. Let other things run."
> 

---

# Use Case 1: **Concurrent API Requests**

### Scenario:

You're building a monitoring tool that queries:

- GitHub API for repo stats
- Jira API for open issues
- Slack API to post alerts

Each API call takes ~1–2 seconds.

### With synchronous code:

```python
# Total time = 3 * 2 seconds = 6 seconds
resp1 = requests.get(github_url)
resp2 = requests.get(jira_url)
resp3 = requests.get(slack_url)
```

### With `asyncio` + `aiohttp`:

```python
# Total time = ~2 seconds
await asyncio.gather(
    fetch(github_url),
    fetch(jira_url),
    fetch(slack_url)
)
```

**Why async is better here:**

- Each call **waits** for the network.
- Async lets **other tasks proceed** while waiting.
- This is called **concurrent I/O**.

---

# Use Case 2: **Polling Health of Many Services**

### Scenario:

You want to check the `/health` endpoint of 20 Kubernetes microservices every 30 seconds.

### With threads:

- You’d create 20 threads
- Each thread uses **system memory** and incurs **overhead**

### With `asyncio`:

- You use **coroutines**, which are lightweight
- You can scale to **hundreds** of concurrent calls

```python
# Async polling loop
async def check_health(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            if r.status == 200:
                print(f"{url} is healthy ✅")
```

**Under the hood:**

- `asyncio` uses a **single thread**
- It switches between tasks **only when they’re waiting** (e.g., for HTTP response)
- This is called **cooperative multitasking**

---

# Use Case 3: **Streaming Logs or Data from Multiple Sources**

### Scenario:

You collect logs from:

- 5 services over REST
- 2 services via WebSocket
- 1 via tailing a file

### Challenge:

- Some sources are slow
- Some are high-frequency
- You want **all streams to update in near real time**

### With Async:

You can read from all of them concurrently, using:

- `aiohttp` for HTTP/WS
- `asyncio.to_thread()` for reading from disk
- `asyncio.Queue()` to buffer incoming lines

```python
async def stream_logs(url):
    async with session.get(url) as resp:
        async for line in resp.content:
            await queue.put(line)
```

**Real-world example:** Prometheus log forwarders, Elastic Filebeat alternatives.

---

# Use Case 5: **Terminal ChatBot with LLMs**

### Scenario:

You build a command-line tool that talks to a **local LLM** like GPT4All.

You want:

- Input prompt from user
- Call to LLM takes 5–10 seconds
- While LLM is generating output, show a loading animation
- Maybe allow pressing Ctrl+C to cancel

### Async makes this easy:

```python
# LLM call
async def query_llm(prompt):
    return await model.chat_async(prompt)

# Spinner
async def spinner():
    while True:
        print(".", end="", flush=True)
        await asyncio.sleep(0.5)

async def main():
    task = asyncio.create_task(query_llm(prompt))
    spin = asyncio.create_task(spinner())
    response = await task
    spin.cancel()
```

---

# Use Case 6: **Web Scraping (non-blocking)**

Let’s say you scrape 500 pages to extract prices of DevOps tools.

- `requests` blocks on every page
- Threads are clunky
- Async is ideal

Libraries like `aiohttp`, `httpx`, and `selectolax` are built for async scraping.

---

## Using `asyncio.gather`

`asyncio.gather()` runs multiple **async functions (coroutines)** **concurrently**, and waits until **all of them** are finished.

It returns a **list of results** (in the same order) when everything is done.

---

> “Run these 5 async tasks at the same time. Don’t block the program. When they’re all done, give me the results.”
> 

### Default behavior: ❌ Gathers all tasks, but **fails immediately** if one throws

```python
async def fail():
    raise ValueError("This failed")

async def succeed():
    await asyncio.sleep(1)
    return "Success"

async def main():
    results = await asyncio.gather(
        succeed(),
        fail(),            # this one raises
        succeed(),
    )

asyncio.run(main())  # Raises ValueError
```

### Solution: Use `return_exceptions=True`

```python
async def main():
    results = await asyncio.gather(
        succeed(),
        fail(),
        succeed(),
        return_exceptions=True
    )

    for i, res in enumerate(results):
	        if isinstance(res, Exception):
            print(f"Task {i} failed with: {res}")
        else:
            print(f"Task {i} succeeded with: {res}")

```

## What is `enumerate()` in Python?

### **Definition:**

`enumerate()` is a built-in Python function that lets you **loop through a list (or any iterable)** and get:

- The **index (position)** of each item
- The **value** of each item
    
    — all at the same time.
    

---

## Syntax

```python
enumerate(iterable, start=0)
```

- `iterable`: A list, tuple, string, etc.
- `start`: The number to start counting from (default is `0`)

---

## Example 1: Loop Through a List with Index

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output:**

```
0 apple
1 banana
2 cherry

```

Without `enumerate()`, you'd have to do this:

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

But `enumerate()` is cleaner, safer, and more readable.

## Difference Between `for item in list` vs. `for i, item in enumerate(list)`

| Syntax | What You Get |
| --- | --- |
| `for item in list:` | Just the item |
| `for i, item in enumerate(list):` | The index (`i`) and the item |

---

## Common Async-Related Libraries

| Library | Use |
| --- | --- |
| `aiohttp` | Async HTTP client/server |
| `asyncio` | Core async engine |
| `httpx` | Sync + async HTTP (modern) |
| `FastAPI` | Async web APIs |
| `rich` | Terminal + async support |
| `aiomysql`, `aiopg` | Async MySQL/Postgres clients |

## References

- [Python asyncio Docs](https://docs.python.org/3/library/asyncio.html)
- [`aiohttp` GitHub](https://github.com/aio-libs/aiohttp)
- Real-world usage:
    - FastAPI (async web framework)
    - [Prometheus async exporters](https://github.com/prometheus/client_python)