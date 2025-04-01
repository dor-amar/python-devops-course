"""
Object-Oriented Programming Exercises

Practice creating classes, inheritance, and OOP concepts.
"""

class Vehicle:
    """
    TODO: Create a base Vehicle class with:
    - Attributes: make, model, year, fuel_type
    - Methods: start_engine(), stop_engine(), fuel_up()
    - Properties for mileage and fuel_level
    """
    pass

class Car(Vehicle):
    """
    TODO: Create a Car class that inherits from Vehicle:
    - Add attributes: num_doors, trunk_capacity
    - Add methods: open_trunk(), close_trunk()
    - Override fuel_up() with specific car logic
    """
    pass

class ElectricCar(Car):
    """
    TODO: Create an ElectricCar class:
    - Override fuel_type to always be 'electric'
    - Add battery_capacity and charge_level attributes
    - Add charge() method instead of fuel_up()
    - Add range_remaining() method
    """
    pass

class Garage:
    """
    TODO: Create a Garage class that can:
    - Store multiple vehicles
    - Track available spaces
    - Park and remove vehicles
    - List all vehicles by type
    - Calculate total value of stored vehicles
    """
    pass

def main():
    """
    TODO: Implement test scenarios:
    1. Create different types of vehicles
    2. Demonstrate inheritance
    3. Use properties and methods
    4. Handle a garage of vehicles
    5. Show error handling
    """
    pass

if __name__ == "__main__":
    main() 