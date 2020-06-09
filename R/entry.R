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
    print = function(show_lang = TRUE) {
      def <- private$.defn

      if (show_lang) {
        def <- paste0(def, " (", private$.lang, ")")
      }

      names(def) <- private$.term
      cli::cli_dl(def)

    }
  )
)

GlossaryEntry <- R6::R6Class("GlossaryEntry",
  private = list(
    .slug = NA_character_,
    .entries = NULL,
    .ref = NULL
  ),
  public = list(
    initialize = function(slug, term, defn, lang, ref = NULL) {
      stopifnot(rlang::is_scalar_character(slug))

      private$.slug <- slug
      e <- LanguageGlossaryEntry$new(term, defn, lang)
      private$.entries <- list(e)

      if (!is.null(ref)) {
        private$.ref <- ref
      }

      self
    },
    add_entry = function(slug, term, defn, lang) {

      ## FIXME: maybe make slug optional for these cases
      if (!identical(private$.slug, slug)) {
        stop(
          "Provided slug (", sQuote(slug),
          ") doesn't match internal slug ",
          sQuote(private$.slug), ").",
          call. = FALSE
        )
      }

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
    list_languages = function() {
      purrr::map_chr(
        private$.entries, function(e) {
          e$language()
        }
      )
    },
    export = function() {
      purrr::map_dfr(
        private$.entries,
        ~ tibble::tibble(
          slug = private$.slug,
          language = .$language(),
          term = .$term(),
          definition = .$definition()
        )
      )
    },
    print = function(lang = NULL, show_lang = TRUE) {

      if (! is.null(lang)) {
        lang <- match.arg(lang, langs, several.ok = TRUE)

        if (!all(lang %in% self$list_languages())) {
          warning(
            "Some languages requested are not availble for this entry.",
            call. = FALSE
          )
        }
        idx <- match(lang, self$list_languages(), nomatch = NULL)
      } else {
        idx <- seq_along(private$.entries)
      }

      purrr::walk(private$.entries[idx], print, show_lang)

      if (!is.null(private$.ref)) {
        cli::cli_text(
          "   {.emph See also:} ", cli::bg_cyan("{private$.ref}")
        )
      }

      cli::cli_text() ## final empty line
    }
  ),
  active = list(
    slug = function(value) {
      if (missing(value)) {
        private$.slug
      } else {
        stop("Slugs can't be modified.", call. = FALSE)
      }
    }
  )
)


Glossary <- R6::R6Class("Glossary",
  private = list(
    .uri = NA_character_,
    .entries = NULL,
    .use_cache = NA
  ),

  public = list(
    initialize = function(glossary_path,
                          cache_path = tempdir()) {

      validate_glossary_uri(glossary_path)

      if (!is.null(cache_path)) {
        raw_glossary <- use_cache(glossary_path, cache_path)
      } else {
        raw_glossary <- list(
          uri = glossary_path,
          entries = yaml::read_yaml(glossary_path)
        )
      }

      private$.uri <- raw_glossary$uri

      validate_raw_glossary(raw_glossary$entries)

      private$.entries <- purrr::map(
        raw_glossary$entries,
        function(e) {
          slug <- e$slug
          ref <- e$ref

          entries_lang <- e[names(e) %in% langs]
          res <- GlossaryEntry$new(
            slug = slug,
            term = entries_lang[[1]]$term,
            defn = entries_lang[[1]]$def,
            lang = names(entries_lang)[1],
            ref = ref
          )

          ## FIXME: is there a better way to do this?
          if (length(entries_lang) > 1) {
            purrr::imap(
              entries_lang[-1],
              function(lang_entry, lang) {
                res$add_entry(
                  slug = slug,
                  term = lang_entry$term,
                  defn = lang_entry$def,
                  lang = lang
                )
              }
            )
          }
          res
        })

      self

    },

    list_slugs = function() {
      purrr::map_chr(private$.entries, "slug")
    },

    define = function(key, lang = NULL, show_lang = FALSE) {
      idx <- match(key, self$list_slugs())
      if (any(is.na(idx))) {
        warning(
          "Some key are not found: ",
          sQuote(paste(key[is.na(idx)], collapse = ", ")),
          ". They are being excluded.",
          call. = FALSE
        )
      }
      idx <- idx[!is.na(idx)]
      purrr::walk(
        private$.entries[idx],
        function(e) {
          e$print(lang, show_lang = show_lang)
        })
    },

    print = function() {
      n_slugs <- self$list_slugs() %>%
        length()

      cli::cli_text("A glossary with {.strong {n_slugs}} entries.")
    }

  )

)
