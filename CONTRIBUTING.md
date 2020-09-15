Thank you for your interest in contributing to Glosario!
We welcome contributions of all kinds.
If you're here to submit a definition,
either for a new term 
or in another language for an existing term,
please take a moment to read the guidance below.

## 1. Adding a new term to the glossary

To add a new entry, please [fork][forking-guide] the [main Glosario repository][repo]
and, on a new branch,
add the term and definition to [`glossary.yml`][glossary].
This glossary file is written in [YAML].
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

Once your term and definition(s) are complete,
[make a Pull Request][pr-guide] back to the main repository.

### 2. Adding a definition in another language to an existing term

To add a new definition to an existing term in the glossary,
please fork [the main Glosario repository][repo]
and, on a new branch,
find the term in [`glossary.yml`][glossary] and
add the two-letter ISO 639 language code such as `en` or `fr`
as a new top-level key.
(Refer to the "639-1" column of [this table][iso639-table-en].)
You can then fill in the `term`, `def`, and (if appropriate) `acronym` for that term in your chosen language.
See the section above for a full description of the required format for a language term.

## Guide to contributing

When you're making your contribution(s) to Glosario, please keep the following
guidance in mind:

1. **Check the [Issues page of the Glosario repository][issues]**
  to see what terms and definitions other contributors are already working on.
  This will help you avoid accidentally spending time writing the same
  term(s)/definition(s) as someone else.
2. When you know what term or definition you'd like to add,
  tell others about it by writing
  **a [new issue] on the main Glosario repository.**
3. **Add one new term or definition per Pull Request.**
  We'd love to receive multiple contributions from you but please
  keep each separate new term or definition in a distinct branch (see below) and Pull Request.
  This makes it much easier for the Glosario maintainers/editors to review your contributions.
  When you open the Pull Request you can refer to the Issue you opened before (see step 2), 
  e.g. by writing "Fixes \#49."
  GitHub will then automatically close the Issue if and when your Pull Request is merged.
4. When making multiple contributions, please **[create a new branch][github-branches] for each term/definition.**
  Add the new term/definition on a separate branch,
  created from the `master` branch, and make a new Pull Request each time.
  This will help you avoid accidentally combining multiple contributions in a single Pull Request.

[forking-guide]: https://guides.github.com/activities/forking/
[github-branches]: https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-branches
[glossary]: https://github.com/carpentries/glosario/blob/master/glossary.yml
[iso639-table-en]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[issues]: https://github.com/carpentries/glosario/issues
[new issue]: https://github.com/carpentries/glosario/issues/new
[pr-guide]: https://guides.github.com/activities/forking/#making-a-pull-request
[repo]: https://github.com/carpentries/glosario
[yaml]: https://learnxinyminutes.com/docs/yaml/
