"""
Exercise 4: JWT Authentication

Practice working with JWT tokens using the DummyJSON API.

TODO:
1. Implement login function to get JWT token
2. Use token for authenticated requests
3. Handle token expiration
4. Implement token refresh
5. Store tokens securely
"""

def login(username: str, password: str) -> str:
    """
    TODO: Login to get JWT token
    
    Args:
        username: User's username
        password: User's password
        
    Returns:
        JWT token string
        
    Raises:
        ValueError: If credentials are invalid
    """
    pass

def get_protected_data(token: str) -> dict:
    """
    TODO: Access protected route using JWT token
    
    Args:
        token: JWT token
        
    Returns:
        Protected data
        
    Raises:
        ValueError: If token is invalid
    """
    pass

def main():
    """
    Test your implementation:
    1. Login with test credentials
    2. Access protected routes
    3. Handle token expiration
    4. Test invalid tokens
    """
    pass

if __name__ == "__main__":
    main() 