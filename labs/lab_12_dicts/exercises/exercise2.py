"""Exercise 2: Dictionary Methods and Operations.

In this exercise, you will work with more advanced dictionary operations. You will learn how to:
1. Count word frequencies in text
2. Invert dictionaries
3. Find common keys between dictionaries
4. Perform deep updates on nested dictionaries (Bonus)
"""

from typing import Dict, List, Optional


def count_word_frequencies(text: str) -> Dict[str, int]:
    """Count frequency of each word in a text.
    
    TODO: Implement this function to:
    1. Split the text into words (convert to lowercase)
    2. Count how many times each word appears
    3. Return a dictionary with words as keys and counts as values
    
    Example:
        Input: "hello world hello python world"
        Output: {"hello": 2, "world": 2, "python": 1}
    """
    # TODO: Implement this function
    pass


def invert_dictionary(d: Dict[str, Any]) -> Dict[Any, List[str]]:
    """Invert a dictionary, mapping values to lists of keys.
    
    TODO: Implement this function to:
    1. Create a new dictionary where values become keys
    2. For each value, collect all keys that had that value
    3. Return the inverted dictionary
    
    Example:
        Input: {"a": 1, "b": 2, "c": 1}
        Output: {1: ["a", "c"], 2: ["b"]}
    """
    # TODO: Implement this function
    pass


def find_common_keys(d1: Dict[str, Any], d2: Dict[str, Any]) -> List[str]:
    """Find keys that exist in both dictionaries.
    
    TODO: Implement this function to:
    1. Find all keys that exist in both dictionaries
    2. Return a list of these common keys
    
    Example:
        Input: d1={"a": 1, "b": 2}, d2={"b": 3, "c": 4}
        Output: ["b"]
    """
    # TODO: Implement this function
    pass


def deep_update(d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
    """Deep update one dictionary with another.
    
    Args:
        d1: Base dictionary to update
        d2: Dictionary with updates
        
    Returns:
        Updated dictionary
    """
    # TODO: Implement this function
    pass 