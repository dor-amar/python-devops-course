# **Loops in Python**

### **Lecture: Loops in Python**

---

### **What Are Loops?**

- **Definition**:
    
    Loops allow you to execute a block of code multiple times, making your programs more efficient for repetitive tasks.
    
- **Why Use Loops?**
    - To automate repetitive tasks like iterating through a list of items or repeatedly checking for a condition.
    - Example: Printing numbers from 1 to 100 without writing 100 lines of code.

---

### Introduction to `for` Loop

A `for` loop is used to repeat actions a certain number of times or to go through each item in a collection, such as a list, string, or range of numbers. With a `for` loop, we can efficiently execute a block of code multiple times without rewriting it.

---

### Structure of a `for` Loop

In Python, the basic structure of a `for` loop looks like this:

```python
for item in collection:
    # Do something with each item
```

- `item` is a variable that represents each element in the collection (like each number in a range or each letter in a string).
- `collection` is the group of items we want to loop through (like a list, string, or range).

---

### Examples

### 1. Looping Through a List

A list is a collection of items. We can use a `for` loop to go through each item in the list.

**Example**:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Explanation**:

- `fruits` is a list containing three fruits.
- For each `fruit` in the list, we print the `fruit` name.
- The output will be:
    
    ```
    apple
    banana
    cherry
    
    ```
    

---

### 2. Looping Through a String

A string is a sequence of characters. Using a `for` loop, we can go through each character in the string.

**Example**:

```python
name = "Alice"

for letter in name:
    print(letter)
```

**Explanation**:

- Here, we loop through each `letter` in the string `"Alice"`.
- Each letter is printed on a new line:
    
    ```css
    A
    l
    i
    c
    e
    
    ```
    

---

### 3. Using `range()` in a `for` Loop

The `range()` function generates a sequence of numbers, which is helpful when we want to repeat something a specific number of times.

**Example**:

```python
for i in range(5):
    print("Hello!")
```

**Explanation**:

- `range(5)` generates the numbers `0, 1, 2, 3, 4` (five numbers in total).
- For each number in this range, we print “Hello!”
- The output will be:
    
    ```
    Hello!
    Hello!
    Hello!
    Hello!
    Hello!
    ```
    

---

### 4. Using `for` with `range(start, stop)`

We can specify a start and stop value in `range()` to control where the loop begins and ends.

**Example**:

```python
for i in range(1, 6):
    print(i)
```

**Explanation**:

- `range(1, 6)` generates numbers from `1` up to `5`.
- Each number in this range is printed:
    
    ```
    1
    2
    3
    4
    5
    
    ```
    

---

### Combining `for` Loops with `if` Statements

We can use `if` statements inside `for` loops to make decisions.

**Example**:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

