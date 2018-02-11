## given the input as block, symbol table and offset of block updates global instructionCode in globalvar with nexuse and live information.
import ir
from symbolTable import SymbolTable

def is_number(var):
    try:
        int(var)
        return True
    except Exception:
        return False


class NextUse:

    def __init__(self,block,table,offset):
        number = len(block)+offset
        prev=None
        for row in reversed(block):
            if prev is not None:
                row.nextUse = prev.nextUse;
                row.live = prev.live

            if row.operator == 'binop': 
                row.live[row.out]=table.getVar(row.out,'live')
                row.live[row.in2]=table.getVar(row.in2,'live')
                row.live[row.in1]=table.getVar(row.in1,'live')
                
                row.nextUse[row.out] = table.getVar(row.out,'nextUse') 
                row.nextUse[row.in2] = table.getVar(row.in2,'nextUse') 
                row.nextUse[row.in1] = table.getVar(row.in1,'nextUse')
                #print(row.out+row.in2+row.in1)
                table.setVar(row.out,{'live':None,'nextUse':None})
                table.setVar(row.in2,{'live':1,'nextUse':number})
                table.setVar(row.in1,{'live':1,'nextUse':number})
            elif row.operator == 'unop':
                row.live[row.out]=table.getVar(row.out,'live')
                row.live[row.in1]=table.getVar(row.in1,'live')
            
                row.nextUse[row.out] = table.getVar(row.out,'nextUse') 
                row.nextUse[row.in1] = table.getVar(row.in1,'nextUse') 
                #print(row.out+row.in1)
                table.setVar(row.out,{'live':None,'nextUse':None})
                table.setVar(row.in1,{'live':1,'nextUse':number})
            elif row.operator == 'assign':
		
                row.live[row.out]=table.getVar(row.out,'live')
            	row.nextUse[row.out] = table.getVar(row.out,'nextUse') 
                
		if not is_number(row.in1):
		    row.nextUse[row.in1] = table.getVar(row.in1,'nextUse') 
                    row.live[row.in1]=table.getVar(row.in1,'live')
                    table.setVar(row.in1,{'live':1,'nextUse':number})
                #print(row.out+row.in1)
                table.setVar(row.out,{'live':None,'nextUse':None})
            #table.print_symboltable()
            prev = row
            number = number-1 
    
        for name in table.var:    #global assumed
            table.var[name]['nextUse']=None
            table.var[name]['live']=1

if __name__ == "__main__":
    t = ir.irTable('3ac.csv').arr
    NextUse(t)
    
