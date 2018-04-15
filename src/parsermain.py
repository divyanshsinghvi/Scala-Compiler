import sys
import ply.yacc as yacc
import lexer
#from globalvar import *
import pickle
from globalOther import ST
#ST=SymbolTable()
#global ST
#ST.newScope()
ST.addFunc('println')
ST.endFunc()
ST.addFunc('readInt')
ST.endFunc()
#ST.endScope()
x=1
def newLabel():
    global x
    x=x+1
    return "label"+str(x)

def is_number(var):
    try:
        int(var)
        return True
    except Exception:
        return False

def check(var,op):
    if is_number(var) and op!="=":
        t = ST.getTemp()
        l=['=',t,var]
        myList = ','.join(map(str, l)) 
        print myList
        return t
    else:
        return var

def emit(op=None,out=None,in1=None,in2=None):
    CRED = '\033[91m'
    CEND = '\033[0m'
   # print(CRED+"")
    l = []
    if op != None:
        l += [op]
    if out != None:
        t=check(out,op)
        l += [t]
    if in1 != None:
        t=check(in1,op)
        l += [t]
    if in2 != None:
        t=check(in2,op)
        l += [t]
    myList = ','.join(map(str, l)) 
    print myList
    #print(""+CEND)

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
    if temp['type'] == 'Array':
        t1 = ST.getTemp()
        #print "I am here"
        emit(op='ldar',out=t1,in1=temp['place'],in2=temp['index'])
        r = {
                'place' : t1,
                'type' : 'Array'
                }
        return r
    return temp

def makeIndex(size,place):
    t=ST.getTemp()
    t1=ST.getTemp()
    old=0
    old1=0
    for i in range(0,len(place)-1):
        for j in range(i+1,len(size)):
            if(j==i+1 and len(size)>1):
                t=ST.getTemp()
                emit("*",t,place[i]['place'],size[j])
                old=t
            elif(len(size)>1):
                t = ST.getTemp()
                emit("*",t,old,size[j])
                old=t
        t1=ST.getTemp()
        emit("+",t1,old1,t)
        old1=t1
    emit("+",t1,old1,place[len(place)-1]["place"])
    return t1

def printp(p):
    #for i in range(0,len(p)):
    #    print (p.slice)[i],
    #print "\n",
    a=2

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
    #if('isArray' in p[5].keys() and p[5]['isArray']):
    if type(p[5]) == type({}) and 'isArray' in p[5] and p[5]['isArray']:
        ST.addVar(p[1],p[1],'Array',p[3]['size'],p[3]['type'])
        ST.addAttribute(p[1],'typeArray',p[3]['type'])
        size=1
        for x in p[3]["size"]:
            size*=x
        emit('array',p[1],size)
        i = 0 
        for d in p[5]['values']:
            emit('star',p[1],i,d['place'])
            i+=1
       # emit('array',p[],'n')
    else:
        ST.addVar(p[1],p[1],p[3]['type'])
	emit('=',in1=p[5]['place'],out=p[1])


    printp(p)

def p_array_size(p):
    ''' array_size : LPARAN ints RPARAN                           
    '''
    p[0] = dict()
    p[0]['size'] = p[2] 
    printp(p)
def p_ints(p):
    ''' ints : INT
             | INT COMMA ints
    '''
    if(len(p)==2):
        p[0] = [p[1]]
    else:
        p[0]=[p[1]]+p[3]
    # Array[Char](10,3,4)
    printp(p)
def p_val_def(p):
    ''' val_def : id COLON type EQUALASGN val_var_init
    '''
    p[0]=p[5]
    printp(p)

def p_val_var_init(p):
    '''val_var_init : array_init
                | infix_expr
    '''
    p[0]={}
    if p.slice[1].type == 'infix_expr':
        p[0]=p[1]
    else:
        p[0]['values'] = p[1]
        p[0]['isArray'] = True

    printp(p)

def p_array_init(p):
    ''' array_init : BLOCKBEGIN epsilon BLOCKEND
                   | BLOCKBEGIN array_init_0 BLOCKEND
    '''
    if p.slice[2].type == "epsilon":
        p[0]=[]
    else:
        p[0]=p[2]
    printp(p)

def p_array_init_0(p):
    '''array_init_0 : val_var_init 
                    | array_init_0 COMMA val_var_init
    '''
    if len(p) == 4:
        p[0] = p[1]+[p[3]]
    else:
        p[0] = [p[1]]
    printp(p)

#some ambiguity here ???
def p_fun_def(p):
    ''' fun_def : fun_sig col_type_1 FunMark1 EQUALASGN BLOCKBEGIN block BLOCKEND FunMark2
    '''
    printp(p)
    

