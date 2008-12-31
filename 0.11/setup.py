#!/usr/bin/env python

import os.path
from setuptools import setup

setup(
    name = 'TracMarkdownMacro',
    packages = ['Markdown'],
    version = '0.11.1',

    author = 'Douglas Clifton',
    author_email = 'dwclifton@gmail.com',
    description = 'Implements Markdown syntax WikiProcessor as a Trac macro.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 dwclifton processor macro wiki',
    url = 'http://trac-hacks.org/wiki/MarkdownMacro',
    license = 'BSD',

    entry_points = { 'trac.plugins': [ 'Markdown.macro = Markdown.macro' ] },
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
)
