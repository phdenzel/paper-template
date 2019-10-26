SHELL := /bin/bash

main:
	pdflatex main.tex \
	&& bibtex main.aux \
	&& pdflatex main.tex

.PHONY: main

clean:
	rm *.aux *.blg *.log *.out
