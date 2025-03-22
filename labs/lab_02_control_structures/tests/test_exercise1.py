"""
Tests for Exercise 1: Number Classification
"""
import pytest
from exercises.exercise1 import *

def test_is_prime():
    """Test prime number detection"""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False

def test_classify_number():
    """Test number classification"""
    # Test positive numbers
    result = classify_number(2)
    assert result['sign'] == 'positive'
    assert result['parity'] == 'even'
    assert result['type'] == 'prime'

    result = classify_number(4)
    assert result['sign'] == 'positive'
    assert result['parity'] == 'even'
    assert result['type'] == 'composite'

    # Test negative numbers
    result = classify_number(-3)
    assert result['sign'] == 'negative'
    assert result['parity'] == 'odd'
    assert result['type'] == 'prime'

    # Test zero
    result = classify_number(0)
    assert result['sign'] == 'zero'
    assert result['parity'] == 'even'
    assert result['type'] == 'composite'

def test_main_function(capsys):
    """Test the main function's output"""
    # Mock input
    with pytest.MonkeyPatch.context() as m:
        m.setattr('builtins.input', lambda _: "7")
        main()
        
        # Capture printed output
        captured = capsys.readouterr()
        
        # Check if all expected outputs are present
        assert "positive" in captured.out
        assert "odd" in captured.out
        assert "prime" in captured.out 