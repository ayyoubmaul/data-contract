from table_schema import person_pb2

person = person_pb2.Person()
person.name = "John Doe"
person.age = 30
person.hobbies.extend(["Reading", "Gardening"])

person_data = person.SerializeToString()

received_person = person_pb2.Person()
received_person.ParseFromString(person_data)

print("Name:", received_person.name)
print("Age:", received_person.age)
print("Hobbies:", received_person.hobbies)
