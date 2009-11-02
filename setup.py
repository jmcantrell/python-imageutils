#!/usr/bin/env python

from setuptools import setup

setup(
        name='ImageUtils',
        version='0.3.0',
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
        entry_points={
            'console_scripts': [
                'igrep=igrep:main',
                ]
            },
        packages=[
            'imageutils',
            ],
        py_modules=[
            'igrep',
            ],
        )
