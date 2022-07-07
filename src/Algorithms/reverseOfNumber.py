inputNumber = int(input("Please enter your number:"))
reversed_number = 0

while inputNumber != 0:
    reminder = inputNumber % 10
    reversed_number = reversed_number * 10 + reminder
    inputNumber //= 10

print("Reversed Number: " + str(reversed_number))
