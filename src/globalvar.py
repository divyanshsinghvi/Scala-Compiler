#declare all global variabels here
import sys
import ir 

filename = sys.argv[1]

global tacTable
global addressDescr
global ST
global basicBlock
tacBB = ir.irTable(filename)
tacTable = tacBB.arr
basicBlock=tacBB.leadList


#from symbolTable import *
#ST = HashTable


addressDescr = {}

#from table import suppTable
#ST = suppTable

#print dir(ST)
#for name in ST.var:
#    addressDescr[name]={'Register':None, 'Stack':None, 'Memory': name}
#    print name


