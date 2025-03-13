# Shopping Cart Program
# This program simulates a shopping cart system with the following features:
# - A menu system that repeats until the user chooses to quit.
# - A list that stores the names of the items in the shopping cart.
# - An option to add items to the cart by entering their names.
# - An option to view the names of the items in the cart.
# - An option to quit the program.
#

def display_menu():
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def main():
    # List to store the names of the items
    cart = []

    while True:
        display_menu()
        action = input("Please enter an action: ")

        if action == "1":  # Add item
            item = input("What item would you like to add? ")
            cart.append(item)
            print(f"'{item}' has been added to the cart.")

        elif action == "2":  # View cart
            if cart:
                print("\nThe contents of the shopping cart are:")
                for item in cart:
                    print(item)
            else:
                print("\nThe shopping cart is empty.")

        elif action == "5":  # Quit
            print("\nThank you. Goodbye.")
            break

        else:
            print("\nThis functionality is not yet implemented.")

if __name__ == "__main__":
    main()
