"""JSON operations module."""

import json
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from jsonschema import validate, ValidationError
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class JSONManager:
    """Manager for JSON operations."""

    def __init__(self):
        """Initialize the JSON manager."""
        self.schemas: Dict[str, Dict[str, Any]] = {}

    def load_json(self, file_path: Union[str, Path]) -> Any:
        """Load JSON data from a file.

        Args:
            file_path: Path to the JSON file

        Returns:
            Any: Parsed JSON data
        """
        with open(file_path, 'r') as f:
            return json.load(f)

    def save_json(
        self,
        data: Any,
        file_path: Union[str, Path],
        indent: int = 2
    ) -> None:
        """Save data to a JSON file.

        Args:
            data: Data to save
            file_path: Path to save the JSON file
            indent: Number of spaces for indentation
        """
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=indent)

    def dumps(self, data: Any, indent: int = 2) -> str:
        """Convert data to JSON string.

        Args:
            data: Data to convert
            indent: Number of spaces for indentation

        Returns:
            str: JSON string
        """
        return json.dumps(data, indent=indent)

    def loads(self, json_str: str) -> Any:
        """Parse JSON string to Python object.

        Args:
            json_str: JSON string to parse

        Returns:
            Any: Parsed data
        """
        return json.loads(json_str)

    def register_schema(self, name: str, schema: Dict[str, Any]) -> None:
        """Register a JSON schema.

        Args:
            name: Schema name
            schema: Schema definition
        """
        self.schemas[name] = schema

    def validate_data(
        self,
        data: Any,
        schema_name: str
    ) -> bool:
        """Validate data against a schema.

        Args:
            data: Data to validate
            schema_name: Name of the schema to use

        Returns:
            bool: True if valid, False otherwise
        """
        if schema_name not in self.schemas:
            raise ValueError(f"Schema '{schema_name}' not found")

        try:
            validate(instance=data, schema=self.schemas[schema_name])
            return True
        except ValidationError as e:
            console.print(f"[red]Validation error: {e}[/]")
            return False

    def pretty_print(self, data: Any) -> None:
        """Pretty print JSON data.

        Args:
            data: Data to print
        """
        console.print(json.dumps(data, indent=2))


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for special types."""

    def default(self, obj: Any) -> Any:
        """Convert special types to JSON-serializable format.

        Args:
            obj: Object to convert

        Returns:
            Any: JSON-serializable object
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class CustomJSONDecoder(json.JSONDecoder):
    """Custom JSON decoder for special types."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Initialize the decoder.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.parse_float = float
        self.parse_int = int
        self.parse_constant = lambda x: None if x == 'null' else x

    def decode(self, s: str) -> Any:
        """Decode JSON string to Python object.

        Args:
            s: JSON string to decode

        Returns:
            Any: Decoded object
        """
        obj = super().decode(s)
        return self._convert(obj)

    def _convert(self, obj: Any) -> Any:
        """Convert JSON object to Python object.

        Args:
            obj: Object to convert

        Returns:
            Any: Converted object
        """
        if isinstance(obj, dict):
            return {k: self._convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert(item) for item in obj]
        elif isinstance(obj, str):
            try:
                return datetime.fromisoformat(obj)
            except ValueError:
                return obj
        return obj


# Example usage
if __name__ == "__main__":
    try:
        # Initialize JSON manager
        json_manager = JSONManager()

        # Example data
        data = {
            "name": "John Doe",
            "age": 30,
            "email": "john@example.com",
            "created_at": datetime.now(),
            "hobbies": ["reading", "gaming", "coding"],
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "country": "USA"
            }
        }

        # Register schema
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer", "minimum": 0},
                "email": {"type": "string", "format": "email"},
                "created_at": {"type": "string", "format": "date-time"},
                "hobbies": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "address": {
                    "type": "object",
                    "properties": {
                        "street": {"type": "string"},
                        "city": {"type": "string"},
                        "country": {"type": "string"}
                    },
                    "required": ["street", "city", "country"]
                }
            },
            "required": ["name", "age", "email", "created_at", "hobbies", "address"]
        }
        json_manager.register_schema("user", schema)

        # Validate data
        console.print("\n[bold]Validating data...[/]")
        is_valid = json_manager.validate_data(data, "user")
        console.print(f"Data is {'valid' if is_valid else 'invalid'}")

        # Convert to JSON string
        console.print("\n[bold]Converting to JSON string...[/]")
        json_str = json_manager.dumps(data, cls=CustomJSONEncoder)
        console.print(json_str)

        # Parse JSON string
        console.print("\n[bold]Parsing JSON string...[/]")
        parsed_data = json_manager.loads(json_str)
        json_manager.pretty_print(parsed_data)

        # Save to file
        console.print("\n[bold]Saving to file...[/]")
        json_manager.save_json(data, "user.json", cls=CustomJSONEncoder)

        # Load from file
        console.print("\n[bold]Loading from file...[/]")
        loaded_data = json_manager.load_json("user.json")
        json_manager.pretty_print(loaded_data)

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 