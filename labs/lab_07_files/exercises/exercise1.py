"""Basic file operations module."""

import os
import shutil
from typing import Any, Dict, List
from pathlib import Path


def read_file(filepath: str) -> str:
    """Read the entire contents of a file.

    Args:
        filepath: Path to the file to read

    Returns:
        str: Contents of the file

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")


def write_file(filepath: str, content: str) -> None:
    """Write content to a file, overwriting if it exists.

    Args:
        filepath: Path to the file to write
        content: Content to write to the file

    Raises:
        IOError: If there's an error writing to the file
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")


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


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists.

    Args:
        filepath: Path to check

    Returns:
        bool: True if file exists, False otherwise
    """
    return os.path.exists(filepath)


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


# Example usage
if __name__ == "__main__":
    try:
        # Test file operations
        test_file = "test.txt"
        content = "Hello, World!\nThis is a test file."
        
        # Write to file
        write_file(test_file, content)
        print(f"Created file: {test_file}")
        
        # Read file
        read_content = read_file(test_file)
        print(f"File contents:\n{read_content}")
        
        # Append to file
        append_to_file(test_file, "\nAppended content")
        print("\nAppended content")
        
        # Get file info
        info = get_file_info(test_file)
        print(f"\nFile info: {info}")
        
        # Copy file
        copy_file(test_file, "test_copy.txt")
        print("\nCopied file to test_copy.txt")
        
        # Move file
        move_file(test_file, "test_moved.txt")
        print("Moved file to test_moved.txt")
        
        # Delete files
        delete_file("test_copy.txt")
        delete_file("test_moved.txt")
        print("\nDeleted test files")
        
    except Exception as e:
        print(f"Error: {e}") 