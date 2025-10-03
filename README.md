# glosario

`glosario` is an open source glossary of terms used in data science that is available online. By adding glossary keys to a lesson's metadata, authors can indicate what the lesson teaches, what learners should know before they start, and where they can find that knowledge. Authors can also use the library's functions to insert consistent hyperlinks for terms and definitions in their lessons in several (human) languages. You can find the glossary here: [https://glosario.carpentries.org/](https://glosario.carpentries.org/)

# Table of Contents

- [Contributing](#contributing)
- [Structure of Glossary](#structure-of-glossary)
- [Funding and Collaborators](#funding-and-collaborators)
- [Credits](#credits)
- [Contributors](#contributors)


## Contributing


To advance data science knowledge and accessibility for our diverse community, we have developed Glosario, a multilingual glossary of data science terms. The easiest way to contribute is to use our [Google Form](https://forms.gle/FJkMsVhqn7qAgwjB8), which does not require any technical experience. 

If you are comfortable using GitHub, you can also contribute there. You do not need to know any programming language — a basic familiarity with the GitHub web interface is sufficient. We have prepared a [detailed and accessible guide](https://docs.google.com/document/d/18oxYd6D9heESqw2gw9cbtxiCfkb4wlxazERFBIDCoeM/edit?tab=t.0#heading=h.wsi1psxc3n64) to assist you. To support contributors further, we have also created short YouTube videos demonstrating how to contribute:

- [Recording in English](https://www.youtube.com/watch?v=ew1eb1ug-Q8)
- [Recording in Español](https://www.youtube.com/watch?v=f9K5wYq0dQM&t=23s)
- or you can [Auto Translate a YouTube Video into your Language](https://www.youtube.com/watch?v=LZz03myFuWA)

Contributions are welcome in any language, not only those currently represented in the glossary. If you need help with your contribution, you can ask questions in the #glosario Slack channel or email us at [community@carpentries.org](mailto:community@carpentries.org). If you are not yet a member of The Carpentries Slack, you may request access [here](https://slack-invite.carpentries.org/).

## Structure of Glossary

Any site where glossary URLS resolve can be used as a glossary.
This project implements a glossary of data science and data engineering terms as a working model.

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

You can access the glossary.yml dataset and citation information by clicking on the following DOI badge: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13589476.svg)](https://doi.org/10.5281/zenodo.13589476)


## Funding and Collaborators

[SADiLaR](https://sadilar.org/en/) is one of the collaborators in the finalisation and expansion of the Glosario
Project to African Languages. SADiLaR is a research infrastructure established by the
Department of Science and Innovation of the South African government as part of the
South African Research Infrastructure Roadmap (SARIR).
 
We are pleased to share that the [Andrew W. Mellon Foundation](https://www.mellon.org/) approved a grant for use 
over 12 months (November 2023 through October 2024) to support an upgrade to Glosario. Additionally, further funding has been secured from the Foundation to continue developing this resource from January 1, 2025, through December 31, 2025.

## Credits

-   Parrot logo by [restocktheshelves](https://www.deviantart.com/restocktheshelves).

## Contributors

[![All Contributors](https://img.shields.io/github/all-contributors/carpentries/glosario?color=ee8449&style=flat-square)](#contributors)

At The Carpentries, [every contribution matters](https://carpentries.org/about-us/#our-values). Individuals help open source projects in many ways: writing guides, reviewing other people’s work, translating content, or sharing ideas. These contributions all take time and effort. We want to thank everyone who helps Glosario grow - not only those who write code but also those who support the project in other ways.

We now show credit for four types of contributions:

- 📖 **Documentation and Planning** – Individuals who helped write the contribution guide, organise ideas, or plan how Glosario works.  
- 👀 **Pull Request Reviewers** – Individuals who read and gave feedback on new suggestions to improve the project.  
- 💬 **Discussion Participants** – Individuals who participated in conversations to help make decisions or solve problems.  
- 🌍 **Translators** – Individuals who translated words and meanings to make Glosario useful in many languages.



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
      <td align="center" valign="top" width="14.28%"><a href="https://batool-almarzouq.netlify.app/"><img src="https://avatars.githubusercontent.com/u/53487593?v=4?s=100" width="100px;" alt="Batool Almarzouq"/><br /><sub><b>Batool Almarzouq</b></sub></a><br /><a href="#review-BatoolMM" title="Reviewed Pull Requests">👀</a> <a href="#translation-BatoolMM" title="Translation">🌍</a> <a href="#question-BatoolMM" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Charlie-George"><img src="https://avatars.githubusercontent.com/u/8723681?v=4?s=100" width="100px;" alt="Charlie-George"/><br /><sub><b>Charlie-George</b></sub></a><br /><a href="#translation-Charlie-George" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://eirinits.github.io/"><img src="https://avatars.githubusercontent.com/u/40056377?v=4?s=100" width="100px;" alt="Eirini Tsirvouli"/><br /><sub><b>Eirini Tsirvouli</b></sub></a><br /><a href="#translation-Eirinits" title="Translation">🌍</a> <a href="#question-Eirinits" title="Answering Questions">💬</a></td>
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
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/0000-0003-3904-6690"><img src="https://avatars.githubusercontent.com/u/5493325?v=4?s=100" width="100px;" alt="Tom Kelly"/><br /><sub><b>Tom Kelly</b></sub></a><br /><a href="#review-TomKellyGenetics" title="Reviewed Pull Requests">👀</a> <a href="#translation-TomKellyGenetics" title="Translation">🌍</a> <a href="#question-TomKellyGenetics" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/WafaaMoh"><img src="https://avatars.githubusercontent.com/u/74782178?v=4?s=100" width="100px;" alt="WafaaMoh"/><br /><sub><b>WafaaMoh</b></sub></a><br /><a href="#translation-WafaaMoh" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ailisarre"><img src="https://avatars.githubusercontent.com/u/73651518?v=4?s=100" width="100px;" alt="Aili Sarre"/><br /><sub><b>Aili Sarre</b></sub></a><br /><a href="#translation-ailisarre" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://annajiat.googlepages.com/"><img src="https://avatars.githubusercontent.com/u/3046889?v=4?s=100" width="100px;" alt="Annajiat Alim Rasel"/><br /><sub><b>Annajiat Alim Rasel</b></sub></a><br /><a href="#translation-annajiat" title="Translation">🌍</a> <a href="#doc-annajiat" title="Documentation">📖</a> <a href="#question-annajiat" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/baileythegreen"><img src="https://avatars.githubusercontent.com/u/12277715?v=4?s=100" width="100px;" alt="Bailey Harrington"/><br /><sub><b>Bailey Harrington</b></sub></a><br /><a href="#doc-baileythegreen" title="Documentation">📖</a> <a href="#review-baileythegreen" title="Reviewed Pull Requests">👀</a> <a href="#question-baileythegreen" title="Answering Questions">💬</a> <a href="#translation-baileythegreen" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://bawee.github.io"><img src="https://avatars.githubusercontent.com/u/4733347?v=4?s=100" width="100px;" alt="Bryan Wee"/><br /><sub><b>Bryan Wee</b></sub></a><br /><a href="#translation-bawee" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://belindafabian.com.au"><img src="https://avatars.githubusercontent.com/u/32319878?v=4?s=100" width="100px;" alt="beacurious"/><br /><sub><b>beacurious</b></sub></a><br /><a href="#translation-beacurious" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://beamilz.com"><img src="https://avatars.githubusercontent.com/u/42153618?v=4?s=100" width="100px;" alt="Beatriz Milz"/><br /><sub><b>Beatriz Milz</b></sub></a><br /><a href="#translation-beatrizmilz" title="Translation">🌍</a> <a href="#review-beatrizmilz" title="Reviewed Pull Requests">👀</a> <a href="#question-beatrizmilz" title="Answering Questions">💬</a></td>
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
      <td align="center" valign="top" width="14.28%"><a href="http://www.jannetta.com"><img src="https://avatars.githubusercontent.com/u/6432530?v=4?s=100" width="100px;" alt="Jannetta Steyn"/><br /><sub><b>Jannetta Steyn</b></sub></a><br /><a href="#translation-jsteyn" title="Translation">🌍</a> <a href="#doc-jsteyn" title="Documentation">📖</a> <a href="#review-jsteyn" title="Reviewed Pull Requests">👀</a> <a href="#question-jsteyn" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/julievecchio"><img src="https://avatars.githubusercontent.com/u/11231049?v=4?s=100" width="100px;" alt="julievecchio"/><br /><sub><b>julievecchio</b></sub></a><br /><a href="#translation-julievecchio" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://konrad.foerstner.org"><img src="https://avatars.githubusercontent.com/u/49392?v=4?s=100" width="100px;" alt="Konrad Förstner"/><br /><sub><b>Konrad Förstner</b></sub></a><br /><a href="#translation-konrad" title="Translation">🌍</a> <a href="#question-konrad" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/leedotson"><img src="https://avatars.githubusercontent.com/u/80065598?v=4?s=100" width="100px;" alt="leedotson"/><br /><sub><b>leedotson</b></sub></a><br /><a href="#translation-leedotson" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://leticiadasilva.github.io"><img src="https://avatars.githubusercontent.com/u/28828381?v=4?s=100" width="100px;" alt="Letícia Silva"/><br /><sub><b>Letícia Silva</b></sub></a><br /><a href="#translation-leticiadasilva" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lmtnezg"><img src="https://avatars.githubusercontent.com/u/33230752?v=4?s=100" width="100px;" alt="Laura Mtnez"/><br /><sub><b>Laura Mtnez</b></sub></a><br /><a href="#translation-lmtnezg" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lucaferranti"><img src="https://avatars.githubusercontent.com/u/49938764?v=4?s=100" width="100px;" alt="Luca Ferranti"/><br /><sub><b>Luca Ferranti</b></sub></a><br /><a href="#translation-lucaferranti" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/manuGil"><img src="https://avatars.githubusercontent.com/u/8195424?v=4?s=100" width="100px;" alt="Manuel Garcia"/><br /><sub><b>Manuel Garcia</b></sub></a><br /><a href="#translation-manuGil" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://marcosvital.github.io"><img src="https://avatars.githubusercontent.com/u/13972235?v=4?s=100" width="100px;" alt="Marcos Vital (LEQ-UFAL)"/><br /><sub><b>Marcos Vital (LEQ-UFAL)</b></sub></a><br /><a href="#translation-marcosvital" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/masamiy"><img src="https://avatars.githubusercontent.com/u/19921944?v=4?s=100" width="100px;" alt="masamiy"/><br /><sub><b>masamiy</b></sub></a><br /><a href="#translation-masamiy" title="Translation">🌍</a> <a href="#review-masamiy" title="Reviewed Pull Requests">👀</a> <a href="#question-masamiy" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://matiasmicheletto.github.io"><img src="https://avatars.githubusercontent.com/u/21092034?v=4?s=100" width="100px;" alt="Matias Micheletto"/><br /><sub><b>Matias Micheletto</b></sub></a><br /><a href="#translation-matiasmicheletto" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mdbjax"><img src="https://avatars.githubusercontent.com/u/52707406?v=4?s=100" width="100px;" alt="mdbjax"/><br /><sub><b>mdbjax</b></sub></a><br /><a href="#translation-mdbjax" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://mpaulacaldas.com"><img src="https://avatars.githubusercontent.com/u/33395215?v=4?s=100" width="100px;" alt="María Paula Caldas"/><br /><sub><b>María Paula Caldas</b></sub></a><br /><a href="#translation-mpaulacaldas" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nanjalaruth"><img src="https://avatars.githubusercontent.com/u/55382239?v=4?s=100" width="100px;" alt="Nanjala Ruth"/><br /><sub><b>Nanjala Ruth</b></sub></a><br /><a href="#translation-nanjalaruth" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.usit.uio.no/english/about/organisation/rc/dcm/staff/naoeta/index.html"><img src="https://avatars.githubusercontent.com/u/56588774?v=4?s=100" width="100px;" alt="Naoe Tatara"/><br /><sub><b>Naoe Tatara</b></sub></a><br /><a href="#translation-naoe-tatara" title="Translation">🌍</a> <a href="#review-naoe-tatara" title="Reviewed Pull Requests">👀</a> <a href="#question-naoe-tatara" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://nicoguaro.github.io"><img src="https://avatars.githubusercontent.com/u/1097787?v=4?s=100" width="100px;" alt="Nicolás Guarín-Zapata"/><br /><sub><b>Nicolás Guarín-Zapata</b></sub></a><br /><a href="#translation-nicoguaro" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nucholab"><img src="https://avatars.githubusercontent.com/u/30484657?v=4?s=100" width="100px;" alt="Wladimir"/><br /><sub><b>Wladimir</b></sub></a><br /><a href="#translation-nucholab" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://stackoverflow.com/users/4334110/paritosh-kulkarni"><img src="https://avatars.githubusercontent.com/u/9400939?v=4?s=100" width="100px;" alt="Paritosh Kulkarni"/><br /><sub><b>Paritosh Kulkarni</b></sub></a><br /><a href="#translation-paritoshk" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pri-hoh"><img src="https://avatars.githubusercontent.com/u/30275921?v=4?s=100" width="100px;" alt="Priscila Hohberg"/><br /><sub><b>Priscila Hohberg</b></sub></a><br /><a href="#translation-pri-hoh" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://rivaquiroga.cl/"><img src="https://avatars.githubusercontent.com/u/31421616?v=4?s=100" width="100px;" alt="Riva Quiroga"/><br /><sub><b>Riva Quiroga</b></sub></a><br /><a href="#translation-rivaquiroga" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sackmanna"><img src="https://avatars.githubusercontent.com/u/20346805?v=4?s=100" width="100px;" alt="Anna Sackmann"/><br /><sub><b>Anna Sackmann</b></sub></a><br /><a href="#translation-sackmanna" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://sarahlrstevens.info"><img src="https://avatars.githubusercontent.com/u/5558419?v=4?s=100" width="100px;" alt="Sarah Stevens"/><br /><sub><b>Sarah Stevens</b></sub></a><br /><a href="#translation-sstevens2" title="Translation">🌍</a> <a href="#question-sstevens2" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://tgconsulting.ca"><img src="https://avatars.githubusercontent.com/u/7302575?v=4?s=100" width="100px;" alt="Thomas Guignard"/><br /><sub><b>Thomas Guignard</b></sub></a><br /><a href="#translation-timtomch" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://tbyhdgs.info"><img src="https://avatars.githubusercontent.com/u/9694524?v=4?s=100" width="100px;" alt="Toby Hodges"/><br /><sub><b>Toby Hodges</b></sub></a><br /><a href="#doc-tobyhodges" title="Documentation">📖</a> <a href="#question-tobyhodges" title="Answering Questions">💬</a> <a href="#translation-tobyhodges" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tyt3"><img src="https://avatars.githubusercontent.com/u/34420663?v=4?s=100" width="100px;" alt="Tyrica Terry Kapral"/><br /><sub><b>Tyrica Terry Kapral</b></sub></a><br /><a href="#translation-tyt3" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://abav.lugaralgum.com"><img src="https://avatars.githubusercontent.com/u/3694604?v=4?s=100" width="100px;" alt="Alexandre B A Villares"/><br /><sub><b>Alexandre B A Villares</b></sub></a><br /><a href="#translation-villares" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://zkamvar.netlify.app"><img src="https://avatars.githubusercontent.com/u/3639446?v=4?s=100" width="100px;" alt="Zhian N. Kamvar"/><br /><sub><b>Zhian N. Kamvar</b></sub></a><br /><a href="#doc-zkamvar" title="Documentation">📖</a> <a href="#review-zkamvar" title="Reviewed Pull Requests">👀</a> <a href="#question-zkamvar" title="Answering Questions">💬</a> <a href="#translation-zkamvar" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sfmig"><img src="https://avatars.githubusercontent.com/u/33267254?v=4?s=100" width="100px;" alt="sfmig"/><br /><sub><b>sfmig</b></sub></a><br /><a href="#translation-sfmig" title="Translation">🌍</a> <a href="#question-sfmig" title="Answering Questions">💬</a></td>
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
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/josenino95"><img src="https://avatars.githubusercontent.com/u/72319858?v=4?s=100" width="100px;" alt="Jose Niño"/><br /><sub><b>Jose Niño</b></sub></a><br /><a href="#translation-josenino95" title="Translation">🌍</a> <a href="#question-josenino95" title="Answering Questions">💬</a></td>
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
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/svenvanderburg"><img src="https://avatars.githubusercontent.com/u/9945255?v=4?s=100" width="100px;" alt="Sven van der Burg"/><br /><sub><b>Sven van der Burg</b></sub></a><br /><a href="#translation-svenvanderburg" title="Translation">🌍</a> <a href="#question-svenvanderburg" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://sites.google.com/view/abhishekchakraborty"><img src="https://avatars.githubusercontent.com/u/6579069?v=4?s=100" width="100px;" alt="Abhishek Chakraborty"/><br /><sub><b>Abhishek Chakraborty</b></sub></a><br /><a href="#translation-abhicc" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/katia-slc"><img src="https://avatars.githubusercontent.com/u/54743399?v=4?s=100" width="100px;" alt="Katia Slodkowski Clerici"/><br /><sub><b>Katia Slodkowski Clerici</b></sub></a><br /><a href="#translation-katia-slc" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jcostacurta11.github.io/"><img src="https://avatars.githubusercontent.com/u/13225001?v=4?s=100" width="100px;" alt="Julia Costacurta"/><br /><sub><b>Julia Costacurta</b></sub></a><br /><a href="#translation-jcostacurta11" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/likeajumprope"><img src="https://avatars.githubusercontent.com/u/23728822?v=4?s=100" width="100px;" alt="Johanna Bayer"/><br /><sub><b>Johanna Bayer</b></sub></a><br /><a href="#translation-likeajumprope" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MaggiK"><img src="https://avatars.githubusercontent.com/u/18407416?v=4?s=100" width="100px;" alt="Maggi Kraft"/><br /><sub><b>Maggi Kraft</b></sub></a><br /><a href="#translation-MaggiK" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dsmits"><img src="https://avatars.githubusercontent.com/u/131889?v=4?s=100" width="100px;" alt="Djura"/><br /><sub><b>Djura</b></sub></a><br /><a href="#translation-dsmits" title="Translation">🌍</a> <a href="#question-dsmits" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JMorado"><img src="https://avatars.githubusercontent.com/u/7460993?v=4?s=100" width="100px;" alt="João Morado"/><br /><sub><b>João Morado</b></sub></a><br /><a href="#translation-JMorado" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://epicworld.co.ke/"><img src="https://avatars.githubusercontent.com/u/14215807?v=4?s=100" width="100px;" alt="Ken Mbuki"/><br /><sub><b>Ken Mbuki</b></sub></a><br /><a href="#translation-kmbuki" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rosemm"><img src="https://avatars.githubusercontent.com/u/9002194?v=4?s=100" width="100px;" alt="Rose M. Hartman"/><br /><sub><b>Rose M. Hartman</b></sub></a><br /><a href="#translation-rosemm" title="Translation">🌍</a> <a href="#question-rosemm" title="Answering Questions">💬</a></td>
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
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dannda"><img src="https://avatars.githubusercontent.com/u/8517999?v=4?s=100" width="100px;" alt="dannda"/><br /><sub><b>dannda</b></sub></a><br /><a href="#translation-dannda" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/TueloNtlotlang"><img src="https://avatars.githubusercontent.com/u/72657722?v=4?s=100" width="100px;" alt="TueloNtlotlang"/><br /><sub><b>TueloNtlotlang</b></sub></a><br /><a href="#translation-TueloNtlotlang" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/gsavva"><img src="https://avatars.githubusercontent.com/u/41191161?v=4?s=100" width="100px;" alt="Giannis Savva"/><br /><sub><b>Giannis Savva</b></sub></a><br /><a href="#translation-gsavva" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/radersma"><img src="https://avatars.githubusercontent.com/u/28388211?v=4?s=100" width="100px;" alt="Reinder Radersma"/><br /><sub><b>Reinder Radersma</b></sub></a><br /><a href="#translation-radersma" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/donatella-cea"><img src="https://avatars.githubusercontent.com/u/104511563?v=4?s=100" width="100px;" alt="donatella-cea"/><br /><sub><b>donatella-cea</b></sub></a><br /><a href="#translation-donatella-cea" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/CunliangGeng"><img src="https://avatars.githubusercontent.com/u/9798985?v=4?s=100" width="100px;" alt="Cunliang Geng"/><br /><sub><b>Cunliang Geng</b></sub></a><br /><a href="#translation-CunliangGeng" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/domhnallc"><img src="https://avatars.githubusercontent.com/u/67946547?v=4?s=100" width="100px;" alt="domhnallc"/><br /><sub><b>domhnallc</b></sub></a><br /><a href="#translation-domhnallc" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ocesaulo.github.io/"><img src="https://avatars.githubusercontent.com/u/11863912?v=4?s=100" width="100px;" alt="Saulo Soares"/><br /><sub><b>Saulo Soares</b></sub></a><br /><a href="#translation-ocesaulo" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/souravsingh"><img src="https://avatars.githubusercontent.com/u/4314261?v=4?s=100" width="100px;" alt="Sourav Singh"/><br /><sub><b>Sourav Singh</b></sub></a><br /><a href="#translation-souravsingh" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://soyandrea.github.io/"><img src="https://avatars.githubusercontent.com/u/45582182?v=4?s=100" width="100px;" alt="Andrea Gomez Vargas"/><br /><sub><b>Andrea Gomez Vargas</b></sub></a><br /><a href="#translation-SoyAndrea" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://estacion-r.netlify.app/"><img src="https://avatars.githubusercontent.com/u/30708601?v=4?s=100" width="100px;" alt="Pablo Tiscornia"/><br /><sub><b>Pablo Tiscornia</b></sub></a><br /><a href="#translation-pablotis" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://sayalaruano.github.io/"><img src="https://avatars.githubusercontent.com/u/52267585?v=4?s=100" width="100px;" alt="Sebastián Ayala Ruano"/><br /><sub><b>Sebastián Ayala Ruano</b></sub></a><br /><a href="#translation-sayalaruano" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.sv.uio.no/tik/english/people/aca/fraukegr/index.html"><img src="https://avatars.githubusercontent.com/u/57175731?v=4?s=100" width="100px;" alt="fraukero"/><br /><sub><b>fraukero</b></sub></a><br /><a href="#translation-fraukero" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/IngaPa"><img src="https://avatars.githubusercontent.com/u/12497640?v=4?s=100" width="100px;" alt="IngaPa"/><br /><sub><b>IngaPa</b></sub></a><br /><a href="#translation-IngaPa" title="Translation">🌍</a> <a href="#question-IngaPa" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://sandragodinhosilva.netlify.app"><img src="https://avatars.githubusercontent.com/u/29963204?v=4?s=100" width="100px;" alt="Sandra Godinho Silva"/><br /><sub><b>Sandra Godinho Silva</b></sub></a><br /><a href="#translation-sandragodinhosilva" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://clemenslange.de"><img src="https://avatars.githubusercontent.com/u/5270053?v=4?s=100" width="100px;" alt="Clemens Lange"/><br /><sub><b>Clemens Lange</b></sub></a><br /><a href="#translation-clelange" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blacktack2"><img src="https://avatars.githubusercontent.com/u/43672375?v=4?s=100" width="100px;" alt="Alison Lewis"/><br /><sub><b>Alison Lewis</b></sub></a><br /><a href="#translation-blacktack2" title="Translation">🌍</a> <a href="#review-blacktack2" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kkauder"><img src="https://avatars.githubusercontent.com/u/5784983?v=4?s=100" width="100px;" alt="kkauder"/><br /><sub><b>kkauder</b></sub></a><br /><a href="#translation-kkauder" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ewinge"><img src="https://avatars.githubusercontent.com/u/864123?v=4?s=100" width="100px;" alt="ewinge"/><br /><sub><b>ewinge</b></sub></a><br /><a href="#translation-ewinge" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://jnywong.github.io"><img src="https://avatars.githubusercontent.com/u/45105935?v=4?s=100" width="100px;" alt="Jenny Wong"/><br /><sub><b>Jenny Wong</b></sub></a><br /><a href="#translation-jnywong" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ahcvlot"><img src="https://avatars.githubusercontent.com/u/53600984?v=4?s=100" width="100px;" alt="Anna Vlot"/><br /><sub><b>Anna Vlot</b></sub></a><br /><a href="#translation-ahcvlot" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/amisios"><img src="https://avatars.githubusercontent.com/u/8419934?v=4?s=100" width="100px;" alt="amisios"/><br /><sub><b>amisios</b></sub></a><br /><a href="#translation-amisios" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MilenaLa"><img src="https://avatars.githubusercontent.com/u/21173185?v=4?s=100" width="100px;" alt="MilenaLa"/><br /><sub><b>MilenaLa</b></sub></a><br /><a href="#translation-MilenaLa" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JorgeBornemann"><img src="https://avatars.githubusercontent.com/u/32248422?v=4?s=100" width="100px;" alt="JorgeBornemann"/><br /><sub><b>JorgeBornemann</b></sub></a><br /><a href="#translation-JorgeBornemann" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SamGuay"><img src="https://avatars.githubusercontent.com/u/30598330?v=4?s=100" width="100px;" alt="Samuel Guay"/><br /><sub><b>Samuel Guay</b></sub></a><br /><a href="#translation-SamGuay" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tanjagaustad"><img src="https://avatars.githubusercontent.com/u/95272341?v=4?s=100" width="100px;" alt="Tanja Gaustad"/><br /><sub><b>Tanja Gaustad</b></sub></a><br /><a href="#translation-tanjagaustad" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://benbrecht.tumblr.com/"><img src="https://avatars.githubusercontent.com/u/50832960?v=4?s=100" width="100px;" alt="Benito"/><br /><sub><b>Benito</b></sub></a><br /><a href="#translation-benbrecht" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://gerhard.pro"><img src="https://avatars.githubusercontent.com/u/20424252?v=4?s=100" width="100px;" alt="Gerhard van Huyssteen"/><br /><sub><b>Gerhard van Huyssteen</b></sub></a><br /><a href="#translation-gerhardvanh" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Sibeko-J"><img src="https://avatars.githubusercontent.com/u/75101826?v=4?s=100" width="100px;" alt="Dr Johannes Sibeko"/><br /><sub><b>Dr Johannes Sibeko</b></sub></a><br /><a href="#translation-Sibeko-J" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mvzaanen"><img src="https://avatars.githubusercontent.com/u/65609197?v=4?s=100" width="100px;" alt="Menno van Zaanen"/><br /><sub><b>Menno van Zaanen</b></sub></a><br /><a href="#translation-mvzaanen" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Harry-Dolan"><img src="https://avatars.githubusercontent.com/u/59711509?v=4?s=100" width="100px;" alt="Harry-Dolan"/><br /><sub><b>Harry-Dolan</b></sub></a><br /><a href="#translation-Harry-Dolan" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.aranthropos.com"><img src="https://avatars.githubusercontent.com/u/74216214?v=4?s=100" width="100px;" alt="Mabrouk"/><br /><sub><b>Mabrouk</b></sub></a><br /><a href="#translation-Mabrouk12300" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lmdabigail"><img src="https://avatars.githubusercontent.com/u/47910378?v=4?s=100" width="100px;" alt="Lydia D"/><br /><sub><b>Lydia D</b></sub></a><br /><a href="#translation-lmdabigail" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/criselsuarez"><img src="https://avatars.githubusercontent.com/u/20343857?v=4?s=100" width="100px;" alt="criselsuarez"/><br /><sub><b>criselsuarez</b></sub></a><br /><a href="#translation-criselsuarez" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/margaridamadeira"><img src="https://avatars.githubusercontent.com/u/9846293?v=4?s=100" width="100px;" alt="Margarida Madeira e Moura"/><br /><sub><b>Margarida Madeira e Moura</b></sub></a><br /><a href="#translation-margaridamadeira" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jesCodingHere"><img src="https://avatars.githubusercontent.com/u/17342514?v=4?s=100" width="100px;" alt="jesCodingHere"/><br /><sub><b>jesCodingHere</b></sub></a><br /><a href="#translation-jesCodingHere" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Agrippina254"><img src="https://avatars.githubusercontent.com/u/56484576?v=4?s=100" width="100px;" alt="Agrippina254"/><br /><sub><b>Agrippina254</b></sub></a><br /><a href="#translation-Agrippina254" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/wanjauk"><img src="https://avatars.githubusercontent.com/u/42046925?v=4?s=100" width="100px;" alt="Kennedy Mwangi"/><br /><sub><b>Kennedy Mwangi</b></sub></a><br /><a href="#translation-wanjauk" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/karegapauline"><img src="https://avatars.githubusercontent.com/u/27417671?v=4?s=100" width="100px;" alt="Pauline Karega"/><br /><sub><b>Pauline Karega</b></sub></a><br /><a href="#translation-karegapauline" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mubangansofu"><img src="https://avatars.githubusercontent.com/u/60039069?v=4?s=100" width="100px;" alt="Mubanga Nsofu"/><br /><sub><b>Mubanga Nsofu</b></sub></a><br /><a href="#translation-mubangansofu" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.lse.de/"><img src="https://avatars.githubusercontent.com/u/18212549?v=4?s=100" width="100px;" alt="Lars Schöbitz"/><br /><sub><b>Lars Schöbitz</b></sub></a><br /><a href="#translation-larnsce" title="Translation">🌍</a> <a href="#question-larnsce" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/evanmarzahn"><img src="https://avatars.githubusercontent.com/u/13949944?v=4?s=100" width="100px;" alt="evanmarzahn"/><br /><sub><b>evanmarzahn</b></sub></a><br /><a href="#translation-evanmarzahn" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MRudey"><img src="https://avatars.githubusercontent.com/u/11921755?v=4?s=100" width="100px;" alt="Michael Rudolf"/><br /><sub><b>Michael Rudolf</b></sub></a><br /><a href="#translation-MRudey" title="Translation">🌍</a> <a href="#question-MRudey" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ageorgou"><img src="https://avatars.githubusercontent.com/u/1186102?v=4?s=100" width="100px;" alt="ageorgou"/><br /><sub><b>ageorgou</b></sub></a><br /><a href="#translation-ageorgou" title="Translation">🌍</a> <a href="#question-ageorgou" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://b1nslashsh.tech"><img src="https://avatars.githubusercontent.com/u/36979660?v=4?s=100" width="100px;" alt="Abdul muhaimin"/><br /><sub><b>Abdul muhaimin</b></sub></a><br /><a href="#translation-b1nslashsh" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/d0rg0ld"><img src="https://avatars.githubusercontent.com/u/2720790?v=4?s=100" width="100px;" alt="Doron Goldfarb"/><br /><sub><b>Doron Goldfarb</b></sub></a><br /><a href="#translation-d0rg0ld" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://danielskatz.org"><img src="https://avatars.githubusercontent.com/u/2913845?v=4?s=100" width="100px;" alt="Daniel S. Katz"/><br /><sub><b>Daniel S. Katz</b></sub></a><br /><a href="#translation-danielskatz" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://farzanazali.com"><img src="https://avatars.githubusercontent.com/u/7939582?v=4?s=100" width="100px;" alt="Farzana Z Ali"/><br /><sub><b>Farzana Z Ali</b></sub></a><br /><a href="#translation-FarzanaZAli" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://fluid.quest"><img src="https://avatars.githubusercontent.com/u/9155111?v=4?s=100" width="100px;" alt="Ashwin V. Mohanan"/><br /><sub><b>Ashwin V. Mohanan</b></sub></a><br /><a href="#translation-ashwinvis" title="Translation">🌍</a> <a href="#question-ashwinvis" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/johnbradley"><img src="https://avatars.githubusercontent.com/u/1024463?v=4?s=100" width="100px;" alt="John Bradley"/><br /><sub><b>John Bradley</b></sub></a><br /><a href="#translation-johnbradley" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cosmofelix"><img src="https://avatars.githubusercontent.com/u/41323997?v=4?s=100" width="100px;" alt="cosmofelix"/><br /><sub><b>cosmofelix</b></sub></a><br /><a href="#translation-cosmofelix" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kozo2"><img src="https://avatars.githubusercontent.com/u/12192?v=4?s=100" width="100px;" alt="Kozo Nishida"/><br /><sub><b>Kozo Nishida</b></sub></a><br /><a href="#translation-kozo2" title="Translation">🌍</a> <a href="#question-kozo2" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ameynert"><img src="https://avatars.githubusercontent.com/u/6746627?v=4?s=100" width="100px;" alt="Alison Meynert"/><br /><sub><b>Alison Meynert</b></sub></a><br /><a href="#translation-ameynert" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lphegley"><img src="https://avatars.githubusercontent.com/u/74062590?v=4?s=100" width="100px;" alt="Lauren Phegley"/><br /><sub><b>Lauren Phegley</b></sub></a><br /><a href="#translation-lphegley" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/diegoonna"><img src="https://avatars.githubusercontent.com/u/46107855?v=4?s=100" width="100px;" alt="Diego Onna"/><br /><sub><b>Diego Onna</b></sub></a><br /><a href="#translation-diegoonna" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://uvri.go.ug/"><img src="https://avatars.githubusercontent.com/u/44267477?v=4?s=100" width="100px;" alt="eddUG"/><br /><sub><b>eddUG</b></sub></a><br /><a href="#translation-eddUG" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/agully1"><img src="https://avatars.githubusercontent.com/u/89023825?v=4?s=100" width="100px;" alt="agully1"/><br /><sub><b>agully1</b></sub></a><br /><a href="#translation-agully1" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cmeessen"><img src="https://avatars.githubusercontent.com/u/14222414?v=4?s=100" width="100px;" alt="Christian Meeßen"/><br /><sub><b>Christian Meeßen</b></sub></a><br /><a href="#translation-cmeessen" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://systemsmedicine.pulmonary.medicine.ufl.edu/profile/brunson-jason/"><img src="https://avatars.githubusercontent.com/u/7768027?v=4?s=100" width="100px;" alt="Cory Brunson"/><br /><sub><b>Cory Brunson</b></sub></a><br /><a href="#translation-corybrunson" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.kariljordan.com"><img src="https://avatars.githubusercontent.com/u/21027863?v=4?s=100" width="100px;" alt="Kari L. Jordan, PhD"/><br /><sub><b>Kari L. Jordan, PhD</b></sub></a><br /><a href="#doc-kariljordan" title="Documentation">📖</a> <a href="#question-kariljordan" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bonnyad"><img src="https://avatars.githubusercontent.com/u/32709824?v=4?s=100" width="100px;" alt="BONNY ADANE"/><br /><sub><b>BONNY ADANE</b></sub></a><br /><a href="#review-bonnyad" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jduck.net"><img src="https://avatars.githubusercontent.com/u/119403?v=4?s=100" width="100px;" alt="Jonah Duckles"/><br /><sub><b>Jonah Duckles</b></sub></a><br /><a href="#question-jduckles" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.facebook.com/NuoroForestrySchoolUniSS/"><img src="https://avatars.githubusercontent.com/u/16821135?v=4?s=100" width="100px;" alt="Roberto Scotti"/><br /><sub><b>Roberto Scotti</b></sub></a><br /><a href="#question-r-scotti" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://about.cubictype.com/"><img src="https://avatars.githubusercontent.com/u/1215412?v=4?s=100" width="100px;" alt="David Jones"/><br /><sub><b>David Jones</b></sub></a><br /><a href="#question-drj11" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Talishask"><img src="https://avatars.githubusercontent.com/u/45104071?v=4?s=100" width="100px;" alt="Talisha Sutton-Kennedy"/><br /><sub><b>Talisha Sutton-Kennedy</b></sub></a><br /><a href="#question-Talishask" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/maneesha"><img src="https://avatars.githubusercontent.com/u/829690?v=4?s=100" width="100px;" alt="maneesha"/><br /><sub><b>maneesha</b></sub></a><br /><a href="#question-maneesha" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kathryn-garside"><img src="https://avatars.githubusercontent.com/u/23357901?v=4?s=100" width="100px;" alt="kathryn-garside"/><br /><sub><b>kathryn-garside</b></sub></a><br /><a href="#question-kathryn-garside" title="Answering Questions">💬</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vdike"><img src="https://avatars.githubusercontent.com/u/38359857?v=4?s=100" width="100px;" alt="Veronica Dike"/><br /><sub><b>Veronica Dike</b></sub></a><br /><a href="#question-vdike" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/karenword"><img src="https://avatars.githubusercontent.com/u/22605448?v=4?s=100" width="100px;" alt="Karen Word"/><br /><sub><b>Karen Word</b></sub></a><br /><a href="#question-karenword" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/zdshaoteach"><img src="https://avatars.githubusercontent.com/u/102433092?v=4?s=100" width="100px;" alt="zdshaoteach"/><br /><sub><b>zdshaoteach</b></sub></a><br /><a href="#question-zdshaoteach" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lingmeng634"><img src="https://avatars.githubusercontent.com/u/4487000?v=4?s=100" width="100px;" alt="Ling"/><br /><sub><b>Ling</b></sub></a><br /><a href="#question-lingmeng634" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://heidiseibold.com/"><img src="https://avatars.githubusercontent.com/u/14146757?v=4?s=100" width="100px;" alt="Heidi Seibold"/><br /><sub><b>Heidi Seibold</b></sub></a><br /><a href="#question-HeidiSeibold" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Lidetewold"><img src="https://avatars.githubusercontent.com/u/167426488?v=4?s=100" width="100px;" alt="Lidetewold"/><br /><sub><b>Lidetewold</b></sub></a><br /><a href="#translation-Lidetewold" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vvkharchenko"><img src="https://avatars.githubusercontent.com/u/146713095?v=4?s=100" width="100px;" alt="Volodymyr Kharchenko"/><br /><sub><b>Volodymyr Kharchenko</b></sub></a><br /><a href="#translation-vvkharchenko" title="Translation">🌍</a> <a href="#review-vvkharchenko" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ChubOlya"><img src="https://avatars.githubusercontent.com/u/66166517?v=4?s=100" width="100px;" alt="Chub Olga"/><br /><sub><b>Chub Olga</b></sub></a><br /><a href="#review-ChubOlya" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ViktoriiaGrivina"><img src="https://avatars.githubusercontent.com/u/171017648?v=4?s=100" width="100px;" alt="ViktoriiaGrivina"/><br /><sub><b>ViktoriiaGrivina</b></sub></a><br /><a href="#review-ViktoriiaGrivina" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Avhustyn-t"><img src="https://avatars.githubusercontent.com/u/188987538?v=4?s=100" width="100px;" alt="Avhustyn-t"/><br /><sub><b>Avhustyn-t</b></sub></a><br /><a href="#translation-Avhustyn-t" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://lauramugeha.bio"><img src="https://avatars.githubusercontent.com/u/47306402?v=4?s=100" width="100px;" alt="Laura Mugeha"/><br /><sub><b>Laura Mugeha</b></sub></a><br /><a href="#review-mugeha-laura" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Mpilo-K"><img src="https://avatars.githubusercontent.com/u/54138769?v=4?s=100" width="100px;" alt="Mpilo Khumalo"/><br /><sub><b>Mpilo Khumalo</b></sub></a><br /><a href="#translation-Mpilo-K" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/TinoCoda"><img src="https://avatars.githubusercontent.com/u/111807873?v=4?s=100" width="100px;" alt="DBM"/><br /><sub><b>DBM</b></sub></a><br /><a href="#translation-TinoCoda" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://federicagazzelloni.com/"><img src="https://avatars.githubusercontent.com/u/61802414?v=4?s=100" width="100px;" alt="Federica Gazzelloni (she/her)"/><br /><sub><b>Federica Gazzelloni (she/her)</b></sub></a><br /><a href="#translation-fgazzelloni" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ahmedunshur"><img src="https://avatars.githubusercontent.com/u/6027258?v=4?s=100" width="100px;" alt="Ahmed Unshur"/><br /><sub><b>Ahmed Unshur</b></sub></a><br /><a href="#translation-ahmedunshur" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/eor"><img src="https://avatars.githubusercontent.com/u/6682226?v=4?s=100" width="100px;" alt="Fabian"/><br /><sub><b>Fabian</b></sub></a><br /><a href="#translation-eor" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yexpp"><img src="https://avatars.githubusercontent.com/u/201125696?v=4?s=100" width="100px;" alt="yexpp"/><br /><sub><b>yexpp</b></sub></a><br /><a href="#review-yexpp" title="Reviewed Pull Requests">👀</a> <a href="#question-yexpp" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://za.github.io"><img src="https://avatars.githubusercontent.com/u/409455?v=4?s=100" width="100px;" alt="za"/><br /><sub><b>za</b></sub></a><br /><a href="#translation-za" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://adryan.de"><img src="https://avatars.githubusercontent.com/u/6317446?v=4?s=100" width="100px;" alt="Boris Adryan"/><br /><sub><b>Boris Adryan</b></sub></a><br /><a href="#translation-badryan" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/VScharf7"><img src="https://avatars.githubusercontent.com/u/73226085?v=4?s=100" width="100px;" alt="vanessa.scharf"/><br /><sub><b>vanessa.scharf</b></sub></a><br /><a href="#review-VScharf7" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/0000-0002-5589-7754"><img src="https://avatars.githubusercontent.com/u/1872302?v=4?s=100" width="100px;" alt="Robert Davey"/><br /><sub><b>Robert Davey</b></sub></a><br /><a href="#doc-froggleston" title="Documentation">📖</a> <a href="#review-froggleston" title="Reviewed Pull Requests">👀</a> <a href="#question-froggleston" title="Answering Questions">💬</a> <a href="#translation-froggleston" title="Translation">🌍</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/AngeliqueV"><img src="https://avatars.githubusercontent.com/u/69516258?v=4?s=100" width="100px;" alt="AngeliqueV"/><br /><sub><b>AngeliqueV</b></sub></a><br /><a href="#translation-AngeliqueV" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ajneil-gh"><img src="https://avatars.githubusercontent.com/u/75391698?v=4?s=100" width="100px;" alt="ajneil-gh"/><br /><sub><b>ajneil-gh</b></sub></a><br /><a href="#translation-ajneil-gh" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/erindfoster/"><img src="https://avatars.githubusercontent.com/u/14339093?v=4?s=100" width="100px;" alt="Erin Foster"/><br /><sub><b>Erin Foster</b></sub></a><br /><a href="#translation-edfoster10" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://carschno.github.io/"><img src="https://avatars.githubusercontent.com/u/4696228?v=4?s=100" width="100px;" alt="Carsten Schnober"/><br /><sub><b>Carsten Schnober</b></sub></a><br /><a href="#translation-carschno" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://sarahmbrown.org"><img src="https://avatars.githubusercontent.com/u/10656079?v=4?s=100" width="100px;" alt="Sarah Brown"/><br /><sub><b>Sarah Brown</b></sub></a><br /><a href="#doc-brownsarahm" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
