from sets import Set

class HashTable:

    def __init__(self):
        self.table={}
    
    def addEntry(self,name,listAttributes)



class Env:
    static_var = 1
    def __init__(self, prev=None):
        self.symbolTable = HashTable()  #Creates a new symbol table for a new scope
        self.functionTable = HashTable()  #Creates a new hash table for a new scope
        self.objectTable = HashTable()  #Creates a new hash table for a new scope
        
