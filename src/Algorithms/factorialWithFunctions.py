# factorial
def factorial(num):
    result = 1
    condition = 1
    while condition <= num:
        result *= condition
        condition += 1
    print("Result is:", result)


a = int(input("Enter your number:"))
factorial(a)
