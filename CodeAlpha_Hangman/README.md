# CodeAlpha Hangman Game


## Project Description

This project is a simple text-based Hangman game developed in Python as part of the CodeAlpha Python Programming Internship.

The player has to guess a randomly selected word one letter at a time. The game allows a maximum of 6 incorrect guesses. Correctly guessed letters are revealed, while incorrect letters reduce the remaining attempts.

The game also handles invalid inputs and prevents the player from guessing the same letter more than once.

## Features

- Randomly selects a word from a predefined list of 5 words
- Allows the player to guess one letter at a time
- Displays correctly guessed letters
- Tracks incorrect guesses with a maximum limit of 6
- Shows correct and incorrect letters separately
- Prevents repeated guesses
- Validates user input
- Displays win and game-over messages

## Technologies Used

- Python
- Random module
- Conditional statements
- While loop
- For loop
- Lists
- Strings
- User input and console output

## How to Run

1. Make sure Python is installed on your system.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:
```bash
python hangman.py 
```
5. Follow the instructions displayed in the console and start guessing letters.

## Game Flow

1. The program randomly selects one word from the predefined word list.
2. The selected word is hidden using underscores.
3. The player enters one letter at a time.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses reduce the remaining attempts.
6. The game ends when the player guesses the complete word or uses all 6 incorrect guesses.

## Project Structure

```text
CodeAlpha_Hangman/
│
├── hangman.py
└── README.md
```

## Author

Vanshika