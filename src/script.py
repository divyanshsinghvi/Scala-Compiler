f = open("input.txt", "rb")
s = f.readlines()
f.close()
f = open("input.txt", "wb")
for line in s:
    print>>f, line
f.close()
