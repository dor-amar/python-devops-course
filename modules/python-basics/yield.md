By the end of this lab, you will be able to:

- Understand what `yield` is and how it differs from `return`
- Create generators using `yield`
- Use generators to efficiently process large or infinite data
- Apply `yield` in real-world-like scenarios

---

### What is `yield`

In Python, `yield` is used to **pause** a function and return a value **without ending the function**. The function becomes a **generator**.

It allows you to:

- Iterate over large data **without loading it all into memory**
- Resume function execution from where it left off

### What Does It Mean When a Function Becomes a Generator?

A **generator function** is a special kind of function that **doesn’t return all its results at once**.

Instead, it **pauses** at each `yield`, remembers its state, and **resumes** from where it left off — like a bookmark in a book.

---

### In simple terms:

> A generator is a function that can give you one value at a time, and then keep going when you ask for the next one.
> 

### Why Is This Useful?

- **Memory efficiency**: No need to store large lists in memory.
- **Lazy evaluation**: Values are only computed when needed.
- **Infinite sequences**: Like Fibonacci or file readers, where data could be endless.

---

### Difference Between `return` and `yield`

| Feature | `return` | `yield` |
| --- | --- | --- |
| Ends function? | Yes | No (pauses execution) |
| Output | Single value | A generator (iterator) |
| Memory usage | High (if many items) | Low (lazy evaluation) |

---

### Simple Example – Countdown Generator

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

**Expected Output:**

```
5
4
3
2
1
```

🧠 Each time through the loop, the function pauses at `yield n`, returns a value, then resumes.

---

### Yield vs Return

```python
def with_return():
    return [1, 2, 3]

def with_yield():
    yield 1
    yield 2
    yield 3

print(with_return())          # [1, 2, 3]
print(list(with_yield()))     # [1, 2, 3]
```

---

### Infinite Sequence with Yield

```python
def infinite_numbers(start=0):
    while True:
        yield start
        start += 1

gen = infinite_numbers()

for i in range(5):
    print(next(gen))  # prints 0, 1, 2, 3, 4
```

💡 Useful when you need infinite streams or lazy evaluation.

---

### File Processing with Yield (Memory Efficient)

```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("big_file.txt"):
    if "error" in line:
        print("Found error:", line)
```

🔥 This is much more memory-friendly than reading the entire file into a list.

---

### Advanced — Using `yield` with `send()`

```python
def echo():
    while True:
        received = yield
        print("You sent:", received)

gen = echo()
next(gen)             # Start generator
gen.send("Hello")     # Output: You sent: Hello

```

🧠 You can **send values into generators**, turning them into **coroutines** (used in async programming too).

---

### **You want to generate a sequence of values one at a time**

Instead of returning a full list, you generate items on the fly.

### Why?

- Saves memory
- Speeds up performance if you don’t need everything at once

### Real Example:

```python
def even_numbers():
    for i in range(1000000):
        if i % 2 == 0:
            yield i

for num in even_numbers():
    if num > 10:
        break
    print(num)
```

- **No need to build a list of 1 million numbers**
- Only generates until you say “stop”