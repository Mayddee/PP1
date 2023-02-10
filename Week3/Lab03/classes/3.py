class Shape:
    def area1(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        length = int(input())
        width = int(input())
        self.length = length
        self.width = width
    def area2(self):
        return self.length * self.width
x = Rectangle()
print(x.area1())
print(x.area2())