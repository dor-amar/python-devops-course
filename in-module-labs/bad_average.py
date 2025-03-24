"""Task: Fix the average calculation function.

The function below has a bug in calculating the average. Fix it and add proper error handling.
"""

def bad_average(numbers: list) -> float:
    """Calculate the average of a list of numbers.
    
    Args:
        numbers (list): List of numbers to calculate average from
        
    Returns:
        float: The average of the numbers
        
    Raises:
        ValueError: If the input list is empty
        
    Example:
        >>> bad_average([1, 2, 3, 4, 5])
        3.0
    """
    # TODO: Fix the bug in this function
    # Current implementation has issues with:
    # 1. Empty list handling
    # 2. Division by zero
    # 3. Type checking
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [0, 0, 0],
        [1.5, 2.5, 3.5],
        []  # This should raise a ValueError
    ]
    
    for numbers in test_cases:
        try:
            result = bad_average(numbers)
            print(f"Average of {numbers} is: {result}")
        except Exception as e:
            print(f"Error calculating average for {numbers}: {str(e)}")


if __name__ == "__main__":
    main() 