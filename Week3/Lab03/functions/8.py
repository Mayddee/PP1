list = [int(x) for x in input().split()]
def spy_game(l):

  cnt = 0
  for i in range(len(l)):
    if l[i] == 0:
        cnt += 1
    elif cnt >= 2 and l[i] == 7:
        cnt += 1
        break

  if cnt == 3:
    print('True')
  else:
    print('False')
spy_game(list)