# Project: **Smart Café Order Management System**

---

## **Project Objective**

Build a system to manage a small café’s daily operations using Object-Oriented Programming. The system allows baristas to take orders, process payments, manage customers, track loyalty points, and generate receipts.

This project will reinforce:

- **OOP Principles** (Inheritance, Polymorphism, Encapsulation, Abstraction)
- **Exception Handling**
- **Loops & Conditionals**
- **Decorators**
- **File I/O**
- **Command-Line Interaction**

---

## System Overview

```
classes/
│
├── Person (base class)
│   ├── Customer
│   └── Barista
│
├── Abstract class: Drink
│   ├── Coffee
│   ├── Tea
│   └── Juice
│
├── Order
│
└── CafeSystem (main interface class)
```

---

## Step-by-Step Tasks

### Step 1: Create a Base Class `Person`

- Attributes: `name`, `email`
- Method: `describe()` to return person's info

---

### Step 2: Subclass `Customer`

- Inherits from `Person`
- Private attribute: `_loyalty_points`
- Methods:
    - `add_points(points)`
    - `redeem_points()` → if over 100, get a free drink
    - `@property loyalty_points`

---

### Step 3: Subclass `Barista`

- Inherits from `Person`
- Can `create_order(customer, drinks)`
- Can `print_receipt(order)`

---

### Step 4: Create Abstract Class `Drink`

- Use `from abc import ABC, abstractmethod`
- Attributes: `name`, `price`
- Abstract method: `prepare()`

Create three subclasses:

- `Coffee`
- `Tea`
- `Juice`

Each implements `prepare()` with a different message.

---

### Step 5: Create `Order` Class

- Attributes: `customer`, `drinks` (list of Drink), `total_price`
- Method: `calculate_total()`
- Decorated with `@log_order` decorator to log the order

---

### Step 6: Encapsulation + Validation

- Protect drink prices and loyalty points
- Use `@property` and `@setter` to validate:
    - Drink price must be > 0
    - Points can't go below 0
- Raise custom exceptions if rules are broken

---

### Loop & Menu (CafeSystem)

```bash
Welcome to the Smart Café!
1. Add customer
2. Take order
3. Show customer points
4. Redeem loyalty reward
5. Exit
```

### 🧾 Decorators

- `@log_order(func)` — logs each order to a file or console
- `@auth_required` — can be used for Barista actions (if the user is Barista)