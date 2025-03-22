"""Basic dictionary operations module."""

from typing import Any, Dict, List, Optional, TypeVar, Union
from collections import defaultdict
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table


# Initialize Rich console
console = Console()


T = TypeVar('T')


@dataclass
class DictStats:
    """Statistics about a dictionary."""

    key_count: int
    value_types: Dict[str, int]
    nested_depth: int
    total_size: int


class DictOperations:
    """Class for basic dictionary operations."""

    def __init__(self):
        """Initialize the dictionary operations class."""
        self._dicts: Dict[str, Dict[str, Any]] = {}

    def create_dict(
        self,
        name: str,
        initial_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new dictionary.

        Args:
            name: Name of the dictionary
            initial_data: Initial data for the dictionary

        Returns:
            Dict[str, Any]: Created dictionary
        """
        self._dicts[name] = initial_data or {}
        return self._dicts[name]

    def create_default_dict(
        self,
        name: str,
        default_factory: type
    ) -> defaultdict:
        """Create a new defaultdict.

        Args:
            name: Name of the dictionary
            default_factory: Default value factory

        Returns:
            defaultdict: Created defaultdict
        """
        self._dicts[name] = defaultdict(default_factory)
        return self._dicts[name]

    def get_dict(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a dictionary by name.

        Args:
            name: Name of the dictionary

        Returns:
            Optional[Dict[str, Any]]: Dictionary if found
        """
        return self._dicts.get(name)

    def set_value(
        self,
        name: str,
        key: str,
        value: Any,
        create_missing: bool = True
    ) -> None:
        """Set a value in a dictionary.

        Args:
            name: Name of the dictionary
            key: Key to set
            value: Value to set
            create_missing: Whether to create missing dictionary
        """
        if create_missing and name not in self._dicts:
            self.create_dict(name)
        self._dicts[name][key] = value

    def get_value(
        self,
        name: str,
        key: str,
        default: Any = None
    ) -> Any:
        """Get a value from a dictionary.

        Args:
            name: Name of the dictionary
            key: Key to get
            default: Default value if key not found

        Returns:
            Any: Value if found, default otherwise
        """
        return self._dicts.get(name, {}).get(key, default)

    def delete_key(self, name: str, key: str) -> bool:
        """Delete a key from a dictionary.

        Args:
            name: Name of the dictionary
            key: Key to delete

        Returns:
            bool: True if key was deleted
        """
        if name in self._dicts and key in self._dicts[name]:
            del self._dicts[name][key]
            return True
        return False

    def merge_dicts(
        self,
        target: str,
        source: str,
        overwrite: bool = True
    ) -> None:
        """Merge two dictionaries.

        Args:
            target: Name of target dictionary
            source: Name of source dictionary
            overwrite: Whether to overwrite existing keys
        """
        if target not in self._dicts:
            self.create_dict(target)
        if source not in self._dicts:
            return

        for key, value in self._dicts[source].items():
            if overwrite or key not in self._dicts[target]:
                self._dicts[target][key] = value

    def update_dict(
        self,
        name: str,
        update_data: Dict[str, Any],
        overwrite: bool = True
    ) -> None:
        """Update a dictionary with new data.

        Args:
            name: Name of the dictionary
            update_data: Data to update with
            overwrite: Whether to overwrite existing keys
        """
        if name not in self._dicts:
            self.create_dict(name)

        for key, value in update_data.items():
            if overwrite or key not in self._dicts[name]:
                self._dicts[name][key] = value

    def get_keys(self, name: str) -> List[str]:
        """Get all keys from a dictionary.

        Args:
            name: Name of the dictionary

        Returns:
            List[str]: List of keys
        """
        return list(self._dicts.get(name, {}).keys())

    def get_values(self, name: str) -> List[Any]:
        """Get all values from a dictionary.

        Args:
            name: Name of the dictionary

        Returns:
            List[Any]: List of values
        """
        return list(self._dicts.get(name, {}).values())

    def get_items(self, name: str) -> List[tuple]:
        """Get all items from a dictionary.

        Args:
            name: Name of the dictionary

        Returns:
            List[tuple]: List of (key, value) pairs
        """
        return list(self._dicts.get(name, {}).items())

    def clear_dict(self, name: str) -> None:
        """Clear a dictionary.

        Args:
            name: Name of the dictionary
        """
        if name in self._dicts:
            self._dicts[name].clear()

    def delete_dict(self, name: str) -> bool:
        """Delete a dictionary.

        Args:
            name: Name of the dictionary

        Returns:
            bool: True if dictionary was deleted
        """
        if name in self._dicts:
            del self._dicts[name]
            return True
        return False

    def get_dict_stats(self, name: str) -> DictStats:
        """Get statistics about a dictionary.

        Args:
            name: Name of the dictionary

        Returns:
            DictStats: Dictionary statistics
        """
        if name not in self._dicts:
            return DictStats(0, {}, 0, 0)

        d = self._dicts[name]
        value_types = {}
        for value in d.values():
            type_name = type(value).__name__
            value_types[type_name] = value_types.get(type_name, 0) + 1

        return DictStats(
            key_count=len(d),
            value_types=value_types,
            nested_depth=self._get_nested_depth(d),
            total_size=self._get_dict_size(d)
        )

    def _get_nested_depth(self, d: Dict[str, Any], current_depth: int = 0) -> int:
        """Get the maximum nested depth of a dictionary.

        Args:
            d: Dictionary to check
            current_depth: Current depth in recursion

        Returns:
            int: Maximum nested depth
        """
        if not isinstance(d, dict):
            return current_depth

        max_depth = current_depth
        for value in d.values():
            if isinstance(value, dict):
                max_depth = max(
                    max_depth,
                    self._get_nested_depth(value, current_depth + 1)
                )
        return max_depth

    def _get_dict_size(self, d: Dict[str, Any]) -> int:
        """Get the total size of a dictionary.

        Args:
            d: Dictionary to check

        Returns:
            int: Total size in bytes
        """
        size = 0
        for key, value in d.items():
            size += len(str(key)) + len(str(value))
            if isinstance(value, dict):
                size += self._get_dict_size(value)
        return size

    def display_dict(self, name: str) -> None:
        """Display a dictionary in a formatted table.

        Args:
            name: Name of the dictionary
        """
        if name not in self._dicts:
            console.print(f"[red]Dictionary '{name}' not found[/]")
            return

        table = Table(title=f"Dictionary: {name}")
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="green")
        table.add_column("Type", style="yellow")

        for key, value in self._dicts[name].items():
            table.add_row(
                str(key),
                str(value),
                type(value).__name__
            )

        console.print(table)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize dictionary operations
        dict_ops = DictOperations()

        # Create a dictionary
        print("Creating a dictionary:")
        d = dict_ops.create_dict("users", {
            "john": {"age": 30, "email": "john@example.com"},
            "jane": {"age": 25, "email": "jane@example.com"}
        })
        dict_ops.display_dict("users")

        # Create a defaultdict
        print("\nCreating a defaultdict:")
        dd = dict_ops.create_default_dict("counts", int)
        dd["a"] += 1
        dd["b"] += 2
        dict_ops.display_dict("counts")

        # Set and get values
        print("\nSetting and getting values:")
        dict_ops.set_value("users", "bob", {"age": 35, "email": "bob@example.com"})
        value = dict_ops.get_value("users", "bob")
        print(f"Retrieved value: {value}")

        # Merge dictionaries
        print("\nMerging dictionaries:")
        dict_ops.create_dict("extra_users", {
            "alice": {"age": 28, "email": "alice@example.com"}
        })
        dict_ops.merge_dicts("users", "extra_users")
        dict_ops.display_dict("users")

        # Get dictionary statistics
        print("\nDictionary statistics:")
        stats = dict_ops.get_dict_stats("users")
        print(f"Key count: {stats.key_count}")
        print(f"Value types: {stats.value_types}")
        print(f"Nested depth: {stats.nested_depth}")
        print(f"Total size: {stats.total_size} bytes")

    except Exception as e:
        print(f"Error: {e}") 