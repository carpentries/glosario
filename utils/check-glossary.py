#!/usr/bin/env python

'''
Check glossary YAML file.

Usage: check-glossary.py [-A] [-c LL] yaml-config-file glossary-file

Flags:
-   `-A`: report all missing definitions for all languages.
-   `-c LL`: report missing definitions for language with code `LL` (e.g., 'fr').

Checks always performed:
-   Only languages listed in `_config.yml` appear in glossary.
-   Entries have all required keys (`ENTRY_REQUIRED_KEYS`).
-   Only known keys are present at the top level of each entry (`ENTRY_KEYS`).
-   Entries are ordered by unique slugs.
-   Every definition has the required keys (`DEFINITION_REQUIRED_KEYS`).
-   Definitions only have allowed keys (`DEFINITION_KEYS`).
-   No duplicate definitions.

Checks performed 
'''

import sys
import getopt
import re
import yaml
from collections import Counter

# Keys for entries and definitions.
ENTRY_REQUIRED_KEYS = {'slug'}
ENTRY_OPTIONAL_KEYS = {'ref'}
ENTRY_LANGUAGE_KEYS = {'af', 'en', 'es', 'fr', 'pt', 'zu'}
ENTRY_KEYS = ENTRY_REQUIRED_KEYS | \
             ENTRY_OPTIONAL_KEYS | \
             ENTRY_LANGUAGE_KEYS
DEFINITION_REQUIRED_KEYS = {'term', 'def'}
DEFINITION_OPTIONAL_KEYS = {'acronym'}
DEFINITION_KEYS = DEFINITION_REQUIRED_KEYS | \
                  DEFINITION_OPTIONAL_KEYS

# Match internal Markdown links.
LINK_PAT = re.compile(r'\[.+?\]\(#(.+?)\)')


def main():
    '''Main driver.'''
    checkLang, configFile, glossaryFile = parseArgs()
    with open(configFile, 'r') as reader:
        config = yaml.load(reader, Loader=yaml.FullLoader)
    with open(glossaryFile, 'r') as reader:
        gloss = yaml.load(reader, Loader=yaml.FullLoader)

    checkLanguages(config)
    for entry in gloss:
        checkEntry(entry)
    checkSlugs(gloss)
    checkDuplicates(gloss)
    checkCrossRef(gloss)

    if checkLang == 'ALL':
        for lang in sorted(ENTRY_LANGUAGE_KEYS):
            checkMissingDefs(lang, gloss)
    elif checkLang:
        checkMissingDefs(checkLang, gloss)

    forward = buildForward(gloss)
    backward = buildBackward(forward)


def parseArgs():
    '''
    Parse command-line arguments, returning language to check,
    configuration file path, and glossary file path.  The language
    to check may be 'ALL' (to check all), None (to check none), or
    a known 2-letter language code.
    '''
    options, filenames = getopt.getopt(sys.argv[1:], 'Ac:')
    if (len(filenames) != 2):
        print(f'Usage: check [-A] [-c LL] configFile glossFile')
        sys.exit(1)
    configFile, glossFile = filenames

    checkLang = None
    for (opt, args) in options:
        if opt == '-A':
            checkLang = 'ALL'
        elif opt == '-c':
            checkLang = arg
            if checkLang not in ENTRY_LANGUAGE_KEYS:
                print(f'Unknown language {checkLang}', file=sys.stderr)
                sys.exit(1)
        else:
            print(f'Unknown flag {opt}', file=sys.stderr)
            sys.exit(1)

    return checkLang, configFile, glossFile


def checkLanguages(config):
    '''Compare configuration with this script's settings.'''
    actual = set([c['key'] for c in config['languages']])
    if actual - ENTRY_LANGUAGE_KEYS:
        print(f'unexpected languages in configuration: {actual - ENTRY_LANGUAGE_KEYS}')
    if ENTRY_LANGUAGE_KEYS - actual:
        print(f'missing languages in configuration: {ENTRY_LANGUAGE_KEYS - actual}')


