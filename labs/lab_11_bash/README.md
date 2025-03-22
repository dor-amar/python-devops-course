# Lab 11: Writing Bash Scripts in Python

This lab focuses on writing Bash scripts in Python, including shell command execution, process management, and system automation capabilities.

## Requirements

1. Create a module for shell command execution with the following features:
   - Command execution with proper error handling
   - Input/output redirection
   - Process management and monitoring
   - Command piping and chaining
   - Background process handling

2. Create a module for shell script automation that includes:
   - Shell script generation
   - Command templating
   - Variable substitution
   - Conditional execution
   - Loop constructs

3. Create a module for system automation that includes:
   - File system operations
   - Process management
   - System monitoring
   - Log management
   - Service control

## Directory Structure

```
labs/lab_11_bash/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Shell command execution
    ├── exercise2.py  # Shell script automation
    └── exercise3.py  # System automation
```

## Dependencies

- psutil
- jinja2
- rich
- pytest 