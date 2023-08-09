import json

data = {
    "ugurcankok": {
        "firstName":"ugurcan",
        "lastName":"kok"
    },
    "ugurcan": {
        "firstName":"ugur",
        "lastName":"can"
    }
}

with open("users2.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users2.json") as file:
    users = json.load(file)

print(users["ugurcankok"])
print(users["ugurcan"])

users.update({
    "aliali":
        {
            "firstName": "ali",
            "lastName": "ali",
            "age":30
        }
})

users.pop("ugurcan")

with open("users2.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)

