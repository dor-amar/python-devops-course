"""Task: Word Absence Checker.

Implement a function to check if a word is absent from a given text.
"""

def is_word_absent(text: str, word: str) -> bool:
    """Check if a word is absent from the text.
    
    Args:
        text (str): Text to search in
        word (str): Word to look for
        
    Returns:
        bool: True if word is not found, False if word is found
        
    Example:
        >>> is_word_absent("Hello world", "python")
        True
        >>> is_word_absent("Hello world", "world")
        False
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        ("Hello world", "python"),      # Should return True
        ("Hello world", "world"),       # Should return False
        ("Python is fun", "python"),    # Should return False (case-insensitive)
        ("", "test"),                   # Should return True
        ("test", ""),                   # Should return False
        ("Hello, world!", "world"),     # Should return False (handles punctuation)
        ("Multiple   spaces", "spaces"), # Should return False (handles multiple spaces)
    ]
    
    for text, word in test_cases:
        result = is_word_absent(text, word)
        print(f"Text: '{text}'")
        print(f"Word: '{word}'")
        print(f"Word is {'absent' if result else 'present'}\n")


if __name__ == "__main__":
    main() 