import sys
import ply.yacc as yacc
import lexer
from symbolTable import *

x=0
y=0
SCOPE=Env(None)

def newlabel():
    global y
    y += 1
    return "L"+str(y)

def newtmp():
    global x
    x += 1
    return "t$"+str(x)

def emit(op=None,out=None,in1=None,in2=None):
    print op,out,in1,in2
    return op,out,in1,in2
    if(in1!=None and in2!=None and out!=None):
        SCOPE.code.append([op,in1,in2,out])
        print op, in1, in2, out
    elif(in1!=None and in2!=None and out==None):
        SCOPE.code.append([op,in1,in2])
        print op, in1, in2
    elif(in1!=None and in2==None and out==None):
        SCOPE.code.append([op,in1])
        print op, in1
    elif(in1==None and in2!=None and out==None):
        SCOPE.code.append([op,in2])
        print op, in2
    elif(in1==None and in2!=None and out!=None):
        SCOPE.code.append([op,in2,out])
        print op, in2, out
    elif(in1==None and in2==None and out==None):
        SCOPE.code.append([op])
        print op

tokens = lexer.tokens
precedence = (
        ('right','XORASGN','ORASGN','ANDASGN','RSHIFTASGN','LSHIFTASGN','MODASGN','DIVASGN','MULASGN','SUBASGN','EQUALASGN'),
        ('left','OR'),
        ('left','AND'),
        ('left','OR_BIT'),
        ('left','XOR'),
        ('left','AND_BIT'),
        ('left','EQ','NEQ'),
        ('left','LE','LT','GT','GE'),
        ('left','RSHIFT','LSHIFT','RRSHIFT'),
        ('left','OP_ADD','OP_SUB'),
        ('left','OP_DIV','OP_MUL','OP_MOD')
#        ('right','OP_NOT')
)
def printp(p):
    for i in range(0,len(p)):
        print (p.slice)[i],

    print "\n",


def p_compilation_unit(p):
    '''compilation_unit : compilation_unit_0 top_stat_seq_0
    '''
    p[0] = dict()
    #printp(p)
    
def p_compilation_unit_0(p):
    '''compilation_unit_0 : epsilon
                         | compilation_unit_0  R_PACKAGE qual_id semi  
    '''
    p[0] = dict()
    #printp(p)


def p_top_stat_seq_0(p):
    '''top_stat_seq_0 :  epsilon
                    | top_stat_seq_0 top_stat semi
    '''
    p[0] = dict()
    #printp(p)

def p_top_stat(p):
    '''top_stat : local_modifier_0 tmpl_def
                | import
    '''
    p[0] = dict()
    #printp(p)

def p_local_modifier_0(p):
    '''local_modifier_0 : epsilon 
                        | local_modifier_0 local_modifier
    '''
    p[0] = dict()
    #printp(p)

def p_tmpl_def(p):
    ''' tmpl_def : R_CLASS class_def
                 | R_OBJECT object_def        
    '''
    p[0] = dict()
    #printp(p)

def p_class_def(p): 
    '''class_def : id class_param_clause class_template_opt
    '''
    p[0] = dict()
    #printp(p)

def p_class_param_clause(p):
    '''class_param_clause : LPARAN  class_params  RPARAN
    '''
    p[0] = dict()
    #printp(p)

def p_class_params(p) :  
    ''' class_params : epsilon
                     | class_param  class_param_0
    '''
    p[0] = dict()
    #printp(p)

def p_class_param_0(p):
    ''' class_param_0 : epsilon
                      | COMMA class_param class_param_0
    '''
    p[0] = dict()
    #printp(p)

def p_class_param(p):
    ''' class_param : val_var_1 id COLON type eq_expr_1
    '''
    p[0] = dict()
    #printp(p)

def p_val_var_1(p):
    ''' val_var_1 : val_var 
                  | epsilon
    '''
    p[0] = dict()
    #printp(p)

def p_val_var(p):
    ''' val_var : R_VAL 
                | R_VAR
    '''
    p[0] = dict()
    #printp(p)
def p_eq_expr_1(p):
    ''' eq_expr_1 : EQUALASGN expr
                  | epsilon
    '''
    p[0] = dict()
    #printp(p)
