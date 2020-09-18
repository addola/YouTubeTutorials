TEX=pdflatex
BIB=bibtex
UNAME_S := $(shell uname)
PDF_VIEWER=evince
ifeq ($(UNAME_S),Linux)
	PDF_VIEWER=evince
endif

ifeq ($(UNAME_S),Darwin)
	PDF_VIEWER=open
endif


COMMON_TEX_PARAMS=-interaction=nonstopmode

MAIN_TEX_FILE=paper

all:
	$(TEX) $(TEX_PARAMS) $(COMMON_TEX_PARAMS) $(MAIN_TEX_FILE).tex

bib:
	$(TEX) $(TEX_PARAMS) $(COMMON_TEX_PARAMS) $(MAIN_TEX_FILE).tex
	$(BIB) $(MAIN_TEX_FILE).aux
	$(TEX) $(TEX_PARAMS) $(COMMON_TEX_PARAMS) $(MAIN_TEX_FILE).tex
	$(TEX) $(TEX_PARAMS) $(COMMON_TEX_PARAMS) $(MAIN_TEX_FILE).tex


view:
	$(PDF_VIEWER) paper.pdf

clean:
	rm -f *.aux *.log *.pyg *.dvi *.pdf *.out *.toc *.vrb *.nav *.fls *.fdb_latexmk *.synctex.gz *.snm
	rm -rf _minted-paper/ _minted-slides
	latexmk -CA