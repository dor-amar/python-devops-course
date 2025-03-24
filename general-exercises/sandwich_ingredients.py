"""Task: Sandwich Ingredients Manager.

Implement a function to manage sandwich ingredients and check if a sandwich can be made.
"""

def sandwich_ingredients(available: list, required: list) -> bool:
    """Check if a sandwich can be made with available ingredients.
    
    Args:
        available (list): List of available ingredients
        required (list): List of required ingredients
        
    Returns:
        bool: True if all required ingredients are available, False otherwise
        
    Example:
        >>> sandwich_ingredients(['bread', 'cheese', 'lettuce'], ['bread', 'cheese'])
        True
        >>> sandwich_ingredients(['bread', 'cheese'], ['bread', 'tomato'])
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        (['bread', 'cheese', 'lettuce'], ['bread', 'cheese']),           # Should return True
        (['bread', 'cheese'], ['bread', 'tomato']),                      # Should return False
        (['bread', 'cheese', 'lettuce', 'tomato'], ['bread', 'cheese']), # Should return True
        ([], ['bread']),                                                 # Should return False
        (['bread'], []),                                                # Should return True
        (['bread', 'bread'], ['bread']),                                # Should return True
        (['bread'], ['bread', 'bread']),                                # Should return False
    ]
    
    for available, required in test_cases:
        result = sandwich_ingredients(available, required)
        print(f"Available: {available}")
        print(f"Required: {required}")
        print(f"Can make sandwich: {result}\n")


if __name__ == "__main__":
    main() 