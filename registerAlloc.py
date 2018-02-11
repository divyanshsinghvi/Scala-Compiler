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

def printInstr(op,x,xDest,y=None,yDest=None,i=-1):
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
        elif xDest == 'Constant' and yDest == 'Register':
            print('\tmovl %'+y + ', $' + x)
    elif op == 'cmpl':
        if xDest == 'Register' and yDest == 'Register':
            print('\tcmpl %'+x + ', %' + y)
        elif xDest == 'Register' and yDest == 'Memory':
            print('\tcmpl %'+x + ', ' + y)
        elif xDest == 'Memory' and yDest == 'Register':
            print('\tcmpl '+x + ', %' + y)
    elif op == 'cmp':
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
    elif op == 'idivl':
        if xDest == 'Register':
            print('\tidivl %' + x)
    elif op == 'xorl':
        if xDest == 'Register' and yDest=='Register':
            print('\txorl %'+y+', %'+x)


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
        addressDescr[tacTable[i].out]['Memory'] = None
    elif tacTable[i].oper == '/' or tacTable[i].oper == '%':
        if registerDescr[0] != None:
            printInstr('movl', address(registerDescr[0]), 'Memory', regName(0), 'Register')
            #print('\tmov  DWORD PTR ' + registerDescr[0] + ', ' + regName(0))
            addressDescr[registerDescr[0]]['Register'] = None
            addressDescr[registerDescr[0]]['Memory'] = registerDescr[0]

        if registerDescr[3] != None:
            printInstr('movl', address(registerDescr[3]), 'Memory', regName(3), 'Register')
            #print('\tmov  DWORD PTR ' + registerDescr[3] + ', ' + regName(3))
            addressDescr[registerDescr[3]]['Register'] = None
            addressDescr[registerDescr[3]]['Memory'] = registerDescr[3]


        printInstr('movl',regName(0), 'Register', address(tacTable[i].in1), 'Memory')
        registerDescr[0] = tacTable[i].in1
        addressDescr[tacTable[i].in1]['Register'] = 0
            
        print('\tcltd')
        registerDescr[3] = tacTable[i].in1
        
        rz = getRegIn(i, tacTable[i].in2) 
        if registerDescr[rz] != tacTable[i].in2:
            printInstr('movl',regName(rz),'Register',address(tacTable[i].in2),'Memory')
            addressDescr[tacTable[i].in2]['Register'] = rz
            registerDescr[rz] = tacTable[i].in2
       
        #print('\tidivl %' + regName(rz))
        printInstr('idivl',regName(rz),'Register')
        rx = getRegOut(i, tacTable[i].out)
        if tacTable[i].oper == '/':
            # move eax to rx
            printInstr('movl', regName(rx), 'Register', 'eax', 'Register') 
            registerDescr[rx] = registerDescr[0]
        elif tacTable[i].oper =='%':
            # move edx to rx
            printInstr('movl', regName(rx), 'Register', 'edx', 'Register') 
            registerDescr[rx] = registerDescr[0]
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
        
        printInstr('cmpl',regName(rz),'Register',regName(ry),'Register')
        
        rx = getRegOut(i,tacTable[i].out)
        #if b = a<b is an independent statement and not followed by if?
        printInstr('movl', address(registerDescr[0]), 'Memory', regName(0), 'Register')
        addressDescr[registerDescr[0]]['Register'] = None
        addressDescr[registerDescr[0]]['Memory'] = registerDescr[0]
        registerDescr[0] = None

        printInstr('cmp', regName(rx), 'Register', i)
        print('\tmovzbl %al, %' + regName(rx))
        registerDescr[rx] = tacTable[i].out
        addressDescr[tacTable[i].out]['Register'] = rx
        addressDescr[tacTable[i].out]['Memory'] = None
        
    elif tacTable[i].oper == 'if':
        ry = getRegIn(i, tacTable[i].in1)
        if registerDescr[ry] != tacTable[i].in1:
            printInstr('movl',regName(ry),'Register',address(tacTable[i].in1),'Memory')
            addressDescr[tacTable[i].in1]['Register'] = ry
            registerDescr[ry] = tacTable[i].in1
        endBlock()
        print('\ttestl %' + regName(ry) + ', %' + regName(ry))
        print('\tjne .' + tacTable[i].out)

    elif tacTable[i].oper == 'goto':
        endBlock()
        print('\tjmp .' + tacTable[i].out)

    elif tacTable[i].oper == 'label':
        endBlock()
        print('.' + tacTable[i].out + ':')
    
    elif tacTable[i].oper == 'ldar':
        rx = getRegOut(i,tacTable[i].out)
        if registerDescr[rx] != tacTable[i].out:
            printInstr('movl',regName(rx),'Register',address(tacTable[i].out),'Memory')
            addressDescr[tacTable[i].out]['Register'] = rx
            registerDescr[rx] = tacTable[i].out
        ri = getRegOut(i,tacTable[i].in2)
        if registerDescr[ri] != tacTable[i].in2:
            printInstr('movl',regName(ri),'Register',address(tacTable[i].in2),'Memory')
            addressDescr[tacTable[i].in2]['Register'] = ri
            registerDescr[ri] = tacTable[i].in2
 
 
        printInstr('movl',regName(rx),'Register',address(tacTable[i].in1)+"(,%"+regName(ri)+",4)",'Memory')
