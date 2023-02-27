import re
str = "YouAreAProgrammer"
pattern9 = r"(.)([A-Z])"
x = re.sub(pattern9, r"\1 \2", str)
print(x)