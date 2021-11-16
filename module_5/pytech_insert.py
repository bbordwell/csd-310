#Ben Bordwell Module 5.3 assignment 11/11/2021
#This program inserts three student documents.

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ckvk8.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

thorin = {
    "student_id":"1007",
    "first_name":"Thorin",
    "last_name":"Oakenshield"
}

bilbo = {
    "student_id":"1008",
    "first_name":"Bilbo",
    "last_name":"Baggins"
}

frodo = {
    "student_id":"1009",
    "first_name":"Frodo",
    "last_name":"Baggins"
}


print("-- INSERT STATEMENTS --")
thorin_student_id = db.students.insert_one(thorin).inserted_id
print(f"Inserted student record Thorin Oakenshield into the students collection with document_id {thorin_student_id}")
bilbo_student_id = db.students.insert_one(bilbo).inserted_id
print(f"Inserted student record Bilbo Baggins into the students collection with document_id {bilbo_student_id}")
frodo_student_id = db.students.insert_one(frodo).inserted_id
print(f"Inserted student record Frodo Baggins into the students collection with document_id {frodo_student_id}")

