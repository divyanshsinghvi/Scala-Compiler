import sys
class SymbolTable:

    def __init__(self):
        self.SymbolTable = {
                "main" : {
                    "name" : "main",
                    "identifiers" : {},
                    "function" :{},
                    "variables" : {},
                    "type" : "main",
                    "parent" : None,
                    }
                }
        self.currScope = "main"
        self.tNo = -1
        self.scopeNo = -1
        self.function = {}
        self.stackbegin = []
        self.stackend = []
    
    def printSymbolTable(self,S,b):
        for i in self.SymbolTable:
            print i
            print self.SymbolTable[i]
        print "ds the awesomest of awesome"
        print "---------------------------"
            #for i in self.SymbolTable:
            #print i
    
    def newScope(self):
        scope = self.newScopeName()
        self.SymbolTable[scope] = {
                "name" : scope,
                "identifiers" : {},
                "function" : {},
                "variables" : {},
                "type" : "scope",
                "parent" : self.currScope,
                }
        self.currScope = scope

    def endScope(self):
        self.currScope = self.SymbolTable[self.currScope]["parent"]

    def addVar(self, idVal, place, idType, idSize = 4):
        scope = self.getScope(idVal)
        if scope != self.currScope:
            #sc = str(self.currScope)+"_"+place
            sc = place
            self.SymbolTable[self.currScope]["identifiers"][idVal] = {
                    "place" : sc,
                    "type" : idType,
                    "size" : idSize
                    }
        else:
            sys.exit("Variable "+idVal+" is already initialised in this scope")
        print(self.SymbolTable[self.currScope]["identifiers"])

    def searchEntry(self, idVal):
        scope = self.getScope(idVal)
        # print(scope)
        if(scope == None):
            return False
        else:
            return scope

    def addFunc(self, fun):
        self.SymbolTable[fun] = {
                "name" : fun,
                "type" : "function",
                "identifiers" : {},
                "variables" : {},
                "function" : {},
                "rType" : "undefined",
                "parent" : self.currScope,
                "arguments" : []
                }
        self.SymbolTable[self.currScope]["function"][fun] = {
                "fname" : fun
                }
        self.currScope = fun
    
    def endFunc(self):
        self.currScope = self.SymbolTable[self.currScope]["parent"]

    def getId(self,idVal):
        scope = self.getScope(idVal)
        if scope is not None:
            return self.SymbolTable[scope]["identifiers"][idVal]
        else:
            sys.exit("Symbol not defined")

    def setRType(self,dataType):
        self.SymbolTable[self.currScope]["rType"] = dataType
    
    def getRType(self, scope):
        return self.SymbolTable[scope]['rType']

    def getAttribute(self, idVal, Name):
        scope = self.getScope(idVal)
        if scope != None:
            return  self.SymbolTable[scope]["identifiers"][idVal].get(Name)
        else:
            return None

    def addAttribute(self, idVal, Name, Val):
        scope = self.getScope(idVal)
        if scope != None:
            self.SymbolTable[self.getScope(idVal)]["identifiers"][idVal][Name] = Val
            return True
            # print("Success")
        else:
            #print("Fail")
            return False

    def getScope(self, idVal):
        scope = self.currScope
        while self.SymbolTable[scope]["type"] not in ["main"]:
            if idVal in self.SymbolTable[scope]["identifiers"]:
                return scope
            scope = self.SymbolTable[scope]["parent"]

        if idVal in self.SymbolTable[scope]["identifiers"].keys():
            return scope
        return None

    def getTemp(self):
        self.tNo += 1
        newTemp = "t"+str(self.tNo) 
        return newTemp

    def newScopeName(self):
        self.scopeNo += 1
        newScope = "s"+str(self.scopeNo) 
        return newScope
