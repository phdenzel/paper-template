# Paper Title

This paper is formatted for submission to MNRAS.


### Compile
Prerequisites: `pdflatex`, `bibtex`, `mnras.cls`

In the terminal, `cd` into the repository and type

```bash
make
```
to get the latest version of the paper in pdf format.
With this 3 commands are automatically executed:

```bash
pdflatex main.tex
bibtex main.aux
pdflatex main.tex
```
To ensure that the citations don't give an error, another pdflatex command might have to be added manually after compilation.
