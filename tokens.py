tokens = [
'BOOL',
'LEFTARROW',
'GT',
'GE',
'LT',
'LE',
'LPARAN',
'RPARAN',
'LSQRB',
'RSQRB',
'BLOCKBEGIN',
'BLOCKEND',
'OP_ADD',
'OP_SUB',
'OP_DIV',
'OP_MUL',
'OP_MOD',
'EQ',
'NEQ',
'AND',
'OR',
'NOT',
'XOR',
'AND_BIT',
'OR_BIT',
'LSHIFT',
'RSHIFT',
'RRSHIFT',
'EQUALASGN',
'ADDASGN',
'SUBASGN',
'MULASGN',
'DIVASGN',
'MODASGN',
'LSHIFTASGN',
'RSHIFTASGN',
'ANDASGN',
'ORASGN',
'XORASGN',
'COLON',
'SEMICOLON',
'DOT',
'COMMA',
'UNDER',
'ID',
'CHAR',
'STRING',
'INT',
'FLOAT'
]

reserved = {
	'abstract' : 'R_ABSTRACT',
	'case' : 'R_CASE',
	'catch' : 'R_CATCH',
	'class' : 'R_CLASS',
	'do' : 'R_DO',
    'def': 'R_DEF',
    'else' : 'R_ELSE',
	'extends' : 'R_EXTENDS',
	'false' : 'R_FALSE',
	'final' : 'R_FINAL',
	'finally' : 'R_FINALLY',
	'for' : 'R_FOR',
#	'forSome' : 'R_FOR_SOME',
	'if' : 'R_IF',
	'implicit' : 'R_IMPLICIT',
	'import' : 'R_IMPORT',
    'Int' : 'TYPE_INT',
    'String': 'TYPE_STRING',
    'Char': 'TYPE_CHAR',
    'Array':'TYPE_ARRAY',
    'Float':'TYPE_FLOAT',
    'Boolean':'TYPE_BOOLEAN',
#	'lazy' : 'R_LAZY',
    'long':'R_LONG', #long in reserved
#    'macro' : 'R_MACRO',
	'match' : 'R_MATCH',
	'new' : 'R_NEW',
	'null' : 'R_NULL',
	'object' : 'R_OBJECT',
	'override' : 'R_OVERRIDE',
	'package' : 'R_PACKAGE',
	'private' : 'R_PRIVATE',
	'protected' : 'R_PROTECTED',
    'public': 'R_PUBLIC',
    'return' : 'R_RETURN',
#	'sealed' : 'R_SEALED',
	'super' : 'R_SUPER',
    'switch': 'R_SWITCH',
	'this' : 'R_THIS',
	'throw' : 'R_THROW',
	'trait' : 'R_TRAIT',
	'try' : 'R_TRY',
	'true' : 'R_TRUE',
	'type' : 'R_TYPE',
	'val' : 'R_VAL',
	'var' : 'R_VAR',
	'while' : 'R_WHILE',
	'with' : 'R_WITH',
	'yeild' : 'R_YIELD',
}

tokens = tokens + list(reserved.values())
