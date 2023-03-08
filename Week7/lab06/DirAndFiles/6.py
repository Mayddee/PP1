import string as s
upcs= s.ascii_uppercase
for letter in upcs:
    f = open(letter+".txt", "w")
    f.close()
