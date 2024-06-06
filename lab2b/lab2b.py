"""
   2b. Demonstrate object serialization in python by creating a custom class called employee.  This stores Employee name, age, salary, married and having kid. Save it and load it up into a separate object and display the new object.
"""

import pickle


class Employee:
    def __init__(self, name, age, salary, married=False, has_kids=False):
        self.name = name
        self.age = age
        self.salary = salary
        self.married = married
        self.has_kids = has_kids

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Married: {self.married}, Has Kids: {self.has_kids}"


# Creating an instance of the Employee class
employee1 = Employee("John Doe", 30, 50000, married=True, has_kids=True)

# Serializing the object to a file using pickle
with open("employee.pickle", "wb") as file:
    pickle.dump(employee1, file)

# Loading the serialized object from the file
with open("employee.pickle", "rb") as file:
    employee2 = pickle.load(file)

# Displaying the attributes of the new object
print("New Employee Object:")
print(employee2)
