file = open("0read.txt", "r")
for cnt, l in enumerate(file):
    pass
print(f"{cnt + 1} lines in the file")
file.close()