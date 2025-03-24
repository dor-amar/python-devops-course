"""Solution for Exercise 3: Advanced Dictionary Applications."""

from typing import Any, Dict, List, Tuple


def create_phone_book() -> Dict[str, str]:
    """Create a phone book with basic operations.
    
    Returns:
        Dictionary representing phone book
    """
    phone_book = {}
    while True:
        print("\nPhone Book Operations:")
        print("1. Add contact")
        print("2. Look up contact")
        print("3. Delete contact")
        print("4. List all contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phone_book[name] = phone
            print(f"Added {name}: {phone}")
            
        elif choice == "2":
            name = input("Enter name to look up: ")
            if name in phone_book:
                print(f"{name}: {phone_book[name]}")
            else:
                print("Contact not found")
                
        elif choice == "3":
            name = input("Enter name to delete: ")
            if name in phone_book:
                del phone_book[name]
                print(f"Deleted {name}")
            else:
                print("Contact not found")
                
        elif choice == "4":
            if phone_book:
                print("\nContacts:")
                for name, phone in phone_book.items():
                    print(f"{name}: {phone}")
            else:
                print("Phone book is empty")
                
        elif choice == "5":
            break
            
        else:
            print("Invalid choice")
    
    return phone_book


def find_duplicate_values(d: Dict[str, Any]) -> List[Tuple[Any, List[str]]]:
    """Find values that appear multiple times in a dictionary.
    
    Args:
        d: Dictionary to analyze
        
    Returns:
        List of tuples containing duplicate values and their keys
    """
    value_to_keys = {}
    for key, value in d.items():
        if value not in value_to_keys:
            value_to_keys[value] = []
        value_to_keys[value].append(key)
    
    return [(value, keys) for value, keys in value_to_keys.items() if len(keys) > 1]


def group_by_key(items: List[Dict[str, Any]], key: str) -> Dict[Any, List[Dict[str, Any]]]:
    """Group items by a specified key.
    
    Args:
        items: List of dictionaries to group
        key: Key to group by
        
    Returns:
        Dictionary mapping key values to lists of items
    """
    grouped = {}
    for item in items:
        value = item[key]
        if value not in grouped:
            grouped[value] = []
        grouped[value].append(item)
    return grouped


def create_nested_structure(data: List[Tuple[str, str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Create a nested dictionary structure from flat data.
    
    Args:
        data: List of (category, subcategory, value) tuples
        
    Returns:
        Nested dictionary structure
    """
    nested = {}
    for category, subcategory, value in data:
        if category not in nested:
            nested[category] = {}
        nested[category][subcategory] = value
    return nested 