#!/bin/bash

# Exit on error
set -e

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install development dependencies
echo "Installing development dependencies..."
pip install -r requirements.txt

# Install package in development mode
echo "Installing package in development mode..."
pip install -e .

# Run tests
echo "Running tests..."
pytest

# Check code style
echo "Checking code style..."
black --check .
isort --check-only .

# Type checking
echo "Running type checks..."
mypy .

# Documentation checks
echo "Checking documentation..."
pydocstyle .

echo "Setup complete! Virtual environment is ready."
echo "To activate the environment, run: source venv/bin/activate" 