all:
		cp src/lexer.py bin/lexer.py
		cp src/lex.py bin/lex.py
		cp src/yacc.py bin/yacc.py
		cp src/tokens.py bin/tokens.py
		cp src/regex.py bin/regex.py
		python -m py_compile bin/lexer.py
		mv bin/lexer.pyc bin/lexer
		chmod -R 777 bin/

clean:
		rm -rf bin/*
