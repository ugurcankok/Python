import pymongo

client = pymongo.MongoClient("connection string")

my_db = client["mydatabase"]

my_col = my_db["customers"]

my_dict = { "name": "John", "address": "Highway 37" }

# Insert one document
# id fields added automatically. MongoDB assigned a unique _id for the record (document). You can give your unique id.

one_record = my_col.insert_one(my_dict)
print(one_record.inserted_id)

my_dict_id = { "_id": 1,"name": "John", "address": "Highway 37" }
one_record_id = my_col.insert_one(my_dict)

print(one_record.inserted_id)

# Insert more than one documents

my_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

manyRecord = my_col.insert_many(my_list)

print(manyRecord.inserted_ids)

# Find one documents

x = my_col.find_one()

# Find all documents
# Get 10 records

for x in my_col.find().limit(10):
  print(x)

# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field)

for x in my_col.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

# Find specific document

my_query = {"address": "Park Lane 38"}

for i in my_col.find(my_query):
    print(i)

# Advance query

my_query_advance = { "address": { "$gt": "S" } }

for i in my_col.find(my_query_advance):
    print(i)

# Sort documents

# 1 means that ascending, -1 means that descending. Default is ascending

my_sort = my_col.find().sort("name", 1)

for i in my_sort:
    print(i)

# Delete documents

my_query_delete = { "address": "Mountain 21" }

# Delete one document
my_col.delete_one(my_query)

# Delete more than one documents
my_col.delete_many(my_query)

# Delete all documents
my_col.delete_many({})

# Update documents
my_query_update = { "address": "Valley 345" }
new_values = { "$set": { "address": "Canyon 123" } }

# One record
my_col.update_one(my_query_update, new_values)

# More than one record
my_col.update_many(my_query_update, new_values)

# Drop Collection
my_col.drop()