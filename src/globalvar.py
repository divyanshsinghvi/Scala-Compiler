#declare all global variabels here
import sys
import ir 

filename = sys.argv[1]

global tacTable
global addressDescr
global ST
global basicBlock
global ST1
tacBB = ir.irTable(filename)
tacTable = tacBB.arr
basicBlock=tacBB.leadList
#from symbolTable import SymbolTable
#ST = SymbolTable()


#from symbolTable import *
#ST = HashTable


addressDescr = {}

from table import suppTable
ST1 = suppTable

#print dir(ST)
for name in ST1.var:
    addressDescr[name]={'Register':None, 'Stack':None, 'Memory': name}
#    print name
