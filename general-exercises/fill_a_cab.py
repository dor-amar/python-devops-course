"""Task: Cab Fare Calculator.

Implement a function to calculate cab fare based on distance and time.
"""

def fill_a_cab(distance: float, time: int) -> float:
    """Calculate cab fare based on distance and time.
    
    Pricing Rules:
    - Base fare: $2.50
    - $1.50 per kilometer for first 5 km
    - $1.00 per kilometer after 5 km
    - $0.50 per minute waiting time
    - Minimum fare: $5.00
    
    Args:
        distance (float): Distance in kilometers
        time (int): Waiting time in minutes
        
    Returns:
        float: Total fare
        
    Raises:
        ValueError: If distance or time is negative
        
    Example:
        >>> fill_a_cab(3.5, 5)
        8.75  # Base fare + 3.5km * $1.50 + 5min * $0.50
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        (3.5, 5),    # Should be $8.75
        (7.0, 10),   # Should be $16.50
        (1.0, 2),    # Should be $5.00 (minimum fare)
        (-1.0, 5),   # Should raise ValueError
        (5.0, -2),   # Should raise ValueError
    ]
    
    for distance, time in test_cases:
        try:
            fare = fill_a_cab(distance, time)
            print(f"Distance: {distance}km, Time: {time}min -> Fare: ${fare:.2f}")
        except Exception as e:
            print(f"Error for distance {distance}km, time {time}min: {str(e)}")


if __name__ == "__main__":
    main() 