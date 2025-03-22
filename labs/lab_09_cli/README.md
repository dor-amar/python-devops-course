# Lab 9: Automating CLI Commands

This lab focuses on automating command-line interface (CLI) operations in Python, including subprocess management, shell commands, and CLI tool development.

## Requirements

1. Create a module for subprocess management with the following functions:
   - Running shell commands
   - Capturing command output
   - Handling command errors
   - Managing process lifecycle
   - Working with environment variables

2. Create a module for CLI tool development that includes:
   - Command-line argument parsing
   - Interactive prompts
   - Progress bars and spinners
   - Colorized output
   - Command history

3. Create a module for shell automation that includes:
   - File system operations
   - Process management
   - System information
   - Network operations
   - Logging and monitoring

## Directory Structure

```
labs/lab_09_cli/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Subprocess management
    ├── exercise2.py  # CLI tool development
    └── exercise3.py  # Shell automation
```

## Dependencies

- click
- rich
- prompt-toolkit
- psutil
- pyyaml
- pytest 