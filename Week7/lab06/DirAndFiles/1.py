import os
path = input()
#"C:\pp2"
dirFile = os.listdir(path)
files =[f for f in dirFile if os.path.isfile(os.path.join(path, f))]
dirs = [d for d in dirFile if not os.path.isfile(os.path.join(path, d))]
print("Only directories:", [*dirs])
print("Only files:", [*files])
print("All files and directories:", dirFile)
