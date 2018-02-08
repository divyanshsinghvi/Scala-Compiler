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
        if ST.getVar(name,'value') is None :
            print("\t.globl "+str(name))
            print(str(name)+":")
            print("\t."+ST.var[name]['type'])
        #else:
        #    print("\t."+ST.var[name]['type'])
        
if __name__ == '__main__':
    globalData()
