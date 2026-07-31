from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["securechain"]

users = db["users"]
transactions = db["transactions"]
transfers = db["transfers"]