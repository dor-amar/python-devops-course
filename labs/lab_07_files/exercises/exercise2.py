"""Advanced file handling module for CSV, JSON, and binary operations."""

import csv
import json
from typing import Any, Dict, List
from pathlib import Path


def read_csv(filepath: str) -> List[Dict[str, Any]]:
    """Read data from a CSV file.

    Args:
        filepath: Path to the CSV file

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing CSV data

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading CSV file: {e}")


def write_csv(filepath: str, data: List[Dict[str, Any]]) -> None:
    """Write data to a CSV file.

    Args:
        filepath: Path to write the CSV file
        data: List of dictionaries to write

    Raises:
        IOError: If there's an error writing to the file
    """
    if not data:
        raise ValueError("No data provided to write")
    
    try:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        raise IOError(f"Error writing CSV file: {e}")


def append_csv(filepath: str, data: List[Dict[str, Any]]) -> None:
    """Append data to an existing CSV file.

    Args:
        filepath: Path to the CSV file to append to
        data: List of dictionaries to append

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If there's an error appending to the file
    """
    if not data:
        raise ValueError("No data provided to append")
    
    try:
        # Read existing headers if file exists
        fieldnames = data[0].keys()
        if Path(filepath).exists():
            with open(filepath, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or fieldnames
        
        with open(filepath, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not Path(filepath).exists():
                writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error appending to CSV file: {e}")


def read_json(filepath: str) -> Dict[str, Any]:
    """Read data from a JSON file.

    Args:
        filepath: Path to the JSON file

    Returns:
        Dict[str, Any]: Dictionary containing JSON data

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is invalid
        IOError: If there's an error reading the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file: {e}", e.doc, e.pos)
    except IOError as e:
        raise IOError(f"Error reading JSON file: {e}")


def write_json(filepath: str, data: Dict[str, Any]) -> None:
    """Write data to a JSON file.

    Args:
        filepath: Path to write the JSON file
        data: Dictionary to write as JSON

    Raises:
        IOError: If there's an error writing to the file
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        raise IOError(f"Error writing JSON file: {e}")


def update_json(filepath: str, updates: Dict[str, Any]) -> None:
    """Update existing JSON file with new data.

    Args:
        filepath: Path to the JSON file to update
        updates: Dictionary containing updates to apply

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is invalid
        IOError: If there's an error updating the file
    """
    try:
        # Read existing data
        data = read_json(filepath)
        
        # Update with new data
        data.update(updates)
        
        # Write back to file
        write_json(filepath, data)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file: {e}", e.doc, e.pos)
    except IOError as e:
        raise IOError(f"Error updating JSON file: {e}")


def read_binary(filepath: str) -> bytes:
    """Read binary data from a file.

    Args:
        filepath: Path to the binary file

    Returns:
        bytes: Binary data from the file

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading binary file: {e}")


def write_binary(filepath: str, data: bytes) -> None:
    """Write binary data to a file.

    Args:
        filepath: Path to write the binary file
        data: Binary data to write

    Raises:
        IOError: If there's an error writing to the file
    """
    try:
        with open(filepath, 'wb') as f:
            f.write(data)
    except IOError as e:
        raise IOError(f"Error writing binary file: {e}")


def append_binary(filepath: str, data: bytes) -> None:
    """Append binary data to an existing file.

    Args:
        filepath: Path to the binary file to append to
        data: Binary data to append

    Raises:
        IOError: If there's an error appending to the file
    """
    try:
        with open(filepath, 'ab') as f:
            f.write(data)
    except IOError as e:
        raise IOError(f"Error appending to binary file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Test CSV operations
        csv_data = [
            {'name': 'John', 'age': 30},
            {'name': 'Jane', 'age': 25}
        ]
        write_csv('test.csv', csv_data)
        print("Created test.csv")
        
        read_data = read_csv('test.csv')
        print(f"CSV data: {read_data}")
        
        # Test JSON operations
        json_data = {
            'name': 'Test',
            'values': [1, 2, 3],
            'nested': {'key': 'value'}
        }
        write_json('test.json', json_data)
        print("\nCreated test.json")
        
        read_json_data = read_json('test.json')
        print(f"JSON data: {read_json_data}")
        
        # Test binary operations
        binary_data = b'Hello, Binary World!'
        write_binary('test.bin', binary_data)
        print("\nCreated test.bin")
        
        read_binary_data = read_binary('test.bin')
        print(f"Binary data: {read_binary_data}")
        
        # Cleanup
        import os
        os.remove('test.csv')
        os.remove('test.json')
        os.remove('test.bin')
        print("\nCleaned up test files")
        
    except Exception as e:
        print(f"Error: {e}") 