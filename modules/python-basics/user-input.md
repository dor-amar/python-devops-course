# Input

In Python, `input()` is a built-in function that allows you to take user input from the keyboard. Here’s how it works and some examples to illustrate its use.

### 1. **Basic Usage of `input()`**

The `input()` function displays a prompt to the user, waits for the user to type something, and then returns that input as a **string**.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

If you run this code, it will display the message `"Enter your name: "`, wait for you to type a response, and then greet you by the name you entered.

### 2. **Example of Using `input()` for Numbers**

Since `input()` always returns a string, you’ll need to **convert** the input to another data type if you want to use it as a number. You can use `int()` for integers or `float()` for decimal numbers.

```python
age = int(input("Enter your age: "))
print("You are", age, "years old.")
```

In this example, `input()` will take the user's input as a string, and `int()` converts it into an integer. If the user enters a non-numeric value, it will raise a `ValueError`, so it’s often a good idea to check the input first if you expect a specific format.

### 3. **Getting Multiple Inputs**

You can also ask for multiple inputs. Here are two ways:

### a) One-by-One Input

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old!")
```

### 4. **Example with Simple Calculations**

Here’s an example that takes two numbers from the user and adds them:

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print("The sum is:", sum)
```

### 6. **Prompt Customization**

The prompt in `input()` can be anything, making it adaptable to various contexts:

```python
color = input("What's your favorite color? ")
print("Your favorite color is", color + "!")
```

### Summary

- `input()` takes user input as a string.
- Use `int()` or `float()` to convert input to numbers.
- Use `split()` to handle multiple inputs in one line.
- `input()` is useful for interactive programs where user input is needed.