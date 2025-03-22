"""REST API operations with authentication and advanced features."""

import json
import logging
import time
from typing import Any, Dict, Optional, Union
from functools import wraps
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from dotenv import load_dotenv
import os


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RESTClient:
    """Client for making authenticated REST API requests with advanced features."""

    def __init__(
        self,
        base_url: str,
        auth_type: str = "none",
        username: Optional[str] = None,
        password: Optional[str] = None,
        api_key: Optional[str] = None,
        token: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        cache_ttl: int = 300
    ):
        """Initialize the REST client.

        Args:
            base_url: Base URL for all requests
            auth_type: Type of authentication ("basic", "api_key", "oauth", "none")
            username: Username for basic auth
            password: Password for basic auth
            api_key: API key for API key auth
            token: OAuth token
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
            cache_ttl: Cache time-to-live in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.auth_type = auth_type
        self.username = username
        self.password = password
        self.api_key = api_key
        self.token = token
        self.timeout = timeout
        self.max_retries = max_retries
        self.cache_ttl = cache_ttl
        self.session = requests.Session()
        self.cache = {}
        self._setup_auth()

    def _setup_auth(self) -> None:
        """Set up authentication based on auth_type."""
        if self.auth_type == "basic" and self.username and self.password:
            self.session.auth = HTTPBasicAuth(self.username, self.password)
        elif self.auth_type == "api_key" and self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        elif self.auth_type == "oauth" and self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def _build_url(self, endpoint: str) -> str:
        """Build the full URL for a request.

        Args:
            endpoint: API endpoint

        Returns:
            str: Full URL
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _get_cached_response(self, key: str) -> Optional[Dict[str, Any]]:
        """Get cached response if available and not expired.

        Args:
            key: Cache key

        Returns:
            Optional[Dict[str, Any]]: Cached response if available and valid
        """
        if key in self.cache:
            data, timestamp = self.cache[key]
            if time.time() - timestamp < self.cache_ttl:
                return data
        return None

    def _cache_response(self, key: str, data: Dict[str, Any]) -> None:
        """Cache response data with timestamp.

        Args:
            key: Cache key
            data: Response data to cache
        """
        self.cache[key] = (data, time.time())

    def _log_request(self, method: str, url: str, **kwargs) -> None:
        """Log request details.

        Args:
            method: HTTP method
            url: Request URL
            **kwargs: Additional request parameters
        """
        logger.info(f"Making {method} request to {url}")
        if 'json' in kwargs:
            logger.debug(f"Request body: {json.dumps(kwargs['json'])}")

    def _log_response(self, response: requests.Response) -> None:
        """Log response details.

        Args:
            response: Response object
        """
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

    def _handle_rate_limit(self, response: requests.Response) -> None:
        """Handle rate limiting headers.

        Args:
            response: Response object
        """
        if response.status_code == 429:  # Too Many Requests
            retry_after = int(response.headers.get('Retry-After', 60))
            logger.warning(f"Rate limited. Waiting {retry_after} seconds.")
            time.sleep(retry_after)

    @staticmethod
    def retry_on_failure(max_retries: int = 3, delay: int = 1):
        """Decorator for retrying failed requests.

        Args:
            max_retries: Maximum number of retry attempts
            delay: Delay between retries in seconds
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_retries):
                    try:
                        return func(*args, **kwargs)
                    except RequestException as e:
                        if attempt == max_retries - 1:
                            raise
                        logger.warning(f"Request failed, retrying... ({attempt + 1}/{max_retries})")
                        time.sleep(delay)
                return None
            return wrapper
        return decorator

    @retry_on_failure()
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, use_cache: bool = True) -> Dict[str, Any]:
        """Make a GET request with caching.

        Args:
            endpoint: API endpoint
            params: Query parameters
            use_cache: Whether to use cached response

        Returns:
            Dict[str, Any]: Response data

        Raises:
            RequestException: If the request fails
        """
        url = self._build_url(endpoint)
        cache_key = f"GET:{url}:{json.dumps(params or {})}"

        if use_cache:
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                logger.info("Using cached response")
                return cached_response

        self._log_request("GET", url, params=params)
        response = self.session.get(url, params=params, timeout=self.timeout)
        self._log_response(response)
        self._handle_rate_limit(response)
        response.raise_for_status()

        data = response.json()
        if use_cache:
            self._cache_response(cache_key, data)
        return data

    @retry_on_failure()
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a POST request.

        Args:
            endpoint: API endpoint
            data: Request data

        Returns:
            Dict[str, Any]: Response data

        Raises:
            RequestException: If the request fails
        """
        url = self._build_url(endpoint)
        self._log_request("POST", url, json=data)
        response = self.session.post(url, json=data, timeout=self.timeout)
        self._log_response(response)
        self._handle_rate_limit(response)
        response.raise_for_status()
        return response.json()

    @retry_on_failure()
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a PUT request.

        Args:
            endpoint: API endpoint
            data: Request data

        Returns:
            Dict[str, Any]: Response data

        Raises:
            RequestException: If the request fails
        """
        url = self._build_url(endpoint)
        self._log_request("PUT", url, json=data)
        response = self.session.put(url, json=data, timeout=self.timeout)
        self._log_response(response)
        self._handle_rate_limit(response)
        response.raise_for_status()
        return response.json()

    @retry_on_failure()
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request.

        Args:
            endpoint: API endpoint

        Returns:
            Dict[str, Any]: Response data

        Raises:
            RequestException: If the request fails
        """
        url = self._build_url(endpoint)
        self._log_request("DELETE", url)
        response = self.session.delete(url, timeout=self.timeout)
        self._log_response(response)
        self._handle_rate_limit(response)
        response.raise_for_status()
        return response.json()


# Example usage
if __name__ == "__main__":
    try:
        # Load environment variables
        load_dotenv()

        # Initialize client with authentication
        client = RESTClient(
            base_url="https://api.example.com",
            auth_type="api_key",
            api_key=os.getenv("API_KEY"),
            max_retries=3,
            cache_ttl=300
        )

        # Test GET request with caching
        print("Testing GET request with caching:")
        data = client.get("users", params={"page": 1})
        print(f"Retrieved {len(data)} users")

        # Test POST request
        print("\nTesting POST request:")
        new_user = client.post("users", {
            "name": "John Doe",
            "email": "john@example.com"
        })
        print(f"Created user with ID: {new_user['id']}")

        # Test PUT request
        print("\nTesting PUT request:")
        updated_user = client.put(f"users/{new_user['id']}", {
            "name": "John Smith",
            "email": "john.smith@example.com"
        })
        print(f"Updated user: {updated_user['name']}")

        # Test DELETE request
        print("\nTesting DELETE request:")
        client.delete(f"users/{new_user['id']}")
        print("Deleted user")

    except Exception as e:
        print(f"Error: {e}") 