import sys
import ply.lex as lex
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
lexer.input('''object Demo {
   def main(args: Array[String]) {
      var a = 10;
        a = 3 + 10;
   	}
}
''')

while True:
	token = lexer.token()
	if not tok:
		break
	print(token)
