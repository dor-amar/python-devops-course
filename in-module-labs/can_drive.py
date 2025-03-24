"""Task: Driving Eligibility Checker.

Implement a function to check if someone can drive based on their age and license status.
"""

def can_drive(age: int, has_license: bool) -> bool:
    """Check if someone can drive based on age and license status.
    
    Rules:
    - Must be at least 16 years old
    - Must have a valid driver's license
    
    Args:
        age (int): Person's age
        has_license (bool): Whether they have a valid driver's license
        
    Returns:
        bool: True if they can drive, False otherwise
        
    Raises:
        ValueError: If age is negative
        
    Example:
        >>> can_drive(18, True)
        True
        >>> can_drive(15, True)
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        (18, True),    # Should return True
        (15, True),    # Should return False
        (16, False),   # Should return False
        (25, True),    # Should return True
        (-1, True),    # Should raise ValueError
        (0, False),    # Should return False
        (100, True),   # Should return True
    ]
    
    for age, has_license in test_cases:
        try:
            result = can_drive(age, has_license)
            print(f"Age {age}, Has License: {has_license} -> Can Drive: {result}")
        except Exception as e:
            print(f"Error checking age {age}: {str(e)}")


if __name__ == "__main__":
    main() 