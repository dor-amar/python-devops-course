"""Advanced function features including recursion, closures, decorators, and complex return types."""

from typing import Any, Callable, Dict, List, Tuple, TypeVar, cast
from functools import wraps

T = TypeVar('T', int, float)


def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms using recursion.

    Args:
        n: Number of terms to generate

    Returns:
        List[int]: List containing Fibonacci sequence

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number of terms must be non-negative")

    def _fibonacci(n: int) -> List[int]:
        if n == 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib = _fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

    return _fibonacci(n)


def counter() -> Callable[[], int]:
    """Create a closure that maintains a count.

    Returns:
        Callable[[], int]: Function that increments and returns the count
    """
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def validate_input(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that validates function arguments are positive numbers.

    Args:
        func: Function to decorate

    Returns:
        Callable[..., Any]: Decorated function with input validation
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("All numeric arguments must be positive")
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError("All numeric keyword arguments must be positive")
        return func(*args, **kwargs)
    return wrapper


def process_data(data: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Process a list of dictionaries and separate valid and invalid entries.

    Args:
        data: List of dictionaries to process

    Returns:
        Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]: Tuple containing
            (valid_entries, invalid_entries)

    Raises:
        ValueError: If data is not a list
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    valid_entries: List[Dict[str, Any]] = []
    invalid_entries: List[Dict[str, Any]] = []

    for entry in data:
        if not isinstance(entry, dict):
            invalid_entries.append(entry)
            continue

        # Example validation: check for required fields
        if "id" in entry and "name" in entry and entry["id"] > 0:
            valid_entries.append(entry)
        else:
            invalid_entries.append(entry)

    return valid_entries, invalid_entries 