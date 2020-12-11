Thank you for your interest in contributing to Glosario!
We welcome contributions of all kinds.
If you are here to submit a definition,
either for a new term
or in another language for an existing term,
please take a moment to read the guidance below.

## Contribution Workflow

When you are making your contribution(s) to Glosario, please:

1. **check the [open Issues][issues] and [Pull Requests][pulls]** to see what terms and definitions other contributors are already working on. This will help you avoid accidentally spending time writing the same term(s)/definition(s) as someone else.
2. **add one or a small number of related new terms or definitions per Pull Request.** We woud love to receive multiple contributions from you but please keep each new term or set of terms and definitions in a distinct Pull Request. This makes it much easier for the Glosario maintainers/editors to review your contributions. By [creating a new branch][github-branches] from the `master` branch and making a new Pull Request each time, you also reduce the chance of accidentally combining multiple contributions.
3. If you plan to contribute a larger number of terms e.g. to cover a new domain, **[open an Issue][issues]** with a title in the format "[language]/domain" e.g. "Romanian/relational database terms." This will help others avoid devoting time to writing the same terms/definitions as you.

## 1. Adding a new term to the glossary

To add a new entry, please [fork][forking-guide] the [main Glosario repository][repo] and, on a new branch, add the term and definition to [`glossary.yml`][glossary]. This glossary file is written in [YAML]. If you already have a fork of the repository, then please [make sure your fork is up-to-date](https://happygitwithr.com/upstream-changes.html#upstream-changes) with the [main Glosario repository][repo].

When adding a new term or translation, please take care with the indentation on the YAML file. Indentation is syntactically significant in YAML.

In case you wish to build up the website locally to double check the final look, you can use `make serve`. 

Here is an example of how your glossary entry should be structured:

```
- slug: cran
  ref:
    - base_r
    - tidyverse
  en:
    term: "Comprehensive R Archive Network"
    acronym: "CRAN"
    def: >
      A public repository of R [packages](#package).
```

-   The value associated with the `slug` key identifies the entry.
    -   It must be unique within the glossary.
    -   It must be in lower case and use only letters, digits, and the underscore
        (to be compatible with Jekyll's automatic slug creation).
-   The entry *may* have a `ref` key.
    If it is present,
    its value must be a list of identifiers of related terms in this glossary.
-   Every other top-level key must be a two-letter ISO 639 language code such as `en` or `fr`.
    (Refer to the "639-1" column of [this table][iso639-table-en].)
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
    -   Note that, regardless of the language of their associated values, the keys like `term`, `acronym`, and `def` are not to be translated.

Once your term and definition(s) are complete, [make a Pull Request][pr-guide] back to the main repository.

### 2. Adding a definition in another language to an existing term

To add a new definition to an existing term in the glossary, please fork [the main Glosario repository][repo] and, on a new branch, find the term in [`glossary.yml`][glossary] and add the two-letter ISO 639 language code such as `en` or `fr` as a new top-level key. (Refer to [the "639-1" column of this table][iso639-table-en].)

You can then fill in the `term`, `def`, and (if appropriate) `acronym` for that term in your chosen language. The example below shows a term entry with definitions in English (`en`), Spanish (`es`), and French (`fr`):

```
- slug: global_variable
  ref:
    - local_variable
  en:
    term: "global variable"
    def: >
      A variable defined outside any particular function, which is therefore visible
      to all functions.
  es:
    term: "variable global"
    def: >
      Una variable definida fuera de alguna función en particular, por lo que es visible
      para todas las funciones.
  fr:
    term: "variable globale"
    def: >
      Une variable définie en dehors d'une fonction donnée, qui est par conséquent visible pour
      toutes les fonctions.
```

[forking-guide]: https://guides.github.com/activities/forking/
[github-branches]: https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-branches
[glossary]: https://github.com/carpentries/glosario/blob/master/glossary.yml
[iso639-table-en]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[issues]: https://github.com/carpentries/glosario/issues
[new issue]: https://github.com/carpentries/glosario/issues/new
[pr-guide]: https://guides.github.com/activities/forking/#making-a-pull-request
[pulls]: https://github.com/carpentries/glosario/pulls
[repo]: https://github.com/carpentries/glosario
[yaml]: https://learnxinyminutes.com/docs/yaml/
