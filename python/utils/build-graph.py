#!/usr/bin/env python

'''Generate YAML with all cross-references filled in, failing if there are undefined terms.'''

import sys
import re
import yaml


# Match internal Markdown links.
LINK_PAT = re.compile(r'\[.+?\]\(#(.+?)\)')


def main():
    '''Main driver.'''
    with open(sys.argv[1], 'r') as reader:
        data = yaml.load(reader, Loader=yaml.FullLoader)
    forward = buildForward(data)
    backward = buildBackward(forward)
    complete(data, forward, backward)
    print(yaml.dump(data, Dumper=yaml.Dumper))


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


def complete(data, forward, backward):
    '''Fill in all references.'''
    for entry in data:
        entry['ref'] = sorted(forward[entry['slug']])
        entry['usedby'] = sorted(backward[entry['slug']])
        entry['en']['def'] = entry['en']['def'].rstrip()


if __name__ == '__main__':
    main()
