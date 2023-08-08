# If we can read the data in the file and bring it to the dictionary format, it is called deserialize.

import json

with open("person.json") as file:
    data = json.load(file) # if we read from file, we use load which is not plural one


print(data["firstName"])
print(data["hobbies"])

# json-string

data = """
    {
      "firstName":"ugur", 
      "lastName":"kok",
      "hobbies": ["sport","cinema"],
      "age":27,
      "children": [
        {
          "firstName": "ali",
          "age":10
        }
      ]
    }
    """

data = json.loads(data) # if we read from json-string, we use loads which is plural one

print(data["hobbies"])
print(data["hobbies"][0])