def p_class_template_opt(p):
    ''' class_template_opt : class_template_opt_2 template_body
    '''
    p[0] = dict()
    #printp(p)
def p_class_template_opt_2(p):
    ''' class_template_opt_2 : R_EXTENDS id  class_template_opt_1
                             | epsilon

    '''
    p[0] = dict()
    #printp(p)
def p_class_template_opt_1(p):
    '''class_template_opt_1 : LPARAN id com_id RPARAN
                            | epsilon
    '''
    p[0] = dict()
    #printp(p)
def p_com_id(p):
    ''' com_id : epsilon
                | com_id COMMA id 
    '''
    p[0] = dict()
    #printp(p)
def p_template_body(p):
    ''' template_body : BLOCKBEGIN template_body_0 BLOCKEND
    '''
    p[0] = dict()
    #printp(p)

def p_template_body_0(p):
    ''' template_body_0 : epsilon
                        | template_body_0 template_stat semi
    '''
    p[0] = dict()
    #printp(p)

def p_template_stat(p):
    ''' template_stat : block_stat
                      | modifier_0 def
                      | modifier_0 dcl
    '''
    p[0] = dict()
    #printp(p)

def p_modifier_0(p):
    ''' modifier_0 : modifier
                    | modifier_0 modifier
    '''
    p[0] = dict()
    #printp(p)
def p_import(p):
    ''' import : R_IMPORT import_expr import_0
    '''
    p[0] = dict()
    #printp(p)

def p_import_0(p):
    ''' import_0 : COMMA import_expr import_0
                 | epsilon

    '''
    p[0] = dict()
    #printp(p)

def p_import_expr(p):
    '''import_expr : path
    '''
    p[0] = dict()
    #printp(p)
def p_def(p):
    ''' def : path_var_def 
            | R_DEF fun_def 
            | tmpl_def
    '''
    p[0] = dict()
    #printp(p)
def p_path_var_def(p):
    ''' path_var_def : R_VAR var_def
                    | R_VAL val_def
    '''
    p[0] = dict()
    #printp(p)
def p_var_def(p):
    ''' var_def : id COLON id EQUALASGN val_var_init
                | id COLON basic_type EQUALASGN val_var_init
                | id COLON array_type array_size EQUALASGN val_var_init

    ''' 
    p[0] = dict()
    #printp(p)

def p_array_size(p):
    ''' array_size : epsilon
                   | LPARAN ints RPARAN                           
    '''   
    p[0] = dict()
    #printp(p)
def p_ints(p):
    ''' ints : INT
             | COMMA ints
    '''
    p[0] = dict()
    # Array[Char](10,3,4)

def p_val_def(p):
    ''' val_def : id COLON type EQUALASGN val_var_init
    '''
    p[0] = dict()
    #printp(p)

def p_val_var_init(p):
    '''val_var_init : array_init
                | infix_expr
    '''
    p[0] = dict()
    #printp(p)

def p_array_init(p):
    ''' array_init : BLOCKBEGIN epsilon BLOCKEND
                   | BLOCKBEGIN val_var_init array_init_0 BLOCKEND
    '''
    p[0] = dict()
    #printp(p)

def p_array_init_0(p):
    '''array_init_0 : val_var_init array_init_0 
                    | COMMA array_init_0
                    | epsilon
    '''
    p[0] = dict()
    #printp(p)

#some ambiguity here ???
def p_fun_def(p):
    ''' fun_def : fun_sig col_type_1 EQUALASGN BLOCKBEGIN block BLOCKEND
    '''
    p[0] = dict()
    #printp(p)
def p_col_type_1(p) :
    ''' col_type_1 : COLON type
                    | epsilon
    '''
    p[0] = dict()
    #printp(p)
def p_fun_sig(p):
    ''' fun_sig : id param_clause
    '''
    p[0] = dict()
    #printp(p)
def p_param_clause(p):
    ''' param_clause : LPARAN  RPARAN
                      | LPARAN params RPARAN
    '''
    p[0] = dict()
    #printp(p)
