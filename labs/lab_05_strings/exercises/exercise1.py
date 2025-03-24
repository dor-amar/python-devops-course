"""Exercise 1: Basic String Operations.

In this exercise, you will work with basic string operations in Python.
"""

def reverse_string(text: str) -> str:
    """Reverse a string.
    
    TODO: Implement this function to:
    1. Take a string as input
    2. Return the reversed string
    
    Example:
        Input: "hello"
        Output: "olleh"
    """
    # Your code here
    pass


def count_vowels(text: str) -> int:
    """Count the number of vowels in a string.
    
    TODO: Implement this function to:
    1. Count all vowels (a, e, i, o, u) in the input string
    2. Return the total count
    
    Example:
        Input: "hello"
        Output: 2
    """
    # Your code here
    pass


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome.
    
    TODO: Implement this function to:
    1. Check if the string reads the same forwards and backwards
    2. Return True if it is a palindrome, False otherwise
    
    Example:
        Input: "radar"
        Output: True
    """
    # Your code here
    pass


def main():
    """Test your implementations here."""
    # Test reverse_string
    print("Testing reverse_string:")
    print(f"Input: 'hello' -> Output: {reverse_string('hello')}")
    
    # Test count_vowels
    print("\nTesting count_vowels:")
    print(f"Input: 'hello' -> Output: {count_vowels('hello')}")
    
    # Test is_palindrome
    print("\nTesting is_palindrome:")
    print(f"Input: 'radar' -> Output: {is_palindrome('radar')}")
    print(f"Input: 'hello' -> Output: {is_palindrome('hello')}")


if __name__ == "__main__":
    main() 