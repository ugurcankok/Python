'''
one=int(input("Enter your number:"))

if one>10:
    print("Your number is greater than 10.")
elif one==10:
    print("Your number is equal number!")
else:
    print("Your number is lower than 10")

a=input("Enter your name:")
if a=="ugurcan":
    print("Your name is good :):)")
else:
    print("Your name is eh işte!!!")
'''
'''name=input("Enter your name:")
if len(name)>5:
    print("Your name is biggest name!")
elif len(name)==5:
    print("Your name length is equal 5.")
else:
    print("Your name is smallest name in the word!!")'''
def one():
    print("merhaba")

def switc(argument):
    switcher={
        0:one,
        1:"two",
        2:lambda :"three",
    }
    return switcher.get(argument,lambda :"nothing")

a=int(input("Enter your choice:"))
if a>=3:
    print("Please enter correct input!!")
switc(a)

