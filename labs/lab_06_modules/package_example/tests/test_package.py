"""Tests for example_package components."""

import unittest
from example_package.core.functions import process_data, analyze_data
from example_package.utils.helpers import format_output, validate_input, sanitize_string


class TestProcessData(unittest.TestCase):
    """Test cases for process_data function."""

    def test_process_dict(self):
        """Test processing dictionary data."""
        data = {"key": "value"}
        result = process_data(data)
        self.assertIn("data", result)
        self.assertIn("processed_at", result)
        self.assertEqual(result["type"], "dict")

    def test_process_list(self):
        """Test processing list data."""
        data = [1, 2, 3]
        result = process_data(data)
        self.assertIn("data", result)
        self.assertEqual(result["type"], "list")

    def test_process_json_string(self):
        """Test processing JSON string."""
        data = '{"key": "value"}'
        result = process_data(data)
        self.assertIn("data", result)
        self.assertEqual(result["type"], "dict")

    def test_invalid_input(self):
        """Test processing invalid input."""
        with self.assertRaises(ValueError):
            process_data(123)  # Invalid type


class TestAnalyzeData(unittest.TestCase):
    """Test cases for analyze_data function."""

    def test_analyze_list(self):
        """Test analyzing list data."""
        data = {"data": [1, 2, 3]}
        result = analyze_data(data)
        self.assertEqual(result["type"], "list")
        self.assertEqual(result["length"], 3)

    def test_analyze_dict(self):
        """Test analyzing dictionary data."""
        data = {"data": {"key": "value"}}
        result = analyze_data(data)
        self.assertEqual(result["type"], "dict")
        self.assertEqual(result["keys"], ["key"])

    def test_invalid_input(self):
        """Test analyzing invalid input."""
        with self.assertRaises(ValueError):
            analyze_data({"invalid": "data"})


class TestFormatOutput(unittest.TestCase):
    """Test cases for format_output function."""

    def test_json_format(self):
        """Test JSON format output."""
        data = {"key": "value"}
        result = format_output(data, "json")
        self.assertEqual(result, data)

    def test_pretty_format(self):
        """Test pretty format output."""
        data = {"key": "value"}
        result = format_output(data, "pretty")
        self.assertIn("timestamp", result)
        self.assertIn("data", result)

    def test_minimal_format(self):
        """Test minimal format output."""
        data = {"key": "value", "empty": None}
        result = format_output(data, "minimal")
        self.assertIn("key", result)
        self.assertNotIn("empty", result)

    def test_invalid_format(self):
        """Test invalid format type."""
        with self.assertRaises(ValueError):
            format_output({}, "invalid")


class TestValidateInput(unittest.TestCase):
    """Test cases for validate_input function."""

    def test_validate_with_schema(self):
        """Test validation with schema."""
        data = {"name": "John", "age": 30}
        schema = {"name": str, "age": int}
        self.assertTrue(validate_input(data, schema))

    def test_validate_invalid_data(self):
        """Test validation with invalid data."""
        data = {"name": "John", "age": "30"}
        schema = {"name": str, "age": int}
        self.assertFalse(validate_input(data, schema))

    def test_validate_missing_key(self):
        """Test validation with missing key."""
        data = {"name": "John"}
        schema = {"name": str, "age": int}
        self.assertFalse(validate_input(data, schema))


class TestSanitizeString(unittest.TestCase):
    """Test cases for sanitize_string function."""

    def test_sanitize_string(self):
        """Test string sanitization."""
        text = "Hello, World! @#$%^&*()"
        result = sanitize_string(text)
        self.assertEqual(result, "Hello, World! ")

    def test_sanitize_empty_string(self):
        """Test sanitizing empty string."""
        self.assertEqual(sanitize_string(""), "")

    def test_sanitize_with_numbers(self):
        """Test sanitizing string with numbers."""
        text = "Hello123! @#$%^&*()"
        result = sanitize_string(text)
        self.assertEqual(result, "Hello123! ")


if __name__ == '__main__':
    unittest.main() 