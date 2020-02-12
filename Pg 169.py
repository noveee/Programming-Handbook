# Challenge 1
class Square():
    squarelist = []

    def __init__(self, x):
        self.x = x
        self.squarelist.append(x)

    # Challenge 2
    def __repr__(self):
        self.x = str(self.x)
        return self.x + " by " + self.x + " by " + self.x + " by " + self.x

square = Square(29)
square2 = Square(30)

print(square)

# Challenge 3
def same_object(x, y):
    if(x is y):
        print(True)
    else:
        print(False)

same_object(square, square2)