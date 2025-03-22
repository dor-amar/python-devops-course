"""
Exercise 3: Menu-Driven Calculator

In this exercise, you will:
1. Create a menu-driven calculator
2. Handle user input and validation
3. Use while loop for menu repetition
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
    # TODO: Get input from user and convert to float
    pass

def get_operation_input():
    """
    Get the operation choice from the user
    Returns:
        str: The selected operation ('+', '-', '*', '/', 'q')
    """
    # TODO: Get operation input and validate it
    pass

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
    # TODO: Implement the operation logic
    pass

def display_menu():
    """
    Display the calculator menu
    """
    # TODO: Print the menu options
    pass

def main():
    # TODO: Implement the main function that:
    # 1. Displays the menu
    # 2. Gets user input for operation and numbers
    # 3. Performs the calculation
    # 4. Continues until user chooses to quit
    # 5. Handles all possible errors
    pass

if __name__ == "__main__":
    main() 