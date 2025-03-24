"""Task: Message Logger.

Implement a function to log messages with timestamps and log levels.
"""

def log_message(message: str, level: str = 'INFO', timestamp: int = None) -> str:
    """Format a log message with timestamp and level.
    
    Args:
        message (str): Message to log
        level (str): Log level ('INFO', 'WARNING', 'ERROR', 'DEBUG')
        timestamp (int, optional): Unix timestamp. If None, use current time
        
    Returns:
        str: Formatted log message
        
    Raises:
        ValueError: If level is invalid
        
    Example:
        >>> log_message("System started", "INFO")
        '[INFO] 2024-03-14 12:00:00 - System started'
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ("System started", "INFO"),           # Should format with INFO level
        ("Disk space low", "WARNING"),        # Should format with WARNING level
        ("Connection failed", "ERROR"),       # Should format with ERROR level
        ("Debug info", "DEBUG"),              # Should format with DEBUG level
        ("Invalid level", "INVALID"),         # Should raise ValueError
        ("No level specified"),               # Should use default INFO level
        ("Custom timestamp", "INFO", 1710428400),  # Should use provided timestamp
    ]
    
    for case in test_cases:
        try:
            if len(case) == 3:
                result = log_message(case[0], case[1], case[2])
            elif len(case) == 2:
                result = log_message(case[0], case[1])
            else:
                result = log_message(case[0])
            print(f"Input: {case}")
            print(f"Output: {result}\n")
        except Exception as e:
            print(f"Error processing {case}: {str(e)}\n")


if __name__ == "__main__":
    main() 