"""
Exercise 2: Function Decorators and Closures - Solution
"""
import time
import functools
from typing import Any, Callable, TypeVar, Dict

T = TypeVar('T')

def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def memoize(func: Callable[..., T]) -> Callable[..., T]:
    """Decorator to cache function results."""
    cache: Dict[str, T] = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        # Create a cache key from function arguments
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Decorator factory to retry failed function calls."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    print(f"Attempt {attempts} failed: {str(e)}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def create_counter(initial: int = 0) -> Callable[[], int]:
    """Create a counter using closure."""
    count = initial
    
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    
    return counter

def create_multiplier(factor: int) -> Callable[[int], int]:
    """Create a multiplier using closure."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

@timer
@memoize
def fibonacci(n: int) -> int:
    """Calculate Fibonacci numbers (decorated with timer and memoize)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@retry(max_attempts=3)
def unstable_function() -> bool:
    """Simulate an unstable function that might fail."""
    if time.time() % 2 < 1:
        raise ValueError("Random failure")
    return True

def main():
    """Demonstrate the use of decorators and factories."""
    # Test timer decorator
    @timer
    def slow_function():
        time.sleep(0.1)
    print("\nTesting timer decorator:")
    slow_function()
    
    # Test memoize decorator
    print("\nTesting memoize decorator:")
    print("First call to fibonacci(10):")
    result1 = fibonacci(10)
    print("Second call to fibonacci(10):")
    result2 = fibonacci(10)
    assert result1 == result2
    
    # Test retry decorator
    print("\nTesting retry decorator:")
    unstable_function()
    
    # Test counter factory
    print("\nTesting counter factory:")
    counter1 = create_counter()
    counter2 = create_counter(10)
    print(f"Counter 1: {counter1()}, {counter1()}")
    print(f"Counter 2: {counter2()}, {counter2()}")
    
    # Test multiplier factory
    print("\nTesting multiplier factory:")
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")

if __name__ == "__main__":
    main() 