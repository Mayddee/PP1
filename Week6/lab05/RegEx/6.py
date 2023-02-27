import re
str = "asdf hf. kj,"
pattern6 = r"[\s,.]"
x = re.sub(pattern6, ":", str)
print(x)