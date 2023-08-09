import json

data = [
    {
        "userName": "ugurcan",
        "firstName": "ugur",
        "lastName": "can"
    },
     {
        "userName": "ugur",
        "firstName": "can",
        "lastName": "kok"
    }
]

user = {
        "userName": "ali",
        "firstName": "ali",
        "lastName": "ali"
}


with open("users.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users.json") as file:
    users = json.load(file)

users.append(user)

for user in users:
    if user["userName"] == "ugurcan":
        user["userName"] = "ugurcankok"

users.remove(users[0])