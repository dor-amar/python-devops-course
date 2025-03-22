"""
Tests for Exercise 3: Type Conversion
"""
import pytest
from exercises.exercise3 import *

def test_convert_to_int():
    """Test string to integer conversion"""
    assert convert_to_int("123") == 123
    assert convert_to_int("-456") == -456
    with pytest.raises(ValueError):
        convert_to_int("abc")
    with pytest.raises(ValueError):
        convert_to_int("12.34")

def test_convert_to_float():
    """Test string to float conversion"""
    assert convert_to_float("123.45") == 123.45
    assert convert_to_float("-456.78") == -456.78
    assert convert_to_float("123") == 123.0
    with pytest.raises(ValueError):
        convert_to_float("abc")

def test_perform_calculations():
    """Test number calculations"""
    result = perform_calculations(10.0)
    assert result['square'] == 100.0
    assert result['half'] == 5.0
    assert result['rounded'] == 10

    result = perform_calculations(3.7)
    assert result['square'] == 13.69
    assert result['half'] == 1.85
    assert result['rounded'] == 4

def test_main_function(capsys):
    """Test the main function's output"""
    # Mock input
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "10.5")
        main()
        
        # Capture printed output
        captured = capsys.readouterr()
        
        # Check if all expected outputs are present
        assert "10" in captured.out  # Integer conversion
        assert "10.5" in captured.out  # Float conversion
        assert "110.25" in captured.out  # Square
        assert "5.25" in captured.out  # Half
        assert "11" in captured.out  # Rounded 