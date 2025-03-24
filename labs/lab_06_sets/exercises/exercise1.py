"""Exercise 1: Basic Set Operations.

In this exercise, you will work with basic set operations in Python.
"""

def find_common_elements(set1: set, set2: set) -> set:
    """Find common elements between two sets.
    
    TODO: Implement this function to:
    1. Take two sets as input
    2. Return a new set containing elements that exist in both sets
    
    Example:
        Input: {1, 2, 3}, {3, 4, 5}
        Output: {3}
    """
    # Your code here
    pass


def remove_duplicates(numbers: list) -> list:
    """Remove duplicates from a list using sets.
    
    TODO: Implement this function to:
    1. Take a list as input
    2. Use a set to remove duplicates
    3. Return a new list with unique elements
    
    Example:
        Input: [1, 2, 3, 2, 4, 1]
        Output: [1, 2, 3, 4]
    """
    # Your code here
    pass


def is_subset(set1: set, set2: set) -> bool:
    """Check if one set is a subset of another.
    
    TODO: Implement this function to:
    1. Take two sets as input
    2. Check if set1 is a subset of set2
    3. Return True if set1 is a subset of set2, False otherwise
    
    Example:
        Input: {1, 2}, {1, 2, 3, 4}
        Output: True
    """
    # Your code here
    pass


def main():
    """Test your implementations here."""
    # Test find_common_elements
    print("Testing find_common_elements:")
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(f"Input: {set1}, {set2} -> Output: {find_common_elements(set1, set2)}")
    
    # Test remove_duplicates
    print("\nTesting remove_duplicates:")
    numbers = [1, 2, 3, 2, 4, 1]
    print(f"Input: {numbers} -> Output: {remove_duplicates(numbers)}")
    
    # Test is_subset
    print("\nTesting is_subset:")
    set1 = {1, 2}
    set2 = {1, 2, 3, 4}
    print(f"Input: {set1}, {set2} -> Output: {is_subset(set1, set2)}")


if __name__ == "__main__":
    main() 