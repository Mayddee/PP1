list = [int(x) for x in input().split()]
def filter_prime(l):
    for i in range(2, l-1):
        if l % i == 0:
            return False
    return True
for i in range(len(list)):
    if filter_prime(list[i]):
        print(list[i], end=" ")
