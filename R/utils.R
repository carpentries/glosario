glossary_default_path <- function(path = tempdir()) {

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

extract_slugs <- function(glossary) {
  purrr::map_chr(glossary, "slug")
}
