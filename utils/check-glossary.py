#!/usr/bin/env python

'''
Check YAML file. Each _entry_ contains one or more _definitions_.
'''

import sys
import re
import yaml
from collections import Counter

# Keys for entries and definitions.
ENTRY_REQUIRED_KEYS = {'slug'}
ENTRY_OPTIONAL_KEYS = {'ref'}
ENTRY_LANGUAGE_KEYS = {'en', 'es', 'fr'}
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
    with open(sys.argv[1], 'r') as reader:
        data = yaml.load(reader, Loader=yaml.FullLoader)
    for entry in data:
        checkEntry(entry)
    checkSlugs(data)
    checkDuplicates(data)
    forward = buildForward(data)
    backward = buildBackward(forward)


def checkEntry(entry):
    '''Check structure of individual entries.'''
    keys = set(entry.keys())
    missing = [k for k in ENTRY_REQUIRED_KEYS if k not in keys]
    if missing:
        print(f'Missing required keys for entry {entry}: {missing}')
    slug = entry['slug']
    unknown_keys = keys - ENTRY_KEYS
    if unknown_keys:
        print(f'Unknown keys in {slug}: {unknown_keys}')
    for lang in ENTRY_LANGUAGE_KEYS:
        if lang in entry:
            checkLanguage(slug, lang, entry[lang])


def checkLanguage(slug, lang, definition):
    '''Check language-specific material in definition.'''
    keys = set(definition.keys())
    missing = [k for k in DEFINITION_REQUIRED_KEYS if k not in keys]
    if missing:
        print(f'Missing required keys for definition {slug}/{lang}: {missing}')
    unknown_keys = keys - DEFINITION_KEYS
    if unknown_keys:
        print(f'Unknown keys in {slug}/{lang}: {unknown_keys}')


def checkSlugs(data):
    '''Check that entries have unique slugs and are ordered by slug.'''
    slugs = [entry['slug'] for entry in data if 'slug' in entry]
    for (i, slug) in enumerate(slugs):
        if (i > 0) and (slug < slugs[i-1]):
            print(f'slug {slug} out of order')
    counts = Counter(slugs)
    dups = [s for s in counts.keys() if counts[s] > 1]
    if dups:
        print(f'duplicate keys: {dups}')


def checkDuplicates(data):
    '''Check for duplicate definitions in each language.'''
    for lang in ENTRY_LANGUAGE_KEYS:
        terms = [entry[lang]['term'] for entry in data
                 if ((lang in entry) and 'term' in entry[lang])]
        counts = Counter(terms)
        dups = [s for s in counts.keys() if counts[s] > 1]
        if dups:
            print(f'duplicate definitions for {lang}: {dups}')


def buildForward(data):
    '''Build graph of forward references.'''
    result = {}
    for entry in data:
        record = set()
        if 'see' in entry:
            record.update(entry['see'])
        for link in LINK_PAT.findall(entry['en']['def']):
            record.add(link)
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
