"""
Tests for Exercise 1: Variables and Data Types
"""
import pytest
from exercises.exercise1 import *

def test_variable_types():
    """Test that variables are declared with correct types"""
    assert isinstance(age, int)
    assert isinstance(height, float)
    assert isinstance(name, str)
    assert isinstance(is_student, bool)

def test_variable_values():
    """Test that variables have correct values"""
    assert age == 25
    assert height == 1.75
    assert name == "Python Learner"
    assert is_student is True

def test_arithmetic_operations():
    """Test arithmetic operations"""
    # Test addition
    assert age + int(height) == 26
    
    # Test multiplication
    assert age * 2 == 50
    
    # Test division
    assert height / 2 == 0.875 