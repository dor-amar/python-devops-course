"""Tests for Exercise 3: Advanced Dictionary Applications."""

import pytest
from exercises.exercise3 import (
    create_phone_book,
    find_duplicate_values,
    group_by_key,
    create_nested_structure
)


def test_create_phone_book():
    """Test phone book creation."""
    phone_book = create_phone_book()
    assert isinstance(phone_book, dict)
    assert len(phone_book) > 0
    assert all(isinstance(phone, str) for phone in phone_book.values())


def test_find_duplicate_values():
    """Test finding duplicate values."""
    d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    duplicates = find_duplicate_values(d)
    assert len(duplicates) == 2
    assert (1, ["a", "c"]) in duplicates
    assert (2, ["b", "e"]) in duplicates


def test_group_by_key():
    """Test grouping items by key."""
    items = [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 20},
        {"name": "Bob", "age": 25}
    ]
    grouped = group_by_key(items, "age")
    assert len(grouped) == 2
    assert len(grouped[20]) == 2
    assert len(grouped[25]) == 1


def test_create_nested_structure():
    """Test creating nested structure."""
    data = [
        ("fruits", "apple", "red"),
        ("fruits", "banana", "yellow"),
        ("vegetables", "carrot", "orange")
    ]
    nested = create_nested_structure(data)
    assert nested == {
        "fruits": {
            "apple": "red",
            "banana": "yellow"
        },
        "vegetables": {
            "carrot": "orange"
        }
    } 