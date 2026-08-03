# Import entire modules
import math
# Using imported modules
diameter = int(input("Enter the diameter of the cicle: "))
radius = diameter/2
circle_area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print(f"Circle Area: {circle_area}")
print(f"Circumference: {circumference}")