# **Shell vs Python**

**Use Shell Scripting When:**

1. **System Administration Tasks:** Shell scripting is excellent for automating routine system administration tasks like managing files, directories, and processes. You can use shell scripts for tasks like starting/stopping services, managing users, and basic file manipulation.
2. **Command Line Interactions:** If your task primarily involves running command line tools and utilities, shell scripting can be more efficient. It's easy to call and control these utilities from a shell script.
3. **Rapid Prototyping:** If you need to quickly prototype a solution or perform one-off tasks, shell scripting is usually faster to write and execute. It's great for ad-hoc tasks.
4. **Text Processing:** Shell scripting is well-suited for tasks that involve text manipulation, such as parsing log files, searching and replacing text, or extracting data from text-based sources.
5. **Environment Variables and Configuration:** Shell scripts are useful for managing environment variables and configuring your system.

**Use Python When:**

1. **Complex Logic:** Python is a full-fledged programming language and is well-suited for tasks that involve complex logic, data structures, and algorithms. If your task requires extensive data manipulation, Python can be a more powerful choice.
2. **Cross-Platform Compatibility:** Python is more platform-independent than shell scripting, making it a better choice for tasks that need to run on different operating systems.
3. **API Integration:** Python has extensive libraries and modules for interacting with APIs, databases, and web services. If your task involves working with APIs, Python may be a better choice.
4. **Reusable Code:** If you plan to reuse your code or build larger applications, Python's structure and modularity make it easier to manage and maintain.
5. **Error Handling:** Python provides better error handling and debugging capabilities, which can be valuable in DevOps where reliability is crucial.
6. **Advanced Data Processing:** If your task involves advanced data processing, data analysis, or machine learning, Python's rich ecosystem of libraries (e.g., Pandas, NumPy, SciPy) makes it a more suitable choice.

## **Shell vs Python for DevOps Engineers**

### **Learning Objectives**

By the end of this lecture, you will:

✅ Understand the differences between **Shell scripting (Bash)** and **Python** in DevOps.

✅ Identify **when to use Shell** vs **when to use Python**.

✅ Write **basic automation scripts** in both Shell and Python.

✅ Compare **performance, scalability, and readability** of both languages.

---

## **1️⃣ Why Compare Shell and Python?**

As a DevOps engineer, automation is key. The two most common scripting choices are:

- **Shell Scripting (Bash, Zsh, etc.)** – Best for **system administration tasks** and **command execution**.
- **Python** – A full-fledged programming language, best for **cloud automation, API interactions, and CI/CD workflows**.

🔹 **Which one should you use?** It depends on the task!

---

## **2️⃣ Key Differences Between Shell and Python**

| Feature | Shell Scripting (Bash) | Python |
| --- | --- | --- |
| **Ease of Use** | Simple syntax for OS commands | More structured and readable |
| **Portability** | Unix/Linux-based | Cross-platform (Windows, Linux, Mac) |
| **Performance** | Faster for small system tasks | More overhead but powerful for larger tasks |
| **Automation Scope** | Best for file manipulation, process management | Best for APIs, data processing, cloud automation |
| **Error Handling** | Limited (`set -e`, `trap`) | Advanced exception handling (`try-except`) |
| **Libraries** | Minimal (awk, sed, grep) | Extensive ecosystem (boto3, requests, paramiko) |
| **Interactivity** | Command-line focused | Can be used in CLI, web apps, and APIs |

---

## **3️⃣ When to Use Shell vs Python?**

### **✅ Use Shell When:**

✔ Automating simple system tasks (**file manipulation, package installs**).

✔ Writing quick one-liners (e.g., `find . -name "*.log" -delete`).

✔ Running repetitive CLI commands (`cron` jobs).

✔ Configuring and managing servers (starting/stopping services).

### **✅ Use Python When:**

✔ Automating complex workflows (**cloud management, monitoring**).

✔ Interacting with APIs (**AWS, Kubernetes, CI/CD pipelines**).

✔ Handling **data processing, parsing JSON, and logs**.

✔ Writing **cross-platform automation tools**.

---

## **4️⃣ Hands-On Example: File Management**

### **🔹 Task: Delete all `.log` files older than 7 days**

### **👉 Using Shell**

```bash
find /var/logs -name "*.log" -mtime +7 -exec rm {} \;

```

✅ One-liner, very efficient.

### **👉 Using Python**

```python
import os
import time

log_dir = "/var/logs"
for file in os.listdir(log_dir):
    file_path = os.path.join(log_dir, file)
    if file.endswith(".log") and os.stat(file_path).st_mtime < time.time() - 7*86400:
        os.remove(file_path)

```

✅ More readable, reusable, and extendable.

---

## **5️⃣ Hands-On Example: Working with APIs**

### **🔹 Task: Get public IP using an API**

### **👉 Using Shell**

```bash
curl -s https://api.ipify.org

```

✅ Simple but limited if further processing is needed.

### **👉 Using Python**

```python
import requests
response = requests.get("https://api.ipify.org")
print(response.text)

```

✅ Python allows better error handling and additional data manipulation.

---

## **6️⃣ Error Handling: Shell vs Python**

### **👉 Error Handling in Shell**

```bash
#!/bin/bash
set -e  # Exit on error
if ! ping -c 1 google.com; then
    echo "Internet down!"
    exit 1
fi
echo "Internet is up!"

```

✅ Basic error handling but less flexibility.

### **👉 Error Handling in Python**

```python
import subprocess

try:
    subprocess.run(["ping", "-c", "1", "google.com"], check=True)
    print("Internet is up!")
except subprocess.CalledProcessError:
    print("Internet down!")

```

✅ More control over exceptions and debugging.

---