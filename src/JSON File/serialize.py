# If we can transfer json string to file, it is called serialize

import json

person = {
    "firstName":"ugur",
    "lastName":"kok",
    "hobbies": [
        "sport",
        "cinema"
    ],
    "age":27,
    "children": [
        {
          "firstName": "ali",
          "age":10
        }
    ]
}

print(person["firstName"])

#result = json.dumps(person, ensure_ascii=False, indent=2) # ensure_ascii=False for ignore character

with open("person.json","w") as file:
    json.dump(person,file, ensure_ascii=False,indent=2)