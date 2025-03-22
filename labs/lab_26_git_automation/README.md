# Lab 26: Git Automation with GitPython

This lab focuses on automating Git operations using GitPython, including repository management, commit automation, branch operations, and workflow automation.

## Requirements

1. Create a module for basic Git operations with the following features:
   - Repository initialization
   - File staging
   - Commit creation
   - Branch management
   - Remote operations

2. Create a module for advanced Git automation that includes:
   - Commit message generation
   - Branch strategy automation
   - Merge conflict resolution
   - Tag management
   - Submodule handling

3. Create a module for Git workflow automation that includes:
   - Automated PR creation
   - Code review automation
   - Release management
   - Deployment integration
   - Status reporting

## Directory Structure

```
labs/lab_26_git_automation/
├── README.md
├── requirements.txt
└── exercises/
    ├── exercise1.py  # Basic Git operations
    ├── exercise2.py  # Advanced Git automation
    └── exercise3.py  # Git workflow automation
```

## Dependencies

- pytest
- rich
- gitpython
- python-dotenv
- jinja2
- requests
- pytest-git 