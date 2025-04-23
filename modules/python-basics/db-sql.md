# Database + SQL

![image.png](/images/dbsql1.png)

### What is a Database?

A **database** is an organized collection of data that is stored and managed in a way that makes it easy to access, update, and retrieve information. It serves as a central location where data is stored so that it can be used efficiently for various purposes, such as querying, reporting, and analysis.

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

## What is SQL ?


![image.png](/images/dbsql2.png)

SQL (Structured Query Language) is a programming language used to interact with databases. In simple terms, it helps you:

1. **Store data**: Add new information to a database (e.g., saving user details or product listings).
2. **Retrieve data**: Get specific information from a database (e.g., finding a user's profile or a list of orders).
3. **Update data**: Modify existing information in a database (e.g., updating a user’s email address).
4. **Delete data**: Remove information from a database (e.g., deleting an account or an old record).

### Types of Databases:

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

### Why Use a Database?

1. **Data Storage**:
    - Keep data organized and persistent (saved even after the program ends).
2. **Data Retrieval**:
    - Quickly search and filter through data using queries.
3. **Data Integrity**:
    - Ensure data is accurate and consistent through rules and relationships.
4. **Data Sharing**:
    - Multiple users or applications can access the same data securely.
5. **Scalability**:
    - Handle growing amounts of data efficiently.

---

### Simple Analogy:

Think of a database like a digital **filing cabinet**:

- Each drawer is a **table**.
- Each folder in the drawer is a **row** in the table.
- Labels on the folders (e.g., "Name," "Age") are the **columns**.
It keeps everything organized so you can find and use information quickly.

---

![image.png](/images/dbsql3.png)


## **SQL Basics**

### SQL Basics

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
    
    **Output**:
    
    ---
    
    ---
    
    ---
    
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

### Practice Exercise:

1. Create a table `Products` with columns: `id`, `name`, `price`, `quantity`.
2. Insert three products into the `Products` table.
3. Retrieve all products with a price greater than $10.
4. Update the quantity of a product.
5. Delete a product with a specific `id`.

---
## Navigation

[⬅️ Previous: Flask Route Template Form](flask-route-template-form.md) | [Next: SQLite3 ➡️](sqlite3.md)
