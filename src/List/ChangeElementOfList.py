inputNumbers = int(input("How many number will you enter:"))

myLists = []

for inputNumber in range(0, inputNumbers):
    item = int(input(f"{inputNumber + 1}. giriniz:"))
    myLists.append(item)

firstIndex = int(input("Please enter your first index:"))

secondIndex = int(input("Please enter your second index:"))

temp = myLists[firstIndex]
myLists[firstIndex] = myLists[secondIndex]
myLists[secondIndex] = temp

for myList in myLists:
    print(myList)
