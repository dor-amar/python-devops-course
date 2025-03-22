"""Tests for advanced function features."""

import unittest
from exercises.exercise2 import fibonacci, counter, validate_input, process_data


class TestFibonacci(unittest.TestCase):
    """Test cases for fibonacci function."""

    def test_fibonacci_sequence(self):
        """Test fibonacci sequence generation."""
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_invalid_input(self):
        """Test fibonacci with invalid input."""
        with self.assertRaises(ValueError):
            fibonacci(-1)


class TestCounter(unittest.TestCase):
    """Test cases for counter function."""

    def test_counter(self):
        """Test counter functionality."""
        count = counter()
        self.assertEqual(count(), 1)
        self.assertEqual(count(), 2)
        self.assertEqual(count(), 3)


class TestValidateInput(unittest.TestCase):
    """Test cases for validate_input decorator."""

    @validate_input
    def test_func(self, x: float, y: float) -> float:
        return x + y

    def test_validation(self):
        """Test input validation."""
        self.assertEqual(self.test_func(1, 2), 3)
        with self.assertRaises(ValueError):
            self.test_func(-1, 2)


class TestProcessData(unittest.TestCase):
    """Test cases for process_data function."""

    def test_data_processing(self):
        """Test data processing."""
        data = [
            {"id": 1, "name": "Alice"},
            {"name": "Bob"},  # Missing id
            "invalid"  # Not a dict
        ]
        valid, invalid = process_data(data)
        self.assertEqual(len(valid), 1)
        self.assertEqual(len(invalid), 2)


if __name__ == '__main__':
    unittest.main() 