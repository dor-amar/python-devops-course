 

import unittest
import math
from typing import List

from exercises.exercise2 import Shape, Circle, Rectangle, Triangle, ShapeCollection

class TestShape(unittest.TestCase):
    def test_abstract_base_class(self):
        """Test that Shape is an abstract base class"""
        with self.assertRaises(TypeError):
            Shape()  # Should not be able to instantiate abstract class
    
    def test_abstract_methods(self):
        """Test that Shape requires implementation of abstract methods"""
        class IncompleteShape(Shape):
            def area(self) -> float:
                return 0.0
        
        with self.assertRaises(TypeError):
            IncompleteShape()  # Missing perimeter implementation

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(5.0)
    
    def test_initialization(self):
        self.assertEqual(self.circle.radius, 5.0)
        with self.assertRaises(ValueError):
            Circle(-1.0)
    
    def test_area(self):
        expected = math.pi * 25.0
        self.assertAlmostEqual(self.circle.area(), expected)
    
    def test_perimeter(self):
        expected = 2 * math.pi * 5.0
        self.assertAlmostEqual(self.circle.perimeter(), expected)
    
    def test_string_representation(self):
        expected = "Circle(radius=5.0)"
        self.assertEqual(str(self.circle), expected)
    
    def test_comparison(self):
        circle1 = Circle(5.0)
        circle2 = Circle(6.0)
        self.assertTrue(circle1 < circle2)
        self.assertFalse(circle2 < circle1)
        self.assertEqual(circle1, Circle(5.0))

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4.0, 6.0)
    
    def test_initialization(self):
        self.assertEqual(self.rectangle.width, 4.0)
        self.assertEqual(self.rectangle.height, 6.0)
        with self.assertRaises(ValueError):
            Rectangle(-1.0, 5.0)
        with self.assertRaises(ValueError):
            Rectangle(5.0, -1.0)
    
    def test_area(self):
        self.assertEqual(self.rectangle.area(), 24.0)
    
    def test_perimeter(self):
        self.assertEqual(self.rectangle.perimeter(), 20.0)
    
    def test_string_representation(self):
        expected = "Rectangle(width=4.0, height=6.0)"
        self.assertEqual(str(self.rectangle), expected)
    
    def test_comparison(self):
        rect1 = Rectangle(4.0, 6.0)
        rect2 = Rectangle(5.0, 7.0)
        self.assertTrue(rect1 < rect2)
        self.assertFalse(rect2 < rect1)
        self.assertEqual(rect1, Rectangle(4.0, 6.0))

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3.0, 4.0, 5.0)
    
    def test_initialization(self):
        self.assertEqual(self.triangle.side1, 3.0)
        self.assertEqual(self.triangle.side2, 4.0)
        self.assertEqual(self.triangle.side3, 5.0)
        with self.assertRaises(ValueError):
            Triangle(1.0, 1.0, 3.0)  # Invalid triangle
    
    def test_area(self):
        # Using Heron's formula
        s = (3.0 + 4.0 + 5.0) / 2
        expected = math.sqrt(s * (s - 3.0) * (s - 4.0) * (s - 5.0))
        self.assertAlmostEqual(self.triangle.area(), expected)
    
    def test_perimeter(self):
        self.assertEqual(self.triangle.perimeter(), 12.0)
    
    def test_string_representation(self):
        expected = "Triangle(side1=3.0, side2=4.0, side3=5.0)"
        self.assertEqual(str(self.triangle), expected)
    
    def test_comparison(self):
        tri1 = Triangle(3.0, 4.0, 5.0)
        tri2 = Triangle(4.0, 5.0, 6.0)
        self.assertTrue(tri1 < tri2)
        self.assertFalse(tri2 < tri1)
        self.assertEqual(tri1, Triangle(3.0, 4.0, 5.0))

class TestShapeCollection(unittest.TestCase):
    def setUp(self):
        self.collection = ShapeCollection()
        self.circle = Circle(5.0)
        self.rectangle = Rectangle(4.0, 6.0)
        self.triangle = Triangle(3.0, 4.0, 5.0)
    
    def test_add_shape(self):
        self.collection.add_shape(self.circle)
        self.collection.add_shape(self.rectangle)
        self.assertEqual(len(self.collection.shapes), 2)
    
    def test_remove_shape(self):
        self.collection.add_shape(self.circle)
        self.collection.remove_shape(self.circle)
        self.assertEqual(len(self.collection.shapes), 0)
    
    def test_total_area(self):
        self.collection.add_shape(self.circle)
        self.collection.add_shape(self.rectangle)
        expected = self.circle.area() + self.rectangle.area()
        self.assertAlmostEqual(self.collection.total_area(), expected)
    
    def test_total_perimeter(self):
        self.collection.add_shape(self.circle)
        self.collection.add_shape(self.rectangle)
        expected = self.circle.perimeter() + self.rectangle.perimeter()
        self.assertAlmostEqual(self.collection.total_perimeter(), expected)
    
    def test_sort_shapes(self):
        self.collection.add_shape(self.circle)
        self.collection.add_shape(self.rectangle)
        self.collection.add_shape(self.triangle)
        
        sorted_shapes = self.collection.sort_shapes()
        self.assertEqual(len(sorted_shapes), 3)
        self.assertTrue(sorted_shapes[0].area() <= sorted_shapes[1].area())
        self.assertTrue(sorted_shapes[1].area() <= sorted_shapes[2].area())

if __name__ == "__main__":
    unittest.main() 
"""
 