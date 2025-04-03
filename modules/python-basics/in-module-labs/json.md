# Lab: Working with a JSON file

- Practice reading and analyzing structured data from a JSON file using Python.

## 📁 `transactions.json`

```json

[
  {
    "timestamp": "2025-04-01T08:00:00Z",
    "event": "user_login",
    "user_id": "u123",
    "status": "success"
  },
  {
    "timestamp": "2025-04-01T08:01:12Z",
    "event": "add_to_cart",
    "user_id": "u123",
    "product_id": "p101",
    "quantity": 2
  },
  {
    "timestamp": "2025-04-01T08:02:45Z",
    "event": "checkout",
    "user_id": "u123",
    "order_id": "o789",
    "total": 49.99,
    "status": "completed"
  },
  {
    "timestamp": "2025-04-01T08:05:00Z",
    "event": "user_login",
    "user_id": "u999",
    "status": "failure"
  },
  {
    "timestamp": "2025-04-01T08:06:33Z",
    "event": "add_to_cart",
    "user_id": "u888",
    "product_id": "p103",
    "quantity": 1
  },
  {
    "timestamp": "2025-04-01T08:07:10Z",
    "event": "checkout",
    "user_id": "u888",
    "order_id": "o790",
    "total": 15.99,
    "status": "error",
    "error": "payment_declined"
  },
  {
    "timestamp": "2025-04-01T08:10:00Z",
    "event": "user_logout",
    "user_id": "u123"
  },
  {
    "timestamp": "2025-04-01T08:12:18Z",
    "event": "user_login",
    "user_id": "u123",
    "status": "success"
  },
  {
    "timestamp": "2025-04-01T08:15:50Z",
    "event": "checkout",
    "user_id": "u123",
    "order_id": "o791",
    "total": 89.00,
    "status": "completed"
  }
]

```

### **Task 1: Load the JSON Data**

Open the file and load the data into a Python variable. Verify the number of events (entries) in the file by printing the total length.

**Expected output:**

You should see how many total transaction events are in the file.

---

### **Task 2: Print All Events of Type `"checkout"`**

Loop through the data and print only those events where the `"event"` is `"checkout"`.

**Hint:** Check if `entry["event"] == "checkout"`.

---

### **Task 3: Count How Many Checkouts Were Completed Successfully**

Count how many checkout events have a `"status"` of `"completed"`.

---

### **Task 4: Calculate Total Revenue From Completed Orders**

Sum the `"total"` field for all checkout events where the `"status"` is `"completed"`.

**Expected output:**

You should see the total revenue made from successful checkouts.

---

### **Task 5: List All Users Who Failed to Log In**

Loop through the data and print `user_id`s for login attempts that failed (`"status": "failure"`).

---

### **Task 6: Write All Error Events to a New JSON File**

Extract all entries where `"status"` is `"error"` and write them to a new file called `errors.json`.

---

### **Task 7: Create a Summary Report of Event Types**

At the end, count how many times each event type occurred (e.g., `user_login`, `checkout`, etc.) and print the results in the format:

```
user_login: 3
checkout: 3
add_to_cart: 2
user_logout: 1
```