"""Task: Advanced Calculator with Additional Operations.

Implement a calculator that can perform advanced arithmetic operations including power, square root, and percentage.
"""

def calculator2(operation: str, num1: float, num2: float = None) -> float:
    """Perform advanced arithmetic operations with error handling.
    
    Args:
        operation (str): The operation to perform ('+', '-', '*', '/', 'pow', 'sqrt', '%')
        num1 (float): First number
        num2 (float, optional): Second number (not needed for sqrt)
        
    Returns:
        float: Result of the operation
        
    Raises:
        ValueError: If operation is not supported or invalid input
        ZeroDivisionError: If attempting to divide by zero
        TypeError: If operation requires two numbers but only one provided
        
    Example:
        >>> calculator2('pow', 2, 3)
        8.0
        >>> calculator2('sqrt', 16)
        4.0
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ('pow', 2, 3),
        ('sqrt', 16),
        ('%', 50, 10),
        ('+', 5, 3),
        ('sqrt', -4),  # Should raise ValueError
        ('pow', 2),    # Should raise TypeError
        ('%', 10, 0),  # Should raise ZeroDivisionError
    ]
    
    for case in test_cases:
        try:
            if len(case) == 2:
                result = calculator2(case[0], case[1])
                print(f"{case[0]}({case[1]}) = {result}")
            else:
                result = calculator2(case[0], case[1], case[2])
                print(f"{case[1]} {case[0]} {case[2]} = {result}")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 