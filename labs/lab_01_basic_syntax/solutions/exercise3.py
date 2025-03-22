"""
Exercise 3: Type Conversion - Solution
"""

def get_number_input():
    """
    Get a number as string input from the user
    Returns:
        str: The input number as string
    """
    return input("Enter a number: ")

def convert_to_int(number_str):
    """
    Convert string to integer
    Args:
        number_str (str): Number as string
    Returns:
        int: Converted integer
    Raises:
        ValueError: If conversion fails
    """
    return int(float(number_str))

def convert_to_float(number_str):
    """
    Convert string to float
    Args:
        number_str (str): Number as string
    Returns:
        float: Converted float
    Raises:
        ValueError: If conversion fails
    """
    return float(number_str)

def perform_calculations(number):
    """
    Perform various calculations with the number
    Args:
        number (float): Input number
    Returns:
        dict: Dictionary containing results of different calculations
    """
    return {
        'square': number * number,
        'half': number / 2,
        'rounded': round(number)
    }

def main():
    try:
        # Get number input from user
        number_str = get_number_input()
        
        # Convert to different types
        number_int = convert_to_int(number_str)
        number_float = convert_to_float(number_str)
        
        print(f"As integer: {number_int}")
        print(f"As float: {number_float}")
        
        # Perform calculations
        results = perform_calculations(number_float)
        
        print(f"Square: {results['square']}")
        print(f"Half: {results['half']}")
        print(f"Rounded: {results['rounded']}")
        
    except ValueError as e:
        print(f"Error: Invalid number format - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 