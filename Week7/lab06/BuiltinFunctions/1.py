import math
lis = [int(x) for x in input().split()]
res = math.prod(lis)
#res = reduce((lambda a, b: a * b), list)
print(res)