```

**Explanation**:

- This loop goes through each `number` in the list.
- If the number is even (divisible by 2), it prints that it's even.
- Otherwise, it prints that it's odd.
- The output will be:
    
    ```csharp
    1 is odd
    2 is even
    3 is odd
    4 is even
    5 is odd
    
    ```
    

---

### Simple Class Exercises

1. **Exercise 1**: Print each letter in the word "Python" on a new line.
2. **Exercise 2**: Use `range()` to print numbers from 1 to 10.
3. **Exercise 3**: Create a list of three animals and print each animal’s name using a `for` loop.
4. **Exercise 4**: Use a `for` loop with `if` statements to check if each number in a list is greater than 10. If it is, print "Large number!"

---

### Additional Resources

For more explanations and practice:

- Python `for` Loops (W3Schools)
- Real Python's Guide to Python `for` Loops

### When to Use a `for` Loop

We use a `for` loop when we need to **repeat actions multiple times** or **go through each item in a collection** (like a list, string, or range of numbers). `for` loops are useful in many situations, such as:

1. **Processing each item in a list**: When you want to go through each item and perform an action, like calculating totals, checking conditions, or modifying items.
2. **Repetitive tasks**: When you need to repeat a specific task a set number of times.
3. **Filtering data**: When you want to find specific items in a collection that meet a certain condition (like all even numbers in a list).
4. **Data analysis**: When you need to analyze data point by point.

### Best Practices for Using `for` Loops

1. **Use Descriptive Variable Names**: Make sure the variable used in the loop is descriptive. For example, use `student` instead of `s` if you’re iterating over a list of students.
    
    ```python
    
    for student in students:
        print(student)
    ```
    
2. **Keep Loops Simple**: Avoid adding too many complex operations inside the loop. If needed, break it down into functions or use comments to make it easier to understand.
3. **Avoid Nested Loops**: If possible, avoid loops within loops (nested loops) as they can slow down the program. Use nested loops only when necessary.
4. **Use `range()` Wisely**: When using `range()`, make sure the start, stop, and step values are correctly defined. For example, `range(1, 10, 2)` will generate 1, 3, 5, 7, 9.
5. **Consider List Comprehensions for Simple Loops**: For simple tasks like creating a new list based on a condition, consider using list comprehensions instead of a `for` loop.
    
    ```python
    numbers = [1, 2, 3, 4, 5]
    even_numbers = [num for num in numbers if num % 2 == 0]
    ```
    
6. **Plan and Test**: Before implementing a loop, think about what you need to accomplish. Write out the logic, and test with small examples to make sure it works as expected.

---

### Summary for the Class

**When to Use `for` Loops**: Use `for` loops when you need to repeat an action multiple times or process each item in a collection. This could be for tasks like analyzing data, filtering items, or performing repetitive actions.

**Best Practices**:

- Use clear variable names.
- Keep loops simple.
- Avoid unnecessary nested loops.
- Use `range()` carefully.
- Consider list comprehensions for simple filtering or transformations.
- Plan your loop logic before writing code.

### Exercise: Calculate the Total and Average of Numbers

**Objective**: Use a `for` loop to calculate the total sum and average of a list of numbers.

---

### Instructions

1. Create a list of numbers. For example:
    
    ```python
    numbers = [10, 20, 30, 40, 50]
    ```
    
2. Use a `for` loop to calculate the total sum of the numbers.
3. After the loop, calculate the average by dividing the total sum by the number of items in the list.
4. Print both the total sum and the average.

---

### Example Solution

Here's a step-by-step solution with explanations.

```python
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Variable to hold the total sum
total_sum = 0

# Loop through each number in the list
for number in numbers:
    total_sum += number  # Add the current number to the total sum

# Calculate the average
average = total_sum / len(numbers)

# Print the results
print("Total sum:", total_sum)
print("Average:", average)

```

**Explanation**:

1. We start with a `total_sum` variable set to `0`.
2. The `for` loop goes through each `number` in the `numbers` list.
3. Inside the loop, each `number` is added to `total_sum`.
4. After the loop, we calculate the `average` by dividing `total_sum` by the length of the list (`len(numbers)`).
5. Finally, we print the `total_sum` and `average`.

**Expected Output**:

```yaml
Total sum: 150
Average: 30.0
```

### Introduction to `while` Loops

A `while` loop repeatedly executes a block of code as long as a specified condition is `True`. It is often used when we don’t know in advance how many times we need to repeat the action, but we have a condition that determines when to stop.

---

### Structure of a `while` Loop

In Python, the basic structure of a `while` loop looks like this:

```python
while condition:
    # Code to execute as long as the condition is True
```

- `condition` is a boolean expression (it can be `True` or `False`).
- The code inside the loop runs as long as `condition` is `True`.
- When `condition` becomes `False`, the loop stops.

---

### Examples

### 1. Counting with a `while` Loop

A `while` loop can be used to count up to a specific number.

**Example**:

```python
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Increase count by 1 each time
```

**Explanation**:

- `count` starts at 1.
- The loop continues as long as `count` is less than or equal to 5.
- Inside the loop, we print the current `count` and then increase it by 1.
- Once `count` becomes 6, the loop stops.

**Output**:

```csharp
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

---

### 2. User Input with a `while` Loop

We can use a `while` loop to keep asking the user for input until they enter a specific value.

**Example**:

```python
password = ""

while password != "python123":
    password = input("Enter the password: ")

print("Access granted!")
```

**Explanation**:

- The loop keeps asking for the password until the user enters `"python123"`.
- Once the correct password is entered, the loop stops, and "Access granted!" is printed.

---

### When to Use a `while` Loop

Use a `while` loop when:

