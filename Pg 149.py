import math

# Challenge 1
class Apple:
    def __init__(self, c, w, f, m):
        self.color = c
        self.weight = w
        self.feeling = f
        self.mold = m

# Challenge 2

class Circle:
    def __init__(circle, r):
        circle.radius = r

    def area(self, r):
        return ((math.pi*r)**2)

circle = Circle(2)
print(circle.area(circle.radius))

# Challenge 3
class Triangle:
    def __init__(triangle, h, b):
        triangle.height = h
        triangle.base = b

    def area(self, h, b):
        return ((h*b)/2)

triangle = Triangle(1, 2)
print(triangle.area(triangle.height, triangle.base))

# Challenge 4
class Hexagon:
    def __init__(hexagon, s):
        hexagon.side = s
    
    def calculate_perimeter(self, s):
        return (s*6)

hexagon = Hexagon(3)
print(hexagon.calculate_perimeter(hexagon.side))