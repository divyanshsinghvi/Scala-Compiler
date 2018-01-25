from tokens import *

#t_INT = r'[+-]?([0-9])+'
#t_FLOAT = r'([+-])?[0-9]+\.([0-9]+([Ee]?[+-][0-9]+)?)?'
t_BOOL = r'(true | false)'
t_LEFTARROW = r'<-'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_LPARAN = r'\('
t_RPARAN = r'\)'
t_LSQRB = r'\['
t_RSQRB = r'\]'
t_BLOCKBEGIN = r'\{'
t_BLOCKEND = r'\}'
t_OP_ADD = r'\+'
t_OP_SUB = r'-'
t_OP_MUL = r'\*'
t_OP_DIV = r'/'
t_OP_MOD = r'%'
t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_XOR = r'\^'
t_AND_BIT = '&'
t_OR_BIT = '\|'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_RRSHIFT = r'>>>'
t_EQUALASGN = r'='
t_ADDASGN = r'\+='
t_SUBASGN = r'-='
t_MULASGN = r'\*='
t_MODASGN = r'%='
t_DIVASGN = r'/='
t_LSHIFTASGN = r'<<='
t_RSHIFTASGN = r'>>='
t_ANDASGN = r'&='
t_ORASGN = r'\|='
t_XORASGN = r'\^='
t_COLON = r':'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_COMMA = r'\,'
t_UNDER = r'_'

#Litereals

def t_INT(t):
    r'((\d+)|(((0x)|(0X))[0-9A-Fa-f]+))[lL]?'

def t_FLOAT(t):
    r'((\d+)?(\.)(\d+)([Ee][+-]?(\d+))?([FfDd])?)| ((\d)+([Ee][+-]?(\d+))?([FfDd]))'

    if t.value[-1]=='F' or t.value[-1]=='f' or t.value[-1]=='D' or t.value[-1]=='d' :
        t.value = t.value[:-1]
        t.value = float(t.value)
        return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t






