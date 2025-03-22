"""GraphQL API operations module."""

import json
import logging
from typing import Any, Dict, Optional, Union
import requests
from requests.exceptions import RequestException
from graphql import (
    parse,
    validate,
    execute,
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull
)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GraphQLClient:
    """Client for making GraphQL API requests."""

    def __init__(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30
    ):
        """Initialize the GraphQL client.

        Args:
            endpoint: GraphQL API endpoint
            headers: Additional headers for requests
            timeout: Request timeout in seconds
        """
        self.endpoint = endpoint
        self.headers = headers or {}
        self.timeout = timeout
        self.session = requests.Session()
        self.schema = None

    def _log_request(self, query: str, variables: Optional[Dict[str, Any]] = None) -> None:
        """Log request details.

        Args:
            query: GraphQL query
            variables: Query variables
        """
        logger.info("Making GraphQL request")
        logger.debug(f"Query: {query}")
        if variables:
            logger.debug(f"Variables: {json.dumps(variables)}")

    def _log_response(self, response: requests.Response) -> None:
        """Log response details.

        Args:
            response: Response object
        """
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")

    def _validate_query(self, query: str) -> None:
        """Validate GraphQL query against schema.

        Args:
            query: GraphQL query to validate

        Raises:
            ValueError: If query is invalid
        """
        if not self.schema:
            return

        try:
            ast = parse(query)
            validation_errors = validate(self.schema, ast)
            if validation_errors:
                raise ValueError(f"Invalid query: {validation_errors}")
        except Exception as e:
            raise ValueError(f"Query validation failed: {e}")

    def query(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        operation_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Execute a GraphQL query.

        Args:
            query: GraphQL query string
            variables: Query variables
            operation_name: Name of the operation to execute

        Returns:
            Dict[str, Any]: Query result

        Raises:
            RequestException: If the request fails
            ValueError: If the query is invalid
        """
        self._validate_query(query)
        self._log_request(query, variables)

        payload = {
            "query": query,
            "variables": variables or {},
        }
        if operation_name:
            payload["operationName"] = operation_name

        try:
            response = self.session.post(
                self.endpoint,
                json=payload,
                headers=self.headers,
                timeout=self.timeout
            )
            self._log_response(response)
            response.raise_for_status()
            result = response.json()

            if "errors" in result:
                raise ValueError(f"GraphQL errors: {json.dumps(result['errors'])}")

            return result.get("data", {})
        except RequestException as e:
            raise RequestException(f"GraphQL query failed: {e}")

    def mutation(
        self,
        mutation: str,
        variables: Optional[Dict[str, Any]] = None,
        operation_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Execute a GraphQL mutation.

        Args:
            mutation: GraphQL mutation string
            variables: Mutation variables
            operation_name: Name of the operation to execute

        Returns:
            Dict[str, Any]: Mutation result

        Raises:
            RequestException: If the request fails
            ValueError: If the mutation is invalid
        """
        return self.query(mutation, variables, operation_name)

    def set_schema(self, schema: GraphQLSchema) -> None:
        """Set the GraphQL schema for validation.

        Args:
            schema: GraphQL schema object
        """
        self.schema = schema


# Example schema definition
def create_example_schema() -> GraphQLSchema:
    """Create an example GraphQL schema.

    Returns:
        GraphQLSchema: Example schema
    """
    # Define types
    UserType = GraphQLObjectType(
        name='User',
        fields={
            'id': GraphQLField(GraphQLNonNull(GraphQLString)),
            'name': GraphQLField(GraphQLString),
            'email': GraphQLField(GraphQLString),
            'age': GraphQLField(GraphQLInt)
        }
    )

    # Define queries
    QueryType = GraphQLObjectType(
        name='Query',
        fields={
            'user': GraphQLField(
                UserType,
                args={'id': GraphQLNonNull(GraphQLString)},
                resolver=lambda root, info, id: {
                    'id': id,
                    'name': 'John Doe',
                    'email': 'john@example.com',
                    'age': 30
                }
            ),
            'users': GraphQLField(
                GraphQLList(UserType),
                resolver=lambda root, info: [
                    {
                        'id': '1',
                        'name': 'John Doe',
                        'email': 'john@example.com',
                        'age': 30
                    },
                    {
                        'id': '2',
                        'name': 'Jane Smith',
                        'email': 'jane@example.com',
                        'age': 25
                    }
                ]
            )
        }
    )

    return GraphQLSchema(query=QueryType)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize client
        client = GraphQLClient(
            endpoint="https://api.example.com/graphql",
            headers={"Authorization": "Bearer your-token"}
        )

        # Set up schema
        schema = create_example_schema()
        client.set_schema(schema)

        # Test query
        print("Testing GraphQL query:")
        query = """
        query GetUser($id: String!) {
            user(id: $id) {
                id
                name
                email
                age
            }
        }
        """
        result = client.query(query, variables={"id": "1"})
        print(f"Query result: {json.dumps(result, indent=2)}")

        # Test mutation
        print("\nTesting GraphQL mutation:")
        mutation = """
        mutation CreateUser($input: CreateUserInput!) {
            createUser(input: $input) {
                id
                name
                email
                age
            }
        }
        """
        result = client.mutation(
            mutation,
            variables={
                "input": {
                    "name": "New User",
                    "email": "new@example.com",
                    "age": 35
                }
            }
        )
        print(f"Mutation result: {json.dumps(result, indent=2)}")

    except Exception as e:
        print(f"Error: {e}") 