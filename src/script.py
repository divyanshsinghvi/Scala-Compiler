def printa1(a1, out):
    for i in range(0,len(a1)-1):
        print>>out, a1[i],
    print>>out, "<font color=\"red\">"+a1[-1]+"</font>",

def printa1last(a1, out):
    for i in range(0,len(a1)):
        print>>out, a1[i],

def printa2(a2, out):
    for i in range(0,len(a2)):
        print>>out, a2[i],
    print>>out, "<br/><br/>"

def update(a1, a2,line):
    a1.pop()
    for i in range(1, len(line)):
        a1.append(line[i])
    for i in reversed(a1):
        if i == "epsilon" or i.startswith('LexToken'):
            word = a1.pop()
            a2.insert(0,word)
        else:
            break

f = open("input.txt", "rb")
s = f.readlines()
s.reverse()
f.close()

f = open("input.txt", "wb")
for line in s:
    print>>f, line,
f.close()
inp = open("input.txt", "rb")
a1 = list(["compilation_unit"])
a2 = list([])
out = open("output.html", "wb")
print>>out, "<!DOCTYPE html>\n<html>\n<head>\n<title>Derivation</title>\n</head>\n<body>\n<p>"

for line in inp:
    line = line.split()
    printa1(a1,out)
    printa2(a2,out)
    update(a1,a2,line)

printa1last(a1,out)
printa2(a2,out)

print>>out, "</p>\n</body>\n</html>"
out.close()
inp.close()
