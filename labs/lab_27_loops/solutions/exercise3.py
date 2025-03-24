"""Solution for Exercise 3: Practical Applications."""

import random
from datetime import datetime
from typing import Dict, List, Optional


def count_word_frequencies(filename: str) -> Dict[str, int]:
    """Count word frequencies in a text file using loops.
    
    Args:
        filename: Path to the text file
        
    Returns:
        Dictionary mapping words to their frequencies
    """
    frequencies = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def number_guessing_game() -> None:
    """Implement a simple number guessing game using while loops.
    
    The game should:
    1. Generate a random number
    2. Ask the user to guess
    3. Provide hints (higher/lower)
    4. Track number of attempts
    """
    target = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")


def generate_calendar(year: int, month: int) -> List[List[Optional[int]]]:
    """Generate a calendar for a given month.
    
    Args:
        year: Year to generate calendar for
        month: Month to generate calendar for (1-12)
        
    Returns:
        2D list representing the calendar grid
    """
    # Get the first day of the month and number of days
    first_day = datetime(year, month, 1)
    days_in_month = (datetime(year, month + 1, 1) - datetime(year, month, 1)).days
    
    # Create calendar grid (6 weeks x 7 days)
    calendar = [[None for _ in range(7)] for _ in range(6)]
    
    # Fill in the days
    current_day = 1
    for week in range(6):
        for day in range(7):
            if current_day <= days_in_month:
                calendar[week][day] = current_day
                current_day += 1
    
    return calendar


def calculator() -> None:
    """Implement a simple calculator with continuous operation.
    
    The calculator should:
    1. Accept basic arithmetic operations
    2. Handle continuous calculations
    3. Provide option to exit
    4. Handle invalid inputs
    """
    print("Simple Calculator")
    print("Enter 'q' to quit")
    
    while True:
        try:
            # Get first number
            num1_input = input("Enter first number: ")
            if num1_input.lower() == 'q':
                break
            num1 = float(num1_input)
            
            # Get operation
            op = input("Enter operation (+, -, *, /): ")
            if op.lower() == 'q':
                break
            if op not in ['+', '-', '*', '/']:
                print("Invalid operation! Please use +, -, *, or /")
                continue
            
            # Get second number
            num2_input = input("Enter second number: ")
            if num2_input.lower() == 'q':
                break
            num2 = float(num2_input)
            
            # Perform calculation
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            else:  # op == '/'
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            
            print(f"Result: {result}")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    print("Thank you for using the calculator!") 