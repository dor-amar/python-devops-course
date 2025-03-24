"""Task: Fix the Buggy Function.

The function below has several bugs that need to be fixed:
1. It doesn't handle empty lists
2. It doesn't handle non-numeric values
3. It doesn't handle negative numbers
4. It has a logic error in the calculation
"""

def bad_function(numbers: list) -> float:
    """Calculate the sum of squares of positive numbers in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Sum of squares of positive numbers
        
    Raises:
        ValueError: If input is empty or contains non-numeric values
        
    Example:
        >>> bad_function([1, 2, 3])
        14  # 1² + 2² + 3² = 1 + 4 + 9 = 14
    """
    # TODO: Fix the bugs in this function
    # Current implementation has issues with:
    # 1. Empty list handling
    # 2. Type checking
    # 3. Negative number handling
    # 4. Calculation logic
    result = 0
    for num in numbers:
        result += num * num
    return result


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        [1, 2, 3],           # Should return 14
        [-1, 2, -3, 4],      # Should return 20 (only 2² + 4²)
        [1.5, 2.5],          # Should return 8.5
        [],                  # Should raise ValueError
        [1, "2", 3],         # Should raise ValueError
        [1, None, 3],        # Should raise ValueError
    ]
    
    for numbers in test_cases:
        try:
            result = bad_function(numbers)
            print(f"Input: {numbers} -> Result: {result}")
        except Exception as e:
            print(f"Error for input {numbers}: {str(e)}")


if __name__ == "__main__":
    main() 