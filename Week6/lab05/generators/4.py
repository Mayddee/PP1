a = int(input())
b = int(input())
def squares(a, b):
    if a <= b: 
     while a <= b:
        yield a**2
        a += 1
    else:
       while a >= b:
        yield a**2
        a -= 1

x = squares(a, b)
for i in x:
    print(i)