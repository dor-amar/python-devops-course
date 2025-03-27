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
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Error appending to file: {e}")


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
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")


def get_file_info(filepath: str) -> Dict[str, Any]:
    """Get information about a file.

    Args:
        filepath: Path to the file

    Returns:
        Dict[str, Any]: Dictionary containing file information

    Raises:
        FileNotFoundError: If file doesn't exist
        OSError: If there's an error getting file info
    """
    try:
        stat = os.stat(filepath)
        return {
            'size': stat.st_size,
            'created': stat.st_ctime,
            'modified': stat.st_mtime,
            'accessed': stat.st_atime,
            'is_file': os.path.isfile(filepath),
            'is_directory': os.path.isdir(filepath)
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except OSError as e:
        raise OSError(f"Error getting file info: {e}")


def file_exists(filepath: str) -> bool:
    """
    TODO: Implement function to check if a file exists
    
    Args:
        filepath: Path to the file to check
        
    Returns:
        True if file exists, False otherwise
    """
    pass


def get_file_size(filepath: str) -> int:
    """Get the size of a file in bytes.

    Args:
        filepath: Path to the file

    Returns:
        int: Size of the file in bytes

    Raises:
        FileNotFoundError: If file doesn't exist
        OSError: If there's an error getting file size
    """
    try:
        return os.path.getsize(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except OSError as e:
        raise OSError(f"Error getting file size: {e}")


def copy_file(source: str, destination: str) -> None:
    """Copy a file from source to destination.

    Args:
        source: Source file path
        destination: Destination file path

    Raises:
        FileNotFoundError: If source file doesn't exist
        IOError: If there's an error copying the file
    """
    try:
        shutil.copy2(source, destination)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {source}")
    except IOError as e:
        raise IOError(f"Error copying file: {e}")


def move_file(source: str, destination: str) -> None:
    """Move a file from source to destination.

    Args:
        source: Source file path
        destination: Destination file path

    Raises:
        FileNotFoundError: If source file doesn't exist
        IOError: If there's an error moving the file
    """
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source file not found: {source}")
    except IOError as e:
        raise IOError(f"Error moving file: {e}")


def delete_file(filepath: str) -> None:
    """Delete a file.

    Args:
        filepath: Path to the file to delete

    Raises:
        FileNotFoundError: If file doesn't exist
        OSError: If there's an error deleting the file
    """
    try:
        os.remove(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except OSError as e:
        raise OSError(f"Error deleting file: {e}")


def main():
    """Test your file operations implementation."""
    # TODO: Add test cases for your functions
    pass


if __name__ == "__main__":
    main() 