def p_params(p):
    ''' params : param  param_0
    '''
    p[0] = dict()
    #printp(p)

def p_param_0(p):
    '''param_0 :  epsilon
               | COMMA param
    '''
    p[0] = dict()
    #printp(p)
def p_param(p):
    ''' param : id COLON param_type eq_expr 
              | R_VAR id COLON param_type eq_expr
              | R_VAL id COLON param_type eq_expr
    '''
    p[0] = dict()
    #printp(p)
def p_eq_expr(p):
    ''' eq_expr : epsilon
                | EQUALASGN expr
    '''
    p[0] = dict()
    #printp(p)
def p_param_type(p):
    ''' param_type : type
                    | type LEFTARROW type
    '''
    p[0] = dict()
    #printp(p)
def p_dcl(p):
    '''dcl  :   R_VAL val_dcl
            |   R_VAR var_dcl
            |   R_DEF fun_dcl'''
    p[0] = dict()
    #printp(p)

def p_val_dcl(p):
    '''val_dcl   :   id COLON type val_dcl_0'''
    p[0] = dict()
    #printp(p)

    #printp(p)
def p_val_dcl_0(p):
    '''val_dcl_0    :   epsilon
                    |   COMMA val_dcl'''
    p[0] = dict()
    #printp(p)

def p_var_dcl(p):
    '''var_dcl  :   id COLON basic_type var_dcl_0
                |   id COLON array_type array_size var_dcl_0
                |   id COLON id var_dcl_0
    '''
    p[0] = dict()
    #printp(p)

def p_var_dcl_0(p):
    '''var_dcl_0    :   epsilon
                    |   COMMA var_dcl'''
    p[0] = dict()
    #printp(p)

def p_fun_dcl(p):
    '''fun_dcl  :   fun_sig COLON type 
                |   fun_sig'''
    p[0] = dict()
    #printp(p)

#def fun_dcl_1(p):
#    '''fun_dcl_0    :   COLON type fun_dcl_0
#                    |   epsilon'''

def p_modifier(p):
    '''modifier :   local_modifier
                |   access_modifier
                |   R_OVERRIDE'''
    p[0] = dict()
    #printp(p)

def p_local_modifier(p):
    '''local_modifier   :   R_FINAL
                        |   R_ABSTRACT'''
    p[0] = dict()
    #printp(p)

def p_access_modifier(p):
    '''access_modifier  :   R_PRIVATE
                        |   R_PROTECTED
                        |   R_PUBLIC'''
    p[0] = dict()
    #printp(p)

def p_path(p):
    '''path :   id
            |   R_THIS
            |   id DOT path
            |   R_SUPER DOT path
            '''
    p[0] = dict()
    #printp(p)

#def path_0(p):
#    '''path_0   :   id DOT path_0
#                |   epsilon'''

def p_block_stat(p):
    '''block_stat   :   def
                    |   dcl
                    |   local_modifier_0 tmpl_def
                    |   expr'''
    p[0] = dict()
    #printp(p)
                    
def p_block(p):
    '''block    :   epsilon
                |   block_stat semi block'''
    p[0] = dict()
    #printp(p)

#def p_stable_id(p):
#    '''stable_id :   id
#                 |   path DOT id
#                 |   id DOT R_SUPER DOT id
#                 |   R_SUPER DOT id'''
#    #printp(p)


def p_simple_expr(p):
    '''simple_expr  :   R_NEW class_template
                    |   simple_expr1'''
    p[0] = dict()
    #printp(p)
 #                   |   block

def p_class_template(p):
    '''class_template   :   id class_template_1'''
    p[0] = dict()
    #printp(p)

def p_class_template_1(p):
    '''class_template_1 :   LPARAN id  class_template_0 RPARAN
                        |   LPARAN literal class_template_0 RPARAN
                        |   epsilon '''
    p[0] = dict()
    #printp(p)

def p_class_template_0(p):
    '''class_template_0 :   COMMA id class_template_0
                        |   COMMA literal class_template_0
                        |   epsilon'''
    p[0] = dict()
    #printp(p)

#def p_block_expr(p):
#    '''block_expr   :   block'''
#    #printp(p)

