#Ben Bordwell Module 5.2 assignment 11/11/2021
#This program tests conecting to a MongoDB and displays the collections it contains.

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ckvk8.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech COllection List --")
print(db.list_collection_names())
