"""Task: Even Number Checker.

Implement a function to check if a number is even, with proper error handling.
"""

def is_even(number: int) -> bool:
    """Check if a number is even.
    
    Args:
        number (int): Number to check
        
    Returns:
        bool: True if number is even, False if odd
        
    Raises:
        TypeError: If input is not an integer
        
    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        4,      # Should return True
        7,      # Should return False
        0,      # Should return True
        -2,     # Should return True
        -3,     # Should return False
        2.5,    # Should raise TypeError
        "4",    # Should raise TypeError
        None,   # Should raise TypeError
    ]
    
    for number in test_cases:
        try:
            result = is_even(number)
            print(f"{number} is {'even' if result else 'odd'}")
        except Exception as e:
            print(f"Error checking {number}: {str(e)}")


if __name__ == "__main__":
    main() 