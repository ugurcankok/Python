import random

player=260
x=60
y=80

while player>0:
    dmg=random.randrange(x,y)
    player=player-dmg

    if player<=30:
        player=30
    print("demage",dmg,"player",player)
    if player==30:
        print("This is end.")
        break
    '''
    if player > 30:
    continue
    print("This is end")
    break
    '''

'''

a=int(input("How many number will you enter:"))
condition=0
x=[]
while condition<a:
    c=int(input("Enter your number:"))
    x.append(c)
    condition+=1

print(sorted(x))

d=int(input("How many number will you remove:"))
condition1=0
while condition1<d:
    e=int(input("Enter your number:"))
    x.remove(e)
    condition1+=1

z=min(x)
con=0

while con<3:
    x.pop(z)
    con+=1

print(sorted(x))


'''
dictinary={"name":"ugurcan","lastname":"kök","city":"aydın"}
keys=dictinary.keys()
value=input("Please enter name:")
if value in value:
    print("correct name")
else:
    print("wrong name")