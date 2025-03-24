"""
Exercise 1: Advanced Function Arguments

In this exercise, you will:
1. Work with different types of function arguments
2. Use lambda functions
3. Implement function overloading
"""

from typing import Any, Dict, List, Optional, Union

def calculate_total(*args: float) -> float:
    print("test")
    
    """
    Calculate the total of variable number of arguments
    Args:
        *args: Variable number of float arguments
    Returns:
        float: Sum of all arguments
    """
    # TODO: Implement the function to sum all arguments
    pass

def create_person(name: str, age: int, **kwargs: Any) -> Dict[str, Any]:
    """
    Create a person dictionary with required and optional fields
    Args:
        name (str): Person's name
        age (int): Person's age
        **kwargs: Additional person attributes
    Returns:
        dict: Person information dictionary
    """
    # TODO: Implement the function to create a person dictionary
    pass

def format_text(text: str, prefix: str = "", suffix: str = "", 
                uppercase: bool = False, reverse: bool = False) -> str:
    """
    Format text with various options
    Args:
        text (str): Text to format
        prefix (str, optional): Prefix to add. Defaults to "".
        suffix (str, optional): Suffix to add. Defaults to "".
        uppercase (bool, optional): Whether to convert to uppercase. Defaults to False.
        reverse (bool, optional): Whether to reverse the text. Defaults to False.
    Returns:
        str: Formatted text
    """
    # TODO: Implement the function to format text based on parameters
    pass

def process_numbers(numbers: List[Union[int, float]], 
                   operation: str = "sum") -> Union[int, float]:
    """
    Process a list of numbers with different operations
    Args:
        numbers (List[Union[int, float]]): List of numbers to process
        operation (str, optional): Operation to perform. Defaults to "sum".
            Options: "sum", "product", "average", "max", "min"
    Returns:
        Union[int, float]: Result of the operation
    """
    # TODO: Implement the function to process numbers based on operation
    pass

# TODO: Create lambda functions for:
# 1. Squaring a number
square = None

# 2. Checking if a number is even
is_even = None

# 3. Converting a string to uppercase
to_upper = None

def main():
    # TODO: Implement the main function that demonstrates:
    # 1. Using calculate_total with different numbers of arguments
    # 2. Creating person dictionaries with different attributes
    # 3. Formatting text with different options
    # 4. Processing numbers with different operations
    # 5. Using the lambda functions
    pass

if __name__ == "__main__":
    main() 