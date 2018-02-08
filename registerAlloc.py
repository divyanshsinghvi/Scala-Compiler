import ir
from globalvar import *
from globalData import *

#addressDescr = {}

noOfReg = 6
registerName = ["eax", "ebx", "ecx","edx","esi", "edi"]
registerDescr=[None]*6

#class RegisterAlloc:

    #def printCode(instr,op1,op2):
    #    if instr == ''
def is_number(var):
    try:
        int(var)
        return True
    except Exception:
        return False 

def regName(regNo):
    return registerName[regNo] 

def address(var):
    return var

def printInstr(op,x,xDest,y=None,yDest=None):
    if op == 'addl':
        if xDest == 'Register' and yDest == 'Register':
            print('\taddl %'+ y + ', %' + x)
    elif op == 'subl':
        if xDest == 'Register' and yDest == 'Register':
            print('\tsubl %'+ y + ', %' + x)
    elif op == 'imull':
        if xDest == 'Register' and yDest == 'Register':
            print('\timull %'+ y + ', %' + x)
    elif op == 'movl':
        if xDest == 'Register' and yDest == 'Register':
            print('\tmovl %'+y + ', %' + x)
        elif xDest == 'Memory' and yDest == 'Register':
            print('\tmovl %'+y + ', ' + x)
        elif xDest == 'Register' and yDest == 'Memory':
            print('\tmovl '+y + ', %' + x)
        elif xDest == 'Register' and yDest == 'Constant':
            print('\tmovl $'+y + ', %' + x)
    elif op == 'cmp':
        if xDest == 'Register' and yDest == 'Register':
            print('\tcmpl %'+x + ', %' + y)
        elif xDest == 'Register' and yDest == 'Memory':
            print('\tcmpl %'+x + ', ' + y)
        elif xDest == 'Memory' and yDest == 'Register':
            print('\tcmpl '+x + ', %' + y)
 



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
            #print(1,var,regNo)
            return regNo

    for regNo in range(noOfReg): # point 2
        if registerDescr[regNo] is None:
            #print(2,var,regNo)
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
            #print(5,var,regNo)
            return regNo

#    for regNo in range(noOfReg):#point 3.3
#        if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2 and nextUseVar(registerDescr[regNo]) is None and liveVar(registerDescr[regNo]) is None:
#            print(6,var,regNo)
#            return regNo


    for regNo in range(noOfReg):#point 3.4
        if registerDescr[regNo]!= tacTable[i].in1 and registerDescr[regNo]!= tacTable[i].in2:
            #print(7,var,regNo)
            printInstr('movl',address(registerDescr[regNo]),'Address',regName(regNo),'Register')
            #print('\tmov DWORD PTR '+address(registerDescr[regNo])+', '+regName(regNo))
            addressDescr[registerDescr[regNo]]['Memory'] = registerDescr[regNo]
            return regNo

def getRegOut(i,var): #getReg  8.6.3
    
    for regNo in range(noOfReg): # point 1 
        if registerDescr[regNo] == var:
            #print(1,var,regNo)
            return regNo

    for regNo in range(noOfReg):
        if registerDescr[regNo] == tacTable[i].in1 and tacTable[i].nextUse[registerDescr[regNo]] is None and tacTable[i].live[registerDescr[regNo]] is None:
            #print(2,var,regNo)
            return regNo


    for regNo in range(noOfReg): # point 2
        if registerDescr[regNo] is None:
            #print(3,var,regNo)
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
            #print(8,var,regNo)
            printInstr('movl',address(registerDescr[regNo]),'Address',regName(regNo),'Register')
            #print('\tmov DWORD PTR '+address(registerDescr[regNo])+', '+regName(regNo)) ### make a spilling function here and above
            addressDescr[registerDescr[regNo]]['Memory'] = registerDescr[regNo]
            return regNo


def generateCode(i):
                   # Division takes divides the contents of the 64 bit integer EDX:EAX 
                    #by the specified operand value. Syntax: idiv <reg32>
 
