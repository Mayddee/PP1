import re
str = "Python"
pattern3 = r"[A-Z][a-z]+"
x = re.findall(pattern3, str)
if x: 
    print(x)
    print("A match is found!")
else:
    print("Not matched!")
