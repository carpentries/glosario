# Glossary

In order to make lessons easier to find and remix,
we propose a simple standard for indicating
the terms learners must know before starting
and the terms that the lesson defines.
Rather than embedding definitions in lessons,
authors will link to a shared glossary
that can be browsed online
or loaded interactively in R and Python sessions,
where it can be used like any other online help.

## What goes in a lesson?

R Markdown and Jupyter notebooks allow authors to place structured metadata in files.
We propose the following metadata (written as YAML):

```
glossary:
  sources:
  - http://some_glossary.org/something/
  language:
  - fr
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
    and must be an ISO 639 language code
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

## What goes in a glossary?

Any site where glossary URLs resolve can be used as a glossary.
As a working model,
this project implements a glossary of terms used in data science and data engineering.

1.  The master copy of the glossary lives in `glossary.yml`.
    Its format is described below.
1.  This file is turned into a single-page GitHub Pages site using Jekyll.
1.  It is also turned into a Python package called `glossary`
    and an R package with the same name.
    -   After installing it,
        a Python user can `import glossary`.
        Calling `glossary.define('something')` will then look up the definition of a term.
    -   Similarly,
        after `library(glossary)`,
        an R user can call `define('something')` to display a term's definition.

## Glossary format



## Open questions

1.  Should we provide one function for interactive definition lookup
    that searches keys and terms,
    a separate function for each,
    or some kind of keyword arguments to control the scope of search?
1.  Should we integrate definition lookup with existing help systems?
    For example,
    should `define('something')` in RStudio put the definition in the help pane
    (and if so, should it hyperlink to terms that the definition depends on)?
