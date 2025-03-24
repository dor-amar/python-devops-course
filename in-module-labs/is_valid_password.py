"""Task: Password Validator.

Implement a function to validate passwords based on multiple requirements.
"""

def is_valid_password(password: str) -> bool:
    """Check if a password meets all requirements.
    
    Password Requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number
    - Contains at least one special character (!@#$%^&*)
    
    Args:
        password (str): Password to validate
        
    Returns:
        bool: True if password is valid, False otherwise
        
    Example:
        >>> is_valid_password("Password123!")
        True
        >>> is_valid_password("weak")
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        "Password123!",      # Should return True
        "weak",             # Should return False (too short)
        "password123",      # Should return False (no uppercase)
        "PASSWORD123",      # Should return False (no lowercase)
        "Password",         # Should return False (no number)
        "Password123",      # Should return False (no special char)
        "",                # Should return False (empty)
        "Pass1!",          # Should return False (too short)
        "Password123!@#",  # Should return True
        "12345678",        # Should return False (no letters)
        "abcdefgh",        # Should return False (no numbers)
    ]
    
    for password in test_cases:
        result = is_valid_password(password)
        print(f"Password: '{password}'")
        print(f"Valid: {result}\n")


if __name__ == "__main__":
    main() 