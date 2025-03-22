"""SQLite operations module."""

import os
import sqlite3
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime
from contextlib import contextmanager
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class SQLiteManager:
    """Manager for SQLite database operations."""

    def __init__(self, db_path: Optional[str] = None):
        """Initialize the SQLite manager.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path or os.getenv(
            'SQLITE_DB_PATH',
            'database.db'
        )
        self._ensure_db_directory()

    def _ensure_db_directory(self) -> None:
        """Ensure the database directory exists."""
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            Path(db_dir).mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self):
        """Context manager for database connections.

        Yields:
            sqlite3.Connection: Database connection
        """
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def create_tables(self) -> None:
        """Create database tables."""
        with self.connect() as conn:
            cursor = conn.cursor()

            # Create customers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Create products table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Create orders table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_amount REAL DEFAULT 0.0,
                    status TEXT DEFAULT 'pending',
                    FOREIGN KEY (customer_id) REFERENCES customers (id)
                )
            ''')

            # Create order_items table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS order_items (
                    order_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    PRIMARY KEY (order_id, product_id),
                    FOREIGN KEY (order_id) REFERENCES orders (id),
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
            ''')

    def drop_tables(self) -> None:
        """Drop all database tables."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS order_items")
            cursor.execute("DROP TABLE IF EXISTS orders")
            cursor.execute("DROP TABLE IF EXISTS products")
            cursor.execute("DROP TABLE IF EXISTS customers")

    def add_customer(self, name: str, email: str) -> int:
        """Add a new customer.

        Args:
            name: Customer name
            email: Customer email

        Returns:
            int: Customer ID
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO customers (name, email) VALUES (?, ?)",
                (name, email)
            )
            return cursor.lastrowid

    def get_customer(self, customer_id: int) -> Optional[Dict[str, Any]]:
        """Get a customer by ID.

        Args:
            customer_id: Customer ID

        Returns:
            Optional[Dict[str, Any]]: Customer data if found
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM customers WHERE id = ?",
                (customer_id,)
            )
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "created_at": row[3]
                }
            return None

    def add_product(
        self,
        name: str,
        description: str,
        price: float,
        stock: int
    ) -> int:
        """Add a new product.

        Args:
            name: Product name
            description: Product description
            price: Product price
            stock: Product stock

        Returns:
            int: Product ID
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO products (name, description, price, stock)
                VALUES (?, ?, ?, ?)
                """,
                (name, description, price, stock)
            )
            return cursor.lastrowid

    def get_product(self, product_id: int) -> Optional[Dict[str, Any]]:
        """Get a product by ID.

        Args:
            product_id: Product ID

        Returns:
            Optional[Dict[str, Any]]: Product data if found
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM products WHERE id = ?",
                (product_id,)
            )
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "price": row[3],
                    "stock": row[4],
                    "created_at": row[5]
                }
            return None

    def create_order(
        self,
        customer_id: int,
        product_ids: List[int],
        quantities: List[int]
    ) -> int:
        """Create a new order.

        Args:
            customer_id: Customer ID
            product_ids: List of product IDs
            quantities: List of quantities

        Returns:
            int: Order ID
        """
        with self.connect() as conn:
            cursor = conn.cursor()

            # Verify customer exists
            cursor.execute(
                "SELECT id FROM customers WHERE id = ?",
                (customer_id,)
            )
            if not cursor.fetchone():
                raise ValueError(f"Customer with ID {customer_id} not found")

            # Calculate total amount and verify stock
            total_amount = 0.0
            for product_id, quantity in zip(product_ids, quantities):
                cursor.execute(
                    "SELECT price, stock FROM products WHERE id = ?",
                    (product_id,)
                )
                result = cursor.fetchone()
                if not result:
                    raise ValueError(f"Product with ID {product_id} not found")
                price, stock = result
                if stock < quantity:
                    raise ValueError(f"Insufficient stock for product {product_id}")

                total_amount += price * quantity

            # Create order
            cursor.execute(
                """
                INSERT INTO orders (customer_id, total_amount)
                VALUES (?, ?)
                """,
                (customer_id, total_amount)
            )
            order_id = cursor.lastrowid

            # Add order items and update stock
            for product_id, quantity in zip(product_ids, quantities):
                cursor.execute(
                    """
                    INSERT INTO order_items (order_id, product_id, quantity)
                    VALUES (?, ?, ?)
                    """,
                    (order_id, product_id, quantity)
                )
                cursor.execute(
                    """
                    UPDATE products
                    SET stock = stock - ?
                    WHERE id = ?
                    """,
                    (quantity, product_id)
                )

            return order_id

    def get_order(self, order_id: int) -> Optional[Dict[str, Any]]:
        """Get an order by ID.

        Args:
            order_id: Order ID

        Returns:
            Optional[Dict[str, Any]]: Order data if found
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT o.*, c.name as customer_name
                FROM orders o
                JOIN customers c ON o.customer_id = c.id
                WHERE o.id = ?
                """,
                (order_id,)
            )
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "customer_id": row[1],
                    "customer_name": row[6],
                    "created_at": row[2],
                    "total_amount": row[3],
                    "status": row[4]
                }
            return None

    def display_customers(self) -> None:
        """Display all customers in a formatted table."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()

            if not customers:
                console.print("[yellow]No customers found[/]")
                return

            table = Table(title="Customers")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Email", style="yellow")
            table.add_column("Created At", style="magenta")

            for customer in customers:
                table.add_row(
                    str(customer[0]),
                    customer[1],
                    customer[2],
                    customer[3]
                )

            console.print(table)

    def display_products(self) -> None:
        """Display all products in a formatted table."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            if not products:
                console.print("[yellow]No products found[/]")
                return

            table = Table(title="Products")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Price", style="yellow")
            table.add_column("Stock", style="magenta")

            for product in products:
                table.add_row(
                    str(product[0]),
                    product[1],
                    f"${product[3]:.2f}",
                    str(product[4])
                )

            console.print(table)

    def display_orders(self) -> None:
        """Display all orders in a formatted table."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT o.*, c.name as customer_name
                FROM orders o
                JOIN customers c ON o.customer_id = c.id
                """
            )
            orders = cursor.fetchall()

            if not orders:
                console.print("[yellow]No orders found[/]")
                return

            table = Table(title="Orders")
            table.add_column("ID", style="cyan")
            table.add_column("Customer", style="green")
            table.add_column("Total Amount", style="yellow")
            table.add_column("Status", style="magenta")
            table.add_column("Created At", style="blue")

            for order in orders:
                table.add_row(
                    str(order[0]),
                    order[6],
                    f"${order[3]:.2f}",
                    order[4],
                    order[2]
                )

            console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize SQLite manager
        db = SQLiteManager()

        # Create tables
        print("Creating database tables...")
        db.create_tables()

        # Add customers
        print("\nAdding customers...")
        customer1_id = db.add_customer("John Doe", "john@example.com")
        customer2_id = db.add_customer("Jane Smith", "jane@example.com")
        print(f"Added customers with IDs: {customer1_id}, {customer2_id}")

        # Add products
        print("\nAdding products...")
        product1_id = db.add_product(
            "Laptop",
            "High-performance laptop",
            999.99,
            10
        )
        product2_id = db.add_product(
            "Smartphone",
            "Latest smartphone model",
            699.99,
            15
        )
        print(f"Added products with IDs: {product1_id}, {product2_id}")

        # Create order
        print("\nCreating order...")
        order_id = db.create_order(
            customer1_id,
            [product1_id, product2_id],
            [1, 2]
        )
        print(f"Created order with ID: {order_id}")

        # Display data
        print("\nDisplaying customers:")
        db.display_customers()

        print("\nDisplaying products:")
        db.display_products()

        print("\nDisplaying orders:")
        db.display_orders()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up
        print("\nCleaning up...")
        db.drop_tables() 