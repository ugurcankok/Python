numberList = [1, 2, 3, 4, 5, 6]

stringList = ["1", "2", "3", "4", "5"]

nameList = ["ugur", "can", "kök"]

userInfo = [
    {"name": "ugur", "lastname": "kök"},
    {"name": "can", "lastname": "kök"}
]

numberResult = list(map(lambda x: x ** 2, numberList))  # you can use list comprehension instead of map function

stringResult = list(map(int, stringList))  # change the data type of each element in the list

nameResult = list(map(str.capitalize, nameList))

userInfoResult = list(map(lambda result: result["name"], userInfo))

print(userInfoResult)
