## Method overriding
class Shape:
    def area(self):
        print("Area")
class Square(Shape):
    def area(self):
        print("Area = side × side")

sq = Square()
sq.area()