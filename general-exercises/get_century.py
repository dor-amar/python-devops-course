"""Task: Determine the century from a year.

Write a function that takes a year as input and returns which century it belongs to.
"""

def get_century(year: int) -> int:
    """Determine the century from a year.
    
    Args:
        year (int): The year to check
        
    Returns:
        int: The century the year belongs to
        
    Example:
        >>> get_century(2024)
        21
        >>> get_century(1900)
        19
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    print(f"Year 2024 is in century: {get_century(2024)}")
    print(f"Year 1900 is in century: {get_century(1900)}")
    print(f"Year 1801 is in century: {get_century(1801)}")
    print(f"Year 2000 is in century: {get_century(2000)}")


if __name__ == "__main__":
    main() 