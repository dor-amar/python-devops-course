# Introduction to Python

## **Learning Objectives**

By the end of this lesson, you will:

✔ Understand what Python is and why it is used in DevOps.

✔ Install Python on your system.

✔ Set up VS Code for Python development.

✔ Install and configure essential extensions for Python development.

✔ Run your first Python script.

---

## **What is Python and Why is it Important for DevOps?**

Python is a high-level, interpreted programming language widely used in **DevOps** for automation, infrastructure management, CI/CD pipelines, and cloud scripting.

### **🔹 Why DevOps Engineers Use Python**

- **Automation**: Manage servers, automate deployments, and interact with cloud APIs.
- **Infrastructure as Code (IaC)**: Work with Terraform, Ansible, and Kubernetes.
- **CI/CD Pipelines**: Automate build and deployment workflows.
- **Monitoring & Logging**: Collect and analyze logs using Python scripts.
- **Cross-platform**: Works on Linux, macOS, and Windows.

---

## **Installing Python**

### **🔹 Windows**

1. **Download Python** from the official site: https://www.python.org/downloads/
2. **Check “Add Python to PATH”** before installing.
3. **Verify installation**:

or
    
    ```
    python --version
    ```
    
    ```
    python3 --version
    ```
    

### **Linux (Ubuntu/Debian)**

```
sudo apt update && sudo apt install python3 python3-pip -
```

Verify installation:

```
python3 --version
```

---

## **Setting Up Visual Studio Code for Python**

**VS Code** is a lightweight IDE that provides great support for Python.

### **🔹 Installing VS Code**

1. Download and install VS Code: https://code.visualstudio.com/
2. Open VS Code and install the **Python extension**.

---

## **Essential VS Code Extensions for Python Development**

Go to **Extensions (`Ctrl + Shift + X`)** and install:

| Extension | Description |
| --- | --- |
| **Python** (by Microsoft) | Adds Python language support, IntelliSense, debugging, and linting. |
| **Python Indent** | Improves indentation handling in Python scripts. |
| **Pylance** | Fast IntelliSense and type checking. |
| **REST Client** | Useful for testing APIs. |

---

## **Configuring VS Code for Python**

### **🔹 Setting the Default Python Interpreter**

1. **Open Command Palette (`Ctrl + Shift + P`)**
2. Search for **“Python: Select Interpreter”**
3. Choose the correct Python version (e.g., Python 3.x).

### **🔹 Enable Autoformatting & Linting**

1. Open **Settings (`Ctrl + ,`)**
2. Search for `"formatOnSave"` and enable it.
3. Install `black` for code formatting:
    
    ```
    pip install black
    ```
    
4. Enable `black` in VS Code settings.

---

## **Running Your First Python Script**

1. **Create a new folder** for your project.
2. **Open it in VS Code** (`File > Open Folder`).
3. **Create a file** named `hello.py`.
4. **Write your first script:**
    
    ```python
    print("Hello, DevOps Engineers!")
    ```
    
5. **Run the script** using:

or
    
    ```
    python hello.py
    ```
    
    ```
    python3 hello.py
    ```
    

---

## **Setting Up a Virtual Environment**

A **virtual environment** helps manage dependencies and isolate projects.

### **🔹 Creating a Virtual Environment**

```
python -m venv myenv
```

### **🔹 Activating the Virtual Environment**

- **Linux**:
    
    ```
    source venv/bin/activate
    ```
    

### **🔹 Installing Dependencies in the Virtual Environment**

```
pip install requests
```

Deactivate when done:

```
deactivate
```