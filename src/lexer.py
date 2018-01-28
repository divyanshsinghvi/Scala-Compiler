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
	if not token.value in tokens_d:
		tokens_d[token.value] = token.type, 1
	else:
		tokens_d[token.value] = token.type, tokens_d[token.value][1]+1

print '%-20s%-20s%-20s' % ("Token", "Occurances", "Lexemes")
print "____________________________________________________"
for value in tokens_d:
	print '%-20s%-20s%-20s' % (tokens_d[value][0], tokens_d[value][1], value)


