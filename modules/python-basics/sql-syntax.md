# SQL queries examples (SQL Server)

We are going to use a free aql tool for demo before we dive into how to integrate a DB and a Python Program - https://sqlfiddle.com/sql-server/online-compiler?id=6afcdc88-0b32-4f5a-823c-fcb7ba8d7dbe

**What is the diffrence between SQL Server and SQLite ?**

| Feature | **SQLite** | **SQL Server** |
| --- | --- | --- |
| Type | Lightweight, file-based | Full-featured, client-server DB |
| Setup | No server, zero config | Requires installation & configuration |
| Storage | Single `.db` file | Runs on a database server |
| Ideal For | Small apps, embedded systems, prototyping | Large apps, enterprise systems, production |
| Performance | Great for small apps | Optimized for high concurrency & big data |
| Scalability | Not built for heavy load | Scales well (clustering, replicas) |
| Auto Increment | `INTEGER PRIMARY KEY` | Must use `IDENTITY` |
| Data Types | Flexible (weak typing) | Strict (strong typing) |
| Access | Local file | Over network via TCP/IP |
| Tools | DB Browser for SQLite | SQL Server Management Studio (SSMS) |
| Transactions | Supported | Fully supported, with advanced control |

---

## How They Work

### **SQLite**

- **No server process.**
- Stores all data in **a single file**.
- Great for local apps, mobile apps (Android/iOS), quick development.
- Requires **no configuration** — just include the `.db` file.

💡 Think of it as a **portable Excel on steroids**, using SQL.

---

### **SQL Server**

- **Runs as a service** (background process).
- You connect to it via a client (e.g., Python, SSMS, .NET).
- Used in **enterprise backends**, supports **huge datasets**, multiple users, **permissions**, stored procedures, and more.
- Much better for **multi-user**, **concurrent**, **secured**, and **large-scale** applications.

💡 Think of it as a **data powerhouse** managed and optimized by DB admins in a company.

# SQL Query List for Practice

## Create the Table

```sql
CREATE TABLE students (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    grade INT NOT NULL,
    city NVARCHAR(100)
);
```

---

## Insert Sample Data

```sql
INSERT INTO students (name, grade, city) VALUES ("Dor", 88, "Bangkok");
INSERT INTO students (name, grade, city) VALUES ("Jessie", 72, "Delaware");
INSERT INTO students (name, grade, city) VALUES ("Eilon", 90, "Tel Aviv");
INSERT INTO students (name, grade, city) VALUES ("Nofar", 65, "Kefar Bialik");
```

---

## Practice Queries

### Basic Select

```sql
SELECT * FROM students;
```

### Filtering

```sql
SELECT * FROM students WHERE grade > 80;

SELECT * FROM students WHERE city = 'Bangkok';

SELECT * FROM students WHERE grade BETWEEN 70 AND 90;

SELECT * FROM students WHERE name LIKE 'A%';
```

### Sorting

```sql
SELECT * FROM students ORDER BY grade DESC;

SELECT * FROM students ORDER BY name ASC;
```

### Specific Columns

```sql
SELECT name, grade FROM students;

SELECT DISTINCT city FROM students;
```

### Aggregation

```sql
SELECT AVG(grade) AS average_grade FROM students;

SELECT COUNT(*) FROM students;

SELECT MAX(grade) FROM students;

SELECT MIN(grade) FROM students;
```

### Grouping

```sql

SELECT city, COUNT(*) AS total FROM students GROUP BY city;

SELECT city, AVG(grade) FROM students GROUP BY city;

```

### Updating

```sql
UPDATE students SET grade = 100 WHERE name = 'Dor';
```

### Deleting

```sql
DELETE FROM students WHERE name = 'Eilon';

```

### Inserting More

```sql
INSERT INTO students (name, grade, city) VALUES ('Emma', 77, 'Boston');
```

### Logic

```sql
SELECT name,
       CASE
           WHEN grade >= 90 THEN 'Excellent'
           WHEN grade >= 75 THEN 'Good'
           ELSE 'Needs Improvement'
       END AS performance
FROM students;
```