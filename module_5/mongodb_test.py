from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ckvk8.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech COllection List --")
print(db.list_collection_names())
