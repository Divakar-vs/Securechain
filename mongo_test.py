from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create/use database
db = client["mydatabase"]

# Create/use collection
collection = db["users"]

# Insert data
collection.insert_one({"name": "Divakar", "project": "Blockchain Storage"})

# Read data
for doc in collection.find():
    print(doc)