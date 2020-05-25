#' Look up definition of term.
#'
#' @param key lookup key
#' @param lang language for the definition
#' @param glossary a glossary object
#'
#' @return string containing definition
#'
#' @export
define <- function(key, lang = "en", glossary, show_lang = FALSE) {
  glossary$define(key, lang, show_lang = show_lang)
}
