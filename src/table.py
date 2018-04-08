#############################Table.py########################################
#This file creates a symbol table and initialises it with all variables of instruction
#code.And calculate next use of each of following

import ir
from symbolTableOld import SymbolTable
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
            if row.operator == 'binop' or row.operator == 'ldar' or row.operator == 'bitwise':           #Reading all values in symboltable
                self.table.setVar(row.out,{'live':1})
                self.table.setVar(row.in1,{'live':1})
                self.table.setVar(row.in2,{'live':1})
            elif row.operator == 'unop' or row.operator == 'array':
                self.table.setVar(row.out,{'live':1})
                self.table.setVar(row.in1,{'live':1})
            elif row.operator == 'assign':
                if is_number(row.in1):
                    self.table.setVar(row.out,{'value':row.in1})	
		else:
                    self.table.setVar(row.in1,{'live':1})
                self.table.setVar(row.out,{'live':1})
            elif row.operator == 'if':
                self.table.setVar(row.in1,{'live':1})
            elif row.operator == 'param':
                self.table.setVar(row.out,{'live':1})
            elif row.operator == 'fcall':
                self.table.setVar(row.out,{'live':1})
                self.table.setVar(row.in2,{'live':1})
            elif row.operator == 'call':
                self.table.setVar(row.in2,{'live':1})
            elif row.operator == 'freturn':
                self.table.setVar(row.in1,{'live':1})
            elif row.operator == 'ldar':          
                self.table.setVar(row.out,{'live':1})
                #self.table.setVar(row.in1,{'live':1})
                self.table.setVar(row.in2,{'live':1})
            elif row.operator == 'star':          
                self.table.setVar(row.out,{'live':1})
                self.table.setVar(row.in1,{'live':1})
                self.table.setVar(row.in2,{'live':1})
            #elif row.operator == 'array':
            #    if is_number(row.in1):
            #        self.table.setVar(row.out,{'type':'array','live':1,'size':row.in1})
            #    else:
            #        self.table.setVar(row.out,{'type':'array','live':1,'size':self.table.getVar(row.in1,'value')})
        for name in self.table.var:
            self.table.var[name]['nextUse']=None
            if name.startswith('#t'):
                self.table.var[name]['live']=0
            else:
                self.table.var[name]['live']=1
        
        #self.table.print_symboltable()
    def print_tactable(self,ac):
        l = self.b
        #print l     
        length = len(ac)                    #last block case dealt
        if l[-1] != length:
            l.append(length)
        #print(l)
        #print(self.table.print_symboltable())
    
        for i in range(1,len(l)): 
            print i
            print("Block form range "+str(l[i-1])+"to"+str(l[i]))
            NextUse(ac[l[i-1]:l[i]], self.table,l[i-1])
            #self.table.print_symboltable()
            no=1
            for row in ac:
                print(str(no)+"------------------")
                no = no+1 
                for y in row.nextUse:
                    print (y,':',row.nextUse[y])
                print("---------------------")   
                for y in row.live:
                    print (y,':',row.live[y])
 
        

#if __name__ == "__main__":
    #filename = '3ac.csv'
    #global tacTable= ir.irTable(filename).arr
#    Table(tacTable)

suppTable  = Table(tacTable).table
#Table(tacTable).print_tactable(tacTable)
