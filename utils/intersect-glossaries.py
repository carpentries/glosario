#!/usr/bin/env python

'''Find duplicate entries in two or more glossary files.'''

import sys
import getopt
import yaml


USAGE = 'intersect glossary [glossary...]'


def main():
    '''Main driver.'''
    filenames = parseArgs()
    seen = findSlugs(filenames)
    showDuplicates(seen)


def parseArgs():
    '''Parse command-line arguments, reading keep list if provided.'''

    options, filenames = getopt.getopt(sys.argv[1:], 'h')
    for (opt, arg) in options:
        if opt == '-h':
            print(USAGE)
            sys.exit(0)
        else:
            print(USAGE, sys.stderr)
            sys.exit(1)

    if not filenames:
        print(USAGE, sys.stderr)
        sys.exit(1)

    return filenames


def findSlugs(filenames):
    '''Build table of files containing slugs.'''
    seen = {}
    for f in filenames:
        with open(f, 'r') as reader:
            for entry in yaml.load(reader, Loader=yaml.FullLoader):
                slug = entry['slug']
                if slug not in seen:
                    seen[slug] = set()
                seen[slug].add(f)
    return seen


def showDuplicates(seen):
    '''Show entries that appear more than once.'''
    for slug in sorted(seen.keys()):
        if len(seen[slug]) > 1:
            print(f'{slug}: {", ".join(sorted(seen[slug]))}')


if __name__ == '__main__':
    main()
