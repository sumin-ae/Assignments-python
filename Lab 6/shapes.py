import math

class Shape:
    def area(self):
        # Abstract method (to be overridden by subclasses)
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


shapes = [
    Rectangle(5, 10),   # Rectangle object
    Circle(7)           # Circle object
]

for shape in shapes:
    print(f"The area is: {shape.area():.2f}")
