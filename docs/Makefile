MAIN = guide
NOTEBOOK = guide_example

all: $(NOTEBOOK).tex $(MAIN).pdf

DEPENDENCIES = $(MAIN).tex ../$(MAIN).ipynb sdp/sdp.bib

CLEAN_FILES += *.aux *bbl *.blg *.log *.out \
				$(MAIN).pdf $(NOTEBOOK).*


%.pdf: $(DEPENDENCIES)
	pdflatex --shell-escape $<
	bibtex $*
	pdflatex --shell-escape $<
	pdflatex --shell-escape $<

$(NOTEBOOK).tex: $(NOTEBOOK).md
	pandoc $(NOTEBOOK).md -o $(NOTEBOOK).tex

$(NOTEBOOK).md: $(NOTEBOOK).ipynb
	jupyter nbconvert $(NOTEBOOK).ipynb --to markdown

$(NOTEBOOK).ipynb: ../$(MAIN).ipynb
	python copy_guide_nb.py


clean:
	rm -f $(CLEAN_FILES)
