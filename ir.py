import csv

PLUS ='+'
MINUS='-'
TIMES='*'
DIV='/'
MOD='%'
AND='&&'
OR ='||'
LT='<'
LE='<='
EQ='=='
GE='>='
GT='>'
NE='!='
NOT='!'
op = {}
op['binop']=[PLUS, MINUS, TIMES, DIV, AND, OR, LT, LE, EQ, GE, GT, NE, MOD]
op['unop']=[NOT]
op['assign']= ['=']
op['goto']=['goto']
op['if']=['if']
op['param']=['param']
op['call']=['call']
op['fcall']=['fcall']
op['return']=['return']
op['freturn']=['freturn']
op['ldar']=['ldar']
op['star']=['star']
op['label']=['label']
op['flabel']=['flabel']
op['array']=['array']
op['bitwise']=['&', '|', '^']
op['printInt']=['printInt']
op['scanInt']=['scanInt']
class ir:
    

    def __init__(self, rowList):
        self.out=None
        self.in1=None
        self.in2=None
        self.nextUse={}
        self.live={}
        self.operator=None
        self.oper = rowList[0]
        for key, val in op.iteritems():
            if rowList[0] in val:
                self.operator = key;
                break
        #print(operator)        
        if self.operator == 'binop':
            self.out = rowList[1]
            self.in1 = rowList[2] 
            self.in2 = rowList[3]
        elif self.operator == 'unop':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif self.operator == 'assign':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif self.operator == 'goto':
            self.out = rowList[1]
        elif self.operator == 'if':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif self.operator == 'param':
            self.in1 =rowList[1]
        elif self.operator == 'fcall':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif self.operator == 'freturn':
            self.in1 = rowList[1]
        elif self.operator == 'ldar':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif self.operator == 'star':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif self.operator == 'call':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif self.operator =='flabel':
            self.out = rowList[1]
        elif self.operator =='label':
            self.out = rowList[1]
        elif self.operator == 'bitwise':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif self.operator == 'array':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif self.operator == 'printInt':
            self.out = rowList[1]
            #print rowList[1]
        elif self.operator == 'scanInt':
            self.out = rowList[1]

class irTable:
    def __init__(self, filename):
        self.arr=[]
        self.leadList=set()
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row[0].startswith('#'):
                    continue
                self.arr.append(ir(row))
        instrTable = self.arr # ir.irTable(filename).arr
        self.leadList.add(0)
        #print type(instrTable)
        for index ,ic  in enumerate(instrTable):
            if ic.oper == 'label':
                self.leadList.add(index)
            elif (ic.oper == 'call' or ic.oper == 'fcall' or ic.oper == 'if' or ic.oper == 'goto' or ic.oper == 'return' or ic.oper == 'freturn') and index != len(instrTable) - 1:
                self.leadList.add(index+1)
        self.leadList= list(self.leadList)
        self.leadList.sort()
               

if __name__ == "__main__":
    t = irTable('3ac.csv')
    print [label.oper for label in t.arr]

