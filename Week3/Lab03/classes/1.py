class toUpper:
    def __init__(self):
        self.str = str
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
x = toUpper()
x.getString()
x.printString()

