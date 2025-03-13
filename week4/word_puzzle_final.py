# Word Puzzle Game: Final Version with Creativity
# ----------------------------------------------------
# This program is a word puzzle game where the user tries to guess a secret word.
# Features of the program:
# 1. A random secret word is chosen from a predefined list.
# 2. The user is prompted to guess the word, and hints are provided after each guess.
# 3. The hint shows:
#    - Letters in the correct position (uppercase).
#    - Letters present in the secret word but in the wrong position (lowercase).
#    - Letters not in the secret word (underscore '_').
# 4. If the guess has a different length than the secret word, the program informs the user without providing a hint.
# 5. The game ends when the user guesses the word or runs out of a limited number of guesses.
#
# Creativity Added:
# - Random selection of the secret word from a list of words for replayability.
# - A maximum number of guesses (10) to increase challenge and urgency.
# - Visual feedback using emojis for success (🎉) and failure (💀).
# - Hints are displayed with spaces and capitalization for better readability.
# ----------------------------------------------------

import random

# Welcome message
print("Welcome to the word guessing game!")

# List of possible secret words
word_list = ["mosiah", "temple", "nephi", "helaman", "moroni"]
secret_word = random.choice(word_list)  # Randomly select the secret word
word_length = len(secret_word)  # Length of the secret word
guesses = 0  # Counter for guesses
max_guesses = 10  # Limit on number of guesses

# Initial hint
hint = "_ " * word_length
print(f"Your hint is: {hint.strip()}")  # Strip trailing space for better formatting

while guesses < max_guesses:
    # Prompt user for a guess
    guess = input("What is your guess? ").lower()
    guesses += 1  # Increment guesses

    # Check if the length of the guess matches the secret word
    if len(guess) != word_length:
        print(f"Sorry, the guess must have {word_length} letters.")
        continue

    # Check if the guess is correct
    if guess == secret_word:
        print("🎉 Congratulations! You guessed it!")
        print(f"It took you {guesses} guesses.")
        break

    # Generate the hint
    hint = ""
    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "  # Correct letter in the correct position
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "  # Correct letter in the wrong position
        else:
            hint += "_ "  # Incorrect letter

    # Display the hint
    print(f"Your hint is: {hint.strip()}")  # Strip trailing space for better formatting

# If the user runs out of guesses
if guesses == max_guesses and guess != secret_word:
    print(f"💀 You've used all {max_guesses} guesses! The secret word was '{secret_word}'. Better luck next time!")
