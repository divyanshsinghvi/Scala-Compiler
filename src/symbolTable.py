from sets import Set

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
    static_var = 1
    def __init__(self, prev=None):
        self.symbolTable = HashTable()  #Creates a new symbol table for a new scope
        self.functionTable = HashTable()  #Creates a new hash table for a new scope
        self.objectTable = HashTable()  #Creates a new hash table for a new scope
        
