list = [int(n) for n in input().split()]
def has_33(x):
  for i in range(len(x)):
    if x[i] == 3 and x[i-1] == 3:
        return True
        break
  return False
print(has_33(list))