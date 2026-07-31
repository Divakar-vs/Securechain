from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["securechain"]

transactions = db["transactions"]

print("\n=== SAVED TRANSACTIONS ===\n")

for tx in transactions.find():
    print(tx)
    print("-" * 60)