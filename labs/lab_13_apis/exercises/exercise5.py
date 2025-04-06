"""
Exercise 5: News API Integration

Practice working with API parameters and response pagination.

TODO:
1. Create function to fetch top headlines
2. Implement search functionality
3. Handle response pagination
4. Filter results
5. Format output
"""

def get_top_headlines(api_key: str, country: str = 'us', category: str = None) -> list:
    """
    TODO: Fetch top headlines from News API
    
    Args:
        api_key: News API key
        country: Country code
        category: News category
        
    Returns:
        List of articles
        
    Raises:
        ValueError: If parameters are invalid
    """
    pass

def search_news(api_key: str, query: str, from_date: str = None, sort_by: str = None) -> list:
    """
    TODO: Search news articles
    
    Args:
        api_key: News API key
        query: Search query
        from_date: Start date (YYYY-MM-DD)
        sort_by: Sort method
        
    Returns:
        List of matching articles
    """
    pass

def main():
    """
    Test your implementation:
    1. Fetch headlines for different countries
    2. Search specific topics
    3. Use different sorting options
    4. Handle pagination
    """
    pass

if __name__ == "__main__":
    main() 