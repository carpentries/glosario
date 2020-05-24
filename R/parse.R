## FIXME: get the real 2-letter iso codes for languages
langs <- c("en", "fr", "es")


validate_glossary <- function(glossary) {

  ## check all entries have slugs
  has_slug <- purrr::map_lgl(glossary, function(e) {
    exists("slug", e)
  })
  stopifnot(all(has_slug))

  ## all slugs are unique
  slugs <- purrr::map_chr(glossary, "slug")
  if (any(duplicated(slugs))) {
    stop(
      "Some slugs are duplicated: ",
      paste(slugs[duplicated(slugs)], collapse = ", ")
    )
  }

  NULL
}

##' Get a glossary
##'
##' Retrive a YAML-formatted glossary from the web or locally.
##'
##' The specification of the file is available from https://github.com/gvwilson/glossary/#readme
##' @param url the path for the glossary
##' @return a list
##' @export
get_glossary <- function(url = "https://raw.githubusercontent.com/gvwilson/glossary/master/glossary.yml") {

  session_file <- file.path(tempdir(), "glossary.rds")

  if (!file.exists(session_file)) {
    glossary <- yaml::read_yaml(url)
    validate_glossary(glossary)
    message("writing ", session_file, appendLF = FALSE)
    saveRDS(glossary, session_file)
    message(" done!")
  } else {
    message("reading ", session_file)
    glossary <- readRDS(session_file)
  }

  invisible(glossary)

}
