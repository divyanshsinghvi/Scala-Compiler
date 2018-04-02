import sys
import ply.yacc as yacc
import lexer
from symbolTable import SymbolTable
ST=SymbolTable()

def emit(op=None,out=None,in1=None,in2=None):
    print op,out,in1,in2

tokens = lexer.tokens
precedence = (
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

def evalArray(temp):
    if type(temp) == type({}) and 'arrAccess' in temp and temp['arrAccess']:
        t1 = ST.getTemp()
        emit(op='ldar',out=t1,in1=temp['place'],in2=temp['index'])
        r = {
                'place' : t1,
                'type' : temp['type']
                }
        return r
    return temp

def printp(p):
    for i in range(0,len(p)):
        print (p.slice)[i],

    print "\n",


def p_compilation_unit(p):
    '''compilation_unit : compilation_unit_0 top_stat_seq_0
    '''
    printp(p)
    
def p_compilation_unit_0(p):
    '''compilation_unit_0 : epsilon
                         | compilation_unit_0  R_PACKAGE qual_id semi  
    '''
    printp(p)


def p_top_stat_seq_0(p):
    '''top_stat_seq_0 :  epsilon
                    | top_stat_seq_0 top_stat semi
    '''
    printp(p)

def p_top_stat(p):
    '''top_stat : local_modifier_0 tmpl_def
                | import
    '''
    printp(p)

def p_local_modifier_0(p):
    '''local_modifier_0 : epsilon 
                        | local_modifier_0 local_modifier
    '''
    printp(p)

def p_tmpl_def(p):
    ''' tmpl_def : R_CLASS class_def
                 | R_OBJECT object_def        
    '''
    printp(p)

def p_class_def(p): 
    '''class_def : id class_param_clause class_template_opt
    '''
    printp(p)

def p_class_param_clause(p):
    '''class_param_clause : LPARAN  class_params  RPARAN
    '''
    printp(p)

def p_class_params(p) :  
    ''' class_params : epsilon
                     | class_param  class_param_0
    '''
    printp(p)

def p_class_param_0(p):
    ''' class_param_0 : epsilon
                      | COMMA class_param class_param_0
    '''
    printp(p)

def p_class_param(p):
    ''' class_param : val_var_1 id COLON type eq_expr_1
    '''
    printp(p)

def p_val_var_1(p):
    ''' val_var_1 : val_var 
                  | epsilon
    '''
    printp(p)

def p_val_var(p):
    ''' val_var : R_VAL 
                | R_VAR
    '''
    printp(p)
def p_eq_expr_1(p):
    ''' eq_expr_1 : EQUALASGN expr
                  | epsilon
    '''
    printp(p)
def p_class_template_opt(p):
    ''' class_template_opt : class_template_opt_2 template_body
    '''
    printp(p)
def p_class_template_opt_2(p):
    ''' class_template_opt_2 : R_EXTENDS id  class_template_opt_1
                             | epsilon

    '''
    printp(p)
def p_class_template_opt_1(p):
    '''class_template_opt_1 : LPARAN id com_id RPARAN
                            | epsilon
    '''
    printp(p)
def p_com_id(p):
    ''' com_id : epsilon
                | com_id COMMA id 
    '''
    printp(p)
def p_template_body(p):
    ''' template_body : BLOCKBEGIN template_body_0 BLOCKEND
    '''
    printp(p)

def p_template_body_0(p):
    ''' template_body_0 : epsilon
                        | template_body_0 template_stat semi
    '''
    printp(p)

def p_template_stat(p):
    ''' template_stat : block_stat
                      | modifier_0 def
                      | modifier_0 dcl
    '''
    printp(p)

def p_modifier_0(p):
    ''' modifier_0 : modifier
                    | modifier_0 modifier
    '''
    printp(p)
def p_import(p):
    ''' import : R_IMPORT import_expr import_0
    '''
    printp(p)

def p_import_0(p):
    ''' import_0 : COMMA import_expr import_0
                 | epsilon

    '''
    printp(p)

def p_import_expr(p):
    '''import_expr : path
    '''
    printp(p)
def p_def(p):
    ''' def : path_var_def 
            | R_DEF fun_def 
            | tmpl_def
    '''
    printp(p)
def p_path_var_def(p):
    ''' path_var_def : R_VAR var_def
                    | R_VAL val_def
    '''
    printp(p)
def p_var_def(p):
    ''' var_def : id COLON type EQUALASGN val_var_init

    '''
    print p[5]
    ST.addEntry(p[1],p[1],p[3]['type']) 
    if('isArray' in p[5].keys() and p[5]['isArray']):
        print "oops array" 
        #emit('array','a','n')
    else:
        emit('=',p[5]['place'],p[1])


    #printp(p)

def p_array_size(p):
    ''' array_size : LPARAN ints RPARAN                           
    '''
    p[0] = dict()
    p[0]['place'] = p[2] 
    #printp(p)
def p_ints(p):
    ''' ints : INT
             | COMMA ints
    '''
    if(len(p)==2):
        p[0] = p[1]
    # Array[Char](10,3,4)

def p_val_def(p):
    ''' val_def : id COLON type EQUALASGN val_var_init
    '''
    printp(p)

def p_val_var_init(p):
    '''val_var_init : array_init
                | infix_expr
    '''
    if p.slice[1].type == 'infix_expr':
        p[0]=p[1]
    else:
        print "chapu"
        p[0] = {
                'isArray' : True
                }

    #printp(p)

def p_array_init(p):
    ''' array_init : BLOCKBEGIN epsilon BLOCKEND
                   | BLOCKBEGIN array_init_0 BLOCKEND
    '''
    printp(p)

def p_array_init_0(p):
    '''array_init_0 : val_var_init 
                    | array_init_0 COMMA val_var_init
    '''
    printp(p)

#some ambiguity here ???
def p_fun_def(p):
    ''' fun_def : fun_sig col_type_1 EQUALASGN BLOCKBEGIN block BLOCKEND FunMark1
    '''
    printp(p)

def p_FunMark1(p):
    ''' FunMark1 : epsilon
    '''
    #if(p[-5]==False):
    #    ST.function[p[-6][1]]["return"]=False
    #if(p[-6][1]!="main@0"):
    #    emit("freturn")

def p_col_type_1(p) :
    ''' col_type_1 : COLON type
                    | epsilon
    '''
    #if(len(p)==2):
    #    p[0]=False
    #printp(p)

def p_fun_sig(p):
    ''' fun_sig : id param_clause
    '''
    #p[0] = ["func"]+[p[1]]+p[2]
    #arg = len(p[2])
    #name = p[1]+"@"+str(arg)
    #p[0][1]=name
    #if name in ST.function:
    #    error("Error: function with same name and same number of arguments already defined.")
    #else:
    #    ST.function[name]={
    #            "name":p[1],
    #            "args":arg,
    #            "return":True
    #        }
    #    emit("flabel",p[1])
    #printp(p)

def p_param_clause(p):
    ''' param_clause : LPARAN  RPARAN
                      | LPARAN params RPARAN
    '''
    #if(len(p)==2):
    #    p[0]=[]
    #else:
    #    p[0]=p[2]
    #printp(p)

def p_params(p):
    ''' params : param
               | params COMMA param
    '''
    #if(len(p)==2):
    #    l = []
    #    l = l + p[1]["place"] + [p[1]["type"]]
    #    p[0]=[l]
    #else:
    #    l = []
    #    l = l + p[3]["place"] + [p[3]["type"]]
    #    p[0]=p[1] + [l]
    #printp(p)

def p_param(p):
    ''' param : id COLON param_type eq_expr 
              | R_VAR id COLON param_type eq_expr
              | R_VAL id COLON param_type eq_expr
    '''
    #if(len(p)==5):
    #    p[0]={
    #            "type" : p[3]["type"],
    #            "place" : p[1]
    #        }
    #else:
    #    p[0]={
    #            "type" : p[4]["type"],
    #            "place" : p[2]
    #        }
    #printp(p)
def p_eq_expr(p):
    ''' eq_expr : epsilon
                | EQUALASGN expr
    '''
    printp(p)
def p_param_type(p):
    ''' param_type : type
    '''
    p[0]=p[1]
    printp(p)
def p_dcl(p):
    '''dcl  :   R_VAL val_dcl
            |   R_VAR var_dcl
            |   R_DEF fun_dcl'''
    printp(p)

def p_val_dcl(p):
    '''val_dcl   :   id COLON type val_dcl_0'''
    #printp(p)

    printp(p)
def p_val_dcl_0(p):
    '''val_dcl_0    :   epsilon
                    |   COMMA val_dcl'''
    printp(p)

def p_var_dcl(p):
    '''var_dcl  :   id COLON type
    '''
    ST.addEntry(p[1],p[1],p[3]['type'])

    #printp(p)

#def p_var_dcl_0(p):
#    '''var_dcl_0    :   epsilon
#                    |   COMMA var_dcl'''
#    printp(p)

def p_fun_dcl(p):
    '''fun_dcl  :   fun_sig COLON type 
                |   fun_sig'''
    printp(p)

#def fun_dcl_1(p):
#    '''fun_dcl_0    :   COLON type fun_dcl_0
#                    |   epsilon'''

def p_modifier(p):
    '''modifier :   local_modifier
                |   access_modifier
                |   R_OVERRIDE'''
    printp(p)

def p_local_modifier(p):
    '''local_modifier   :   R_FINAL
                        |   R_ABSTRACT'''
    printp(p)

def p_access_modifier(p):
    '''access_modifier  :   R_PRIVATE
                        |   R_PROTECTED
                        |   R_PUBLIC'''
    printp(p)

def p_path(p):
    '''path :   id
            |   R_THIS
            |   id DOT path
            |   R_SUPER DOT path
            '''
    p[0] = p[1]
    printp(p)

#def path_0(p):
#    '''path_0   :   id DOT path_0
#                |   epsilon'''

def p_block_stat(p):
    '''block_stat   :   def
                    |   dcl
                    |   local_modifier_0 tmpl_def
                    |   expr'''
    #printp(p)
                    
def p_block(p):
    '''block    :   epsilon
                |   block_stat semi block'''
    printp(p)

#def p_stable_id(p):
#    '''stable_id :   id
#                 |   path DOT id
#                 |   id DOT R_SUPER DOT id
#                 |   R_SUPER DOT id'''
#    printp(p)


def p_simple_expr(p):
    '''simple_expr  :   R_NEW class_template
                    |   simple_expr1'''
    if len(p) == 2:
        p[0] = p[1]
    printp(p)
 #                   |   block

def p_class_template(p):
    '''class_template   :   id class_template_1'''
    printp(p)

def p_class_template_1(p):
    '''class_template_1 :   LPARAN id  class_template_0 RPARAN
                        |   LPARAN literal class_template_0 RPARAN
                        |   epsilon '''
    printp(p)

def p_class_template_0(p):
    '''class_template_0 :   COMMA id class_template_0
                        |   COMMA literal class_template_0
                        |   epsilon'''
    printp(p)

#def p_block_expr(p):
#    '''block_expr   :   block'''
#    printp(p)

def p_simple_expr1(p):
    '''simple_expr1 :   literal
                    |   ID LSQRB access RSQRB
                    |   path
                    |   LPARAN exprs_1 RPARAN
                    |   simple_expr DOT id
                    |   simple_expr1 argument_exprs'''
    p[0] = dict()

    if p.slice[1].type == 'literal':
        p[0] = p[1]
    elif p.slice[1].type == 'path':
        p[0] = {
                'place' : p[1]
                }
    elif len(p)==5:
        p[0]['idVal'] = p[1]
        p[0]['isArrayAccess'] = True
        p[0]['type'] = ST.getAttribute(p[0]['idVal'],'type')
        p[0]['place'] = ST.getAttribute(p[0]['idVal'],'place')
        p[0]['index_place'] = p[3]['place']
        del p[0]['idVal'] 
    #Check
    elif p.slice[1]=='LPARAN':
        p[0] = p[2]
    elif p.slice[2] == 'argument_exprs':
        x = p[1]['idVal'].split('.')
        if(p[1]['idVal'] == 'PrintInt'):
            emit('PrintInt',p[2]['place'])
        else:
            emit('call',None,p[1]['idVal'],1)
    
    #printp(p)
    #                |   simple_expr type_args

#def p_exprs_1(p):
#    '''exprs_1  :   exprs
#                |   epsilon'''
#    printp(p)

def p_prefix_expr(p):
    '''prefix_expr  :   simple_expr
                    |   OP_SUB simple_expr
                    |   OP_ADD simple_expr
                    |   OP_NOT simple_expr'''
    if len(p) ==2 :
        p[0]=p[1]

    printp(p)

def p_type(p):                      # look at <T>
    ''' type : basic_type
             | array_type
             | id
    '''
    #print p[1]
    if p.slice[1].type == 'basic_type':
        p[0] = {
                'type' : p[1]['idVal'].upper()
                }
    elif p.slice[1].type == 'array_type':
        p[0] = {
                'type' : p[1]['type']
                }
    else:
        p[0] = {
                'type' : p[1].upper()
                }
    #printp(p)

def p_array_type(p):
    ''' array_type : TYPE_ARRAY LSQRB type RSQRB array_size
    '''
    p[0] = {
            'type' : p[3]['type'],
            'place' : p[5]['place'],
            'isarray' :  True
            
            }
    #printp(p)

#def p_simple_type(p):
#    ''' simple_type : type
#                    | LPARAN type RPARAN
#    '''
#    printp(p)

def p_semi(p):
    ''' semi : SEMICOLON
    '''
    printp(p)

def p_qual_id(p):
    ''' qual_id : id
                | qual_id DOT id
    '''
    if(len(p)==2):
        p[0]={
                'idVal' : p[1],
                'var' : False
                }
    else:
        p[0] = {
                'idVal' : p[1]['idVal']+"." +p[3]
                }

    #printp(p)

#def p_dot_id_0(p):
#    ''' dot_id_0 : epsilon
#             | dot_id_0 DOT id
#    '''
#    printp(p)

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

def p_for_logic(p):
    ''' for_logic : LPARAN for_init semi infix_expr semi for_upd
                  | LPARAN for_init semi epsilon semi for_upd
    '''
    printp(p)

def p_for_init(p):
    ''' for_init : epsilon
                 | var_def for_inits
                 | var_dcl for_inits
                 | infix_expr for_inits
    '''
    printp(p)

def p_for_inits(p):
    '''for_inits : COMMA for_inits
                 | for_init

    '''

def p_for_upd(p):           # to be done later, the for case
    ''' for_upd : RPARAN
                   | infix_expr RPARAN
    '''
    printp(p)

#def p_semi_for_logic_1(p):
#    ''' semi_for_logic_1 : semi for_logic
#| epsilon
#    '''
#    printp(p)

def p_switch_labels(p):
    ''' switch_labels : R_CASE literal COLON
                      | R_DEFAULT COLON
    '''
    printp(p)

def p_switch_block_statements(p):
    ''' switch_block_statements : switch_labels_0 BLOCKBEGIN block BLOCKEND semi
    '''
    printp(p)

def p_switch_labels_0(p):
    ''' switch_labels_0 : epsilon
                        | switch_labels_0 switch_labels
    '''
    printp(p)

def p_switch_block(p):
    ''' switch_block : BLOCKBEGIN switch_block_statements_0 BLOCKEND
    '''
    printp(p)

def p_switch_block_statements_0(p):
    ''' switch_block_statements_0 : epsilon
                                 | switch_block_statements_0 switch_block_statements
    '''
    printp(p)

#def p_switch_labels_1(p):
#    ''' switch_labels_1 : switch_labels
#                        | epsilon
#    '''
#    printp(p)

def p_expr(p):
    ''' expr : R_IF LPARAN postfix_expr RPARAN BLOCKBEGIN block BLOCKEND expression1
              | R_WHILE LPARAN postfix_expr RPARAN BLOCKBEGIN block BLOCKEND
              | R_TRY BLOCKBEGIN block BLOCKEND catch_clause_1 expression2
              | R_DO BLOCKBEGIN block BLOCKEND R_WHILE LPARAN postfix_expr RPARAN
              | R_FOR  for_logic  BLOCKBEGIN block BLOCKEND
              | R_RETURN expr
              | R_BREAK
              | R_CONTINUE
              | postfix_expr
              | R_SWITCH LPARAN expr RPARAN switch_block
    '''
              #| R_ARRAY LPARAN literal literal_0 RPARAN
    printp(p)

def p_expression1(p):
    ''' expression1 : R_ELSE BLOCKBEGIN block BLOCKEND
                    | epsilon
    '''
    printp(p)

def p_expression2(p):
    ''' expression2 : R_FINALLY BLOCKBEGIN block BLOCKEND
                    | epsilon
    '''
    printp(p)

#def p_literal_0(p):
#    ''' literal_0 : epsilon
#                  | literal_0 COMMA literal
#    '''
#    printp(p)


def p_argument_exprs(p):
    ''' argument_exprs : LPARAN exprs_1 RPARAN
    '''
    p[0] = p[2]
    #printp(p)


def p_exprs_1(p):
    ''' exprs_1 : expr
                | exprs_1 COMMA expr
    '''
    if(len(p)==2):
        p[0]=p[1]
    #printp(p)

def p_postfix_expr(p):
    ''' postfix_expr : infix_expr id_1
                     | infix_expr
    '''
    printp(p)

def p_id_1(p):
    ''' id_1 : id
             | id_1 id
    '''
    printp(p)

#def p_infix_expr(p):
#    ''' infix_expr : infix_expr op infix_expr
#                   | infix_expr asgn infix_expr
#                   | prefix_expr
#    '''
#    printp(p)

def p_infix_expr(p):
    ''' infix_expr : assign
                   | or_expression
    '''
    print "infix ininnnnnnnn"
    p[0] = p[1]
    printp(p)

def p_assign(p):
    ''' assign : simple_expr1  asgn infix_expr
    '''
    temp = ST.getTemp()
    p[0] = {
            'place' : temp,
            'isarray' : False,
            'type': 'Not defined'
            }
    if p[2] == '=':
        p[3]=evalArray(p[3])
        if type(temp) == type({}) and 'arrAccess' in temp and temp['arrAccess']:
            emit(op='star',out=p[1]['place'],in1=p[1]['index'],in2=p[3]['place'])
        else:
            emit(op='=',out=p[1]['place'],in1=p[3]['place'])
    ##Check
    printp(p)

def p_or_expression(p):
    ''' or_expression : and_expression
                      | or_expression OR and_expression
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op='||',out=temp,in1=p[1]['place'],in2=p[3]['place'])
    #print "-----"
    #print p[0]
    #printp(p)

def p_and_expression(p):
    ''' and_expression : bit_or_expression 
                       | and_expression AND bit_or_expression 
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op='&&',out=temp,in1=p[1]['place'],in2=p[3]['place'])
    printp(p)

