"""
Tests for Exercise 2: Function Decorators and Closures
"""
import pytest
import time
from exercises.exercise2 import *

def test_timer_decorator(capsys):
    """Test the timer decorator"""
    @timer
    def test_function():
        time.sleep(0.1)
    
    test_function()
    captured = capsys.readouterr()
    assert "Execution time:" in captured.out

def test_memoize_decorator():
    """Test the memoize decorator"""
    @memoize
    def test_function(n):
        return n * 2
    
    # First call should compute
    result1 = test_function(5)
    # Second call should use cached result
    result2 = test_function(5)
    assert result1 == result2
    assert result1 == 10

def test_retry_decorator():
    """Test the retry decorator"""
    attempts = 0
    
    @retry(max_attempts=3)
    def test_function():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise Exception("Temporary failure")
        return True
    
    result = test_function()
    assert result is True
    assert attempts == 3

def test_counter_factory():
    """Test the counter factory"""
    counter = create_counter(5)
    assert counter() == 5
    assert counter() == 6
    assert counter() == 7
    
    # Test independent counters
    counter2 = create_counter(0)
    assert counter2() == 0
    assert counter() == 8

def test_multiplier_factory():
    """Test the multiplier factory"""
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    assert double(5) == 10
    assert double(10) == 20
    assert triple(5) == 15
    assert triple(10) == 30

def test_fibonacci():
    """Test the fibonacci function with decorators"""
    # First call should compute
    result1 = fibonacci(10)
    # Second call should use cached result
    result2 = fibonacci(10)
    assert result1 == result2
    assert result1 == 55

def test_unstable_function():
    """Test the unstable function with retry decorator"""
    result = unstable_function()
    assert result is True

def test_main_function(capsys):
    """Test the main function's output"""
    main()
    captured = capsys.readouterr()
    assert "Timer demo:" in captured.out
    assert "Memoize demo:" in captured.out
    assert "Retry demo:" in captured.out
    assert "Counter demo:" in captured.out
    assert "Multiplier demo:" in captured.out 