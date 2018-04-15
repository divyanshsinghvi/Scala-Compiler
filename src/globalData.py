from globalvar import *
from symbolTableOld import *
def globalData():
#    print("\t.data")
#    for name in ST1.var:
#        if ST1.getVar(name,'value') is not None :
#            print("\t.globl "+str(name))
#            print(str(name)+":")
#            print("\t."+ST1.var[name]['type']+" "+ST1.var[name]['value'])
#    print("\t.bss")
#    for name in ST1.var:
#        if ST1.getVar(name,'value') is None and ST1.getVar(name,'type') == 'array':
#            print("\t.globl "+str(name))
#            print(str(name)+":")
#            print("\t.zero " + str(int(ST1.getVar(name,'size'))*4)) #all are integers so space is 4byte
#        elif ST1.getVar(name,'value') is None and ST1.getVar(name,'type') == 'int':
#            print("\t.globl "+str(name))
#            print(str(name)+":")
#            print("\t.zero 4") #all are integers so space is 4byte
        #else:
    print("\t.section\t.rodata")
    print(".format :")
    print('\t.string "%d\\n"')
    print(".format1 :")
    print('\t.string "%d "')
    print(".format2 :")
    print('\t.string "%d"')
        #    print("\t."+ST1.var[name]['type'])
        
if __name__ == '__main__':
    globalData()
