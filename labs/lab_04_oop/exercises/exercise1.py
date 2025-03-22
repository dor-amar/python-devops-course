"""
Exercise 1: Basic Classes and Objects

In this exercise, you will:
1. Create a class hierarchy for a library system
2. Use properties for data validation
3. Implement string representation methods
4. Use class methods and static methods
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict

@dataclass
class LibraryItem:
    """
    Base class for library items
    """
    title: str
    item_id: str
    status: str = "available"  # available, checked_out, reserved
    due_date: Optional[datetime] = None
    
    # TODO: Add properties for status and due_date with validation
    
    def __str__(self) -> str:
        """Return string representation of the item"""
        # TODO: Implement string representation
        pass
    
    def __repr__(self) -> str:
        """Return detailed string representation"""
        # TODO: Implement detailed string representation
        pass

class Book(LibraryItem):
    """
    Class representing a book in the library
    """
    def __init__(self, title: str, item_id: str, author: str, 
                 isbn: str, pages: int):
        # TODO: Initialize book with parent class and additional attributes
        pass
    
    # TODO: Add properties for isbn and pages with validation
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Create a Book instance from a dictionary"""
        # TODO: Implement class method to create book from dictionary
        pass
    
    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        """Validate ISBN format"""
        # TODO: Implement ISBN validation
        pass

class DVD(LibraryItem):
    """
    Class representing a DVD in the library
    """
    def __init__(self, title: str, item_id: str, director: str, 
                 runtime: int, rating: str):
        # TODO: Initialize DVD with parent class and additional attributes
        pass
    
    # TODO: Add properties for runtime and rating with validation
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'DVD':
        """Create a DVD instance from a dictionary"""
        # TODO: Implement class method to create DVD from dictionary
        pass
    
    @staticmethod
    def validate_rating(rating: str) -> bool:
        """Validate rating format"""
        # TODO: Implement rating validation
        pass

class Library:
    """
    Class representing a library
    """
    def __init__(self):
        self.items: List[LibraryItem] = []
    
    def add_item(self, item: LibraryItem) -> None:
        """Add an item to the library"""
        # TODO: Implement item addition
        pass
    
    def remove_item(self, item_id: str) -> None:
        """Remove an item from the library"""
        # TODO: Implement item removal
        pass
    
    def find_item(self, item_id: str) -> Optional[LibraryItem]:
        """Find an item by ID"""
        # TODO: Implement item search
        pass
    
    def checkout_item(self, item_id: str, days: int = 14) -> bool:
        """Check out an item"""
        # TODO: Implement item checkout
        pass
    
    def return_item(self, item_id: str) -> bool:
        """Return a checked out item"""
        # TODO: Implement item return
        pass
    
    def get_overdue_items(self) -> List[LibraryItem]:
        """Get list of overdue items"""
        # TODO: Implement overdue items check
        pass

def main():
    """Demonstrate the use of the library system"""
    # TODO: Create a library instance
    # TODO: Add some books and DVDs
    # TODO: Demonstrate checking out and returning items
    # TODO: Show string representations
    # TODO: Test class methods and static methods
    pass

if __name__ == "__main__":
    main() 