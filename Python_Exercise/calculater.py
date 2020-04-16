import re

print("Welcome to my calculater")
print("Type quit to exit the program")

previous=0
run=True

def Math1():
    global run
    global previous
    answer=""
    if previous==0:
        answer=input("Enter your equation:")
    else:
        answer=input(str(previous))

    if answer=="quit":
        print("Goodby.See you soon :)")
        run = False
    else:
        answer=re.sub('[a-zA-Z,.:()" "]',"",answer)
        if previous==0:
            previous=eval(answer)
        else:
            previous=eval(str(previous)+answer)
while run:
    Math1()