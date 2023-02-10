from math import *
class Point:
    def __init__(self):
        x = int(input())
        y = int(input())
        x2 = int(input())
        y2 = int(input())
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    def show(self):
        print(self.x, self.y)
    def move(self):
        self.x2 += self.x
        self.y2 += self.y
        print(self.x2, self.y2)
    def dist(self):
        d = sqrt((self.x2 - self.x)**2 + (self.y2 - self.y)**2)
        print(d)
pnt = Point()
pnt.show()
pnt.move()
pnt.dist()