"""
Exercise 1: Number Classification - Solution
"""

def get_number_input():
    """
    Get a number input from the user
    Returns:
        int: The input number
    """
    return int(input("Enter a number: "))

def is_prime(number):
    """
    Check if a number is prime
    Args:
        number (int): The number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def classify_number(number):
    """
    Classify the number based on various properties
    Args:
        number (int): The number to classify
    Returns:
        dict: Dictionary containing classifications
    """
    result = {}
    
    # Classify sign
    if number > 0:
        result['sign'] = 'positive'
    elif number < 0:
        result['sign'] = 'negative'
    else:
        result['sign'] = 'zero'
    
    # Classify parity
    if number % 2 == 0:
        result['parity'] = 'even'
    else:
        result['parity'] = 'odd'
    
    # Classify type (prime/composite)
    if is_prime(number):
        result['type'] = 'prime'
    else:
        result['type'] = 'composite'
    
    return result

def main():
    try:
        # Get number from user
        number = get_number_input()
        
        # Classify the number
        classification = classify_number(number)
        
        # Print results
        print(f"\nNumber Classification:")
        print(f"Sign: {classification['sign']}")
        print(f"Parity: {classification['parity']}")
        print(f"Type: {classification['type']}")
        
    except ValueError:
        print("Error: Please enter a valid integer number")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 