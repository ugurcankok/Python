
def add():
    file = open("staj.txt", "a")
    personNum = int(input("How many person will you add:"))
    condition=0
    while condition<personNum:
        a =input("Please enter his/her ID,name,lastname,city (Please keep this line)\n")
        condition+=1
        file.write(a+"\n")
    print("Your record added!!")
    file.close()

def search():
    file=open("staj.txt","r").readlines()
    error=""
    id=input("Enter his/her ID:")
    for i in file:
        if(i.split(',')[0]==id):
            print("Record: " + i)
        else:
            error="Your record cannot find!!"

def show():
    file=open("staj.txt","r").read().splitlines()
    print(file)

def menu():
    print("1-Add person")
    print("2-Search person")
    print("3-Show all record")
    print("4-Exit")


print("*** Welcome to my program ***")
while True:
    menu()
    try:
        d = int(input("Choose what you want:"))
    except ValueError:
        print("Please enter correct value!")
        continue
    if d == 1:
        print("**Welcome to adding section**")
        add()
    elif d == 2:
        print("**Welcome to searching section**")
        search()
    elif d == 3:
        print("** All Records **")
        show()
    elif d == 4:
        print("**Goodbye :( **")
        exit(0)
    else:
        print("INVALID CHOICE! Please check your choice!!")