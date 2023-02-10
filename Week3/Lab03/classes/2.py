class Shape:
    def area1(self):
        return 0
class Square(Shape):
    def __init__(self):
        length = int(input())
        self.length = length
    def area2(self):
        return self.length ** 2
x = Square()
print(x.area1())
print(x.area2())
    