def p_FunMark1(p):
    ''' FunMark1 : epsilon
    '''
    if p[-2][1] in ST.SymbolTable[ST.currScope]["function"].keys():
        error("Error: function with same name and same number of arguments already defined.")
    else:
        if(len(p[-2])>2):
            ST.addFunc(p[-2][1],p[-2][2:])
        else:
            ST.addFunc(p[-2][1])
        ST.setRType(p[-1])
    printp(p)
def p_FunMark2(p):
    ''' FunMark2 : epsilon
    '''
    ST.endFunc()
    #if(p[-5]==False):
    #    ST.function[p[-6][1]]["return"]=False
    #if(p[-6][1]!="main@0"):
    #    emit("freturn")
    printp(p)
def p_col_type_1(p) :
    ''' col_type_1 : COLON type
                    | epsilon
    '''
    if(len(p)==2):
        p[0]="void"
    else:
        p[0]=p[2]
    printp(p)

def p_fun_sig(p):           # function is named id@no.of args
    ''' fun_sig : id param_clause  
    '''
    p[0] = ["func"]+[p[1]]+p[2]
    arg = len(p[2])
    name = p[1]+"@"+str(arg)
    p[0][1]=name
    ST.function.append(p[1])
    #if name in ST.function:
    #    error("Error: function with same name and same number of arguments already defined.")
    #else:
    #    ST.function[name]={
    #            "name":p[1],
    #            "args":arg,
    #            "return":True
    #        }
    emit("flabel",p[1])
    printp(p)

def p_param_clause(p):
    ''' param_clause : LPARAN  RPARAN
                      | LPARAN params RPARAN
    '''
    if(len(p)==3):
        p[0]=[]
    else:
        p[0]=p[2]
    printp(p)

def p_params(p):
    ''' params : param
               | params COMMA param
    '''
    if(len(p)==2):
        l = []
        l = l + [p[1]["place"]] + [p[1]["type"]]
        p[0]=[l]
    else:
        l = []
        l = l + [p[3]["place"]] + [p[3]["type"]]
        p[0]=p[1] + [l]
    printp(p)

def p_param(p):
    ''' param : R_VAR var_def
              | var_def
              | var_dcl
              | R_VAR var_dcl
    '''
    if(len(p)==2):
        p[0]=p[1]
    else:
        p[0]=p[2]
    printp(p)

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
    printp(p)
def p_val_dcl_0(p):
    '''val_dcl_0    :   epsilon
                    |   COMMA val_dcl'''
    printp(p)

def p_var_dcl(p):
    '''var_dcl  :   id COLON type
    '''
    ST.addVar(p[1],p[1],p[3]['type'])
    print p[1]
    p[0] = {}
    p[0]['place'] = p[1]
    p[0]['type']= p[3]['type']
    printp(p)

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
            |   path DOT id
            |   R_SUPER DOT path
            '''
   # ST.printSymbolTable(ST,1)
    if(p.slice[1].type == 'id'):
        if p[1] not in ST.function:
            p[0] = ST.getId(p[1])
        else:
            p[0]=ST.getFunc(p[1])
    printp(p)

#def path_0(p):
#    '''path_0   :   id DOT path_0
#                |   epsilon'''

def p_block_stat(p):
    '''block_stat   :   def
                    |   dcl
                    |   local_modifier_0 tmpl_def
                    |   expr'''
    printp(p)
                    
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
        p[0] = p[1]
    elif len(p)==5:
        p[0]['idVal'] = p[1]
        p[0]['arrAccess'] = True
        p[0]['type'] = ST.getAttribute(p[0]['idVal'],'type')
        p[0]['place'] = p[1]
        size=ST.getId(p[1])['size'] #a,b,c size
        place=p[3]          # i,j,k access index
        temp=makeIndex(size,place)
        p[0]['index'] = temp
        #p[0]['index'] = p[3]['place']
    elif p.slice[1].type =='LPARAN':
        p[0] = p[2]
    elif p.slice[2].type == 'argument_exprs':
 #       x = p[1]['idVal'].split('.')
        if(p[1]['name'] == 'println'):
            if(is_number(p[2][0]['place'])):
                temp=ST.getTemp()
                emit("=",temp,p[2][0]['place'])
                emit('printInt',temp)
            else:
                emit('printInt',p[2][0]['place'])
        elif(p[1]['name'] == 'readInt'):
            emit('scanInt',p[2][0]['place'])
        else:
            temp=ST.getTemp()
            print("=,"+temp+","+str(len(p[2])))
            l=[]
            for i in p[2]:
                if(is_number(i['place'])):
                    temp=ST.getTemp()
                    print("=,"+temp+","+str(i['place']))
                    l.append(temp)
                else:
                    l.append(i['place'])
            for i in reversed(l):
                emit("par",None,i)
            name=p[1]["place"]+"@"+str(len(p[2]))
            rtype = ST.getRType(name)
            if(rtype!="void"):
                temp1 = ST.getTemp()
                p[0]["place"]=temp1
                emit("fcall",temp1,p[1]["place"],temp)
            else:
                emit('call',None,p[1]['place'],temp)
    printp(p)

