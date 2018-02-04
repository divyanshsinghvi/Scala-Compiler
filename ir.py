import csv
from enum import Enum
from goto import goto, label

class ir:
    
    out=None
    in1=None
    in2=None
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
    op['assign']= '='
    op['goto']='goto'
    op['if']='if'
    op['param']='param'
    op['call']='call'
    op['fcall']='fcall'
    op['return']='return'
    op['freturn']='freturn'
    op['ldar']='ldar'
    op['star']='star'

    def __init__(self, op, out, in1, in2):
        self.oper = oper
        self.out = out #x
        self.in1 = in1 #y
        self.in2 = in2 #z
    
    def Insert(self, rowList):
        operator = rowList[0]
        for key, val in Dict.iteritems():
            
        
        if operator == 'binop':
            out = rowList[1]
            in1 = rowList[2] 
            in2 = rowList[3]
        elif operator == 'unop':
            out = rowList[1]
            in1 = rowList[2]
            in2 = 0
        elif operator == 'assign':
            out = rowList[1]
            in1 = rowList[2]
        elif operator == 'goto':
            out = rowList[1]
        elif operator == 'if':
            out = rowList[1]
            in1 = rowList[2]
        elif operator == 'param':
            in1 =rowList[1]
        elif operator == 'fcall':
            out = rowList[1]
            in1 = rowList[2]
            in2 = rowList[3]
        elif operator == 'freturn':
            in1 = rowList[1]
        elif operator == 'ldar':
            out = rowList[1]
            in1 = rowList[2]
            in2 = rowList[3]
        elif operator == 'star':
            out = rowList[1]
            in1 = rowList[2]
            in2 = rowList[3]

with open('3ac.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        for element in row:

