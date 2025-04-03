"""
Exercise 4: JSON Configuration Manager

Create a configuration management system using JSON.

TODO:
1. Create functions to load configuration from JSON
2. Implement configuration validation
3. Add support for default values
4. Handle configuration updates
5. Implement configuration backup
"""

class ConfigManager:
    """
    TODO: Implement a configuration manager class that:
    - Loads config from JSON file
    - Validates configuration
    - Provides access to config values
    - Handles updates and backups
    """
    
    def __init__(self, config_path: str):
        """
        TODO: Initialize the config manager
        - Load initial configuration
        - Set up defaults
        - Create backup if needed
        """
        pass
    
    def get_value(self, key: str, default: any = None) -> any:
        """
        TODO: Get a configuration value
        - Handle nested keys
        - Return default if not found
        - Support type conversion
        """
        pass
    
    def update_value(self, key: str, value: any) -> bool:
        """
        TODO: Update a configuration value
        - Validate new value
        - Update the file
        - Create backup
        """
        pass

def main():
    """
    Test your implementation:
    1. Create sample config
    2. Read values
    3. Update values
    4. Test backup/restore
    """
    pass

if __name__ == "__main__":
    main() 