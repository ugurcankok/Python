numberList = [5, 12, 18, 24, 45]

listOfName = ["ugur", "can", "ali", "ahmet"]

numberResult = list(filter(lambda x: x > 18, numberList))  # you can use list comprehension instead of filter function

resultOfNumber = list(filter(lambda x: x % 2 == 0, numberList))

# After we select the elements which start with 'a' from listofName, we apply upper method each elements using map.
stringResult = list(map(lambda x: x.upper(), filter(lambda x: x[0] == "a", listOfName)))

print(stringResult)
