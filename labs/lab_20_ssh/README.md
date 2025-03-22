# Lab 20: Automating SSH with Paramiko

This lab focuses on automating SSH operations using Paramiko in Python, including SSH connections, command execution, file transfers, and key-based authentication.

## Requirements

1. Create a module for basic SSH operations with the following features:
   - SSH connection management
   - Password authentication
   - Key-based authentication
   - Command execution
   - Session handling

2. Create a module for advanced SSH features that includes:
   - SFTP file transfers
   - Port forwarding
   - Channel management
   - Error handling
   - Connection pooling

3. Create a module for SSH automation that includes:
   - Batch command execution
   - File synchronization
   - Remote file operations
   - Logging and monitoring
   - Security best practices

## Directory Structure

```
labs/lab_20_ssh/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Basic SSH operations
    ├── exercise2.py  # Advanced SSH features
    └── exercise3.py  # SSH automation
```

## Dependencies

- pytest
- rich
- paramiko
- cryptography
- python-dotenv 