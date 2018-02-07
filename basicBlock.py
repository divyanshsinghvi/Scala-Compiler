import ir
import globalvar 

class basicBlock:
    leadList = set()
    def __init__(self):
        instrTable = globalvar.tacTable # ir.irTable(filename).arr
        self.leadList.add(0)
        #print type(instrTable)
        for index ,ic  in enumerate(instrTable):
            if ic.oper == 'label':
                self.leadList.add(index)
            elif (ic.oper == 'call' or ic.oper == 'fcall' or ic.oper == 'if' or ic.oper == 'goto' or ic.oper == 'return' or ic.oper == 'freturn') and index != len(instrTable) - 1:
                self.leadList.add(index+1)
        self.leadList= list(self.leadList)
        self.leadList.sort()

if __name__ == '__main__': 
    b = basicBlock()
    print [ d for d in b.leadList]

