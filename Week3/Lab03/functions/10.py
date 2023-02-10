list = [int(x) for x in input().split()]
def NewList(l):
    l2 = []
    for x in l:
        if x not in l2:
            l2.append(x)
    print(l2)
NewList(list)
        