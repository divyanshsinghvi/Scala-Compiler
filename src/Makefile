.DEFAULT_GOAL := irgen
.PHONY: irgen
irgen:
	python registerAlloc.py 3ac.csv > test.out
	gcc -m32 test.out
