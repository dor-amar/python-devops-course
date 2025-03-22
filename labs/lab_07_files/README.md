# Lab 07: Working with Files

## Objectives
- Understand file operations in Python
- Master different file modes and their use cases
- Learn about file handling best practices
- Practice working with different file formats
- Explore file system operations
- Understand file encoding and text handling

## Prerequisites
- Basic Python programming
- Understanding of file systems
- Familiarity with text encoding concepts

## Exercises

### Exercise 1: Basic File Operations
Create a module `exercises/exercise1.py` with the following tasks:

1. File Reading and Writing:
   - `read_file(filepath: str) -> str`
   - `write_file(filepath: str, content: str) -> None`
   - `append_to_file(filepath: str, content: str) -> None`
   - `read_lines(filepath: str) -> List[str]`

2. File Information:
   - `get_file_info(filepath: str) -> Dict[str, Any]`
   - `check_file_exists(filepath: str) -> bool`
   - `get_file_size(filepath: str) -> int`

3. File Operations:
   - `copy_file(source: str, destination: str) -> None`
   - `move_file(source: str, destination: str) -> None`
   - `delete_file(filepath: str) -> None`

### Exercise 2: Advanced File Handling
Create a module `exercises/exercise2.py` with the following tasks:

1. CSV File Operations:
   - `read_csv(filepath: str) -> List[Dict[str, Any]]`
   - `write_csv(filepath: str, data: List[Dict[str, Any]]) -> None`
   - `append_csv(filepath: str, data: List[Dict[str, Any]]) -> None`

2. JSON File Operations:
   - `read_json(filepath: str) -> Dict[str, Any]`
   - `write_json(filepath: str, data: Dict[str, Any]) -> None`
   - `update_json(filepath: str, updates: Dict[str, Any]) -> None`

3. Binary File Operations:
   - `read_binary(filepath: str) -> bytes`
   - `write_binary(filepath: str, data: bytes) -> None`
   - `append_binary(filepath: str, data: bytes) -> None`

### Exercise 3: File System Operations
Create a module `exercises/exercise3.py` with the following tasks:

1. Directory Operations:
   - `create_directory(path: str) -> None`
   - `list_directory(path: str) -> List[str]`
   - `delete_directory(path: str) -> None`
   - `walk_directory(path: str) -> List[str]`

2. File Search:
   - `find_files(pattern: str, path: str) -> List[str]`
   - `find_by_extension(extension: str, path: str) -> List[str]`
   - `find_by_size(min_size: int, max_size: int, path: str) -> List[str]`

3. File Monitoring:
   - `monitor_file_changes(filepath: str, callback: Callable) -> None`
   - `get_file_hash(filepath: str) -> str`
   - `compare_files(file1: str, file2: str) -> bool`

## Testing
Create test files in the `tests` directory:
- `test_exercise1.py`: Tests for basic file operations
- `test_exercise2.py`: Tests for advanced file handling
- `test_exercise3.py`: Tests for file system operations

Each test file should include:
- Unit tests for all functions
- File system operation tests
- Error handling tests
- Edge case tests

## Requirements
1. File Operations:
   - Proper file handling with context managers
   - Error handling and exceptions
   - File encoding support
   - Resource cleanup

2. File Formats:
   - CSV file handling
   - JSON file handling
   - Binary file handling
   - Text file handling

3. File System:
   - Directory operations
   - File search and filtering
   - File monitoring
   - File comparison

## Submission
Submit the following:
1. All exercise modules
2. Test files
3. Sample data files
4. Documentation

## Grading Criteria
- File Operations Implementation (30%)
- File Format Handling (25%)
- File System Operations (25%)
- Testing and Documentation (20%) 