def p_prefix_expr(p):
    '''prefix_expr  :   simple_expr
                    |   OP_SUB infix_expr
                    |   OP_ADD infix_expr
                    |   OP_NOT infix_expr'''
    if len(p) ==2 :
        p[0]=p[1]
    else:
        if p.slice[1].type == 'OP_ADD':
            p[0]=p[2]
        elif p.slice[1].type == 'OP_SUB':
            temp=ST.getTemp()
            emit("-",temp,0,p[2]['place'])
            p[0]={}
            p[0]['type']=p[2]['type']
            p[0]['place']=temp
            p[0]['idVal']=temp
        else:
            temp=ST.getTemp()
            emit("!",temp,p[2]['place'])
            p[0]={}
            p[0]['type']=p[2]['type']
            p[0]['place']=temp
            p[0]['idVal']=temp

    printp(p)

def p_type(p):                      # look at <T>
    ''' type : basic_type
             | array_type
             | id
    '''
    if p.slice[1].type == 'basic_type':
        p[0] = {
                'type' : p[1]['idVal'].upper()
                }
    elif p.slice[1].type == 'array_type':
        p[0] = p[1]
    else:
        p[0] = {
                'type' : p[1].upper()
                }
    printp(p)
def p_array_type(p):
    ''' array_type : TYPE_ARRAY LSQRB type RSQRB array_size
    '''

    p[0] = {
            'type' : p[3]['type'],
           # 'place' : p[5]['place'],
            'isarray' :  True,
            'size' : p[5]['size']    
            }
    printp(p)

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

def p_for_logic(p):
    ''' for_logic : LPARAN f_scope_mark for_init semi f_mark1 infix_expr f_mark2 semi for_upd f_mark4
    '''
    p[0] = p[7]
    #Check Scope
    printp(p)

def p_for_init(p):
    ''' for_init : epsilon
                 | path_var_def for_inits
                 | var_dcl for_inits
                 | infix_expr for_inits
    '''
    printp(p)

def p_for_inits(p):
    '''for_inits : COMMA for_inits
                 | for_init

    '''
    printp(p)

def p_for_upd(p):           # to be done later, the for case
    ''' for_upd : RPARAN
                   | infix_expr RPARAN
    '''
    printp(p)


def p_switch_labels(p):
    ''' switch_labels : R_CASE literal COLON
                      | R_DEFAULT COLON
    '''
    if p.slice[1].type == 'R_CASE':
        l1=newLabel()
        emit(op='label',out=l1)
        p[0] = {}
        p[0]['label'] = l1
        p[0]['place'] = p[2]['place']
    printp(p)

def p_switch_block_statements(p):
    ''' switch_block_statements : switch_labels BLOCKBEGIN block BLOCKEND semi
    '''
    p[0] = p[1]
    printp(p)

#def p_switch_labels_0(p):
#    ''' switch_labels_0 : switch_labels
#                        | switch_labels_0 switch_labels
#    '''
#    printp(p)

def p_switch_block(p):
    ''' switch_block : BLOCKBEGIN s_mark1 switch_block_statements_0 BLOCKEND
    '''
    emit('goto',p[2]['label'][1])
    emit('label',p[2]['label'][0])
    for d in p[3]:
        temp =ST.getTemp()
        emit(op='==',out=temp,in1=d['place'],in2=p[2]['idVal']['place'])
        emit('if',d['label'],temp)
    emit('label',p[2]['label'][1])
    ST.endScope()
    printp(p)

def p_switch_block_statements_0(p):
    ''' switch_block_statements_0 : switch_block_statements
                                 | switch_block_statements_0 switch_block_statements
    '''

    if len(p)==2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]+[p[2]]
    printp(p)


