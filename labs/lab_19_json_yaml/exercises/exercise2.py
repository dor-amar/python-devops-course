"""
Exercise 2: JSON File Operations

Practice reading from and writing to JSON files.

TODO:
1. Create functions to read JSON from a file
2. Create functions to write JSON to a file
3. Handle file paths correctly
4. Implement error handling for file operations
5. Add support for different file encodings
"""

def read_json_file(filepath: str) -> dict:
    """
    TODO: Read JSON data from a file
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary containing the JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    pass

def write_json_file(data: dict, filepath: str, indent: int = 4) -> bool:
    """
    TODO: Write dictionary data to a JSON file
    
    Args:
        data: Dictionary to write
        filepath: Path to save the file
        indent: Number of spaces for indentation
        
    Returns:
        True if successful, False otherwise
        
    Raises:
        IOError: If writing fails
    """
    pass

def main():
    """
    Test your implementation:
    1. Create sample data
    2. Write it to a file
    3. Read it back
    4. Verify the data matches
    """
    pass

if __name__ == "__main__":
    main() 