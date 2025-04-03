"""
Exercise 1: Basic JSON Operations

Practice basic JSON serialization and deserialization operations.

TODO:
1. Create a function that converts a Python dictionary to JSON string
2. Create a function that converts a JSON string back to Python dictionary
3. Handle different data types (strings, numbers, booleans, lists, nested dictionaries)
4. Implement proper error handling
5. Add pretty printing with indentation
"""

def dict_to_json(data: dict) -> str:
    """
    TODO: Convert a Python dictionary to a JSON string
    
    Args:
        data: Dictionary to convert
        
    Returns:
        JSON formatted string
        
    Raises:
        TypeError: If input is not serializable
    """
    pass

def json_to_dict(json_str: str) -> dict:
    """
    TODO: Convert a JSON string to a Python dictionary
    
    Args:
        json_str: JSON string to convert
        
    Returns:
        Python dictionary
        
    Raises:
        json.JSONDecodeError: If JSON is invalid
    """
    pass

def main():
    """
    Test your implementation with different data types:
    - Simple key-value pairs
    - Nested dictionaries
    - Lists
    - Different data types (int, float, bool, None)
    """
    pass

if __name__ == "__main__":
    main() 