"""
Tests for Exercise 3: Menu-Driven Calculator
"""
import pytest
from exercises.exercise3 import *

def test_get_number_input():
    """Test number input validation"""
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "123.45")
        assert get_number_input("Enter number: ") == 123.45

    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "abc")
        with pytest.raises(ValueError):
            get_number_input("Enter number: ")

def test_get_operation_input():
    """Test operation input validation"""
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "+")
        assert get_operation_input() == "+"

    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "q")
        assert get_operation_input() == "q"

    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "invalid")
        with pytest.raises(ValueError):
            get_operation_input()

def test_perform_operation():
    """Test arithmetic operations"""
    assert perform_operation("+", 5, 3) == 8
    assert perform_operation("-", 5, 3) == 2
    assert perform_operation("*", 5, 3) == 15
    assert perform_operation("/", 6, 2) == 3

    with pytest.raises(ValueError):
        perform_operation("invalid", 5, 3)

    with pytest.raises(ZeroDivisionError):
        perform_operation("/", 5, 0)

def test_main_function(capsys):
    """Test the main function's output"""
    # Mock inputs for a complete calculation
    inputs = ["+", "5", "3", "q"]
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: inputs.pop(0))
        main()
        
        # Capture printed output
        captured = capsys.readouterr()
        
        # Check if menu and result are present
        assert "Calculator Menu" in captured.out
        assert "Result: 8" in captured.out
        assert "Goodbye!" in captured.out 