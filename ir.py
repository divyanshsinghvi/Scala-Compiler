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
    
    out=None
    in1=None
    in2=None

    def __init__(self, rowList):
        self.oper = rowList[0]
        #self.out = out  #x
        #self.in1 = in1 #y
        #self.in2 = in2 #z
        #print(rowList[0])   
    #def MakeEntry(rowList):
    #    row = ir(rowList[0],null, null, null)
        for key, val in op.iteritems():
            if rowList[0] in val:
                operator = key;
                break
        #print(operator)        
        if operator == 'binop':
            self.out = rowList[1]
            self.in1 = rowList[2] 
            self.in2 = rowList[3]
        elif operator == 'unop':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = 0
        elif operator == 'assign':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif operator == 'goto':
            self.out = rowList[1]
        elif operator == 'if':
            self.out = rowList[1]
            self.in1 = rowList[2]
        elif operator == 'param':
            self.in1 =rowList[1]
        elif operator == 'fcall':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif operator == 'freturn':
            self.in1 = rowList[1]
        elif operator == 'ldar':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif operator == 'star':
            self.out = rowList[1]
            self.in1 = rowList[2]
            self.in2 = rowList[3]
        elif operator == 'call':
            self.in1 = rowList[1]
            self.in2 = rowList[2]
        elif operator =='label':
            self.out = rowList[1]

array = []

with open('3ac.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        #print(ir(row))
        array.append(ir(row))

print [label.oper for label in array]
        
