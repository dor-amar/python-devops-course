"""
Tests for Exercise 1: Basic Classes and Objects
"""

import unittest
from datetime import datetime, timedelta
from typing import Dict, Any

from exercises.exercise1 import LibraryItem, Book, DVD, Library

class TestLibraryItem(unittest.TestCase):
    def setUp(self):
        self.item = LibraryItem("Test Item", "ITEM001")
    
    def test_initialization(self):
        self.assertEqual(self.item.title, "Test Item")
        self.assertEqual(self.item.item_id, "ITEM001")
        self.assertEqual(self.item.status, "available")
        self.assertIsNone(self.item.due_date)
    
    def test_property_validation(self):
        with self.assertRaises(ValueError):
            self.item.title = ""
        
        with self.assertRaises(ValueError):
            self.item.item_id = ""
        
        with self.assertRaises(ValueError):
            self.item.status = "invalid_status"
    
    def test_string_representation(self):
        expected = "LibraryItem(title='Test Item', item_id='ITEM001', status='available')"
        self.assertEqual(str(self.item), expected)

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Python Programming", "BOOK001", "John Doe", "1234567890")
    
    def test_initialization(self):
        self.assertEqual(self.book.title, "Python Programming")
        self.assertEqual(self.book.item_id, "BOOK001")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.isbn, "1234567890")
    
    def test_isbn_validation(self):
        with self.assertRaises(ValueError):
            self.book.isbn = "123"  # Too short
    
    def test_from_dict(self):
        data = {
            "title": "New Book",
            "item_id": "BOOK002",
            "author": "Jane Doe",
            "isbn": "0987654321"
        }
        book = Book.from_dict(data)
        self.assertEqual(book.title, "New Book")
        self.assertEqual(book.item_id, "BOOK002")
        self.assertEqual(book.author, "Jane Doe")
        self.assertEqual(book.isbn, "0987654321")

class TestDVD(unittest.TestCase):
    def setUp(self):
        self.dvd = DVD("Python Tutorial", "DVD001", 120, "English")
    
    def test_initialization(self):
        self.assertEqual(self.dvd.title, "Python Tutorial")
        self.assertEqual(self.dvd.item_id, "DVD001")
        self.assertEqual(self.dvd.duration, 120)
        self.assertEqual(self.dvd.language, "English")
    
    def test_duration_validation(self):
        with self.assertRaises(ValueError):
            self.dvd.duration = -10
    
    def test_from_dict(self):
        data = {
            "title": "New DVD",
            "item_id": "DVD002",
            "duration": 90,
            "language": "Spanish"
        }
        dvd = DVD.from_dict(data)
        self.assertEqual(dvd.title, "New DVD")
        self.assertEqual(dvd.item_id, "DVD002")
        self.assertEqual(dvd.duration, 90)
        self.assertEqual(dvd.language, "Spanish")

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Python Programming", "BOOK001", "John Doe", "1234567890")
        self.dvd = DVD("Python Tutorial", "DVD001", 120, "English")
    
    def test_add_item(self):
        self.library.add_item(self.book)
        self.library.add_item(self.dvd)
        self.assertEqual(len(self.library.items), 2)
    
    def test_remove_item(self):
        self.library.add_item(self.book)
        self.library.remove_item("BOOK001")
        self.assertEqual(len(self.library.items), 0)
    
    def test_find_item(self):
        self.library.add_item(self.book)
        found = self.library.find_item("BOOK001")
        self.assertEqual(found, self.book)
    
    def test_checkout_return(self):
        self.library.add_item(self.book)
        self.library.checkout_item("BOOK001")
        self.assertEqual(self.book.status, "checked_out")
        self.assertIsNotNone(self.book.due_date)
        
        self.library.return_item("BOOK001")
        self.assertEqual(self.book.status, "available")
        self.assertIsNone(self.book.due_date)
    
    def test_overdue_items(self):
        self.library.add_item(self.book)
        self.library.checkout_item("BOOK001")
        self.book.due_date = datetime.now() - timedelta(days=15)
        
        overdue = self.library.get_overdue_items()
        self.assertEqual(len(overdue), 1)
        self.assertEqual(overdue[0], self.book)

if __name__ == "__main__":
    unittest.main() 