1. **You don’t know how many times** the loop needs to run (e.g., waiting for the correct user input).
2. **There is a condition** that may change over time, and the loop should continue until the condition is met.

---

### Best Practices for Using `while` Loops

1. **Avoid Infinite Loops**: Make sure there’s a way to stop the loop. Without this, the loop will run forever, potentially freezing the program.
    - Example: If you forget to increment `count` in the first example, the loop would never stop.
2. **Check Your Condition**: Double-check the condition to make sure the loop will eventually stop.
3. **Use Break Statements Sparingly**: Avoid using `break` to exit a `while` loop unless necessary. Instead, structure the loop condition to control when it should end.
4. **Plan and Test**: Before writing the loop, think about the goal and make sure the condition and any updates (like incrementing `count`) will lead to the loop ending.

---

### Exercise: Guess the Number

**Objective**: Use a `while` loop to create a simple guessing game.

---

### Instructions

1. Set a "secret" number. For example:
    
    ```python
    secret_number = 7
    ```
    
2. Use a `while` loop to ask the user to guess the number until they get it right.
3. If the guess is too high or too low, give them a hint.
4. When they guess correctly, print a success message.

---

### Example Solution

Here’s a simple version of the guessing game with explanations.

```python
secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the right number.")
```

**Explanation**:

1. `secret_number` is set to 7.
2. `guess` starts as `None`, so the loop starts because `guess != secret_number`.
3. Inside the loop, the user is prompted to guess the number.
4. The program checks if the guess is too low, too high, or correct, and gives feedback accordingly.
5. When the guess is correct, the loop stops, and a success message is printed.

**Expected Output**:
The program will keep prompting until the user guesses `7`, with hints like "Too low!" or "Too high!"

---

### Why Use a `while` Loop Here?

We use a `while` loop because we don’t know how many guesses the user will need. The loop continues until they get the correct answer, which is ideal for `while` loops.

---

This exercise gives students a practical use case for `while` loops and helps reinforce best practices, such as avoiding infinite loops by updating the condition.


### `break` Statement

The `break` statement is used to **exit a loop early**. When `break` is executed, the loop stops immediately, and the program continues with the next line of code after the loop.

### When to Use `break`

Use `break` when:

- You want to stop the loop once a certain condition is met.
- You don’t need to check any more items after finding what you’re looking for.

---

### `continue` Statement

The `continue` statement is used to **skip the current iteration** and move to the next one. When `continue` is executed, the loop doesn't finish its current cycle; instead, it goes back to the top of the loop to start the next iteration.

### When to Use `continue`

Use `continue` when:

- You want to skip certain values or conditions but continue looping.
- You need to ignore specific cases within the loop but don’t want to exit the loop entirely.

---

### Examples of `break` and `continue`

### Using `break` in a `for` Loop

**Example**: Finding a specific fruit in a list. When the fruit is found, the loop stops.

```python
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        print("Found cherry!")
        break  # Exit the loop once "cherry" is found
    print(fruit)

```

**Explanation**:

- The loop goes through each fruit.
- When `fruit` is "cherry", `break` stops the loop.
- The output will be:
    
    ```
    apple
    banana
    Found cherry!
    ```
    

---

### Using `continue` in a `for` Loop

**Example**: Skipping even numbers in a list and only printing odd numbers.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```

**Explanation**:

- `continue` skips over even numbers (those where `number % 2 == 0`).
- Only odd numbers are printed.
- The output will be:
    
    ```
    1
    3
    5
    ```
    

---

### Using `break` in a `while` Loop

**Example**: Asking the user to enter the correct password. If they enter "exit", the loop stops immediately.

```python
while True:
    password = input("Enter the password (or type 'exit' to quit): ")
    if password == "exit":
        print("Exiting program.")
        break  # Exit the loop immediately
    elif password == "python123":
        print("Access granted!")
        break  # Exit the loop if the correct password is entered
    else:
        print("Incorrect password. Try again.")

```

**Explanation**:

- The loop runs until `break` is executed.
- If the user types "exit" or the correct password, the loop stops.
- Otherwise, the user is prompted to try again.

---

### Using `continue` in a `while` Loop

**Example**: Counting numbers from 1 to 10, but skipping numbers that are divisible by 3.

```python
count = 0

