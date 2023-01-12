inputNumbers = int(input("How many number will you enter:"))

myLists = []

for inputNumber in range(0, inputNumbers):
    item = int(input(f"{inputNumber + 1}. enter:"))
    myLists.append(item)

maxElement = myLists[0]
minElement = myLists[0]

for myList in range(0, inputNumbers):
    if myLists[myList] < minElement:
        minElement = myLists[myList]
    if myLists[myList] > maxElement:
        maxElement = myLists[myList]

print(f"Max element is {maxElement}")
print(f"Min element is {minElement}")
