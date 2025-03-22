"""Database operations module using SQLAlchemy."""

import os
from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


# Create declarative base
Base = declarative_base()


# Association table for many-to-many relationships
order_items = Table(
    'order_items',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('quantity', Integer)
)


class Customer(Base):
    """Customer model."""

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    orders = relationship('Order', back_populates='customer')

    def __repr__(self) -> str:
        """String representation of the customer."""
        return f"<Customer(name='{self.name}', email='{self.email}')>"


class Product(Base):
    """Product model."""

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    orders = relationship('Order', secondary=order_items, back_populates='products')

    def __repr__(self) -> str:
        """String representation of the product."""
        return f"<Product(name='{self.name}', price={self.price})>"


class Order(Base):
    """Order model."""

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, default=0.0)
    status = Column(String(20), default='pending')
    customer = relationship('Customer', back_populates='orders')
    products = relationship('Product', secondary=order_items, back_populates='orders')

    def __repr__(self) -> str:
        """String representation of the order."""
        return f"<Order(id={self.id}, total_amount={self.total_amount})>"


class DatabaseManager:
    """Manager for database operations."""

    def __init__(self, connection_string: Optional[str] = None):
        """Initialize the database manager.

        Args:
            connection_string: Database connection string
        """
        self.connection_string = connection_string or os.getenv(
            'DATABASE_URL',
            'postgresql://user:password@localhost:5432/dbname'
        )
        self.engine = create_engine(
            self.connection_string,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10
        )
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def create_tables(self) -> None:
        """Create all database tables."""
        Base.metadata.create_all(self.engine)

    def drop_tables(self) -> None:
        """Drop all database tables."""
        Base.metadata.drop_all(self.engine)

    @contextmanager
    def session(self):
        """Context manager for database sessions.

        Yields:
            Session: Database session
        """
        session = self.Session()
        try:
            yield session
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def add_customer(self, name: str, email: str) -> Customer:
        """Add a new customer.

        Args:
            name: Customer name
            email: Customer email

        Returns:
            Customer: Created customer
        """
        with self.session() as session:
            customer = Customer(name=name, email=email)
            session.add(customer)
            session.flush()
            return customer

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        """Get a customer by ID.

        Args:
            customer_id: Customer ID

        Returns:
            Optional[Customer]: Customer if found
        """
        with self.session() as session:
            return session.query(Customer).get(customer_id)

    def add_product(self, name: str, description: str, price: float, stock: int) -> Product:
        """Add a new product.

        Args:
            name: Product name
            description: Product description
            price: Product price
            stock: Product stock

        Returns:
            Product: Created product
        """
        with self.session() as session:
            product = Product(
                name=name,
                description=description,
                price=price,
                stock=stock
            )
            session.add(product)
            session.flush()
            return product

    def get_product(self, product_id: int) -> Optional[Product]:
        """Get a product by ID.

        Args:
            product_id: Product ID

        Returns:
            Optional[Product]: Product if found
        """
        with self.session() as session:
            return session.query(Product).get(product_id)

    def create_order(
        self,
        customer_id: int,
        product_ids: List[int],
        quantities: List[int]
    ) -> Order:
        """Create a new order.

        Args:
            customer_id: Customer ID
            product_ids: List of product IDs
            quantities: List of quantities

        Returns:
            Order: Created order
        """
        with self.session() as session:
            # Get customer
            customer = session.query(Customer).get(customer_id)
            if not customer:
                raise ValueError(f"Customer with ID {customer_id} not found")

            # Create order
            order = Order(customer_id=customer_id)
            session.add(order)
            session.flush()

            # Add products to order
            total_amount = 0.0
            for product_id, quantity in zip(product_ids, quantities):
                product = session.query(Product).get(product_id)
                if not product:
                    raise ValueError(f"Product with ID {product_id} not found")
                if product.stock < quantity:
                    raise ValueError(f"Insufficient stock for product {product.name}")

                # Update product stock
                product.stock -= quantity
                total_amount += product.price * quantity

                # Add to order items
                order.products.append(product)

            order.total_amount = total_amount
            return order

    def get_order(self, order_id: int) -> Optional[Order]:
        """Get an order by ID.

        Args:
            order_id: Order ID

        Returns:
            Optional[Order]: Order if found
        """
        with self.session() as session:
            return session.query(Order).get(order_id)

    def display_customers(self) -> None:
        """Display all customers in a formatted table."""
        with self.session() as session:
            customers = session.query(Customer).all()
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
                    str(customer.id),
                    customer.name,
                    customer.email,
                    customer.created_at.isoformat()
                )

            console.print(table)

    def display_products(self) -> None:
        """Display all products in a formatted table."""
        with self.session() as session:
            products = session.query(Product).all()
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
                    str(product.id),
                    product.name,
                    f"${product.price:.2f}",
                    str(product.stock)
                )

            console.print(table)

    def display_orders(self) -> None:
        """Display all orders in a formatted table."""
        with self.session() as session:
            orders = session.query(Order).all()
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
                    str(order.id),
                    order.customer.name,
                    f"${order.total_amount:.2f}",
                    order.status,
                    order.created_at.isoformat()
                )

            console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize database manager
        db = DatabaseManager()

        # Create tables
        print("Creating database tables...")
        db.create_tables()

        # Add customers
        print("\nAdding customers...")
        customer1 = db.add_customer("John Doe", "john@example.com")
        customer2 = db.add_customer("Jane Smith", "jane@example.com")
        print(f"Added customers: {customer1}, {customer2}")

        # Add products
        print("\nAdding products...")
        product1 = db.add_product(
            "Laptop",
            "High-performance laptop",
            999.99,
            10
        )
        product2 = db.add_product(
            "Smartphone",
            "Latest smartphone model",
            699.99,
            15
        )
        print(f"Added products: {product1}, {product2}")

        # Create order
        print("\nCreating order...")
        order = db.create_order(
            customer1.id,
            [product1.id, product2.id],
            [1, 2]
        )
        print(f"Created order: {order}")

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