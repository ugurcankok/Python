# demo #1
numberLists = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1 : get number value from the numberList

for numberList in numberLists:
    try:
        result = int(numberList)
        print(result)
    except Exception as error:
        print(f"Your value: {numberList} and Exception: {error}")

# demo #2

# The number entered by the user is converted to float, but if user enters q, the program closes.

while True:
    inputValue = input("Value: ")
    if inputValue == "q":
        print("Closed..")
        break

    try:
        result = float(inputValue)
        print(f"Your result: {result}")
        break
    except Exception:
        print("Please give us a number")
        continue

# demo #3

# get dictionary key value, write a function. İf key doesn't exist in our dictionary return None otherwise return value

ourDict = {"productName": "iphone13"}


def getValue(ourDict, key):
    try:
        return ourDict[key]
    except Exception:
        return None


print(getValue(ourDict, "price"))
print(getValue(ourDict, "productName"))
