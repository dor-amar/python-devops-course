"""Example package demonstrating Python package structure."""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .core.functions import process_data, analyze_data
from .utils.helpers import format_output, validate_input

__all__ = [
    'process_data',
    'analyze_data',
    'format_output',
    'validate_input'
] 