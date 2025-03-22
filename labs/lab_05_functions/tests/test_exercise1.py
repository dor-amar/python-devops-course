"""Tests for basic functions and arguments."""

import unittest
from exercises.exercise1 import calculate_bmi, greet, sum_numbers, create_person


class TestCalculateBMI(unittest.TestCase):
    """Test cases for calculate_bmi function."""

    def test_valid_inputs(self):
        """Test BMI calculation with valid inputs."""
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.857142857)
        self.assertAlmostEqual(calculate_bmi(65, 1.65), 23.875114784)

    def test_invalid_inputs(self):
        """Test BMI calculation with invalid inputs."""
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)


class TestGreet(unittest.TestCase):
    """Test cases for greet function."""

    def test_default_greeting(self):
        """Test greeting with default argument."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_custom_greeting(self):
        """Test greeting with custom greeting word."""
        self.assertEqual(greet("Alice", "Hi"), "Hi, Alice!")
        self.assertEqual(greet("Bob", "Good morning"), "Good morning, Bob!")

    def test_invalid_inputs(self):
        """Test greeting with invalid inputs."""
        with self.assertRaises(ValueError):
            greet("")
        with self.assertRaises(ValueError):
            greet(" ")


class TestSumNumbers(unittest.TestCase):
    """Test cases for sum_numbers function."""

    def test_single_number(self):
        """Test sum with single number."""
        self.assertEqual(sum_numbers(5), 5)
        self.assertEqual(sum_numbers(3.14), 3.14)

    def test_multiple_numbers(self):
        """Test sum with multiple numbers."""
        self.assertEqual(sum_numbers(1, 2, 3), 6)
        self.assertEqual(sum_numbers(1.1, 2.2, 3.3), 6.6)

    def test_invalid_inputs(self):
        """Test sum with invalid inputs."""
        with self.assertRaises(ValueError):
            sum_numbers()


class TestCreatePerson(unittest.TestCase):
    """Test cases for create_person function."""

    def test_basic_person(self):
        """Test creating person with required fields."""
        person = create_person("Alice", 25)
        self.assertEqual(person["name"], "Alice")
        self.assertEqual(person["age"], 25)

    def test_person_with_extra_fields(self):
        """Test creating person with additional fields."""
        person = create_person("Bob", 30, city="New York", occupation="Engineer")
        self.assertEqual(person["name"], "Bob")
        self.assertEqual(person["age"], 30)
        self.assertEqual(person["city"], "New York")
        self.assertEqual(person["occupation"], "Engineer")

    def test_invalid_inputs(self):
        """Test creating person with invalid inputs."""
        with self.assertRaises(ValueError):
            create_person("", 25)
        with self.assertRaises(ValueError):
            create_person("Alice", -25)


if __name__ == '__main__':
    unittest.main() 