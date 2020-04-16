
userName="ugurcan"
userPassword="1234"

while(True):
    name=input("Enter your user name:")
    password=input("Enter your password:")
    if userName==name and userPassword==password:
        print("Welcome again")
        break
    elif userName!=name and userPassword==password:
        print("Your user name is nor correct.Please check it!!")
    elif userName==name and userPassword!=password:
        print("Your password is not correct.Please check it!!")
        print("Do you want to change your password?")
        while (True):
            try:
                answer=int(input("Enter 1 or 0:"))
                if (answer == 1):
                    newPassword = input("Enter your new password:")
                    print("Please wait..")
                    userPassword = newPassword
                    print("Your password uptaded..")
                    break
                else:
                    break
            except ValueError:
                print("Please enter correct version!!")
                continue
    else:
        print("Try again..")