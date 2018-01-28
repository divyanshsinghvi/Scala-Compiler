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
	if not token.type in tokens_d:
		tokens_d[token.type] = [token.value], 1
	else:
		if not token.value in tokens_d[token.type][0]:
			tokens_d[token.type] = (tokens_d[token.type][0]) + [token.value], tokens_d[token.type][1]+1
		else:
			tokens_d[token.type] = (tokens_d[token.type][0]), tokens_d[token.type][1]+1

print '%-20s%-20s%s' % ("Token", "Occurances", "Lexemes")
print "____________________________________________________"
for value in tokens_d:
	print '%-20s%-20s%s' % (value, tokens_d[value][1], (tokens_d[value][0][0]))
	for i in range(1,len(tokens_d[value][0])):
		print '%-40s%s' %(" ", (tokens_d[value][0][i]))


