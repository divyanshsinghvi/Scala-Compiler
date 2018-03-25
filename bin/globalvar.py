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

from table import symbolTable
ST = symbolTable

addressDescr = {}

#print dir(ST)
for name in ST.var:
    addressDescr[name]={'Register':None, 'Stack':None, 'Memory': name}
#    print name
