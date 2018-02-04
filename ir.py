import csv
from enum import Enum

class ir:
   # Types = Enum(Binop,Unop,Assign,Goto,If,Param,Call,Fcall,Return,Freturn,Ldar,Star)
    
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
        self.op = op
        self.out = out
        self.in1 = in1
        self.in2 = in2
    
    def Insert(self, rowList):
        for key, val in Dict.iteritems():

with open('3ac.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', doublequote=True, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        for element in row:

