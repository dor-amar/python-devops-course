"""Exercise 1: Basic Error Handling.

In this exercise, you will work with try-except blocks and error handling in Python.
"""

def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers with error handling.
    
    TODO: Implement this function to:
    1. Take two numbers as input
    2. Handle division by zero error
    3. Return the result of division
    
    Example:
        Input: 10, 2 -> Output: 5.0
        Input: 10, 0 -> Output: "Error: Cannot divide by zero"
    """
    # Your code here
    pass


def read_file(filename: str) -> str:
    """Read a file with error handling.
    
    TODO: Implement this function to:
    1. Take a filename as input
    2. Handle file not found error
    3. Return the file contents
    
    Example:
        Input: "existing.txt" -> Output: file contents
        Input: "nonexistent.txt" -> Output: "Error: File not found"
    """
    # Your code here
    pass


def convert_to_int(value: str) -> int:
    """Convert string to integer with error handling.
    
    TODO: Implement this function to:
    1. Take a string as input
    2. Handle ValueError for invalid string
    3. Return the integer value
    
    Example:
        Input: "123" -> Output: 123
        Input: "abc" -> Output: "Error: Invalid integer"
    """
    # Your code here
    pass


def main():
    """Test your implementations here."""
    # Test divide_numbers
    print("Testing divide_numbers:")
    print(f"Input: 10, 2 -> Output: {divide_numbers(10, 2)}")
    print(f"Input: 10, 0 -> Output: {divide_numbers(10, 0)}")
    
    # Test read_file
    print("\nTesting read_file:")
    print(f"Input: 'test.txt' -> Output: {read_file('test.txt')}")
    print(f"Input: 'nonexistent.txt' -> Output: {read_file('nonexistent.txt')}")
    
    # Test convert_to_int
    print("\nTesting convert_to_int:")
    print(f"Input: '123' -> Output: {convert_to_int('123')}")
    print(f"Input: 'abc' -> Output: {convert_to_int('abc')}")


if __name__ == "__main__":
    main() 