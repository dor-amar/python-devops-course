"""Tests for Exercise 2: Dictionary Methods and Operations."""

import pytest
from exercises.exercise2 import (
    count_word_frequencies,
    invert_dictionary,
    find_common_keys,
    deep_update
)


def test_count_word_frequencies():
    """Test counting word frequencies."""
    text = "hello world hello python world"
    frequencies = count_word_frequencies(text)
    assert frequencies == {
        "hello": 2,
        "world": 2,
        "python": 1
    }


def test_invert_dictionary():
    """Test dictionary inversion."""
    d = {"a": 1, "b": 2, "c": 1}
    inverted = invert_dictionary(d)
    assert inverted == {
        1: ["a", "c"],
        2: ["b"]
    }


def test_find_common_keys():
    """Test finding common keys."""
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 4, "c": 5, "d": 6}
    common = find_common_keys(d1, d2)
    assert set(common) == {"b", "c"}


def test_deep_update():
    """Test deep dictionary update."""
    d1 = {
        "a": 1,
        "b": {
            "c": 2,
            "d": 3
        }
    }
    d2 = {
        "b": {
            "d": 4,
            "e": 5
        }
    }
    updated = deep_update(d1, d2)
    assert updated == {
        "a": 1,
        "b": {
            "c": 2,
            "d": 4,
            "e": 5
        }
    } 