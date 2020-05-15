'''Look up terms in a glossary.'''

import os
import yaml


with open(os.path.join(os.path.dirname(__file__), 'glossary.yml'), 'r') as reader:
    raw = yaml.load(reader, Loader=yaml.FullLoader)
    Terms = {term['slug']: term for term in raw}
    

def define(slug):
    '''Look up a definition in a glossary by slug.'''
    return Terms.get(slug, f'Unknown slug {slug}')


def known():
    '''Report all known definition slugs as a set.'''
    return set(Terms.keys())
