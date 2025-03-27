"""
Exercise 3: CSV File Handling

Practice working with CSV files in Python.

TODO:
1. Implement functions to read and write CSV files
2. Handle different CSV formats
3. Process CSV data
"""

from typing import List, Dict

def read_csv(filepath: str) -> List[Dict]:
    """
    TODO: Implement function to read a CSV file and return data as list of dictionaries
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        List of dictionaries where each dictionary represents a row
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the CSV format is invalid
    """
    pass

def write_csv(filepath: str, data: List[Dict]) -> bool:
    """
    TODO: Implement function to write data to a CSV file
    
    Args:
        filepath: Path to the CSV file to write
        data: List of dictionaries to write to CSV
        
    Returns:
        True if write was successful, False otherwise
        
    Raises:
        IOError: If there's an error writing to the file
    """
    pass

def filter_csv(filepath: str, column: str, value: str) -> List[Dict]:
    """
    TODO: Implement function to filter CSV data based on column value
    
    Args:
        filepath: Path to the CSV file
        column: Column name to filter on
        value: Value to filter by
        
    Returns:
        List of dictionaries containing filtered data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        KeyError: If the column doesn't exist
    """
    pass

def main():
    """Test your CSV handling implementation."""
    # TODO: Add test cases for your functions
    pass

if __name__ == "__main__":
    main() 