def p_bit_or_expression(p):
    ''' bit_or_expression : xor_expression 
                          | bit_or_expression OR_BIT xor_expression
    '''
    if len(p)==2:
        p[0] = p[1]
    printp(p)

def p_xor_expression(p):
    ''' xor_expression : bit_and_expression
                       | xor_expression XOR bit_and_expression
    '''
    if len(p)==2:
        p[0] = p[1]
    printp(p)

def p_bit_and_expression(p):
    '''bit_and_expression : eq_expression
                      | bit_and_expression AND_BIT eq_expression
    '''
    if len(p)==2:
        p[0] = p[1]
    #printp(p)

def p_eq_expression(p):
    '''eq_expression : comp_expression
                      | eq_expression EQ comp_expression
                      | eq_expression NEQ comp_expression
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op=p[2],out=temp,in1=p[1]['place'],in2=p[3]['place'])
    #printp(p)


def p_comp_expression(p):
    '''comp_expression : shift_expression
                      | comp_expression LE shift_expression
                      | comp_expression LT shift_expression
                      | comp_expression GE shift_expression
                      | comp_expression GT shift_expression
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        print "============="
        print p[1]
        print p[3]
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op=p[2],out=temp,in1=p[1]['place'],in2=p[3]['place'])
    printp(p)
