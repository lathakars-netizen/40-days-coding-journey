# inheritance
class Animal:

    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    pass

d = Dog()

d.sound()

#Adding New Methods
class Animal:

    def sound(self):
        print("Animals make sounds")

class Dog(Animal):

    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()