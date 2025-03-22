"""
Exercise 1: Advanced Function Arguments - Solution
"""
from typing import Any, Dict, List, Union

def calculate_total(*args: float) -> float:
    """Calculate the total of a variable number of float arguments."""
    return sum(args)

def create_person(name: str, age: int, **kwargs: Any) -> Dict[str, Any]:
    """Create a person dictionary with required and optional fields."""
    person = {
        "name": name,
        "age": age
    }
    person.update(kwargs)
    return person

def format_text(text: str, prefix: str = "", suffix: str = "", 
                uppercase: bool = False, reverse: bool = False) -> str:
    """Format text with various options."""
    result = text
    if uppercase:
        result = result.upper()
    if reverse:
        result = result[::-1]
    return f"{prefix}{result}{suffix}"

def process_numbers(numbers: List[Union[int, float]], 
                   operation: str = "sum") -> Union[int, float]:
    """Process a list of numbers with different operations."""
    if not numbers:
        return 0
    
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

# Lambda functions
square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0
to_upper = lambda s: s.upper()

def main():
    """Demonstrate the use of the functions and lambda functions."""
    # Test calculate_total
    print("Total:", calculate_total(1.5, 2.5, 3.5))
    
    # Test create_person
    person = create_person("John", 30, city="New York", occupation="Engineer")
    print("Person:", person)
    
    # Test format_text
    print("Formatted text:", format_text("hello", prefix="[", suffix="]", uppercase=True))
    print("Reversed text:", format_text("hello", reverse=True))
    
    # Test process_numbers
    numbers = [1, 2, 3, 4, 5]
    print("Sum:", process_numbers(numbers, "sum"))
    print("Average:", process_numbers(numbers, "average"))
    
    # Test lambda functions
    print("Square of 5:", square(5))
    print("Is 6 even?", is_even(6))
    print("Uppercase 'hello':", to_upper("hello"))

if __name__ == "__main__":
    main() 