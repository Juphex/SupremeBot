#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# =============================================================================
# Written by Rentouch 2014 - http://www.rentouch.ch
# =============================================================================

from setuptools import setup

with open('requirements.txt') as fd:
    reqs = [l.strip() for l in fd.readlines() if not l.startswith('#') and l.strip()]

# -----------------------------------------------------------------------------
exec(open('cefbrowser/version.py').read())  # Will store __version__

# setup
setup(
    name='cefbrowser',
    version=__version__,  # noqa: F820
    author='Rentouch GmbH',
    author_email='info@rentouch.ch',
    url='http://www.rentouch.ch',

    package_data={
        'cefbrowser': ['images/*.png', '*.kv'],
        'cefbrowser.lib': ['*.json'],
    },

    packages=['cefbrowser'],

    install_requires=reqs,
)

# -----------------------------------------------------------------------------
