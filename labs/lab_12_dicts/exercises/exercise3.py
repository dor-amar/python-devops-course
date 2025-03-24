"""Exercise 3: Advanced Dictionary Applications.

In this exercise, you will work on practical applications of dictionaries. You will learn how to:
1. Create an interactive phone book application
2. Find duplicate values in dictionaries
3. Group data by key
4. Create nested dictionary structures
"""

def create_phone_book() -> dict:
    """Create a phone book with basic operations.
    
    TODO: Implement this function to create an interactive phone book with the following features:
    1. Add new contacts (name and phone number)
    2. Look up contacts by name
    3. Delete contacts
    4. List all contacts
    5. Exit option
    
    The function should:
    - Keep running until the user chooses to exit
    - Handle invalid inputs gracefully
    - Print appropriate messages for each operation
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


def find_duplicate_values(d: dict) -> list:
    """Find values that appear multiple times in a dictionary.
    
    TODO: Implement this function to:
    1. Create a dictionary mapping values to lists of keys
    2. Find all values that have more than one key
    3. Return a list of tuples containing (value, [keys])
    
    Example:
        Input: {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
        Output: [(1, ["a", "c"]), (2, ["b", "e"])]
    """
    value_to_keys = {}
    for key, value in d.items():
        if value not in value_to_keys:
            value_to_keys[value] = []
        value_to_keys[value].append(key)
    
    return [(value, keys) for value, keys in value_to_keys.items() if len(keys) > 1]


def group_by_key(items: list, key: str) -> dict:
    """Group items by a specified key.
    
    TODO: Implement this function to:
    1. Create a dictionary where keys are unique values from the specified key
    2. Group all items that share the same value for the specified key
    3. Return the grouped dictionary
    
    Example:
        Input: items=[{"name": "John", "age": 20}, {"name": "Jane", "age": 20}], key="age"
        Output: {20: [{"name": "John", "age": 20}, {"name": "Jane", "age": 20}]}
    """
    grouped = {}
    for item in items:
        value = item[key]
        if value not in grouped:
            grouped[value] = []
        grouped[value].append(item)
    return grouped


def create_nested_structure(data: list) -> dict:
    """Create a nested dictionary structure from flat data.
    
    TODO: Implement this function to:
    1. Create a nested dictionary structure from a list of (category, subcategory, value) tuples
    2. Group items by category
    3. Create subcategories within each category
    
    Example:
        Input: [("fruits", "apple", "red"), ("fruits", "banana", "yellow")]
        Output: {"fruits": {"apple": "red", "banana": "yellow"}}
    """
    nested = {}
    for category, subcategory, value in data:
        if category not in nested:
            nested[category] = {}
        nested[category][subcategory] = value
    return nested


def main():
    """Test your implementations here."""
    # Test phone book
    print("\nTesting Phone Book:")
    phone_book = create_phone_book()
    
    # Test duplicate values
    d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    duplicates = find_duplicate_values(d)
    print(f"\nDuplicate values: {duplicates}")
    
    # Test grouping
    items = [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 20},
        {"name": "Bob", "age": 25}
    ]
    grouped = group_by_key(items, "age")
    print(f"\nGrouped by age: {grouped}")
    
    # Test nested structure
    data = [
        ("fruits", "apple", "red"),
        ("fruits", "banana", "yellow"),
        ("vegetables", "carrot", "orange")
    ]
    nested = create_nested_structure(data)
    print(f"\nNested structure: {nested}")


if __name__ == "__main__":
    main() 