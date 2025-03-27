"""
Exercise 2: File Analysis and Text Processing

This exercise focuses on implementing basic file analysis functions to process
text files and gather statistics about their contents.

Learning objectives:
- Reading files in Python
- Text processing and analysis
- Error handling for file operations
- Working with strings and counting
"""

def count_lines(filepath: str) -> int:
    """
    TODO: Implement a function that counts the number of lines in a file
    
    Args:
        filepath: Path to the file to analyze
        
    Returns:
        Number of lines in the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    pass


def count_words(filepath: str) -> int:
    """
    TODO: Implement a function that counts the total number of words in a file
    
    Args:
        filepath: Path to the file to analyze
        
    Returns:
        Number of words in the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    pass


def find_word_frequency(filepath: str, word: str) -> int:
    """
    TODO: Implement a function that counts how many times a specific word appears
    
    Args:
        filepath: Path to the file to analyze
        word: Word to search for
        
    Returns:
        Number of times the word appears in the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    pass


def main():
    """
    TODO: Implement test cases for your functions
    
    Suggested test cases:
    1. Count lines in a file with:
       - Empty file
       - Single line
       - Multiple lines
       - Only newlines
    
    2. Count words in a file with:
       - Empty file
       - Single word
       - Multiple words
       - Special characters
    
    3. Find word frequency with:
       - Word that doesn't exist
       - Word that appears once
       - Word that appears multiple times
       - Case-sensitive vs case-insensitive
    """
    pass


if __name__ == "__main__":
    main() 