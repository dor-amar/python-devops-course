"""
Exercise 2: Pattern Printing - Solution
"""

def get_size_input():
    """
    Get the size of the pattern from the user
    Returns:
        int: The size of the pattern
    """
    return int(input("Enter the size of the pattern: "))

def print_right_triangle(size):
    """
    Print a right-angled triangle pattern
    Args:
        size (int): The size of the triangle
    """
    for i in range(1, size + 1):
        print("*" * i)

def print_pyramid(size):
    """
    Print a pyramid pattern
    Args:
        size (int): The size of the pyramid
    """
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def print_hollow_square(size):
    """
    Print a hollow square pattern
    Args:
        size (int): The size of the square
    """
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")

def main():
    try:
        # Get size from user
        size = get_size_input()
        
        if size <= 0:
            print("Error: Size must be positive")
            return
        
        print("\nRight-angled Triangle:")
        print_right_triangle(size)
        
        print("\nPyramid:")
        print_pyramid(size)
        
        print("\nHollow Square:")
        print_hollow_square(size)
        
    except ValueError:
        print("Error: Please enter a valid integer number")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 