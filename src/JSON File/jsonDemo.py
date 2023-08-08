import json
def addProduct(productName, price, isActive, categories):
    product = {
        "productName": productName,
        "price": price,
        "isActive": isActive,
        "categories": categories
    }

    with open("products.json","w") as file:
        json.dump(product, file, ensure_ascii=False)

addProduct("iphone 12",8000,True,["phone","electronic"])

def getProducts():
    with open("products.json") as file:
        products = json.load(file)

    categories = ' '.join([category for category in products["categories"]])

    print(f'product name: {products["productName"]} price: {products["price"]} category: {categories}')

getProducts()