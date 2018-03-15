import shlex

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

def update(a1, a2, line, out):
    a1.pop()
    for i in range(1, len(line)):
        a1.append(line[i])
    for i in reversed(a1):
        if i.startswith('LexToken'):
            word = a1.pop()
            a2.insert(0,word)
        elif i == "epsilon":
            printa1(a1, out)
            printa2(a2, out)
            a1.pop()
        else:
            break

with open("input.txt", "rb") as f:
    f.seek(0)
    s = f.readlines()
    s.reverse()
#f.close()

with open("new.txt", "wb+") as f:
    f.seek(0)
    for line in s:
        print>>f, line,

#f.close()
with open("new.txt", "rb") as inp:
    inp.seek(0)
    a1 = list(["compilation_unit"])
    a2 = list([])
    out = open("output.html", "wb")
    out.seek(0)
    print>>out, "<!DOCTYPE html>\n<html>\n<head>\n<title>Derivation</title>\n</head>\n<body>\n<p>"
    for line in inp:
        line = shlex.split(line)
        printa1(a1,out)
        printa2(a2,out)
        update(a1,a2,line, out)

    printa1last(a1,out)
    printa2(a2,out)
    print>>out, "</p>\n</body>\n</html>"

    out.close()

#inp.close()
