import json

# JSON string representing a person
json_str = '{"name": "John", "age": 30, "city": "New York"}'

# Deserialize JSON string into a Python dictionary
data_dict = json.loads(json_str)

# Access the data as a Python object
name = data_dict["name"]
age = data_dict["age"]
city = data_dict["city"]


# Create a Python class to represent a person
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


# Create a Python object from the dictionary
person_obj = Person(name, age, city)

# Access object attributes
print("Name:", person_obj.name)
print("Age:", person_obj.age)
print("City:", person_obj.city)
