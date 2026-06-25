class Student:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)

s1 = Student("Simhadri", "AIML")

s1.display()