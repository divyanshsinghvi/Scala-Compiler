class HashTable:
    def __init__(self):
        self.table={}
   
### addEntry : adds entry to ST. list Attribute is dictionary of attributes and name is entry added to ST 
    def addEntry(self,name,listAttributes):
        if name in self.table:
            print 'Entry exists in symbol table'+ name
        else:
            self.table[name] = {}
            for key in listAttributes:
                self.table[name][key]=listAttribute[key]
## updateEntry : update attribute list of given entry 
    
    def updateEntry(self, name, attributeName, attributeValue ):
        try:
            self.table[name][attributeName] = attributeValue
            return True
        except:
            return False
    
    def getAttributeValue(self,name,attributeName):
        try:
            return self.table[name][attributeName]
        except:
            return None
    
    def isPresent(self,name):
        if name in self.table:
            return True
        else:
            return False
    
    def getTable(self):
        return self.table

    def printTable(self):
        for name in self.table:
            print name,'====>',self.table[name]

            
class Env:
    tableNo = 0
    def __init__(self, prev=None):
        self.symbolTable = HashTable()
        self.functionTable = HashTable()
        self.objectTable = HashTable()
        self.name = "Table" + str(Env.tableNo)
        self.children = []
        self.width = 0
        self.prevEnv = prev
        self.code = []
        self.startChildBlock = None
        self.endChildBlock = None
        self.funcName = None
        self.objName = None
        self.offset = 0
        if prev == None:
            self.level = 0
            self.parentName = ""
        else:
            self.level = prev.level + 1
            self.parentName = prev.name
        Env.tableNo += 1
        if(prev != None):
            prev.children.append(self)
        self.totalSize = 0

    def gprev(self):
        return self.prev

    def goto(self, data):
        for child in range(0, len(self.children)):
            if(self.children[child].name == data):
                return self.children[child]

    def subtree(self):
        print "NAME: ", self.name, "LEVEL: ", self.level
        self.symbolTable.printTable()
        for child in range(0, len(self.children)):
            self.child.subtree()

    def addEntry(self, name, listAttributes, updateField = "symbol"):
    	if updateField=="symbol":
            self.symbolTable.addEntry(name, listAttributes)
        elif updateField=="function":
            self.functionTable.addEntry(name, listAttributes)
        elif updateField == "object":
            self.objectTable.addEntry(name, listAttributes)
        else:
            print "Attribute Missing 'updateField'"

    def childObject(self, objSearched):
        for child in self.children:
            if child.objName == objSearched:
                return child

    # update entry in the most recent hash table in case not found in the most recent goes to the parent and then to next parent and 
    # successive goes up till the time entry is found if not found found printf error (Checks if the variable used is previously declared)
    def updateEntry(self, name, attributeName, attributeValue, updateField = "symbol"):
    	if updateField=="symbol":
            env=self
            while env!=None:
                if env.symbolTable.updateEntry(name, attributeName, attributeValue) == True:
                    return
                env=env.prevEnv
            print 'Error: Variable not present for updation - [' + name + ']'
        elif updateField=="function":
            env=self
            while env!=None:
                if env.functionTable.updateEntry(name, attributeName, attributeValue) == True:
                    return
                env=env.prevEnv
            print 'Error: Function not present for updation - [' + name + ']'
        elif updateField=="object":
            env=self
            while env!=None:
                if env.objectTable.updateEntry(name, attributeName, attributeValue) == True:
                    return
                env=env.prevEnv
            print 'Error: Object not present for updation - [' + name + ']'
        else:
            print "Attribute Missing"


    def getCurrentSymbolTable(self):
        return self.symbolTable.get_table()


    def print_table(self):
        env=self
        i=0
        while env!=None:
            print "Ancestor ==========>",i
            env.objectTable.print_table()
            env = env.prev_env
            i=i+1
    def get_width(self):
        return self.width

    def incrementWidth(self, inc):  
        self.width += inc

    