def p_expr(p):
    ''' expr : R_IF LPARAN postfix_expr  RPARAN BLOCKBEGIN if_mark1 block BLOCKEND expression1
              | R_WHILE LPARAN WhMark1 postfix_expr RPARAN WhMark2 BLOCKBEGIN block WhMark3  BLOCKEND
              | R_TRY BLOCKBEGIN block BLOCKEND catch_clause_1 expression2
              | R_DO BLOCKBEGIN block BLOCKEND R_WHILE LPARAN postfix_expr RPARAN
              | R_FOR for_logic  BLOCKBEGIN block f_mark3 BLOCKEND
              | R_RETURN postfix_expr
              | R_RETURN
              | R_BREAK
              | R_CONTINUE
              | postfix_expr
              | R_SWITCH LPARAN postfix_expr RPARAN switch_block
    '''
              #| R_ARRAY LPARAN literal literal_0 RPARAN
    if(p[1]=="break"):
        emit("goto",ST.stackend[-1])
    if(p[1]=="continue"):
        emit("goto",ST.stackbegin[-1])
    if(p[1]=="return" and len(p)==2):
        emit("return")
    if(p[1]=="return" and len(p)==3):
        emit("freturn",p[2]["place"])  # freturn,-,x,- , won't be able to get x easily in this case
    printp(p)

def p_s_mark1(p):
    '''s_mark1 : epsilon
    '''
    ST.newScope()
    test = newLabel()
    exit=newLabel()
    emit('goto',test)
    ST.stackbegin.append(test)
    ST.stackend.append(exit)
    p[0] = {   'label' : [test,exit], 
                'idVal' :    p[-3]
                }
    printp(p)

def p_f_scope_mark(p):
    '''f_scope_mark : epsilon
    '''
    ST.newScope()
    printp(p)

def p_f_mark1(p):
    ''' f_mark1 : epsilon
    '''
    l1 = newLabel()
    l2 = newLabel()
    l3 = newLabel()
    l4 = newLabel()
    ST.stackbegin.append(l2)
    ST.stackend.append(l4)
    emit(op='label',out=l1) #emit label 1 
    p[0]=[l1,l2,l3,l4]
    
    printp(p)
def p_f_mark2(p):
    ''' f_mark2 : epsilon
    '''
    emit(op='if',in1=p[-1]['place'],out=p[-2][2]) #if true goto l2 
    emit(op='goto',out=p[-2][3]) #goto exit l3
    emit(op='label',out=p[-2][1],) # emit label l2
    p[0] = [p[-2][0],p[-2][1],p[-2][2],p[-2][3]]
    printp(p)

def p_f_mark3(p):
    ''' f_mark3 : epsilon
    '''
    emit(op='goto',out=p[-3][1]) #goto l2
    emit(op='label',out=p[-3][3]) #exit label
    ST.endScope()
    ST.stackbegin.pop()
    ST.stackend.pop()
    printp(p)

def p_f_mark4(p):
    '''f_mark4 : epsilon
    '''
    emit('goto',p[-5][0])
    emit('label',p[-5][2])
    printp(p)


def p_WhMark1(p):
    '''WhMark1 : '''
    l1 = newLabel()
    l2 = newLabel()
    l3 = newLabel()
    ST.stackbegin.append(l1)
    ST.stackend.append(l3)
    ST.newScope()
    emit(op='label',out=l1) #emit label 1 
    p[0]=[l1,l2,l3]
    printp(p)

def p_WhMark2(p):
    '''WhMark2 : '''
    emit(op='if',in1=p[-2]['place'],out=p[-3][1]) #if true goto l2 
    emit(op='goto',out=p[-3][2]) #goto exit l3
    emit(op='label',out=p[-3][1],) # emit label l2
    printp(p)

def p_WhMark3(p):
    '''WhMark3 : '''
    emit(op='goto',out=p[-6][0]) #goto l1
    emit(op='label',out=p[-6][2]) #exit label
    ST.endScope()
    ST.stackbegin.pop()
    ST.stackend.pop()
    printp(p)


def p_expression1(p):
    ''' expression1 : R_ELSE if_mark3 BLOCKBEGIN block BLOCKEND if_mark4
                    | if_mark2
    '''
    printp(p)


def p_if_mark1(p):
    '''if_mark1 : epsilon
    '''
    p[0]={}
    l1 = newLabel()
    l2 = newLabel()
    emit('if',l1,p[-3]['place'])
    emit('goto',l2)
    emit('label',l1)
    ST.newScope()
    p[0]['label']=[l1,l2]
    printp(p)

def p_if_mark2(p):
    '''if_mark2 : epsilon
    '''
    ST.endScope()
    emit('label',p[-3]['label'][1])
    printp(p)

