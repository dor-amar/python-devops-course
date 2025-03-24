"""Task: Time Conversion Utility.

Implement a function to convert between different time formats (12-hour, 24-hour, and minutes since midnight).
"""

def time_convertor(time_str: str, target_format: str = '24h') -> str:
    """Convert time between different formats.
    
    Args:
        time_str (str): Input time string in format 'HH:MM AM/PM' or 'HH:MM'
        target_format (str): Target format ('12h', '24h', or 'minutes')
        
    Returns:
        str: Converted time string
        
    Raises:
        ValueError: If input format is invalid or time values are out of range
        
    Example:
        >>> time_convertor('02:30 PM', '24h')
        '14:30'
        >>> time_convertor('14:30', 'minutes')
        '870'
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ('02:30 PM', '24h'),    # Should return '14:30'
        ('14:30', '12h'),       # Should return '02:30 PM'
        ('09:15 AM', 'minutes'), # Should return '555'
        ('23:45', '12h'),       # Should return '11:45 PM'
        ('555', '24h'),         # Should return '09:15'
        ('invalid', '24h'),     # Should raise ValueError
        ('25:00', '12h'),       # Should raise ValueError
    ]
    
    for time_str, target in test_cases:
        try:
            result = time_convertor(time_str, target)
            print(f"Convert {time_str} to {target} format: {result}")
        except Exception as e:
            print(f"Error converting {time_str} to {target} format: {str(e)}")


if __name__ == "__main__":
    main() 