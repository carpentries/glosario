## FIXME: get the real 2-letter iso codes for languages
langs <- c("en", "fr", "es")


##' Get a glossary
##'
##' Retrive a YAML-formatted glossary from the web or locally.
##'
##' The specification of the file is available from
##' https://github.com/gvwilson/glossary/#readme
##'
##' @param url the url, path for the glossary or the OWNER/REPO for a GitHub
##'   repository that hosts a glossary.
##'
##' @details If <OWNER/REPO> is provided to the `url` argument, the successful
##'   conversion into an URL that will resolve to a glossary assumes that the
##'   glossary is called `glossary.yml` in the repository and it lives in the
##'   branch `master`.
##'
##' @return a list
##' @export
get_glossary <- function(url = "https://raw.githubusercontent.com/gvwilson/glossary/master/glossary.yml", cache = tempdir()) {

  if (identical(nchar(gsub("[^/]", "", url)), 1L) &&
        !grepl("\\.yml$", url, ignore.case = TRUE)) {
    url <- paste0(
      "https://raw.githubusercontent.com/",
      url,
      "/master/glossary.yml"
    )
  }

  Glossary$new(url, cache_path = cache)

}
