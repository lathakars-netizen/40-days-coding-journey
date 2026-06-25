##  CONSTRUCTOR
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Simhadri", 18)

print(s1.name)
print(s1.age)

## methods
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Simhadri")

s1.display()