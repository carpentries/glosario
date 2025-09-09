#!/usr/bin/env python3

import pprint
import yaml

from collections import OrderedDict
from pathlib import Path

import icu

# set up supported languages
LANGUAGES = [
    ('aa', 'Afar'),
    ('ab', 'Abkhazian'),
    ('af', 'Afrikaans'),
    ('ak', 'Akan'),
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('an', 'Aragonese'),
    ('hy', 'Armenian'),
    ('as', 'Assamese'),
    ('av', 'Avaric'),
    ('ae', 'Avestan'),
    ('ay', 'Aymara'),
    ('az', 'Azerbaijani'),
    ('ba', 'Bashkir'),
    ('bm', 'Bambara'),
    ('eu', 'Basque'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('bh', 'Bihari languages'),
    ('bi', 'Bislama'),
    ('bo', 'Tibetan'),
    ('bs', 'Bosnian'),
    ('br', 'Breton'),
    ('bg', 'Bulgarian'),
    ('my', 'Burmese'),
    ('ca', 'Catalan; Valencian'),
    ('ch', 'Chamorro'),
    ('ce', 'Chechen'),
    ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
    ('cv', 'Chuvash'),
    ('kw', 'Cornish'),
    ('co', 'Corsican'),
    ('cr', 'Cree'),
    ('cy', 'Welsh'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('dv', 'Divehi; Dhivehi; Maldivian'),
    ('dz', 'Dzongkha'),
    ('el', 'Greek, Modern (1453-)'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('ee', 'Ewe'),
    ('fo', 'Faroese'),
    ('fa', 'Persian'),
    ('fj', 'Fijian'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('fy', 'Western Frisian'),
    ('ff', 'Fulah'),
    ('Ga', 'Georgian'),
    ('gd', 'Gaelic; Scottish Gaelic'),
    ('ga', 'Irish'),
    ('gl', 'Galician'),
    ('gv', 'Manx'),
    ('gn', 'Guarani'),
    ('gu', 'Gujarati'),
    ('ht', 'Haitian; Haitian Creole'),
    ('ha', 'Hausa'),
    ('he', 'Hebrew'),
    ('hz', 'Herero'),
    ('hi', 'Hindi'),
    ('ho', 'Hiri Motu'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('ig', 'Igbo'),
    ('io', 'Ido'),
    ('ii', 'Sichuan Yi; Nuosu'),
    ('iu', 'Inuktitut'),
    ('ie', 'Interlingue; Occidental'),
    ('ia', 'Interlingua (International Auxiliary Language Association)'),
    ('id', 'Indonesian'),
    ('ik', 'Inupiaq'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('jv', 'Javanese'),
    ('ja', 'Japanese'),
    ('kl', 'Kalaallisut; Greenlandic'),
    ('kn', 'Kannada'),
    ('ks', 'Kashmiri'),
    ('ka', 'Georgian'),
    ('kr', 'Kanuri'),
    ('kk', 'Kazakh'),
    ('km', 'Central Khmer'),
    ('ki', 'Kikuyu; Gikuyu'),
    ('rw', 'Kinyarwanda'),
    ('ky', 'Kirghiz; Kyrgyz'),
    ('kv', 'Komi'),
    ('kg', 'Kongo'),
    ('ko', 'Korean'),
    ('kj', 'Kuanyama; Kwanyama'),
    ('ku', 'Kurdish'),
    ('lo', 'Lao'),
    ('la', 'Latin'),
    ('lv', 'Latvian'),
    ('li', 'Limburgan; Limburger; Limburgish'),
    ('ln', 'Lingala'),
    ('lt', 'Lithuanian'),
    ('lb', 'Luxembourgish; Letzeburgesch'),
    ('lu', 'Luba-Katanga'),
    ('lg', 'Ganda'),
    ('mk', 'Macedonian'),
    ('mh', 'Marshallese'),
    ('ml', 'Malayalam'),
    ('mi', 'Maori'),
    ('mr', 'Marathi'),
    ('ms', 'Malay'),
    ('Mi', 'Micmac'),
    ('mg', 'Malagasy'),
    ('mt', 'Maltese'),
    ('mn', 'Mongolian'),
    ('na', 'Nauru'),
    ('nv', 'Navajo; Navaho'),
    ('nr', 'Ndebele, South; South Ndebele'),
    ('nd', 'Ndebele, North; North Ndebele'),
    ('ng', 'Ndonga'),
    ('ne', 'Nepali'),
    ('nl', 'Dutch; Flemish'),
    ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
    ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
    ('no', 'Norwegian'),
    ('oc', 'Occitan (post 1500)'),
    ('oj', 'Ojibwa'),
    ('or', 'Oriya'),
    ('om', 'Oromo'),
    ('os', 'Ossetian; Ossetic'),
    ('pa', 'Panjabi; Punjabi'),
    ('pi', 'Pali'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ps', 'Pushto; Pashto'),
    ('qu', 'Quechua'),
    ('rm', 'Romansh'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('rn', 'Rundi'),
    ('ru', 'Russian'),
    ('sg', 'Sango'),
    ('sa', 'Sanskrit'),
    ('si', 'Sinhala; Sinhalese'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('se', 'Northern Sami'),
    ('sm', 'Samoan'),
    ('sn', 'Shona'),
    ('sd', 'Sindhi'),
    ('so', 'Somali'),
    ('st', 'Sotho, Southern'),
    ('es', 'Spanish; Castilian'),
    ('sc', 'Sardinian'),
    ('sr', 'Serbian'),
    ('ss', 'Swati'),
    ('su', 'Sundanese'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('ty', 'Tahitian'),
    ('ta', 'Tamil'),
    ('tt', 'Tatar'),
    ('te', 'Telugu'),
    ('tg', 'Tajik'),
    ('tl', 'Tagalog'),
    ('th', 'Thai'),
    ('ti', 'Tigrinya'),
    ('to', 'Tonga (Tonga Islands)'),
    ('tn', 'Tswana'),
    ('ts', 'Tsonga'),
    ('tk', 'Turkmen'),
    ('tr', 'Turkish'),
    ('tw', 'Twi'),
    ('ug', 'Uighur; Uyghur'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('ve', 'Venda'),
    ('vi', 'Vietnamese'),
    ('vo', 'Volapük'),
    ('wa', 'Walloon'),
    ('wo', 'Wolof'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('yo', 'Yoruba'),
    ('za', 'Zhuang; Chuang'),
    ('zh', 'Chinese'),
    ('zu', 'Zulu')
]

def _generate_untranslated_terms(sorted_glossary_by_lang):
    # generate a dict of untranslated terms keyed by term
    untranslated_terms_by_lang = {}

    # if a term is in the english glossary but in no others, then add it to the untranslated dict
    for lang in sorted_glossary_by_lang.keys():
        if lang != "en":
            # get a list of current slugs in the current language glossary
            lang_slugs = [term["slug"] for term in sorted_glossary_by_lang[lang]]

            # if a term is in the english glossary but not in the current language glossary, add it to the untranslated dict
            for term in sorted_glossary_by_lang["en"]:
                # check if the term is in the current language glossary
                if term["slug"] not in lang_slugs:
                    if lang not in untranslated_terms_by_lang:
                        untranslated_terms_by_lang[lang] = []

                    # add the term to the untranslated dict
                    od = OrderedDict({
                        "slug": term["slug"],
                        lang: {
                            "term": term["en"]["term"],
                            "def": term["en"]["def"]
                        }
                    })
                    untranslated_terms_by_lang[lang].append(od)

    return untranslated_terms_by_lang

def _sort_terms(count_dict, data_path):
    # sort and reassign terms
    for lang in count_dict:
        # check 2-letter language codes vs 3-letter language codes
        # std_lang = standardize_tag(lang)
        # print(f"{lang} -> {std_lang} -> {Language.get(std_lang).to_alpha3()}")

        # create a locale from the language code and a collator to perform sorting
        icu_locale = icu.Locale(lang)
        collator = icu.Collator.createInstance(icu_locale)

        # only create directories for languages with terms
        if count_dict[lang]["count"] > 0:
            lang_path = data_path.joinpath(lang)
            lang_path.mkdir(parents=True, exist_ok=True)

            # sort and store sorted terms separate from the original list
            sorted_terms = sorted(count_dict[lang]["terms"], key=collator.getSortKey)
            count_dict[lang]["sorted_terms"] = sorted_terms
    return count_dict


def _setup_dict(glossary, data_path):
    # data structure to hold counts and terms
    count_dict = {}

    lang_codes = []
    for cc in LANGUAGES:
        count_dict[cc[0]] = {}
        count_dict[cc[0]]["count"] = 0
        count_dict[cc[0]]["name"] = cc[1]
        count_dict[cc[0]]["terms"] = []
        count_dict[cc[0]]["sorted_terms"] = []
        count_dict[cc[0]]["term_entry_map"] = {}
        lang_codes.append(cc[0])

    # total number of glossary terms
    # print(len(glos))

    # count terms and store them in the data structure
    for slug in glossary:
        for lang in slug.keys():
            if lang in lang_codes:
                count_dict[lang]["count"] += 1
                count_dict[lang]["terms"].append(slug[lang]["term"])
                count_dict[lang]["term_entry_map"][slug[lang]["term"]] = dict(
                    {
                        "slug": slug["slug"],
                        "def": slug[lang]["def"]
                    }
                )

                if "ref" in slug:
                    count_dict[lang]["term_entry_map"][slug[lang]["term"]]["ref"] = slug["ref"]

    # return the data structure including sorted terms
    return _sort_terms(count_dict, data_path)


def _build_lang_glossary(count_dict):
    glossary_by_lang = {}
    for lang in count_dict:
        sorted_glossary = []

        # process the data structure to create a new sorted glossary per language
        for sorted_term in count_dict[lang]["sorted_terms"]:
            if sorted_term in count_dict[lang]["term_entry_map"]:
                term_map = count_dict[lang]["term_entry_map"][sorted_term]
                slug = term_map["slug"]
                _def = term_map["def"]

                od = OrderedDict({
                    "slug": slug,
                    lang: {
                        "term": sorted_term,
                        "def": _def
                    }
                })

                if "ref" in term_map:
                    _ref = term_map["ref"]
                    od["ref"] = _ref

                # use an OrderedDict to retain insertion order
                sorted_glossary.append(od)

        # only include languages with terms
        if sorted_glossary:
            glossary_by_lang[lang] = sorted_glossary
    return glossary_by_lang


def setup_yaml():
    """ https://stackoverflow.com/a/8661021 """
    def represent_dict_order(self, data):
        return self.represent_mapping('tag:yaml.org,2002:map', data.items())
    yaml.add_representer(OrderedDict, represent_dict_order)


def main():
    try:
        # get path
        current_path = Path(__file__).resolve()

        # load main glossary file
        data_path = current_path.parent.parent.joinpath("_data/")
        glossary_path = data_path.joinpath("glossary.yml")
        glos = yaml.safe_load(glossary_path.read_text())

        # sort terms
        sort_dict = _setup_dict(glos, data_path)

        # rebuild glossary per language
        sorted_glossary_by_lang = _build_lang_glossary(sort_dict)

        # generate untranslated terms
        untranslated_terms = _generate_untranslated_terms(sorted_glossary_by_lang)

        # setup yaml for outputting
        setup_yaml()
        for lang in sorted_glossary_by_lang:
            yaml.dump(sorted_glossary_by_lang[lang], Path(f'_data/{lang}/glossary.yml').open('w'))
            if lang != "en":
                yaml.dump(untranslated_terms[lang], Path(f'_data/{lang}/untranslated_terms.yml').open('w'))

        # print untranslated terms
        # pprint.pprint(untranslated_terms)

        # for lang in untranslated_terms:
        #     print(f"Untranslated terms for {lang}: {len(untranslated_terms[lang])}/{len(sorted_glossary_by_lang['en'])}")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
