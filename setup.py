#!/usr/bin/env python

from setuptools import setup

setup(
        name='ImageUtils',
        version='0.3.7',
        description='Various utilities for working with images.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Programming Language :: Python',
            ],
        packages=[
            'imageutils',
            ],
        install_requires=[
            'PIL',
            ],
        )
