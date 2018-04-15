#!/bin/bash
python parsermain.py ../lexer_testcases/for.scala > 3ac.csv
make
./test.out


python parsermain.py ../lexer_testcases/loop.scala > 3ac.csv
make
./test.out


python parsermain.py ../lexer_testcases/func.scala > 3ac.csv
make
./test.out


python parsermain.py ../lexer_testcases/while.scala > 3ac.csv
make
./test.out


python parsermain.py ../lexer_testcases/switch.scala > 3ac.csv
make
./test.out

python parsermain.py ../lexer_testcases/dangling_if_else.scala > 3ac.csv
make
./test.out
