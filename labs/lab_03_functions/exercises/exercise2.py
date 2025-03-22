"""
Exercise 2: Function Decorators and Closures

In this exercise, you will:
1. Create and use function decorators
2. Work with closures
3. Implement function factories
"""

import time
from functools import wraps
from typing import Any, Callable, Dict, TypeVar, cast

T = TypeVar('T')

def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to measure function execution time
    Args:
        func: Function to measure
    Returns:
        Wrapped function that prints execution time
    """
    # TODO: Implement the timer decorator
    pass

def memoize(func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator to cache function results
    Args:
        func: Function to memoize
    Returns:
        Wrapped function that caches results
    """
    # TODO: Implement the memoize decorator
    pass

def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    Decorator factory to retry failed function calls
    Args:
        max_attempts (int): Maximum number of retry attempts
        delay (float): Delay between retries in seconds
    Returns:
        Decorator function
    """
    # TODO: Implement the retry decorator factory
    pass

def create_counter(initial: int = 0) -> Callable[[], int]:
    """
    Create a counter function using closure
    Args:
        initial (int): Initial counter value
    Returns:
        Function that returns and increments counter
    """
    # TODO: Implement the counter factory using closure
    pass

def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    Create a multiplier function using closure
    Args:
        factor (int): Multiplication factor
    Returns:
        Function that multiplies input by factor
    """
    # TODO: Implement the multiplier factory using closure
    pass

@timer
@memoize
def fibonacci(n: int) -> int:
    """
    Calculate Fibonacci number (for testing decorators)
    Args:
        n (int): Position in Fibonacci sequence
    Returns:
        int: Fibonacci number at position n
    """
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@retry(max_attempts=3)
def unstable_function() -> bool:
    """
    Simulate an unstable function (for testing retry decorator)
    Returns:
        bool: True if successful
    Raises:
        Exception: Randomly to simulate failures
    """
    # TODO: Implement a function that randomly fails
    pass

def main():
    # TODO: Implement the main function that demonstrates:
    # 1. Using the timer decorator
    # 2. Using the memoize decorator
    # 3. Using the retry decorator
    # 4. Using the counter factory
    # 5. Using the multiplier factory
    pass

if __name__ == "__main__":
    main() 