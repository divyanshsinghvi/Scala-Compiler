import ir
from globalvar import *

addressDescr = {}

class RegistorAlloc:
    noOfReg = 6

    def printCode(instr,op1,op2):
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
