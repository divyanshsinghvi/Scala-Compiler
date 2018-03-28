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
