class Person:
    def introduce(self):
        print("I am a person")
class Student(Person):
    pass

s = Student()
s.introduce()