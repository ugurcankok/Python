# prime number
a = int(input("Enter your number:"))

condition = 1
t = 0

while condition <= a:
    if a % condition == 0:
        t += 1
    condition += 1

if t == 2:
    print("Your number is prime")
else:
    print("Your number is not prime")
