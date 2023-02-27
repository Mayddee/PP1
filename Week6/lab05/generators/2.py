n = int(input())
def evenGenerator(n):
    a = 0
    while a <= n:
        if a%2==0:
            yield a
            a += 2
        else:
            a += 1
even = evenGenerator(n)
print(*even, sep =", ")
    