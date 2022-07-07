# factorial
a = int(input("Enter your number:"))

result = 1
condition = 1

while condition <= a:
    result *= condition
    condition += 1

print("Your result is :", result)
