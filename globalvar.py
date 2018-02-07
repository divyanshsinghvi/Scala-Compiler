#declare all global variabels here
import ir 

filename = '3ac.csv'
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
    addressDescr[name]={'Register':None, 'Stack':None, 'Memory':None}
#    print name
