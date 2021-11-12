#Ben Bordwell Module 5.3 assignment 11/11/2021
#This program displays all documents in the students collection.

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

student = db.students.find_one({"student_id":"1007"})
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(f'Student ID: {student["student_id"]}')
print(f'First Name: {student["first_name"]}')
print(f'Last Name: {student["last_name"]}')