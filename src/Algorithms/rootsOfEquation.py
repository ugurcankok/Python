# root of second order of equation
import math

a = int(input("Enter your x^2 value of equation:"))
b = int(input("Enter your x value of equation:"))
c = int(input("Enter your constant number:"))

# Delta=b^2-4ac

delta = math.pow(b, 2) - 4 * a * c

if delta < 0:
    print("There is no root!!")
elif delta == 0:
    root1 = (-b + math.sqrt(delta)) / 2 * a
    print("Two roots are equal and value is:", root1)
else:
    print("There is two different root")
    root2 = (-b + math.sqrt(delta)) / 2 * a
    root3 = (-b - math.sqrt(delta)) / 2 * a
    print("One root is:", root2)
    print("Second root is:", root3)
