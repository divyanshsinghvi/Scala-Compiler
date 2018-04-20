#!/bin/bash
python src/parsermain.py $1 > 3ac.csv
python src/registerAlloc.py 3ac.csv > test.s
gcc -m32 test.s -o test.out
./test.out
