import ir
from globalvar import *

addressDescr = {}

class RegistorAlloc:
    noOfReg = 6

    def printCode(instr,op1,op2):
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
                print('\tmov '+address(registerDescr[regNo])+' '+regName(regNo)) ### make a spilling function here and above
                return regNo


    def generateCode(i):
		if tacTable[i].oper == '+' or tacTable[i].oper == '-':
			rx, ry, rz = getReg(i)

			if registerDescr[ry] != tacTable[i].in1:
				print('\tmov ' + regName(ry) + ', DWORD PTR' + tacTable[i].in1)
				addressDescr[tacTable[i].in1]['register'] = ry

			if registerDescr[rz] != tacTable[i].in2:
				print('\tmov ' + regName(rz) + ', DWORD PTR' + tacTable[i].in2)
				addressDescr[tacTable[i].in2]['register'] = rz
			
			print('\tmov ' + regName(rx) + ', ' + regName(ry))

			if tacTable[i].oper == '+':
				print('\tadd ' + regName(rx) + ', ' + regName(rz))
				registerDescr[rx] = tacTable[i].out
				registerDescr[ry] = tacTable[i].in1
				registerDescr[rz] = tacTable[i].in2
				addressDescr[tacTable[i].out]['register'] = rx
			elif tacTable[i].oper == '-':
				print('\tsub ' + regName(rx) + ', ' + regName(rz))
				registerDescr[rx] = tacTable[i].out
				registerDescr[ry] = tacTable[i].in1
				registerDescr[rz] = tacTable[i].in2
				addressDescr[tacTable[i].out]['register'] = rx
			elif tacTable[i].oper == '*':
				print('\timul ' + regName(rx) + ', ' + regName(rz))
				registerDescr[rx] = tacTable[i].out
				registerDescr[ry] = tacTable[i].in1
				registerDescr[rz] = tacTable[i].in2
				addressDescr[tacTable[i].out]['register'] = rx
			# Division takes divides the contents of the 64 bit integer EDX:EAX 
			#by the specified operand value. Syntax: idiv <reg32>
		elif tacTable[i].oper == ('='):
			rx, ry = getReg(i)

			if registerDescr[ry] != tacTable[i].in1:
				print('\tmov ' + regName(ry) + ', DWORD PTR' + tacTable[i].in1)
				addressDescr[tacTable[i].in1]['register'] = ry

			print('\tmov' + regName(rx) + ', ' + regName(ry))
				registerDescr[rx] = tacTable[i].out
				registerDescr[ry] = tacTable[i].in1
				addressDescr[tacTable[i].out]['register'] = rx

	def endBlock():
		for variable in addressDescr:
			if addressDescr[variable][memory] is None:
				print('\tmov DWORD PTR' + addressDescr[variable] + ', ' + regName(addressDescr[variable][register]))
