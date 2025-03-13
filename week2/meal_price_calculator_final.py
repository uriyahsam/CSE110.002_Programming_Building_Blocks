# This program calculates the total cost of a meal at a restaurant.
# It asks for the price of a child's meal, an adult's meal, the number of children and adults, and the sales tax rate.
# It calculates the subtotal, sales tax, total cost, and prints them.
# Addition: The program also asks for a tip percentage and calculates the tip amount.


child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

subtotal = (child_meal * children) + (adult_meal * adults)
print()
print(f"Subtotal: ${subtotal:.2f}")

# This will print the sales tax and total cost of the meal.
print()
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (subtotal * sales_tax_rate) / 100
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

print()
change = float(input("What is the payment amount? ")) - total
print()
print(f"Change: ${change:.2f}")

# Addition: The program also asks the user for the tips percentage and then calculates the tip amount.
print()
tip_rate = float(input("Enter the tip percentage: "))
tip = subtotal * tip_rate
total = subtotal + sales_tax + tip
print()
print(f"Tip: ${tip:.2f}")
