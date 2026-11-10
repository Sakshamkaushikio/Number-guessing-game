# Number Guessing Game 🎯

A simple command-line Number Guessing Game built using Python. The computer randomly selects a number between 1 and 100, and the player has to guess it.

The program provides hints to help the player guess the correct number while keeping track of the number of attempts.

## Features

- **Random Number Generation:** Computer randomly selects a number between 1 and 100.
- **Interactive Gameplay:** Player receives hints to guess higher or lower.
- **Input Validation:** Handles invalid inputs and prevents non-positive guesses.
- **Attempt Counter:** Tracks the number of valid guesses.
- **High Score System:** Saves the best score (fewest attempts) in `highscore.txt`.
- **High Score Reset:** Allows the player to reset the saved high score.
- **Exception Handling:** Uses `try-except` to handle invalid numerical inputs.

## Concepts Used

This project helped me practise the following Python concepts:

- Variables and Data Types
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`)
- Functions
- Exception Handling (`try`, `except`, `ValueError`)
- File Handling (`open`, `read`, `write`)
- File Modes (`a+`, `w`)
- File Cursor Management (`seek`)
- String Methods (`strip`, `casefold`)
- Random Module (`random.randint`)
- Loop Control Statements (`break`, `continue`)

## How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository or download the project files.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python main.py
```

## How to Play

1. Run the program.
2. Enter a number between 1 and 100.
3. Follow the hints:
   - **Try a higher number** – Your guess is too low.
   - **Try a lower number** – Your guess is too high.
4. Keep guessing until you find the correct number.
5. Your score is calculated based on the number of attempts.
6. You can choose whether