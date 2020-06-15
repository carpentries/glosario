validate_glossary_uri <- function(glossary_path) {
  if (!rlang::is_scalar_character(glossary_path)) {
    stop(
      "The location of the glossary must be a character vector of length 1.",
      call. = FALSE
    )
  }

  ## FIXME: what other tests do we want to have here?
  TRUE
}

validate_raw_glossary <- function(parsed_yaml) {

  ## check all entries have slugs
  has_slug <- purrr::map_lgl(
    parsed_yaml,
    function(e) {
      exists("slug", e)
    })

  if (!all(has_slug)) {
    stop(
      "Improperly formatted glossary. Some entries don't have a slug.",
      call. = FALSE
    )
  }

  ## all slugs are unique
  slugs <- purrr::map_chr(parsed_yaml, "slug")
  if (any(duplicated(slugs))) {
    stop(
      "Some slugs are duplicated: ",
      paste(slugs[duplicated(slugs)], collapse = ", "),
      call. = FALSE
    )
  }

  ## the "see also" (ref) are all valid slugs
  refs <- purrr::map_df(parsed_yaml, function(e) {
    if (!exists("ref", e)) {
      return(NULL)
    }
    list(
      slug = rep(e$slug, length(e$ref)),
      ref = e$ref
    )
  })
  refs <- tibble::add_column(
    refs,
    is_in_glossary = purrr::map_lgl(
      refs$ref,
      ~ . %in% slugs
    )
  )
  if (!all(refs$is_in_glossary)) {
    ## FIXME: improve error message
    stop("Some references are slugs that are not found.", call. = FALSE)
  }
  TRUE
}


validate_cached_glossary <- function(glossary) {

  if (
    !inherits(glossary, "list") ||
      !exists("uri", glossary) ||
       !exists("entries", glossary)
  ) {
    stop("Invalid format for the cached glossary.", call. = FALSE)
  }

  TRUE
}
