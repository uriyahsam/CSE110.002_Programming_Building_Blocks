# Milestone Requirements
print("Welcome to the word guessing game!")

# Secret word
secret_word = "mosiah"
guesses = 0  # Counter for guesses

while True:
    # Prompt user for a guess
    guess = input("What is your guess? ").lower()
    guesses += 1  # Increment guesses

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guesses} guesses.")
        break
    else:
        print("Your guess was not correct.")
