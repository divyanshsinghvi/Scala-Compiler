import ir
from globalvar import *

#addressDescr = {}

noOfReg = 6
registerName = ["eax", "ebx", "ecx","edx","esi", "edi"]
registerDescr=[None]*6

#class RegisterAlloc:

    #def printCode(instr,op1,op2):
    #    if instr == ''
    
def regName(regNo):
    return registerName[regNo] 

def address(var):
    return var

#def otherReg(noOf)
        
#def getReg(i):
    #return 1,2,3
#    outReg = getRegOut(i,tacTable[i].out)
#    in1Reg = getRegIn(i,tacTable[i].in1)
#    in2Reg = 
#    return , getRegIn(i,tacTable[i].in1), getRegIn(i,tacTable[i].in2)
def getRegIn(i,var): #getReg  8.6.3
    
    for regNo in range(noOfReg): # point 1 
        if registerDescr[regNo] == var:
            print(1,var,regNo)
            return regNo

    for regNo in range(noOfReg): # point 2
        if registerDescr[regNo] is None:
            print(2,var,regNo)
            return regNo

#    for regNo in range(noOfReg): #point 3.1
#        if otherReg(addressDescr[registerDescr[regNo]],regNo):
#            print(3,var,regNo)
#            return regNo

#    for regNo in range(noOfReg):
#        if otherLoc(addressDescr[registerDescr[regNo]]) and nextUseVar(addressDescr[registerDescr[regNo]]) is None:
#            print(4,var,regNo)
#            return regNo
    
    for regNo in range(noOfReg): #point 3.2
        if registerDescr[regNo] == tacTable[i].out and  registerDescr[regNo] != tacTable[i].in2 and registerDescr[regNo] != tacTable[i].in1:
            print(5,var,regNo)
            return regNo

#    for regNo in range(noOfReg):#point 3.3
#        if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2 and nextUseVar(registerDescr[regNo]) is None and liveVar(registerDescr[regNo]) is None:
#            print(6,var,regNo)
#            return regNo


    for regNo in range(noOfReg):#point 3.4
        if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2:
            print(7,var,regNo)
            print('\tmov '+address(registerDescr[regNo])+', '+regName(regNo))
            addressDescr[registerDescr[regNo]]['Memory'] = registerDescr[regNo]
            return regNo

def getRegOut(i,var): #getReg  8.6.3
    
    for regNo in range(noOfReg): # point 1 
        if registerDescr[regNo] == var:
            print(1,var,regNo)
            return regNo

    for regNo in range(noOfReg):
        if registerDescr[regNo] == tacTable[i].in1 and tacTable[i].nextUse[registerDescr[regNo]] is None and tacTable[i].live[registerDescr[regNo]] is None:
            print(2,var,regNo)
            return regNo


    for regNo in range(noOfReg): # point 2
        if registerDescr[regNo] is None:
            print(3,var,regNo)
            return regNo

#    if tacTable[i].nextUse[var] is None:
#        print(4,var,regNo)
#        return address(var)

#    for regNo in range(noOfReg): #point 3.1
#        if otherReg(addressDescr[registerDescr[regNo]],regNo):
#            print(5,var,regNo)
#            return regNo


#### for the time being this optimisation is removed. We can do it later if  time permits
#    for regNo in range(noOfReg):
#        if otherLoc(addressDescr[registerDescr[regNo]]) and nextUseVar(addressDescr[registerDescr[regNo]]) is None:
#            print(6,var,regNo)
#            return regNo
    
#    for regNo in range(noOfReg):#point 3.3
#        if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2 and registerDescr[regNo].nextUse is None and registerDescr[regNo].live is None:
#            print(7,var,regNo)
#            return regNo


    for regNo in range(noOfReg):#point 3.4
        if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2:
            print(8,var,regNo)
            print('\tmov DWORD PTR '+address(registerDescr[regNo])+', '+regName(regNo)) ### make a spilling function here and above
            addressDescr[registerDescr[regNo]]['Memory'] = registerDescr[regNo]
            return regNo


def generateCode(i):
            if tacTable[i].oper == '+' or tacTable[i].oper == '-':
                    #rx, ry, rz = getReg(i)

                    ry = getRegIn(i,tacTable[i].in1)
                    if registerDescr[ry] != tacTable[i].in1:
                            print('\tmov ' + regName(ry) + ', DWORD PTR ' + tacTable[i].in1)
                            addressDescr[tacTable[i].in1]['Register'] = ry
                            registerDescr[ry] = tacTable[i].in1

                    rz = getRegIn(i,tacTable[i].in2)
                    if registerDescr[rz] != tacTable[i].in2:
                            print('\tmov ' + regName(rz) + ', DWORD PTR ' + tacTable[i].in2)
                            addressDescr[tacTable[i].in2]['Register'] = rz
                            registerDescr[rz] = tacTable[i].in2
                    
                    rx = getRegOut(i,tacTable[i].out)
                    registerDescr[rx] = tacTable[i].out
                    print('\tmov ' + regName(rx) + ', ' + regName(ry))

                    if tacTable[i].oper == '+':
                            print('\tadd ' + regName(rx) + ', ' + regName(rz))
                            addressDescr[tacTable[i].out]['Register'] = rx
                            addressDescr[tacTable[i].out]['Memory'] = None
                    elif tacTable[i].oper == '-':
                            print('\tsub ' + regName(rx) + ', ' + regName(rz))
                            addressDescr[tacTable[i].out]['Register'] = rx
                            addressDescr[tacTable[i].out]['Memory'] = None
                    elif tacTable[i].oper == '*':
                            print('\timul ' + regName(rx) + ', ' + regName(rz))
                            addressDescr[tacTable[i].out]['Register'] = rx
                            addressDescr[tacTable[i].out]['Memory'] = None
                    # Division takes divides the contents of the 64 bit integer EDX:EAX 
                    #by the specified operand value. Syntax: idiv <reg32>
'''            elif tacTable[i].oper == ('='):
                    rx, ry = getReg(i)

                    if registerDescr[ry] != tacTable[i].in1:
                            print('\tmov ' + regName(ry) + ', DWORD PTR' + tacTable[i].in1)
                            addressDescr[tacTable[i].in1]['register'] = ry

                    print('\tmov' + regName(rx) + ', ' + regName(ry))
                    registerDescr[rx] = tacTable[i].out
                    registerDescr[ry] = tacTable[i].in1
                    addressDescr[tacTable[i].out]['register'] = rx
'''                    
def endBlock():
            print "t"
            for variable in addressDescr:
                    if addressDescr[variable]['Memory'] is None:    
                        print('\tmov DWORD PTR ' + variable + ', ' + regName(addressDescr[variable]['Register']))


if __name__ == '__main__':
    #d = RegisterAlloc()
    l = basicBlock
    length = len(tacTable)
    l.append(length)
    for i in range(1,len(l)-1):
        for j in range(len(tacTable[l[i-1]:l[i]])):
            generateCode(j+l[i-1])
        endBlock()
