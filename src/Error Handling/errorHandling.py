# There are different error types

# Most of them:
# SyntaxError => written wrong
# NameError => used undefined variable
# ValueError => use of wrong type
# TypeError => incorrect parameter usage
# IndexError => wrong index number
# KeyError => trying to reach the key value that does not exist
# AttributeError => a property that does not exist

try:
    firstInput = int(input("x: "))
    secondInput = int(input("y: "))
    print(firstInput / secondInput)
except ZeroDivisionError:
    print("You cant divide by 0")
except ValueError:
    print("First and second input must be number")
except Exception as error:
    print(f"There is an error: {error}")
else:
    print("That else blog will always execute if you dont get error!!")
finally:
    print("If you got error or not finally blog will execute!!")
