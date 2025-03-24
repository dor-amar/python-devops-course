"""Tests for Exercise 2: Loop Control and Patterns."""

import pytest
from exercises.exercise2 import (
    find_prime_numbers,
    print_number_pyramid,
    find_largest_palindrome_product,
    generate_fibonacci
)


def test_find_prime_numbers():
    """Test prime number finding."""
    primes = find_prime_numbers(20)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
    
    primes = find_prime_numbers(10)
    assert primes == [2, 3, 5, 7]


def test_print_number_pyramid(capsys):
    """Test number pyramid printing."""
    print_number_pyramid(3)
    captured = capsys.readouterr()
    expected = "1\n1 2\n1 2 3\n"
    assert captured.out == expected


def test_find_largest_palindrome_product():
    """Test largest palindrome product finding."""
    result = find_largest_palindrome_product()
    assert result == 906609  # 913 * 993


def test_generate_fibonacci():
    """Test Fibonacci sequence generation."""
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(3) == [0, 1, 1]
    assert generate_fibonacci(1) == [0] 