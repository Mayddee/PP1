import re
str = "camelCase"
pattern10 = r"(.)([A-Z].+)"
x1 = re.sub(pattern10, r"\1_\2", str)
print(x1.lower())