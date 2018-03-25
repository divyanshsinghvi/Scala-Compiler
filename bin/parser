#!/bin/bash

tf=$1
file=$(echo $1 | sed -e 's/.*\/\(.*\)\..*/\1/')
python src/parsermain.py $1 > input.txt
filename="$file.html"
python src/script.py $filename
