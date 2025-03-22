# Lab 14: Databases and Basic SQL in Python

This lab focuses on working with databases in Python, including SQLAlchemy ORM, basic SQL operations, and database management.

## Requirements

1. Create a module for database operations with the following features:
   - Database connection management
   - SQLAlchemy ORM setup
   - Basic CRUD operations
   - Transaction management
   - Connection pooling

2. Create a module for SQL operations that includes:
   - Basic SQL queries
   - Joins and relationships
   - Aggregations and grouping
   - Subqueries
   - Query optimization

3. Create a module for database utilities that includes:
   - Database migrations
   - Schema management
   - Data validation
   - Backup and restore
   - Database monitoring

## Directory Structure

```
labs/lab_14_databases/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Database operations
    ├── exercise2.py  # SQL operations
    └── exercise3.py  # Database utilities
```

## Dependencies

- pytest
- rich
- sqlalchemy
- alembic
- psycopg2-binary
- python-dotenv 