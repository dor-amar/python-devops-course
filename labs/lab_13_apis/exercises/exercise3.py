"""
Exercise 3: NASA API Integration

Practice working with API keys and handling complex responses.

TODO:
1. Create function to fetch Astronomy Picture of the Day
2. Handle API key authentication
3. Process image data
4. Save images locally
5. Create response cache
"""

def get_apod(api_key: str, date: str = None) -> dict:
    """
    TODO: Fetch NASA's Astronomy Picture of the Day
    
    Args:
        api_key: NASA API key
        date: Specific date for APOD (YYYY-MM-DD)
        
    Returns:
        Dictionary containing image data
        
    Raises:
        ValueError: If date format is invalid
        requests.RequestException: If API request fails
    """
    pass

def save_apod_image(image_url: str, filename: str) -> bool:
    """
    TODO: Download and save APOD image
    
    Args:
        image_url: URL of the image
        filename: Where to save the image
        
    Returns:
        True if successful, False otherwise
    """
    pass

def main():
    """
    Test your implementation:
    1. Fetch today's APOD
    2. Fetch APOD for specific date
    3. Save images
    4. Handle errors
    """
    pass

if __name__ == "__main__":
    main() 