def checkEntry(entry):
    '''
    Check structure of individual entries, returning a language-to-set
    dictionary of terms references in the body.
    '''
    keys = set(entry.keys())
    missing = [k for k in ENTRY_REQUIRED_KEYS if k not in keys]
    if missing:
        print(f'Missing required keys for entry {entry}: {missing}')
    slug = entry['slug']
    unknown_keys = keys - ENTRY_KEYS
    if unknown_keys:
        print(f'Unknown keys in {slug}: {unknown_keys}')
    result = {}
    crossrefs = set(entry['ref']) if ('ref' in entry) else set()
    for lang in ENTRY_LANGUAGE_KEYS:
        if lang in entry:
            label = f'{slug}/{lang}'
            result[lang] = checkLanguageDef(label, crossrefs, entry[lang])
    return result


def checkLanguageDef(label, crossrefs, definition):
    '''
    Check language-specific material in definition, returning slugs
    of terms referenced in the body of the definition.
    '''
    keys = set(definition.keys())
    missing = [k for k in DEFINITION_REQUIRED_KEYS if k not in keys]
    if missing:
        print(f'Missing required keys for definition {label}: {missing}')
    unknown_keys = keys - DEFINITION_KEYS
    if unknown_keys:
        print(f'Unknown keys in {label}: {unknown_keys}')
    inBody = set(LINK_PAT.findall(definition['def']))
    duplicate = crossrefs & inBody
    if duplicate:
        duplicate = ', '.join(sorted(duplicate))
        print(f'Terms in both body and cross-references for {label}: {duplicate}')
    return inBody


def checkSlugs(gloss):
    '''Check that entries have unique slugs and are ordered by slug.'''
    slugs = [entry['slug'] for entry in gloss if 'slug' in entry]
    for (i, slug) in enumerate(slugs):
        if (i > 0) and (slug < slugs[i-1]):
            print(f'slug {slug} out of order')
    counts = Counter(slugs)
    dups = [s for s in counts.keys() if counts[s] > 1]
    if dups:
        print(f'duplicate keys: {dups}')


def checkDuplicates(gloss):
    '''Check for duplicate definitions in each language.'''
    for lang in ENTRY_LANGUAGE_KEYS:
        terms = [entry[lang]['term'] for entry in gloss
                 if ((lang in entry) and 'term' in entry[lang])]
        counts = Counter(terms)
        dups = [s for s in counts.keys() if counts[s] > 1]
        if dups:
            print(f'duplicate definitions for {lang}: {dups}')


def checkCrossRef(gloss):
    '''Check that all explicit cross-references resolve.'''
    known = {entry['slug'] for entry in gloss}
    missing = {}
    for entry in gloss:
        if 'ref' in entry:
            if not entry['ref']:
                print(f'{entry["slug"]} has empty "ref" key')
            else:
                unknown = [slug for slug in entry['ref'] if slug not in known]
                if unknown:
                    print(f'{entry["slug"]} has unknown crossref(s) {", ".join(unknown)}')


def checkMissingDefs(lang, gloss):
    '''Check for missing definitions in the given language.'''
    missing = []
    for entry in gloss:
        if lang not in entry:
            print(f'{lang}: {entry["slug"]}')


def buildForward(gloss):
    '''Build graph of forward references.'''
    result = {}
    for entry in gloss:
        record = set(LINK_PAT.findall(entry['en']['def']))
        result[entry['slug']] = record
    return result


def buildBackward(forward):
    '''Build graph of backward references, checking for missing terms.'''
    result = {}
    for source in forward:
        result[source] = set()
    failed = set()
    for source in forward:
        for dest in forward[source]:
            if dest in result:
                result[dest].add(source)
            else:
                failed.add(dest)
    if failed:
        failed = '\n  '.join(sorted(failed))
        print('Missing terms:\n ', failed, file=sys.stderr)
        sys.exit(1)
    return result


if __name__ == '__main__':
    main()
