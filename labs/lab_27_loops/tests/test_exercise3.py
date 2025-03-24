"""Tests for Exercise 3: Practical Applications."""

import pytest
import tempfile
import os
from exercises.exercise3 import (
    count_word_frequencies,
    number_guessing_game,
    generate_calendar,
    calculator
)


def test_count_word_frequencies():
    """Test word frequency counting."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("hello world\nhello python\nworld python")
        temp_file = f.name
    
    try:
        frequencies = count_word_frequencies(temp_file)
        assert frequencies == {
            "hello": 2,
            "world": 2,
            "python": 2
        }
    finally:
        os.unlink(temp_file)


def test_generate_calendar():
    """Test calendar generation."""
    calendar = generate_calendar(2024, 1)
    assert len(calendar) == 6  # 6 weeks
    assert len(calendar[0]) == 7  # 7 days
    assert calendar[0][0] is None  # First day is Monday
    assert calendar[0][1] == 1  # First day of month


def test_calculator(capsys, monkeypatch):
    """Test calculator functionality."""
    # Simulate user input
    inputs = iter(['5', '+', '3', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    calculator()
    captured = capsys.readouterr()
    assert "8" in captured.out 