import sys
import lex
import yacc
from tokens import *
from regex import *

# Build the lexer.
lexer = lex.lex()

# # Read the input file as first argument.
# file = open(sys.argv[1],"r")
# code = file.read()
# # code = code + '\n'
# file.close()

# # Use the lexer.
# lexer.input(code)

#Example
lexer.input('''
  var myVar :Int;
  val myVal :String;

    a='\u0041'
    a='\n'
    a='\t'

''')

while True:
	token = lexer.token()
	if not token:
		break
	print(token)
