#!/usr/bin/env python

import sys
assert sys.version >= '2.5', "Requires Python v2.5 or above."
from setuptools import setup

classifiers = [
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="numeronym",
    version="1.0.4",
    author="Barry Melton",
    author_email="barry.melton@gmail.com.com",
    url="https://github.com/bmelton/numeronym/",
    description="A simple library for generating numeronyms",
    long_description="A simple library for generates numeronyms.",
    license="BSD",
    classifiers=classifiers,
    packages=["numeronym"],
)
