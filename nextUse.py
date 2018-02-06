import ir
from symbolTable import SymbolTable


class NextUse:

    def __init__(self,block,table):
        number = len(block)
        for row in reversed(block):
            if row.operator == 'binop': 
                if table.get(row.out,'live') is not None:
                    row.live[row.out]=table.get(row.out,'live')
                else:
                    row.live[row.out]=0
        
                if table.get(row.in2,'live') is not None:
                    row.live[row.in2]=table.get(row.in2,'live')
                else:
                    row.live[row.in2]=0
                
                if table.get(row.in1,'live') is not None:
                    row.live[row.in1]=table.get(row.in1,'live')
                else:
                    row.live[row.in1]=0
                
                table.set(row.out,{'live':'0','nextUse':None})
                table.set(row.in2,{'live':'1','nextUse':number})
                table.set(row.in1,{'live':'1','nextUse':number})
            elif row.operator == 'assign' or 'unop':
                if table.get(row.out,'live') is not None:
                    row.live[row.out]=table.get(row.out,'live')
                else:
                    row.live[row.out]=0
    
                if table.get(row.in1,'live') is not None:
                    row.live[row.in1]=table.get(row.in2,'live')
                else:
                    row.live[row.in1]=0 
            
                table.set(row.out,{'live':'0','nextUse':None})
                table.set(row.in1,{'live':'1','nextUse':number})
            table.print_symboltable()
            number = number-1 
if __name__ == "__main__":
    t = ir.irTable('3ac.csv').arr
    NextUse(t)
    
