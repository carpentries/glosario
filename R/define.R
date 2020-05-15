#' Look up definition of term.
#'
#' @param key lookup key
#'
#' @return string containing definition
#'
#' @export
define <- function(key) {
  glossary:::glossary[[key]]
}