def p_simple_expr1(p):
    '''simple_expr1 :   literal
                    |   path
                    |   LPARAN exprs_1 RPARAN
                    |   simple_expr DOT id
                    |   simple_expr type_args
                    |   simple_expr1 argument_exprs'''
    p[0] = dict()
    #printp(p)

#def p_exprs_1(p):
#    '''exprs_1  :   exprs
#                |   epsilon'''
#    #printp(p)

def p_prefix_expr(p):
    '''prefix_expr  :   simple_expr
                    |   OP_SUB simple_expr
                    |   OP_ADD simple_expr
                    |   OP_NOT simple_expr'''
    p[0] = dict()
    #printp(p)

def p_type(p):                      # look at <T>
    ''' type : basic_type
             | array_type
             | id
    '''
    p[0] = dict()
    #printp(p)

def p_array_type(p):
    ''' array_type : TYPE_ARRAY LSQRB type RSQRB
    '''
    p[0] = dict()
    #printp(p)

#def p_simple_type(p):
#    ''' simple_type : type
#                    | LPARAN type RPARAN
#    '''
#    #printp(p)

def p_semi(p):
    ''' semi : SEMICOLON
    '''
    p[0] = dict()
    #printp(p)

def p_qual_id(p):
    ''' qual_id : id dot_id_0
    '''
    p[0] = dict()
    #printp(p)

def p_dot_id_0(p):
    ''' dot_id_0 : epsilon
             | dot_id_0 DOT id
    '''
    p[0] = dict()
    #printp(p)

def p_object_def(p):
    ''' object_def : id class_template_opt
    '''
    p[0] = dict()
    #printp(p)

def p_catch_params(p):
    ''' catch_params : type id
    '''
    p[0] = dict()
    #printp(p)

def p_catch_clause(p):
    ''' catch_clause : R_CATCH LPARAN catch_params LPARAN BLOCKBEGIN block BLOCKEND catch_clause_1
    '''
    p[0] = dict()
    #printp(p)

def p_catch_clause_1(p):
    ''' catch_clause_1 : catch_clause
                       | epsilon
    '''
    p[0] = dict()
    #printp(p)

def p_for_logic(p):
    ''' for_logic : LPARAN for_init semi infix_expr semi for_upd
                  | LPARAN for_init semi epsilon semi for_upd
    '''
    p[0] = dict()
    #printp(p)

def p_for_init(p):
    ''' for_init : epsilon
                 | var_def for_inits
                 | var_dcl for_inits
                 | infix_expr for_inits
    '''
    p[0] = dict()
    #printp(p)

def p_for_inits(p):
    '''for_inits : COMMA for_inits
                 | for_init

    '''
    p[0] = dict()

def p_for_upd(p):           # to be done later, the for case
    ''' for_upd : RPARAN
                   | infix_expr RPARAN
    '''
    p[0] = dict()
    #printp(p)

#def p_semi_for_logic_1(p):
#    ''' semi_for_logic_1 : semi for_logic
#| epsilon
#    '''
#    #printp(p)

def p_switch_labels(p):
    ''' switch_labels : R_CASE literal COLON
                      | R_DEFAULT COLON
    '''
    p[0] = dict()
    #printp(p)

def p_switch_block_statements(p):
    ''' switch_block_statements : switch_labels_0 BLOCKBEGIN block BLOCKEND semi
    '''
    p[0] = dict()
    #printp(p)

def p_switch_labels_0(p):
    ''' switch_labels_0 : epsilon
                        | switch_labels_0 switch_labels
    '''
    p[0] = dict()
    #printp(p)

def p_switch_block(p):
    ''' switch_block : BLOCKBEGIN switch_block_statements_0 BLOCKEND
    '''
    p[0] = dict()
    #printp(p)

def p_switch_block_statements_0(p):
    ''' switch_block_statements_0 : epsilon
                                 | switch_block_statements_0 switch_block_statements
    '''
    p[0] = dict()
    #printp(p)

#def p_switch_labels_1(p):
#    ''' switch_labels_1 : switch_labels
#                        | epsilon
#    '''
#    #printp(p)

