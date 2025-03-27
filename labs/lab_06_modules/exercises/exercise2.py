"""
Exercise 2: Working with Packages

This exercise focuses on creating and using Python packages.

Learning objectives:
- Understanding package structure
- Working with __init__.py
- Package importing
- Package documentation
"""

# TODO: Create a package called 'store' with the following structure:
"""
store/
├── __init__.py
├── inventory.py
├── customer.py
└── utils.py

Requirements for each module:

1. inventory.py:
   - Class Product(name: str, price: float, quantity: int)
   - Function add_product()
   - Function remove_product()
   - Function update_quantity()

2. customer.py:
   - Class Customer(name: str, email: str)
   - Function register_customer()
   - Function find_customer()

3. utils.py:
   - Function generate_product_id()
   - Function validate_email()
   - Function calculate_total()

4. __init__.py:
   - Import and expose main classes
   - Define __all__
   - Add package metadata
"""

def test_store_package():
    """
    TODO: Implement this function to test your store package
    
    Requirements:
    1. Import your package modules
    2. Create test products and customers
    3. Test all functionality
    4. Handle errors appropriately
    """
    pass


def main():
    """
    TODO: Implement main function to demonstrate package usage
    
    Suggested demonstrations:
    1. Creating and managing products
    2. Customer registration and lookup
    3. Calculating orders
    4. Error handling
    """
    pass


if __name__ == "__main__":
    main() 