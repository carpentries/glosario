# glosario

`glosario` is an open source glossary of terms used in data science
that is available online and also as a library in both R and Python.
By adding glossary keys to a lesson's metadata,
authors can indicate what the lesson teaches,
what learners ought to know before they start,
and where they can go to find that knowledge.
Authors can also use the library's functions
to insert consistent hyperlinks for terms and definitions in their lessons
in any of several (human) languages.

## Lessons

R Markdown and Jupyter notebooks allow authors to place structured metadata in files.
We propose the following metadata (written as YAML):

```
glossary:
  sources:
  - http://some_glossary.org/something/
  language: fr
  requires:
  - aggregation_function
  - call_stack
  defines:
  - closure
  - name_collision
```

1.  The `source` key is required.
    -   It must introduce a list containing at least one URL.
    -   Those URLs must resolve to glossaries as described in the next section.
    -   Those glossaries are searched in order from first to last to find definitions.
1.  The `language` key is required,
    and must be a single ISO 639 language code
    (e.g., `fr` for French).
1.  The keys `requires` and `defines` are optional.
    -   Either may introduce an empty list.
    -   The values under these keys are keys into a shared glossary (discussed in the next section).
1.  We expect the terms identified under `requires` to be used *without* being defined in this lesson
    (i.e., the lesson author assumes users already know them).
1.  All of the terms identified under `defines` must be hyperlinked in the lesson.
    -   The target of the hyperlink for the term's definition must be `GLOSSARY_SITE#glossary_key`,
        where `GLOSSARY_SITE` is one of the sites listed under the `sources` key
        and `glossary_key` is an exact match for one of the `defines` keys.

We will provide simple tools to that
all of the terms listed in a lesson's metadata are linked correctly in its body.
We will also provide shortcuts to make it easy to create correctly-formatted links,
so that authors can write things like:

```
The computer uses a `r link('call stack', 'call_stack')` to keep track of function calls.
```

## Glossaries

Any site where glossary URLs resolve can be used as a glossary.
As a working model,
this project implements a glossary of terms used in data science and data engineering.

1.  The master copy of the glossary lives in `glossary.yml`.
    Its format is described below.
1.  This file is turned into a single-page GitHub Pages site using Jekyll.
1.  It is also turned into a [Python package](https://github.com/carpentries/glosario-py) called `glosario`
    and an [R package](https://github.com/carpentries/glosario-r) with the same name.

A glossary entry is structured like this:

```
- slug: cran
  en:
    term: "Comprehensive R Archive Network"
    acronym: "CRAN"
    def: >
      A public repository of R [packages](#package).
  ref:
    - base_r
    - tidyverse
```

-   The value associated with the `slug` key identifies the entry.
    -   It must be unique within the glossary.
    -   It must be in lower case and use only letters, digits, and the underscore
        (to be compatible with Jekyll's automatic slug creation).
    -   It becomes the fragment identifier in the online version of the glossary.
-   The entry *may* have a `ref` key.
    If it is present,
    its value must be a list of identifiers of related terms in this glossary.
-   Every other top-level key must be an ISO 639 language code such as `en` or `fr`.
    -   Every entry must have at least one such language section.
-   Within each language section for each term:
    -   The value of `term` is the term being defined.
        This key must be present.
    -   The key `acronym` is optional.
        If present, its value is the acronym for this term.
    -   The value of `def` is the definition.
        This key must be present,
        and the value may contain local links to other terms in this glossary
        (i.e., links starting with `#`)
        and/or links to outside sources.

## Open issues

1.  Should we provide one function for interactive definition lookup
    that searches keys and terms,
    a separate function for each,
    or some kind of keyword arguments to control the scope of search?

1.  Should we integrate definition lookup with existing help systems?
    For example,
    should `define('something')` in RStudio put the definition in the help pane
    (and if so, should it hyperlink to terms that the definition depends on)?

## Use Cases

1.  **Linking to a definition.**
    1.  *Amari* writes a lesson in R Markdown that introduces some new terms.
    1.  She has defined the language to be Spanish using the `glossary/language` key
        in the YAML header,
        but has not changed any other settings.
    1.  She adds an inline code block `` `r gdef('linear-model', 'Linear models')` ``
        to her lesson.
    1.  When she knits her document,
        the inline code block produces the HTML
        `<a href="http://carpentries.org/glossary/es/#linear-model" class="glossary-definition">Linear Models</a>`

1.  **Checking a lesson.**
    1.  *Beatriz* has made some changes to a lesson she inherited from *Amari*,
        and wants to check that it is still consistent.
    1.  She runs a command-line script that:
        1.  Reads the R Markdown file.
        1.  Extracts the terms under the `glossary/defines` key.
        1.  Searches the body of the document for calls to `gdef(...)`.
        1.  Checks that every term listed in `glossary/defines` is referenced in the document body,
            and that every term referenced in the document body is mentioned in `glossary/defines`.

1.  **Finding lessons.**
    1.  *Amari* writes a lesson in R Markdown.
        She adds the `glossary` key to its YAML metadata
        and indicates that the lesson requires the term `correlation`
        and defines the term `regression`.
    1.  *Beatriz* is writing a lesson on linear models.
        She adds YAML metadata indicating that
        the lesson requires the term `regression`.
    1.  To find prerequisite lessons she can recommend to her students,
        Beatriz runs a command-line script that:
        1.  Uses `rmarkdown::yaml_front_matter(filename)`
            to reads metadata from all of the lessons she has archived.
        1.  Lists all of the lessons that state they define the term `regression`.

1.  **Summarizing a lesson.**
    1.  *Amari* has written a lesson in R Markdown that includes YAML metadata
        stating that it defines `correlation` and `causation`.
    1.  She adds a code chunk to the end of her lesson that includes a call to
        `glosario::summarize_terms()`.
    1.  When she knits the document to HTML,
        this code chunk inserts a definition list `dl` at that point.
        Its entries are the definitions of
        all of the terms listed under the `glossary/defines` key
        in the page's YAML header
        in alphabetical order by term according to the rules for `glossary/language`.

## FAQ

-   **Why not just link to Wikipedia?**
    We expect that many glossary definitions will do so,
    but Wikipedia articles are explanations, not definitions.

-   **YAML is hard for people to edit—why not use something else for the glossary file?**
    Because other formats are just as hard to edit (e.g., JSON)
    or make one-to-many relationships hard to express (e.g., CSV).

-   **Why use Jekyll for the online version?**
    It's the default for GitHub Pages.

## Credits

-   Parrot logo by [restocktheshelves](https://www.deviantart.com/restocktheshelves).
