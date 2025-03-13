import math

# Square
square_side = float(input("What is the length of a side of the square? "))
square_area = square_side ** 2

print(f"The area of the square is {square_area:.1f}")

# Rectangle
rectangle_length = float(input("What is the length of the rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width

print(f"The area of the rectangle is {rectangle_area:.1f}")

# Circle
circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * circle_radius ** 2

print(f"The area of the circle is {circle_area:.1f}")