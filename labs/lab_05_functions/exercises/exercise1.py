"""Basic functions demonstrating different types of arguments and return values."""

from typing import Any, Dict, Union


def calculate_bmi(weight: float, height: float) -> float:
    """Calculate Body Mass Index (BMI) using weight and height.

    Args:
        weight: Weight in kilograms
        height: Height in meters

    Returns:
        float: Calculated BMI value

    Raises:
        ValueError: If weight or height is non-positive
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers")
    return weight / (height ** 2)


def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting message with the given name.

    Args:
        name: Name of the person to greet
        greeting: Greeting word to use (default: "Hello")

    Returns:
        str: Formatted greeting message

    Raises:
        ValueError: If name is empty
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return f"{greeting}, {name}!"


def sum_numbers(*numbers: float) -> float:
    """Calculate the sum of a variable number of numbers.

    Args:
        *numbers: Variable number of float arguments

    Returns:
        float: Sum of all provided numbers

    Raises:
        ValueError: If no numbers are provided
    """
    if not numbers:
        raise ValueError("At least one number must be provided")
    return sum(numbers)


def create_person(name: str, age: int, **kwargs: Any) -> Dict[str, Any]:
    """Create a person dictionary with required and optional fields.

    Args:
        name: Person's name
        age: Person's age
        **kwargs: Additional fields to include in the person dictionary

    Returns:
        Dict[str, Any]: Dictionary containing person information

    Raises:
        ValueError: If name is empty or age is negative
    """
    if not name:
        raise ValueError("Name cannot be empty")
    if age < 0:
        raise ValueError("Age cannot be negative")

    person = {
        "name": name,
        "age": age,
        **kwargs
    }
    return person 