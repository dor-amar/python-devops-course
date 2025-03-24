"""Task: Basic Calculator with Error Handling.

Implement a calculator that can perform basic arithmetic operations with proper error handling.
"""

def calculator1(operation: str, num1: float, num2: float) -> float:
    """Perform basic arithmetic operations with error handling.
    
    Args:
        operation (str): The operation to perform ('+', '-', '*', '/')
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: Result of the operation
        
    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If attempting to divide by zero
        
    Example:
        >>> calculator1('+', 5, 3)
        8.0
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ('+', 5, 3),
        ('-', 10, 4),
        ('*', 6, 7),
        ('/', 15, 3),
        ('/', 10, 0),  # Should raise ZeroDivisionError
        ('%', 10, 3),  # Should raise ValueError
    ]
    
    for op, n1, n2 in test_cases:
        try:
            result = calculator1(op, n1, n2)
            print(f"{n1} {op} {n2} = {result}")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 