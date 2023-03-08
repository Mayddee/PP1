import string
str = input()
cnt1, cnt2 = 0, 0
for i in str:
    if i.isupper():
        cnt1 += 1
    elif i.islower():
        cnt2 += 1
    
print("Number of uppercase characters:", cnt1)
print("Number of lowercase characters:", cnt2)

