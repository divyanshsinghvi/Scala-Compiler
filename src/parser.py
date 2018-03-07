#import lex
import yacc
from tokens import tokens


def p_ADD(p):
    ''' ADD : INT OP_ADD INT
    '''
    p[0] = p[1] + p[3]
    print p[0]

parser = yacc.yacc()
parser.parse('2+3')

