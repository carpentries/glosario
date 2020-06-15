#!/usr/bin/env Rscript

# Create .rda version of glossary for R package.
# Usage: Rscript make-glossary.R /path/to/glossary.yml


args <- commandArgs(trailingOnly = TRUE)
raw <- yaml::read_yaml(args[1])
glossary <- list()
for (entry in raw) {
  glossary[[entry$slug]] <- entry
}

setwd('r-package') # We have to trick usethis because of package safeguarding on the functions

usethis::use_data(glossary, internal = TRUE)
