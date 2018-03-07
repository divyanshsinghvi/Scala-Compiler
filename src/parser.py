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
