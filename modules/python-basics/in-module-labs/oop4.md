# Lab: Encapsulation & Abstraction

# *The Online Payment System*

### Prerequisites:

- Understanding of basic Python classes and methods
- Familiarity with OOP terms: attributes, methods, and constructors

---

## Objectives:

By the end of this lab, You will:

- Understand and apply **encapsulation** using private variables
- Use getter and setter methods to control access to sensitive data
- Understand and implement **abstraction** using abstract base classes (ABC)
- Practice creating reusable, extensible, and secure class structures

---

## Part 1: Encapsulation

### Task 1: Create a `UserAccount` Class

1. Create a class `UserAccount` with:
    - `username` (public)
    - `_balance` (private)
2. Add methods:
    - `deposit(amount)` → increases balance
    - `withdraw(amount)` → decreases balance
    - `get_balance()` → returns current balance
3. Protect the `_balance` attribute so it can't be changed directly from outside the class.

---

### Task 2: Add Access Control (Setters & Getters)

- Add a `@property` for balance and a `@balance.setter` that:
    - Prevents setting a negative balance
    - Prints a warning if someone tries to set it directly

---

## Part 2: Abstraction

### Task 3: Create an Abstract Base Class `PaymentMethod`

1. Use `from abc import ABC, abstractmethod`
2. Define a class `PaymentMethod(ABC)` with:
    - `pay(amount)` as an abstract method

---

### Task 4: Implement Concrete Classes

Create two subclasses:

- `CreditCardPayment` with:
    - `card_number`, `card_holder`
    - `pay(amount)` → prints "Paid $X with credit card ending in 1234"
- `PayPalPayment` with:
    - `email`
    - `pay(amount)` → prints "Paid $X using PayPal account: email"

---

### Task 5: Use Abstraction in Action

Write a function `process_payment(method: PaymentMethod, amount)` that:

- Accepts any subclass of `PaymentMethod`
- Calls `.pay(amount)` on it

Then:

- Create a credit card and a PayPal object
- Call `process_payment()` for each

---

## Link Payments to UserAccount

- After payment is successful, deduct the amount from a `UserAccount` using `withdraw()`
- Add error handling if the user doesn’t have enough balance

---

### Summary of Key Concepts:
| Concept | Demonstrated In |
| --- | --- |
| **Encapsulation** | Private `_balance` + controlled setters |
| **Abstraction** | `PaymentMethod` abstract class |
| **Reusability** | Multiple payment methods |
| **Security** | No direct access to sensitive attributes |