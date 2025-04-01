# Project: **Freelancer Project Tracker**

---

In this project, you’re going to simulate how a freelancer tracks clients, projects, and payments.

This will help you practice OOP in a real-world-like scenario. No fluff — just classes and logic.

---

## ✨ What you’ll practice:

- Classes & objects
- Inheritance
- Abstraction
- Encapsulation
- Polymorphism
- Exception handling
- Lists, loops, basic CLI

---

## The Plan

We’ll have a few simple classes to start:

### 📦 `Person`

Just a base class for `Client`.

Has:

- `name`, `email`
- a `describe()` method

---

### 💼 `Client` (inherits from Person)

Adds:

- `company`
- a `make_payment()` method

---

### 🧠 `Project` (abstract base class)

You don’t start with a generic project. We’ll subclass this later.

Has:

- `title`, `client`, `rate_per_hour`, `hours_worked`
- `log_hours()`
- `calculate_cost()`
- abstract method: `describe()`

---

### 👷 Subclasses of `Project`:

We’ll make 3 types just for fun:

- `DesignProject` → uses a design tool (e.g., Figma)
- `DevProject` → adds a programming language

Each one overrides `describe()` — this is where you’ll see **polymorphism** in action.

---

### 📄 `Invoice`

Very simple:

- connected to a project
- tracks: `due_amount`, `paid`, `status`
- has a method `mark_paid()` and a property `status` to return "Paid"/"Pending"

---

### 👤 `Freelancer`

Manages:

- List of clients
- List of projects
- Can:
    - Add clients
    - Start new projects
    - Log hours
    - Generate invoices

---

### Basic menu loop

Make it feel interactive (just using `input()` and `print()`):

```bash
Welcome to Freelancer Tracker!
1. Add new client
2. Start new project
3. Log hours
4. View invoices
5. Mark invoice as paid
6. Exit
```

---

## What You’ll End Up With:

A nice little CLI app where you can:

- Add clients
- Start projects
- Track hours
- Bill people
- Get some OOP confidence