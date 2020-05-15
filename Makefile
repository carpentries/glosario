# Default target.
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## site : rebuild GitHub Pages site locally.
site : _data/glossary.yml
	rm -rf .jekyll-cache .jekyll-metadata _site
	jekyll build

## serve : serve GitHub Pages site locally.
serve : _data/glossary.yml
	rm -rf _site
	jekyll serve -I

## clean : clean up unneeded files.
clean :
	@rm -rf _site
	@find . -name '*~' -exec rm {} \;
	@rm -rf glossary/__pycache__
	@rm -rf MANIFEST build dist py-installed-files.txt Glossary.egg-info
	@rm -f _data/glossary.yml glossary/glossary.yml
	@rm -f R/sysdata.rda

## ---- : ----

## py-package : build Python package.
py-package : glossary/glossary.yml
	python setup.py sdist
	rm -rf Glossary.egg-info

## py-install : install Python package.
py-install :
	python setup.py install --record py-installed-files.txt

## py-uninstall : remove Python package using record of installed files.
py-uninstall : py-installed-files.txt
	cat py-installed-files.txt | xargs rm -rf

## ---- : ----

## r-package : build R package.
r-package : R/sysdata.rda
	cd .. && R CMD build glossary

#----------------------------------------------------------------------

# Create copy of glossary file for GitHub Pages site.
_data/glossary.yml : ./glossary.yml
	@mkdir -p _data
	@cp $< $@

# Create copy of glossary file for Python package.
glossary/glossary.yml : ./glossary.yml
	@cp $< $@

# Create R data version of glossary file for R package.
R/sysdata.rda : ./glossary.yml
	@Rscript bin/make-glossary.R $<
