LanguageGlossaryEntry <- R6::R6Class("LanguageGlossaryEntry",
  private = list(
    .lang = NA_character_,
    .term = NA_character_,
    .defn = NA_character_
  ),
  public = list(
    initialize = function(term, defn, lang = "en") {
      stopifnot(rlang::is_scalar_character(term))
      stopifnot(rlang::is_scalar_character(defn))
      stopifnot(rlang::is_scalar_character(lang))
      private$.term <- term
      private$.defn <- defn
      private$.lang <- lang
    },
    language =  function() {
      private$.lang
    },
    term = function() {
      private$.term
    },
    definition = function() {
      private$.defn
    },
    print = function() {
      cat("  + (", private$.lang, ")", sep = "")
      cat(" **", private$.term, "**: ", sep = "")
      cat( private$.defn, "\n", sep = "")
    }
  )
)

GlossaryEntry <- R6::R6Class("GlossaryEntry",
  private = list(
    .slug = NA_character_,
    .entries = NULL
  ),
  public = list(
    initialize = function(slug, term, defn, lang) {
      stopifnot(rlang::is_scalar_character(slug))
      private$.slug <- slug
      e <- LanguageGlossaryEntry$new(term, defn, lang)
      private$.entries <- list(e)
      self
    },
    list_languages = function() {
      vapply(private$.entries, function(e) {
        e$language()
      }, character(1))
    },
    add_entry = function(term, defn, lang) {
      existing_lang <- self$list_languages()
      if (lang %in% existing_lang) {
        stop("entry already exists for language: ", lang, call. = FALSE)
      }
      e <- LanguageGlossaryEntry$new(term, defn, lang)
      private$.entries <- c(
        private$.entries,
        e
      )
      self
    },
    export = function() {
      purrr::map_dfr(private$.entries,
        ~ tibble::tibble(
          slug = private$.slug,
          language = .$language(),
          term = .$term(),
          definition = .$definition()
        )
      )
    },
      print = function() {
        cat("Slug: ", private$.slug, "\n", sep = "")
        lapply(private$.entries, print)
      }
  )
)
