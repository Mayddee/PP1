import os
p = input()
if os.path.exists(p):
    print("Path exists")
    print("File name:", os.path.basename(p))
    print("Dir portion:", os.path.dirname(p))
else:
    print("Path does not exist")