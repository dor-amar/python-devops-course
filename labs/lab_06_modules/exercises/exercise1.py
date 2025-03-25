"""Module demonstrating Python module organization and imports."""

import math
import re
from typing import Dict, Union


# Constants
PI = math.pi
E = math.e
CURRENCY_RATES = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 110.0
}

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def calculate_area(shape: str, dimensions: Dict[str, Union[int, float]]) -> float:
    """Calculate the area of various geometric shapes.

    Args:
        shape: Type of shape ('circle', 'rectangle', 'triangle')
        dimensions: Dictionary containing shape dimensions

    Returns:
        float: Calculated area

    Raises:
        ValueError: If shape is not supported or dimensions are invalid
    """
    shape = shape.lower()
    
    if shape == 'circle':
        if 'radius' not in dimensions:
            raise ValueError("Circle requires 'radius' dimension")
        return PI * dimensions['radius'] ** 2
    
    elif shape == 'rectangle':
        if 'length' not in dimensions or 'width' not in dimensions:
            raise ValueError("Rectangle requires 'length' and 'width' dimensions")
        return dimensions['length'] * dimensions['width']
    
    elif shape == 'triangle':
        if 'base' not in dimensions or 'height' not in dimensions:
            raise ValueError("Triangle requires 'base' and 'height' dimensions")
        return 0.5 * dimensions['base'] * dimensions['height']
    
    else:
        raise ValueError(f"Unsupported shape: {shape}")


def format_currency(amount: float, currency: str = "USD") -> str:
    """Format amount as currency string.

    Args:
        amount: Amount to format
        currency: Currency code (default: "USD")

    Returns:
        str: Formatted currency string

    Raises:
        ValueError: If currency is not supported
    """
    if currency not in CURRENCY_RATES:
        raise ValueError(f"Unsupported currency: {currency}")
    
    rate = CURRENCY_RATES[currency]
    converted = amount * rate
    
    if currency == "USD":
        return f"${converted:.2f}"
    elif currency == "EUR":
        return f"€{converted:.2f}"
    elif currency == "GBP":
        return f"£{converted:.2f}"
    elif currency == "JPY":
        return f"¥{converted:.0f}"
    
    return f"{currency} {converted:.2f}"


def validate_email(email: str) -> bool:
    """Validate email address format.

    Args:
        email: Email address to validate

    Returns:
        bool: True if email is valid, False otherwise
    """
    return bool(EMAIL_PATTERN.match(email))


# Example usage
if __name__ == "__main__":
    try:
        # Test area calculations
        circle_area = calculate_area('circle', {'radius': 5})
        print(f"Circle area: {circle_area:.2f}")
        
        # Test currency formatting
        usd_amount = format_currency(100.0)
        eur_amount = format_currency(100.0, "EUR")
        print(f"USD: {usd_amount}")
        print(f"EUR: {eur_amount}")
        
        # Test email validation
        valid_email = validate_email("test@example.com")
        invalid_email = validate_email("invalid-email")
        print(f"Valid email: {valid_email}")
        print(f"Invalid email: {invalid_email}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


"""
Exercise 1: Creating and Using Python Modules

In this exercise, you'll practice creating and importing modules in Python.
You'll create a simple calculator module with basic arithmetic operations.

TODO:
1. Create a file called 'calculator.py' with the following functions:
   - add(a: float, b: float) -> float
   - subtract(a: float, b: float) -> float
   - multiply(a: float, b: float) -> float
   - divide(a: float, b: float) -> float
   Make sure to handle division by zero!

2. In this file, import your calculator module and:
   - Create a function called 'calculate' that takes:
     * operation: str (one of: 'add', 'subtract', 'multiply', 'divide')
     * num1: float
     * num2: float
   - The function should return the result of the specified operation
   - Raise ValueError for invalid operations
   - Handle division by zero gracefully

Example usage:
    result = calculate('add', 10, 5)      # Should return 15.0
    result = calculate('divide', 10, 2)    # Should return 5.0
    result = calculate('divide', 10, 0)    # Should raise an error
    result = calculate('power', 2, 3)      # Should raise ValueError
"""

# TODO: Import your calculator module here


def calculate(operation: str, num1: float, num2: float) -> float:
    """
    Performs the specified arithmetic operation on two numbers.
    
    Args:
        operation: The arithmetic operation to perform ('add', 'subtract', 'multiply', 'divide')
        num1: The first number
        num2: The second number
        
    Returns:
        float: The result of the operation
        
    Raises:
        ValueError: If the operation is invalid or if trying to divide by zero
    """
    # TODO: Implement this function
    pass


def main():
    """Test the calculate function with various operations."""
    test_cases = [
        ('add', 10, 5),
        ('subtract', 10, 5),
        ('multiply', 10, 5),
        ('divide', 10, 5),
        ('divide', 10, 0),  # Should handle this error
        ('power', 2, 3),    # Should raise ValueError
    ]

    for operation, num1, num2 in test_cases:
        try:
            result = calculate(operation, num1, num2)
            print(f"{operation}({num1}, {num2}) = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main() 