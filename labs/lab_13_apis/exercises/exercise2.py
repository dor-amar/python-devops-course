"""
Exercise 2: Working with GitHub API

Practice fetching and processing data from the GitHub API.

TODO:
1. Create functions to fetch repository information
2. Get repository issues
3. Handle pagination
4. Process response data
5. Implement error handling
"""

def get_repo_info(owner: str, repo: str) -> dict:
    """
    TODO: Fetch repository information from GitHub API
    
    Args:
        owner: Repository owner
        repo: Repository name
        
    Returns:
        Dictionary containing repository information
        
    Raises:
        requests.RequestException: If the API request fails
    """
    pass

def get_repo_issues(owner: str, repo: str, state: str = "open") -> list:
    """
    TODO: Fetch repository issues
    
    Args:
        owner: Repository owner
        repo: Repository name
        state: Issue state (open/closed)
        
    Returns:
        List of issues
    """
    pass

def main():
    """
    Test your implementation:
    1. Fetch info for popular repositories
    2. Get their issues
    3. Handle errors
    """
    pass

if __name__ == "__main__":
    main() 