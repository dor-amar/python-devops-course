# Database + SQL

![image.png](/images/dbsql1.png)

### What is a Database?

A **database** is an organized collection of data that is stored and managed in a way that makes it easy to access, update, and retrieve information. It serves as a central location where data is stored so that it can be used efficiently for various purposes, such as querying, reporting, and analysis.

A **database** is like a **digital storage room** for your application’s data.

Whenever your app needs to **remember** something (users, tasks, posts), you store it in a database.

### Key Features of a Database:

1. **Organized Structure**:
    - Data is stored in tables (rows and columns) in relational databases, or in other structures like documents, key-value pairs, or graphs in non-relational databases.
2. **Data Management**:
    - A database ensures consistency, accuracy, and reliability of data through features like constraints, indexes, and relationships.
3. **Efficient Retrieval**:
    - Databases allow for efficient querying of large datasets using languages like SQL (Structured Query Language).
4. **Scalability**:
    - Databases can handle small amounts of data (e.g., personal data) to massive datasets (e.g., enterprise or cloud-scale data).
5. **Security**:
    - Access to the database can be controlled to protect sensitive information.

---

## Two Main Types of Databases

| Type | Description | Example Databases |
| --- | --- | --- |
| **SQL** | Structured data, uses tables & relationships | SQLite, PostgreSQL, MySQL |
| **NoSQL** | Flexible, uses JSON-like data or key-value | MongoDB, Redis, Firebase |

### Types of Databases examples:

1. **Relational Databases (SQL)**:
    - Data is stored in structured tables with predefined schemas.
    - Common examples: MySQL, PostgreSQL, Microsoft SQL Server, SQLite.
    - Example:
        
        ```sql
        CREATE TABLE Users (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50)
        );
        ```
        
2. **Non-Relational Databases (NoSQL)**:
    - Data is stored in formats like key-value pairs, documents, graphs, or wide-columns.
    - Common examples: MongoDB, Redis, Cassandra, Neo4j.
    - Example (MongoDB):
        
        ```json
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        }
        ```
        
3. **Cloud Databases**:
    - Hosted in the cloud and scalable on-demand.
    - Examples: AWS RDS, Google BigQuery, Azure Cosmos DB.
4. **In-Memory Databases**:
    - Data is stored in memory for faster access.
    - Example: Redis.

---

## What is SQL ?

### Think in **Tables**

- Like Excel sheets: rows & columns.
- Each row = one record (e.g. a user).
- Each column = one field (e.g. name, age).


![image.png](/images/dbsql2.png)

SQL (Structured Query Language) is a programming language used to interact with databases. In simple terms, it helps you:

1. **Store data**: Add new information to a database (e.g., saving user details or product listings).
2. **Retrieve data**: Get specific information from a database (e.g., finding a user's profile or a list of orders).
3. **Update data**: Modify existing information in a database (e.g., updating a user’s email address).
4. **Delete data**: Remove information from a database (e.g., deleting an account or an old record).


![image.png](/images/dbsql3.png)
## **SQL Basics**

**SQL (Structured Query Language)** is a language used to interact with databases. It allows you to create, read, update, and delete data in a database. These operations are commonly known as **CRUD** operations.

---

### Basic Concepts of SQL:

1. **Database**: A collection of tables where data is stored.
2. **Table**: A structured format to store data in rows and columns.
    - **Row**: A single record in a table.
    - **Column**: An attribute or field in the table.

---

### Common SQL Commands:

### 1. **Creating a Table**

Defines the structure of a table in the database.

```sql
CREATE TABLE Users (
    id INT PRIMARY KEY,       -- Unique identifier
    name VARCHAR(50),         -- String with a max length of 50
    email VARCHAR(100),       -- String with a max length of 100
    age INT                   -- Integer for age
);
```

---

### 2. **Inserting Data**

Adds new rows (records) into a table.

```sql
INSERT INTO Users (id, name, email, age)
VALUES (1, 'John Doe', 'john@example.com', 25);

```

---

### 3. **Selecting Data**

Retrieves data from one or more tables.

- Retrieve all columns:

```sql
SELECT * FROM Users
```

- Retrieve specific columns:

```sql
SELECT name, email FROM Users;
```

---

### 4. **Updating Data**

Modifies existing data in a table.

```sql
UPDATE Users
SET age = 26
WHERE id = 1;
```

---

### 5. **Deleting Data**

Removes data from a table.

```sql
DELETE FROM Users
WHERE id = 1;
```

---

### 6. **Filtering Data**

Uses the `WHERE` clause to retrieve specific records.

```sql
SELECT * FROM Users
WHERE age > 20;  -- Selects users older than 20
```

---

### 7. **Sorting Data**

Sorts records using `ORDER BY`.

```sql
SELECT * FROM Users
ORDER BY age DESC;  -- Sorts by age in descending order
```

---

### 8. **Aggregate Functions**

Performs calculations on multiple rows.

- Count the number of rows:

```sql
SELECT COUNT(*) FROM Users;
```

- Find the average age:

```sql
SELECT AVG(age) FROM Users;
```

- Get the maximum age:

```sql
SELECT MAX(age) FROM Users;
```

---

### 9. **Grouping Data**

Groups records using `GROUP BY`.

```sql
SELECT age, COUNT(*)
FROM Users
GROUP BY age
```

---

### 10. **Joining Tables**

Combines rows from two or more tables based on a related column.

- Example with two tables: `Users` and `Orders`:

```sql
SELECT Users.name, Orders.order_date
FROM Users
JOIN Orders ON Users.id = Orders.user_id;
```

---

### Sample Table and Queries:

### Table: `Users`

| id | name | email | age |
| --- | --- | --- | --- |
| 1 | John Doe | john@example.com | 25 |
| 2 | Jane Smith | jane@example.com | 30 |

### Example Queries:

1. Get all user names:nameJohn DoeJane Smith
    
    ```sql
    SELECT name FROM Users;
    ```
    
2. Find users older than 25:
    
    ```sql
    SELECT * FROM Users WHERE age > 25;
    ```
    
    **Output**:
    
    | id | name | email | age |
    | --- | --- | --- | --- |
    | 2 | Jane Smith | jane@example.com | 30 |
3. Count the total number of users:
    
    ```sql
    SELECT COUNT(*) FROM Users;
    ```
    
    **Output**: `2`
    

---

## Tools We’ll Use Later

| Tool | Use |  
| --- | --- |
| SQLite Browser | GUI to view & test SQL |
| SQLAlchemy | Python ORM to connect Flask to SQL |
| Flask + SQLite | Our first real web app with a database |
| Flask + MongoDB | (later) Flask app with a NoSQL backend |

## Navigation

[⬅️ Previous: Flask Route Template Form](flask-route-template-form.md) | [Next: SQLite3 ➡️](sqlite3.md)
