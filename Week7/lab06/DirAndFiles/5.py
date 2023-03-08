file = open("0read.txt", "w")

for x in input().split():
    file.write(x+"\n")
file.close()