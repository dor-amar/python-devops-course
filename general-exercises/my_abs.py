"""Task: Absolute Value Function.

Implement a function to calculate the absolute value of a number.
"""

def my_abs(number: float) -> float:
    """Calculate the absolute value of a number.
    
    Args:
        number (float): Number to calculate absolute value for
        
    Returns:
        float: Absolute value of the number
        
    Raises:
        TypeError: If input is not a number
        
    Example:
        >>> my_abs(-5)
        5.0
        >>> my_abs(3.14)
        3.14
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        -5,        # Should return 5.0
        3.14,      # Should return 3.14
        0,         # Should return 0.0
        -2.5,      # Should return 2.5
        "5",       # Should raise TypeError
        None,      # Should raise TypeError
        True,      # Should raise TypeError
    ]
    
    for number in test_cases:
        try:
            result = my_abs(number)
            print(f"|{number}| = {result}")
        except Exception as e:
            print(f"Error calculating absolute value of {number}: {str(e)}")


if __name__ == "__main__":
    main() 