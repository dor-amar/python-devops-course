"""
Tests for Exercise 1: Advanced Function Arguments
"""
import pytest
from exercises.exercise1 import *

def test_calculate_total():
    """Test variable argument function"""
    assert calculate_total(1, 2, 3) == 6
    assert calculate_total(1.5, 2.5, 3.5) == 7.5
    assert calculate_total() == 0

def test_create_person():
    """Test keyword argument function"""
    person = create_person("John", 30)
    assert person["name"] == "John"
    assert person["age"] == 30
    
    person = create_person("Jane", 25, city="New York", occupation="Engineer")
    assert person["name"] == "Jane"
    assert person["age"] == 25
    assert person["city"] == "New York"
    assert person["occupation"] == "Engineer"

def test_format_text():
    """Test function with default parameters"""
    assert format_text("hello") == "hello"
    assert format_text("hello", prefix="[", suffix="]") == "[hello]"
    assert format_text("hello", uppercase=True) == "HELLO"
    assert format_text("hello", reverse=True) == "olleh"
    assert format_text("hello", prefix="[", uppercase=True, reverse=True) == "[OLLEH]"

def test_process_numbers():
    """Test function with default parameters and type hints"""
    numbers = [1, 2, 3, 4, 5]
    assert process_numbers(numbers) == 15  # sum
    assert process_numbers(numbers, operation="product") == 120
    assert process_numbers(numbers, operation="average") == 3
    assert process_numbers(numbers, operation="max") == 5
    assert process_numbers(numbers, operation="min") == 1

def test_lambda_functions():
    """Test lambda function definitions"""
    assert square(5) == 25
    assert is_even(4) is True
    assert is_even(5) is False
    assert to_upper("hello") == "HELLO"

def test_main_function(capsys):
    """Test the main function's output"""
    main()
    captured = capsys.readouterr()
    assert "Total:" in captured.out
    assert "Person:" in captured.out
    assert "Formatted text:" in captured.out
    assert "Processed numbers:" in captured.out 