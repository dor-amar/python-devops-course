"""
Exercise 1: Basic API Requests

Practice making basic API requests and handling responses using the Random Fox API.

TODO:
1. Create a function that fetches a random fox image
2. Handle the response properly
3. Extract and return the image URL
4. Implement proper error handling
5. Add status code checking
"""

def get_random_fox() -> dict:
    """
    TODO: Fetch a random fox image from the API
    
    Returns:
        Dictionary containing image URL and link
        
    Raises:
        requests.RequestException: If the API request fails
    """
    pass

def validate_response(response_data: dict) -> bool:
    """
    TODO: Validate that the response contains required fields
    
    Args:
        response_data: Dictionary from API response
        
    Returns:
        True if valid, False otherwise
    """
    pass

def main():
    """
    Test your implementation:
    1. Fetch multiple fox images
    2. Handle potential errors
    3. Print image URLs
    """
    pass

if __name__ == "__main__":
    main() 