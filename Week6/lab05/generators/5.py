n = int(input())
def revGenerator(n):
    while n >= 0:
        yield n
        n -= 1
reverse = revGenerator(n)
for i in reverse:
    print(i)