"""Core functions for data processing and analysis."""

from typing import Any, Dict, List, Union
import json
from datetime import datetime


def process_data(data: Union[str, Dict[str, Any], List[Any]]) -> Dict[str, Any]:
    """Process input data and return structured output.

    Args:
        data: Input data in various formats (string, dict, list)

    Returns:
        Dict[str, Any]: Processed data with metadata

    Raises:
        ValueError: If data format is invalid
    """
    try:
        if isinstance(data, str):
            # Try to parse JSON string
            processed = json.loads(data)
        elif isinstance(data, (dict, list)):
            processed = data
        else:
            raise ValueError("Unsupported data type")

        return {
            "data": processed,
            "processed_at": datetime.now().isoformat(),
            "type": type(processed).__name__
        }
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON string")
    except Exception as e:
        raise ValueError(f"Error processing data: {str(e)}")


def analyze_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze processed data and generate insights.

    Args:
        data: Processed data dictionary

    Returns:
        Dict[str, Any]: Analysis results

    Raises:
        ValueError: If data is not properly processed
    """
    if "data" not in data:
        raise ValueError("Invalid data format: missing 'data' key")

    processed_data = data["data"]
    
    if isinstance(processed_data, list):
        return {
            "length": len(processed_data),
            "type": "list",
            "empty": len(processed_data) == 0
        }
    elif isinstance(processed_data, dict):
        return {
            "keys": list(processed_data.keys()),
            "type": "dict",
            "empty": len(processed_data) == 0
        }
    else:
        return {
            "type": type(processed_data).__name__,
            "value": str(processed_data)
        } 