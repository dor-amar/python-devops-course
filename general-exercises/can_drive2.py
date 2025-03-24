"""Task: Enhanced Driving Eligibility Checker.

Implement a function to check if someone can drive based on age, license status, and additional conditions.
"""

def can_drive2(age: int, has_license: bool, has_insurance: bool, is_sober: bool) -> bool:
    """Check if someone can drive based on multiple conditions.
    
    Rules:
    - Must be at least 16 years old
    - Must have a valid driver's license
    - Must have valid insurance
    - Must be sober
    
    Args:
        age (int): Person's age
        has_license (bool): Whether they have a valid driver's license
        has_insurance (bool): Whether they have valid insurance
        is_sober (bool): Whether they are sober
        
    Returns:
        bool: True if they can drive, False otherwise
        
    Raises:
        ValueError: If age is negative
        
    Example:
        >>> can_drive2(18, True, True, True)
        True
        >>> can_drive2(16, True, False, True)
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        (18, True, True, True),     # Should return True
        (16, True, False, True),    # Should return False
        (25, True, True, False),    # Should return False
        (15, True, True, True),     # Should return False
        (-1, True, True, True),     # Should raise ValueError
        (30, False, True, True),    # Should return False
        (20, True, True, True),     # Should return True
    ]
    
    for age, has_license, has_insurance, is_sober in test_cases:
        try:
            result = can_drive2(age, has_license, has_insurance, is_sober)
            print(f"Age {age}, License: {has_license}, Insurance: {has_insurance}, "
                  f"Sober: {is_sober} -> Can Drive: {result}")
        except Exception as e:
            print(f"Error checking age {age}: {str(e)}")


if __name__ == "__main__":
    main() 