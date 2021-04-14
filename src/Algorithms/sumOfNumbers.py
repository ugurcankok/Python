a=int(input("Enter your initial value:"))
b=int(input("Enter your final value:"))
c=int(input("Enter your step value:"))

sum=0

while a<=b:
    sum+=a
    a+=c


print("Your result is:",sum)
