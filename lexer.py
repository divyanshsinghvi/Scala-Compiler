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
lexer.input('''abc HelloWorld {
    def main(args: Array[String]) {
      println("Hello, world!")
      return 0;
      a = -24;
      b = +10.87;
      c = 00001;
    }
  }
''')

while True:
	token = lexer.token()
	if not token:
		break
	print(token)
