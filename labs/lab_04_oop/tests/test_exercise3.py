"""Tests for Exercise 3: Advanced OOP Concepts"""

import unittest
import os
from typing import Any, Dict, List

from exercises.exercise3 import (
    ValidatedProperty, register_method, MethodRegistry,
    Singleton, DatabaseConnection, User, Logger, Application
)

class TestValidatedProperty(unittest.TestCase):
    def test_property_validation(self):
        class TestClass:
            value = ValidatedProperty(lambda x: x > 0, "Value must be positive")
            
            def __init__(self, value: int):
                self.value = value
        
        obj = TestClass(5)
        self.assertEqual(obj.value, 5)
        
        with self.assertRaises(ValueError):
            obj.value = -1

class TestMethodRegistry(unittest.TestCase):
    def test_method_registration(self):
        class TestClass(metaclass=MethodRegistry):
            @register_method("test")
            def test_method(self):
                return "test"
        
        obj = TestClass()
        self.assertTrue(hasattr(obj, "test_method"))
        self.assertEqual(obj.test_method(), "test")

class TestSingleton(unittest.TestCase):
    def test_singleton_pattern(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)
    
    def test_database_connection(self):
        db = DatabaseConnection()
        self.assertFalse(db.is_connected)
        
        db.connect()
        self.assertTrue(db.is_connected)
        
        db.disconnect()
        self.assertFalse(db.is_connected)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("John Doe", 30, "john@example.com", "password123")
    
    def test_age_validation(self):
        with self.assertRaises(ValueError):
            self.user.age = -1
    
    def test_email_validation(self):
        with self.assertRaises(ValueError):
            self.user.email = "invalid_email"
    
    def test_password_validation(self):
        with self.assertRaises(ValueError):
            self.user.password = "short"  # Too short
    
    def test_validate_method(self):
        self.assertTrue(self.user.validate())
    
    def test_save_method(self):
        self.assertTrue(self.user.save())

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test.log"
        self.logger = Logger(self.log_file)
    
    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_logging(self):
        test_message = "Test log message"
        self.logger.log(test_message)
        
        with open(self.log_file, "r") as f:
            content = f.read()
            self.assertIn(test_message, content)

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_logger_composition(self):
        self.assertIsInstance(self.app.logger, Logger)
    
    def test_run_method(self):
        self.app.run()
        self.assertTrue(os.path.exists(self.app.logger.filename))
        os.remove(self.app.logger.filename)

if __name__ == "__main__":
    unittest.main() 