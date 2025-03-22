"""
Tests for Exercise 2: Pattern Printing
"""
import pytest
from exercises.exercise2 import *

def test_right_triangle(capsys):
    """Test right-angled triangle pattern"""
    print_right_triangle(4)
    captured = capsys.readouterr()
    expected = """*
**
***
****
"""
    assert captured.out == expected

def test_pyramid(capsys):
    """Test pyramid pattern"""
    print_pyramid(4)
    captured = capsys.readouterr()
    expected = """   *
  ***
 *****
*******
"""
    assert captured.out == expected

def test_hollow_square(capsys):
    """Test hollow square pattern"""
    print_hollow_square(4)
    captured = capsys.readouterr()
    expected = """****
*  *
*  *
****
"""
    assert captured.out == expected

def test_main_function(capsys):
    """Test the main function's output"""
    # Mock input
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "3")
        main()
        
        # Capture printed output
        captured = capsys.readouterr()
        
        # Check if all patterns are present
        assert "*\n**\n***" in captured.out  # Right triangle
        assert "  *\n ***\n*****" in captured.out  # Pyramid
        assert "***\n* *\n***" in captured.out  # Hollow square 