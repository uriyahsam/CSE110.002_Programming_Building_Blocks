# This program calculates the cost of a meal at a restaurant.
# It asks for the price of a child's meal, an adult's meal, the number of children and adults, and the sales tax rate.
# It calculates and prints the subtotal and sales tax.

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

subtotal = (child_meal * children) + (adult_meal * adults)
print()
print(f"Subtotal: ${subtotal:.2f}")

# This will print the sales tax.
print()
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (subtotal * sales_tax_rate) / 100

print(f"Sales Tax: ${sales_tax:.2f}")
