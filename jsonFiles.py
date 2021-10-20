import json

# Person's JSON

# person = '{"name" : "Ashrith","city" : "Pune","pincode" : "101010"}' # JSON STRING
# print(person)
# print(type(person))

# personDict = json.loads(person)

# print(personDict['name'])



person = {
    "name" : "Sanket",
    "age" : 21,
    "city" : "Mumbai",
    "designation" : "python Developer"
}

# print(person)

personJsonString = json.dumps(person)
print(personJsonString)
print(type(personJsonString))

