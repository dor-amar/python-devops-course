"""
Tests for Exercise 2: String Manipulation
"""
import pytest
from exercises.exercise2 import *

def test_convert_to_uppercase():
    """Test string conversion to uppercase"""
    assert convert_to_uppercase("hello") == "HELLO"
    assert convert_to_uppercase("Python") == "PYTHON"
    assert convert_to_uppercase("123") == "123"

def test_reverse_string():
    """Test string reversal"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("123") == "321"

def test_count_vowels():
    """Test vowel counting"""
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOU") == 5
    assert count_vowels("123") == 0

def test_main_function(capsys):
    """Test the main function's output"""
    # Mock input
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "Hello World")
        main()
        
        # Capture printed output
        captured = capsys.readouterr()
        
        # Check if all expected outputs are present
        assert "HELLO WORLD" in captured.out
        assert "DLROW OLLEH" in captured.out
        assert "3" in captured.out  # Number of vowels in "Hello World" 