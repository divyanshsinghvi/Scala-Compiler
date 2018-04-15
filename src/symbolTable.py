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
                    "offset" : 0,
                    "temp"  : 0,
                    "tempmax" : 0,
                    "varwidth" : 0
                    }
                }
        self.currScope = "main"
        self.tNo = -1
        self.scopeNo = -1
        self.function = []
        self.stackbegin = []
        self.stackend = []
    
    def printSymbolTable(self,S=None,b=None):
        for i in self.SymbolTable:
            print i
            print self.SymbolTable[i]
    
    def newScope(self):
        scope = self.newScopeName()
        self.SymbolTable[scope] = {
                "name" : scope,
                "identifiers" : {},
                "function" : {},
                "variables" : {},
                "type" : "scope",
                "parent" : self.currScope,
                "offset" : self.SymbolTable[self.currScope]['offset'],
                "temp" : 0,
                "tempmax" : 0,
                "varwidth" : 0
                }
        self.currScope = scope
        print "startscope,"+scope

    def endScope(self):
        parent = self.SymbolTable[self.currScope]["parent"]
        self.SymbolTable[parent]["tempmax"]=max(self.SymbolTable[self.currScope]["tempmax"],self.SymbolTable[self.currScope]["temp"])
        #self.SymbolTable[self.currScope]["tempmax"]=0
        self.currScope = self.SymbolTable[self.currScope]["parent"]
        print "scope,"+self.currScope

    def addVar(self, idVal, place, idType, idSize = 4,typeArray=None):
        scope = self.getScope(idVal)
        if scope != self.currScope:
            #sc = str(self.currScope)+"_"+place
            sc = place
            self.SymbolTable[self.currScope]["identifiers"][idVal] = {
                    "place" : sc,
                    "type" : idType,
                    "size" : idSize,
                    }
            if idType == 'Array':
                self.SymbolTable[self.currScope]["identifiers"][idVal]['typeArray']=typeArray
                size = self.getSize(idVal)
                s = self.getWidth(typeArray)
                self.SymbolTable[self.currScope]["offset"] += size*s
                self.SymbolTable[self.currScope]["varwidth"]+= size*s
                self.SymbolTable[self.currScope]["identifiers"][idVal]['offset'] = self.SymbolTable[self.currScope]["offset"]
            else:
                self.SymbolTable[self.currScope]["offset"] += idSize
                self.SymbolTable[self.currScope]["identifiers"][idVal]['offset'] = self.SymbolTable[self.currScope]["offset"]
        else:
            sys.exit("Variable "+idVal+" is already initialised in this scope")
        #print(self.SymbolTable[self.currScope]["identifiers"])
    
    def getWidth(self,idType):
        if idType == "INT":
            return 4
        elif idType == "FLOAT":
            return 8
        elif idType == "CHAR":
            return 1
        elif idType == "BOOL":
            return 1

    def getSize(self,idVal):
        scope = self.getScope(idVal)
        while self.SymbolTable[scope]['type'] not in ['main']:
            if idVal in self.SymbolTable[scope]["identifiers"].keys():
                if self.SymbolTable[scope]["identifiers"][idVal]['type'] == 'Array':
                    import numpy
                    return numpy.prod(self.SymbolTable[scope]["identifiers"][idVal]['size'])
                else:
                    return self.SymbolTable[scope]["identifiers"][idval]['size']

    def searchEntry(self, idVal):
        scope = self.getScope(idVal)
        # print(scope)
        if(scope == None):
            return False
        else:
            return scope

    def addFunc(self, fun, args=None):
        self.SymbolTable[fun] = {
                "name" : fun,
                "type" : "function",
                "identifiers" : {},
                "variables" : {},
                "function" : {},
                "rType" : "undefined",
                "parent" : self.currScope,
                "arguments" : args,
                "place" : (fun).split("@")[0],
                "offset" : 4,
                "temp" : 0,
                "tempmax" : 0,
                "varwidth" : 0
                }
        self.SymbolTable[self.currScope]["function"][fun] = {
                "fname" : fun
                }
        self.currScope = fun
        print "fstartscope,"+fun
    
    def getFunc(self,name):
        scope = self.currScope
        while self.SymbolTable[scope]['type'] not in ['main']:
            for i in self.SymbolTable[scope]["function"].keys():
                if name == i.split("@")[0]:
                    return self.SymbolTable[i]
            scope = self.SymbolTable[scope]['parent']
        for i in self.SymbolTable[scope]["function"].keys():
            if name == i.split("@")[0]:
                return self.SymbolTable[i]
        sys.exit("function not declared")

    def endFunc(self):
        self.SymbolTable[self.currScope]["tempmax"]=max(self.SymbolTable[self.currScope]["tempmax"],self.SymbolTable[self.currScope]["temp"])
        self.currScope = self.SymbolTable[self.currScope]["parent"]
        print "scope,"+self.currScope
    
    def getId(self,idVal):
        scope = self.getScope(idVal)
        if scope is not None:
            return self.SymbolTable[scope]["identifiers"][idVal]
        else:
            if self.SymbolTable[idVal] is not None:
                return self.SymbolTable[idVal]
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
    
    def getOffset(self,idVal):
        scope = self.getScope(idVal)
        tempmax = self.SymbolTable[scope]['tempmax']
        return self.SymbolTable[scope]["identifiers"][idVal]['offset']+tempmax*4

    def numVarScope(self):
        #print(self.currScope)
        return self.SymbolTable[self.currScope]["varwidth"]


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
        self.SymbolTable[self.currScope]["temp"]+=1
        newTemp = "_t"+str(self.SymbolTable[self.currScope]["temp"]) 
        return newTemp

    def newScopeName(self):
        self.scopeNo += 1
        newScope = "s"+str(self.scopeNo) 
        return newScope
    
    def printScopeOffset(self):
        scope = self.currScope
        return self.SymbolTable[scope]['offset']