#    elif tacTable[i].oper == ('='):
#                    rx, ry = getReg(i)
#                    ry = getRegIn(i,tacTable[i].in1)
#                    if registerDescr[ry] != tacTable[i].in1:
#                            printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
#                            #print('\tmov ' + regName(ry) + ', DWORD PTR ' + tacTable[i].in1)
#                            addressDescr[tacTable[i].in1]['Register'] = ry
#                            registerDescr[ry] = tacTable[i].in1
#
#                    rx = getRegOut(i,tacTable[i].out)
#                    printInstr('movl',regName(rx),'Register',regName(ry),'Register')
#                    #print('\tmov ' + regName(rx) + ', ' + regName(ry))
#                    registerDescr[rx] = tacTable[i].out
#                    addressDescr[tacTable[i].out]['Register'] = rx
#    if tacTable[i].oper in ['+', '-', '*']:
#        #rx, ry, rz = getReg(i)
#
#        ry = getRegIn(i,tacTable[i].in1)
#        if registerDescr[ry] != tacTable[i].in1:
#            printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
#            #print('\tmov ' + regName(ry) + ', DWORD PTR ' + tacTable[i].in1)
#            addressDescr[tacTable[i].in1]['Register'] = ry
#            registerDescr[ry] = tacTable[i].in1
#
#        rz = getRegIn(i,tacTable[i].in2)
#        if registerDescr[rz] != tacTable[i].in2:
#            printInstr('movl',regName(rz),'Register',address(tacTable[i].in2),'Memory')
#            #print('\tmov ' + regName(rz) + ', DWORD PTR ' + tacTable[i].in2)
#            addressDescr[tacTable[i].in2]['Register'] = rz
#            registerDescr[rz] = tacTable[i].in2
#        
#        rx = getRegOut(i,tacTable[i].out)
#        registerDescr[rx] = tacTable[i].out
#        printInstr('movl',regName(rx),'Register',regName(ry),'Register')
#        #print('\tmov ' + regName(rx) + ', ' + regName(ry))
#
#        if tacTable[i].oper == '+':
#            printInstr('addl',regName(rx),'Register',regName(rz),'Register')
#            #print('\tadd ' + regName(rx) + ', ' + regName(rz))
#            addressDescr[tacTable[i].out]['Register'] = rx
#            addressDescr[tacTable[i].out]['Memory'] = None
#        elif tacTable[i].oper == '-':
#            printInstr('subl',regName(rx),'Register',regName(rz),'Register')
#            #print('\tsub ' + regName(rx) + ', ' + regName(rz))
#            addressDescr[tacTable[i].out]['Register'] = rx
#            addressDescr[tacTable[i].out]['Memory'] = None
#        elif tacTable[i].oper == '*':
#            printInstr('imul',regName(rx),'Register',regName(rz),'Register')
#            #print('\timul ' + regName(rx) + ', ' + regName(rz))
#            addressDescr[tacTable[i].out]['Register'] = rx
#            addressDescr[tacTable[i].out]['Memory'] = None
#        # Division takes divides the contents of the 64 bit integer EDX:EAX 
#        #by the specified operand value. Syntax: idiv <reg32>
    if tacTable[i].oper == '+' or tacTable[i].oper == '-' or tacTable[i].oper == '*': 
        ry = getRegIn(i,tacTable[i].in1)
        if registerDescr[ry] != tacTable[i].in1:
            printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
            #print('\tmov ' + regName(ry) + ', DWORD PTR ' + tacTable[i].in1)
            addressDescr[tacTable[i].in1]['Register'] = ry
            registerDescr[ry] = tacTable[i].in1

        rz = getRegIn(i,tacTable[i].in2)
        if registerDescr[rz] != tacTable[i].in2:
            printInstr('movl',regName(rz),'Register',address(tacTable[i].in2),'Memory')
            #print('\tmov ' + regName(rz) + ', DWORD PTR ' + tacTable[i].in2)
            addressDescr[tacTable[i].in2]['Register'] = rz
            registerDescr[rz] = tacTable[i].in2
        
        rx = getRegOut(i,tacTable[i].out)
        registerDescr[rx] = tacTable[i].out
        printInstr('movl',regName(rx),'Register',regName(ry),'Register')
        #print('\tmov ' + regName(rx) + ', ' + regName(ry))

        if tacTable[i].oper == '+':
            printInstr('addl',regName(rx),'Register',regName(rz),'Register')
            #print('\tadd ' + regName(rx) + ', ' + regName(rz))
            addressDescr[tacTable[i].out]['Register'] = rx
            addressDescr[tacTable[i].out]['Memory'] = None
        elif tacTable[i].oper == '-':
            printInstr('subl',regName(rx),'Register',regName(rz),'Register')
                #print('\tsub ' + regName(rx) + ', ' + regName(rz))
            addressDescr[tacTable[i].out]['Register'] = rx
            addressDescr[tacTable[i].out]['Memory'] = None
        elif tacTable[i].oper == '*':
            printInstr('imull',regName(rx),'Register',regName(rz),'Register')
            #print('\timul ' + regName(rx) + ', ' + regName(rz))
            addressDescr[tacTable[i].out]['Register'] = rx
            addressDescr[tacTable[i].out]['Memory'] = None
    elif tacTable[i].oper == '=':
        #rx, ry = getReg(i)
	if not is_number(tacTable[i].in1):
            ry = getRegIn(i,tacTable[i].in1)
            if registerDescr[ry] != tacTable[i].in1:
                printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
                #print('\tmov ' + regName(ry) + ', DWORD PTR ' + tacTable[i].in1)
                addressDescr[tacTable[i].in1]['Register'] = ry
                registerDescr[ry] = tacTable[i].in1
            rx = getRegOut(i,tacTable[i].out)
            printInstr('movl',regName(rx),'Register',regName(ry),'Register')
        else:
            rx = getRegOut(i,tacTable[i].out)
            const = tacTable[i].in1
            printInstr('movl',regName(rx),'Register',const,'Constant')

        #print('\tmov ' + regName(rx) + ', ' + regName(ry))
        registerDescr[rx] = tacTable[i].out
        addressDescr[tacTable[i].out]['Register'] = rx
    elif tacTable[i].oper == '/' or tacTable[i].oper == '%':
        if registerDescr[0] != None:
            print('\tmov  DWORD PTR ' + registerDescr[0] + ', ' + regName(0))
            addressDescr[registerDescr[0]]['Register'] = None
            addressDescr[registerDescr[0]]['Memory'] = registerDescr[0]

        if registerDescr[3] != None:
            print('\tmov  DWORD PTR ' + registerDescr[0] + ', ' + regName(0))
            addressDescr[registerDescr[3]]['Register'] = None
            addressDescr[registerDescr[3]]['Memory'] = registerDescr[3]

        print('\tmov ' + regName(3) + ', 0')
        registerDescr[3] = tacTable[i].in1
        print('\tmov ' + regName(0) + ', ' + tacTable[i].in1)
        registerDescr[0] = tacTable[i].in1
        addressDescr[tacTable[i].in1]['Register'] = 0

        rz = getRegIn(i, tacTable[i].in2) 
        if registerDescr[rz] != tacTable[i].in2:
            print('\tmov ' + regName(rz) + ', DWORD PTR ' + tacTable[i].in2)
            addressDescr[tacTable[i].in2]['Register'] = rz
            registerDescr[rz] = tacTable[i].in2
       
        print('\tidiv ' + regName(rz))
        rx = getRegOut(i, tacTable[i].out)
        if tacTable[i].oper == '/':
            # move eax to rx
            registerDescr[rx] = registerDescr[0]
        elif tacTable[i].oper =='%':
            # move edx to rx
            registerDescr[rx] = registerDescr[3]
        addressDescr[tacTable[i].out]['Register'] = rx
        registerDescr[0], registerDescr[3] = None, None
    
    elif tacTable[i].oper in ['<', '<=', '==', '>=', '>', '!=']:
        ry = getRegIn(i,tacTable[i].in1)
        if registerDescr[ry] != tacTable[i].in1:
            printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
            addressDescr[tacTable[i].in1]['Register'] = ry
            registerDescr[ry] = tacTable[i].in1

        rz = getRegIn(i,tacTable[i].in2)
        if registerDescr[rz] != tacTable[i].in2:
            printInstr('movl',regName(rz),'Register',address(tacTable[i].in2),'Memory')
            addressDescr[tacTable[i].in2]['Register'] = rz
            registerDescr[rz] = tacTable[i].in2
        
        printInstr('cmpl',regName(ry),'Register',regName(rz),'Register')
        
        rx = getRegOut(i,tacTable[i].out)
        #if b = a<b is an independent statement and not followed by if?
        if tacTable[i].oper == '<':
            print('\tsetl %al')
        elif tacTable[i].oper == '<=':
            print('\tsetle %al')
        elif tacTable[i].oper == '==':
            print('\tsete %al')
        elif tacTable[i].oper == '>=':
            print('\tsetge %al')
        elif tacTable[i].oper == '>':
            print('\tsetg %al')
        elif tacTable[i].oper == '!=':
            print('\tsetne %al')
        print('\tmovzbl %al, %' + regName(rx))
        registerDescr[rx] = tacTable[i].out
        addressDescr[tacTable[i].out]['Register'] = rx
        addressDescr[tacTable[i].out]['Mempry'] = None
        
    elif tacTable[i].oper == 'if':
        ry = getRegIn(i, tacTable[i].in1)
        if registerDescr[ry] != tacTable[i].in1:
            printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
            addressDescr[tacTable[i].in1]['Register'] = ry
            registerDescr[ry] = tacTable[i].in1
        
        print('\ttestl %' + regName(ry) + ', %' + regName(ry))
        print('\tjne .' + tacTable[i].out)

def endBlock():
    #print "t"
    for variable in addressDescr:
        if addressDescr[variable]['Memory'] is None:    
            printInstr('movl',address(variable),'Memory',regName(addressDescr[variable]['Register']),'Register')
            #print('\tmov DWORD PTR ' + variable + ', ' + regName(addressDescr[variable]['Register']))


if __name__ == '__main__':
    #d = RegisterAlloc()
    l = basicBlock
    length = len(tacTable)
    l.append(length)
    globalData()
    print('\t.text')
    print('\t.globl main')
    print("main:")
    for i in range(1,len(l)-1):
        for j in range(len(tacTable[l[i-1]:l[i]])):
            generateCode(j+l[i-1])
        endBlock()
