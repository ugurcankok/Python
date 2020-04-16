'''
x=["1","2","3","4","5"]#[1,2,3,4,5]
for number in x:
    print(number)


run=True
counter=0
print("\n")
while run:
    if counter == 20:
        run=False
    else:
        print(counter)
        counter +=1
'''
'''
import re

string="I AM UGURCAN , my department is computer engineering.."
print(string)
new=re.sub("[A-Z]","",string)
new1=re.sub("[.]",",",string)
print(new)
print(new1)
string1=string+"45 995 - 7345"
new2=re.sub("[^0-9]","",string1)
print(new2)
'''
'''
x=[]
condition=0
a=int(input("How many numbers will you enter:"))
while condition<a:
    c=int(input("Enter your number:"))
    x.append(c)
    condition+=1

for each in x:
    z=sum(x)

print(z)
'''

'''
for x in range(1,11):
    print(x)
x=[]
b=int(input("Enter your number:"))
x.append(b)
print(x)
'''
import sys
a=sys.version
print(a)
import os
b=os.name
print(b)