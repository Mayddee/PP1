F = int(input())
def readTemp(f):
    c = (5 / 9) * (f - 32)
    return c
C = readTemp(F)
print(C)