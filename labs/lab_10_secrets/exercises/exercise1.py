"""Environment variable management module."""

import os
import logging
from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from datetime import datetime


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


T = TypeVar('T')


@dataclass
class EnvironmentConfig:
    """Configuration class for environment variables."""

    def __post_init__(self):
        """Validate configuration after initialization."""
        self.validate()

    def validate(self) -> None:
        """Validate the configuration."""
        for field_name, field_value in self.__dict__.items():
            if field_value is None:
                raise ValueError(f"Required environment variable '{field_name}' is not set")


class EnvironmentManager:
    """Manager for handling environment variables."""

    def __init__(
        self,
        env_file: Optional[str] = None,
        env_prefix: str = "",
        required_vars: Optional[List[str]] = None
    ):
        """Initialize the environment manager.

        Args:
            env_file: Path to .env file
            env_prefix: Prefix for environment variables
            required_vars: List of required environment variables
        """
        self.env_prefix = env_prefix
        self.required_vars = required_vars or []
        self._load_env_file(env_file)
        self._validate_required_vars()

    def _load_env_file(self, env_file: Optional[str]) -> None:
        """Load environment variables from file.

        Args:
            env_file: Path to .env file
        """
        if env_file:
            env_path = Path(env_file)
            if not env_path.exists():
                raise FileNotFoundError(f"Environment file not found: {env_file}")
            load_dotenv(env_path)
        else:
            # Try to find .env file in current directory
            env_path = find_dotenv()
            if env_path:
                load_dotenv(env_path)

    def _validate_required_vars(self) -> None:
        """Validate that all required variables are set."""
        missing_vars = []
        for var in self.required_vars:
            if not self.get(var):
                missing_vars.append(var)

        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

    def _get_key(self, key: str) -> str:
        """Get the full environment variable key with prefix.

        Args:
            key: Environment variable name

        Returns:
            str: Full environment variable key
        """
        return f"{self.env_prefix}{key}" if self.env_prefix else key

    def get(
        self,
        key: str,
        default: Any = None,
        type_: Optional[Type[T]] = None
    ) -> Optional[T]:
        """Get an environment variable value.

        Args:
            key: Environment variable name
            default: Default value if not found
            type_: Type to convert the value to

        Returns:
            Optional[T]: Environment variable value
        """
        full_key = self._get_key(key)
        value = os.getenv(full_key, default)

        if value is None:
            return None

        if type_:
            try:
                if type_ == bool:
                    return self._parse_bool(value)
                elif type_ == list:
                    return self._parse_list(value)
                elif type_ == datetime:
                    return datetime.fromisoformat(value)
                else:
                    return type_(value)
            except (ValueError, TypeError) as e:
                logger.warning(f"Failed to convert {value} to {type_}: {e}")
                return default

        return value

    def get_int(self, key: str, default: Optional[int] = None) -> Optional[int]:
        """Get an integer environment variable.

        Args:
            key: Environment variable name
            default: Default value if not found

        Returns:
            Optional[int]: Integer value
        """
        return self.get(key, default, int)

    def get_float(self, key: str, default: Optional[float] = None) -> Optional[float]:
        """Get a float environment variable.

        Args:
            key: Environment variable name
            default: Default value if not found

        Returns:
            Optional[float]: Float value
        """
        return self.get(key, default, float)

    def get_bool(self, key: str, default: Optional[bool] = None) -> Optional[bool]:
        """Get a boolean environment variable.

        Args:
            key: Environment variable name
            default: Default value if not found

        Returns:
            Optional[bool]: Boolean value
        """
        return self.get(key, default, bool)

    def get_list(self, key: str, default: Optional[List[str]] = None) -> Optional[List[str]]:
        """Get a list environment variable.

        Args:
            key: Environment variable name
            default: Default value if not found

        Returns:
            Optional[List[str]]: List value
        """
        return self.get(key, default, list)

    def get_datetime(self, key: str, default: Optional[datetime] = None) -> Optional[datetime]:
        """Get a datetime environment variable.

        Args:
            key: Environment variable name
            default: Default value if not found

        Returns:
            Optional[datetime]: Datetime value
        """
        return self.get(key, default, datetime)

    def set(self, key: str, value: Any) -> None:
        """Set an environment variable.

        Args:
            key: Environment variable name
            value: Value to set
        """
        full_key = self._get_key(key)
        os.environ[full_key] = str(value)

    def unset(self, key: str) -> None:
        """Remove an environment variable.

        Args:
            key: Environment variable name
        """
        full_key = self._get_key(key)
        os.environ.pop(full_key, None)

    def to_dict(self) -> Dict[str, Any]:
        """Convert environment variables to dictionary.

        Returns:
            Dict[str, Any]: Dictionary of environment variables
        """
        return {
            k: v for k, v in os.environ.items()
            if not self.env_prefix or k.startswith(self.env_prefix)
        }

    @staticmethod
    def _parse_bool(value: str) -> bool:
        """Parse a boolean value.

        Args:
            value: String value to parse

        Returns:
            bool: Parsed boolean value
        """
        value = value.lower()
        if value in ('true', '1', 'yes', 'on'):
            return True
        if value in ('false', '0', 'no', 'off'):
            return False
        raise ValueError(f"Invalid boolean value: {value}")

    @staticmethod
    def _parse_list(value: str) -> List[str]:
        """Parse a list value.

        Args:
            value: String value to parse

        Returns:
            List[str]: Parsed list value
        """
        return [item.strip() for item in value.split(',')]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize environment manager
        env = EnvironmentManager(
            env_prefix="APP_",
            required_vars=["API_KEY", "DATABASE_URL"]
        )

        # Set some environment variables
        env.set("API_KEY", "secret123")
        env.set("DATABASE_URL", "postgresql://user:pass@localhost:5432/db")
        env.set("DEBUG", "true")
        env.set("PORT", "8080")
        env.set("ALLOWED_HOSTS", "localhost,127.0.0.1")

        # Get values with type conversion
        print("Environment Variables:")
        print(f"API Key: {env.get('API_KEY')}")
        print(f"Database URL: {env.get('DATABASE_URL')}")
        print(f"Debug Mode: {env.get_bool('DEBUG')}")
        print(f"Port: {env.get_int('PORT')}")
        print(f"Allowed Hosts: {env.get_list('ALLOWED_HOSTS')}")

        # Convert to dictionary
        print("\nEnvironment Dictionary:")
        print(env.to_dict())

    except Exception as e:
        print(f"Error: {e}") 