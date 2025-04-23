# MongoDB vs SQL
### **Schema Flexibility**

- **MongoDB**: Schema-less (documents can have different fields).
- **SQL**: Requires a predefined schema (tables, columns, data types).

**Use MongoDB when**:

- Your data shape might change frequently (e.g., user profiles, product listings).
- You want to store flexible or unstructured data (JSON-like).

**Example**:

```json
{ "name": "Alice", "email": "alice@example.com" }
{ "name": "Bob", "email": "bob@example.com", "hobbies": ["guitar", "chess"] }
```

---

### **Faster Prototyping**

- MongoDB lets you build and iterate **faster**.
- No need to define or alter database schemas every time you tweak a field.

> Ideal for startups, MVPs, or agile dev teams.
> 

---

### **Document-Oriented for JSON-Like Data**

- MongoDB stores data as **documents** (BSON).
- Perfect fit if your app already works with JSON (like REST APIs or frontend frameworks).

```json
{
  "post": "Mongo vs SQL",
  "tags": ["database", "mongodb", "nosql"],
  "published": true
}
```

---

### **Horizontal Scalability (Sharding)**

- MongoDB supports **easy scaling across multiple servers**.
- SQL databases often require vertical scaling or complex clustering.

> Mongo is great for big data, real-time analytics, or IoT apps.
> 

---

### **Built-In GeoQueries & Aggregations**

- MongoDB supports:
    - Full-text search
    - Geospatial queries
    - Rich aggregation pipelines

> These would be more complex to implement in traditional SQL.
> 

---

## When **NOT** to Use MongoDB

Use **SQL instead of MongoDB** when:

| Requirement | Choose SQL |
| --- | --- |
| Strong data consistency | ✅ Transactions |
| Relational data (foreign keys) | ✅ Joins |
| Complex queries across tables | ✅ SQL is stronger |
| Mature ecosystem (reporting, BI) | ✅ SQL support |

---

## Summary Table

| Feature | MongoDB (NoSQL) | SQL (e.g., PostgreSQL) |
| --- | --- | --- |
| Schema | Dynamic | Fixed |
| Data Structure | Document (JSON) | Tabular (rows/columns) |
| Scalability | Horizontal (sharding) | Vertical or complex cluster |
| Transactions | Limited (multi-doc: newer) | Strong ACID |
| Relationships | Manual (embedding/linking) | Joins |
| Flexibility | High | Low (strict schema) |
| Learning Curve | Lower | Higher |

---

### Real-World Use Case for MongoDB

- **User profiles** with many optional fields
- **Product catalog** where items can have different attributes
- **Log collection & analytics**
- **Mobile apps** syncing JSON to the cloud
- **Real-time applications** (chat, dashboards)