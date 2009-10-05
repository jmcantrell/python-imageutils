#!/usr/bin/env python

from setuptools import setup, find_packages
from glob import glob

setup(
        name='ImageUtils',
        version='0.2.3',
        description='Various small utilities for working with images.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Programming Language :: Python',
            ],
        packages=[
            'imageutils',
            ],
        )
