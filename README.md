# Basic-Guess-Game
# Project Description

This project is a Python-based Guess Game developed using fundamental programming concepts such as variables, input/output operations, loops, functions, and lists.

The program randomly selects 8 words from a predefined list of 100 words. One of these words is chosen as the password. The user is required to guess the correct password within a limited number of attempts.

After each incorrect guess, the program provides feedback indicating how many letters are correct and in the correct position.



# How the Game Works

1. The program displays a list of 8 words.
2. Each word is associated with an index number.
3. The user selects a word by entering its index number.
4. If the guess is incorrect, the program displays the number of matching letters.
5. The user has a total of 4 attempts to guess the correct word.
6. The game ends when the user either guesses correctly or runs out of attempts.



# System Requirements

 Python 3 installed on the system



# Instructions to Run the Program

# Step 1: Open Command Prompt or Terminal

Navigate to the directory where the project files are stored.

Example:
cd Desktop/Guess-Game

# Step 2: Run the Program

Execute the following command:

python guess_game.py

If using the extended version of the program:

python guess_game_additions.py



# User Instructions

* Review the list of displayed words carefully.
* Enter the index number corresponding to your chosen word.
* Use the feedback provided after each guess to improve your next attempt.
* Try to identify the correct password within the given number of attempts.



# Important Notes

* Ensure that the input provided is a valid number within the displayed range.
* Invalid inputs may cause errors unless handled within the program.
* Each incorrect guess reduces the number of remaining attempts.


# Project Files

* guess_game.py: Main implementation of the game
* guess_game_additions.py: Enhanced version with additional features
* README.txt: Documentation and instructions for the project


# Author

Name: Wijekumara Kavindu Akash
Student Number: 10687621


# Objective

The objective of this project is to apply fundamental programming concepts to design and implement a functional interactive program. It also helps in developing problem-solving skills and understanding program structure.


# Example

If the password is COMEDY and the user guesses MOULDY, the program will output:

3/6 letters are correct

This indicates that three letters are in the correct position.


# Conclusion

This project demonstrates the practical application of basic programming concepts in Python through an interactive guessing game.
