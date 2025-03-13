# This program asks the user for a series of words and inserts them into a story.
# Additions: The story has been expanded, and the program automatically handles "a" or "an."

def get_article(word):
    """Determines whether to use 'a' or 'an' based on the input word."""
    return "an" if word[0].lower() in "aeiou" else "a"

# Start of the program directly
print("Please enter the following:\n")

# Collect inputs from the user with simpler, clearer prompts
adjective = input("Give an adjective: ").strip()
animal = input("Name an animal you like: ").strip()
verb1 = input(f"Give a verb (something a {animal} might do): ").strip()
exclamation = input("Provide an exclamation (word): ").capitalize().strip()
verb2 = input("Give another verb: ").strip()
verb3 = input("Give one more verb: ").strip()
place = input("Name a random place (e.g., in a park, at a zoo): ").strip()
object = input("Name a random Object: ").strip()

# Build the story
story = (
    f"The other day, I was really in trouble. It all started when I saw {get_article(adjective)} "
    f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all "
    f"I could think to do was to {verb2} over and over. Miraculously, "
    f"that caused it to stop, but not before it tried to {verb3} "
    f"right in front of my family. Later, it escaped to {place} and took my {object} with it!"
)

# Display the story
print(f"\nYour story is:\n\n{story}")
