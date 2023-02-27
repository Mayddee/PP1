import re
str = "abbb"
pattern2 = r"ab{2,3}"
x = re.search(pattern2, str)
if x: 
    print("A match is found!")
else:
    print("Not matched!")
