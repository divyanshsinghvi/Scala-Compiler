#!/usr/bin/env python
import sys
import lex
import yacc
from tokens import *
from regex import *

# Build the lexer.
lexer = lex.lex()


# Python Reading the file contents
fileName = open(sys.argv[1],"r")
code = fileName.read()
fileName.close()


lexer.input(code)

tokens_d = {}

while True:
	token = lexer.token()
	if not token:
		break
	# print(token)
	if not token.type in tokens_d:
		tokens_d[token.type] = {str(token.value)}
	else:
		tokens_d[token.type].add(str(token.value))

print '%-20s%-20s%-20s' % ("Token", "Occurances", "Lexemes")
print "____________________________________________________"
for typ in tokens_d:
	print '%-20s%-20s%-20s' % (typ, len(tokens_d[typ]), '\n                                        '.join(tokens_d[typ]))


