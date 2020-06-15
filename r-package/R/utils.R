validate_glossary_cache_path <- function(path) {

  if (!rlang::is_scalar_character(path)) {
    stop("invalid format for cache path provided.", call. = FALSE)
  }

  if (!dir.exists(path)) {
    stop(
      "path: ",
      sQuote(path),
      " doesn't exist. Please create it first.",
      call. = FALSE
    )
  }

  path

}
