#!/bin/bash
python parsermain.py $1 > 3ac.csv
python registerAlloc.py 3ac.csv > test.s
gcc -m32 test.s
./a.out
