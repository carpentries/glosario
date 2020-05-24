#' Look up definition of term.
#'
#' @param key lookup key
#'
#' @return string containing definition
#'
#' @export
define <- function(key, lang = "en", glossary = get_glossary()) {
  all_entries <- purrr::keep(
    glossary,  purrr::map_chr(glossary, "slug") == key
  )
  if (length(all_entries) < 1L) {
    stop("Key not found")
  }

  if (length(all_entries) > 1L) {
    stop("More than one key found")
  }

  all_entries <- purrr::flatten(all_entries)

  if (!exists(lang, all_entries)) {
    stop("Language not found for this key.")
  }
  entry <- all_entries[[lang]]


  class(entry) <- c("glossary_entry", class(entry))
  attr(entry, "slug") <- all_entries$slug
  attr(entry, "ref") <- all_entries$ref
  entry
}

##' Print glossary definitions
##'
##' @param x a object returned by define()
##' @param ... additional argument for generic print method
##' @export
print.glossary_entry <- function(x, ...) {

  def <- x$def
  names(def) <- x$term
  cli::cli_text()
  cli::cli_dl(def)

}
