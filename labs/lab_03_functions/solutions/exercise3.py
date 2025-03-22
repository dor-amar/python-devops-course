"""
Exercise 3: Custom Module Development - Solution
"""
from typing import List

def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]

def count_vowels(text: str) -> int:
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def _is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def remove_duplicates(text: str) -> str:
    """Remove duplicate characters from a string."""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def _count_substring(text: str, substring: str) -> int:
    """Count occurrences of a substring."""
    if not substring:
        return 0
    return text.count(substring)

def main():
    """Demonstrate the use of all public functions."""
    # Test string
    test_string = "hello world"
    
    # Test each function
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reverse_string(test_string)}")
    print(f"Vowel count: {count_vowels(test_string)}")
    print(f"Capitalized words: {capitalize_words(test_string)}")
    print(f"Without duplicates: {remove_duplicates(test_string)}")
    
    # Test palindrome
    palindrome_test = "A man, a plan, a canal: Panama"
    print(f"\nTesting palindrome: {palindrome_test}")
    print(f"Is palindrome: {_is_palindrome(palindrome_test)}")
    
    # Test substring counting
    text = "hello hello world"
    substring = "hello"
    print(f"\nTesting substring count:")
    print(f"Count of '{substring}' in '{text}': {_count_substring(text, substring)}")

if __name__ == "__main__":
    main() 