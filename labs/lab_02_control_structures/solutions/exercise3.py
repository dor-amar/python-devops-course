"""
Exercise 3: Menu-Driven Calculator - Solution
"""

def get_number_input(prompt):
    """
    Get a number input from the user
    Args:
        prompt (str): The prompt message
    Returns:
        float: The input number
    Raises:
        ValueError: If input is not a valid number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number")

def get_operation_input():
    """
    Get the operation choice from the user
    Returns:
        str: The selected operation ('+', '-', '*', '/', 'q')
    """
    while True:
        operation = input("Enter operation (+, -, *, /, q to quit): ").strip()
        if operation in ['+', '-', '*', '/', 'q']:
            return operation
        print("Error: Invalid operation. Please try again.")

def perform_operation(operation, num1, num2):
    """
    Perform the selected operation on two numbers
    Args:
        operation (str): The operation to perform
        num1 (float): First number
        num2 (float): Second number
    Returns:
        float: The result of the operation
    Raises:
        ValueError: If operation is invalid
        ZeroDivisionError: If dividing by zero
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

def display_menu():
    """
    Display the calculator menu
    """
    print("\nCalculator Menu")
    print("+ : Add")
    print("- : Subtract")
    print("* : Multiply")
    print("/ : Divide")
    print("q : Quit")

def main():
    print("Welcome to the Calculator!")
    
    while True:
        display_menu()
        
        # Get operation
        operation = get_operation_input()
        
        # Check for quit
        if operation == 'q':
            print("Goodbye!")
            break
        
        # Get numbers
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        try:
            # Perform calculation
            result = perform_operation(operation, num1, num2)
            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        print()  # Empty line for better readability

if __name__ == "__main__":
    main() 