#import lex
import yacc
from tokens import tokens

def printp(p):
    for i in range(0,len(p)):
        print(p[0],end=' ')

def p_compilation_unit(p):
    '''compilation_unit : compilation_unit_0 top_stat_seq
    '''
    
def p_compilation_unit_0(p):
    '''compilation_unit_0 : empty
                         | compilation_unit_0  R_PACKAGE qual_id semi  
    '''

def p_top_stat_seq(p):
    '''top_stat_seq : top_stat_seq_0
    '''

def p_top_stat_seq_0(p):
    '''top_stat_seq_0 :  empty
                    | top_stat_seq_0 top_stat semi
    '''

def p_top_stat(p):
    '''top_stat : local_modifier_0 tmpl_def
                | import
    '''

def p_local_modifier_0(p):
    '''local_modifier_0 : empty 
                        | local_modifier_0 local_modifier
    '''

def p_tmpl_def(p):
    ''' tmpl_def : R_CLASS class_def
                 | R_OBJECT object_def        
    '''

def p_class_def(p): 
    '''class_def : id class_param_clause class_template_opt
    '''

def p_class_param_clause(p):
    '''class_param_clause : LPARAN  class_params_1  RPARAN
    '''

def p_class_params_1(p):
    '''class_params_1 : class_params
                      | epsilon
    '''

def p_class_params(p) :  
    ''' class_params : class_param
                     | class_param_0
    '''

def p_class_param_0(p):
    ''' class_param_0 : empty
                      | class_param_0 COMMA class_param
    '''

def p_class_param(p):
    ''' class_param : val_var_1 id COLON type eq_expr_1
    '''

def p_val_var_1(p):
    ''' val_var_1 : val_var 
                  | epsilon
    '''

def p_val_var(p):
    ''' val_var : R_VAL 
                | R_VAR
    '''
def p_eq_expr_1(p):
    ''' eq_expr_1 : EQUALASGN expr
                  | epsilon
    '''
def p_class_template_opt(p):
    ''' class_template_opt : class_template_opt_2 template_body
    '''
def p_class_template_opt_2(p):
    ''' class_template_opt_2 : R_EXTENDS id  class_template_opt_1
                             | empty

    '''
def p_class_template_opt_1(p):
    '''class_template_opt_1 : LPARAN id com_id_0 RPARAN
                            | empty
    '''
def p_com_id(p):
    ''' com_id : empty
                | com_id COMMA id 
    '''
def p_template_body(p):
    ''' template_body : BLOCKBEGIN template_body_0 BLOCKEND
    '''

def p_template_body_0(p):
    ''' template_body_0 : empty
                        | template_body_0 template_stat semi
    '''
def p_template_stat(p):
    ''' template_stat : expr
                      | modifier_0 def
                      | modifier_0 dcl
    '''
def p_modifier_0(p):
    ''' modifier_0 : empty
                    | modifier_0 modifier
    '''
def p_import(p):
    ''' import : R_IMPORT import_expr COMMA import_expr
    '''
def p_import_expr(p):
    '''import_expr : stable_id DOT id
    '''
def p_def(p):
    ''' def : path_var_def 
            | R_DEF fun_def 
            | tmpl_def
    '''
def p_pat_var_def(p):
    ''' pat_var_def : R_VAR var_def
                    | R_VAL val_def
    '''
def p_var_def(p):
    ''' var_def : id COLON type EQUALASGN expr
    '''
def p_val_def(p):
    ''' val_def : id COLON type EQUALASGN expr
    '''
#some ambiguity here ???
def p_fun_def(p):
    ''' fun_def : fun_sig col_type_1 EQUALASGN BLOCKBEGIN expr semi BLOCKEND
    '''
def p_col_type_1(p) :
    ''' col_type_1 : COLON type
                    | epsilon
    '''
def p_funsig(p):
    ''' funsig : id param_clause
    '''
def p_param_clause(p):
    ''' param_clause : LPARAN  RPARAN
                      | LPARAM params RPARAN
    '''
def p_params(p):
    ''' params : param COMMA param
    '''
def p_param(p):
    ''' param : id COLON param_type eq_expr | id eq_expr
    '''
def p_eq_expr(p):
    ''' eq_expr : empty
                | EQUALASGN expr
    '''
def p_param_type(p):
    ''' param_type : type
                    | type LEFTARROW type
    '''
def p_ADD(p):
    ''' ADD : INT OP_ADD INT
    '''
    p[0] = p[1] + p[3]
    print p[0]

parser = yacc.yacc()
parser.parse('2+3')

