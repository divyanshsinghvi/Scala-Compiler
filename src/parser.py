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
def p_dcl(p):
    '''dcl  :   R_VAL val_dcl
            |   R_VAR var_dcl
            |   R_DEF fun_dcl'''
    printp(p)

def p_val_dcl(p):
    '''val_dcl   :   id COLON type val_dcl_0'''

def p_val_dcl_0(p):
    '''val_dcl_0    :   epsilon
                    |   COMMA val_dcl'''

def p_var_dcl(p):
    '''var_dcl  :   id COLON type var_dcl_0'''

def p_var_dcl_0(p):
    '''var_dcl_0    :   epsilon
                    |   COMMA var_dcl'''

def p_fun_dcl(p):
    '''fun_dcl  :   fun_sig COLON type 
                |   fun_sig'''

#def fun_dcl_1(p):
#    '''fun_dcl_0    :   COLON type fun_dcl_0
#                    |   epsilon'''

def p_modifier(p):
    '''modifier :   local_modifier
                |   access_modifier
                |   R_OVERRIDE'''

def p_local_modifier(p):
    '''local_modifier   :   R_FINAL
                        |   R_ABSTRACT'''

def p_access_modifier(p):
    '''access_modifier  :   R_PRIVATE
                        |   R_PROTECTED'''

def p_path(p):
    '''path :   stable_id
            |   id DOT R_THIS
            |   R_THIS'''

#def path_0(p):
#    '''path_0   :   id DOT path_0
#                |   epsilon'''

def p_block_stat(p):
    '''block_stat   :   R_DEF
                    |   R_DCL
                    |   local_modifier_0 tmpl_def
                    |   expr1'''
                    
def p_block(p):
    '''block    :   epsilon
                |   block_stat semi block'''

def p_stable_id(p):
    '''id       :   id
                |   path DOT id
                |   id DOT R_SUPER DOT id
                |   R_SUPER DOT id'''


def p_simple_expr(p):
    '''simple_expr  :   R_NEW class_template
                    |   block_expr
                    |   simple_expr1'''

def p_class_template(p):
    '''class_template   :   id class_template_1'''

def p_class_template_1(p):
    '''class_template_1 :   LAPARAN id  class_template_0 RPARAN class_template_1
                        |   epsilon '''

def p_class_template_0(p):
    '''class_template_0 :   COMMA id class_template_0
                        |   epsilon'''

def p_block_expr(p):
    '''block_expr   :   block'''

def p_simple_expr1(p):
    '''simple_expr1 :   literal
                    |   path
                    |   LPARAN exprs_1 RPARAN
                    |   simple_expr DOT id
                    |   simple_expr type_args
                    |   simple_expr1 arguement_exprs'''

def p_exprs_1(p):
    '''exprs_1  :   exprs
                |   epsilon'''

def p_prefix_expr(p):
    '''prefix_expr  :   simple_expr
                    |   OP_MINUS simple_exprs
                    |   OP_PLUS simple_exprs
                    |   OP_NOT simple_exprs'''



def p_array_type(p):
    ''' type : id LSQRB type RSQRB
    '''
    printp(p)

def p_type(p):                      # look at <T>
    ''' type : basic_type
             | array_type
             | <T>
    '''
    printp(p)

def p_simple_type(p):
    ''' simple_type : type
                   | LPARAN type RPARAN
    '''
    printp(p)

def p_semi(p):
    ''' semi : SEMICOLON
    '''
    printp(p)

def p_qual_id(p):
    ''' qual_id : id dot_id_0
    '''
    printp(p)

def p_dot_id_0(p):
    ''' dot_id_0 : epsilon
             | dot_id_0 DOT id
    '''
    printp(p)

def p_object_def(p):
    ''' object_def : id class_template_opt
    '''
    printp(p)

def p_catch_params(p):
    ''' catch_params : type id
    '''
    printp(p)

def p_catch_clause(p):
    ''' catch_clause : R_CATCH LPARAN catch_params LPARAN BLOCKBEGIN block BLOCKEND catch_clause_1
    '''
    printp(p)

def p_catch_clause_1(p):
    ''' catch_clause_1 : catch_clause
                       | epsilon
    '''
    printp(p)

def p_for_upd(p):           # to be done later, the for case

def p_for_logic(p):
    ''' for_logic : for_upd semi_for_logic_1
    '''
    printp(p)

def p_semi_for_logic_1(p):
    ''' semi_for_logic_1 : semi for_logic
                    | epsilon
    '''
    printp(p)

def p_switch_labels(p):
    ''' switch_labels : R_CASE literal COLON
                      | R_DEFAULT COLON
    '''
    printp(p)

def p_switch_block_statements(p):
    ''' switch_block_statements : switch_labels_0 BLOCKBEGIN block BLOCKEND
    '''
    printp(p)

def p_switch_labels_0(p):
    ''' switch_labels_0 : epsilon
                        | switch_labels_0 switch_labels
    '''
    printp(p)

def p_switch_block(p):
    '''  BLOCKBEGIN switch_block_statements_0 switch_labels_1 BLOCKEND
    '''
    printp(p)

def p_switch_block_statements_0(p):
    ''' switch_block_satements_0 : epsilon
                                 | switch_block_statements_0 switch_block_statements
    '''
    printp(p)

def p_switch_labels_1(p):
    ''' switch_labels_1 : switch_labels
                        | epsilon
    '''
    printp(p)

def p_expr1(p):
    ''' expr1 : R_IF LPARAN expr RPARAN BLOCKBEGIN expr semi BLOCKEND expression1
              | R_WHILE LPARAN expr RPARAN BLOCKBEGIN expr semi BLOCKEND
              | R_TRY BLOCKBEGIN block BLOCKEND catch_clause_1 expressoin2
              | R_DO BLOCKBEGIN expr semi BLOCKEND R_WHILE LPARAN expr RPARAN
              | R_FOR LPARAN for_logic RPARAN BLOCKBEGIN expr semi BLOCKEND
              | R_RETURN expr
              | post_fix_expr
              | switch LPARAN expr RPARAN switch_block
              | R_ARRAY LPARAN literal literal_0 RPARAN
    '''
    printp(p)

def p_expression1(p):
    ''' expression1 : R_ELSE BLOCKBEGIN expr semi BLOCKEND
                    | epsilon
    '''
    printp(p)

def p_expression2(p):
    ''' expression2 : R_FINALLY BLOCKBEGIN expr semi BLOCKEND
                    | epsilon
    '''
    printp(p)

def p_literal_0(p):
    ''' literal_0 : epsilon
                  | literal_0 COMMA literal
    '''
    printp(p)

def p_expr(p):
    ''' expr : expr1
    '''
    printp(p)

def p_argument_exprs(p):
    ''' argument_exprs : LPARAN exprs_1 RPARAN
    '''
    printp(p)

def p_exprs_1(p):
    ''' exprs_1 : exprs
                | epsilon
    '''
    printp(p)

def p_postfix_expr(p):
    ''' postfix_expr : infix_expr id_1
    '''
    printp(p)

def p_id_1(p):
    ''' id_1 : id
             | id_1 id
    '''
    printp(p)

def p_infix_expr(p):
    ''' infix_expr : infix_expr id infix_expr
                   | prefix_expr
    '''
    printp(p)

def p_types(p):
    ''' types : type comma_type_0
    '''
    printp(p)

def p_comma_type_0(p):
    ''' comma_type_0 : epsilon
                     | comma_type_0 COMMA type
    '''
    printp(p)

def p_type_args(p):
    ''' type_args : LSQRB types RSQRB
    '''
    printp(p)
