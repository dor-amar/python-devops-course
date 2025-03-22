"""HTTP requests and response handling module."""

import json
import xml.etree.ElementTree as ET
from typing import Any, Dict, Optional, Union
import requests
from requests.exceptions import RequestException


class HTTPClient:
    """Client for making HTTP requests with response handling."""

    def __init__(self, base_url: str = "", timeout: int = 30):
        """Initialize the HTTP client.

        Args:
            base_url: Base URL for all requests
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _build_url(self, endpoint: str) -> str:
        """Build the full URL for a request.

        Args:
            endpoint: API endpoint

        Returns:
            str: Full URL
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request.

        Args:
            endpoint: API endpoint
            params: Query parameters

        Returns:
            Dict[str, Any]: Response data

        Raises:
            RequestException: If the request fails
        """
        try:
            response = self.session.get(
                self._build_url(endpoint),
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return self._parse_response(response)
        except RequestException as e:
            raise RequestException(f"GET request failed: {e}")

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
        try:
            response = self.session.post(
                self._build_url(endpoint),
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return self._parse_response(response)
        except RequestException as e:
            raise RequestException(f"POST request failed: {e}")

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
        try:
            response = self.session.put(
                self._build_url(endpoint),
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return self._parse_response(response)
        except RequestException as e:
            raise RequestException(f"PUT request failed: {e}")

    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request.

        Args:
            endpoint: API endpoint

        Returns:
            Dict[str, Any]: Response data

        Raises:
            RequestException: If the request fails
        """
        try:
            response = self.session.delete(
                self._build_url(endpoint),
                timeout=self.timeout
            )
            response.raise_for_status()
            return self._parse_response(response)
        except RequestException as e:
            raise RequestException(f"DELETE request failed: {e}")

    def _parse_response(self, response: requests.Response) -> Dict[str, Any]:
        """Parse the response based on content type.

        Args:
            response: Response object

        Returns:
            Dict[str, Any]: Parsed response data

        Raises:
            ValueError: If response format is not supported
        """
        content_type = response.headers.get('content-type', '').lower()

        if 'application/json' in content_type:
            return response.json()
        elif 'application/xml' in content_type or 'text/xml' in content_type:
            return self._parse_xml(response.text)
        elif 'text/plain' in content_type:
            return {'text': response.text}
        else:
            raise ValueError(f"Unsupported content type: {content_type}")

    def _parse_xml(self, xml_string: str) -> Dict[str, Any]:
        """Parse XML response into a dictionary.

        Args:
            xml_string: XML string to parse

        Returns:
            Dict[str, Any]: Parsed XML data
        """
        root = ET.fromstring(xml_string)
        return self._xml_to_dict(root)

    def _xml_to_dict(self, element: ET.Element) -> Dict[str, Any]:
        """Convert XML element to dictionary.

        Args:
            element: XML element to convert

        Returns:
            Dict[str, Any]: Converted dictionary
        """
        result = {}
        for child in element:
            if len(child) == 0:
                result[child.tag] = child.text
            else:
                result[child.tag] = self._xml_to_dict(child)
        return result


# Example usage
if __name__ == "__main__":
    try:
        # Initialize client with a test API
        client = HTTPClient("https://jsonplaceholder.typicode.com")

        # Test GET request
        print("Testing GET request:")
        posts = client.get("posts")
        print(f"Retrieved {len(posts)} posts")

        # Test POST request
        print("\nTesting POST request:")
        new_post = client.post("posts", {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        })
        print(f"Created post with ID: {new_post['id']}")

        # Test PUT request
        print("\nTesting PUT request:")
        updated_post = client.put(f"posts/{new_post['id']}", {
            "title": "Updated Post",
            "body": "This is an updated post",
            "userId": 1
        })
        print(f"Updated post: {updated_post['title']}")

        # Test DELETE request
        print("\nTesting DELETE request:")
        client.delete(f"posts/{new_post['id']}")
        print("Deleted post")

    except Exception as e:
        print(f"Error: {e}") 