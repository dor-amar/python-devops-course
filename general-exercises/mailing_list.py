"""Task: Mailing List Manager.

Implement a function to manage a mailing list with email validation and duplicate prevention.
"""

def mailing_list(emails: list, operation: str, email: str) -> list:
    """Manage a mailing list with email validation.
    
    Operations:
    - 'add': Add a valid email to the list
    - 'remove': Remove an email from the list
    
    Args:
        emails (list): Current list of email addresses
        operation (str): Operation to perform ('add' or 'remove')
        email (str): Email address to add or remove
        
    Returns:
        list: Updated list of email addresses
        
    Raises:
        ValueError: If operation is invalid or email format is invalid
        
    Example:
        >>> mailing_list([], 'add', 'user@example.com')
        ['user@example.com']
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ([], 'add', 'user@example.com'),           # Should add valid email
        (['user@example.com'], 'add', 'user2@example.com'),  # Should add another email
        (['user@example.com', 'user2@example.com'], 'add', 'user@example.com'),  # Should not add duplicate
        (['user@example.com'], 'remove', 'user@example.com'),  # Should remove email
        (['user@example.com'], 'add', 'invalid-email'),  # Should raise ValueError
        (['user@example.com'], 'invalid', 'user2@example.com'),  # Should raise ValueError
        (['user@example.com'], 'remove', 'nonexistent@example.com'),  # Should not modify list
    ]
    
    current_list = []
    for emails, op, email in test_cases:
        try:
            current_list = mailing_list(emails, op, email)
            print(f"After {op} '{email}': {current_list}")
        except Exception as e:
            print(f"Error performing {op} on '{email}': {str(e)}")


if __name__ == "__main__":
    main() 