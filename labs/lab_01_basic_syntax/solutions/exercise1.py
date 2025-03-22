"""
Exercise 1: Variables and Data Types - Solution
"""

# Declare variables of different types
age = 25
height = 1.75
name = "Python Learner"
is_student = True

# Print each variable and its type
print(f"Variable: {age}, Type: {type(age)}")
print(f"Variable: {height}, Type: {type(height)}")
print(f"Variable: {name}, Type: {type(name)}")
print(f"Variable: {is_student}, Type: {type(is_student)}")

# Perform basic arithmetic operations
# Add age and height (convert height to integer)
sum_result = age + int(height)
print(f"Sum of age and height (as integer): {sum_result}")

# Multiply age by 2
multiply_result = age * 2
print(f"Age multiplied by 2: {multiply_result}")

# Divide height by 2
divide_result = height / 2
print(f"Height divided by 2: {divide_result}") 