s = input()
def permute(str, i = 0):
    if i == len(str):
        print("".join(str))
    for j in range(i, len(str)):
        wrd = [a for a in str]
        wrd[i], wrd[j] = wrd[j], wrd[i]
        permute(wrd, i + 1)
permute(s)
        
