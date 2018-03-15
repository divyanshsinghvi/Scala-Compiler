from tokens import *
from lex import TOKEN

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
t_OP_NOT = r'!'
t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
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
#t_UNDER = r'_'


def t_FLOAT(t):
    r'((\d+)?(\.)(\d+)([Ee][+-]?(\d+))?([FfDd])?) | ((\d)+([Ee][+-]?(\d+))?([FfDd]))|((\d)+([Ee][+-](\d+))([FfDd])?)'
    if (t.value[-1]=='F' or t.value[-1]=='f' or t.value[-1]=='D' or t.value[-1]=='d'):
        t.value = t.value[:-1]
    t.value = float(t.value)
    return t

def t_INT(t):
    r'(((((0x)|(0X))[0-9a-fA-F]+)|(\d+))([uU]|[lL]|[uU][lL]|[lL][uU])?)'
#r'(0|[1-9](\d+)|(((0x)|(0X))[0-9A-Fa-f]+))[lL]?'
    #print t.value
    if len(t.value) > 1 and (t.value[1]=='x' or t.value[1]=='X'):
      #  print t 
        return t
    if t.value[-1]=='L' or t.value[-1]=='l':
        t.value=t.value[:-1]
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'\'([^\\\'\r\n\\[^\r\n]|\\u[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f])(\'|\\)'
    return t 

def t_STRING(t):
   # r'\"([^\"]|\"|\\|\n|\b)*\"'
    r'\"(\\.|[^\\"]| )*\"'
    t.value = t.value[1:-1]
    return t


digit            = r'([0-9])'
nondigit         = r'([_A-Za-z])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

@TOKEN(identifier)
def t_ID(t):
	t.type = reserved.get(t.value,'ID')    # Check for reserved words
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

t_ignore = ' \t'

#handling nested comments and single line comments
def t_MCOMMENT(t):
    r'(/\*(\n|.)*?\*/)'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_SCOMMENT(t):
    r'(//.*?\n)'
    t.lexer.lineno += t.value.count('\n')
    pass

# error handling 
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
    pass






