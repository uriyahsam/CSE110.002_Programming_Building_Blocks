# This program will as user for two intergers and compare them to see if they are equal, greater or less than each other.

# Ask user for two integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The first number is greater.")
else:
    print(f"The first number is not greater")

if num1 == num2:
    print(f"The numbers are equal.")
else:
    print(f"The numbers are not equal.")

if num2 > num1:
    print(f"The second number is greater.")
else:
    print(f"The second number is not greater.")

print()
animal = input("What is your favorite animal? ")
animal = animal.lower()
if animal == "dog":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
