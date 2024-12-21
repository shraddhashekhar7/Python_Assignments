class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


s = Square(2)
print("Area of square is:", s.area())
s2 = Shape()
print("Area of shape is:", s2.area())
