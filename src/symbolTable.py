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
    def __inti__(self, prev=None):
        self.symbolTable = HashTable()
        self.functionTable = HashTable()
        self.objectTable = HashTable()
        self.name = "Table" + str(env.tableNo)
        self.children = []
        self.width = 0
        self.prev = prev
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
            for child in range(0, len(slef.children)):
                if(self.children[child].name == data):
                    return self.children[child]

        def subtree(self):
            print "NAME: ", self.name, "LEVEL: ", self.level
            self.symbolTable.printTable()
            for child in range(0, len(self.children)):
                self.child.subtree()

        def addEntry(self, name, list_attributes, updateField = "symbol"):
