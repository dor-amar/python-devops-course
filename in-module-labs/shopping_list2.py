"""Task: Enhanced Shopping List Manager.

Implement a function to manage a shopping list with categories and quantities.
"""

def shopping_list2(items: list, operation: str, item: str, category: str, quantity: int = 1) -> list:
    """Manage a shopping list with categories and quantities.
    
    Operations:
    - 'add': Add an item with category and quantity
    - 'remove': Remove an item completely
    - 'update': Update quantity of an existing item
    
    Args:
        items (list): Current shopping list as list of tuples (item, category, quantity)
        operation (str): Operation to perform ('add', 'remove', 'update')
        item (str): Item to operate on
        category (str): Category of the item
        quantity (int): Quantity for add/update operations
        
    Returns:
        list: Updated shopping list
        
    Raises:
        ValueError: If operation is invalid or quantity is negative
        
    Example:
        >>> shopping_list2([], 'add', 'apple', 'fruits', 2)
        [('apple', 'fruits', 2)]
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ([], 'add', 'apple', 'fruits', 2),                    # Should add apple
        ([('apple', 'fruits', 2)], 'add', 'banana', 'fruits', 3),  # Should add banana
        ([('apple', 'fruits', 2), ('banana', 'fruits', 3)], 'remove', 'apple', 'fruits'),  # Should remove apple
        ([('banana', 'fruits', 3)], 'update', 'banana', 'fruits', 5),  # Should update banana quantity
        ([('banana', 'fruits', 5)], 'add', 'milk', 'dairy', -1),     # Should raise ValueError
        ([('banana', 'fruits', 5)], 'invalid', 'apple', 'fruits'),   # Should raise ValueError
        ([('apple', 'fruits', 2)], 'add', 'apple', 'fruits', 3),     # Should update existing item
    ]
    
    current_list = []
    for items, op, item, category, *args in test_cases:
        try:
            quantity = args[0] if args else None
            if quantity is not None:
                current_list = shopping_list2(items, op, item, category, quantity)
            else:
                current_list = shopping_list2(items, op, item, category)
            print(f"After {op} '{item}' ({category}): {current_list}")
        except Exception as e:
            print(f"Error performing {op} on '{item}' ({category}): {str(e)}")


if __name__ == "__main__":
    main() 