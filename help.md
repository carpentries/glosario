---
permalink: /help/
layout: page
direction: ltr
---


#### What is Glosario?
**Glosario** is an open-source, multilingual glossary of data science terms. Lesson authors can use glossary keys in lesson metadata to clarify what is taught, what learners need to know, and where that knowledge can be found. The libraries also enable the insertion of consistent hyperlinks to term definitions across multiple human languages.

---

#### Why not just link to Wikipedia?
While Wikipedia provides **explanations**, Glosario provides **concise definitions**. We aim to support clarity and consistency across lessons, rather than replacing encyclopedic references.

---

#### What formats are used to build Glosario?
The master glossary is maintained in a `glossary.yml` file. While YAML can be challenging to edit, it's preferred because it better supports complex relationships than other formats, such as JSON or CSV.

---

#### How can I view or use Glosario online?
Glosario is deployed as a **GitHub Pages** site using **Jekyll**—the default site generator for GitHub Pages. The glossary is also available as installable packages for **R** and **Python**.

---

#### What does a glossary entry look like?

```yaml
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

Each entry includes:

- A unique slug
- Optional related term references
- Definitions in one or more ISO 639 languages (e.g., en, es, fr)
- An optional acronym
- Definitions may include links to other glossary terms or external sources

---

### Where do I start?

We accept either:
- new terms and definitions in English and one or more other languages
- translations of existing English terms and definitions into one or more other languages

There are three routes available to you to make your contribution (see the section below):
- via our Google Form (recommended)
- via a GitHub issue
- via a direct change in the Glosario glossary.yml file and a pull request raise in GitHub (advanced)

To make contributions via GitHub, you will need a valid GitHub login.

---

#### How do I submit a translation?

##### Via Google Form

Go to the language page that you want to translate a term for, and click the accordion dropdown "Show Terms That Need Translation". Find the term in the list that you wish to translate, and click the Google icon to the right. The form will open in a new tab, and the English term and language will be prefilled for you. Please add your GitHub username, the translated term, and the translated definition. Click Submit. You are done!

##### Via GitHub Issue

Go to the language page that you want to translate a term for, and click the accordion dropdown "Show Terms That Need Translation". Find the term in the list that you wish to translate, and click the GitHub icon to the right. The GitHub new issue form will open in a new tab, and the English term title and language label will be prefilled for you. Please add the translated term and the translated definition in the main issue text box. Click Create. You are done!

#### Via GitHub Pull Request

See our [contribution guide](https://docs.google.com/document/d/18oxYd6D9heESqw2gw9cbtxiCfkb4wlxazERFBIDCoeM/edit?tab=t.0#heading=h.wsi1psxc3n64) for full instructions.

Also, check out our short YouTube tutorials:

- [Recording in English](https://www.youtube.com/watch?v=ew1eb1ug-Q8)
- [Recording in Español](https://www.youtube.com/watch?v=f9K5wYq0dQM&t=23s)  
(Use YouTube’s auto-translate feature for other languages)

---

#### Can I contribute in any language?

Yes! Contributions are welcome in **all languages**, even those not currently represented in the glossary.

---

#### How do I submit a new term?

##### Via GitHub Issue

Go to the [English language page](en.md) and click the "+ Add new term" GitHub link in the top right. The GitHub new issue form will open in a new tab, and the English term title and language label will be prefilled for you. Please add the new term you wish to add to the English glossary and the definition in the main issue text box. Click Create. You are done!


##### Via GitHub Pull Request

See our [contribution guide](https://docs.google.com/document/d/18oxYd6D9heESqw2gw9cbtxiCfkb4wlxazERFBIDCoeM/edit?tab=t.0#heading=h.wsi1psxc3n64) for full instructions

---

#### Where can I get help or ask questions?

- Join the `#glosario` channel in **The Carpentries Slack**
- Email us at [community@carpentries.org](mailto:community@carpentries.org)
- Need Slack access? [Request it here](https://carpentries.org/slack/)

---

#### What is the structure behind Glosario?

- The core glossary is stored in `glossary.yml`
- Built into a **GitHub Pages** site using **Jekyll**

---

#### What does the icons → and ⊗ mean?

The → icon indicates associated terms. For example, mean, mode, and median are related and will be linked using →.
The ⊗ icon shows translations of a term in other languages.

---

#### Who funds and collaborates on Glosario?

- **SADiLaR** supports expansion into African languages.
- The **Andrew W. Mellon Foundation** has provided funding from **November 2023 to December 2025** for upgrades and ongoing development.

---

#### Who gets credit for contributing?

At The Carpentries, every contribution matters. See [All Contributors](https://github.com/carpentries/glosario/graphs/contributors) for a list of contributions. 
