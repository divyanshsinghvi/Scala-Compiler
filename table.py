#############################Table.py########################################
#This file creates a symbol table and initialises it with all variables of instruction
#code.And calculate next use of each of following

import ir
from symbolTable import SymbolTable
from nextUse import NextUse
#from basicBlock import basicBlock
from  globalvar import *
import numbers

def is_number(var):
    try:
        int(var)
        return True
    except Exception:
        return False

class Table:
    table = SymbolTable()
    b = basicBlock
    def __init__(self ,ac):
        for row in ac:
            if row.operator == 'binop':           #Reading all values in symboltable
                self.table.setVar(row.out,{'type':'int','live':1})
                self.table.setVar(row.in1,{'type':'int','live':1})
                self.table.setVar(row.in2,{'type':'int','live':1})
            elif row.operator == 'unop':
                self.table.setVar(row.out,{'type':'int','live':1})
                self.table.setVar(row.in1,{'type':'int','live':1})
            elif row.operator == 'assign':
                if is_number(row.in1):
                    self.table.setVar(row.out,{'value':row.in1})	
		else:
                    self.table.setVar(row.in1,{'type':'int','live':1})
                self.table.setVar(row.out,{'type':'int','live':1})
            elif row.operator == 'goto':
                self.table.setVar(row.out,{'type':'int','live':1})
            elif row.operator == 'if':
                self.table.setVar(row.out,{'type':'int','live':1})
                self.table.setVar(row.in1,{'type':'int','live':1})
            elif row.operator == 'param':
                self.table.setVar(row.out,{'type':'int','live':1})
            elif row.operator == 'fcall':
                self.table.setVar(row.out,{'type':'int','live':1})
                self.table.setVar(row.in1,{'type':'int','live':1})
            elif row.operator == 'freturn':
                self.table.setVar(row.in1,{'type':'int','live':1})
            elif row.operator == 'ldar':          
                self.table.setVar(row.out,{'type':'int','live':1})
                self.table.setVar(row.in1,{'type':'int','live':1})
                self.table.setVar(row.in2,{'type':'int','live':1})
            elif row.operator == 'star':          
                self.table.setVar(row.out,{'type':'int','live':1})
                self.table.setVar(row.in1,{'type':'int','live':1})
                self.table.setVar(row.in2,{'type':'int','live':1})
             

        l = self.b
            
        length = len(ac)                    #last block case dealt
        l.append(length)
        #print(l)
        #print(self.table.print_symboltable())

        for i in reversed(range(1,len(l))): 
            #print("Block form range "+str(l[i-1])+"to"+str(l[i]))
            NextUse(ac[l[i-1]:l[i]], self.table,l[i-1])
            #self.table.print_symboltable()
        #    no=1
        #for row in ac:
        #    print(str(no)+"------------------")
        #    no = no+1 
        #    for y in row.nextUse:
        #        print (y,':',row.nextUse[y])
        #    print("--------------")   
        #    for y in row.live:
        #        print (y,':',row.live[y])
 
        

#if __name__ == "__main__":
    #filename = '3ac.csv'
    #global tacTable= ir.irTable(filename).arr
#    Table(tacTable)

symbolTable = Table(tacTable).table
