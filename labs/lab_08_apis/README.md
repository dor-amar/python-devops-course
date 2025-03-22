# Lab 8: Working with APIs

This lab focuses on working with APIs in Python, including making HTTP requests, handling responses, and working with different API formats.

## Requirements

1. Create a module for making HTTP requests with the following functions:
   - GET requests with query parameters
   - POST requests with JSON data
   - PUT requests for updating resources
   - DELETE requests
   - Handling different response formats (JSON, XML, text)
   - Error handling and status codes

2. Create a module for working with REST APIs that includes:
   - Authentication handling (Basic Auth, API Keys, OAuth)
   - Rate limiting and retries
   - Response caching
   - Request/response logging
   - Error handling and validation

3. Create a module for working with GraphQL APIs that includes:
   - Making GraphQL queries
   - Handling GraphQL mutations
   - Error handling
   - Response parsing

## Directory Structure

```
labs/lab_08_apis/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # HTTP requests and response handling
    ├── exercise2.py  # REST API operations
    └── exercise3.py  # GraphQL API operations
```

## Dependencies

- requests
- aiohttp
- graphql-core
- python-dotenv
- pytest
- pytest-asyncio 