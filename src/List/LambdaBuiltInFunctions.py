# lambda variable: expression

print((lambda x: x ** 2)(4))

sum = lambda firstNum, secondNum, thirdNum: firstNum + secondNum + thirdNum

print("Result", sum(1, 2, 3))

reverse = lambda string: string[::-1]

print(reverse("ugurcan"))


def multiply(variable):
    return lambda result: result * variable


resultOfFunction = multiply(5)

print(resultOfFunction(4))