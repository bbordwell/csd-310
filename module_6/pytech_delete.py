#Ben Bordwell Module 6.3 assignment. 11/16/2021
#This program add, then deletes a document from the database.

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ckvk8.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()

merry = {
    "student_id":"1010",
    "first_name":"Merry",
    "last_name":"Took"
}

print("-- INSERT STATEMENTS --")
merry_student_id = db.students.insert_one(merry).inserted_id
print(f"Inserted student record Merry Took into the students collection with document_id {merry_student_id}")
print()

student = db.students.find_one({"student_id":"1010"})
print("-- DISPLAYING STUDENT TEST DOC --")
print(f'Student ID: {student["student_id"]}')
print(f'First Name: {student["first_name"]}')
print(f'Last Name: {student["last_name"]}')
print()

result = db.students.delete_one({"student_id": "1010"})

docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()