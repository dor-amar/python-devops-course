"""File system operations and utilities module."""

import os
import shutil
from typing import List, Optional, Tuple
from pathlib import Path
from datetime import datetime


def list_directory(path: str = '.') -> List[str]:
    """List all files and directories in the specified path.

    Args:
        path: Directory path to list (default: current directory)

    Returns:
        List[str]: List of file and directory names

    Raises:
        FileNotFoundError: If directory doesn't exist
        NotADirectoryError: If path is not a directory
    """
    try:
        return os.listdir(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory not found: {path}")
    except NotADirectoryError:
        raise NotADirectoryError(f"Path is not a directory: {path}")


def create_directory(path: str, parents: bool = False) -> None:
    """Create a directory and its parent directories if needed.

    Args:
        path: Directory path to create
        parents: Whether to create parent directories (default: False)

    Raises:
        FileExistsError: If directory already exists
        OSError: If there's an error creating the directory
    """
    try:
        os.makedirs(path, exist_ok=parents)
    except FileExistsError:
        if not parents:
            raise FileExistsError(f"Directory already exists: {path}")
    except OSError as e:
        raise OSError(f"Error creating directory: {e}")


def remove_directory(path: str, recursive: bool = False) -> None:
    """Remove a directory and its contents.

    Args:
        path: Directory path to remove
        recursive: Whether to remove directory and all contents (default: False)

    Raises:
        FileNotFoundError: If directory doesn't exist
        OSError: If there's an error removing the directory
    """
    try:
        if recursive:
            shutil.rmtree(path)
        else:
            os.rmdir(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory not found: {path}")
    except OSError as e:
        raise OSError(f"Error removing directory: {e}")


def get_file_info(path: str) -> Tuple[str, int, datetime, datetime]:
    """Get detailed information about a file.

    Args:
        path: Path to the file

    Returns:
        Tuple[str, int, datetime, datetime]: Tuple containing:
            - File type (file/directory)
            - Size in bytes
            - Creation time
            - Last modified time

    Raises:
        FileNotFoundError: If file doesn't exist
        OSError: If there's an error getting file info
    """
    try:
        stat = os.stat(path)
        file_type = 'directory' if os.path.isdir(path) else 'file'
        return (
            file_type,
            stat.st_size,
            datetime.fromtimestamp(stat.st_ctime),
            datetime.fromtimestamp(stat.st_mtime)
        )
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except OSError as e:
        raise OSError(f"Error getting file info: {e}")


def find_files(pattern: str, start_path: str = '.') -> List[str]:
    """Find files matching a pattern in a directory and its subdirectories.

    Args:
        pattern: File pattern to match (e.g., '*.txt')
        start_path: Directory to start search from (default: current directory)

    Returns:
        List[str]: List of matching file paths

    Raises:
        FileNotFoundError: If start directory doesn't exist
        OSError: If there's an error searching for files
    """
    try:
        matches = []
        for root, _, files in os.walk(start_path):
            for file in files:
                if file.endswith(pattern):
                    matches.append(os.path.join(root, file))
        return matches
    except FileNotFoundError:
        raise FileNotFoundError(f"Start directory not found: {start_path}")
    except OSError as e:
        raise OSError(f"Error searching for files: {e}")


def copy_directory(source: str, destination: str) -> None:
    """Copy a directory and its contents to a new location.

    Args:
        source: Source directory path
        destination: Destination directory path

    Raises:
        FileNotFoundError: If source directory doesn't exist
        OSError: If there's an error copying the directory
    """
    try:
        shutil.copytree(source, destination)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source directory not found: {source}")
    except OSError as e:
        raise OSError(f"Error copying directory: {e}")


def move_directory(source: str, destination: str) -> None:
    """Move a directory to a new location.

    Args:
        source: Source directory path
        destination: Destination directory path

    Raises:
        FileNotFoundError: If source directory doesn't exist
        OSError: If there's an error moving the directory
    """
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        raise FileNotFoundError(f"Source directory not found: {source}")
    except OSError as e:
        raise OSError(f"Error moving directory: {e}")


def get_directory_size(path: str) -> int:
    """Calculate the total size of a directory and its contents.

    Args:
        path: Directory path to calculate size for

    Returns:
        int: Total size in bytes

    Raises:
        FileNotFoundError: If directory doesn't exist
        OSError: If there's an error calculating directory size
    """
    try:
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory not found: {path}")
    except OSError as e:
        raise OSError(f"Error calculating directory size: {e}")


def get_directory_tree(path: str, level: int = 0) -> List[str]:
    """Generate a tree-like representation of a directory structure.

    Args:
        path: Directory path to generate tree for
        level: Current indentation level (default: 0)

    Returns:
        List[str]: List of strings representing the directory tree

    Raises:
        FileNotFoundError: If directory doesn't exist
        OSError: If there's an error generating directory tree
    """
    try:
        tree = []
        prefix = '  ' * level + '├── ' if level > 0 else ''
        
        # Add current directory
        tree.append(prefix + os.path.basename(path))
        
        # List contents
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                tree.extend(get_directory_tree(item_path, level + 1))
            else:
                tree.append('  ' * (level + 1) + '├── ' + item)
        
        return tree
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory not found: {path}")
    except OSError as e:
        raise OSError(f"Error generating directory tree: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create test directory structure
        test_dir = "test_dir"
        create_directory(test_dir)
        create_directory(os.path.join(test_dir, "subdir1"))
        create_directory(os.path.join(test_dir, "subdir2"))
        
        # Create some test files
        with open(os.path.join(test_dir, "file1.txt"), "w") as f:
            f.write("Test file 1")
        with open(os.path.join(test_dir, "subdir1", "file2.txt"), "w") as f:
            f.write("Test file 2")
        
        # List directory contents
        print("Directory contents:")
        for item in list_directory(test_dir):
            print(f"  {item}")
        
        # Get file info
        print("\nFile info:")
        info = get_file_info(os.path.join(test_dir, "file1.txt"))
        print(f"  Type: {info[0]}")
        print(f"  Size: {info[1]} bytes")
        print(f"  Created: {info[2]}")
        print(f"  Modified: {info[3]}")
        
        # Find files
        print("\nFinding files:")
        files = find_files(".txt", test_dir)
        for file in files:
            print(f"  {file}")
        
        # Get directory size
        size = get_directory_size(test_dir)
        print(f"\nDirectory size: {size} bytes")
        
        # Generate directory tree
        print("\nDirectory tree:")
        tree = get_directory_tree(test_dir)
        for line in tree:
            print(line)
        
        # Cleanup
        remove_directory(test_dir, recursive=True)
        print("\nCleaned up test directory")
        
    except Exception as e:
        print(f"Error: {e}") 