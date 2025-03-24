"""Task: Digit Counter.

Implement a function to count the number of digits in a number.
"""

def num_of_digits(number: int) -> int:
    """Count the number of digits in a number.
    
    Args:
        number (int): Number to count digits in
        
    Returns:
        int: Number of digits
        
    Raises:
        ValueError: If input is negative
        
    Example:
        >>> num_of_digits(123)
        3
        >>> num_of_digits(0)
        1
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        123,      # Should return 3
        0,        # Should return 1
        1000,     # Should return 4
        999,      # Should return 3
        -123,     # Should raise ValueError
        1,        # Should return 1
        999999,   # Should return 6
    ]
    
    for number in test_cases:
        try:
            count = num_of_digits(number)
            print(f"Number: {number}")
            print(f"Number of digits: {count}\n")
        except Exception as e:
            print(f"Error processing {number}: {str(e)}\n")


if __name__ == "__main__":
    main() 