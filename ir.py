import csv

PLUS ='+'
MINUS='-'
TIMES='*'
DIV='/'
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
op['binop']=[PLUS, MINUS, TIMES, DIV, AND, OR, LT, LE, EQ, GE, GT, NE]
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
            self.in1 = rowList[1]
            self.in2 = rowList[2]
        elif self.operator =='label':
            self.out = rowList[1]

class irTable:
    def __init__(self, filename):
        self.arr=[]
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                self.arr.append(ir(row))
               

if __name__ == "__main__":
    t = irTable('3ac.csv')
    print [label.oper for label in t.arr]

