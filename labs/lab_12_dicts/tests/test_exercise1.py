"""Tests for Exercise 1: Basic Dictionary Operations."""

import pytest
from exercises.exercise1 import (
    create_student_record,
    update_student_grade,
    calculate_average_grade,
    merge_student_records
)


def test_create_student_record():
    """Test creating a student record."""
    record = create_student_record("John", 20, [85.5, 90.0, 88.5])
    assert record == {
        "name": "John",
        "age": 20,
        "grades": [85.5, 90.0, 88.5]
    }


def test_update_student_grade():
    """Test updating student grade."""
    record = {
        "name": "John",
        "age": 20,
        "grades": [85.5, 90.0]
    }
    updated = update_student_grade(record, 95.0)
    assert updated["grades"] == [85.5, 90.0, 95.0]


def test_calculate_average_grade():
    """Test calculating average grade."""
    record = {
        "name": "John",
        "age": 20,
        "grades": [85.5, 90.0, 88.5]
    }
    assert calculate_average_grade(record) == 88.0


def test_merge_student_records():
    """Test merging student records."""
    record1 = {
        "name": "John",
        "age": 20,
        "grades": [85.5, 90.0]
    }
    record2 = {
        "name": "John",
        "age": 20,
        "grades": [88.5, 95.0]
    }
    merged = merge_student_records(record1, record2)
    assert merged["grades"] == [85.5, 90.0, 88.5, 95.0] 