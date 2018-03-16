.DEFAULT_GOAL := parser

parser:
	cp src/lexer.py bin/lexer.py
	cp src/lex.py bin/lex.py
	cp src/yacc.py bin/yacc.py
	cp src/tokens.py bin/tokens.py
	cp src/regex.py bin/regex.py
	cp src/parsermain.py bin/parsermain.py
	cp src/parser.sh bin/parser
	chmod +x bin/parser
	chmod -R 777 bin/


codegen:
	cp src/ir.py bin/ir.py
	cp src/basicBlock.py bin/basicBlock.py
	cp src/globalData.py bin/globalData.py
	cp src/globalvar.py bin/globalvar.py
	cp src/nextUse.py bin/nextUse.py
	cp src/registerAlloc.py bin/registerAlloc.py
	cp src/symbolTable.py bin/symbolTable.py
	cp src/table.py bin/table.py
	python -m py_compile bin/registerAlloc.py
	mv bin/registerAlloc.pyc bin/codegen
	chmod -R 777 bin/

lexer:
		cp src/lexer.py bin/lexer.py
		cp src/lex.py bin/lex.py
		cp src/yacc.py bin/yacc.py
		cp src/tokens.py bin/tokens.py
		cp src/regex.py bin/regex.py
		python -m py_compile bin/lexer.py
		mv bin/lexer.pyc bin/lexer
		chmod -R 777 bin/

ass:
		python registerAlloc.py > seemsok.s
		gcc  seemsok.s -o seemsok.out

clean:
		rm -rf bin/*
