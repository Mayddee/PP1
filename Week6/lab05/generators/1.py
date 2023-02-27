n = int(input())
def squareGenerator(n):
    a = 1
    while a <= n:
        yield a**2
        a += 1

square = squareGenerator(n)
for i in square:
    print(i)