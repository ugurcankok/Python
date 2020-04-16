def factoriel():
    try:
        a=int(input("Enter your number:"))
        if a<0:
            print("Please enter positive number!!")
        else:
            multiple=1
            condition=1
            while condition<=a:
                multiple*=condition
                condition+=1
            print("Your factoriel is",multiple)
    except ValueError:
        print("Please enter a number!!")

'''
if you want to write while part in the funtion like that
factoriel=1
for each in range(1,a+1):
    factoriel*=each
'''

while (True):
    factoriel()
    while True:
        try:
            print("Do you want to continue?")
            d=int(input("Enter 1 or 0:"))
            if d== 1 :
                factoriel()
            else:
                exit(0)
        except ValueError:
                print("Please enter a correct version!!")
                continue
