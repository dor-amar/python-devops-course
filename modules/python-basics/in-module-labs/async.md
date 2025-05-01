# Lab: Async

## Objective

By the end of this lab, you will:

- Understand the difference between sync and async functions
- Use `async def` and `await`
- Experience concurrent execution using `asyncio`
- Write a simple concurrent API fetcher using `aiohttp`

---

## Prerequisites

```bash
pip install aiohttp
```

---

## Lab Structure

```
async_lab/
├── step1_sync_sleep.py
├── step2_async_sleep.py
├── step3_api_sync.py
├── step4_api_async.py
├── step5_custom_project.py
```

---

## Synchronous Sleep Demo

### `step1_sync_sleep.py`

```python
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

def main():
    task("One")
    task("Two")
    task("Three")

if __name__ == "__main__":
    main()
```

### Tasks:

- Run it and time how long it takes
- Why does it take ~6 seconds?
- What is blocking the execution?

---

## Make It Asynchronous

### `step2_async_sleep.py`

```python
# Make the Program Asynchronous using asyncio library

```

### Tasks:

- Run it and see the time drop to ~2 seconds
- What changed?
- Why did it get faster?
- What does `await` do?

---

## Sync API Calls

### `step3_api_sync.py`

```python
import requests
import time

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/get",
    "https://httpbin.org/uuid"
]

def fetch(url):
    print(f"Fetching {url}")
    response = requests.get(url)
    print(f"Done {url} – {response.status_code}")

start = time.time()

for url in urls:
    fetch(url)

print(f"Took {time.time() - start:.2f} seconds")
```

### Tasks:

- Observe the total time (should be ~4-5 seconds)
- This is a real-world I/O bottleneck

---

## Async API Calls with `aiohttp`

### `step4_api_async.py`

```python
import aiohttp
import asyncio
import time

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/get",
    "https://httpbin.org/uuid"
]

async def fetch(url, session):
    print(f"Fetching {url}")
    async with session.get(url) as resp:
        print(f"Done {url} – {resp.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f"Took {time.time() - start:.2f} seconds")

```

### Tasks:

- Compare the runtime
- Explain why it’s faster
- Understand how coroutines are used
- Note how `aiohttp` replaces `requests`

---

## Build Your Own Website Health Checker

### Instructions:

1. Create a file `step5_custom_project.py`
2. Create an async function to check if a website returns status 200
3. Use a list of URLs (at least 5)
4. Log their status
5. Print a summary

```python
# Sample URLs
urls = [
    "https://google.com",
    "https://dorthebestteacher.url.test",  # test error (url doesnt exists)
    "https://github.com"
]
```

**Optional Bonus:**

- Add retry with `asyncio.sleep()`
- Write failures to a file