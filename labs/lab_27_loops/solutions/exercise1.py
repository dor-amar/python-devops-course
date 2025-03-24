"""Solution for Exercise 1: Basic Loop Operations."""

from typing import List


def print_even_numbers(n: int = 10) -> List[int]:
    """Print the first n even numbers using a for loop.
    
    Args:
        n: Number of even numbers to print
        
    Returns:
        List of even numbers
    """
    even_numbers = []
    for i in range(n):
        even_numbers.append(i * 2)
    return even_numbers


def factorial(n: int) -> int:
    """Calculate factorial of a number using a while loop.
    
    Args:
        n: Number to calculate factorial for
        
    Returns:
        Factorial of the number
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


def print_multiplication_table(n: int = 5) -> None:
    """Print multiplication table for numbers 1 to n.
    
    Args:
        n: Upper limit for multiplication table
    """
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}")


def reverse_string(s: str) -> str:
    """Reverse a string using a loop without built-in methods.
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    """
    result = ""
    for char in s:
        result = char + result
    return result 