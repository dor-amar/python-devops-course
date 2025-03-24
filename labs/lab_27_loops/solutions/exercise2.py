"""Solution for Exercise 2: Loop Control and Patterns."""

from typing import List


def find_prime_numbers(limit: int = 100) -> List[int]:
    """Find prime numbers up to the given limit using break and continue.
    
    Args:
        limit: Upper limit for prime number search
        
    Returns:
        List of prime numbers
    """
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def print_number_pyramid(n: int = 5) -> None:
    """Print a pyramid of numbers using nested loops.
    
    Args:
        n: Height of the pyramid
    """
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def find_largest_palindrome_product() -> int:
    """Find the largest palindrome product of two 3-digit numbers.
    
    Returns:
        Largest palindrome product
    """
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):  # Start from i to avoid duplicate products
            product = i * j
            if str(product) == str(product)[::-1]:
                max_palindrome = max(max_palindrome, product)
    return max_palindrome


def generate_fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms.
    
    Args:
        n: Number of terms to generate
        
    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib 