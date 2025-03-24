### Objective

Create a game where the computer picks a **random number between 1 and 100**, and the user must guess it. After each guess, the program tells the user if the guess is **too high** or **too low**, until they get it right.

---

## You Will

- Using `random.randint()`
- Taking and validating user input
- Loops (`while`) and conditionals (`if/elif/else`)
- Basic game logic
- Keeping track of attempts
- Clean code and user feedback

---

## Project Tasks

---

### Task 1: Import and Generate Random Number

Import the `random` module and generate a number between 1 and 100.

```python
import random

number = random.randint(1, 100)
```

---

### Task 2: Ask for User Guesses

Use a loop to:

- Ask for a number
- Convert it to an `int`
- Compare it to the secret number
- Tell the user whether to guess **higher** or **lower**

---

### Task 3: Count Attempts

Keep track of how many guesses the user took and show the number at the end.

---

### Task 4: Handle Bad Input

If the user types something that’s not a number, catch the error and ask again.

---