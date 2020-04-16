'''
def Function():
    print("This is my first function!!")
    print("hello guuuyyssss!!")

Function()

def function(a,b):
    print("\n"+a)
    print(b)

function("This is string","This is string as well")

def fonksiyon(name,age):
    print("My name is " + name + " my age is " + age)#str(age)

fonksiyon("ugurcan","23")

def fonk(name,age):
    print("My name is",name,"my age is",age )

fonk("ugurcan",23)

def fonk2(name="someone",age="unknown"):
    print("My name is",name,"my age is",age)

fonk2("ugurcan")
fonk2(None,23)
fonk2(age=23,name="ugurcan")
fonk2(age=23)
'''
'''
def function(*people):
    for person in people:
        print("Your name is",person)

function("ugur","can","kerem","ilayda")

x=["1","2","3","4","5"]
for number in x:
    print(number)
'''
'''
def fonksiyon(num1,num2):
    return num1+num2

a=fonksiyon(4,5)
print("Result is",a)

one=int(input("Enter your number:"))
two=int(input("Enter your second number:"))
d=fonksiyon(one,two)
print("Result is",d)
'''
def fonksiyon(num1,num2):
    return num1+num2

a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
print("Result is",fonksiyon(a,b))

def func(name="someone",age="unkonown"):
    print("My name is " + name + " ,my age is " + str(age))

b=input("Enter your name:")
a=int(input("Enter your age:"))
func(name=b,age=a)