def p_expr(p):
    ''' expr : R_IF LPARAN postfix_expr RPARAN BLOCKBEGIN ifmark1 block ifmark2 BLOCKEND %prec
              | R_IF LPARAN postfix_expr RPARAN BLOCKBEGIN ifmark1 block BLOCKEND R_ELSE BLOCKBEGIN ifmark3 block  ifmark4 BLOCKEND
              | R_WHILE LPARAN wmark1 postfix_expr RPARAN BLOCKBEGIN wmark2 block wmark3 BLOCKEND
              | R_TRY BLOCKBEGIN block BLOCKEND catch_clause_1 expression2
              | R_DO BLOCKBEGIN block BLOCKEND R_WHILE LPARAN postfix_expr RPARAN
              | R_FOR  fmark1 for_logic  BLOCKBEGIN fmark2 block fmark3 BLOCKEND
              | R_RETURN expr
              | R_BREAK
              | R_CONTINUE
              | postfix_expr
              | R_SWITCH LPARAN expr RPARAN switch_block
    '''
    p[0] = dict()
              #| R_ARRAY LPARAN literal literal_0 RPARAN

#    if (p.slice)[1].type == "R_IF":
    #printp(p)

def p_ifmark1(p):
    '''ifmark1 : epsilon
    '''
    l1 = newlabel()
    l2 = newlabel()
    emit(op='if',in1=p[-2]['palce'],out=l1) #if expr is true goto label1
    emit(op='goto',out=l2) #else goto label 2
    emit(op='label',out=l1) #declare label1
    ST.newScope()
    p[0] = [l1,l2]

def p_ifmark2(p):
    '''ifmark2 : epsilon
    '''
    ST.endScope()
    emit(op='label',out=p[-2]['label'][1])#deinf label 2 here

def p_ifmark3(p):
    '''ifmark3 : epsilon
    '''
    l3 = newlabel()
    emit(op='goto',out=l3) #goto exit label 3 
    emit(op='label',out=p[-5]['label'][1]) #deine label2
    p[0]['label'] = [l3]

def p_ifmark4(p):
    '''ifmark4 : epsilon
    '''
    ST.endScope()
    emit(op='label',out=p[-2][label][0]) #define label 3


def p_wmark1(p):
    '''wmark1 : epsilon
    '''
    l1 = newlabel()
    l2 = newlabel()
    l3 = newlabel()
    ST.newScope()
    emit(op='label',out=l1) #define label 1 here
    p[0]['label'] = [l1,l2,l3]

def p_wmark2(p):
    '''wmark2 : epsilon
    '''
    emit(op='if',out=p[-4]['label'][1],in1=p[-3]['place']) #if given expr is true go to l2
    emit(op='goto',out=p[-4]['label'][2]) # else goto exit label 3
    emit(op='label',out=p[-4]['label'][1]) #define label 2 here

def p_wmark3(p):
    '''wmark3 : epsilon
    '''
    emit(op='goto',out=p[-6]['label'][0]) #define goto label1
    emit(op='label',out=p[-6]['label'][2]) #define exit label label 3 here
    ST.endScope()

def p_fmark1(p):
    '''fmark1 : epsilon
    '''
    l1 = newlabel()
    l2 = newlabel()
    l3 = newlabel()
    ST.newScope()
    emit(op='label',out=l1) #define label 1 here
    p[0]['label'] = [l1,l2,l3]

def p_fmark2(p):
    '''fmark2 : epsilon
    '''
    emit(op='if',out=p[-3]['label'][1],in1=p[-3]['place']) #if given expr is true go to l2
    emit(op='goto',out=p[-3]['label'][2]) # else goto exit label 3
    emit(op='label',out=p[-3]['label'][1]) #define label 2 here

def p_fmark3(p):
    '''fmark3 : epsilon
    '''
    emit(op='goto',out=p[-5]['label'][0]) #define goto label1
    emit(op='label',out=p[-5]['label'][2]) #define exit label label 3 here
    ST.endScope()
#def p_expression1(p):
#    ''' expression1 : R_ELSE BLOCKBEGIN block BLOCKEND
#                    | epsilon
#    '''
#    p[0] = dict()
#    #printp(p)

