"""Tests for Exercise 1: Basic Loop Operations."""

import pytest
from exercises.exercise1 import (
    print_even_numbers,
    factorial,
    print_multiplication_table,
    reverse_string
)


def test_print_even_numbers():
    """Test printing even numbers."""
    result = print_even_numbers(5)
    assert result == [0, 2, 4, 6, 8]
    
    result = print_even_numbers(3)
    assert result == [0, 2, 4]


def test_factorial():
    """Test factorial calculation."""
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_print_multiplication_table(capsys):
    """Test multiplication table printing."""
    print_multiplication_table(2)
    captured = capsys.readouterr()
    expected = "1 x 1 = 1\n1 x 2 = 2\n2 x 1 = 2\n2 x 2 = 4\n"
    assert captured.out == expected


def test_reverse_string():
    """Test string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a" 