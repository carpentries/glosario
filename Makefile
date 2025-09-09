# Default target.
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

# Create copy of glossary file for GitHub Pages site.
_data/glossary.yml : ./glossary.yml
	@mkdir -p _data
	@cp $< $@

## sort : sort the glossary file and build _data glossary file per language
sort-glossary : _data/glossary.yml
	@yamllint glossary.yml
	@python3 utils/sort-glossary.py

## site : rebuild GitHub Pages site locally.
site :
	$(MAKE) sort-glossary
	rm -rf .jekyll-cache .jekyll-metadata _site
	bundle exec jekyll build

## gh-site : builds the website for GitHub pages (part of the GH Actions workflow)
gh-site : _data/glossary.yml
	$(MAKE) sort-glossary
	@rm -rf _gh-site
	@mkdir -p _gh-site
	@cp -r `ls -A | grep -v '.git' | grep -v '_gh-site' | grep -v '_site'` _gh-site
	@mkdir -p _gh-site/_data
	@cp $< _gh-site/$<

## serve : serve GitHub Pages site locally.
serve :
	$(MAKE) sort-glossary
	rm -rf _site
	bundle exec jekyll serve -I

## clean : clean up unneeded files.
clean :
	@rm -rf _site
	@rm -rf _gh-site
	@find . -name '*~' -exec rm {} \;
	@rm -rf _data/*

## check : check glossary consistency.
check :
	@yamllint glossary.yml
	@python3 utils/check-glossary.py _config.yml glossary.yml

## checkall : check glossary consistency including missing terms in all languages.
checkall :
	@python3 utils/check-glossary.py -A _config.yml glossary.yml
