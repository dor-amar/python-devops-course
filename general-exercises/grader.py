"""Task: Grade Calculator.

Implement a function to calculate letter grades based on numerical scores.
"""

def grader(score: float) -> str:
    """Calculate letter grade based on numerical score.
    
    Grading Scale:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
    
    Args:
        score (float): Numerical score (0-100)
        
    Returns:
        str: Letter grade (A, B, C, D, or F)
        
    Raises:
        ValueError: If score is not between 0 and 100
        
    Example:
        >>> grader(85)
        'B'
        >>> grader(92)
        'A'
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        95,    # Should return 'A'
        85,    # Should return 'B'
        75,    # Should return 'C'
        65,    # Should return 'D'
        55,    # Should return 'F'
        100,   # Should return 'A'
        0,     # Should return 'F'
        -5,    # Should raise ValueError
        105,   # Should raise ValueError
        89.9,  # Should return 'B'
        90.0,  # Should return 'A'
    ]
    
    for score in test_cases:
        try:
            grade = grader(score)
            print(f"Score: {score} -> Grade: {grade}")
        except Exception as e:
            print(f"Error processing score {score}: {str(e)}")


if __name__ == "__main__":
    main() 