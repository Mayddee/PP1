n = int(input())
def DivisGenerator(n):
    a = 0
    while a <= n:
        if a%3 == 0 and a%4==0:
            yield a
        a += 1
b = DivisGenerator(n)
for i in b:
    print(i)