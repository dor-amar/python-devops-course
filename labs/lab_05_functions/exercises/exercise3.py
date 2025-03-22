"""Practical applications of functions including statistics, data processing, and async operations."""

import asyncio
from typing import Any, Callable, Dict, List, Union
from statistics import mean, median, mode
from collections import Counter


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """Calculate mean, median, and mode of a list of numbers.

    Args:
        numbers: List of numbers to calculate statistics for

    Returns:
        Dict[str, float]: Dictionary containing mean, median, and mode

    Raises:
        ValueError: If numbers list is empty
    """
    if not numbers:
        raise ValueError("List of numbers cannot be empty")

    try:
        return {
            "mean": mean(numbers),
            "median": median(numbers),
            "mode": mode(numbers)
        }
    except StatisticsError:
        return {
            "mean": mean(numbers),
            "median": median(numbers),
            "mode": None
        }


def filter_and_transform(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter and transform a list of dictionaries based on conditions.

    Args:
        data: List of dictionaries to process

    Returns:
        List[Dict[str, Any]]: Filtered and transformed data

    Raises:
        ValueError: If data is not a list
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # Example: Filter users over 18 and transform their data
    return [
        {
            "name": entry["name"].upper(),
            "age": entry["age"],
            "status": "adult" if entry["age"] >= 18 else "minor"
        }
        for entry in data
        if isinstance(entry, dict) and "name" in entry and "age" in entry
    ]


def create_calculator() -> Dict[str, Callable[[float, float], float]]:
    """Create a dictionary of mathematical operations using lambda functions.

    Returns:
        Dict[str, Callable[[float, float], float]]: Dictionary of mathematical operations
    """
    return {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float('inf'),
        "power": lambda x, y: x ** y,
        "average": lambda x, y: (x + y) / 2
    }


async def async_process_data(data: List[Any]) -> List[Any]:
    """Process data asynchronously with simulated delays.

    Args:
        data: List of items to process

    Returns:
        List[Any]: Processed data

    Raises:
        ValueError: If data is not a list
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    async def process_item(item: Any) -> Any:
        # Simulate some async processing
        await asyncio.sleep(0.1)
        if isinstance(item, (int, float)):
            return item * 2
        elif isinstance(item, str):
            return item.upper()
        return item

    tasks = [process_item(item) for item in data]
    return await asyncio.gather(*tasks) 