# Shopping Cart Program
# This program simulates a basic shopping cart where users can:
# 1. Add items to the cart (name, price, quantity)
# 2. View the contents of the cart with better formatting (aligned prices)
# 3. Remove items from the cart
# 4. Compute the total price of the items in the cart
# 5. Quit the program
# 
# Exceeding the Basic Requirement:
# - The display_cart function aligns the prices and quantities properly in a table format.
# - Added clear and consistent spacing to the output for better readability.
# - The cart is displayed in a well-organized table with headers for item number, name, price, and quantity.

def display_menu():
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")


def display_cart(names, prices, quantities):
    if not names:
        print("\nThe shopping cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        print("{:<5} {:<20} {:<10} {:<10}".format("No.", "Item", "Price", "Quantity"))
        print("-" * 50)
        for i, (name, price, quantity) in enumerate(zip(names, prices, quantities), start=1):
            print(f"{i:<5} {name:<20} ${price:<9.2f} {quantity:<10}")


def main():
    names = []
    prices = []
    quantities = []

    while True:
        display_menu()
        action = input("Please enter an action: ")

        if action == "1":  # Add item
            name = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{name}'? "))
            quantity = int(input(f"How many '{name}' would you like to add? "))
            names.append(name)
            prices.append(price)
            quantities.append(quantity)
            print(f"'{name}' has been added to the cart.")

        elif action == "2":  # View cart
            display_cart(names, prices, quantities)

        elif action == "3":  # Remove item
            if not names:
                print("\nThe shopping cart is empty. There is nothing to remove.")
            else:
                display_cart(names, prices, quantities)
                try:
                    item_to_remove = int(input("\nWhich item would you like to remove? ")) - 1
                    if 0 <= item_to_remove < len(names):
                        removed_item = names.pop(item_to_remove)
                        prices.pop(item_to_remove)
                        quantities.pop(item_to_remove)
                        print(f"'{removed_item}' has been removed from the cart.")
                    else:
                        print("Sorry, that is not a valid item number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif action == "4":  # Compute total
            total = sum(price * quantity for price, quantity in zip(prices, quantities))
            print(f"\nThe total price of the items in the shopping cart is: ${total:.2f}")

        elif action == "5":  # Quit
            print("\nThank you. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
