#!/usr/bin/env Rscript

# Create .rda version of glossary for R package.
# Usage: Rscript make-glossary.R /path/to/glossary.yml

args <- commandArgs(trailingOnly = TRUE)
raw <- yaml::read_yaml(args[1])
glossary <- list()
for (entry in raw) {
  glossary[[entry$slug]] <- entry
}
usethis::use_data(glossary, internal = TRUE)