while count < 10:
    count += 1
    if count % 3 == 0:
        continue  # Skip numbers divisible by 3
    print(count)

```

**Explanation**:

- The `continue` statement skips numbers divisible by 3.
- Only numbers that are not divisible by 3 are printed.
- The output will be:
    
    ```
    1
    2
    4
    5
    7
    8
    10
    
    ```
    

---

### Summary for the Class

- **`break`**: Exits the loop immediately when encountered.
    - Use it when you want to stop looping early if a specific condition is met.
- **`continue`**: Skips the current iteration and goes to the next one.
    - Use it when you want to ignore certain cases but continue with the rest of the loop.

These examples illustrate the purpose of `break` and `continue`, helping students understand when to use each and how they affect the flow of a loop.

## Another Version of the Class

### 1. The `break` Statement

The `break` statement is used to exit a loop prematurely. When Python encounters a `break` statement inside a loop, it immediately terminates the loop and continues with the next statement after the loop.

### **Example:**

```python
for number in range(10):
    if number == 5:
        break
    print(number)

```

**Output:**

```
0
1
2
3
4
```

Here, the loop starts printing numbers from 0 to 9. However, when `number` equals 5, the `break` statement is triggered, and the loop stops.

### **Use Case:**

- You might use `break` when searching for an item in a list and want to stop the search as soon as you find it.

### 2. The `continue` Statement

The `continue` statement skips the current iteration of a loop and moves on to the next iteration. It’s useful when you want to skip certain items but still want to complete the loop.

### **Example:**

```python
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)

```

**Output:**

```
Copy code
1
3
5
7
9
```

In this example, the loop prints only odd numbers. When `number % 2 == 0` (i.e., `number` is even), the `continue` statement is triggered, and the loop skips to the next iteration.

### **Use Case:**

- You might use `continue` when processing a list of items but need to skip certain conditions or invalid data.

### Combining `break` and `continue`

You can use both `break` and `continue` in the same loop, but you should do so carefully to avoid creating confusing logic.

### **Example:**

```python
for number in range(10):
    if number == 3:
        continue  # Skip 3
    if number == 7:
        break     # Stop the loop when 7 is reached
    print(number)

```

**Output:**

```
Copy code
0
1
2
4
5
6

```

Here, the loop skips printing `3` due to the `continue` statement and stops entirely once `number` equals `7` because of the `break` statement.

### Hands-On Exercise

Let’s work on a small exercise to practice these concepts. Write a loop that:

- Prints all numbers from 1 to 15, except it skips numbers that are multiples of 4.
- Stops the loop if the number is greater than 10.

This should help you solidify your understanding of `break` and `continue`.

### **Best Practices**

1. **Use Descriptive Variable Names**:
    - Instead of `i`, use meaningful names like `index` or `item`.
2. **Avoid Nested Loops If Possible**:
    - Nested loops can slow down your program. Use better logic or algorithms if feasible.
3. **Test Loop Conditions**:
    - Ensure the loop condition will eventually become `False`.
4. **Use `break` and `continue` Sparingly**:
    - Overusing them can make your code harder to read.

---

### **Real-World Applications of Loops**

1. **Processing Data**:
    - Iterating through files, rows in a database, or API responses.
2. **Automating Tasks**:
    - Automatically generating reports or emails.
3. **Simulations**:
    - Running simulations or repetitive calculations.

---

### **Practice Tasks**

### **Task 1: Print Multiplication Table**

Write a script to print the multiplication table of a given number (e.g., `5`).

### **Task 2: Reverse a String**

Ask the user for a string and print its reverse using a loop.

### **Task 3: Sum of Digits**

Write a script to calculate the sum of digits in an integer (e.g., `123` → `1+2+3=6`).

### **Task 4: Find the Maximum in a List**

Write a script to find the largest number in a list using a loop.

### **Task 5: Generate Fibonacci Series**

Print the Fibonacci series up to a given number (e.g., `10`).

---

### **Key Takeaways**

- Loops are essential for repetitive tasks.
- Use `for` loops for sequences and `while` loops for condition-based iterations.
- Loop control statements (`break`, `continue`, `else`) give you fine-grained control over the loop flow.
- Always test your loops to avoid infinite iterations.