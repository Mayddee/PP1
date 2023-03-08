str = input()
def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
if isPalindrome(str):
    print("The sring is palindrome!")
else:
    print("The sring is not palindrome!")   