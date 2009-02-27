#!/usr/bin/env python

from setuptools import setup, find_packages
from glob import glob

setup(
        name='ImageUtils',
        version='0.1.1',
        description='Various small utilities for working with images.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Programming Language :: Python',
            ],
        packages=[
            'imageutils',
            ],
        )
