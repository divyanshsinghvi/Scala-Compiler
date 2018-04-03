.DEFAULT_GOAL := irgen
.PHONY: irgen
irgen:
	python registerAlloc.py 3ac.csv > test.s
	gcc -m32 test.s
