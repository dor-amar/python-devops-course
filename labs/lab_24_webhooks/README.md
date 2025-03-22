# Lab 24: Building HTTP Webhooks with Flask

This lab focuses on building HTTP webhooks using Flask, including webhook endpoints, request handling, security measures, and best practices for webhook implementation.

## Requirements

1. Create a module for basic webhook functionality with the following features:
   - Webhook endpoint creation
   - Request validation
   - Payload handling
   - Response formatting
   - Error handling

2. Create a module for webhook security that includes:
   - Signature verification
   - Authentication
   - Rate limiting
   - IP filtering
   - SSL/TLS enforcement

3. Create a module for advanced webhook features that includes:
   - Event handling
   - Retry mechanisms
   - Webhook logging
   - Monitoring
   - Testing utilities

## Directory Structure

```
labs/lab_24_webhooks/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Basic webhook functionality
    ├── exercise2.py  # Webhook security
    └── exercise3.py  # Advanced webhook features
```

## Dependencies

- pytest
- rich
- flask
- flask-limiter
- pyjwt
- cryptography
- python-dotenv
- requests
- pytest-flask 