def p_expression2(p):
    ''' expression2 : R_FINALLY BLOCKBEGIN block BLOCKEND
                    | epsilon
    '''
    p[0] = dict()
    #printp(p)

#def p_literal_0(p):
#    ''' literal_0 : epsilon
#                  | literal_0 COMMA literal
#    '''
#    #printp(p)


def p_argument_exprs(p):
    ''' argument_exprs : LPARAN exprs_1 RPARAN
    '''
    p[0] = dict()
    #printp(p)

def p_exprs(p):
    ''' exprs : COMMA exprs_1
              | epsilon
    '''
    p[0] = dict()
    #printp(p)

def p_exprs_1(p):
    ''' exprs_1 : expr exprs
                | epsilon
    '''
    p[0] = dict()
    #printp(p)

def p_postfix_expr(p):
    ''' postfix_expr : infix_expr id_1
                     | infix_expr
    '''
    p[0] = dict()
    #printp(p)

def p_id_1(p):
    ''' id_1 : id
             | id_1 id
    '''
    p[0] = dict()
    #printp(p)

#def p_infix_expr(p):
#    ''' infix_expr : infix_expr op infix_expr
#                   | infix_expr asgn infix_expr
#                   | prefix_expr
#    '''
#    #printp(p)

def p_infix_expr(p):
    ''' infix_expr : assign
                   | or_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']

    #printp(p)

def p_assign(p):
    ''' assign : id asgn infix_expr
    '''
    p[0] = dict()

    if SCOPE.symbolTable.isPresent(p[1]['name']):
        emit(op="=",out=p[1]['name'],in1=p[3]['place'],in2=None)
    else:
        "assignment"
        #printp(p)



def p_or_expression(p):
    ''' or_expression : and_expression
                      | or_expression OR and_expression
    '''
    p[0] = dict()
    if len(p) == 4:
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op="||",out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    #printp(p)

def p_and_expression(p):
    ''' and_expression : bit_or_expression 
                       | and_expression AND bit_or_expression 
    '''
    p[0] = dict()
    if len(p) == 4:
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op="&&",out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    #printp(p)

def p_bit_or_expression(p):
    ''' bit_or_expression : xor_expression 
                          | bit_or_expression OR_BIT xor_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    #printp(p)

def p_xor_expression(p):
    ''' xor_expression : bit_and_expression
                       | xor_expression XOR bit_and_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    #printp(p)

def p_bit_and_expression(p):
    '''bit_and_expression : eq_expression
                      | bit_and_expression AND_BIT eq_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    #printp(p)

def p_eq_expression(p):
    '''eq_expression : comp_expression
                      | eq_expression EQ comp_expression
                      | eq_expression NEQ comp_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    elif (p.slice)[2].type == "EQ":
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op="==",out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif (p.slice)[2].type == "NEQ":
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op="!=",out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    #printp(p)


def p_comp_expression(p):
    '''comp_expression : shift_expression
                      | comp_expression LE shift_expression
                      | comp_expression LT shift_expression
                      | comp_expression GE shift_expression
                      | comp_expression GT shift_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    elif (p.slice)[2].type == 'LE':
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op='<=',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif (p.slice)[2].type == 'LT':
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op='<',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif (p.slice)[2].type == 'GE':
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op='>=',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif (p.slice)[2].type == 'GT':
        p[0]=dict()
        p[0]['place'] = newtmp()
        emit(op='>',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])

    
 #   #printp(p)
def p_shift_expression(p):
    '''shift_expression : add_expression
                      | shift_expression RSHIFT add_expression
                      | shift_expression LSHIFT add_expression
                      | shift_expression RRSHIFT add_expression
    '''
    p[0] = dict()
    if len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    #printp(p)

