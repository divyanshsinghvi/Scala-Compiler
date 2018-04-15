#!/usr/bin/env python
import ir
from globalvar import *
from globalData import *

#addressDescr = {}

noOfReg = 6
registerName = ["%eax", "%ebx", "%ecx","%edx","%esi", "%edi"]
registerDescr=[None]*6

def is_number(var):
    try:
        int(var)
        return True
    except Exception:
        return False 

def isAssigned(var):
    for i in range(noOfReg):
         if(registerDescr[i] == var):
             return i
    return -1

def spillAll():
    for i in range(noOfReg):
        if(registerDescr[i]!=None):
            print('\tmovl '+regName[i]+", "+registerDescr[i])
    for i in range(noOfReg):
        registerDescr[i] = None
    for r in addressDescr:
        addressDescr[r]['Register'] = None
        addressDescr[r]['Memory'] = None

def regName(regNo):
    return registerName[regNo] 

def address(var):
    return var


def getReg(i,var):
    for regNo in range(noOfReg):
        if registerDescr[regNo]==var:
            return regNo

    for regNo in range(noOfReg):
        if registerDescr[regNo] == None:
            registerDescr[regNo] = var
            if var[0] != '#':
                print('\tmovl '+var+", "+regName(regNo))
            return regName(regNo)

    for j,other in enumerate(registerDescr):
        if other in tacTable[i].nextUse and other != tacTable[i].in1 and other != tacTable[i].in2 and other != tacTable[i].out:
            print('\tmovl '+ regName(j)+", "+other) #address
            registerDescr[j]=other
            print('\tmovl '+ var+", "+regName(j)) #address
            return regName(j)

    tempVar = registerDescr[0]
    tempVarNextUse = tacTable[i].nextUse[tempVar]
    for j in range(1,noOfReg):
        other = registerDescr[j]
        if  other == tacTable[i].in1 or other == tacTable[i].in2 or other == tacTable[i].out:
            continue
        if tempVarNextUse < tacTable[i].nextUse[registerDescr[j]]:
            tempVar = registerDescr[j]
            tempVarNextUse = tacTable[i].nextUse[registerDescr[j]]
        print('\tmovl '+regName(j)+", "+tempvar) #address
        registerDescr[j] = var
        print('\tmovl '+var +", "+regName(j)) #address
        return regName(j)

