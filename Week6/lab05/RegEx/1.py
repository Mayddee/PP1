import re
str = "abbbbut"
pattern1 = r"ab*"
x = re.search(pattern1, str)
if x: 
    print("A match is found!")
else:
    print("Not matched!")

