all: citeGen acm ieee

citeGen: citeGen.o
	g++ -o citeGen citeGen.cpp

acm: citeGen
	./citeGen acm-tagged_1.bib citations-acm.txt

ieee: citeGen
	./citeGen ieee-tagged_1.bib citations-ieee.txt