#        printInstr('movl',regName(rx),'Register',address(tacTable[i].in1) + " + " + str(int(tacTable[i].in2)*4),'Memory')
    elif tacTable[i].oper == 'star':
        ry = getRegIn(i,tacTable[i].in2)
        if registerDescr[ry] !=tacTable[i].in2:
            printInstr('movl',regName(ry),'Register',address(tacTable[i].in2),'Memory')
            addressDescr[tacTable[i].in2]['Register'] = ry
            registerDescr[ry] = tacTable[i].in2
        ri = getRegIn(i,tacTable[i].in1)
        if registerDescr[ri] !=tacTable[i].in1:
            printInstr('movl',regName(ri),'Register',address(tacTable[i].in1),'Memory')
            addressDescr[tacTable[i].in1]['Register'] = ri
            registerDescr[ri] = tacTable[i].in1

        printInstr('movl',address(tacTable[i].out)+ "(,%"+regName(ri)+",4)",'Memory',regName(ry),'Register')
        #printInstr('movl',address(tacTable[i].out)+ " + " + str(int(tacTable[i].in1)*4),'Memory',regName(ry),'Register')
    elif tacTable[i].oper == 'printInt':
        if registerDescr[5] != None:
            printInstr('movl', address(registerDescr[5]), 'Memory', regName(5), 'Register')
            #print('\tmov  DWORD PTR ' + registerDescr[0] + ', ' + regName(0))
            addressDescr[registerDescr[5]]['Register'] = None
            addressDescr[registerDescr[5]]['Memory'] = registerDescr[5]
        if registerDescr[4] != None:
            printInstr('movl', address(registerDescr[4]), 'Memory', regName(4), 'Register')
            #print('\tmov  DWORD PTR ' + registerDescr[0] + ', ' + regName(0))
            addressDescr[registerDescr[4]]['Register'] = None
            addressDescr[registerDescr[4]]['Memory'] = registerDescr[4]
        if registerDescr[0] != None:
            printInstr('movl', address(registerDescr[0]), 'Memory', regName(0), 'Register')
            #print('\tmov  DWORD PTR ' + registerDescr[0] + ', ' + regName(0))
            addressDescr[registerDescr[0]]['Register'] = None
            addressDescr[registerDescr[0]]['Memory'] = registerDescr[0]
        printInstr('xorl',regName(0),'Register',regName(0),'Register')
        printInstr('movl',regName(4),'Register','5','Constant')
        printInstr('movl',regName(5),'Register','$.format','Memory')
        print('\tcall printf')

    elif tacTable[i].oper in ['call', 'fcall']:
        endBlock();
        print('\tcall ' + tacTable[i].in1)
        if tacTable[i].oper == 'fcall':
            printInstr('movl', tacTable[i].out, 'Memory', regName(0), 'Register')
            registerDescr[0] = None;
            addressDescr[tacTable[i].out]['Memory'] = tacTable[i].out
            addressDescr[tacTable[i].out]['Register'] = None

    elif tacTable[i].oper in ['return', 'freturn']:
        endBlock();
        if tacTable[i].oper == 'freturn':
            prtinInstr('movl', regName(0), 'Register', tacTable[i].in1, 'Memory')
            addressDescr[tacTable[i].in1]['Register'] = 0
        print('\tret')

def endBlock():
#    print "t"
    for variable in addressDescr:
        if addressDescr[variable]['Memory'] is None and addressDescr[variable]['Register'] is not None:    
            printInstr('movl',address(variable),'Memory',regName(addressDescr[variable]['Register']),'Register')
            #print('\tmov DWORD PTR ' + variable + ', ' + regName(addressDescr[variable]['Register']))
    for r in registerDescr:
        r = None
    for r in addressDescr:
        addressDescr[r]['Register'] = None


if __name__ == '__main__':
    #d = RegisterAlloc()
    l = basicBlock
    length = len(tacTable)
    l.append(length)
    for op in tacTable:
        if op.oper == 'printInt':
            print('\t.extern printf')
            break;

    globalData()
    print('\t.text')
    print('\t.globl main')
    print("main:")
    for i in range(1,len(l)-1):
        for j in range(len(tacTable[l[i-1]:l[i]])):
            generateCode(j+l[i-1])
#        endBlock()
