import ir

class RegistorAlloc:
    noOfReg = 6

    def x86InstrCode(instr,op1,op2):
        if instr == '':
   
    def getReg(i):
        return getRegIn(i,tacTable[i].in1), getRegIn(i,tacTable[i].in2), getRegOut(i,tacTable[i].out)

    def getRegIn(i,var): #getReg  8.6.3
        
        for regNo in range(noOfReg): # point 1 
            if registerDescr[regNo] == var:
                return regNo

        for regNo in range(noOfReg): # point 2
            if registerDescr[regNo] is None:
                return regNo

        for regNo in range(noOfReg): #point 3.1
            if otherReg(addressDescr[registerDescr[regNo]],regNo):
                return regNo

        for regNo in range(noOfReg):
            if otherLoc(addressDescr[registerDescr[regNo]]) and nextUseVar(addressDescr[registerDescr[regNo]]) is None:
                return regNo
        
        for regNo in range(noOfReg): #point 3.2
            if registerDescr[regNo] == tacTable[i].out and  registerDescr[regNo] != tacTable[i].in2 and registerDescr[regNo] != tacTable[i].in1:
                return regNo

        for regNo in range(noOfReg):#point 3.3
            if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2 and nextUseVar(registerDescr[regNo]) is None and liveVar(registerDescr[regNo]) is None:
                return regNo


        for regNo in range(noOfReg):#point 3.4
            if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2:
                print('\tmov '+address(registerDescr[regNo])+' '+regName(regNo))
                return regNo

    def getRegOut(i,var): #getReg  8.6.3
        
        for regNo in range(noOfReg): # point 1 
            if registerDescr[regNo] == var:
                return regNo

        for regNo in range(noOfReg):
            if registerDescr[regNo] == tacTable[i].in1 and nextUseVar(registerDescr[regNo]) is None and liveVar(registerDescr[regNo]) is None:
                return regNo


        for regNo in range(noOfReg): # point 2
            if registerDescr[regNo] is None:
                return regNo

        if nextUseVar(var) is None:
            return address(var)

        for regNo in range(noOfReg): #point 3.1
            if otherReg(addressDescr[registerDescr[regNo]],regNo):
                return regNo

        for regNo in range(noOfReg):
            if otherLoc(addressDescr[registerDescr[regNo]]) and nextUseVar(addressDescr[registerDescr[regNo]]) is None:
                return regNo
        

        for regNo in range(noOfReg):#point 3.3
            if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2 and registerDescr[regNo].nextUse is None and registerDescr[regNo].live is None:
                return regNo


        for regNo in range(noOfReg):#point 3.4
            if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2:
                print('\tmov '+address(registerDescr[regNo])+' '+regName(regNo))
                return regNo

