##########################SymbolTable############################################
#Dictionary of Dictionary to store nextUse and livelniess information about all variab

class SymbolTable:
    idNo = 0
    def __init__(self):
        self.var = {}           #dictionary of all variables
    
    def setVar(self,name,attribute):
        if name not in self.var:
            self.var[name]=attribute
        else:
            for key in attribute:
                self.var[name][key]=attribute[key]

    def getVar(self,name,value):
        if name not in self.var:
            return None
        if value not in self.var[name]:
            return None
        return self.var[name][value]

    def print_symboltable(self):
        
        if not self.var:
            return 
        for name in self.var:
            print name,
            #print("Attribute for variable :")
            for key in self.var[name]:
                print key+"="+str(self.var[name][key]), 
            print "\n"
        print("----------------------------------------")
    

#Example to check symbol table 
if __name__ == '__main__':
    s=SymbolTable()
    s.set('a',{'name':'zara','type':'int','age':'7'})
    s.print_symboltable()
    s.set('b',{'age':7,'name':'megha'})
    s.print_symboltable()
    print(s.get('a','name'))
    print(s.get('a','height'))
    s.set('b',{'height':'11'})
    s.print_symboltable()