def p_if_mark3(p):
    '''if_mark3 : epsilon
    '''
    p[0]={}
    l3 = newLabel()
    emit('goto',l3)
    emit('label',p[-4]['label'][1])
    p[0]['label']=[l3]
    printp(p)

def p_if_mark4(p):
    '''if_mark4 : epsilon
    '''
    ST.endScope()
    emit('label',p[-4]['label'][0])
    printp(p)



def p_expression2(p):
    ''' expression2 : R_FINALLY BLOCKBEGIN block BLOCKEND
                    | epsilon
    '''
    printp(p)



def p_argument_exprs(p):
    ''' argument_exprs : LPARAN exprs_1 RPARAN
    '''
    p[0] = p[2]
    #printp(p)
    printp(p)


def p_exprs_1(p):
    ''' exprs_1 : postfix_expr
                | epsilon
                | exprs_1 COMMA postfix_expr
    '''
    if(p.slice[1].type == 'postfix_expr'):
        p[0]=[p[1]]
    elif(len(p)==4):
        p[0]=p[1]+[p[3]]
    else:
        p[0]=[]
    printp(p)

def p_postfix_expr(p):
    ''' postfix_expr : infix_expr id_1
                     | infix_expr
    '''
    if len(p)==2:
        p[0]=p[1]
    printp(p)

def p_id_1(p):
    ''' id_1 : id
             | id_1 id
    '''
    printp(p)


def p_infix_expr(p):
    ''' infix_expr : assign
                   | or_expression
    '''
    p[0] = p[1]
    printp(p)

def p_assign(p):
    ''' assign : simple_expr1  asgn or_expression
    '''
    if 'islit' in p[1].keys():
        sys.exit("Type Error: Assignment to constant not defined.")
    temp = ST.getTemp()
    p[0] = {
            'place' : temp,
            'isarray' : False,
            'type': 'Not defined'
            }
    if p[2] == '=':
        p[3]=evalArray(p[3])
        if p[1]['type'] == 'Array' :
            emit('star',p[1]['place'],p[1]['index'],p[3]['place'])
        else:
            emit(op='=',out=p[1]['place'],in1=p[3]['place'])
    else:
        #print "ds is awesome"
        p[3]=evalArray(p[3])
        t1 = ST.getTemp()
        t2 = evalArray(p[1])
        #print p[2][0]
        emit(p[2][0],t1,t2['place'],p[3]['place'])
        if p[1]['type'] == 'Array':
            emit('star',p[1]['place'],p[1]['index'],t1)
        else:
            emit('=',p[1]['place'],t1)
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
    printp(p)

def p_and_expression(p):
    ''' and_expression : bit_or_expression 
                       | and_expression AND bit_or_expression 
    '''
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp,
                    'type'  : 'bool'
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
    printp(p)

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
                    'place' : temp,
                    'type'  : 'bool'
                }
        p[3]=evalArray(p[3])
        p[1]=evalArray(p[1])
        emit(op=p[2],out=temp,in1=p[1]['place'],in2=p[3]['place'])
    #printp(p)
    printp(p)


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
                    'place' : temp,
                    'type'  : 'bool'
                }
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
                    'place' : temp,
                    'type'  : 'INT'
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
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp,
                    'type'  : 'INT'
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
    if len(p) == 2:
        p[0]=p[1]
    else:
        temp = ST.getTemp()
        p[0] = {
                    'place' : temp,
                    'type'  : 'INT'
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
    printp(p)


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
    
    p[0] = {
            'idVal': p[1],
            'type' : p[1].upper()
            }
    #printp(p)
    printp(p)

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
    if len(p) == 2 and p.slice[1].type =="INT":
        p[0] = [{
            'place' : p[1],
            'type' : "INT"
            }]
    elif len(p)==2 and p.slice[1].type =="ID":
        p[0] = [{
            'place' : p[1],
            'type' : "INT"
            }]
    elif p.slice[3].type=="INT":
        p[0]=p[1]+[{
            'place' : p[3],
            'type' : "INT"
            }]
    elif p.slice[3].type=="ID":
        p[0]=p[1]+[{
            'place':p[3],
            'type':"ID"
            }]
    printp(p)


def p_literal(p):
    ''' literal : BOOL
                | INT
                | CHAR
                | STRING
                | FLOAT
    '''
    p[0] = {
            'type' : p.slice[1].type,
            'place' : p[1],
            'islit' : True
                }

    #printp(p)
    printp(p)

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
pickle_out=open("ST.picle","wb")
pickle.dump(ST,pickle_out)
#print ST.printSymbolTable(ST,1)
