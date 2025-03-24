"""Task: Time Comparison.

Implement a function to check if one time is earlier than another.
"""

def is_earlier(time1: str, time2: str) -> bool:
    """Check if time1 is earlier than time2.
    
    Args:
        time1 (str): First time in format "HH:MM"
        time2 (str): Second time in format "HH:MM"
        
    Returns:
        bool: True if time1 is earlier than time2, False otherwise
        
    Raises:
        ValueError: If time format is invalid
        
    Example:
        >>> is_earlier("09:00", "10:00")
        True
        >>> is_earlier("10:00", "09:00")
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ("09:00", "10:00"),    # Should return True
        ("10:00", "09:00"),    # Should return False
        ("09:00", "09:00"),    # Should return False
        ("23:59", "00:00"),    # Should return False
        ("00:00", "23:59"),    # Should return True
        ("12:00", "12:01"),    # Should return True
        ("12:01", "12:00"),    # Should return False
        ("invalid", "10:00"),  # Should raise ValueError
        ("10:00", "invalid"),  # Should raise ValueError
        ("25:00", "10:00"),    # Should raise ValueError
        ("10:60", "10:00"),    # Should raise ValueError
    ]
    
    for time1, time2 in test_cases:
        try:
            result = is_earlier(time1, time2)
            print(f"Is '{time1}' earlier than '{time2}'? {result}")
        except Exception as e:
            print(f"Error comparing '{time1}' and '{time2}': {str(e)}")


if __name__ == "__main__":
    main() 