"""
Exercise 1: Basic File Operations

Practice basic file operations in Python including reading, writing, and checking file existence.

TODO:
1. Implement the following functions to handle basic file operations
2. Add proper error handling for file operations
3. Test your implementation with different file types
"""

import os
import shutil
from typing import Any, Dict, List
from pathlib import Path


def read_file(filepath: str) -> str:
    """
    TODO: Implement function to read and return the contents of a file
    
    Args:
        filepath: Path to the file to read
        
    Returns:
        Contents of the file as a string
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    pass


def write_file(filepath: str, content: str) -> bool:
    """
    TODO: Implement function to write content to a file
    
    Args:
        filepath: Path to the file to write
        content: Content to write to the file
        
    Returns:
        True if write was successful, False otherwise
        
    Raises:
        IOError: If there's an error writing to the file
    """
    pass


def append_to_file(filepath: str, content: str) -> None:
    """Append content to the end of a file.

    Args:
        filepath: Path to the file to append to
        content: Content to append to the file

    Raises:
        IOError: If there's an error appending to the file
    """



def read_lines(filepath: str) -> List[str]:
    """Read a file line by line.

    Args:
        filepath: Path to the file to read

    Returns:
        List[str]: List of lines from the file

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If there's an error reading the file
    """




def main():
    """Test your file operations implementation."""
    # TODO: Add test cases for your functions
    pass


if __name__ == "__main__":
    main() 