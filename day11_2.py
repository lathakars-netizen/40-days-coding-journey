##  Method Overriding
#  A child class can replace a method from the parent class.
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
dog = Dog()
dog.sound()

## Encapsulation
## Encapsulation means protecting data inside a class.

class Student:
    def __init__(self):
        self.__marks = 95
    def show_marks(self):
        print(self.__marks)
s = Student()
s.show_marks()
# Notice:: the double underscore (__marks). This makes the variable private.

#Polymorphism
#The same method name can behave differently for different classe

class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
