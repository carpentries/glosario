## FIXME: get the real 2-letter iso codes for languages
langs <- c("en", "fr", "es")


##' Get a glossary
##'
##' Retrive a YAML-formatted glossary from the web or locally.
##'
##' The specification of the file is available from https://github.com/gvwilson/glossary/#readme
##' @param url the path for the glossary
##' @return a list
##' @export
get_glossary <- function(url = "https://raw.githubusercontent.com/gvwilson/glossary/master/glossary.yml") {

  Glossary$new(url)

}
