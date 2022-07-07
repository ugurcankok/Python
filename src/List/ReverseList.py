inputNumbers = int(input("How many number will you enter:"))

myLists = []

for inputNumber in range(0, inputNumbers):
    item = int(input(f"{inputNumber + 1}. giriniz:"))
    myLists.append(item)

for myList in range(0, int(inputNumbers / 2)):
    temp = myLists[myList]
    myLists[myList] = myLists[inputNumbers - myList - 1]
    myLists[inputNumbers - myList - 1] = temp

for myList in myLists:
    print(myList)
