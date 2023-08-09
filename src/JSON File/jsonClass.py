import json

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

p1 = Product("Samsung S10",5000)
p2 = Product("Samsung S11",6000)

products = [p1.__dict__,p2.__dict__] # it makes class serializable

'''products = {
    p1.id: p1.__dict__,
    p2.id: p2.__dict__
    }'''

with open("products.json","w") as file:
    json.dump(products,file)

with open("products.json") as file:
    data = json.load(file)

products = []

for p in data:
    products.append(Product(p["name"],p["price"]))

print(products)