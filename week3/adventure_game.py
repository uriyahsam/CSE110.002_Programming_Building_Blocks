# Milestone: (Jungle Quest) Adventure Game
# For the milestone, the game implements the first question and its possible choices, including an else condition.

def adventure_game_milestone():
    print("Welcome to Jungle Quest!")
    print("You find yourself stranded in a dense jungle. Your goal is to find a way to safety. Choose wisely!")

    # First Level
    print("\nYou see two paths ahead. One is DARK and overgrown, and the other is BRIGHT and clear. Which path do you take?")
    choice1 = input("Enter DARK or BRIGHT: ").strip().lower()

    if choice1 == "dark":
        print("\nYou brave the dark path, pushing aside thick vines. You hear a growl behind you. What will you do next?")
    elif choice1 == "bright":
        print("\nYou take the bright path and find a river ahead. What will you do next?")
    else:
        print("\nInvalid choice. You wander aimlessly and become another mystery of the jungle.")

# Run the milestone version of the game
adventure_game_milestone()