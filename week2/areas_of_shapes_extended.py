# This program Prompt the user for a single length value, 
# then compute and display the areas of a square with that length of side, 
# a circle with that radius, and then the volumes of a cube with that side 
# and a sphere with that radius, all from the same value from the user

import math

number = float(input("Enter a number: "))
square_area = number ** 2
circle_area = 3.141592653589793 * (number ** 2)
cube_volume = number ** 3  
sphere_volume = (4/3) * 3.141592653589793 * (number ** 3)

print(f"The area of the square is {square_area:.1f}")
print(f"The area of the circle is {circle_area:.1f}")
print(f"The volume of the cube is {cube_volume:.1f}")
print(f"The volume of the sphere is {sphere_volume:.1f}")

