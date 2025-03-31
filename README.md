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

## Contributing

[![All Contributors](https://img.shields.io/github/all-contributors/carpentries/glosario?color=ee8449&style=flat-square)](#contributors)

To advance data science knowledge and accessibility for our diverse community, we developed Glosario. You do not need to know any programming language to contribute to Glosario: anyone with a basic familiarity with the GitHub web interface can get involved! We have prepared a [detailed and accessible guide for contributing](https://docs.google.com/document/d/18oxYd6D9heESqw2gw9cbtxiCfkb4wlxazERFBIDCoeM/edit#heading=h.wsi1psxc3n64), which has been translated into several languages. Contributions are welcome in any language, not only those represented in that document. If you need help with your contribution, feel free to come to ask questions on the [#glosario](https://carpentries.slack.com/archives/C01G4HYGAQ6) Slack channel (if you are not a member of The Carpentries Slack you can join by filling [this form](https://slack-invite.carpentries.org/)).

## Lessons

R Markdown and Jupyter Notebooks allow authors to place structured metadata in files.
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
1.  The `language` key is required
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

We will provide simple tools so that
all of the terms listed in a lesson's metadata are linked correctly in its body.
We will also provide shortcuts to make it easy to create correctly-formatted links
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
        1.  Searches the document's body for calls to `gdef(...)`.
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
            to read metadata from all of the lessons she has archived.
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
    However, Wikipedia articles provide explanations, not definitions.

-   **YAML is hard for people to edit—why not use something else for the glossary file?**
    Because other formats are just as hard to edit (e.g., JSON)
    or make one-to-many relationships hard to express (e.g., CSV).

-   **Why use Jekyll for the online version?**
    It is the default for GitHub Pages.

## Funding and Collaborators

[SADiLaR](https://sadilar.org/en/) is one of the collaborators in the finalisation and expansion of the Glosario
Project to African Languages. SADiLaR is a research infrastructure established by the
Department of Science and Innovation of the South African government as part of the
South African Research Infrastructure Roadmap (SARIR).
 
We are pleased to share that the Andrew W. Mellon Foundation approved a grant for use 
over 12 months (November 2023 through October 2024) to support an upgrade to Glosario. Additionally, further funding has been secured from the Foundation to continue developing this resource from January 1, 2025, through December 31, 2025.

## Credits

-   Parrot logo by [restocktheshelves](https://www.deviantart.com/restocktheshelves).

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/elletjies"><img src="https://avatars.githubusercontent.com/u/28295969?v=4?s=100" width="100px;" alt="Angelique Trusler"/><br /><sub><b>Angelique Trusler</b></sub></a><br /><a href="#doc-elletjies" title="Documentation">📖</a> <a href="#review-elletjies" title="Reviewed Pull Requests">👀</a> <a href="#question-elletjies" title="Answering Questions">💬</a> <a href="#translation-elletjies" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://francoismichonneau.net/"><img src="https://avatars.githubusercontent.com/u/5502922?v=4?s=100" width="100px;" alt="François Michonneau"/><br /><sub><b>François Michonneau</b></sub></a><br /><a href="#doc-fmichonneau" title="Documentation">📖</a> <a href="#review-fmichonneau" title="Reviewed Pull Requests">👀</a> <a href="#question-fmichonneau" title="Answering Questions">💬</a> <a href="#translation-fmichonneau" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://third-bit.com"><img src="https://avatars.githubusercontent.com/u/911566?v=4?s=100" width="100px;" alt="Greg Wilson"/><br /><sub><b>Greg Wilson</b></sub></a><br /><a href="#doc-gvwilson" title="Documentation">📖</a> <a href="#review-gvwilson" title="Reviewed Pull Requests">👀</a> <a href="#question-gvwilson" title="Answering Questions">💬</a> <a href="#translation-gvwilson" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://yabellini.netlify.app"><img src="https://avatars.githubusercontent.com/u/2473676?v=4?s=100" width="100px;" alt="Yanina Bellini Saibene"/><br /><sub><b>Yanina Bellini Saibene</b></sub></a><br /><a href="#doc-yabellini" title="Documentation">📖</a> <a href="#review-yabellini" title="Reviewed Pull Requests">👀</a> <a href="#question-yabellini" title="Answering Questions">💬</a> <a href="#translation-yabellini" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ianfs.dev"><img src="https://avatars.githubusercontent.com/u/18703558?v=4?s=100" width="100px;" alt="Ian Flores Siaca "/><br /><sub><b>Ian Flores Siaca </b></sub></a><br /><a href="#doc-ian-flores" title="Documentation">📖</a> <a href="#review-ian-flores" title="Reviewed Pull Requests">👀</a> <a href="#question-ian-flores" title="Answering Questions">💬</a> <a href="#translation-ian-flores" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Armadilloa16"><img src="https://avatars.githubusercontent.com/u/11642131?v=4?s=100" width="100px;" alt="Lyron Winderbaum"/><br /><sub><b>Lyron Winderbaum</b></sub></a><br /><a href="#translation-Armadilloa16" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/BFrit"><img src="https://avatars.githubusercontent.com/u/32676777?v=4?s=100" width="100px;" alt="BFrit"/><br /><sub><b>BFrit</b></sub></a><br /><a href="#translation-BFrit" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://batool-almarzouq.netlify.app/"><img src="https://avatars.githubusercontent.com/u/53487593?v=4?s=100" width="100px;" alt="Batool Almarzouq"/><br /><sub><b>Batool Almarzouq</b></sub></a><br /><a href="#review-BatoolMM" title="Reviewed Pull Requests">👀</a> <a href="#translation-BatoolMM" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Charlie-George"><img src="https://avatars.githubusercontent.com/u/8723681?v=4?s=100" width="100px;" alt="Charlie-George"/><br /><sub><b>Charlie-George</b></sub></a><br /><a href="#translation-Charlie-George" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://eirinits.github.io/"><img src="https://avatars.githubusercontent.com/u/40056377?v=4?s=100" width="100px;" alt="Eirini Tsirvouli"/><br /><sub><b>Eirini Tsirvouli</b></sub></a><br /><a href="#translation-Eirinits" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/EveBigras"><img src="https://avatars.githubusercontent.com/u/12716168?v=4?s=100" width="100px;" alt="EveBigras"/><br /><sub><b>EveBigras</b></sub></a><br /><a href="#translation-EveBigras" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Fehings"><img src="https://avatars.githubusercontent.com/u/22681345?v=4?s=100" width="100px;" alt="Frances Turner"/><br /><sub><b>Frances Turner</b></sub></a><br /><a href="#translation-Fehings" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/GenevieveMilliken"><img src="https://avatars.githubusercontent.com/u/39474494?v=4?s=100" width="100px;" alt="Genevieve Milliken"/><br /><sub><b>Genevieve Milliken</b></sub></a><br /><a href="#translation-GenevieveMilliken" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://about.me/lilithelina"><img src="https://avatars.githubusercontent.com/u/7427134?v=4?s=100" width="100px;" alt="Sarah Pohl"/><br /><sub><b>Sarah Pohl</b></sub></a><br /><a href="#translation-LilithElina" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MarieHouillon"><img src="https://avatars.githubusercontent.com/u/17878878?v=4?s=100" width="100px;" alt="Marie Houillon"/><br /><sub><b>Marie Houillon</b></sub></a><br /><a href="#translation-MarieHouillon" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MikeResearch"><img src="https://avatars.githubusercontent.com/u/66963319?v=4?s=100" width="100px;" alt="MikeResearch"/><br /><sub><b>MikeResearch</b></sub></a><br /><a href="#translation-MikeResearch" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MysteryBlokHed"><img src="https://avatars.githubusercontent.com/u/13910387?v=4?s=100" width="100px;" alt="Adam Thompson-Sharpe"/><br /><sub><b>Adam Thompson-Sharpe</b></sub></a><br /><a href="#translation-MysteryBlokHed" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://about.me/npalopoli"><img src="https://avatars.githubusercontent.com/u/1713937?v=4?s=100" width="100px;" alt="Nicolas Palopoli"/><br /><sub><b>Nicolas Palopoli</b></sub></a><br /><a href="#translation-NPalopoli" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RabeaMue"><img src="https://avatars.githubusercontent.com/u/42644523?v=4?s=100" width="100px;" alt="Rabea Müller"/><br /><sub><b>Rabea Müller</b></sub></a><br /><a href="#translation-RabeaMue" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/0000-0003-3904-6690"><img src="https://avatars.githubusercontent.com/u/5493325?v=4?s=100" width="100px;" alt="Tom Kelly"/><br /><sub><b>Tom Kelly</b></sub></a><br /><a href="#review-TomKellyGenetics" title="Reviewed Pull Requests">👀</a> <a href="#translation-TomKellyGenetics" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/WafaaMoh"><img src="https://avatars.githubusercontent.com/u/74782178?v=4?s=100" width="100px;" alt="WafaaMoh"/><br /><sub><b>WafaaMoh</b></sub></a><br /><a href="#translation-WafaaMoh" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ailisarre"><img src="https://avatars.githubusercontent.com/u/73651518?v=4?s=100" width="100px;" alt="Aili Sarre"/><br /><sub><b>Aili Sarre</b></sub></a><br /><a href="#translation-ailisarre" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://annajiat.googlepages.com/"><img src="https://avatars.githubusercontent.com/u/3046889?v=4?s=100" width="100px;" alt="Annajiat Alim Rasel"/><br /><sub><b>Annajiat Alim Rasel</b></sub></a><br /><a href="#translation-annajiat" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/baileythegreen"><img src="https://avatars.githubusercontent.com/u/12277715?v=4?s=100" width="100px;" alt="Bailey Harrington"/><br /><sub><b>Bailey Harrington</b></sub></a><br /><a href="#doc-baileythegreen" title="Documentation">📖</a> <a href="#review-baileythegreen" title="Reviewed Pull Requests">👀</a> <a href="#question-baileythegreen" title="Answering Questions">💬</a> <a href="#translation-baileythegreen" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://bawee.github.io"><img src="https://avatars.githubusercontent.com/u/4733347?v=4?s=100" width="100px;" alt="Bryan Wee"/><br /><sub><b>Bryan Wee</b></sub></a><br /><a href="#translation-bawee" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://belindafabian.com.au"><img src="https://avatars.githubusercontent.com/u/32319878?v=4?s=100" width="100px;" alt="beacurious"/><br /><sub><b>beacurious</b></sub></a><br /><a href="#translation-beacurious" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://beamilz.com"><img src="https://avatars.githubusercontent.com/u/42153618?v=4?s=100" width="100px;" alt="Beatriz Milz"/><br /><sub><b>Beatriz Milz</b></sub></a><br /><a href="#translation-beatrizmilz" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://callumrollo.com"><img src="https://avatars.githubusercontent.com/u/28703282?v=4?s=100" width="100px;" alt="Callum Rollo"/><br /><sub><b>Callum Rollo</b></sub></a><br /><a href="#translation-callumrollo" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/chaimae123-ai"><img src="https://avatars.githubusercontent.com/u/66030422?v=4?s=100" width="100px;" alt="chaimae123-ai"/><br /><sub><b>chaimae123-ai</b></sub></a><br /><a href="#translation-chaimae123-ai" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dannyba"><img src="https://avatars.githubusercontent.com/u/4780507?v=4?s=100" width="100px;" alt="Danny Ben-Avraham"/><br /><sub><b>Danny Ben-Avraham</b></sub></a><br /><a href="#translation-dannyba" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mariadermit.netlify.app/"><img src="https://avatars.githubusercontent.com/u/5008157?v=4?s=100" width="100px;" alt="Maria Dermit"/><br /><sub><b>Maria Dermit</b></sub></a><br /><a href="#translation-demar01" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/elsikorski"><img src="https://avatars.githubusercontent.com/u/20630148?v=4?s=100" width="100px;" alt="elsikorski"/><br /><sub><b>elsikorski</b></sub></a><br /><a href="#doc-elsikorski" title="Documentation">📖</a> <a href="#translation-elsikorski" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/feddelegrand7"><img src="https://avatars.githubusercontent.com/u/28841210?v=4?s=100" width="100px;" alt="Ihaddaden Mohamed El Fodil"/><br /><sub><b>Ihaddaden Mohamed El Fodil</b></sub></a><br /><a href="#doc-feddelegrand7" title="Documentation">📖</a> <a href="#translation-feddelegrand7" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/fiona-galston"><img src="https://avatars.githubusercontent.com/u/49239621?v=4?s=100" width="100px;" alt="Fiona"/><br /><sub><b>Fiona</b></sub></a><br /><a href="#translation-fiona-galston" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.fpozoc.com"><img src="https://avatars.githubusercontent.com/u/19167350?v=4?s=100" width="100px;" alt="Fernando Pozo"/><br /><sub><b>Fernando Pozo</b></sub></a><br /><a href="#translation-fpozoc" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/groodri"><img src="https://avatars.githubusercontent.com/u/22616857?v=4?s=100" width="100px;" alt="Rodrigo Meneses"/><br /><sub><b>Rodrigo Meneses</b></sub></a><br /><a href="#translation-groodri" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/heidikarlsen"><img src="https://avatars.githubusercontent.com/u/56078217?v=4?s=100" width="100px;" alt="heidikarlsen"/><br /><sub><b>heidikarlsen</b></sub></a><br /><a href="#translation-heidikarlsen" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.edf.org/people/jamie-collins"><img src="https://avatars.githubusercontent.com/u/12241873?v=4?s=100" width="100px;" alt="Jamie Collins"/><br /><sub><b>Jamie Collins</b></sub></a><br /><a href="#translation-jamesrco" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jananiharan"><img src="https://avatars.githubusercontent.com/u/8431485?v=4?s=100" width="100px;" alt="Janani Hariharan"/><br /><sub><b>Janani Hariharan</b></sub></a><br /><a href="#translation-jananiharan" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jas1"><img src="https://avatars.githubusercontent.com/u/1795403?v=4?s=100" width="100px;" alt="Julio Spairani"/><br /><sub><b>Julio Spairani</b></sub></a><br /><a href="#translation-jas1" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://faculty.washington.edu/ychoe/"><img src="https://avatars.githubusercontent.com/u/3599146?v=4?s=100" width="100px;" alt="John Y. Choe"/><br /><sub><b>John Y. Choe</b></sub></a><br /><a href="#translation-joun58" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.jannetta.com"><img src="https://avatars.githubusercontent.com/u/6432530?v=4?s=100" width="100px;" alt="Jannetta Steyn"/><br /><sub><b>Jannetta Steyn</b></sub></a><br /><a href="#translation-jsteyn" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/julievecchio"><img src="https://avatars.githubusercontent.com/u/11231049?v=4?s=100" width="100px;" alt="julievecchio"/><br /><sub><b>julievecchio</b></sub></a><br /><a href="#translation-julievecchio" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://konrad.foerstner.org"><img src="https://avatars.githubusercontent.com/u/49392?v=4?s=100" width="100px;" alt="Konrad Förstner"/><br /><sub><b>Konrad Förstner</b></sub></a><br /><a href="#translation-konrad" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/leedotson"><img src="https://avatars.githubusercontent.com/u/80065598?v=4?s=100" width="100px;" alt="leedotson"/><br /><sub><b>leedotson</b></sub></a><br /><a href="#translation-leedotson" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://leticiadasilva.github.io"><img src="https://avatars.githubusercontent.com/u/28828381?v=4?s=100" width="100px;" alt="Letícia Silva"/><br /><sub><b>Letícia Silva</b></sub></a><br /><a href="#translation-leticiadasilva" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lmtnezg"><img src="https://avatars.githubusercontent.com/u/33230752?v=4?s=100" width="100px;" alt="Laura Mtnez"/><br /><sub><b>Laura Mtnez</b></sub></a><br /><a href="#translation-lmtnezg" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lucaferranti"><img src="https://avatars.githubusercontent.com/u/49938764?v=4?s=100" width="100px;" alt="Luca Ferranti"/><br /><sub><b>Luca Ferranti</b></sub></a><br /><a href="#translation-lucaferranti" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/manuGil"><img src="https://avatars.githubusercontent.com/u/8195424?v=4?s=100" width="100px;" alt="Manuel Garcia"/><br /><sub><b>Manuel Garcia</b></sub></a><br /><a href="#translation-manuGil" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://marcosvital.github.io"><img src="https://avatars.githubusercontent.com/u/13972235?v=4?s=100" width="100px;" alt="Marcos Vital (LEQ-UFAL)"/><br /><sub><b>Marcos Vital (LEQ-UFAL)</b></sub></a><br /><a href="#translation-marcosvital" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/masamiy"><img src="https://avatars.githubusercontent.com/u/19921944?v=4?s=100" width="100px;" alt="masamiy"/><br /><sub><b>masamiy</b></sub></a><br /><a href="#translation-masamiy" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://matiasmicheletto.github.io"><img src="https://avatars.githubusercontent.com/u/21092034?v=4?s=100" width="100px;" alt="Matias Micheletto"/><br /><sub><b>Matias Micheletto</b></sub></a><br /><a href="#translation-matiasmicheletto" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mdbjax"><img src="https://avatars.githubusercontent.com/u/52707406?v=4?s=100" width="100px;" alt="mdbjax"/><br /><sub><b>mdbjax</b></sub></a><br /><a href="#translation-mdbjax" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://mpaulacaldas.com"><img src="https://avatars.githubusercontent.com/u/33395215?v=4?s=100" width="100px;" alt="María Paula Caldas"/><br /><sub><b>María Paula Caldas</b></sub></a><br /><a href="#translation-mpaulacaldas" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nanjalaruth"><img src="https://avatars.githubusercontent.com/u/55382239?v=4?s=100" width="100px;" alt="Nanjala Ruth"/><br /><sub><b>Nanjala Ruth</b></sub></a><br /><a href="#translation-nanjalaruth" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.usit.uio.no/english/about/organisation/rc/dcm/staff/naoeta/index.html"><img src="https://avatars.githubusercontent.com/u/56588774?v=4?s=100" width="100px;" alt="Naoe Tatara"/><br /><sub><b>Naoe Tatara</b></sub></a><br /><a href="#translation-naoe-tatara" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://nicoguaro.github.io"><img src="https://avatars.githubusercontent.com/u/1097787?v=4?s=100" width="100px;" alt="Nicolás Guarín-Zapata"/><br /><sub><b>Nicolás Guarín-Zapata</b></sub></a><br /><a href="#translation-nicoguaro" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nucholab"><img src="https://avatars.githubusercontent.com/u/30484657?v=4?s=100" width="100px;" alt="Wladimir"/><br /><sub><b>Wladimir</b></sub></a><br /><a href="#translation-nucholab" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://stackoverflow.com/users/4334110/paritosh-kulkarni"><img src="https://avatars.githubusercontent.com/u/9400939?v=4?s=100" width="100px;" alt="Paritosh Kulkarni"/><br /><sub><b>Paritosh Kulkarni</b></sub></a><br /><a href="#translation-paritoshk" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pri-hoh"><img src="https://avatars.githubusercontent.com/u/30275921?v=4?s=100" width="100px;" alt="Priscila Hohberg"/><br /><sub><b>Priscila Hohberg</b></sub></a><br /><a href="#translation-pri-hoh" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://rivaquiroga.cl/"><img src="https://avatars.githubusercontent.com/u/31421616?v=4?s=100" width="100px;" alt="Riva Quiroga"/><br /><sub><b>Riva Quiroga</b></sub></a><br /><a href="#translation-rivaquiroga" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sackmanna"><img src="https://avatars.githubusercontent.com/u/20346805?v=4?s=100" width="100px;" alt="Anna Sackmann"/><br /><sub><b>Anna Sackmann</b></sub></a><br /><a href="#translation-sackmanna" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://sarahlrstevens.info"><img src="https://avatars.githubusercontent.com/u/5558419?v=4?s=100" width="100px;" alt="Sarah Stevens"/><br /><sub><b>Sarah Stevens</b></sub></a><br /><a href="#translation-sstevens2" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://tgconsulting.ca"><img src="https://avatars.githubusercontent.com/u/7302575?v=4?s=100" width="100px;" alt="Thomas Guignard"/><br /><sub><b>Thomas Guignard</b></sub></a><br /><a href="#translation-timtomch" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://tbyhdgs.info"><img src="https://avatars.githubusercontent.com/u/9694524?v=4?s=100" width="100px;" alt="Toby Hodges"/><br /><sub><b>Toby Hodges</b></sub></a><br /><a href="#doc-tobyhodges" title="Documentation">📖</a> <a href="#question-tobyhodges" title="Answering Questions">💬</a> <a href="#translation-tobyhodges" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tyt3"><img src="https://avatars.githubusercontent.com/u/34420663?v=4?s=100" width="100px;" alt="Tyrica Terry Kapral"/><br /><sub><b>Tyrica Terry Kapral</b></sub></a><br /><a href="#translation-tyt3" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://abav.lugaralgum.com"><img src="https://avatars.githubusercontent.com/u/3694604?v=4?s=100" width="100px;" alt="Alexandre B A Villares"/><br /><sub><b>Alexandre B A Villares</b></sub></a><br /><a href="#translation-villares" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://zkamvar.netlify.app"><img src="https://avatars.githubusercontent.com/u/3639446?v=4?s=100" width="100px;" alt="Zhian N. Kamvar"/><br /><sub><b>Zhian N. Kamvar</b></sub></a><br /><a href="#doc-zkamvar" title="Documentation">📖</a> <a href="#review-zkamvar" title="Reviewed Pull Requests">👀</a> <a href="#question-zkamvar" title="Answering Questions">💬</a> <a href="#translation-zkamvar" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sfmig"><img src="https://avatars.githubusercontent.com/u/33267254?v=4?s=100" width="100px;" alt="sfmig"/><br /><sub><b>sfmig</b></sub></a><br /><a href="#translation-sfmig" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://olexandr-konovalov.github.io"><img src="https://avatars.githubusercontent.com/u/5751387?v=4?s=100" width="100px;" alt="Olexandr Konovalov"/><br /><sub><b>Olexandr Konovalov</b></sub></a><br /><a href="#translation-olexandr-konovalov" title="Translation">🌍</a> <a href="#review-olexandr-konovalov" title="Reviewed Pull Requests">👀</a> <a href="#question-olexandr-konovalov" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kashpit0507"><img src="https://avatars.githubusercontent.com/u/47479385?v=4?s=100" width="100px;" alt="spiciment"/><br /><sub><b>spiciment</b></sub></a><br /><a href="#translation-kashpit0507" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/VeronikaShevc"><img src="https://avatars.githubusercontent.com/u/147643787?v=4?s=100" width="100px;" alt="VeronikaShevc"/><br /><sub><b>VeronikaShevc</b></sub></a><br /><a href="#translation-VeronikaShevc" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Herobread"><img src="https://avatars.githubusercontent.com/u/52717777?v=4?s=100" width="100px;" alt="Oleksii Nazarenko"/><br /><sub><b>Oleksii Nazarenko</b></sub></a><br /><a href="#translation-Herobread" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/YehorBoiar"><img src="https://avatars.githubusercontent.com/u/94189697?v=4?s=100" width="100px;" alt="Yehor Boiar"/><br /><sub><b>Yehor Boiar</b></sub></a><br /><a href="#translation-YehorBoiar" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/doerners"><img src="https://avatars.githubusercontent.com/u/38356908?v=4?s=100" width="100px;" alt="Sophia Dörner"/><br /><sub><b>Sophia Dörner</b></sub></a><br /><a href="#translation-doerners" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mariyaspatar"><img src="https://avatars.githubusercontent.com/u/135342983?v=4?s=100" width="100px;" alt="mariyaspatar"/><br /><sub><b>mariyaspatar</b></sub></a><br /><a href="#translation-mariyaspatar" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sofiiamatios"><img src="https://avatars.githubusercontent.com/u/125209985?v=4?s=100" width="100px;" alt="sofiiamatios"/><br /><sub><b>sofiiamatios</b></sub></a><br /><a href="#translation-sofiiamatios" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/iramosp"><img src="https://avatars.githubusercontent.com/u/8619939?v=4?s=100" width="100px;" alt="iramosp"/><br /><sub><b>iramosp</b></sub></a><br /><a href="#translation-iramosp" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/OscarSiba"><img src="https://avatars.githubusercontent.com/u/132367843?v=4?s=100" width="100px;" alt="Oscar Masinyana"/><br /><sub><b>Oscar Masinyana</b></sub></a><br /><a href="#translation-OscarSiba" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/josenino95"><img src="https://avatars.githubusercontent.com/u/72319858?v=4?s=100" width="100px;" alt="Jose Niño"/><br /><sub><b>Jose Niño</b></sub></a><br /><a href="#translation-josenino95" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/marionwalton"><img src="https://avatars.githubusercontent.com/u/4045958?v=4?s=100" width="100px;" alt="Marion Walton"/><br /><sub><b>Marion Walton</b></sub></a><br /><a href="#translation-marionwalton" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/winfrednyoroka"><img src="https://avatars.githubusercontent.com/u/40457085?v=4?s=100" width="100px;" alt="Winfred_Gatua"/><br /><sub><b>Winfred_Gatua</b></sub></a><br /><a href="#translation-winfrednyoroka" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://paocorrales.github.io"><img src="https://avatars.githubusercontent.com/u/9036871?v=4?s=100" width="100px;" alt="Paola Corrales"/><br /><sub><b>Paola Corrales</b></sub></a><br /><a href="#translation-paocorrales" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://aprendetidyverse.com"><img src="https://avatars.githubusercontent.com/u/17366889?v=4?s=100" width="100px;" alt="Carlos Agüero B."/><br /><sub><b>Carlos Agüero B.</b></sub></a><br /><a href="#translation-aguerodev" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Alicia-Talavera"><img src="https://avatars.githubusercontent.com/u/12556709?v=4?s=100" width="100px;" alt="Alicia Talavera "/><br /><sub><b>Alicia Talavera </b></sub></a><br /><a href="#translation-Alicia-Talavera" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ShrRa"><img src="https://avatars.githubusercontent.com/u/16464387?v=4?s=100" width="100px;" alt="ShrRa"/><br /><sub><b>ShrRa</b></sub></a><br /><a href="#translation-ShrRa" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MarielenaS"><img src="https://avatars.githubusercontent.com/u/38910258?v=4?s=100" width="100px;" alt="~Way of the Wug"/><br /><sub><b>~Way of the Wug</b></sub></a><br /><a href="#translation-MarielenaS" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hernandezj1"><img src="https://avatars.githubusercontent.com/u/98195541?v=4?s=100" width="100px;" alt="Jose Hernandez"/><br /><sub><b>Jose Hernandez</b></sub></a><br /><a href="#translation-hernandezj1" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://alvaradocss.com"><img src="https://avatars.githubusercontent.com/u/97917730?v=4?s=100" width="100px;" alt="Edwin Alvarado-Mena"/><br /><sub><b>Edwin Alvarado-Mena</b></sub></a><br /><a href="#translation-ealvaradomena" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/svenvanderburg"><img src="https://avatars.githubusercontent.com/u/9945255?v=4?s=100" width="100px;" alt="Sven van der Burg"/><br /><sub><b>Sven van der Burg</b></sub></a><br /><a href="#translation-svenvanderburg" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://sites.google.com/view/abhishekchakraborty"><img src="https://avatars.githubusercontent.com/u/6579069?v=4?s=100" width="100px;" alt="Abhishek Chakraborty"/><br /><sub><b>Abhishek Chakraborty</b></sub></a><br /><a href="#translation-abhicc" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/katia-slc"><img src="https://avatars.githubusercontent.com/u/54743399?v=4?s=100" width="100px;" alt="Katia Slodkowski Clerici"/><br /><sub><b>Katia Slodkowski Clerici</b></sub></a><br /><a href="#translation-katia-slc" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jcostacurta11.github.io/"><img src="https://avatars.githubusercontent.com/u/13225001?v=4?s=100" width="100px;" alt="Julia Costacurta"/><br /><sub><b>Julia Costacurta</b></sub></a><br /><a href="#translation-jcostacurta11" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/likeajumprope"><img src="https://avatars.githubusercontent.com/u/23728822?v=4?s=100" width="100px;" alt="Johanna Bayer"/><br /><sub><b>Johanna Bayer</b></sub></a><br /><a href="#translation-likeajumprope" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MaggiK"><img src="https://avatars.githubusercontent.com/u/18407416?v=4?s=100" width="100px;" alt="Maggi Kraft"/><br /><sub><b>Maggi Kraft</b></sub></a><br /><a href="#translation-MaggiK" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dsmits"><img src="https://avatars.githubusercontent.com/u/131889?v=4?s=100" width="100px;" alt="Djura"/><br /><sub><b>Djura</b></sub></a><br /><a href="#translation-dsmits" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JMorado"><img src="https://avatars.githubusercontent.com/u/7460993?v=4?s=100" width="100px;" alt="João Morado"/><br /><sub><b>João Morado</b></sub></a><br /><a href="#translation-JMorado" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://epicworld.co.ke/"><img src="https://avatars.githubusercontent.com/u/14215807?v=4?s=100" width="100px;" alt="Ken Mbuki"/><br /><sub><b>Ken Mbuki</b></sub></a><br /><a href="#translation-kmbuki" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rosemm"><img src="https://avatars.githubusercontent.com/u/9002194?v=4?s=100" width="100px;" alt="Rose M. Hartman"/><br /><sub><b>Rose M. Hartman</b></sub></a><br /><a href="#translation-rosemm" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/edinkasia"><img src="https://avatars.githubusercontent.com/u/37267064?v=4?s=100" width="100px;" alt="Kasia Banas"/><br /><sub><b>Kasia Banas</b></sub></a><br /><a href="#translation-edinkasia" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/PatriciaSA"><img src="https://avatars.githubusercontent.com/u/41639685?v=4?s=100" width="100px;" alt="PatriciaSA"/><br /><sub><b>PatriciaSA</b></sub></a><br /><a href="#translation-PatriciaSA" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.linkedin.com/in/didier-barradas-bautista"><img src="https://avatars.githubusercontent.com/u/17081199?v=4?s=100" width="100px;" alt="Didier Barradas Bautista"/><br /><sub><b>Didier Barradas Bautista</b></sub></a><br /><a href="#translation-D-Barradas" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cmdalton"><img src="https://avatars.githubusercontent.com/u/36085215?v=4?s=100" width="100px;" alt="cmdalton"/><br /><sub><b>cmdalton</b></sub></a><br /><a href="#translation-cmdalton" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jameswarduwa"><img src="https://avatars.githubusercontent.com/u/114635946?v=4?s=100" width="100px;" alt="jameswarduwa"/><br /><sub><b>jameswarduwa</b></sub></a><br /><a href="#translation-jameswarduwa" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Dallak"><img src="https://avatars.githubusercontent.com/u/47871346?v=4?s=100" width="100px;" alt="Abdulrahman Dallak"/><br /><sub><b>Abdulrahman Dallak</b></sub></a><br /><a href="#translation-Dallak" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ianvcaldas"><img src="https://avatars.githubusercontent.com/u/22592759?v=4?s=100" width="100px;" alt="Ian"/><br /><sub><b>Ian</b></sub></a><br /><a href="#translation-ianvcaldas" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://asiermoneva.com/"><img src="https://avatars.githubusercontent.com/u/49791526?v=4?s=100" width="100px;" alt="Asier Moneva"/><br /><sub><b>Asier Moneva</b></sub></a><br /><a href="#translation-amoneva" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/clem33"><img src="https://avatars.githubusercontent.com/u/1318877?v=4?s=100" width="100px;" alt="clem33"/><br /><sub><b>clem33</b></sub></a><br /><a href="#translation-clem33" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dougdaniels"><img src="https://avatars.githubusercontent.com/u/27438900?v=4?s=100" width="100px;" alt="dougdaniels"/><br /><sub><b>dougdaniels</b></sub></a><br /><a href="#translation-dougdaniels" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://warrickball.gitlab.io"><img src="https://avatars.githubusercontent.com/u/20858744?v=4?s=100" width="100px;" alt="Warrick Ball"/><br /><sub><b>Warrick Ball</b></sub></a><br /><a href="#translation-warrickball" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/NOngeso"><img src="https://avatars.githubusercontent.com/u/47664805?v=4?s=100" width="100px;" alt="Nehemiah Ongeso"/><br /><sub><b>Nehemiah Ongeso</b></sub></a><br /><a href="#translation-NOngeso" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://imre.app"><img src="https://avatars.githubusercontent.com/u/52718007?v=4?s=100" width="100px;" alt="Imre Draskovits"/><br /><sub><b>Imre Draskovits</b></sub></a><br /><a href="#translation-imre" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://liaossanna.wixsite.com/liaos"><img src="https://avatars.githubusercontent.com/u/56702600?v=4?s=100" width="100px;" alt="Lia Ossanna"/><br /><sub><b>Lia Ossanna</b></sub></a><br /><a href="#translation-lossanna" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JClokey"><img src="https://avatars.githubusercontent.com/u/16443231?v=4?s=100" width="100px;" alt="JClokey"/><br /><sub><b>JClokey</b></sub></a><br /><a href="#translation-JClokey" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/eunicenjuguna"><img src="https://avatars.githubusercontent.com/u/72735080?v=4?s=100" width="100px;" alt="Waithira Njuguna"/><br /><sub><b>Waithira Njuguna</b></sub></a><br /><a href="#translation-eunicenjuguna" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bkmgit"><img src="https://avatars.githubusercontent.com/u/1679477?v=4?s=100" width="100px;" alt="Benson Muite"/><br /><sub><b>Benson Muite</b></sub></a><br /><a href="#translation-bkmgit" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ftabaro"><img src="https://avatars.githubusercontent.com/u/1375504?v=4?s=100" width="100px;" alt="Francesco Tabaro"/><br /><sub><b>Francesco Tabaro</b></sub></a><br /><a href="#translation-ftabaro" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Deisiany"><img src="https://avatars.githubusercontent.com/u/70155730?v=4?s=100" width="100px;" alt="Deisiany"/><br /><sub><b>Deisiany</b></sub></a><br /><a href="#translation-Deisiany" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.cbs.mpg.de/methods-and-development-groups/neural-data-science-and-statistical-computing"><img src="https://avatars.githubusercontent.com/u/2906267?v=4?s=100" width="100px;" alt="Nico Scherf"/><br /><sub><b>Nico Scherf</b></sub></a><br /><a href="#translation-nscherf" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://hperrythatchfield.com"><img src="https://avatars.githubusercontent.com/u/28646340?v=4?s=100" width="100px;" alt="H Perry Hatchfield"/><br /><sub><b>H Perry Hatchfield</b></sub></a><br /><a href="#translation-hpthatchfield" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/GorataB"><img src="https://avatars.githubusercontent.com/u/107930714?v=4?s=100" width="100px;" alt="Gorata Malose"/><br /><sub><b>Gorata Malose</b></sub></a><br /><a href="#translation-GorataB" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/talyacooper"><img src="https://avatars.githubusercontent.com/u/54854192?v=4?s=100" width="100px;" alt="talyacooper"/><br /><sub><b>talyacooper</b></sub></a><br /><a href="#translation-talyacooper" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://kamapu.github.io"><img src="https://avatars.githubusercontent.com/u/17233562?v=4?s=100" width="100px;" alt="Miguel Alvarez"/><br /><sub><b>Miguel Alvarez</b></sub></a><br /><a href="#translation-kamapu" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Taalmasoud"><img src="https://avatars.githubusercontent.com/u/96828378?v=4?s=100" width="100px;" alt="---"/><br /><sub><b>---</b></sub></a><br /><a href="#translation-Taalmasoud" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/BioNomad"><img src="https://avatars.githubusercontent.com/u/59677194?v=4?s=100" width="100px;" alt="Jason Laird"/><br /><sub><b>Jason Laird</b></sub></a><br /><a href="#translation-BioNomad" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dnoelsav"><img src="https://avatars.githubusercontent.com/u/11523698?v=4?s=100" width="100px;" alt="dnoelsav"/><br /><sub><b>dnoelsav</b></sub></a><br /><a href="#translation-dnoelsav" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vguillemot"><img src="https://avatars.githubusercontent.com/u/3502138?v=4?s=100" width="100px;" alt="Vincent Guillemot"/><br /><sub><b>Vincent Guillemot</b></sub></a><br /><a href="#translation-vguillemot" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://linkedin.com/in/iman-al-hasani-23a5b4a8"><img src="https://avatars.githubusercontent.com/u/48654637?v=4?s=100" width="100px;" alt="Iman Al Hasani"/><br /><sub><b>Iman Al Hasani</b></sub></a><br /><a href="#translation-imanalhasani" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mounabelaid.netlify.app/"><img src="https://avatars.githubusercontent.com/u/17770692?v=4?s=100" width="100px;" alt="Mouna Belaid"/><br /><sub><b>Mouna Belaid</b></sub></a><br /><a href="#translation-MounaBelaid" title="Translation">🌍</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
