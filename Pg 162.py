# Challenge 1

# Challenge 3
class Shape():
    def what_am_i(self): 
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_perimeter(self, x, y):
        return (x*2) + (y*2)

class Square(Rectangle, Shape):
    pass
    def __init__(self, x):
        self.x = x
        self.y = x

    # Challenge 2
    def change_size(self, x):
        self.x = self.x + x
        self.y = self.y + x


square = Square(2)
rectangle = Rectangle(4, 7)

print(square.calculate_perimeter(square.x, square.y))
print(rectangle.calculate_perimeter(rectangle.x, rectangle.y))

square.what_am_i()

# Challenge 4
class Horse():
    def __init__(self, size, speed, rider):
        self.size = size
        self.speed = speed
        self.rider = rider

class Rider():
    def __init__(self, rider):
        self.name = rider

rider = Rider("Jay")
horse = Horse("Big", 20, rider)

