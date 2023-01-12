import math

# c^2=a^2+b^2 Hypotension

a = int(input("Enter your one side of triangle:"))
b = int(input("Enter your other side of triangle:"))

c = math.pow(a, 2) + math.pow(b, 2)

print("The longest side of triangle:", math.sqrt(c))
