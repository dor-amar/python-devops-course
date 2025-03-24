"""Solution for Exercise 2: Dictionary Methods and Operations."""

from typing import Any, Dict, List


def count_word_frequencies(text: str) -> Dict[str, int]:
    """Count frequency of each word in a text.
    
    Args:
        text: Input text to analyze
        
    Returns:
        Dictionary mapping words to their frequencies
    """
    words = text.lower().split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def invert_dictionary(d: Dict[str, Any]) -> Dict[Any, List[str]]:
    """Invert a dictionary, mapping values to lists of keys.
    
    Args:
        d: Dictionary to invert
        
    Returns:
        Inverted dictionary
    """
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted


def find_common_keys(d1: Dict[str, Any], d2: Dict[str, Any]) -> List[str]:
    """Find keys that exist in both dictionaries.
    
    Args:
        d1: First dictionary
        d2: Second dictionary
        
    Returns:
        List of common keys
    """
    return list(set(d1.keys()) & set(d2.keys()))


def deep_update(d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
    """Deep update one dictionary with another.
    
    Args:
        d1: Base dictionary to update
        d2: Dictionary with updates
        
    Returns:
        Updated dictionary
    """
    result = d1.copy()
    for key, value in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_update(result[key], value)
        else:
            result[key] = value
    return result 