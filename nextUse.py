## given the input as block, symbol table and offset of block updates global instructionCode in globalvar with nexuse and live information.
import ir
from symbolTable import SymbolTable


class NextUse:

    def __init__(self,block,table,offset):
        number = len(block)+offset
        for row in reversed(block):
            if row.operator == 'binop': 
                if table.getVar(row.out,'live') is not None:
                    row.live[row.out]=table.getVar(row.out,'live')
                else:
                    row.live[row.out]=0

        
                if table.getVar(row.in2,'live') is not None:
                    row.live[row.in2]=table.getVar(row.in2,'live')
                else:
                    row.live[row.in2]=0
                
                if table.getVar(row.in1,'live') is not None:
                    row.live[row.in1]=table.getVar(row.in1,'live')
                else:
                    row.live[row.in1]=0
                
                row.nextUse[row.out] = table.getVar(row.out,'nextUse') 
                row.nextUse[row.in2] = table.getVar(row.in2,'nextUse') 
                row.nextUse[row.in1] = table.getVar(row.in1,'nextUse')
                #print(row.out+row.in2+row.in1)
                table.setVar(row.out,{'live':0,'nextUse':None})
                table.setVar(row.in2,{'live':1,'nextUse':number})
                table.setVar(row.in1,{'live':1,'nextUse':number})
            elif row.operator == 'assign' or row.operator == 'unop':
                if table.getVar(row.out,'live') is not None:
                    row.live[row.out]=table.getVar(row.out,'live')
                else:
                    row.live[row.out]=0
    
                if table.getVar(row.in1,'live') is not None:
                    row.live[row.in1]=table.getVar(row.in2,'live')
                else:
                    row.live[row.in1]=0 
            
                row.nextUse[row.out] = table.getVar(row.out,'nextUse') 
                row.nextUse[row.in1] = table.getVar(row.in1,'nextUse') 
                #print(row.out+row.in1)
                table.setVar(row.out,{'live':0,'nextUse':None})
                table.setVar(row.in1,{'live':1,'nextUse':number})
            #for y in row.nextUse:
            #    if y and row.nextUse[y] is not None:
            #print (y +':' +str(row.nextUse[y]))
            #table.print_symboltable()
            number = number-1 
if __name__ == "__main__":
    t = ir.irTable('3ac.csv').arr
    NextUse(t)
    
