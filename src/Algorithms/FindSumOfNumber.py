inputNumber = int(input("Enter your number:"))

total = 0

while inputNumber != 0:
    total += inputNumber % 10
    inputNumber //= 10

print(f"Result is: {total}")
