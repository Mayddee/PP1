a = input()
def isPalindrome(a):
    if a != a[::-1]:
        print('No')
    else:
        print('Yes')

isPalindrome(a)
