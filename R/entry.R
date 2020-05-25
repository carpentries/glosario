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
    .content = NULL, # list as direct output from read_yaml
    .entries = NULL  # R6 classes as defined above
  ),

  public = list(
    initialize = function(glossary_path) {

      private$.uri <- glossary_path
      private$.content <- yaml::read_yaml(glossary_path)

      self$validate()

      private$.entries <- purrr::map(
        private$.content,
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
                  term = l$term,
                  defn = l$def,
                  lang = lang
                )
              }
            )
          }
          res
        })

      self

    },

    validate = function() {
      ## check all entries have slugs
      has_slug <- purrr::map_lgl(private$.content, function(e) {
        exists("slug", e)
      })
      if (!all(has_slug)) {
        stop(
          "Improperly formatted glossary. Some entries don't have a slug.",
          call. = FALSE
        )
      }

      ## all slugs are unique
      slugs <- extract_slugs(private$.content)
      if (any(duplicated(slugs))) {
        stop(
          "Some slugs are duplicated: ",
          paste(slugs[duplicated(slugs)], collapse = ", "),
          call. = FALSE
        )
      }

      ## the "see also" (ref) are all valid slugs
      refs <- purrr::map_df(private$.content, function(e) {
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
      self
    },

    define = function(key, lang = NULL) {
      entry <- private$.entries
      idx <- match(key, extract_slugs(private$.entries))
      if (any(is.na(idx))) {
        warning("Some key are not found: ",
          sQuote(paste(key[is.na(idx)], collapse = ", ")),
          ". They are being excluded.",
          call. = FALSE)
      }
      idx <- idx[!is.na(idx)]
      purrr::walk(
        entry[idx],
        function(e) {
          e$print(lang, show_lang = FALSE)
        })
    },

    print = function() {
      n_slugs <- extract_slugs(private$.content) %>%
        length()

      cli::cli_text("A glossary with {.strong {n_slugs}} entries.")
    }

  )

)
