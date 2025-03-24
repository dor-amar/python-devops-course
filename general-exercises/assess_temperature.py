"""Task: Temperature Assessment.

Implement a function to assess temperature and provide appropriate recommendations.
"""

def assess_temperature(temp: float, scale: str = 'C') -> str:
    """Assess temperature and provide recommendations.
    
    Temperature Ranges (in Celsius):
    - Below 0°C: "Freezing"
    - 0-10°C: "Very Cold"
    - 11-20°C: "Cold"
    - 21-25°C: "Mild"
    - 26-30°C: "Warm"
    - Above 30°C: "Hot"
    
    Args:
        temp (float): Temperature value
        scale (str): Temperature scale ('C' for Celsius, 'F' for Fahrenheit)
        
    Returns:
        str: Assessment of the temperature
        
    Raises:
        ValueError: If scale is not 'C' or 'F'
        
    Example:
        >>> assess_temperature(25, 'C')
        'Mild'
        >>> assess_temperature(77, 'F')
        'Warm'
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        (25, 'C'),    # Should return "Mild"
        (77, 'F'),    # Should return "Warm"
        (-5, 'C'),    # Should return "Freezing"
        (32, 'C'),    # Should return "Hot"
        (15, 'C'),    # Should return "Cold"
        (0, 'C'),     # Should return "Freezing"
        (30, 'C'),    # Should return "Hot"
        (25, 'K'),    # Should raise ValueError
    ]
    
    for temp, scale in test_cases:
        try:
            result = assess_temperature(temp, scale)
            print(f"{temp}°{scale} is {result}")
        except Exception as e:
            print(f"Error assessing {temp}°{scale}: {str(e)}")


if __name__ == "__main__":
    main() 