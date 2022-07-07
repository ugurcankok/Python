import math

a = int(input("Enter your radius:"))

volume = 4 / 3 * ((math.pi) * math.pow(a, 3))
surfaceArea = 4 * math.pi * pow(a, 2)
print("Volume of sphere:", volume)
print("Surface Area of sphere:", surfaceArea)
