"""Task: Recent Messages Manager.

Implement a function to manage recent messages with timestamps and limit the number of stored messages.
"""

def recent_messages(messages: list, new_message: str, timestamp: int, max_messages: int = 5) -> list:
    """Add a new message and maintain only the most recent messages.
    
    Args:
        messages (list): List of tuples (message, timestamp)
        new_message (str): New message to add
        timestamp (int): Timestamp of the new message
        max_messages (int): Maximum number of messages to keep
        
    Returns:
        list: Updated list of messages
        
    Example:
        >>> recent_messages([("Hello", 1000)], "Hi", 1001)
        [("Hello", 1000), ("Hi", 1001)]
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ([("Hello", 1000)], "Hi", 1001, 5),                    # Should add message
        ([("Hello", 1000), ("Hi", 1001)], "Hey", 1002, 2),     # Should remove oldest
        ([], "First", 1000, 3),                                # Should add to empty list
        ([("A", 1000), ("B", 1001)], "C", 1000, 3),           # Should handle same timestamp
        ([("A", 1000), ("B", 1001)], "C", 999, 3),            # Should handle older timestamp
    ]
    
    current_messages = []
    for messages, new_msg, timestamp, max_msgs in test_cases:
        current_messages = recent_messages(messages, new_msg, timestamp, max_msgs)
        print(f"After adding '{new_msg}' (timestamp: {timestamp}):")
        print(f"Messages: {current_messages}\n")


if __name__ == "__main__":
    main() 