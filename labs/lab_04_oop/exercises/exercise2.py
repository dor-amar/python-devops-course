"""
Exercise 2: Inheritance and Polymorphism

In this exercise, you will:
1. Create a shape hierarchy with abstract base class
2. Implement concrete shape classes
3. Use operator overloading
4. Demonstrate polymorphic behavior
"""

from abc import ABC, abstractmethod
from math import pi, sqrt
from typing import List, Optional, Union

class Shape(ABC):
    """
    Abstract base class for shapes
    """
    @property
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape"""
        pass
    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape"""
        pass
    
    def __str__(self) -> str:
        """Return string representation of the shape"""
        return f"{self.__class__.__name__}(area={self.area:.2f}, perimeter={self.perimeter:.2f})"
    
    def __repr__(self) -> str:
        """Return detailed string representation"""
        return str(self)
    
    def __lt__(self, other: 'Shape') -> bool:
        """Compare shapes by area"""
        return self.area < other.area
    
    def __eq__(self, other: object) -> bool:
        """Compare shapes by area"""
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area == other.area

class Circle(Shape):
    """
    Class representing a circle
    """
    def __init__(self, radius: float):
        # TODO: Initialize circle with radius
        pass
    
    @property
    def radius(self) -> float:
        """Get the radius of the circle"""
        # TODO: Implement radius property
        pass
    
    @radius.setter
    def radius(self, value: float) -> None:
        """Set the radius of the circle"""
        # TODO: Implement radius setter with validation
        pass
    
    @property
    def area(self) -> float:
        """Calculate the area of the circle"""
        # TODO: Implement area calculation
        pass
    
    @property
    def perimeter(self) -> float:
        """Calculate the perimeter of the circle"""
        # TODO: Implement perimeter calculation
        pass

class Rectangle(Shape):
    """
    Class representing a rectangle
    """
    def __init__(self, width: float, height: float):
        # TODO: Initialize rectangle with width and height
        pass
    
    @property
    def width(self) -> float:
        """Get the width of the rectangle"""
        # TODO: Implement width property
        pass
    
    @width.setter
    def width(self, value: float) -> None:
        """Set the width of the rectangle"""
        # TODO: Implement width setter with validation
        pass
    
    @property
    def height(self) -> float:
        """Get the height of the rectangle"""
        # TODO: Implement height property
        pass
    
    @height.setter
    def height(self, value: float) -> None:
        """Set the height of the rectangle"""
        # TODO: Implement height setter with validation
        pass
    
    @property
    def area(self) -> float:
        """Calculate the area of the rectangle"""
        # TODO: Implement area calculation
        pass
    
    @property
    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle"""
        # TODO: Implement perimeter calculation
        pass

class Triangle(Shape):
    """
    Class representing a triangle
    """
    def __init__(self, a: float, b: float, c: float):
        # TODO: Initialize triangle with three sides
        pass
    
    @property
    def sides(self) -> tuple[float, float, float]:
        """Get the sides of the triangle"""
        # TODO: Implement sides property
        pass
    
    @sides.setter
    def sides(self, value: tuple[float, float, float]) -> None:
        """Set the sides of the triangle"""
        # TODO: Implement sides setter with validation
        pass
    
    @property
    def area(self) -> float:
        """Calculate the area of the triangle using Heron's formula"""
        # TODO: Implement area calculation
        pass
    
    @property
    def perimeter(self) -> float:
        """Calculate the perimeter of the triangle"""
        # TODO: Implement perimeter calculation
        pass

class ShapeCollection:
    """
    Class representing a collection of shapes
    """
    def __init__(self):
        self.shapes: List[Shape] = []
    
    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the collection"""
        # TODO: Implement shape addition
        pass
    
    def remove_shape(self, shape: Shape) -> None:
        """Remove a shape from the collection"""
        # TODO: Implement shape removal
        pass
    
    def get_total_area(self) -> float:
        """Calculate the total area of all shapes"""
        # TODO: Implement total area calculation
        pass
    
    def get_total_perimeter(self) -> float:
        """Calculate the total perimeter of all shapes"""
        # TODO: Implement total perimeter calculation
        pass
    
    def get_largest_shape(self) -> Optional[Shape]:
        """Get the shape with the largest area"""
        # TODO: Implement largest shape finding
        pass
    
    def get_smallest_shape(self) -> Optional[Shape]:
        """Get the shape with the smallest area"""
        # TODO: Implement smallest shape finding
        pass

def main():
    """Demonstrate the use of the shape hierarchy"""
    # TODO: Create various shapes
    # TODO: Create a shape collection
    # TODO: Add shapes to the collection
    # TODO: Demonstrate area and perimeter calculations
    # TODO: Show shape comparisons
    # TODO: Test shape collection methods
    pass

if __name__ == "__main__":
    main() 