#import lex
import yacc
from tokens import tokens

def p_dcl(p):
    '''dcl  :   R_VAL val_dcl
            |   R_VAR var_dcl
            |   R_DEF fun_dcl'''
    printp(p)

def val_dcl(p):
    '''val_dcl   :   id COLON type val_dcl_0'''

def val_dcl_0(p):
    '''val_dcl_0    :   epsilon
                    |   COMMA val_dcl'''

def var_dcl(p):
    '''var_dcl  :   id COLON type var_dcl_0'''

def var_dcl_0(p):
    '''var_dcl_0    :   epsilon
                    |   COMMA var_dcl'''

def fun_dcl(p):
    '''fun_dcl  :   fun_sig COLON type 
                |   fun_sig'''

#def fun_dcl_1(p):
#    '''fun_dcl_0    :   COLON type fun_dcl_0
#                    |   epsilon'''

def modifier(p):
    '''modifier :   local_modifier
                |   access_modifier
                |   R_OVERRIDE'''

def local_modifier(p):
    '''local_modifier   :   R_FINAL
                        |   R_ABSTRACT'''

def access_modifier(p):
    '''access_modifier  :   R_PRIVATE
                        |   R_PROTECTED'''

def path(p):
    '''path :   stable_id
            |   id DOT R_THIS
            |   R_THIS'''

#def path_0(p):
#    '''path_0   :   id DOT path_0
#                |   epsilon'''

def block_stat(p):
    '''block_stat   :   R_DEF
                    |   R_DCL
                    |   local_modifier_0 tmpl_def
                    |   expr1'''
                    
def block(p):
    '''block    :   epsilon
                |   block_stat semi block'''

def stable_id(p):
    '''id       :   id
                |   path DOT id
                |   id DOT R_SUPER DOT id
                |   R_SUPER DOT id'''


def simple_expr(p):
    '''simple_expr  :   R_NEW class_template
                    |   block_expr
                    |   simple_expr1'''

def class_template(p):
    '''class_template   :   id class_template_1'''

def class_template_1(p):
    '''class_template_1 :   LAPARAN id  class_template_0 RPARAN class_template_1
                        |   epsilon '''

def class_template_0(p):
    '''class_template_0 :   COMMA id class_template_0
                        |   epsilon'''

def block_expr(p):
    '''block_expr   :   block'''

def simple_expr1(p):
    '''simple_expr1 :   literal
                    |   path
                    |   LPARAN exprs_1 RPARAN
                    |   simple_expr DOT id
                    |   simple_expr type_args
                    |   simple_expr1 arguement_exprs'''

def exprs_1(p):
    '''exprs_1  :   exprs
                |   epsilon'''

def prefix_expr(p):
    '''prefix_expr  :   simple_expr
                    |   OP_MINUS simple_exprs
                    |   OP_PLUS simple_exprs
                    |   OP_NOT simple_exprs'''


parser = yacc.yacc()
#parser.parse('2+3')

