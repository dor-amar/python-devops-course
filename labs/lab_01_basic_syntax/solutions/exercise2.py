"""
Exercise 2: String Manipulation - Solution
"""

def get_user_input():
    """
    Get a string input from the user
    Returns:
        str: The input string
    """
    return input("Enter a string: ")

def convert_to_uppercase(text):
    """
    Convert the input string to uppercase
    Args:
        text (str): Input string
    Returns:
        str: Uppercase version of the input string
    """
    return text.upper()

def reverse_string(text):
    """
    Reverse the input string
    Args:
        text (str): Input string
    Returns:
        str: Reversed version of the input string
    """
    return text[::-1]

def count_vowels(text):
    """
    Count the number of vowels in the input string
    Args:
        text (str): Input string
    Returns:
        int: Number of vowels in the string
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def main():
    # Get input from user
    text = get_user_input()
    
    # Convert to uppercase
    upper_text = convert_to_uppercase(text)
    print(f"Uppercase: {upper_text}")
    
    # Reverse the string
    reversed_text = reverse_string(text)
    print(f"Reversed: {reversed_text}")
    
    # Count vowels
    vowel_count = count_vowels(text)
    print(f"Number of vowels: {vowel_count}")

if __name__ == "__main__":
    main() 