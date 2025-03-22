"""Helper functions for formatting and validation."""

from typing import Any, Dict, Union
import re
from datetime import datetime


def format_output(data: Dict[str, Any], format_type: str = "json") -> Union[str, Dict[str, Any]]:
    """Format output data in specified format.

    Args:
        data: Data to format
        format_type: Output format type (json, pretty, minimal)

    Returns:
        Union[str, Dict[str, Any]]: Formatted output

    Raises:
        ValueError: If format type is not supported
    """
    if format_type == "json":
        return data
    elif format_type == "pretty":
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data
        }
    elif format_type == "minimal":
        return {k: v for k, v in data.items() if v is not None}
    else:
        raise ValueError(f"Unsupported format type: {format_type}")


def validate_input(data: Any, schema: Dict[str, Any]) -> bool:
    """Validate input data against a schema.

    Args:
        data: Data to validate
        schema: Validation schema

    Returns:
        bool: True if data is valid, False otherwise
    """
    if not isinstance(data, dict):
        return False

    for key, value in schema.items():
        if key not in data:
            return False
        
        if isinstance(value, type):
            if not isinstance(data[key], value):
                return False
        elif isinstance(value, dict):
            if not validate_input(data[key], value):
                return False
        elif callable(value):
            if not value(data[key]):
                return False

    return True


def sanitize_string(text: str) -> str:
    """Sanitize input string by removing special characters.

    Args:
        text: Input string to sanitize

    Returns:
        str: Sanitized string
    """
    # Remove special characters except alphanumeric, spaces, and basic punctuation
    return re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) 