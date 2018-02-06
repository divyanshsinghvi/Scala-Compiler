import ir
from symbolTable import SymbolTable
from nextUse import NextUse
from basicBlock import basicBlock

class Table:
    table = SymbolTable()
    b = basicBlock('3ac.csv')
    def __init__(self ,ac):
        for row in ac:
            if row.operator == 'binop':
                self.table.set(row.out,{'type':'int'})
                self.table.set(row.in1,{'type':'int'})
                self.table.set(row.in2,{'type':'int'})
            elif row.operator == 'assign' or 'unop':
                self.table.set(row.out,{'type':'int'})
                self.table.set(row.in1,{'type':'int'})
            l = self.b.leadList
        
        for i in range(0,len(l)-1):
            NextUse(ac[l[i]:l[i+1]], self.table)

if __name__ == "__main__":
    filename = '3ac.csv'
    instrTable = ir.irTable(filename).arr
    Table(instrTable)
                    
