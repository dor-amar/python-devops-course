"""
Exercise 3: Module Search Path and Importing

This exercise focuses on understanding Python's module search path
and different importing techniques.

Learning objectives:
- Understanding sys.path
- Absolute vs relative imports
- Import hooks
- Module reloading
"""

# TODO: Create the following directory structure:
"""
custom_modules/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── constants.py
├── helpers/
│   ├── __init__.py
│   ├── logger.py
│   └── utils.py
└── main.py

Requirements:
1. Implement proper relative imports between modules
2. Create circular import example and fix it
3. Implement lazy loading for heavy modules
4. Add module search path manipulation
"""

def explore_module_path():
    """
    TODO: Implement function to explore module search path
    
    Requirements:
    1. Print current search path
    2. Add new directories to search path
    3. Demonstrate import behavior changes
    """
    pass


def test_imports():
    """
    TODO: Implement different import scenarios
    
    Requirements:
    1. Test absolute imports
    2. Test relative imports
    3. Test circular imports
    4. Test lazy loading
    """
    pass


def main():
    """
    TODO: Demonstrate different importing techniques
    
    Suggested demonstrations:
    1. Module search path manipulation
    2. Import error handling
    3. Module reloading
    4. Import hooks
    """
    pass


if __name__ == "__main__":
    main() 