def p_add_expression(p):
    '''add_expression : mul_expression
                      | add_expression OP_ADD mul_expression
                      | add_expression OP_SUB  mul_expression
    '''
    p[0] = dict()
    if len(p) == 4:
        if (p.slice)[2].type =='OP_ADD':
            p[0]=dict()
            p[0]['place'] = newtmp()
            #print p[0]['place']
            emit(op='+',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
        else:
            p[0]=dict()
            p[0]['place'] = newtmp()
            emit(op='-',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
    elif len(p) == 2:
        p[0]=dict()
        p[0]['place'] == p[1]['place']

#    #printp(p)

def p_mul_expression(p):
    '''mul_expression : unary_expression
                      | mul_expression OP_MOD unary_expression
                      | mul_expression OP_MUL  unary_expression
                      | mul_expression OP_DIV  unary_expression
    '''
    p[0] = dict()
    if len(p) == 4:
        if (p.slice)[1].type =='OP_MOD':
            p[0]=dict()
            p[0]['place'] = newtmp()
            emit(op='%',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
        elif (p.slice)[1].type == 'OP_MUL':
            p[0]=dict()
            p[0]['place'] = newtmp()
            emit(op='*',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place'])
        elif (p.slice)[1].type == 'OP_DIV':
            p[0]=dict()
            p[0]['place'] = newtmp()
            emit(op='/',out=p[0]['place'],in1=p[1]['place'],in2=p[3]['place']) 
    elif len(p) == 2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
        ##printp(p)

def p_unary_expression(p):
    '''unary_expression : prefix_expr
                        | LPARAN infix_expr RPARAN
    '''
    p[0] = dict()
    if len(p) == 4:
        p[0]=dict()
        p[0]['place'] = p[2]['place']
    elif len(p)==2:
        p[0]=dict()
        p[0]['place'] = p[1]['place']
    ##printp(p)

#def p_cast_expression(p):
#    '''cast_expression : LPARAN basic_type RPARAN unary_expression
#
#    '''
#    #printp(p)


def p_types(p):
    ''' types : type comma_type_0
    '''
    p[0] = dict()
    #printp(p)

def p_comma_type_0(p):
    ''' comma_type_0 : epsilon
                     | comma_type_0 COMMA type
    '''
    p[0] = dict()
    #printp(p)

def p_type_args(p):
    ''' type_args : LSQRB types RSQRB
    '''
    p[0] = dict()
    #printp(p)

#def p_op(p):
#    ''' op : OR
#           | AND_BIT
#           | OR_BIT
#           | LT
#           | LE
#           | GT
#           | GE
#           | LSHIFT
#           | RSHIFT
#           | RRSHIFT
#           | OP_ADD
#           | OP_DIV
#           | OP_MUL
#           | OP_SUB
#           | OP_MOD
#    '''
#    #printp(p)

def p_asgn(p):
    ''' asgn : EQUALASGN
             | ADDASGN
             | SUBASGN
             | MULASGN
             | DIVASGN
             | MODASGN
             | LSHIFTASGN
             | RSHIFTASGN
             | ANDASGN
             | ORASGN
             | XORASGN
    '''
    p[0] = dict()
    #printp(p)

def p_basic_type(p):
    ''' basic_type : TYPE_INT
                   | TYPE_FLOAT
                   | TYPE_CHAR
                   | TYPE_STRING
                   | TYPE_BOOLEAN
                   | R_NULL
    '''
    p[0] = dict()
    #printp(p)

def p_id(p):
    ''' id : ID
           | ID LSQRB access RSQRB
    '''
    p[0] = dict()
    #printp(p)

def p_access(p):
    ''' access : ID access_0
    '''
    p[0] = dict()
    #printp(p)

def p_access_0(p):
    '''access_0 : COMMA access
                | epsilon
    '''
    p[0] = dict()
    #printp(p)

def p_literal(p):
    ''' literal : BOOL
                | INT
                | CHAR
                | STRING
                | FLOAT
    '''
    p[0] = dict()
    #printp(p)

def p_epsilon(p):
    ''' epsilon :

    '''
    pass
#    print(p)
def p_error(p):
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED+"Syntax error at '%s'" % p.value +CEND)
    print(CRED+"Syntax error at '%s'" % p.lineno + CEND)
    
parser = yacc.yacc()

f = open(sys.argv[1],"r")
code_full = f.read()
code_full=code_full+'\n'
f.close()

parser.parse(code_full)
