"""Task: Convert time to seconds.

Write a function that takes hours, minutes, and seconds as input and returns the total number of seconds.
"""

def get_seconds(hours: int, minutes: int, seconds: int) -> int:
    """Convert time to total seconds.
    
    Args:
        hours (int): Number of hours
        minutes (int): Number of minutes
        seconds (int): Number of seconds
        
    Returns:
        int: Total number of seconds
        
    Example:
        >>> get_seconds(1, 30, 45)
        5445
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    print(f"1 hour, 30 minutes, 45 seconds = {get_seconds(1, 30, 45)} seconds")
    print(f"0 hours, 5 minutes, 30 seconds = {get_seconds(0, 5, 30)} seconds")
    print(f"2 hours, 0 minutes, 15 seconds = {get_seconds(2, 0, 15)} seconds")


if __name__ == "__main__":
    main() 