# Lab 10: Environment Variables & Secrets Management

This lab focuses on managing environment variables and secrets in Python applications, including secure storage, retrieval, and best practices for handling sensitive data.

## Requirements

1. Create a module for environment variable management with the following functions:
   - Loading environment variables from files
   - Validation of required variables
   - Type conversion and validation
   - Default value handling
   - Environment-specific configurations

2. Create a module for secrets management that includes:
   - Secure storage of secrets
   - Encryption/decryption of sensitive data
   - Integration with secret management services
   - Key rotation and expiration
   - Audit logging

3. Create a module for configuration management that includes:
   - YAML/JSON configuration files
   - Environment-specific settings
   - Configuration validation
   - Dynamic configuration updates
   - Configuration templating

## Directory Structure

```
labs/lab_10_secrets/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Environment variable management
    ├── exercise2.py  # Secrets management
    └── exercise3.py  # Configuration management
```

## Dependencies

- python-dotenv
- cryptography
- pyyaml
- python-jose
- vault
- pytest 