def p_shift_expression(p):
    '''shift_expression : add_expression
                      | shift_expression RSHIFT add_expression
                      | shift_expression LSHIFT add_expression
                      | shift_expression RRSHIFT add_expression
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op=p[2],out=temp,in1=p[1]['place'],in2=p[3]['place'])
    printp(p)

def p_add_expression(p):
    '''add_expression : mul_expression
                      | add_expression OP_ADD mul_expression
                      | add_expression OP_SUB  mul_expression
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        print "ds chapu"
        print p[1]
        print p[3]
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op=p[2],out=temp,in1=p[1]['place'],in2=p[3]['place'])
    printp(p)

def p_mul_expression(p):
    '''mul_expression : unary_expression
                      | mul_expression OP_MOD unary_expression
                      | mul_expression OP_MUL  unary_expression
                      | mul_expression OP_DIV  unary_expression
    '''
    print p[1]
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op=p[2],out=temp,in1=p[1]['place'],in2=p[3]['place'])
    printp(p)

def p_unary_expression(p):
    '''unary_expression : prefix_expr
                        | LPARAN infix_expr RPARAN
    '''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = p[2]
#    printp(p)

#def p_cast_expression(p):
#    '''cast_expression : LPARAN basic_type RPARAN unary_expression
#
#    '''
#    printp(p)


#def p_types(p):
#    ''' types : type
#              | types COMMA type
#    '''
#    printp(p)

#def p_type_args(p):
#    ''' type_args : LSQRB types RSQRB
#    '''
#    printp(p)

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
#    printp(p)

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
    print p[1]
    p[0] = p[1]
    printp(p)

def p_basic_type(p):
    ''' basic_type : TYPE_INT
                   | TYPE_FLOAT
                   | TYPE_CHAR
                   | TYPE_STRING
                   | TYPE_BOOLEAN
                   | R_NULL
    '''
    
    #CRED = '\033[91m'
    #CEND = '\033[0m'
    #print(CRED+p[1]+CEND)
    p[0] = {
            'idVal': p[1],
            'type' : p[1].upper()
            }
    #printp(p)

def p_id(p):
    ''' id : ID
    '''
    if len(p)==2:
        p[0]=p[1]
        
    printp(p)

def p_access(p):
    ''' access : ID
               | INT
               | access COMMA ID
               | access  COMMA INT
    '''
    #printp(p)

def p_literal(p):
    ''' literal : BOOL
                | INT
                | CHAR
                | STRING
                | FLOAT
    '''
    p[0] = {
            'type' : p.slice[1].type,
            'place' : p[1]
                }

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
