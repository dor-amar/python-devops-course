# Project: Rock Paper Scissors

### Objective

Build an interactive Python program that allows a user to play **Rock, Paper, Scissors** against the computer.

### 🧠 What Students Will Learn:

- Using `input()` for user interaction
- Random module usage
- Conditional logic (`if`, `elif`, `else`)
- Looping and game repetition
- Exception handling
- Writing clean and readable code

---

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both choose the same, it's a tie

---

## 🛠️ Project Tasks

### Task 1: Import and Setup

Import the `random` module and create a list of valid choices: `["rock", "paper", "scissors"]`.

```python
# Example:
import random

choices = ["rock", "paper", "scissors"]
```

---

### Task 2: Get User Input

Prompt the user to type `"rock"`, `"paper"`, or `"scissors"`. Validate input and ask again if invalid.

---

### Task 3: Generate Computer Choice

Use `random.choice()` to let the computer randomly pick a move from the list.

---

### Task 4: Determine Winner

Compare user input and computer choice. Print who wins or if it’s a tie.

Example Output:

```
You chose rock. Computer chose scissors.
You win!
```

---

### Task 5: Loop Until Quit

Wrap the game in a loop. Allow the user to play again or type `"q"` to quit.

---

### Task 6: Handle Case Sensitivity and Errors

Ensure that user input is not case-sensitive. Use `.lower()` and check for unexpected input using exception handling.

---

### Bonus: Track Score

Add a scoring system:

- Display the score after each round.
- Show wins, losses, and ties.