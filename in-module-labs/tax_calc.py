"""Task: Tax Calculator with Multiple Brackets.

Implement a tax calculator that calculates income tax based on different tax brackets.
"""

def tax_calc(income: float) -> float:
    """Calculate income tax based on tax brackets.
    
    Tax Brackets:
    - 0% for income up to $10,000
    - 10% for income from $10,001 to $30,000
    - 20% for income from $30,001 to $100,000
    - 30% for income above $100,000
    
    Args:
        income (float): Annual income
        
    Returns:
        float: Total tax amount
        
    Raises:
        ValueError: If income is negative
        
    Example:
        >>> tax_calc(25000)
        1500.0
    """
    # Your code here
    pass


def main():
    """Test your implementation."""
    # Test cases
    test_cases = [
        25000,    # Should be $1,500 (10% of $15,000)
        50000,    # Should be $5,000 (10% of $20,000 + 20% of $20,000)
        150000,   # Should be $35,000 (10% of $20,000 + 20% of $70,000 + 30% of $50,000)
        5000,     # Should be $0 (below first bracket)
        -1000,    # Should raise ValueError
    ]
    
    for income in test_cases:
        try:
            tax = tax_calc(income)
            print(f"Income: ${income:,.2f} -> Tax: ${tax:,.2f}")
        except Exception as e:
            print(f"Error for income ${income:,.2f}: {str(e)}")


if __name__ == "__main__":
    main() 