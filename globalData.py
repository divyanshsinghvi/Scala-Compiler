from globalvar import *
from symbolTable import *
def globalData():
    print("\t.data")
    for name in ST.var:
        if ST.getVar(name,'value') is not None :
            print("\t.globl "+str(name))
            print(str(name)+":")
            print("\t."+ST.var[name]['type']+" "+ST.var[name]['value'])
    print("\t.bss")
    for name in ST.var:
        if ST.getVar(name,'value') is None and ST.getVar(name,'type') == 'array':
            print("\t.globl "+str(name))
            print(str(name)+":")
            print("\t.zero " + str(int(ST.getVar(name,'size'))*4)) #all are integers so space is 4byte
        elif ST.getVar(name,'value') is None and ST.getVar(name,'type') == 'int':
            print("\t.globl "+str(name))
            print(str(name)+":")
            print("\t.zero 4") #all are integers so space is 4byte
        #else:
    print("\t.section\t.rodata")
    print(".format :")
    print('\t.string "%d\\n"')
    print(".format1 :")
    print('\t.string "%d "')
    print(".format2 :")
    print('\t.string "%d"')
        #    print("\t."+ST.var[name]['type'])
        
if __name__ == '__main__':
    globalData()
