import ir

class RegistorAlloc:
    noOfReg = 6

    def x86InstrCode(instr,op1,op2):
        if instr == '':
    
    def getReg(i,var): #getReg takes the function 
        
        for regNo in range(noOfReg):
            if registerDescr[regNo] == var:
                return regNo

        for regNo in range(noOfReg):
            if registerDescr[regNo] is None:
                print('mov '+regName(regNo)+' '+var)
                return regNo

        
        for regNo in range(noOfReg):
            if registerDescr[regNo] != tacTable[i].in1 and registerDescr[regNo] != tacTable[i].in2 and registerDescr[regNo] != tacTable[i].out:
                
        

