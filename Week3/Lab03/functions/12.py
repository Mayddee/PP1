list = [int(x) for x in input().split()]
def histogram(l):
    for i in range(len(l)):
        for j in range(l[i]):
            print('*', end="")
        print('')
histogram(list)